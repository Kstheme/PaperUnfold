# Same-source comparison: conventional prose and an expandable guide

This is a display comparison, not an experiment on learning speed or comprehension.

## Identical source and generation conditions

Both explanations below were freshly authored in the same Codex agent turn on 2026-10-04, in English, after reading the same acquired 15-page Li et al. (2024) main-paper text. The source is DOI 10.1371/journal.pone.0306911, **Challenging the N-Heuristic: Effect size, not sample size, predicts the replicability of psychological science**. The actual entry used was `skills/paper-guide/SKILL.md`, including its remote/PDF, visual, and format references. The prompt requested a source-grounded whole-paper guide and an ordinary text explanation of this same passage; it specified no reader proficiency, target duration, comprehension score, sampling seed, or temperature. No prior generated guide or expected answer was read. Runtime, source URL, retrieval timestamp and extraction hashes are in `generation-provenance.json`.

Target: the joint-predictor passage in Results, physical PDF pages 7–8, evidence `e8` in `empirical-en.json`. The guide counterpart is **Results: the suppressor qualification matters**, its third point. Both also rely on adjacent Results context `e7` (separate models) and `e9` (N–d association); neither treats this isolated paragraph as the complete paper.

## Exact target passage

```text
Consistent with a suppression effect, sample size,
as well as effect size, now significantly predicted replicability (B = 0.56, SE = 0.20, p = 0.005
Fig 2. Comparisons of predictors of replicabilit y. Coefficient estimat es from separate logistic regressio ns predicting replication success from the sample size
and effect size of the original study, control ling for study design. Error bars represent 95% confiden ce intervals.
https://do i.org/10.1371/j ournal.pone .0306911.g00 2
PLOS ONE
Effect Size Predict s the Replicabil ity of Psychologi cal Science
PLOS ONE | https://doi.or g/10.137 1/journal.po ne.03069 11 August 23, 2024 7 / 15

[PDF page 8 of 15]
and B = 1.03, SE = 0.28, p = 0.0002, respectively). 
```

## Ordinary text explanation

In the earlier separate logistic models, each predictor was tested with study design controlled: sample size did not significantly predict replication success, whereas effect size did. But sample size and effect size were inversely associated across these studies. When both log-transformed predictors entered the same model, sample size became significant (B=.56, SE=.20, p=.005) and effect size remained significant (B=1.03, SE=.28, p=.0002). The authors describe this as consistent with suppression: smaller investigated effects can obscure the conditional predictive relationship of larger N. This is a comparison of associations across selected studies. It does not show that increasing N causes greater replication under arbitrary changes to a study, or that N is irrelevant. The nonrepresentative dataset and possible publication bias further limit generalization.

## Guide presentation of the same point

Open [the actual English guide](empirical-en.html#section-results). The chapter separates the simple correlations, separate adjusted models and joint model into three expandable points with literal evidence anchors. Its Fig 2 reading explains that the plotted confidence intervals belong to separate models and do not display the significant joint-model N coefficient. Essential terms define Cohen’s d, the binary replication outcome and suppression. The chapter’s actual copyable teaching prompt supplies original evidence and the goal of distinguishing these models; it does not send an automatic model request or claim that a reader has mastered the distinction.

The ordinary paragraph supplies the same conceptual distinction in continuous prose. The guide adds navigation, optional detail, evidence inspection and a manually copied teaching goal. There is no randomized comparison, measured time saving, comprehension gain or mastery-rate claim here. Actual browser checks and fresh tutor sessions are separate release records, not invented by this authoring script.

Attribution: Li X, Liu J, Gao W, Cohen GL (2024), PLOS ONE 19(8):e0306911, DOI 10.1371/journal.pone.0306911. The original paper is CC-BY; its wording in the exact excerpt is retained, including PDF extraction line breaks.
