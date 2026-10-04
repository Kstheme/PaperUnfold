# Optional mechanism interaction

Complete the basic guide first. Add an interaction only when requested or when
one controllable variable answers a specific understanding question. State the
question in the title, connect the relationship to an observed source passage,
and keep assumptions and limits beside the controls.

## Supported softmax example

Use `type: softmax` only for a source-supported softmax weighting relationship.
It answers how relative weights and a weighted scalar output change when fixed
scores are divided by a teaching temperature T. The renderer accepts 2–6 fixed
scores and the same number of scalar values, each finite and within −100..100.
The only control is T, from 0.25 to 4, in steps of 0.25, initially 1.

The renderer shows the equations, fixed inputs, weights and weighted output;
static worked rows at T=0.25, 1 and 4 remain readable without JavaScript. This
does not simulate training, predict performance, or reconstruct a paper result.
The scalar values simplify the general vector-weighted relationship.

Choose constructed inputs that make the change intelligible. Label them as
teaching data using `kind: analogy` where appropriate. State explicitly whether
temperature is a teaching intervention rather than an author-defined parameter.
For Attention, keep the paper's fixed `1/sqrt(d_k)` scaling distinct from this
teaching temperature; changing T does not reproduce changing the model dimension
or training an attention layer.

Read [guide-format.md](guide-format.md) for the fields. A literal evidence match
checks traceability, not whether the mechanism is justified by the source.
Review that relationship before rendering. Exercise both slider endpoints and a
worked interior value when browser inspection is available. Otherwise retain the
static explanation and report that the controls were not browser-verified.

## Static fallback

For unsupported mechanisms or insufficient evidence, use an existing process,
concept, table or formula visual with a focused explanation of the limits.
Prefer source-supported steps or a clearly labeled worked numerical example.
Keep the basic guide usable when execution is unavailable.

For example, researchers' importance ratings of sample size do not supply a
validated model that predicts an individual paper's replication probability.
Explain the design, measurements and inference limits in a static comparison;
do not invent such a predictor. The renderer executes only its bounded softmax
control, never agent-authored code supplied in JSON.
