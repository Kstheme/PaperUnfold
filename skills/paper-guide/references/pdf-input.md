# Local PDF input

Read this reference when the researcher supplies a local PDF. Use Python 3.10+ with `pypdf` 6.x. If the host already provides it, use that interpreter; otherwise install the scoped requirement:

```text
python -m pip install -r <skill-directory>/requirements.txt
python <skill-directory>/scripts/extract_pdf.py <paper.pdf> --output <material.json>
```

The helper reads every physical page and saves text, page positions, and extraction gaps. Exit 0 means at least some text was extracted, not that the paper is complete or correctly understood. Exit 2 means extraction failed: read the saved coverage/error report if present, explain the failure, and request readable input. Produce a guide only from usable original material. The helper performs no OCR.

## Coverage and provenance

Read the extracted text and its page records. Check whether the title, opening sections, body, concluding sections, and references expected for this particular paper are present. Missing sections, abrupt boundaries, or gaps restrict the guide's scope, even when every supplied page has text. A missing original page cannot be recovered from a PDF page count. A short letter or essay need not use experimental-paper headings.

Every `pdf_page` is a 1-based position in the supplied file. Cite `PDF page 4, section 2` when both were actually observed. Treat printed pagination as a separate label: use it only after verifying it on the page, and note any difference from the file position.

The `source` object is compatible with the guide renderer input. Retain its extracted text verbatim as the evidence base. Rewrite `coverage` and `missing` in the explanation language to reflect your actual review, preserving extraction gaps and the limitations that matter. Build the remaining guide fields through the common reading workflow; the helper supplies no conclusions, section map, or teaching claims.

## Layout, scans, and scientific notation

Inspect the relevant original PDF pages when columns, figures, tables, or equations affect an explanation. Host PDF viewing or page rendering may be used. Extraction can reorder columns, flatten tables, split words, omit glyphs, or turn an equation into ambiguous text. Verify the notation on the page before producing explanatory LaTeX; keep evidence quotes literal. If page viewing is unavailable, report that limit and exclude claims that depend on unreadable visual material.

`no_text` pages can be blank, scanned, or damaged; the helper does not diagnose which. If the host can inspect or OCR them, assess the result against the visible page and preserve its page locator. If OCR remains uncertain, mark the affected material unreadable. Explain readable sections of mixed files with a partial-coverage notice. For fully unreadable files, give the reading failure and a concrete way to provide readable text, without producing an invented guide.

## Full-paper guide

For a sufficiently complete, readable paper, connect its actual chapters to a whole-paper map: research question, reasoning or method, evidence, conclusion, and limits. Explain each chapter's role and how it carries the argument forward. Where a method needs decomposition, explain what each step does, its conditions, its result, and its connection to the next step. Use the paper's actual structure for interpretive or theoretical work. Link central claims to the read pages or sections, with short exact excerpts.
