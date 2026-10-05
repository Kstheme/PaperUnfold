# Minimal renderer input

Write UTF-8 JSON. All fields below are required; terms and missing lists may be
empty. Keep `source.text` as verbatim material actually read, or a clearly labeled
selection of verbatim passages. Preserve a canonical source URL/path in
`source.name` so teaching can return to the paper. Each quote must occur literally
in that text. Physical PDF page numbers and web section labels must be observed.

```json
{
  "title": "Paper title: reading guide",
  "language": "en",
  "source": {
    "name": "Paper title — canonical URL/path and observed version",
    "text": "Verbatim source passage.",
    "coverage": "Actual sections read; appendix contains selected passages only.",
    "missing": ["Supplementary results were not reviewed."]
  },
  "evidence": [
    {"id": "e1", "location": "Observed section/page", "quote": "Verbatim source passage."}
  ],
  "thread": [
    {"kind": "author", "text": "Qualified main finding.", "evidence": ["e1"]}
  ],
  "sections": [
    {
      "id": "approach", "title": "How does the approach work?",
      "role": "Connect the approach to the research question.",
      "points": [
        {"kind": "inference", "text": "Explanation supported by the passage.", "evidence": ["e1"]}
      ]
    }
  ],
  "terms": [
    {
      "original": "Original term", "name": "Translated term", "essential": true,
      "explanation": {"kind": "background", "text": "Concise definition.", "evidence": []}
    }
  ]
}
```

Use `author`, `inference`, `background` or `analogy`. Author and inference points
need evidence IDs. IDs begin with a letter and contain letters, digits, hyphens
or underscores. Math uses delimiters with JSON escaping, e.g.
`"text": "Scale by \\(1/\\sqrt{d}\\)."`; evidence remains literal text.
Section and term teaching prompts are generated automatically. Add a focused
`learning_goal` only when the title is too vague.

## Central pipeline

Add `visuals` at guide level or inside a section. A `process` has `type`, `title`,
`purpose`, `reading`, `contribution` (each an explanation object), `nodes` and
`edges`. Nodes are `{ "id": "stage", "label": <explanation> }`; edges are
`{ "from": "stage", "to": "next", "relation": <explanation> }`.
Write each label as a stage name plus its input/operation/output, and the relation
as the intermediate artifact passed to the next stage. Source-based explanations
need evidence. Supply nodes in reading order and actual dependencies in edges.
The renderer connects a genuine linear process with visible downward arrows and
relation labels. Branches retain numbered nodes and explicitly directed relations;
it never invents a linear connection from array order alone. This is a teaching
reconstruction, not a reproduced author figure. Use matching stage numbers in
the detailed explanation. Add separate tables/formulas when needed.

Read only the needed part of [guide-format.md](guide-format.md) for a selected
visual payload or labels for languages other than English/Chinese. Omit unused
optional fields; the renderer supplies navigation, folding and copying controls.

The evidence appendix and individual excerpts are collapsed by default. Clicking
an evidence link opens its excerpt and containing appendix before positioning it;
direct fragment URLs work too. Without JavaScript, native disclosure controls
still permit manual expansion. This behavior requires no additional JSON fields.
