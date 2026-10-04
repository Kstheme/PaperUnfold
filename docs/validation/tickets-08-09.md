# Tickets08/09 validation

Date: 2026-10-04. User-confirmed review baseline: `f1f60da10cff33892a383a2afd731300b8ea25f3`. Acceptance uses actual skill inputs, visible artifacts, dialogue and saved progress. Internal prompt wording is not a test seam.

## Ticket08: optional mechanism and static fallback

A fresh agent read the skill and branch references, without implementation/tests or earlier answers, then produced [Attention guide and optional demo](../../examples/mechanism08/attention-guide.html) and [empirical static fallback](../../examples/mechanism08/empirical-guide.html). [Run record](../../examples/mechanism08/run.md) retains exact requests, partial source coverage, source checks and rendering commands.

The first request asks how sharper softmax weights change the weighted output. Constructed scores `[0, ln(3)]`, scalar values `[2,6]`, temperature0.25–4 and their assumptions are visibly teaching data. Temperature is a teaching intervention, distinct from the paper's fixed key-dimension scaling; no training or paper reproduction is claimed. Independent worked values are:

| T | Weights | Weighted output |
| --- | --- | --- |
| 0.25 | 0.0122,0.9878 | 5.9512 |
| 1 | 0.2500,0.7500 | 5.0000 |
| 4 | 0.4318,0.5682 | 4.2729 |

Parent browser QA used keyboard Home/End on the actual generated slider, checking all three known values. With JavaScript disabled, controls stay hidden and the static worked table is readable. The [actual demo screenshot](../../examples/mechanism08/attention-demo.png) shows the T=4 endpoint. A source request to predict an arbitrary paper's replication probability by changing N instead receives a static design/rating explanation; no unsupported predictor or fabricated probability appears. Both basic guides remain useful independently of interaction.

Two renderer CLI tests were added through vertical red/green cycles; the first public input failed before support existed. Twenty renderer tests passed. `tests/check_mechanism_browser.cjs` additionally checks independent worked outputs, keyboard endpoints, offline operation, mobile layout, no-JavaScript fallback and rejection of JSON-authored executable behavior. The renderer is intentionally bounded to source-supported softmax teaching examples; other mechanisms use existing static explanations.

## Ticket09: actual reading, presentation and teaching

[Release examples](../../examples/release09/README.md) contain four freshly generated whole-main-paper orientation guides: algorithm Chinese, empirical English, and theory Chinese/English. Full bodies were actually readable; detailed object inspection, missing supplements and absent reanalysis are stated. [Provenance](../../examples/release09/generation-provenance.json) records versions, source hashes, actual environment and output languages. [Independent review](../../examples/release09/source-audit.md) read the primary papers separately and compared key claims and conditions with the generated JSON/HTML.

Review corrected overbroad evidence locators, clarified the original2005 versus2022 correction scope, and surfaced the empirical Bayesian p=.057 caveat. The significant joint-model N result, algorithm score discrepancy and theoretical conditional conclusions remain visible. Minimal retained algorithm anchors are distinguished from the full original material read. PLOS source text is attributed under the observed CC-BY statements.

All six newly generated guides passed the public offline Edge/Playwright artifact checker: navigation, folding, local anchors, teaching payloads, clipboard fallback/success stub, JavaScript-disabled selection, math and 390px viewport; zero network requests. Screenshot viewports were visually inspected and are actual captures. Keyboard copy/paste of the empirical Results and a term prompt passed without a clipboard API stub. The historical payload used by the tutor is retained separately from the payload recaptured after final guide corrections.

| Artifact | Details | Anchors | Math | Visuals |
| --- | ---: | ---: | ---: | ---: |
| Mechanism Attention | 12 | 19 | 10 | 1 |
| Mechanism empirical fallback | 14 | 40 | 0 | 1 |
| Release algorithm Chinese | 27 | 64 | 1 | 2 |
| Release empirical English | 24 | 48 | 0 | 1 |
| Release theory Chinese | 24 | 50 | 1 | 1 |
| Release theory English | 24 | 50 | 1 | 1 |

An actual tutor invocation used the copied chapter prompt and readable original source. Scripted evaluator replies exercised a mixed/incomplete answer, explicit lack of knowledge, direct explanation and stopping. Feedback separated the supported comparison distinction from the incorrect causal and universal claims. The tutor taught after “I do not know,” honored direct explanation without a quiz, and stopped while saving truthful progress. A fresh agent read only the saved record and original text, restored the target/gap, and continued without rewriting the entire lesson or upgrading statuses. Public save/resume helpers succeeded; paused and resumed records retain identical `understanding` and `gaps`, and both relative source paths resolve. Transcript link targets were normalized for portable publication.

The conventional prose comparison uses the same actual passage and context as its guide counterpart. No time savings, mastery rates or all-discipline quality are inferred. These evaluator inputs are not actual human learning evidence. Installation, host discovery and project licensing remain ticket10.
