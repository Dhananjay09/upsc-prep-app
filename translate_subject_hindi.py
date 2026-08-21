#!/usr/bin/env python3
"""
translate_subject_hindi.py
===========================

Translates every question in ONE subject of subject_data.json into Hindi,
using the Anthropic API, and writes the results to a per-subject progress
file (translations/<subject>.json) rather than touching subject_data.json
directly. This lets you run one instance of this script per subject, in
parallel, in separate terminals, with zero risk of two processes stomping
on each other's writes.

Once all subjects you care about are translated, run merge_hindi_translations.py
once to fold everything back into subject_data.json (adding "q_hi", "o_hi",
"e_hi" fields alongside the existing "q", "o", "e" fields on every question).

--------------------------------------------------------------------------
SETUP (one-time)
--------------------------------------------------------------------------
1. pip install anthropic --break-system-packages   # or in a venv
2. export ANTHROPIC_API_KEY="sk-ant-..."

--------------------------------------------------------------------------
USAGE (run one of these per terminal, in parallel — one subject each)
--------------------------------------------------------------------------
    python3 translate_subject_hindi.py --subject polity
    python3 translate_subject_hindi.py --subject economy
    python3 translate_subject_hindi.py --subject history
    python3 translate_subject_hindi.py --subject geography
    python3 translate_subject_hindi.py --subject history_upsc

All five can be launched at once from the repo root:

    for s in polity economy history geography history_upsc; do
        python3 translate_subject_hindi.py --subject "$s" > "logs_$s.txt" 2>&1 &
    done
    wait

--------------------------------------------------------------------------
RESUMABILITY
--------------------------------------------------------------------------
Progress is saved to translations/<subject>.json after every batch. If the
script is interrupted (Ctrl-C, crash, rate limit, laptop sleeps, etc.) just
re-run the exact same command — already-translated questions are skipped
automatically, so you only pay for/wait on what's left.

--------------------------------------------------------------------------
COST / TIME NOTE
--------------------------------------------------------------------------
Each batch translates ~15 questions in a single API call. A subject with
~1500-2500 questions therefore needs roughly 100-170 API calls. Expect this
to take somewhere between 30 minutes and a couple of hours per subject
depending on your rate limits and network — run several subjects in
parallel (as above) since they're fully independent.
"""

import argparse
import json
import os
import sys
import time

try:
    import anthropic
except ImportError:
    sys.exit("Missing dependency 'anthropic'. Install with: pip install anthropic --break-system-packages")


SYSTEM_PROMPT = """You are translating UPSC (Union Public Service Commission) exam-prep \
multiple-choice questions from English into Hindi, for Hindi-medium aspirants.

You will be given a JSON array of question objects, each with an "id", "q" (question text), \
"o" (array of exactly 4 options), and "e" (explanation). Translate each into natural, exam-register \
Hindi (Devanagari script) suitable for a serious UPSC aspirant.

STRICT RULES:
1. Preserve meaning exactly. Do not add, remove, or alter any fact, date, name, or number.
2. Keep proper nouns (person names, place names, Acts, organisations, book titles) in Devanagari \
   transliteration. On first natural occurrence within a single question's text, you may add the \
   original English term in brackets if it aids clarity for an aspirant used to English-medium sources \
   (e.g. "गवर्नर-जनरल (Governor-General)"), but do not do this for every single word — use judgement, \
   sparingly.
3. Keep numbers, dates, and numerals as Arabic numerals (not spelled out, not Devanagari numerals).
4. If the question text uses "\\n" to separate lines (e.g. numbered statements, assertion/reason, \
   match-list rows), preserve that same line structure with "\\n" in the Hindi translation.
5. Preserve option structure exactly: exactly 4 Hindi options, in the SAME order as the English ones, \
   so option index 0 in Hindi corresponds to option index 0 in English, etc. Common option phrases like \
   "1 and 2 only", "Both A and R are true...", "None of the above" must be translated to their standard \
   Hindi UPSC equivalents (e.g. "केवल 1 और 2", "A और R दोनों सत्य हैं...", "उपरोक्त में से कोई नहीं").
6. Preserve any HTML tags (like <b>...</b>) found in the explanation text, keeping them wrapped around \
   the corresponding translated Hindi phrase.
7. Output ONLY a JSON array (no markdown fences, no commentary) of objects with exactly these keys:
   "id": the same id string you were given (copy exactly, do not alter),
   "q_hi": Hindi translation of "q",
   "o_hi": array of exactly 4 Hindi strings, translating "o" in the same order,
   "e_hi": Hindi translation of "e".
Return translations for EVERY question you were given, in any order, matched by "id".
"""


