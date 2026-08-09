"""
extract_book_chapters.py

Splits a large PDF (e.g. Laxmikanth's Indian Polity, ~1100 pages) into one
clean .txt file per chapter, so you can hand it to me a chapter (or a few)
at a time instead of uploading the whole PDF at once.

SETUP (run once):
    pip install pymupdf

USAGE:
    python extract_book_chapters.py "path/to/Laxmikanth.pdf"

OUTPUT:
    A folder named "chapters_extracted" next to the PDF, containing one
    .txt file per chapter, named like "01_Historical_Background.txt",
    plus a summary printed to the screen showing word counts.

HOW IT WORKS:
    1. It first tries to read the PDF's built-in bookmarks / table of
       contents. Most e-book PDFs (including most Laxmikanth editions
       sold as PDFs) have these embedded, so this usually works with
       zero manual effort.
    2. If your PDF has no bookmarks, it tells you so. In that case:
       open the PDF yourself, write down each chapter's title and the
       page number it starts on (the page number your PDF reader shows,
       not the printed page number in the book), fill those into
       MANUAL_CHAPTERS below, set USE_MANUAL = True, and run again.
"""

import sys
import os
import re

try:
    import fitz  # PyMuPDF
except ImportError:
    print("Missing dependency. Run this first:\n    pip install pymupdf")
    sys.exit(1)

# ---------------------------------------------------------------------
# Only edit this section if the script tells you no bookmarks were found.
# ---------------------------------------------------------------------
USE_MANUAL = False
MANUAL_CHAPTERS = [
    # ("Chapter title", start_page_as_shown_in_your_pdf_reader),
    # ("Historical Background", 1),
    # ("Making of the Constitution", 12),
    # ("Salient Features of the Constitution", 25),
]
# ---------------------------------------------------------------------


def clean_text(text):
    """Strip bare page-number lines and collapse excess blank lines."""
    lines = text.split("\n")
    cleaned = [ln for ln in lines if not re.fullmatch(r"\d{1,4}", ln.strip())]
    text = "\n".join(cleaned)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def safe_filename(title, idx):
    slug = re.sub(r"[^a-zA-Z0-9]+", "_", title).strip("_")
    return f"{idx:02d}_{slug[:60]}.txt"


def extract_by_toc(doc):
    toc = doc.get_toc()  # list of [level, title, page], 1-based pages
    if not toc:
        return None
    top = [t for t in toc if t[0] == 1] or toc
    chapters = []
    for i, (level, title, page) in enumerate(top):
        start = page - 1  # PyMuPDF pages are 0-indexed
        end = (top[i + 1][2] - 1) if i + 1 < len(top) else doc.page_count
        chapters.append((title, start, end))
    return chapters


def extract_by_manual(doc, manual_list):
    chapters = []
    for i, (title, start_page) in enumerate(manual_list):
        start = start_page - 1
        end = (manual_list[i + 1][1] - 1) if i + 1 < len(manual_list) else doc.page_count
        chapters.append((title, start, end))
    return chapters


def main():
    if len(sys.argv) < 2:
        print('Usage: python extract_book_chapters.py "path/to/book.pdf"')
        sys.exit(1)

    pdf_path = sys.argv[1]
    doc = fitz.open(pdf_path)
    print(f"Opened {pdf_path}: {doc.page_count} pages")

    if USE_MANUAL and MANUAL_CHAPTERS:
        chapters = extract_by_manual(doc, MANUAL_CHAPTERS)
        print("Using the manually specified chapter list.")
    else:
        chapters = extract_by_toc(doc)
        if chapters:
            print(f"Found {len(chapters)} chapters from the PDF's bookmarks.")
        else:
            print("No bookmarks found in this PDF, and USE_MANUAL is not set.")
            print("Open the PDF, note each chapter's starting page number,")
            print("fill in MANUAL_CHAPTERS near the top of this script, set")
            print("USE_MANUAL = True, and run this script again.")
            sys.exit(1)

    out_dir = os.path.join(os.path.dirname(os.path.abspath(pdf_path)), "chapters_extracted")
    os.makedirs(out_dir, exist_ok=True)

    print()
    for i, (title, start, end) in enumerate(chapters, start=1):
        text_parts = [doc.load_page(p).get_text() for p in range(start, end)]
        full_text = clean_text("\n".join(text_parts))
        word_count = len(full_text.split())
        fname = safe_filename(title, i)
        with open(os.path.join(out_dir, fname), "w", encoding="utf-8") as f:
            f.write(full_text)
        flag = "  <- large, consider splitting further" if word_count > 15000 else ""
        print(f"[{i:02d}] {title!r}: pages {start+1}-{end}, {word_count} words -> {fname}{flag}")

    print(f"\nDone. {len(chapters)} chapter files written to:\n  {out_dir}")
    print("Send me these .txt files a few at a time (not all 1100 pages at once)")
    print("and I'll use them to fact-check and rewrite the app's questions.")


if __name__ == "__main__":
    main()
