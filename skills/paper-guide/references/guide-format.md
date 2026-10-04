# Guide input

The renderer consumes UTF-8 JSON. All content is plain text. Agent-authored explanations should follow the selected output language; the renderer does not translate them.

```json
{
  "title": "Reading guide: supplied passage",
  "language": "en",
  "source": {
    "name": "Paper title or user-provided passage",
    "text": "The supplied paper text, verbatim.",
    "coverage": "Only the supplied passage was read.",
    "missing": ["The remaining sections were not provided."]
  },
  "evidence": [
    {"id": "e1", "location": "Pasted paragraph 1", "quote": "supplied paper text"}
  ],
  "thread": [
    {"kind": "author", "text": "An explanation supported by the source.", "evidence": ["e1"]}
  ],
  "sections": [
    {
      "id": "section-1", "title": "Passage explanation",
      "role": "What this passage contributes to the research thread.",
      "points": [
        {"kind": "inference", "text": "A grounded reading of the argument.", "evidence": ["e1"]}
      ]
    }
  ],
  "terms": [
    {
      "original": "original term", "name": "Name in output language",
      "essential": true,
      "explanation": {"kind": "background", "text": "A supplemental definition.", "evidence": []}
    }
  ]
}
```

Use `author`, `background`, `inference`, or `analogy` for each explanation's `kind`. Author statements and inferences need at least one evidence ID. Background and analogy may have none. An evidence excerpt must occur literally in `source.text`; preserve the text rather than normalize or reconstruct it. Evidence anchors let the reader see both the stated locator and excerpt. A matching excerpt does not certify that the explanation follows from it. Review the actual claim-to-evidence relationship separately.

All fields above are required, except `labels`. Lists of missing material and terms can be empty. Include at least one research-thread point, evidence excerpt, section, and section point. Section roles are editorial explanations, visibly marked as inference. Section IDs must start with a letter and contain only letters, digits, hyphens, or underscores. Evidence IDs use the same pattern. Generated HTML namespaces the IDs to avoid collisions.

For an explicit output language other than English or Chinese, provide the complete `labels` object below, translated into that language. English and Chinese default labels can also be overridden. Original term names and source locators remain recognizable.

```json
{
  "labels": {
    "coverage": "Coverage", "missing": "Not covered", "thread": "Research thread",
    "contents": "Contents", "terms": "Terms", "evidence": "Source passages",
    "source": "Supplied text", "role": "Role / explanatory inference",
    "essential": "Essential", "optional": "Optional", "author": "Author statement",
    "background": "Background", "inference": "Inference", "analogy": "Analogy"
  }
}
```

Keep the page proportionate to the source: essential definitions are visible by default, optional definitions are collapsed, and section details remain expandable. The source appendix preserves material for checking and does not imply full-paper coverage.
