# Recorded tutor entrypoint check

2026-10-04, independent native Codex agent invoking `paper-tutor` directly with
`tests/fixtures/attention-excerpt.txt`. Researcher inputs below were scripted by
the evaluator; quoted tutor excerpts are from actual generated responses.
The lesson used no guide output. This is a selected-turn record, not a manually
written demonstration or evidence of educational effectiveness.

1. **Start:** explain Attention output and Q/K/V in Chinese from the supplied text.
   The tutor stated the excerpt's limits, located the weighted sum in §3.2 and
   Equation (1) in §3.2.1, and labeled vector examples as invented teaching data.
   Its single check asked for the weighted output and which values were combined.

2. **Mixed answer:** “我算出 0.75×(2,0)+0.25×(0,4)=(1.5,1)。组合的是 V，所以我觉得 (1.5,1) 就是模型算出来的注意力权重。”
   The tutor credited arithmetic and V, corrected output versus weights, and
   asked how fixed Q/K with a changed V affects the result. It did not infer
   general mastery from the correct calculation.

3. **Knowledge gap:** “我不知道，我没弄懂矩阵乘法，也不知道怎么算两个value的加权和。”
   The tutor immediately worked through coordinate-wise weighted addition,
   treated the prerequisite gap as tentative, and gave a smaller check: `0.5×(2,6)`.

4. **Prerequisite answer:** “0.5×(2,6)=(1,3)，就是每个坐标乘0.5，再和其他value的对应坐标相加。请继续这一轮，回到最初的 Attention 输出和 Q/K/V 问题。”
   Actual tutor excerpt: “这支持你已掌握**向量加权求和这一步**，我们回到最初的问题。”
   It returned to Q/K → weights → weighted V → output and asked one dependency
   check instead of expanding into a general mathematics exam.

5. **Direct explanation, language override, map, pause:** “懂了。Please explain the answer directly in English, without asking me a question. Then give a small concept map and pause this session.”
   It explained the fixed weights and changed output in English, gave an ASCII
   concept map, and asked no question. Actual excerpt: “The distinction between
   weights and output, and their dependence on Q/K/V, has been **explained but
   remains unverified**; ‘懂了’ alone does not establish that distinction.”
   It ended: “The session is paused.”

6. **Resume, skip, change target:** “继续，但跳过输出计算，改讲第3.2.1节末段的缩放系数。先不要直接告诉我答案，按默认节奏用中文教这个点。”
   Actual excerpt: “我们跳过输出计算，转到缩放系数；之前‘权重与输出的区别’仍保留为已讲解、未验证。”
   It flagged the omitted scaling rationale, labeled `d_k`'s definition as
   background, and gave one invented numerical check.

7. **Correct result, wrong rule:** “结果是2，所以就是把分数除以维度d_k。”
   Actual excerpt: “结果 **2** 是正确的；但你说‘除以维度 d_k’需要修正。公式（1）除的是**维度的平方根**。”
   It contrasted `16/sqrt(64)=2` with `16/64=0.25`, then asked one transfer check.

8. **End:** “结束，不再回答问题。”
   Actual final response: “本次教学结束。你已展示了向量加权求和的计算方法。Attention 权重与输出的区别、Q/K/V 的作用已讲解，但尚未得到回答验证。缩放系数方面，你正确算出 16/√64=2；‘除以 d_k’已纠正为‘除以 √d_k’，该区别仍未验证。提供的片段省略了缩放所针对效应的前文，因此尚未展开其完整理由。”
   Mathematical typesetting is normalized here; no new question was asked.
