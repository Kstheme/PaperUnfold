# Pasted attention excerpt example

Source: `tests/fixtures/attention-excerpt.txt`, a fixture containing two short quotations and a transcription of Equation (1) from Vaswani et al., *Attention Is All You Need*, arXiv 1706.03762v7, Sections 3.2 and 3.2.1. Surrounding context is deliberately absent. The guide explains the supplied excerpt in Chinese and preserves the missing-context limit.

`attention-excerpt-guide.json` is a manually authored renderer example, not a recorded independent agent invocation. `attention-excerpt-guide.html` is its renderer output. Run from the repository root with Python 3.10+:

```text
python skills/paper-guide/scripts/render_guide.py examples/paper-guide/attention-excerpt-guide.json --output examples/paper-guide/attention-excerpt-guide.html
python -m unittest discover -s tests -p test_paper_guide.py
```

Source review: the formula, the factor `1/sqrt(d_k)`, and the weighted-sum description have literal excerpt anchors. The cause of scaling is withheld because the referenced effect is absent. General definitions and the analogy are labeled separately. No full-paper results, page numbers, or learner mastery are claimed.

The deterministic suite checks saved output, anchor integrity, native expansion controls, language tags, escaping, rejection of untraceable evidence, and offline math asset inclusion. It cannot prove explanation accuracy or actual browser behavior. Independent skill invocation and browser operation checks are recorded in [the validation report](../../docs/validation/tickets-01-02.md). Both examples now use delimited LaTeX in explanations and embedded KaTeX for offline rendering; source text and quotations remain verbatim.
