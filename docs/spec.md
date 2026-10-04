# PaperUnfold: paper guides and guided learning

Date: 2026-10-04. This specification synthesizes the confirmed product decisions. This is the design baseline. Tickets01/02/03/06/07 are now implemented; see [the latest validation record](validation/tickets-03-06-07.md). The user has confirmed the entrypoint-level testing boundary. The ten implementation tickets are published in the local Markdown tracker.

## Problem Statement

Researchers in all disciplines worldwide need to understand research papers quickly without losing the conditions, uncertainty, and reasoning that make the papers meaningful. A dense summary can leave the reader unable to explain what each chapter contributes, how a method or argument works, or why the evidence supports the conclusion.

Explanations can also create new obstacles: inconsistent terminology, unexplained prerequisites, unsupported motives, or a workflow that assumes every paper has experiments, algorithms, and formulas. A reader who has seen an explanation may still have unresolved knowledge gaps.

Researchers need a shared reading method that adapts to each paper, uses their conversation language, keeps explanations traceable to the source, and lets them choose when to go deeper. The first reading experience should be lightweight rather than depend on a lesson, simulation, or video being completed.

## Solution

PaperUnfold provides two independent skills built around a shared paper-reading methodology.

**paper-guide** produces a saveable, single-file HTML reading guide. It presents the whole-paper map, chapter explanations, essential terminology, research logic, and relevant visual explanations. It identifies the material actually read and provides source locations for key explanations. The guide starts with the paper's main thread; background and details appear where they help understanding.

**paper-tutor** teaches a selected chapter, concept, formula, mechanism, or argument through focused dialogue. It can start from the original paper or continue from a guide. It checks only relevant prerequisites, explains when the researcher is stuck, verifies understanding through specific answers, and preserves a concise learning-progress record for later sessions.

The shared method connects the research question, concepts, method or argument, evidence, and conclusion. Each paper's actual content determines the explanation structure. Researchers do not select a discipline template before reading. Explanations follow the conversation language, with explicit language requests taking priority and key terms retaining their original names.

The default experience is a lightweight guide, necessary diagrams, and optional teaching. Small interactive demonstrations are optional when requested or materially useful for a particular mechanism. They do not block the basic guide.

## User Stories

