# Quick-guide workflow change — 2026-10-04

## Subsequent correction: explanation depth and pipelines

The researcher found the first quick guide too shallow. The 4–6 section/word-count
targets and one-visual cap were removed. The default now requires a concise
overview plus complete central mechanism/argument, with stage inputs, operations,
outputs and purpose; principal results and component evidence where supplied.
Method papers require a connected pipeline, with study-design or argument maps
chosen for other disciplines. Time is a checkpoint rather than a truncation rule.
The earlier cached timing below remains historical and does not benchmark the
revised depth requirement.

The renderer now connects actual linear `process` stages with visible downward
arrows and relationship labels. Branching graphs retain explicit numbered
relations rather than fabricating a linear chain. Two acceptance cases verify
edge-order independence and preservation of branch topology.

[Updated FOCUS mechanism guide](../../outputs/focus-v2/mechanism-guide.zh-CN.html)
reuses the previously reviewed version and adds six detailed stages, a connected
pipeline, a local ROI flow and an ablation table. The pasted comparison was used
as a quality example, not as verified paper evidence; it was not copied into the
source appendix. The existing source-version, protocol and reproduction limits
remain in the guide.

Renderer acceptance now passes 22 cases, including the two topology checks.
Actual in-app-browser inspection of the saved updated guide found two connected
pipelines, ten connector arrows, six rendered math expressions, zero math errors,
zero broken local anchors and no horizontal overflow at normal and 390px width.
The method section folded and reopened. Viewport override was reset. The page
has no external script/style/image references; browser network-offline mode and
OS clipboard integration were not newly exercised. The real pipeline screenshot
is saved as `outputs/focus-v2/pipeline-preview.png`.

The researcher reported a 23-minute FOCUS invocation. The prior reading audit
records main-text review, extensive appendix reading, ten page-image inspections,
and repeated browser/clipboard checks. There are no stage timestamps for that
run, so this identifies excess work, not a measured allocation of the 23 minutes.

## Changed default

The skill now delivers a bounded first reading, with deeper topics available on
request. Its entry file owns the scope and time targets. It reuses a readable
body source, reads for the central argument, inspects only objects needed by its
claims, writes a compact JSON guide, renders and delivers. Critical conditions,
counterexamples and source limits remain required. Appendix audits and full
browser regression suites are outside the normal delivery gate.

The short `quick-format.md` supplies the core renderer contract; optional visual
schemas and additional language labels are read only when needed. Deep mode has
its own reference and preserves comprehensive reading on explicit request.

`fetch_remote.py --max-pdf-links 0` keeps HTML without downloading declared PDFs;
`--max-pdf-links 1` bounds a landing-page PDF attempt. The CLI default remains
three links for compatibility. Acquisition limits cannot establish full-text
coverage; title/abstract-only material stays limited.

## Actual checks

- 11 remote-input CLI tests passed over local HTTP: normal acquisition, zero-
  download HTML, one-link stop, failure reports and limited coverage.
- 20 renderer acceptance tests passed: evidence validation, safe content,
  mathematics, visuals and teaching payload generation.
- 3 installation tests passed, including independent installed rendering.
- `git diff --check` passed. No renderer code changed; the browser regression
  suite was not rerun, and this change does not claim fresh browser validation.

## Cached FOCUS check and timing limit

The same conversation's already verified v2 source was reused to author a new
[quick guide](../../outputs/focus-v2/quick-guide.zh-CN.html), with five sections,
nine literal evidence passages and four terms. It retains the V–V/ROI mechanism,
verification distinction, Qwen HRBench-8K improvement, GQA regression and the FP
metric's exclusion of final VQA. The full original guide remains available.

Clock observations from selected cached-source inspection to successful output:
14:03:37–14:04:55 UTC, **78 seconds**. The renderer subprocess took **0.087 seconds**.
The 78 seconds includes this agent's drafting, but excludes source acquisition,
earlier reading/verification, and this implementation turn. It is not a fresh
agent cold-start benchmark, a comparison with equal reading depth, or evidence
of a guaranteed 3–5 minute full invocation. The quick guide was rendered and
validated; its controls were not independently exercised in a browser this time.

Next performance acceptance should time a fresh invocation from user request
through delivery, separately recording acquisition, reading/drafting, render and
optional inspection. Compare factual coverage and errors as well as elapsed
time. Network, source layout and model latency can still exceed the execution
target; essential source verification takes priority over padding a timing claim.
