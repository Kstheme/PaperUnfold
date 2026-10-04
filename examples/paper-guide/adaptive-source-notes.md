# Adaptive source fixtures and observed acquisition

Verified on 2026-10-04. These are real scholarly-paper fragments, not full-paper fixtures. Exact source words are separated from fixture-author coverage notes. No full third-party PDF is committed. Positive acquisition was read without account login or CAPTCHA; access may change.

## Executable method

- Fixture: `tests/fixtures/adaptive-method-excerpt.txt`, copied from the existing `attention-excerpt.txt`.
- Vaswani et al., *Attention Is All You Need*: [arXiv HTML v7](https://arxiv.org/html/1706.03762v7), [PDF](https://arxiv.org/pdf/1706.03762), [arXiv DOI](https://doi.org/10.48550/arXiv.1706.03762).
- Coverage: Section 3.2 short statement, Section 3.2.1 Equation (1), short scaling statement. The existing fixture deliberately does not include the scaling argument’s surrounding context. No additional licensed-copy assertion is made here; the stored prose is two short quotations plus mathematical notation.
- This supports weighted aggregation and equation decomposition. It cannot support full architecture, training claims, BLEU scores, or an attributed derivation of the scaling motivation without acquiring more source.

## Empirical evidence

- Fixture: `tests/fixtures/adaptive-empirical-excerpt.txt`.
- Li, Liu, Gao and Cohen (2024), *Challenging the N-Heuristic: Effect size, not sample size, predicts the replicability of psychological science*, PLOS ONE 19(8): e0306911, [DOI](https://doi.org/10.1371/journal.pone.0306911).
- [Publisher HTML](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0306911); [publisher PDF](https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0306911&type=printable). Both read in the web tool. PDF has 15 pages. Direct curl DOI acquisition returned HTTP 200 and redirected to the publisher HTML; direct curl PDF acquisition returned HTTP 200 `application/pdf`.
- Publisher copyright statement identifies © 2024 Li et al. and Creative Commons Attribution License, allowing reuse with author/source attribution. Short excerpts are attributed in the fixture.
- Observed locators: `Survey study`, PDF page 10/15; `Fig 5` caption, page 11/15; `Discussion` limitations, page 12/15. Browser text also directly exposes these named headings.
- The fixture preserves recruitment, exclusion, criterion-order randomization, scale, two means and their comparison, error-bar convention, and nonrepresentative sample limitation. Respondents rate importance; these are not causal sample-size interventions or observed replication rates. A two-mean comparison can be a labeled teaching reconstruction; it must not invent the seven other means or numerical SEs. The original figure image is omitted.

## Theory and argument

- Fixture: `tests/fixtures/adaptive-theory-excerpt.txt`.
- Ioannidis (2005), *Why Most Published Research Findings Are False*, PLOS Medicine 2(8): e124, [DOI](https://doi.org/10.1371/journal.pmed.0020124). Publisher identifies it as an Essay: a scholarly journal argument, rather than a textbook or an empirical experiment.
- [Publisher HTML](https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.0020124); [publisher PDF](https://journals.plos.org/plosmedicine/article/file?id=10.1371/journal.pmed.0020124&type=printable). Both read in the web tool; PDF has six pages. Direct curl DOI acquisition returned HTTP 200 and redirected to publisher HTML.
- Publisher and PDF identify © 2005 John P. A. Ioannidis and Creative Commons Attribution License permitting reuse with proper citation.
- Observed locator: `Modeling the Framework for False Positive Findings`, PDF pages 1–2/6 (printed 0696–0697), formula in unnumbered prose beside Table 1. The fixture includes selected definitions, simplifying assumptions, PPV formula and truth-more-likely inequality. Table 1 itself is omitted.
- The explanatory structure should retain assumptions → prior odds/power/error definitions → posterior reasoning → conditional conclusion. The baseline formula precedes bias and multiple-team extensions; neither those extensions nor the whole title claim is demonstrated by this fragment. R is odds; R/(R+1) is probability. Any worked numerical case or reconstructed 2×2 table must be explicitly instructional.
- Publisher links a [2022 correction](https://doi.org/10.1371/journal.pmed.1004085). The fixture omits Box 1 and its numerical example; do not import an old Box 1 result into a guide from this fragment.

## Genuine limited publisher route

- Fixture: `tests/fixtures/adaptive-abstract-only-excerpt.txt`.
- Silver et al. (2016), *Mastering the game of Go with deep neural networks and tree search*, Nature 529: 484–489, [DOI](https://doi.org/10.1038/nature16961), [publisher preview](https://www.nature.com/articles/nature16961).
- Observed publisher page: readable abstract followed by subscription preview, institutional access and purchase options. The web DOI resolver and direct PDF route stopped at an identity-provider redirect. Curl to `https://www.nature.com/articles/nature16961.pdf` returned HTTP 200 **text/html**, redirected to the article page with `error=cookies_not_supported`; it did not return PDF bytes. HTTP success therefore does not establish full-text acquisition.
- Only one short abstract sentence fragment is stored; no open reuse license was observed. This is a failure of the attempted publisher full-text route, not proof that no lawful full text exists anywhere. A truthful outcome either explains abstract-only scope or requests a lawful readable copy. DOI metadata, preview figure captions, and references are insufficient for full coverage.

## Tool-specific observations

The web tool’s DOI requests for both PLOS papers returned internal errors, while direct curl requests resolved to readable HTML with status 200. Python urllib also eventually resolved both PLOS DOIs to publisher HTML (189,235 and 182,702 bytes, respectively). This is a tool/path discrepancy, not a claim that the DOI is invalid. Positive page/PDF paths are independently verified above. A separate urllib Nature DOI probe, 10.1038/35057062, and its publisher PDF route each returned 3,038 bytes of HTML, not PDF; this probe is not the selected abstract-only fixture.

All generated guides using these fixtures should expose fragment coverage on the page and preserve the same numerical quantities, conditions and named locators in Chinese and English. Fixture selection is source preparation; render and bilingual checks are recorded separately by the implementing agents.