1. As a researcher in any discipline, I want a common paper-reading workflow, so that I can use the same skills across different research topics.
2. As a researcher, I want explanations adapted to the paper's actual research and argument, so that an unrelated experimental or algorithmic template does not distort it.
3. As a researcher, I want to provide a local PDF, so that I can study a paper I already have.
4. As a researcher, I want to provide a paper URL or webpage, so that I can begin with an accessible online source.
5. As a researcher, I want to provide a DOI, so that the agent can try to locate the paper and tell me what it can read.
6. As a researcher, I want to paste a section, so that I can understand a limited part without supplying the whole paper.
7. As a researcher, I want the guide to identify missing or unreadable material, so that I know which parts of the paper were not covered.
8. As a researcher, I want an honest account of an inaccessible source, so that an abstract or metadata record is not presented as a full-paper analysis.
9. As a researcher, I want explanations in my conversation language, so that I can work in the language most useful to me.
10. As a researcher, I want an explicit output-language request to take priority, so that I can change the explanation language when needed.
11. As a researcher, I want key terms to retain their original names, so that I can locate them in the paper and related literature.
12. As a researcher, I want a whole-paper map, so that I can see the core problem, paper structure, and research thread before exploring details.
13. As a researcher, I want each chapter's role explained, so that I can describe how it contributes to the paper.
14. As a researcher, I want links between chapters explained, so that I can follow the path from research question to conclusion.
15. As a researcher, I want the first guide without a prerequisite quiz, so that I can establish the main thread immediately.
16. As a researcher, I want unfamiliar essential terms explained when they affect understanding, so that background repair does not overwhelm the first reading.
17. As a researcher, I want optional terms listed with brief explanations, so that I can choose which ones deserve deeper study.
18. As a researcher, I want term explanations grounded in the paper's context, so that a general definition is not silently attributed to the author.
19. As a researcher, I want research logic separated from detailed method steps, so that I can understand the argument before studying its mechanics.
20. As a researcher, I want executable method steps explained through their actions, conditions, and results, so that I can follow how the method works.
21. As a researcher, I want theoretical or interpretive reasoning explained through premises, support, and inference, so that it is not forced into an execution pipeline.
22. As a researcher, I want figures and formulas explained when they support the main thread, so that I can interpret their purpose and conclusions.
23. As a researcher, I want a paper without relevant figures or formulas explained through its actual evidence, so that the guide does not add empty or invented modules.
24. As a researcher, I want diagrams, tables, and numerical examples chosen for my understanding problem, so that visual complexity serves a clear purpose.
25. As a researcher, I want source locations for key explanations, so that I can check them against the material the agent read.
26. As a researcher, I want numbers, conditions, and uncertainty preserved, so that clearer prose retains the paper's meaning.
27. As a researcher, I want source claims distinguished from background, interpretation, and analogy, so that I can judge which statements the paper supports.
28. As a researcher, I want a single-file HTML guide with navigation and expandable details, so that I can save it and return to the relevant content.
29. As a researcher, I want copyable chapter and term learning prompts, so that I can move from the guide to focused teaching in my agent chat.
30. As a researcher, I want to start teaching directly from a paper, so that I can study an existing question without generating a guide first.
31. As a researcher, I want each teaching round to focus on one main point, so that I can respond without facing a long examination.
32. As a researcher, I want prerequisite checks limited to my chosen question, so that familiar background does not delay useful teaching.
33. As a researcher, I want specific feedback on my answer, so that I know what I understood, omitted, or misunderstood.
34. As a researcher, I want an explanation when I say I do not know, so that the tutor helps me rather than repeatedly asking the same question.
35. As a researcher, I want knowledge gaps repaired before returning to my original question, so that prerequisite teaching remains connected to my goal.
36. As a researcher, I want a knowledge map when it helps orient me, so that I can see concept relationships without repeating the whole map every round.
37. As a researcher, I want to request a direct explanation, skip, change chapters, pause, or stop, so that I retain control of my study.
38. As a researcher, I want explained material distinguished from verified understanding, so that reading a guide or saying I understand is not treated as mastery.
39. As a researcher, I want checks suited to my learning goal, so that I can demonstrate understanding without a fixed question sequence for every concept.
40. As a researcher, I want a concise progress record when I finish a chapter or pause, so that I can continue later from my actual learning state.
41. As a researcher, I want unresolved gaps and the next learning entry preserved, so that a later session can return to the right question.
42. As a researcher, I want optional mechanism interactions with stated assumptions, so that I can explore changes without mistaking teaching values for paper results.
43. As a researcher, I want a static explanation when an interaction cannot be produced reliably, so that the basic reading experience remains usable.
44. As a prospective user, I want English and Chinese project documentation and real examples, so that I can understand the workflow and its current capabilities.
45. As a prospective user, I want verified installation and environment information, so that I can distinguish working support from future plans.
46. As a contributor, I want observable acceptance conditions and source-based examples, so that I can evaluate changes to the skills without asserting a single preferred wording.

## Implementation Decisions

### Skill boundaries

- Deliver two independently invocable skills named paper-guide and paper-tutor, each with its own instructions, necessary reference resources, and examples.
- Share the reading methodology and meaning-preservation principles across both capabilities. Guide generation and teaching remain separate user choices.
- The implementation is an agent-skill project. The HTML guide is an output artifact; teaching runs in the host agent conversation.
- Package the supported invocation and resource requirements after verifying them in the actual host environment. No particular host, model, framework, or dependency has been selected in this conversation.

### Source and explanation contract

- Accept local PDFs, paper links, DOIs, webpages, and pasted sections. Resolve inputs with tools available in the host environment.
- Establish the readable material and coverage before making claims about the paper. A DOI is a locator, not evidence of full-text access.
- When coverage is partial, make the limited scope prominent and explain the available material. When no usable text is available, report the access problem and the material needed to proceed.
- Associate key explanations with real source locations available from the material, such as an observed page, section, figure, or identifiable passage. Preserve location labels rather than inventing pagination.
- Use the paper's context to define terms. Label general background when the paper's intended usage cannot be established.
- Preserve facts, numbers, qualifications, scope, and uncertainty. Keep terminology consistent. Distinguish author statements, supplemental background, explanatory inference, and analogy.
- Follow the conversation language unless the user explicitly selects another language. Retain original names for key terms and source identifiers. Paper input language and explanation language are separate choices.

### Guide contract

