# Remote acquisition checks (ticket 04)

Executed on 2026-10-04. These are transport/material checks, not claims that a
complete guide or its scientific interpretation has passed review. The separate
ticket validation record covers actual Agent-to-HTML runs and source inspection.

## Public CLI tests

```sh
python -m unittest discover -s tests -p test_remote_input.py -v
```

Eight tests passed using an actual local HTTP server and saved material JSON:
redirected webpage body/provenance, publisher PDF-link acquisition, title metadata
as locator, direct PDF physical-page positions, abstract retained after denied
PDF access, actionable HTTP denial with no invented guide, metadata-only failure,
and usable abstract retained after an unreadable linked PDF.

The redirect, linked PDF, metadata-only locator and unreadable-PDF fallback
cases were observed failing before their corresponding implementation changes.
Other negative cases verify the already-added shared failure behavior.
The fixtures are explicitly synthetic research text, not published evidence.

## Live sources

The same public CLI was run with these actual inputs:

| Input | Observed result |
| --- | --- |
| `10.1371/journal.pmed.0020124` | DOI resolver led to PLOS Medicine article HTML; its declared PDF link supplied body text from 6/6 physical PDF pages. |
| `https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.0020124` | Publisher webpage led to the same declared printable PDF, with landing and final URLs recorded separately. |
| `https://journals.plos.org/plosmedicine/article/file?id=10.1371/journal.pmed.0020124&type=printable` | Direct PDF response, 6/6 text-layer pages; cached PDF retained for source inspection. |
| `https://www.nature.com/articles/nature16961` | Publisher preview returned abstract text; linked `.pdf` route returned HTML rather than a PDF. Material stayed `partial`, with the failed route recorded. No global claim about all possible lawful full-text versions. |

Live material was written outside the repository to
`C:/Users/34220/AppData/Local/Temp/paperunfold-04/`:
`doi-material.json`, `web-material.json`, `online-pdf-material.json`, and
`limited-material.json`. Successful PDF inputs also wrote adjacent `.source.pdf`
files. These temporary artifacts are diagnostic caches and are not required to
run the deterministic tests. Publisher availability can change.

No login, CAPTCHA or access-control bypass was attempted. PDF text-layer
coverage is not proof of complete scientific content; equations, tables and
figures require the existing PDF inspection workflow.
