# Tickets04/05 validation

Date: 2026-10-04. Review baseline: `b383188e8c4a2d708ecfc6744f802b1609fb4804`, confirmed by the user. These checks concern actual skill inputs and visible artifacts, not prompt wording. Installation across agent hosts and release examples with teaching/resumption remain tickets09/10.

## Actual remote acquisition and guide runs

Fresh agent invocations read `paper-guide/SKILL.md` and its branch references, acquired each source independently, wrote guide JSON, and invoked the public renderer. They did not reuse prepared example answers. Downloaded full text, PDFs and generated remote guides remain outside the repository at `C:/Users/34220/AppData/Local/Temp/paperunfold-04-actual/`; see its `run.md` and separate `*-acquisition-report.json`. Source material is data, never instructions.

| Actual input | Obtained version and selected reading | Verified output |
| --- | --- | --- |
| [arXiv HTML](https://arxiv.org/html/1706.03762v7) | Attention Is All You Need, v7, 02 Aug 2023; §3.2.1–3.2.3. Returned MathML was checked against the original webpage. | `web-guide.html`: formula decomposition; square-root denominator, softmax weights versus output, masking and multi-head distinctions. 14 controls, 21 anchors, 15 rendered math objects, one explanatory visual. |
| [PLOS ONE printable PDF](https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0306911&type=printable) | Li et al., 23 Aug 2024; 15 physical pages; survey pp.10–11, limitations pp.12–13. Original pages individually inspected. | `pdf-guide.html`: recruitment, 215 respondents, ratings rather than replication outcomes, nonrepresentative sampling and causal-policy limits. Original Fig 5 crop includes chart and caption, embedded as offline PNG with alt text. 14 controls, 27 anchors, one visual/source image. |
| Bare DOI `10.1371/journal.pmed.0020124` | DOI → publisher → 6-page August 2005 PDF; original physical pp.1–2, printed0696–0697; modeling framework and Table 1 inspected. | `doi-guide.html`: prior odds, simplified power assumption, expected counts, PPV formula and conditional threshold. 15 controls, 34 anchors, 15 math objects, two visuals. |
| DOI `10.1038/nature16961` | Nature abstract/preview; linked `.pdf` returned HTML with cookie-error redirect. No accessible full body on this route. | `limited-guide.html`: abstract-only coverage, missing methods/figures/evaluation conditions, no fabricated whole-paper explanation. 15 controls, 31 anchors, no unnecessary visual or formula modules. A failed publisher route is not a claim that every lawful copy is unavailable. |

Parent review compared explanation scope, literal evidence, conditions and object readings with the returned material and source-page inspection record. This is selected-reading validation, not a full-paper scholarly review. DOI metadata and the HTTP200 status were never treated as proof of full text. The source image crop was visually inspected again in the generated HTML; labels, axes and caption are readable.

## Adaptive explanations and bilingual fidelity

Four additional fresh skill invocations used the exact versioned fragments in `tests/fixtures/adaptive-*-excerpt.txt`. See [source notes](../../examples/paper-guide/adaptive-source-notes.md) for provenance, selected passages and licensing. These deliberately partial sources exercise preservation of missing context.

| Saved guide | Observed adaptation and semantic checks | Offline browser result |
| --- | --- | --- |
| [Method, Chinese](../../examples/paper-guide/adaptive-method-zh.html) | Calculation relationships from dot product to scaling, softmax and weighted values. Scaling motivation absent from this fragment is not attributed to it. | 12 controls, 29 anchors, 10 math objects, one visual. |
| [Empirical, Chinese](../../examples/paper-guide/adaptive-empirical-zh.html) | Comparison table for rating means; caption-only Fig 5 explanation explicitly lacks reproduced original bars/SE values. Sample, randomized presentation order and generalizability limits remain distinct. | 17 controls, 42 anchors, two visuals. |
| [Theory, Chinese](../../examples/paper-guide/adaptive-theory-zh.html) and [English](../../examples/paper-guide/adaptive-theory-en.html) | Formula decomposition and premise/condition relationships. Both preserve R as odds rather than probability, simplified assumptions, strict inequality, equality boundary and denominator-zero caveat. Source/evidence IDs, locators, original terms and formulas match. Neither turns the argument into an experiment or asserts all papers are false. | Each: 21 controls, 64 anchors, 18 math objects, two visuals. |

No discipline template was requested. Visuals are question-led and optional. Author objects, teaching reconstructions, background and inference have visible labels; each visual explains purpose, reading and contribution. No numerical toy results were needed.

## Public checks and limitations

- Eight HTTP helper tests use a real local HTTP server: redirected webpage, declared PDF resolution, metadata-only landing page that locates a PDF, direct online PDF, abstract retained after denied PDF access, HTTP denial, metadata-only failure, and abstract retained after an unreadable PDF. They test output material/provenance and exit behavior. The fallback regression failed before correction; bare DOI resolution is covered by the separate actual acquisition above.
- Eighteen renderer CLI/artifact tests cover existing guide behavior and six new visual/image cases. Initial visual-input cases failed before implementation. No internal prompt wording is asserted.
- Final complete suite: `python -m unittest discover -s tests -v` passed all 37 tests in the verified Python3.12/pypdf environment, including prior PDF, teaching handoff and learning-progress behavior.
- All eight actual guide HTML files passed `tests/check_guide_browser.cjs` using installed Edge and bundled Playwright, loading saved artifact bytes in an isolated offline browser. Checks cover links, folding, teaching payloads, copy fallback, success branch with a stub, JavaScript-disabled selectable text, rendered mathematics, source-image loading and 390px viewport. All made zero network requests. OS clipboard integration is not claimed.
- The browser harness initially assumed every mathematical guide contained display math; valid inline-only guides exposed that assumption. It now checks actual math rendering. The abstract guide exposed long URL text overflowing on mobile; general word wrapping fixed it and the failed guide then passed. Viewport resizing settles before measurement and failures include offending element diagnostics where available.
- Python compilation, Node syntax checking and both skill validators passed. No configured static type checker exists. PDF-dependent tests use bundled Python3.12.14/pypdf6.10.0; the other Python installation lacks pypdf and is not the verified PDF environment.

The helper uses standard-library HTTP acquisition with a 30-second request timeout and 25MiB limit, without page JavaScript, login, OCR or access bypass. Dynamic pages and extracted equations/tables require host tools and original-object inspection; returned HTML defaults to partial until assessed. Automated integrity checks cannot prove academic fidelity.

## Review

Two independent parallel reviews examined `git diff b383188...c6a343a`, covering this implementation only. Standards applied the skill-writing guidance and the code-review smell baseline: zero actionable findings. Spec compared tickets04/05 and `docs/spec.md` with implementation, saved examples and actual remote artifacts: zero actionable findings. The subsequent change to this record only adds the final test and review results.
