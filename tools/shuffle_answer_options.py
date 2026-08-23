#!/usr/bin/env python3
"""
shuffle_answer_options.py
===========================

Fixes a data-quality bug found across subject_data.json: for a large share
of questions, the correct option was always placed at index 0 (i.e. "A"),
making answers guessable without reading the question. Confirmed examples:
  - polity/emergency_provisions: 59/59 questions had a == 0
  - geography: 863/863 questions had a == 0
  - history_upsc: 925/927 questions had a == 0

This script deterministically shuffles the 4 options of every question
(and the matching o_hi translation, if present, to keep languages in sync),
updating "a" to the option's new index, so correct answers land roughly
uniformly across A/B/C/D. The shuffle is seeded per-question (subject +
chapter id + test bucket + index + question text) so re-running this
script is a no-op after the first run (idempotent on already-shuffled data
would just reproduce the same permutation, not re-shuffle further) as long
as inputs haven't changed structurally.

A tiny number of explanations literally reference an option by letter
(e.g. "contradicts option D"); shuffling those would make the explanation
wrong, so any question whose explanation matches that pattern is left
untouched (and reported at the end).

USAGE
    python3 shuffle_answer_options.py --in subject_data.json --out subject_data.json
"""

import argparse
import hashlib
import json
import random
import re
from collections import Counter

LETTER_REF_RE = re.compile(r'\boption\s*\(?[a-dA-D]\)?\b|\bchoice\s*\(?[a-dA-D]\)?\b', re.I)


def stable_seed(*parts):
    s = "|".join(parts)
    return int(hashlib.sha256(s.encode("utf-8")).hexdigest()[:16], 16)


def should_skip(q):
    return bool(LETTER_REF_RE.search(q.get("e", "") or ""))


def shuffle_question(q, seed_key):
    """Mutates q in place. Returns True if shuffled, False if skipped."""
    if should_skip(q):
        return False
    opts = q.get("o")
    if not isinstance(opts, list) or len(opts) != 4:
        return False

    idxs = [0, 1, 2, 3]
    rng = random.Random(stable_seed(seed_key))
    rng.shuffle(idxs)

    old_correct_text = opts[q["a"]]
    new_o = [opts[i] for i in idxs]
    new_a = idxs.index(q["a"])
    assert new_o[new_a] == old_correct_text, "permutation bug — correctness not preserved"

    q["o"] = new_o
    q["a"] = new_a

    if isinstance(q.get("o_hi"), list) and len(q["o_hi"]) == 4:
        q["o_hi"] = [q["o_hi"][i] for i in idxs]

    return True


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--in", dest="in_path", default="subject_data.json")
    p.add_argument("--out", dest="out_path", default="subject_data.json")
    args = p.parse_args()

    with open(args.in_path, encoding="utf-8") as f:
        sd = json.load(f)

    shuffled = 0
    skipped = 0
    skipped_examples = []
    before = Counter()
    after = Counter()

    for subj_key, subj in sd.items():
        if not isinstance(subj, dict) or "chapters" not in subj:
            continue
        for ch in subj["chapters"]:
            qs = ch.get("questions", {})
            buckets = qs.items() if isinstance(qs, dict) else [("_flat", qs)]
            for test_key, qlist in buckets:
                for idx, q in enumerate(qlist):
                    before[q["a"]] += 1
                    seed_key = f"{subj_key}|{ch['id']}|{test_key}|{idx}|{q['q'][:60]}"
                    ok = shuffle_question(q, seed_key)
                    if ok:
                        shuffled += 1
                    else:
                        skipped += 1
                        if len(skipped_examples) < 10:
                            skipped_examples.append(f"{subj_key}/{ch['id']}/{test_key}[{idx}]")
                    after[q["a"]] += 1

    print(f"Shuffled: {shuffled}   Skipped (letter-reference in explanation): {skipped}")
    if skipped_examples:
        print("Skipped questions (left unchanged):")
        for s in skipped_examples:
            print("  -", s)

    print("\nDistribution BEFORE:", dict(before))
    print("Distribution AFTER: ", dict(after))

    with open(args.out_path, "w", encoding="utf-8") as f:
        json.dump(sd, f, ensure_ascii=False, indent=2)
    print(f"\nWrote {args.out_path}")


if __name__ == "__main__":
    main()
