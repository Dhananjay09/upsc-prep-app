#!/usr/bin/env python3
"""
merge_hindi_translations.py
=============================

Run this AFTER translate_subject_hindi.py has finished (fully or partially)
for one or more subjects. It folds every translations/<subject>.json file
back into subject_data.json, adding "q_hi", "o_hi", "e_hi" fields onto each
matching question object — leaving the existing "q", "o", "e" (English)
fields untouched. This is what lets the app show a language toggle: each
question simply has both language variants sitting side by side.

--------------------------------------------------------------------------
USAGE
--------------------------------------------------------------------------
    python3 merge_hindi_translations.py --subject-data subject_data.json --translations-dir translations

By default this OVERWRITES subject_data.json in place (a timestamped
backup is written first, e.g. subject_data.json.bak.1730000000). Pass
--out some_other_file.json if you'd rather not touch the original.

It's safe to run this multiple times as translation progresses — e.g. run
it once after two subjects finish while the other three are still being
translated in their own terminals, then run it again later to pick up the
rest. Already-merged fields are simply overwritten with the latest data.
"""

import argparse
import glob
import json
import os
import sys
import time


def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def merge_subject(subject_data, subject_key, translations):
    subject = subject_data.get(subject_key)
    if subject is None:
        print(f"  Warning: subject key '{subject_key}' not found in subject_data.json — skipping.")
        return 0, 0

    matched = 0
    missing = 0
    for chapter in subject.get("chapters", []):
        chapter_id = chapter["id"]
        questions_field = chapter.get("questions", {})
        if isinstance(questions_field, dict):
            buckets = questions_field.items()
        else:
            buckets = [("_flat", questions_field)]
        for test_key, qlist in buckets:
            for idx, q in enumerate(qlist):
                qid = f"{chapter_id}::{test_key}::{idx}"
                t = translations.get(qid)
                if t is None:
                    missing += 1
                    continue
                q["q_hi"] = t["q_hi"]
                q["o_hi"] = t["o_hi"]
                q["e_hi"] = t["e_hi"]
                matched += 1
    return matched, missing


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--subject-data", default="subject_data.json", help="Path to subject_data.json.")
    p.add_argument("--translations-dir", default="translations",
                   help="Directory containing <subject>.json translation progress files.")
    p.add_argument("--out", default=None,
                   help="Output path (default: overwrite --subject-data in place, with a .bak backup).")
    args = p.parse_args()

    if not os.path.exists(args.subject_data):
        sys.exit(f"Not found: {args.subject_data}")

    subject_data = load_json(args.subject_data)

    translation_files = sorted(glob.glob(os.path.join(args.translations_dir, "*.json")))
    if not translation_files:
        sys.exit(f"No translation files found in {args.translations_dir}/ — "
                  f"run translate_subject_hindi.py first.")

    grand_matched = 0
    grand_missing = 0
    for path in translation_files:
        subject_key = os.path.splitext(os.path.basename(path))[0]
        translations = load_json(path)
        print(f"Merging {path} ({len(translations)} translated questions) into subject '{subject_key}' ...")
        matched, missing = merge_subject(subject_data, subject_key, translations)
        print(f"  Matched: {matched}   Still untranslated: {missing}")
        grand_matched += matched
        grand_missing += missing

    out_path = args.out or args.subject_data
    if out_path == args.subject_data:
        backup_path = f"{args.subject_data}.bak.{int(time.time())}"
        os.replace(args.subject_data, backup_path)
        print(f"\nBacked up original to {backup_path}")

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(subject_data, f, ensure_ascii=False, indent=2)

    print(f"\nWrote {out_path}")
    print(f"Total matched across all subjects: {grand_matched}")
    print(f"Total still untranslated (need another translate_subject_hindi.py run): {grand_missing}")


if __name__ == "__main__":
    main()
