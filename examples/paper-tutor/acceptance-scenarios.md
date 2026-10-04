# Paper Tutor acceptance scenarios

These are invocation inputs and review criteria, not generated lesson transcripts
or successful-run claims. Execute them with a host agent that reads
`skills/paper-tutor/SKILL.md`. Retain actual user-visible turns and compare the
lesson with the supplied original passage. Predetermined replies exercise feedback;
they do not measure a real researcher's learning.

Use the readable original excerpt in `tests/fixtures/attention-excerpt.txt` when
available. It identifies *Attention Is All You Need*, §3.2 and §3.2.1, but contains
only two short excerpts and Equation (1). Paste that excerpt or provide the file
together with the invocation. The scaling-motivation context is intentionally
absent: explaining it requires a visible background label or reading the missing
source before attributing it to the authors.

## Direct source entry and a teaching round-trip

Request: “Use $paper-tutor with this excerpt. 我想理解为什么 Scaled Dot-Product
Attention 要除以 √d_k。”

Inspect the actual first turn: Chinese explanation with original terms, observed
source locations and limited coverage, a short main thread, one main question,
and no requirement to generate a guide. Reply with an answer appropriate to the
question actually asked; the following inputs exercise separate branches rather
than prescribe the tutor's question sequence.

| Researcher input | Observable review criterion |
| --- | --- |
| “除以 √d_k 是为了把点积变小。” | Recognizes the operation but identifies the missing explanatory link; motivation beyond this fixture is marked as background or supported by additionally read source. |
| “除完以后，softmax 肯定会给每个位置一样的权重。” | Corrects the uniform-weight misconception with the actual relationship; avoids claiming a guaranteed uniform distribution. |
| “我不知道 softmax 是什么。” | Explains this relevant prerequisite as background; after a reply demonstrates it, returns to the scaling question. |
| “不知道，讲一下吧。” | Provides teaching immediately and one smaller check, rather than repeating the same diagnostic. |
| “懂了。” | Acknowledges without asserting mastery from that phrase alone. |
| A substantive explanation of the taught scaling rationale in the researcher's own words | Specifies the narrow point supported by the answer, preserves stated assumptions, and keeps any supplementary rationale distinct from the originally supplied passage; does not certify chapter-wide mastery. |

## Researcher control

Run each independently after source entry so one exit does not conceal another:

- “直接解释，不要提问。” The selected explanation appears without a compulsory quiz.
- “跳过这个，讲这里的加权求和。” The target changes; the skipped point stays unverified.
- “换个问题：这个公式里的 Value 是做什么的？” The readable new target takes priority.
- “画一下知识地图。” A compact map distinguishes the goal, prerequisites, and evidence
  of understanding; it does not appear unprompted in every turn.
- “暂停。” and “结束。” Teaching and questions stop, with an honest short recap.

## Fidelity, language, and other argument structures

Repeat source entry in English, then explicitly request Chinese. Inspect language
switching while source labels and original terms stay recognizable. Trace selected
claims, assumptions, formula symbols, and any numeric teaching values to the source
or to visible background/example labels.

With a readable empirical or argumentative paper excerpt and a chosen inference
question, inspect whether the tutor follows the actual evidence and premises.
Neither computational steps nor a standard experimental section should be invented.
If the selected question needs an absent passage, inspect an honest coverage limit
and a focused request for that passage rather than a source-attributed guess.

Persistent learning files, HTML-to-chat integration, PDF extraction, and paper
retrieval are outside ticket 02's acceptance scope.
