# Explain the mechanism, not just its name

Use this check in the default guide. Keep the overview short; give the central
mechanism enough space. Speed comes from reusing sources and avoiding redundant
acquisition/testing, not from removing explanatory steps.

## Problem and idea

Explain the obstacle, what existing approaches accomplish, their relevant limit,
and what this paper changes. Separate the authors' rationale from explanatory
inference. Novelty judgments need comparison evidence; avoid unsupported scores.

## Central steps or inferences

For each method stage explain **input → operation → output → role in the next
stage**, including stopping criteria and essential branches. Explain why the
stage is needed. A worked example can connect stages; label invented inputs as
teaching examples. Distinguish training from inference when relevant. For empirical
research explain design, sampling, measurement and inference; for arguments explain
premises, support and the transition to the conclusion, without inventing a pipeline.

For central mathematics define symbols and shapes/units when supplied, the
operation, its effect and assumptions. Link it to the next step. Preserve
ambiguous notation as an unresolved issue. An equation alone is not an explanation.

## Evidence and limits

Report baseline, metric, configuration and qualified change for main results.
Include material counterexamples. Where reported, use a compact ablation/comparison
to explain which components matter; separate empirical support from proof of a
causal or semantic mechanism. Say when component evidence is missing. Separate
what the paper establishes, what is interpretation and what is future work.

## Visuals and completion

A pipeline shows actual dependencies, not unrelated cards. Number stages so text
can refer to them. Label branches, quantities and intermediate artifacts. Every
important stage needs corresponding explanation and an observed source anchor.
Add local diagrams/tables for difficult transformations. Use original objects
only when read. Could the reader describe the important intermediate steps, why
each is present and which evidence supports the benefit? If not, add the missing
explanation. Exhaustive audits and browser regression remain explicit follow-ups.