- Generate a saveable, single-file HTML reading page with a whole-paper map, chapter roles and connections, term explanations, research logic, source locations, and coverage information.
- Present the research thread and essential explanations first. Offer details through section navigation, term expansion, and content folding.
- Add method steps only when the paper contains a meaningful method or derivation to break down. Explain argumentative reasoning through premises, support, inference, and conclusions.
- Include relevant source figures and formulas when present and useful. Explain their purpose, reading, and contribution to the conclusion. A paper without these elements still receives a complete guide to the readable material.
- Choose teaching visuals according to the question: maps for orientation, flowcharts for process relationships, tables for comparison, and stepwise symbolic or numerical explanations for formulas.
- Provide copyable learning prompts containing the paper source, chapter or term location, and learning goal. They initiate teaching after the researcher copies them into the agent chat; the page does not call a model.
- Optional mechanism demonstrations focus on one understanding problem. State source-derived relationships, teaching assumptions, variable meanings, and applicable ranges. Clearly distinguish constructed teaching values from paper results.
- If an optional demonstration cannot be produced reliably, provide static diagrams or worked steps. Do not hold the basic guide open waiting for an interaction.
- Document any network-dependent resources chosen during implementation. Single-file output is confirmed; complete offline resource independence has not been established as a requirement.

### Teaching and progress contract

- Accept an original paper and a selected chapter or question; an existing guide and progress record are optional context.
- Limit prerequisite checks to the current learning goal. Teach a missing prerequisite and then return to the original question.
- Each ordinary round focuses on one main knowledge point and one main question before waiting for the researcher to answer.
- Give concrete feedback identifying correct understanding, missing elements, misconceptions, and relevant prerequisite gaps.
- Use hints, explanations, and checks as needed. A researcher explicitly saying they do not know receives teaching; a direct-explanation request takes priority over the default questioning style.
- Apply concept, mechanism, relationship, transfer, or teach-back checks according to the current goal. Do not require every concept to pass an identical checklist.
- Maintain the knowledge map and show it at useful moments, such as chapter completion, concept confusion, or an explicit request for an overview.
- Respect requests to explain directly, skip, change chapters, pause, or stop. On exit, record the actual state rather than extending the session to force mastery.
- Record a learning-progress file at chapter completion or pause. It contains the paper source, current learning position, explained content, understanding supported by specific answers, unresolved gaps, and the next learning entry. It supplements the HTML guide rather than replacing it.
- A later session can use that record to continue. It still needs readable source material for source-grounded explanations; progress is not a substitute for the original paper.

### Documentation and release

- Use PaperUnfold as the project name, with English and Chinese README versions. Keep both versions aligned on behavior and implementation status.
- Produce representative real-paper examples covering different research and argument structures, including an algorithm paper, an empirical study, and a theoretical or humanities argument. Include English and Chinese outputs.
- Record each example's source, coverage, output language, and generation environment. Publish real HTML results and screenshots after implementation.
- Validate installation instructions and platform claims before presenting them as supported. Record actual reading dependencies, resource requirements, and failure behavior.
- Retain the original teaching prompt as source material for comparison. The confirmed product behavior takes priority where the original prompt differs, particularly on guide generation and the researcher's right to stop.
- The referenced ASD-STE100 skill supplies design inspiration rather than a runtime dependency. Meaning-preserving explanation and consistent terminology do not amount to certified STE compliance or proof of factual correctness.

## Testing Decisions

### Confirmed boundary

Use one shared scenario-based acceptance approach at the actual skill-invocation boundary. Invoke either skill with source material and, for teaching, a sequence of researcher replies; inspect the user-visible artifact, dialogue, and progress record. A guide-to-teaching-to-resumption scenario exercises their combined behavior through the same external boundary.

The user confirmed acceptance through actual inputs and visible results on 2026-10-04. At specification time there was no implementation or test harness. The current implementation has public CLI/artifact checks plus actual agent-invocation validation; the confirmed boundary remains inputs and visible results rather than internal prompt wording.

### What makes a good test

- Assert behavior observable by a researcher: coverage, source traceability, artifact usability, specific feedback, user control, and truthful progress.
- Use readable source fixtures and retain the passages supporting expected claims. Review generated explanations against those passages, including conditions and uncertainty.
- Combine deterministic artifact checks with source-grounded human evaluation. HTML structure alone cannot prove explanation accuracy, and an agent's self-evaluation is not sufficient evidence of factual fidelity.
- Test capabilities and outcomes rather than exact generated wording, internal prompts, model reasoning, or a preferred rendering implementation.
- Keep teaching scenarios focused on externally distinguishable behavior. Prewritten researcher replies are test inputs, not evidence that an actual user mastered a topic.

