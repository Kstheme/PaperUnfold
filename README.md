# PaperUnfold

**Unfold research papers into clear, visual guides.**

[English](README.md) · [简体中文](README.zh-CN.md)

PaperUnfold develops a shared paper-reading methodology for researchers in all disciplines worldwide. It adapts explanations to each paper's research question, argument, methods, and evidence. The experience starts with a lightweight HTML guide, then offers focused teaching when you want to go deeper.

**Status: first two tickets implemented.** Pasted-text HTML guides and independent conversational teaching are available. PDF/URL ingestion, persistent learning progress, and verified installation remain on the roadmap. See the [validation record](docs/validation/tickets-01-02.md).

## Reading experience

1. Provide a pasted paper section. Local PDFs, URLs, and DOI retrieval are planned.
2. Get a single-file HTML guide with a map of the supplied material, section explanations, essential terms, and relevant diagrams.
3. Check key explanations against locations in the source paper.
4. Choose a chapter, formula, or question for guided learning in your agent chat.

Explanations follow your conversation language unless you request another language. Key terms retain their original names. A DOI helps locate a paper; the guide covers only the material the agent can actually read.

The guide starts with the paper's main thread and adds background where it helps understanding. You do not need to choose a discipline template or take a knowledge check before getting a guide. Focused teaching checks the prerequisites needed for your chosen question.

## Two independent skills

| Skill | When to use it | Output |
| --- | --- | --- |
| `paper-guide` | You need the big picture and the path from question to conclusion. | A lightweight HTML reading guide. |
| `paper-tutor` | You want to understand a specific concept, mechanism, or argument. | Focused teaching in the current conversation. |

You can start teaching directly from a paper. Generating a guide first is optional. Teaching happens in your agent chat. HTML teaching prompts and cross-session progress files are planned.

## Try the current skills

In an agent with filesystem and command access, explicitly ask it to read [paper-guide](skills/paper-guide/SKILL.md) or [paper-tutor](skills/paper-tutor/SKILL.md), then supply readable paper text. The guide renderer requires Python 3.10+; it uses only the standard library. A skill is an instruction package for your agent, not a standalone paper-analysis command.

Example requests:

- “Use the paper-guide skill in this repository. Explain this pasted section in English and save the HTML guide.”
- “Use paper-tutor with this pasted section. Help me understand how the evidence supports the conclusion.”

Open the [actual Chinese agent-generated guide](examples/paper-guide/agent-invocation-zh.html), inspect its [source and renderer input](examples/paper-guide/agent-invocation-zh.json), or read the [recorded tutor checks](examples/paper-tutor/actual-session.md). These are checks on a short attention excerpt; broader discipline examples belong to ticket09. Agent discovery and installation differ by host and remain to be verified in ticket10.

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
- [ ] Implement persistent learning progress and resumption.
- [ ] Publish examples covering an algorithm paper, an empirical study, and a theoretical or humanities argument, including English and Chinese outputs.
- [ ] Add real output screenshots, source references, verified installation steps, and a license.
- [ ] Publish a short comparison of a conventional text explanation and a PaperUnfold guide using the same source material.

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
