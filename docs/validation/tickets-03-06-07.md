# Tickets03/06/07 validation

2026-10-04. Review baseline: `d0b861b`, selected by the user. Three implementation
agents worked in parallel with separate file ownership. Fresh native Codex agents
then exercised actual skill entrypoints. Scripted researcher answers are test
inputs, not evidence of learning efficacy.

## Environment and dependencies

Windows; bundled Python 3.12.14 and pypdf 6.10.0 for PDFs; Python 3.10.9 also
exercised standard-library rendering/progress checks. PDF dependencies are
declared in `skills/paper-guide/requirements.txt` (`pypdf>=6,<7`). The reader has
no OCR. Bundled Poppler was used for original-page visual verification; a host
with equivalent PDF viewing can do that review. Node.js, bundled Playwright and
installed Microsoft Edge were used for isolated artifact checks. Neither Node
nor Playwright is a runtime dependency of the generated guide.

## Ticket03: actual local PDF

The independent reader invoked `paper-guide`, its PDF extractor, and renderer on
the downloaded local [Attention Is All You Need PDF](https://arxiv.org/pdf/1706.03762)
(arXiv:1706.03762v7, 15 physical pages). PDF SHA256:
`bdfaa68d8984f0dc02beaca527b76f207d99b666d31d1da728ee0728182df697`.
The full third-party PDF, full extracted text and full-source HTML remain local
temporary validation artifacts rather than repository-distributed source.

Actual outputs are under `%TEMP%/paperunfold-ticket03-validation/`:
`actual-full-guide.json`, `actual-full-guide.html`, `actual-full-guide-run.md`.
The agent read all 15 text-layer pages and visually inspected PDF pages3–10 and
13–15. The guide has a whole-paper research map, 19 explanatory sections, 13
terms and 42 exact evidence anchors. Method steps connect inputs, projections,
scaled scores, masks, normalized weights and weighted values; training and
evaluation conditions are kept distinct. Physical page positions are labeled
separately from printed numbering verified on inspected pages.

Parent source review checked the actual generated explanations and original
page8. The guide preserves the paper's internal EN-FR BLEU conflict (Table2 41.8,
§6.1 prose 41.0), base versus big training budgets, test versus development
results, complexity conditions, and uncertainty in future-work/visualization
claims. A figure-layer phrase was clarified to “the fifth of six encoder layers”
after review. This illustrates why evidence-anchor validation is paired with
semantic review rather than treated as proof of factual accuracy.

The reader's CUA attempt to navigate a local file URL was denied by its protocol
policy and is recorded as unverified. Separately, the existing public renderer
artifact harness loaded the saved bytes into an isolated offline Edge test page
without local-URL navigation: 65 expansion controls, 144 anchors, 17 math
expressions and 32 teaching prompts passed; no network request or mobile overflow.
This establishes content/control behavior in that test environment, not every
host's local-file-opening policy.

An independent invocation on `synthetic-no-text.pdf` reported absence of usable
text and recovery choices, saved a diagnostic report, and produced no HTML.
Raw extractor exit2 was confirmed; an initial exit1 observation came from its
PowerShell wrapper and was corrected in the run report. Another invocation on
`synthetic-partial.pdf` generated only a one-page excerpt guide, explicitly
reported the second page's text absence and retained “may” plus the small-sample
condition. It did not infer a scan diagnosis, whole-paper map, method or results.
The [partial guide](../../examples/paper-guide/synthetic-partial-guide.html) is
synthetic, not a representative research-paper example. Its nine controls,
eleven anchors and four prompts passed the same offline browser checks.

## Ticket06: actual copying and tutor handoff

The saved excerpt guide supplies chapter/term prompts containing source identity,
observed locations, goals and literal passages. Unlinked short-source terms
include supplied material; unlinked long-source terms ask for relevant material
instead of repeating a full paper. The page makes no model call.

The public browser harness checks selectable fallback, disabled-JavaScript
fallback and clipboard API success with a stub (explicitly not real clipboard
proof). A separate real Edge keyboard Ctrl+C/Ctrl+V check passed for a chapter
and a term. Those pasted prompt values were handed to two fresh actual tutors,
both of which started relevant, source-grounded teaching. See the
[recorded flow](../../examples/paper-tutor/ticket06-07-actual-session.md).
Automatic Clipboard API availability varies by host; the manual text-copy path
is the actually verified fallback. Missing-paper continuation behavior was also
exercised in the source-missing tutor invocation below.

## Ticket07: pause, saved progress and fresh resumption

The copied chapter lesson received a mixed answer: correct weighted calculation
but incorrect identification of the output as weights. After targeted feedback,
the researcher paused without answering the next check. The tutor actually saved
the portable record with exact supporting answer, narrow verified calculation,
unverified distinction, current source/position, open gap and next entry.

A new conversation read that record plus the relevant original passage and
continued the unresolved distinction at its saved question. Another new
conversation received only the record, reported the needed original passage,
and did not substitute the record for paper evidence. It preserved the file.
The [actual progress file](../../examples/paper-tutor/ticket07-actual-progress.json)
and [session record](../../examples/paper-tutor/ticket06-07-actual-session.md)
are separate from the explicitly handcrafted progress-format example.

## Reproduction and limits

From the repository root, use a Python environment with the declared PDF dependency:

```text
python -m pip install -r skills/paper-guide/requirements.txt
python -m unittest discover -s tests -v
python skills/paper-guide/scripts/extract_pdf.py <paper.pdf> --output <material.json>
python skills/paper-tutor/scripts/progress.py resume examples/paper-tutor/ticket07-actual-progress.json --source examples/paper-tutor/ticket07-actual-source.txt
node tests/check_guide_browser.cjs <playwright-module> <browser-executable> examples/paper-guide/agent-invocation-zh.html
node tests/check_handoff_keyboard.cjs <playwright-module> <browser-executable> examples/paper-guide/agent-invocation-zh.html <temporary-prompts.json>
```

The deterministic seams are public commands and saved artifacts; teaching and
source fidelity are assessed through actual invocations and original passages.
Python compilation and Node syntax checks pass; no static typechecker is
configured. Broader field coverage, URL/DOI retrieval, adaptive diagrams, and
verified installation remain later tickets. PDF text-layer coverage alone cannot
prove that an input includes every original page or preserves visual content.