### Acceptance scenarios

| Scenario | Observable acceptance |
| --- | --- |
| Full readable paper | Guide identifies the source and coverage, explains chapter roles and the research thread, and ties key claims to real source locations. |
| Partial chapter or abstract | Output describes only the available material, identifies missing coverage, and avoids implying a full-paper reading. |
| Inaccessible DOI or unreadable PDF | Agent reports the access or readability limit; metadata is not substituted for a completed full-paper explanation. |
| Empirical research | Explanation follows the actual design and evidence, preserving conditions and avoiding unsupported causal upgrades. |
| Theory or argumentative paper | Explanation connects premises, reasoning, support, and conclusions; executable method steps and numerical experiments are not forced into the output. |
| Paper without relevant figures or formulas | Guide explains the actual research and argument without fabricated visuals, formulas, or empty required sections. |
| Language selection | Same source can be explained in the conversation language and an explicitly requested alternative, while original terms and source locations remain recognizable. |
| Meaning preservation | Check selected claims, numbers, qualifiers, and inferred motives against the source; background, analogy, and inference are distinguishable. |
| HTML navigation and prompts | Saved page opens; provided navigation, term expansion, folding, and prompt copying work; copied prompts identify the source, target, and learning goal. |
| Direct teaching entry | Tutor starts from a readable paper and a chosen question without requiring a previously generated guide. |
| Knowledge gap or incomplete answer | Tutor gives specific feedback, repairs relevant prerequisites when needed, and returns to the original question. |
| Researcher says they do not know | Tutor provides teaching and an appropriately small check instead of an indefinite sequence of repeated questions. |
| Researcher changes or ends the session | Direct explanation, skip, chapter change, pause, and stop are honored. Ending does not imply mastery. |
| Progress and resumption | Record separates explained from answer-supported understanding, preserves unresolved gaps, and provides a usable continuation entry. A later session does not invent mastery or unavailable source details. |
| Optional mechanism demonstration | Demonstration states relationships and assumptions, distinguishes teaching values from results, and does not block the basic guide when unavailable. |
| Release documentation | English and Chinese README status agrees with implemented capabilities; listed installation paths and environments have been exercised. |

A release should include real-paper guide evaluations across the chosen argument structures, source-fidelity review, artifact usability checks, and teaching/resumption scenarios. Results and environment limits should be recorded. Existing examples are not evidence of all-discipline validation.

## Out of Scope

- A hosted research platform, in-page model calls, accounts, billing, or a new backend service.
- Mandatory discipline selection or a separate prescribed teaching workflow for every discipline.
- Prerequisite examinations before initial guide generation.
- Mandatory simulations, parameter experiments, animations, videos, or TeX reports for every paper.
- Full mathematical derivations or reproduction-level detail in every initial guide. These remain possible directions for requested deeper teaching.
- Mandatory bilingual paragraph alignment in the default guide.
- A literature-search service, reference manager, publication strategy, or formal peer-review product as additional project capabilities.
- Forced mastery before allowing the researcher to end a session.
- Automatic claims of factual correctness, formal STE certification, or validated performance in every discipline.
- Guaranteed star growth, unmeasured reading-time reductions, or unmeasured learning outcomes.
- Renaming a local checkout or remote repository as part of writing this specification.

## Further Notes

The confirmed design and domain vocabulary are documented in the [design](design.md) and [glossary](../CONTEXT.md). This specification organizes their implementation behavior and acceptance requirements. The [project review](project-review.md) records naming, positioning, and publication priorities.

The current checkout contains runnable instruction packages for guides and teaching; local PDF reading, HTML teaching prompts, and progress save/resume are implemented. The implementation order is guide and template, teaching and progress, representative examples, then verified release documentation and a comparison using the same source material.

Implementation work must establish and document the supported agent environment, reading dependencies, HTML resource choices, and license. The validation records identify the concrete choices already exercised; broader host installation remains a later ticket.

The user invoked to-spec, which includes publishing the specification to the project issue tracker with the ready-for-agent label. The user subsequently selected local Markdown tracking, and the ten tickets were published under `.scratch/paperunfold/`. This checkout has no configured Git remote; no remote issue publication is claimed. Remaining optional tracker-label configuration is noted in the task index.
