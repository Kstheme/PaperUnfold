# Choose explanations from the paper

Use one reading method across disciplines: identify the question, trace the
reasoning or evidence that answers it, and preserve the conditions of the claim.
Resolve the reader's likely confusion. The central structure needs a rendered
visual whenever the source contains meaningful dependencies or inference relations.
The user does not need to select a discipline or a template.

## Adapt the research thread

- **Executable methods:** explain what each operation does, why adjacent steps
  connect, and what assumptions or constraints control the result. A process map
  or formula breakdown can show a difficult transition. Input/output labels are
  useful when present in the method, not mandatory across all papers.
- **Empirical evidence:** connect the question to the population, observation or
  intervention, comparison, measurement, result, and limits. Preserve sample
  size, units, uncertainty, eligibility, and observational/causal distinctions.
  A comparison table often helps more than an algorithm diagram.
- **Theoretical and humanities arguments:** distinguish premises, definitions,
  evidence or examples, inference, objections, and the qualified conclusion.
  Explain how the conclusion follows and what would weaken it. A concept map or
  premise-to-conclusion relationship can clarify this without inventing an
  experiment, a pipeline, or empirical results.

A paper can mix these structures. Follow its actual argument; no mandatory
`research_type` field or discipline taxonomy is needed. Keep the first research
thread brief. Put derivations, reading instructions, secondary comparisons, and
limitations in expandable section/visual details when appropriate. Essential
conditions must stay with the visible claim.

## Select a visual only for a question

Use a guide-level `map` for a genuinely observed broad thread; use a local map
for an excerpt and label its scope. Choose `process` for meaningful step
dependencies, `concepts` for premises or relationships, `table` for comparisons,
and `formula` for difficult notation or transformations. Executable methods need
a central `process` pipeline with directed edges and intermediate outputs.
Add local diagrams, formulas or evidence tables for separate understanding
questions; there is no one-visual cap. Isolated facts need no diagram. No empty
charts or mandatory visual per chapter. Format details are in [guide-format.md](guide-format.md).

Describe edge meaning explicitly. “Supports,” “assumes,” “contrasts with,” and
“is followed by” express different relations. Never let an unlabeled arrow
silently turn association into causality or premises into verified facts.

## Read actual figures, tables, and equations

When a relevant source object was actually available, explain:

1. **Purpose:** which research question or argument step it addresses.
2. **Reading:** relevant axes, units, variables, legend, comparison, or notation.
3. **Contribution:** what follows, which conditions apply, and what it cannot
   establish. Distinguish reported result from your explanatory inference.

Use `source_figure` for original figure/table readings, preserve its exact label
and observed location, and link literal caption/result evidence. An available,
verified local PNG/JPEG crop can be embedded. If only the caption was readable,
state that limitation; it does not license claims about unseen axes or marks.
If no crop is available, the renderer clearly says the image is not reproduced.
For an original equation, use a `formula` breakdown linked to its actual equation
locator and literal source evidence; mark derivation added by the teacher as
background or inference. Do not create a formula module for prose-only material.

All new maps/tables/formula breakdowns are visibly teaching reconstructions.
Use `analogy` for constructed numerical examples and name them as such. Never
present toy measurements as author data. Use `inference` for design motivation
not explicitly stated, with the specific source passage supporting that reading;
when even that support is absent, state that the motivation is unknown.

## Verify across languages

Keep original term spellings, equation labels, source locators, number values,
units, negation, and qualifications consistent. Translate explanations and
visual labels into the conversation language. Before saving, compare each claim
and relationship to its cited passage; a literal quote match alone does not prove
the interpretation. Chinese and English readings of the same source must make
the same qualified claims, not strengthen them during translation.
