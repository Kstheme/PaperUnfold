# Recorded copy, teaching, pause and resumption

Date: 2026-10-04. Native Codex agents, independent of the implementation agents.
Researcher answers were scripted by the evaluator; tutor responses and the saved
progress were generated through actual skill invocation. These checks do not
measure an actual researcher's learning or general reliability.

## Copy and enter teaching

The evaluator loaded the saved `agent-invocation-zh.html` bytes in an isolated
offline Edge page. A chapter prompt and a term prompt were selected, copied by
real Ctrl+C, and pasted by Ctrl+V into a second textarea. The pasted values
matched the original prompt text; no clipboard API stub was used for this check.
[The actual copied prompts](ticket06-copied-prompts.json) were passed to two
separate fresh tutor agents. The chapter agent used only its copied chapter
excerpt; the term agent used only its copied term excerpt, not another guide.

Chapter teaching explained §3.2's weighted output and §3.2.1 Equation (1), then
asked for the contributions from two example values. The term agent explained
weighted sum, labeled its values as teaching data, and asked how exchanging the
weights changes the result. Each started on the specified goal with one main
question and stated the supplied coverage.

## Answer, feedback and pause

Evaluator answer to the chapter lesson:

> 每个value的贡献分别是0.75×(2,0)=(1.5,0)，0.25×(0,4)=(0,1)，加起来是(1.5,1)。所以(1.5,1)就是注意力权重。

Actual tutor excerpt:

> 你算出的两项贡献和总和都正确，这说明你已经能计算这个例子的加权和。需要修正的是最后一句：(1.5,1) 是 attention 的输出向量。

It contrasted weights with output, then asked about fixed weights and changing
the second value to `(0,8)`. The evaluator answered “懂了，先暂停，不回答新问题”
and specified a progress destination, explicitly asking not to count the
affirmation as verification. The agent actually read the progress reference and
saved [ticket07-actual-progress.json](ticket07-actual-progress.json).

The record credits only the supported numerical calculation. The conceptual
distinction stays `explained_unverified`, with the original mistaken statement,
unanswered check, and next learning entry retained. Its source path is null
because this lesson used pasted prompt excerpts, not an original material file.
No mandatory extra question was imposed on pause.

## New conversation with original material

A new agent, with no earlier lesson history, read the saved record and
[ticket07-actual-source.txt](ticket07-actual-source.txt). It invoked the public
resume helper, then said:

> 记录里，你已经正确算出两个 value 的加权和；接下来要核对的是注意力权重与输出向量的区别。

Its first resumed check reused the fixed-weights/change-value example and asked
how the result distinguishes the two quantities. It did not repeat the entire
lesson, claim mastery, or lose the open conceptual gap. No further answer was
supplied in this validation; the paused record remains the actual saved example.

## New conversation without original material

Another fresh agent was given the same progress record and no original paper.
It read only the skill, progress reference and record. Actual reply excerpt:

> 记录没有保存原文，因此目前只能恢复学习位置，不能据此继续解释论文。需要补回第 3.2 节关于输出是 values 加权和的短句，以及第 3.2.1 节公式 (1)。

It offered clearly labeled generic background as an optional choice, without
inventing a paper explanation or altering the saved progress. Mathematical
typesetting in the quoted excerpts above is normalized for Markdown readability.
