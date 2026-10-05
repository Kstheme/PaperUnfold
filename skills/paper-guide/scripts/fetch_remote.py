"""Read an HTTP(S) paper page or DOI into material with transport provenance.

This helper acquires material; an agent assesses coverage and writes the guide.
"""
import argparse
from datetime import datetime, timezone
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
from urllib.parse import quote, urljoin, urlparse
from urllib.request import Request, urlopen

WEB_LIMIT = ("Only the returned HTML text was read. Check paper completeness and version; "
             "images, equations, tables, supplements and dynamically loaded content require inspection.")
MAX_BYTES = 25 * 1024 * 1024


def pdf_material(data, resolved, content_type, output, report):
    from extract_pdf import extract
    pdf_path = output.with_name(output.stem + ".source.pdf")
    pdf_path.write_bytes(data)
    material = extract(pdf_path)
    result = dict(report)
    result.update({k: v for k, v in material.items() if k not in ("input", "version")})
    result["provenance"] = dict(report["provenance"], resolved_url=resolved, content_type=content_type,
                                locator="1-based physical PDF page; inspect cached PDF before explaining visuals",
                                downloaded_pdf=str(pdf_path.resolve()))
    return result


class PageText(HTMLParser):
    """Extract visible blocks and article/main scope without executing page code."""
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.blocks, self.article, self.main = [], [], []
        self.buffer, self.stack, self.title = [], [], []
        self.links = []

    def flush(self):
        value = " ".join("".join(self.buffer).split())
        self.buffer = []
        if value:
            self.blocks.append(value)
            if "article" in self.stack:
                self.article.append(value)
            if "main" in self.stack:
                self.main.append(value)

    def handle_starttag(self, tag, attrs):
        attrs = {key: value or "" for key, value in attrs}
        if tag in ("p", "div", "section", "article", "main", "h1", "h2", "h3", "li", "br"):
            self.flush()
        if tag == "meta" and attrs.get("name", "").lower() == "citation_pdf_url":
            self.links.append(attrs.get("content", ""))
        if tag == "a" and re.search(r"\.pdf(?:[?#]|$)", attrs.get("href", ""), re.I):
            self.links.append(attrs["href"])
        if tag not in ("meta", "link", "br", "img", "hr", "input", "source", "wbr"):
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag in ("p", "div", "section", "article", "main", "h1", "h2", "h3", "li"):
            self.flush()
        if tag in self.stack:
            del self.stack[len(self.stack) - 1 - self.stack[::-1].index(tag):]

    def handle_data(self, data):
        if "title" in self.stack:
            self.title.append(data)
        elif not any(t in self.stack for t in ("script", "style", "nav", "header", "footer", "noscript", "button", "form")):
            self.buffer.append(data)


def read_url(url):
    if urlparse(url).scheme not in ("http", "https"):
        raise ValueError("Provide an HTTP(S) URL or DOI.")
    with urlopen(Request(url, headers={"User-Agent": "PaperUnfold/1.0 (paper reading)",
                                      "Accept": "text/html, application/pdf;q=0.9"}), timeout=30) as response:
        data = response.read(MAX_BYTES + 1)
        if len(data) > MAX_BYTES:
            raise ValueError("Source exceeds 25 MiB. Download a readable copy and use local PDF input.")
        return data, response.geturl(), response.headers.get_content_type(), response.headers.get_content_charset() or "utf-8"


def acquire(value, output, max_pdf_links=3):
    value = value.strip()
    doi = re.sub(r"^doi:\s*", "", value, flags=re.I).strip()
    url = "https://doi.org/" + quote(doi, safe="/") if re.fullmatch(r"10\.\d{4,9}/\S+", doi) else value
    report = {"version": 1, "status": "unreadable", "input": value,
              "provenance": {"requested_url": url, "resolved_url": None,
                             "retrieved_at": datetime.now(timezone.utc).isoformat()},
              "source": {"name": value, "text": "", "coverage": "No readable body material obtained.", "missing": []}}
    try:
        data, resolved, content_type, charset = read_url(url)
        report["provenance"].update(resolved_url=resolved, content_type=content_type)
        page = None
        if not data.startswith(b"%PDF-") and content_type != "application/pdf":
            if content_type not in ("text/html", "application/xhtml+xml", "text/plain"):
                raise ValueError("Unsupported response type: " + content_type)
            if content_type == "text/plain":
                text = data.decode(charset, errors="replace").strip()
            else:
                page = PageText()
                page.feed(data.decode(charset, errors="replace"))
                page.flush()
                text = "\n\n".join(page.article or page.main or page.blocks)
            report["status"] = "partial" if text else "unreadable"
            report["source"] = {"name": "".join(page.title).strip() if page and page.title else resolved,
                                "text": text, "coverage": "Returned webpage/text only; paper coverage requires assessment.",
                                "missing": [WEB_LIMIT]}
            report["provenance"]["locator"] = "Web heading/paragraph and literal excerpt at resolved_url"
            if page:
                report["provenance"]["landing_url"] = resolved
                report["provenance"]["pdf_attempts"] = []
                declared = list(dict.fromkeys(urljoin(resolved, link) for link in page.links if link))
                candidates = declared[:max_pdf_links]
                if declared and max_pdf_links == 0:
                    report["source"]["missing"].append("Linked PDFs were not fetched; only the returned webpage was acquired.")
                for candidate in candidates:
                    attempt = {"url": candidate}
                    report["provenance"]["pdf_attempts"].append(attempt)
                    try:
                        pdf_data, pdf_url, pdf_type, _ = read_url(candidate)
                        if not pdf_data.startswith(b"%PDF-") and pdf_type != "application/pdf":
                            raise ValueError("Link returned a page rather than a PDF")
                        candidate_report = pdf_material(pdf_data, pdf_url, pdf_type, output, report)
                        attempt["status"] = candidate_report["status"]
                        if candidate_report["status"] == "unreadable":
                            attempt["error"] = candidate_report.get("error", "No readable PDF text")
                        else:
                            report = candidate_report
                            break
                    except (OSError, ValueError, LookupError) as exc:
                        attempt.update(status="unavailable", error=str(exc))
                if candidates and not report["provenance"].get("downloaded_pdf"):
                    report["source"]["missing"].append("Linked PDF could not be read; only the returned webpage is available.")
            if not report["source"]["text"]:
                raise ValueError("Returned page contains no readable body text; title/metadata are only locators")
        else:
            report = pdf_material(data, resolved, content_type, output, report)
    except (OSError, ValueError, LookupError) as exc:
        report["error"] = str(exc) + ". Supply readable paper text or an accessible local PDF."
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="HTTP(S) URL, DOI, or doi:10... locator")
    parser.add_argument("--output", required=True, type=Path, help="Material/coverage JSON")
    parser.add_argument("--max-pdf-links", type=int, choices=range(4), default=3,
                        help="Maximum declared PDF links to try (0 keeps HTML; default: 3)")
    args = parser.parse_args()
    try:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        report = acquire(args.input, args.output, args.max_pdf_links)
        args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    except OSError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    if report["status"] == "unreadable":
        print(report.get("error", "No readable material obtained."), file=sys.stderr)
        return 2
    print(f"{report['status']}: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
