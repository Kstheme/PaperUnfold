# Real-paper reading examples

Generated and reviewed on 2026-10-04 through the actual `paper-guide` and `paper-tutor` entrypoints in native Codex agents. Open the HTML files locally; they include their own resources and work offline. The guides orient readers across the main paper, while detailed object checks and missing supplements are explicitly scoped. These examples do not establish quality across all disciplines or measure learning gains.

| Paper and original source | Guide | Actual screenshot |
| --- | --- | --- |
| Vaswani et al., *Attention Is All You Need*, [arXiv HTML v7](https://arxiv.org/html/1706.03762v7), 02 Aug 2023 | [Chinese](algorithm-zh.html) · [renderer input](algorithm-zh.json) | [Chinese viewport](screenshots/algorithm-zh.png) |
| Li et al. (2024), *Challenging the N-Heuristic: Effect size, not sample size, predicts the replicability of psychological science*, [publisher](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0306911) | [English](empirical-en.html) · [renderer input](empirical-en.json) | [English viewport](screenshots/empirical-en.png) |
| Ioannidis (2005), *Why Most Published Research Findings Are False*, [publisher](https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.0020124) | [Chinese](theory-zh.html) · [English](theory-en.html) · [Chinese input](theory-zh.json) · [English input](theory-en.json) | [Chinese viewport](screenshots/theory-zh.png) · [English viewport](screenshots/theory-en.png) |

The screenshots are captures of the actual saved pages, not design mockups. Source identities, acquired versions, languages, object inspection and generation conditions are in [generation-provenance.json](generation-provenance.json). [Independent source review](source-audit.md) checks claims, numbers, qualifiers and source positions. Guide validation is distinct from a complete technical reproduction or peer review.

The algorithm guide preserves the source's EN-FR score discrepancy. The empirical guide retains the significant joint-model N result and the Bayesian sensitivity caveat. The theory guides identify the original2005 edition and narrowly describe the publisher's [2022 Table2 correction](https://doi.org/10.1371/journal.pmed.1004085). Neither the essay's illustrative model nor respondents' ratings become measured universal truth rates.

## Teaching, exit and a new conversation

1. The evaluator actually copied the English empirical guide's Results prompt using keyboard copy/paste in an isolated offline Edge page. [Session input snapshot](session-input-prompts.json) preserves the payload used by the tutor. This snapshot predates the guide review's locator/identifier cleanup; it is historical input, not the current guide. [Current copied prompts](copied-prompts.json) were recaptured from the corrected final HTML and checked separately.
2. [Actual teaching dialogue](teaching-session.md) shows an incomplete/mixed answer, “I do not know,” a direct-explanation request, and immediate exit. Researcher replies were scripted evaluator inputs. The tutor responses and file operations actually occurred; no actual person's learning was measured.
3. [Paused progress](paused-progress.json) credits only the demonstrated across-study versus within-study distinction. Causal reasoning remains partial and the model explanation remains unverified. The source path is portable and points to [readable original material](empirical-source.txt).
4. A separate fresh agent read only that progress and original material. [Resumed dialogue](resumed-session.md) starts at the retained question and gap. [Resumed progress](resumed-progress.json) preserves every understanding status and answer; resuming and stopping earned no additional mastery credit.

[Same-source display comparison](conventional-comparison.md) pairs conventional prose with an expandable guide explanation using the same joint-model passage and generation context. It demonstrates differences in presentation, not measured speed or comprehension improvements.

## Source reuse and limits

The PLOS papers carry Creative Commons Attribution statements. [Empirical source](empirical-source.txt) is attributed to Li et al. (2024), DOI10.1371/journal.pone.0306911; [theory source](theory-source.txt) is attributed to John P. A. Ioannidis (2005), DOI10.1371/journal.pmed.0020124. The saved text has extraction/page markers and does not replace original visual objects. Separate supporting files and OSF data were not inspected or reanalyzed. The original theory PDF was not silently updated to a corrected edition.

No full Attention paper is redistributed. [Retained algorithm anchors](algorithm-source-extracts.txt) are a compact evidence appendix, not the full material read; consult the primary version for context. Appendix attention plots were not individually visually checked. Explanations and teaching reconstructions are distinguishable from source objects.

Verified artifact environment: Windows, Python3.12.14/pypdf6.10.0 for PDF reading, standard-library renderer, bundled Poppler for source inspection, installed Edge and bundled Playwright for offline artifact QA. Broader agent installation and platform support remain ticket10. Saved JSON can be rerendered with the repository's `render_guide.py`; authoring caches under the recorded temporary paths are diagnostic provenance rather than portable runtime dependencies.
