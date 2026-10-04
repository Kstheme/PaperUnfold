# PaperUnfold

**Unfold research papers into clear, visual guides.**

[English](README.md) · [简体中文](README.zh-CN.md)

PaperUnfold develops a shared paper-reading methodology for researchers in all disciplines worldwide. It adapts explanations to each paper's research question, argument, methods, and evidence. The planned experience starts with a lightweight HTML guide, then offers focused teaching when you want to go deeper.

**Status: design stage.** The design is documented. The skills, HTML template, installation instructions, and real-paper demos have not been implemented yet.

## The planned reading experience

1. Provide a local PDF, paper URL, DOI, webpage, or pasted section.
2. Get a single-file HTML guide with a paper map, chapter explanations, essential terms, and relevant diagrams.
3. Check key explanations against locations in the source paper.
4. Choose a chapter, formula, or question for guided learning in your agent chat.

Explanations follow your conversation language unless you request another language. Key terms retain their original names. A DOI helps locate a paper; the guide covers only the material the agent can actually read.

The guide starts with the paper's main thread and adds background where it helps understanding. You do not need to choose a discipline template or take a knowledge check before getting a guide. Focused teaching checks the prerequisites needed for your chosen question.

## Two independent skills

| Planned skill | When to use it | Output |
| --- | --- | --- |
| `paper-guide` | You need the big picture and the path from question to conclusion. | A lightweight HTML reading guide. |
| `paper-tutor` | You want to understand a specific concept, mechanism, or argument. | Focused teaching and a resumable learning-progress file. |

You can start teaching directly from a paper. Generating a guide first is optional. The HTML page provides copyable teaching prompts; teaching happens in your agent chat.

## Design principles

- **Start with the research logic.** Explain what each chapter contributes and how the evidence connects to the conclusion. Adapt the explanation to the paper's research and argument; include method steps, figures, or formulas where relevant.
- **Choose visuals for the question.** Use flowcharts for processes, tables for comparisons, and stepwise explanations for formulas.
- **Keep the first pass light.** Put essential explanations first and reveal details as needed. Interactive experiments are optional, used when requested or when they materially help explain a mechanism.
- **Keep explanations traceable.** Preserve numbers, conditions, and uncertainty. Distinguish source claims from background, interpretation, and analogy.
- **Teach without trapping the reader.** Identify knowledge gaps, explain when needed, and check understanding through specific answers. You can ask for a direct explanation, skip, pause, or stop.

## Roadmap

- [x] Define the audience, reading workflow, language policy, and teaching principles.
- [ ] Implement `paper-guide` and its HTML template.
- [ ] Implement `paper-tutor` and the learning-progress format.
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