def load_subject_data(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def flatten_questions(subject_data, subject_key):
    """Yield (id, q, o, e) for every question in a subject, walking all
    chapters and all test buckets (test1, test2, ..., upsc1, upsc2, ...)."""
    subject = subject_data.get(subject_key)
    if subject is None:
        sys.exit(f"Subject key '{subject_key}' not found in subject_data.json. "
                  f"Available keys: {list(subject_data.keys())}")
    for chapter in subject.get("chapters", []):
        chapter_id = chapter["id"]
        questions_field = chapter.get("questions", {})
        if isinstance(questions_field, dict):
            buckets = questions_field.items()
        else:
            # Defensive: a flat list rather than a dict of test buckets.
            buckets = [("_flat", questions_field)]
        for test_key, qlist in buckets:
            for idx, q in enumerate(qlist):
                qid = f"{chapter_id}::{test_key}::{idx}"
                yield qid, q


def load_progress(progress_path):
    if os.path.exists(progress_path):
        with open(progress_path, encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_progress(progress_path, progress):
    os.makedirs(os.path.dirname(progress_path) or ".", exist_ok=True)
    tmp_path = progress_path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)
    os.replace(tmp_path, progress_path)  # atomic on POSIX — safe even if interrupted


def _parse_json_array(raw):
    raw = raw.strip()
    if raw.startswith("```"):
        raw = raw.split("```", 2)[1]
        if raw.startswith("json"):
            raw = raw[4:]
        raw = raw.strip()
    return json.loads(raw)


def _is_valid_translation(t):
    if not isinstance(t, dict):
        return False
    if not isinstance(t.get("id"), str):
        return False
    if not isinstance(t.get("q_hi"), str) or not t["q_hi"].strip():
        return False
    if not isinstance(t.get("o_hi"), list) or len(t["o_hi"]) != 4:
        return False
    if not all(isinstance(o, str) and o.strip() for o in t["o_hi"]):
        return False
    if not isinstance(t.get("e_hi"), str) or not t["e_hi"].strip():
        return False
    return True


def translate_batch(client, model, batch, max_retries=4):
    """batch: list of (qid, q_dict). Returns dict {qid: {"q_hi":..,"o_hi":..,"e_hi":..}}."""
    payload = [
        {"id": qid, "q": q["q"], "o": q["o"], "e": q.get("e", "")}
        for qid, q in batch
    ]
    user_prompt = (
        "Translate the following questions into Hindi per the system prompt rules. "
        "Return ONLY the JSON array.\n\n" + json.dumps(payload, ensure_ascii=False)
    )

    delay = 5
    for attempt in range(1, max_retries + 1):
        try:
            response = client.messages.create(
                model=model,
                max_tokens=8000,
                temperature=0.2,
                system=SYSTEM_PROMPT,
                messages=[{"role": "user", "content": user_prompt}],
            )
            raw_text = "".join(b.text for b in response.content if b.type == "text")
            parsed = _parse_json_array(raw_text)
            if not isinstance(parsed, list):
                raise ValueError("Model did not return a JSON array.")
            result = {}
            for t in parsed:
                if _is_valid_translation(t):
                    result[t["id"]] = {"q_hi": t["q_hi"], "o_hi": t["o_hi"], "e_hi": t["e_hi"]}
            return result
        except Exception as e:  # noqa: BLE001 — deliberately broad; this is a retry loop
            print(f"    Attempt {attempt}/{max_retries} failed: {e}")
            if attempt == max_retries:
                return {}
            time.sleep(delay)
            delay *= 2
    return {}


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--subject", required=True,
                   help="Subject key in subject_data.json, e.g. polity, economy, history, geography, history_upsc.")
    p.add_argument("--subject-data", default="subject_data.json", help="Path to subject_data.json.")
    p.add_argument("--out-dir", default="translations", help="Directory to write/read the progress file.")
    p.add_argument("--model", default="claude-sonnet-5", help="Anthropic model to use.")
    p.add_argument("--batch-size", type=int, default=15, help="Questions translated per API call.")
    p.add_argument("--sleep-between-batches", type=float, default=1.0,
                   help="Seconds to sleep between batches (be polite to rate limits).")
    args = p.parse_args()

    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("Set ANTHROPIC_API_KEY in your environment first.")

    subject_data = load_subject_data(args.subject_data)
    all_questions = list(flatten_questions(subject_data, args.subject))
    print(f"Subject '{args.subject}': {len(all_questions)} total questions found.")

    progress_path = os.path.join(args.out_dir, f"{args.subject}.json")
    progress = load_progress(progress_path)
    print(f"Already translated: {len(progress)} questions (resuming from {progress_path}).")

    pending = [(qid, q) for qid, q in all_questions if qid not in progress]
    print(f"Remaining to translate: {len(pending)} questions.")

    if not pending:
        print("Nothing to do — all questions already translated.")
        return

    client = anthropic.Anthropic()
    total_batches = (len(pending) + args.batch_size - 1) // args.batch_size

    for batch_num in range(total_batches):
        start = batch_num * args.batch_size
        batch = pending[start:start + args.batch_size]
        print(f"[{args.subject}] Batch {batch_num + 1}/{total_batches} "
              f"({len(batch)} questions, {len(progress)} done so far)...")

        result = translate_batch(client, args.model, batch)
        progress.update(result)
        save_progress(progress_path, progress)

        missing = [qid for qid, _ in batch if qid not in result]
        if missing:
            print(f"    Warning: {len(missing)} question(s) in this batch failed translation "
                  f"and will be retried on next run: {missing[:3]}{'...' if len(missing) > 3 else ''}")

        time.sleep(args.sleep_between_batches)

    print(f"\n[{args.subject}] Done. {len(progress)}/{len(all_questions)} questions translated.")
    if len(progress) < len(all_questions):
        print("Some questions are still missing (failed batches). Just re-run the same command to retry them.")


if __name__ == "__main__":
    main()
