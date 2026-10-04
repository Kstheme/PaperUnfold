"""Extract local PDF text with physical-page provenance and explicit coverage limits.

This prepares material for an agent, not a reading guide or an OCR service.
"""
import argparse
import json
from pathlib import Path
import sys


EXTRACTION_LIMIT = (
    "Text extraction does not verify figures, tables, equations, reading order, "
    "or original printed page labels. Inspect relevant PDF pages before explaining them."
)


def extract(path):
    try:
        import pypdf
    except ImportError as exc:
        raise ValueError("PDF extraction needs pypdf. Install with: python -m pip install "
                         "-r <skill-directory>/requirements.txt") from exc
    result = {"version": 1, "status": "unreadable", "input": str(path.resolve()),
              "extractor": "pypdf " + pypdf.__version__, "page_count": 0,
              "readable_pages": [], "pages": [],
              "source": {"name": path.name, "text": "", "coverage":
                         "No PDF body text was read.", "missing": [EXTRACTION_LIMIT]}}
    try:
        reader = pypdf.PdfReader(path)
        if reader.is_encrypted and not reader.decrypt(""):
            result["error"] = "PDF requires a password. Provide an unlocked copy you can read."
            return result
        result["page_count"] = len(reader.pages)
        title = reader.metadata.title if reader.metadata else None
        if isinstance(title, str) and title.strip():
            result["source"]["name"] = title.strip() + " (" + path.name + ")"
        for number, page in enumerate(reader.pages, 1):
            try:
                text = (page.extract_text() or "").strip()
                entry = {"pdf_page": number, "status": "text" if text else "no_text", "text": text}
            except Exception as exc:
                entry = {"pdf_page": number, "status": "error", "text": "",
                         "error": str(exc)}
            result["pages"].append(entry)
            if entry["text"]:
                result["readable_pages"].append(number)
            else:
                result["source"]["missing"].append(
                    f"PDF page {number}: no usable text extracted. It may be blank, scanned, "
                    "or damaged. Inspect the page; OCR or a readable replacement may be needed.")
    except Exception as exc:
        result["error"] = "Could not open/read the PDF: " + str(exc)
        return result

    count, total = len(result["readable_pages"]), result["page_count"]
    result["source"]["text"] = "\n\n".join(
        f"[PDF page {p['pdf_page']} of {total}]\n{p['text']}"
        for p in result["pages"] if p["text"])
    result["source"]["coverage"] = (
        f"Text extracted from {count} of {total} physical PDF pages. Locators are 1-based "
        "PDF page positions, not verified original printed page numbers. Full text-layer "
        "coverage alone does not establish that the paper is complete.")
    if not count:
        result["error"] = "No usable body text extracted. Supply a text-layer PDF, OCR text with page labels, or a pasted passage."
    else:
        result["status"] = "readable" if count == total else "partial"
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Local PDF path")
    parser.add_argument("--output", required=True, type=Path, help="Extracted material/coverage JSON")
    args = parser.parse_args()
    if args.input.resolve() == args.output.resolve():
        parser.error("Input and output must be different paths.")
    try:
        result = extract(args.input)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    except (OSError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 2
    if result["status"] == "unreadable":
        print(result["error"], file=sys.stderr)
        return 2
    print(f"{result['status']}: {len(result['readable_pages'])}/{result['page_count']} pages; {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
