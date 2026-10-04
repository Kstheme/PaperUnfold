# Ticket09 independent source audit

Review date: 2026-10-04. This reviewer established the source baseline independently before opening any ticket09 guide. The scope is source fidelity and whole-paper orientation, not a guarantee of exhaustive mathematical verification or learning outcomes. Generated-artifact findings are appended after the artifacts become available.

## Material actually inspected

- **Vaswani et al., Attention Is All You Need:** live [arXiv HTML v7](https://arxiv.org/html/1706.03762v7), explicitly marked 2023-08-02. Read Abstract and every main section 1–7 including subsections, Tables 1–4, equations, references boundary, and Attention Visualizations captions. Visually inspected the original Figure 1 and both halves of Figure 2 from that version. Appendix visualization captions were read; the individual appendix attention plots were not visually verified. Locations in this audit are HTML sections/table labels, not invented PDF pages or positions from the 2017 conference edition.
- **Li et al. (2024):** cached publisher printable PDF, [DOI](https://doi.org/10.1371/journal.pone.0306911), 15 physical pages. Read all main text pp1–13, supporting-information inventory and author statements pp13–14, and references pp14–15. Visually rendered/inspected pp7, 9, 11, including Figures 2, 4, 5 and Table 2. The separate supporting files and OSF data/code were not inspected or reanalyzed.
- **Ioannidis (2005):** cached publisher printable PDF, [DOI](https://doi.org/10.1371/journal.pmed.0020124), six physical pages, printed pages 696–701. Read every main section, Box 1, Tables 1–4 and figure captions, with references on p6. Visually rendered/inspected pp2–5, including original formulas/tables, Figures 1–2 and Box 1. Also opened the publisher landing page and the [2022 correction](https://doi.org/10.1371/journal.pmed.1004085).

PDF cache provenance comes from the earlier acquisition records, rather than a claim of a new PDF download in this review:

| Source | Recorded acquisition time UTC | SHA256 of inspected PDF |
| --- | --- | --- |
| Li2024 publisher printable PDF | 2026-10-04T07:41:15.343550+00:00 | `b895a7ad9544ee917a2205071925ba81eeb8bfe12a74c9c1e7cf93d6bc8556e4` |
| Ioannidis2005 publisher printable PDF | 2026-10-04T07:41:18.156076+00:00 | `ffc1005680cb620eec4c913437dfabbf311b535cfe16cbaeb2faec1f92afc362` |

Both PDFs carry a Creative Commons Attribution statement on p1. The arXiv HTML identifies its perpetual nonexclusive license and separately permits attributed reproduction of figures/tables for journalistic or scholarly work; this is not a blanket CC license for its full text. This audit paraphrases source claims and does not redistribute full paper text. All render/extraction intermediates were prepared in the Windows temporary directory.

## Whole-paper map and focused source checks

### Algorithm source

The map should connect the sequential-computation problem (§1), earlier alternatives and the motivation for attention (§2), the complete encoder–decoder mechanism (§3), complexity/path-length rationale (§4), reproducible training conditions (§5), three kinds of empirical evidence (§6), and qualified future directions (§7). A guide solely explaining Q/K/V would omit the paper's research thread.

| Check | Observed source location | Preservation requirement |
| --- | --- | --- |
| Architecture | §3.1; Fig1 | Encoder and decoder stacks use six layers in the base model; decoder includes masked self-attention and encoder–decoder attention. Residual addition precedes layer normalization in this source. Generation remains autoregressive. Training parallelism does not imply parallel generation. |
| Attention | §3.2.1 eq(1); Fig2 left | Scale QK-transpose by square root of key dimension, apply softmax to produce weights, multiply by V. Decoder masking is applied before softmax. The variance argument assumes independent zero-mean unit-variance components. |
| Heads | §3.2.2; Fig2 right | Learned Q/K/V projections run in parallel; concatenate heads then apply output projection. Base configuration has eight heads and 64-dimensional keys/values. Do not claim heads must each acquire an assigned linguistic role. |
| Non-attention components | §§3.3–3.5 | Preserve positionwise FFN, embeddings, output softmax, and added sinusoidal positions. Learned positions perform nearly identically in Table3; extrapolation is a motivation/hypothesis, not demonstrated universal success. |
| Complexity | §4 Table1 and subsequent discussion | Self-attention is quadratic in length per layer; constant sequential operations/path length are different quantities. The comparison with recurrence is favorable when n is smaller than d. Restricted attention is future work here. Table1 in v7 lists logarithmic convolution path length; prose distinguishes contiguous and dilated kernels. |
| Training | §§5.1–5.4 | WMT14 datasets differ in size/tokenization; eight P100 GPUs; base 100K steps/12h versus big 300K/3.5days. Adam schedule includes 4000-step warmup. Training costs in Table2 are estimated FLOPs, not measurements on identical competing hardware. |
| Results | §§6.1–6.3 Tables2–4 | Translation test results, development-set variations, and parsing evidence must remain distinct. EN-DE big BLEU28.4. Important source inconsistency: Abstract/Table2 give EN-FR41.8, while §6.1 prose gives41.0. Label the respective locations instead of silently reconciling them. Parsing is evidence on a further task, not all-domain proof. |
| Conclusion/appendix | §7; Attention Visualizations | Generalization beyond text and less sequential generation are proposed future work. Captions interpret selected attention heads as apparently related to dependencies/anaphora; avoid treating attention plots as causal explanations. |

### Empirical source

The map should include Introduction's diagnostic question (pp1–3), dataset construction and operational definitions (pp4–5), correlations and separate controlled regressions (p6), the suppressor qualification and robustness discussion (pp7–10), the independent survey (pp10–12), and Discussion's limitations and recommendations (pp12–13).

| Check | Observed location | Preservation requirement |
| --- | --- | --- |
| Scope/design | pp3–5 Method | Observational synthesis of replication attempts; diagnostic, not causal. Retrieved316 effects; null effects excluded; available-data analyses have307 sample-size observations and284 effect-size observations. Original-study N refers to retested conditions, not replication-study N. |
| Outcome | p5; Table1 p4 | Main outcome is the projects' binary replication-success assessment, with heterogeneous operationalizations. Alternative definitions are robustness analyses, not interchangeable identical measurements. |
| Main association | p6 | Spearman original N versus replication r_s=-.02, p=.741; original effect size r_s=.21, p<.001. Separate logistic models control design and use logged predictors. These are associations in this dataset. |
| Important qualification | pp7–8 | With N and effect size entered together, both significantly predict replication: N B=.56, SE=.20, p=.005; effect size B=1.03, SE=.28, p=.0002. A blanket statement that N never predicts replication would misrepresent the paper. |
| Inverse relation | p6; Fig4 p9 | N and effect size r_s=-.49, p<.001, identified post hoc. Five extreme points omitted from the display remain in the analysis. Publication bias is a possible contributor, not eliminated or established cause. |
| Visual statistics | Fig2 p7; Fig5 p11 | Fig2 shows coefficients from separate models and95% CIs; Fig5 shows surveyed importance ratings with ±1SE, not observed replication probabilities. |
| Survey | p10 | Final215 respondents after excluding10 undergraduates; convenience recruitment. Sample size mean3.84 versus effect size3.61, t(214)=3.21, p=.002, on five-point ratings. Preference evidence is separate from the replication dataset. |
| Limits | pp12–13 | Both replicated-study pool and survey respondents are nonrepresentative; causal effects of publication policies are unknown; small-N effects may be inflated. Larger N still improves power under fixed other conditions and precision. Avoid recommending an equally rigid effect-size heuristic. |

Additional uncertainty: the Bayesian-definition sensitivity result on p5 reports effect-size p=.057, so not every alternative reaches the conventional .05 threshold. Table1 lists57 Many Labs effects, while the continuous-outcome passage p8 says58; do not manufacture a reconciliation if using those counts.

### Theoretical/argumentative source

The paper is an essay deriving and interpreting a probability framework, not an observed census of all published research. The map should connect the base model (pp1–2), bias and independently repeated testing (p2), six corollaries (pp2–4), illustrative low-prior-odds example and study-design settings (pp4–5), the null-field/bias argument (p5), and proposed improvements (pp5–6).

| Check | Observed location | Preservation requirement |
| --- | --- | --- |
| Definitions/base formula | p1; Table1 p2 | R is true-to-null odds among tested relationships, not a probability. Prior probability is R/(1+R). PPV=(1-beta)R/((1-beta)R+alpha). It concerns a claimed positive relationship under model assumptions, not p interpreted as probability of truth. |
| Majority criterion | p2 | PPV>.5 iff (1-beta)R>alpha in the unbiased single-study model. Title/conclusions should be framed through modeled settings, rather than claimed measured global prevalence. |
| Bias | p2; Fig1 p3 | u converts otherwise nonpositive analyses into reported findings, assuming the conversion does not depend on truth. It differs from random error. Effects of changing u are qualified by power relative to alpha. |
| Multiple teams | p2; Table3 p3; Fig2 p4 | At-least-one-significant selection among independent, equal-power studies; formula R(1-beta^n)/(R(1-beta^n)+1-(1-alpha)^n). This does not show that pooling all evidence or multiple independent confirmations necessarily reduces truth. |
| Corollaries | pp2–4 | Six implications follow under the modeled comparisons; p4 explicitly discusses interactions and countervailing influences. Preserve all-other-factors-equal qualification and the distinction between power and sample size. |
| Box/settings | Box1 p4; Table4 p5 | These are assumed/simulated illustrative settings. Table4's first row PPV=.85 uses power.80, R=1:1, u=.10, alpha=.05; not a measured RCT success rate. Avoid treating old illustrative genomic counts as present empirical estimates. |
| Null fields | p5 | Argument is conditional on a field with no true relationships (or very low PPV); it does not establish that an identified real field contains no true effects. |
| Improvements | pp5–6 | Better powered evidence, reduced bias, the totality of evidence, registration/protocols, and attention to prior odds. Large studies can retain bias; truth is not known with100% certainty; prior assumptions can be subjective. |

The inspected PDF is the original2005 version. The publisher's **2022 correction only repairs missing parentheses in Table2's Research Finding=Yes / True Relationship=No cell**. It does not say all tables or Table4 were numerically corrected; the cached PDF must not be described as an already corrected edition. The guide may explain the original bias PPV in the running text while linking the later correction precisely.

## Artifact review status

Reviewed all four JSON guides and their corresponding HTML against the independent baseline above. The review includes every research-thread statement, section point, term explanation, formula/figure explanation, and retained evidence record. Checked that the HTML includes all natural-language thread/point/term claims from JSON (20 algorithm, 19 empirical, 15 each theory guide at the initial review snapshot). This is a content transfer check; browser interaction checks are reported separately by the main agent.

| Artifact | Independent content assessment |
| --- | --- |
| algorithm-zh | Seven section groups cover motivation/background, attention, other architecture components, complexity, training, results, and conclusion. Attention equation, mask/shift distinction, autoregressive generation, task limits, and the source's EN-FR41.8/41.0 discrepancy are preserved. The original Figure2 explanation agrees with the inspected visual. Compact treatment omits most training hyperparameters and numerical parsing results; it does not falsely present those as reproduced experiments. |
| empirical-en | Covers the diagnostic question, pooled design, separate correlations/models, joint-model suppression qualification, survey, discussion and unread supplemental files. Counts307/284, r_s values, model coefficients/SE/p, and survey means/test agree with the source. Fig2 is correctly described as separate models with95%CI rather than the joint model or ±1SE. Nonrepresentativeness, possible publication bias, and unknown policy causality are retained. |
| theory-zh and theory-en | Both follow the same six section groups through framework, bias, independent testing, corollaries, simulated settings/null fields, and proposals. Base PPV is algebraically equivalent to p1. Both preserve R as odds rather than probability, the similar-power assumption, u's truth-independence assumption, at-least-one-significant selection, conditional null-field interpretation, large-study bias, and subjectivity of R. Neither turns the title into a measured universal false-finding rate. |

Bilingual comparison: manually compared all thread statements, section roles/points, formula reading/contribution/steps and five term explanations between the two theory guides. The English and Chinese versions retain the same condition directions and negative qualifications: PPV is neither power nor1−p; no general measured global error census; no claim that consistent independent confirmation lowers credibility; null-field assumption does not diagnose a real field; large studies may retain bias. They share the source equation and evidence IDs. This is semantic review of these examples, not evidence of general translation quality.

Required fixes reported to the builder before approving the final snapshot:

1. The initial empirical evidence `e3` labeled PDFpage5 spans pp5–8; initial theory `t5` labeled p2 begins on p1. Narrow or accurately relabel these extracts. Theory `t12` unnecessarily includes the intervening Table4 across a page break; narrow it to the actual evidence sentence.
2. Add a visible empirical sensitivity caveat: Bayesian-definition association on p5 has r_s=.27 and p=.057, rather than burying it in an oversized evidence extract. The initial explanatory text does not falsely claim that every robustness test is significant, but readers need the uncertainty explicitly.
3. Add original2005-version identification and the precise2022 Table2-only parentheses correction note/link to both theory guides. The initial guides do not make a false correction claim, but omit this important version limitation.
4. Replace opaque theory PDFmetadata source names with paper title, author/year and DOI; add DOI/arXiv version to the other standalone guide source identifiers. An external source index alone does not give a copied teaching prompt a robust paper identifier.

All four requested fixes were independently verified in the rerendered final JSON and HTML. The empirical guide now explicitly reports the54-study Bayesian-definition r_s=.27, p=.057 uncertainty, with exact p5 evidence. `e3`/`e4` now remain on p5. Both theory `t5` records start at the actual p2 bias definition; `t12` is the p6 continuation of the totality-of-evidence sentence. Both theory guides identify the original2005PDF, cite the2022 correction DOI, and correctly restrict its scope to the missing parentheses in Table2's indicated cell. All four standalone source identifiers now contain the paper title and DOI/arXiv version, with original URLs in coverage.

Final semantic checks also retain the Attention41.8/41.0 discrepancy, both Li joint-model coefficients, and all bilingual negative/conditional distinctions listed above. Verified all70 natural-language thread/point/term statements in the final JSON appear in corresponding HTML (20 algorithm, 20 empirical, 15 each theory). The main agent reports final `copied-prompts.json` was recaptured through actual copying from corrected guides; historical pre-repair inputs remain separately in `session-input-prompts.json`, and the teaching run used those inputs plus full original text. This reviewer did not edit prompt/session artifacts or repeat their browser verification.

Publication cleanup recheck: the algorithm guide now retains22 minimal retrieval anchors plus the Figure2 caption instead of long ordinary-text extracts. Independently checked all23 retained strings occur in the actual acquired arXivv7 source, and each expanded section/paragraph locator matches the original context read above. The20 algorithm thread/point/term statements remain unchanged and all appear in rerendered HTML. Coverage explicitly distinguishes whole-body reading from retained short anchors; those anchors alone are not claimed to establish the full explanation, and deep teaching requires obtaining the complete relevant passages. The duplicated numerical anchors are accurately labeled as HTML extraction traces. The unchanged main claims still pass the original source-based review. PLOS artifacts were not changed in this cleanup.

During artifact review, also independently rendered and inspected physical p4 of the newly available15-page arXivv7PDF cache (`release09-attention-pdf.source.pdf`), confirming Figure2 and equation(1) really occur at the guide's PDFpage4 locator. This is additional visual/location evidence beyond the initial live-HTML inspection.

**Result:** all four final guides pass this focused independent source-fidelity and bilingual semantic review. This means no remaining material claim error was found in the reviewed explanations/evidence; it does not prove every omitted detail, all-disciplinary effectiveness, reproducibility of the paper's experiments, or researcher mastery. No edits were made to the guides by this reviewer. The independent baseline does not prove from output alone that the generating agent read every source page; generation provenance remains in that agent's retained run records.

The reviewed final HTML snapshots have these SHA256 values, allowing later edits to be distinguished from this review:

| HTML | SHA256 |
| --- | --- |
| algorithm-zh.html | `025082652622a06a679375b3fe62bcac6afa09cac5561d5fe230b1b5bf526229` |
| empirical-en.html | `8b6e549af7e4332350746aaeae531d69de16fe02bdaf1274cd390ac1507ce45d` |
| theory-zh.html | `205af94f3c0252f24bc00b5c4c23a6de640f52027b2f00c2e0066488ddc10900` |
| theory-en.html | `9bf3e685b6d69ec0c12230d78dfa1b853349521a60a364a53392a4c7f4895c31` |
