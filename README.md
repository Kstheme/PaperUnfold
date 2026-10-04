# PaperUnfold

**Unfold research papers into clear, visual guides.**

[English](README.md) · [简体中文](README.zh-CN.md)

PaperUnfold develops a shared paper-reading methodology for researchers in all disciplines worldwide. It adapts explanations to each paper's research question, argument, methods, and evidence. The experience starts with a lightweight HTML guide, then offers focused teaching when you want to go deeper.

**Status: tickets01–10 implemented.** Generate source-grounded HTML guides from pasted text, local PDFs, accessible webpages, online PDFs and DOI locators; teach directly or from copied guide prompts; save and resume progress with readable source. Optional interaction is limited to a bounded softmax teaching example. Fresh local installation has been exercised in Codex desktop on Windows with explicit installed-entry invocation. CLI and other platforms remain unverified. See [installation](docs/installation.md) and [first-use validation](docs/validation/ticket-10.md).

## Reading experience

1. Provide a pasted paper section, local PDF, accessible webpage, online PDF, or DOI.
2. Get a single-file HTML guide with a map of the supplied material, section explanations, essential terms, and relevant diagrams.
3. Check key explanations against locations in the source paper.
4. Choose a chapter, formula, or question for guided learning in your agent chat.

Explanations follow your conversation language unless you request another language. Key terms retain their original names. A DOI helps locate a paper; the guide covers only the material the agent can actually read.

The guide starts with the paper's main thread and adds background where it helps understanding. You do not need to choose a discipline template or take a knowledge check before getting a guide. Focused teaching checks the prerequisites needed for your chosen question.

## Two independent skills

| Skill | When to use it | Output |
| --- | --- | --- |
| `paper-guide` | You need the big picture and the path from question to conclusion. | A lightweight HTML reading guide. |
| `paper-tutor` | You want to understand a specific concept, mechanism, or argument. | Focused teaching and a portable learning-progress file. |

You can start teaching directly from a paper. Generating a guide first is optional. Teaching happens in your agent chat. Copy a chapter or term prompt from the HTML guide, or start directly from the original paper. At chapter completion or pause, the tutor saves a progress record. Supply that record and readable source text in a new conversation to resume; the record does not replace paper evidence.

## Install and try

From the checkout root in PowerShell, install into your chosen sibling project:

```powershell
python -m venv ..\my-paper-project\.venv
& ..\my-paper-project\.venv\Scripts\python.exe -m pip install -r skills/paper-guide/requirements.txt
& ..\my-paper-project\.venv\Scripts\python.exe scripts/install_skills.py --dest ..\my-paper-project\.agents\skills
```

Append `--skill paper-guide` or `--skill paper-tutor` for an independent installation. Existing packages are preserved: the installer refuses to overwrite them. Open the target project in Codex and explicitly ask it to read `.agents/skills/paper-guide/SKILL.md` or `.agents/skills/paper-tutor/SKILL.md`; use that project's `.venv/Scripts/python.exe` when needed. The [bilingual installation guide](docs/installation.md) covers teaching, fresh-conversation resumption, dependencies and failure alternatives.

Verified: Codex desktop Agent on Windows, Python 3.12.14 and pypdf 6.19.0, with explicit entry-file invocation. A blocked Codex CLI invocation did not verify automatic discovery or CLI first use. Other hosts and operating systems are unverified. HTML generation and text teaching helpers use Python 3.10+ standard library; PDF extraction additionally needs pypdf 6.x and performs no OCR. Figures and equations need source-page inspection. URL acquisition requires network access and does not sign in or execute webpage JavaScript; abstract-only material produces a limited guide. Saved HTML embeds math assets and needs no network. Without JavaScript, notation and static/keyboard alternatives remain visible. Skills are instruction packages for your Agent, not standalone paper-analysis commands.

Example requests:

- “Read the installed .agents/skills/paper-guide/SKILL.md and follow it. Explain this paper URL, DOI, pasted section, or local PDF in English and save the HTML guide.”
- “Read the installed .agents/skills/paper-tutor/SKILL.md and follow it with this pasted section. Help me understand how the evidence supports the conclusion.”

Open the [actual Chinese agent-generated guide](examples/paper-guide/agent-invocation-zh.html), inspect its [source and renderer input](examples/paper-guide/agent-invocation-zh.json), or read the [recorded tutor checks](examples/paper-tutor/actual-session.md). See the [actual paused progress](examples/paper-tutor/ticket07-actual-progress.json) and [guide-to-teaching-to-resumption record](examples/paper-tutor/ticket06-07-actual-session.md).

