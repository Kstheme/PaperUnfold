# Ticket 08 — fresh paper-guide skill run

Run date: 2026-10-04. Output language: Chinese. These are actual skill-produced reading guides for two researcher requests, not unit-test fixtures or reconstructed existing answers.

Read before drafting: `skills/paper-guide/SKILL.md`, `references/mechanism-interaction.md`, `references/guide-format.md`, and `references/visual-explanations.md`. Read the two actual supplied text sources. No renderer implementation, tests, existing guide answers, README, or tracker was read or modified. No commit was created.

## Request A

“先给这段论文的简明导读，再加一个轻量小实验，帮助我看清 softmax 分布变尖时，权重和加权输出分别怎样变化。用明确标注的教学数值，说明温度T并不是论文定义的训练参数。”

Source: `tests/fixtures/attention-excerpt.txt` (present; fallback unnecessary). Only the supplied Section 3.2 short excerpt, Section 3.2.1 Equation (1) transcription and final-paragraph short excerpt were used. The original remote paper was not consulted because the request concerns this supplied text. The equation supports softmax weighting followed by multiplication by values. The omitted antecedent of “this effect” does not establish a specific author motive; the guide explicitly says its context is missing.

Output: `attention-guide.json` and `attention-guide.html`. The basic guide is complete before the optional bounded softmax teaching visual. Fixed teaching scores are `[0, ln(3)]`; scalar values are `[2,6]`. The temperature is explicitly a teaching intervention, not a parameter defined in the supplied paper excerpt. The paper's `1/sqrt(d_k)` factor remains distinct. No training or paper-result reproduction is claimed. The example explains that sharper weights favor the higher-scoring value; output direction also depends on the chosen values, rather than being universal.

## Request B

“做个滑块，改变样本量N，预测任意单篇论文的真实复现概率；无法可靠预测时，给静态解释即可。”

Source: `tests/fixtures/adaptive-empirical-excerpt.txt`. Only supplied Survey study sentences, Fig 5 caption sentence and Discussion limitation were read. The source appendix preserves identity, DOI, publisher source and stated CC BY attribution. The source-supplied PDF page locators remain identifiable and are labeled as supplied; no original page image was inspected.

Output: `empirical-guide.json` and `empirical-guide.html`. The basic guide remains useful: recruitment, 215 analyzed respondents after excluding ten undergraduates, randomized criterion presentation order, five-point importance ratings, means 3.84 and 3.61, t(214)=3.21, p=0.002, and nonrepresentative samples are preserved. A static table reconstructs only the two reported means. No N slider or invented probability predictor is included. The guide distinguishes judgments from actual replication outcomes and random presentation from a sample-size intervention. It explains why these excerpts cannot validate individual-paper prediction. The caption's ±1 SE is retained without inventing SE values or the omitted seven means. The original Fig 5 is unavailable and is not claimed as reproduced.

## Rendering and review actually performed

Host Python: `E:\anaconda3\python.exe` (available `python` command). Both commands completed with exit code 0 and reported their saved HTML path:

```text
python skills/paper-guide/scripts/render_guide.py examples/mechanism08/attention-guide.json --output examples/mechanism08/attention-guide.html
python skills/paper-guide/scripts/render_guide.py examples/mechanism08/empirical-guide.json --output examples/mechanism08/empirical-guide.html
```

A separate artifact-only inspection loaded the generated JSON and HTML with the Python standard library. It checked that each `source.text` equals the actual fixture text as read, every evidence quote occurs literally in that text, and each local `href="#..."` resolves to an HTML ID. Results:

| Artifact | Literal quotes | Local links | Dangling local links | Native details | Range controls |
| --- | ---: | ---: | ---: | ---: | ---: |
| Attention | 3 | 19 | 0 | 12 | 1 |
| Empirical | 6 | 40 | 0 | 14 | 0 |

The Attention HTML's range input attributes are min=0.25, max=4, step=0.25, value=1. Independent calculation of the teaching example gave:

| T | Weight 1 | Weight 2 | Weighted output |
| ---: | ---: | ---: | ---: |
| 0.25 | 0.012195121951 | 0.987804878049 | 5.951219512195 |
| 1 | 0.25 | 0.75 | 5 |
| 4 | 0.431765131169 | 0.568234868831 | 4.272939475323 |

Semantic review compared explanations to the actual excerpts: author claims and inferences cite observed passages; constructed values and temperature are marked teaching analogy; generic notation definitions are marked background. The Attention source does not supply the omitted scaling rationale or results. The empirical source does not supply actual replication-rate measurements, causal effects of N, a validated prediction model, representative sampling, or original Fig 5 geometry. Neither guide extends its scope to a whole-paper conclusion.

Browser controls, rendered math appearance, interactive slider calculations, clipboard behavior, and visual layout were **not browser-verified in this run**. Parent-agent browser QA remains to exercise both endpoints and T=1, navigation, and expansion controls. Static link integrity and the existence of native expansion markup do not establish browser behavior.