Adaptive validation examples use selected source excerpts: [Attention calculation steps](examples/paper-guide/adaptive-method-zh.html), [empirical survey evidence](examples/paper-guide/adaptive-empirical-zh.html), and a theoretical model in [Chinese](examples/paper-guide/adaptive-theory-zh.html) and [English](examples/paper-guide/adaptive-theory-en.html). Their [source notes](examples/paper-guide/adaptive-source-notes.md) record coverage and attribution. These excerpt examples validate different reasoning structures. The [release examples](examples/release09/README.md) add whole-main-paper reading guides: an algorithm paper in Chinese, an empirical study in English, and a theoretical argument in English and Chinese. They include real screenshots, source audits, scripted researcher inputs to actual tutor sessions, saved progress and fresh-session resumption, and a [same-passage comparison](examples/release09/conventional-comparison.md). These cases do not establish quality across every discipline or measure learning gains. The [fresh-install examples](examples/first-use10/README.md) add a local PDF guide, a live DOI guide, keyboard copying and independently installed tutoring; see their source and actual screenshot.

The [optional mechanism examples](examples/mechanism08/run.md) show a [bounded softmax temperature experiment](examples/mechanism08/attention-guide.html) with explicit teaching values and a [static empirical explanation](examples/mechanism08/empirical-guide.html) where a requested probability predictor is unsupported by the source. Other mechanisms receive source-guided static explanations; arbitrary interactive simulations are not implemented.

## Design principles

- **Start with the research logic.** Explain what each chapter contributes and how the evidence connects to the conclusion. Adapt the explanation to the paper's research and argument; include method steps, figures, or formulas where relevant.
- **Choose visuals for the question.** Use flowcharts for processes, tables for comparisons, and stepwise explanations for formulas.
- **Keep the first pass light.** Put essential explanations first and reveal details as needed. Interactive experiments are optional, used when requested or when they materially help explain a mechanism.
- **Keep explanations traceable.** Preserve numbers, conditions, and uncertainty. Distinguish source claims from background, interpretation, and analogy.
- **Teach without trapping the reader.** Identify knowledge gaps, explain when needed, and check understanding through specific answers. You can ask for a direct explanation, skip, pause, or stop.

## Roadmap

- [x] Define the audience, reading workflow, language policy, and teaching principles.
- [x] Implement `paper-guide` for pasted text and its HTML renderer.
- [x] Implement independent `paper-tutor` teaching.
- [x] Read local PDFs with page provenance and explicit extraction gaps.
- [x] Acquire accessible webpages, online PDFs, and DOI-linked material with explicit coverage and access limits.
- [x] Adapt research-logic explanations and optional visuals to methods, empirical evidence, and theoretical arguments.
- [x] Copy chapter/term teaching prompts from HTML.
- [x] Save learning progress and resume with source material.
- [x] Publish representative release examples combining guides, teaching, and resumption across an algorithm paper, an empirical study, and a theoretical or humanities argument, including English and Chinese outputs.
- [x] Add real output screenshots and source references.
- [x] Provide an optional bounded mechanism demonstration with a static fallback.
- [x] Verify local installation, explicit invocation in Codex desktop on Windows, first use and licensing (ticket10).
- [x] Publish a short comparison of a conventional text explanation and a PaperUnfold guide using the same source material.

## Inspiration

The project draws on clear technical writing and the idea of making custom visual artifacts to help readers understand complex material. See [Karpathy's discussion](https://x.com/karpathy/status/2105819303471976479) and [asd-ste100-skill](https://github.com/danyuchn/asd-ste100-skill).

PaperUnfold applies consistent terminology, explicit actors, and meaning-preserving explanations. It is an independent project; `asd-ste100-skill` is a design reference, not a runtime dependency.

## Project documents

- [Implementation tickets](.scratch/paperunfold/README.md): 10 approved tasks, their dependencies, and acceptance criteria.
- [Implementation specification](docs/spec.md): user stories, behavior contracts, and acceptance scenarios.
- [Design](docs/design.md): confirmed scope, guide structure, teaching workflow, and output checks (Chinese).
- [Glossary](CONTEXT.md): shared domain terms (Chinese).
- [Project review](docs/project-review.md): confirmed positioning and release priorities (Chinese).
- [Original teaching prompt](docs/source/socratic-ddd-prompt.txt): source material retained for comparison. The design document defines the intended behavior.

## License and contributions

Original project code, skills and documentation use [MIT](LICENSE). Papers and bundled KaTeX retain their own [licenses and attribution](THIRD_PARTY_NOTICES.md). See [contribution acceptance steps](CONTRIBUTING.md).
