# Ticket10: installation and first-use acceptance

Date: 2026-10-04. Review baseline: `df6f093120108c738bd2d9d6fdc2423af4ae5b38`, confirmed by the user. The user selected MIT. No remote repository or public release was created by this ticket.

## Fresh environment

An empty project outside the source checkout was initialized at `C:/Users/34220/AppData/Local/Temp/paperunfold-first-use-89xtswd6`. Python 3.12.14 created a virtual environment without system site packages. Initially `import pypdf` failed with ModuleNotFoundError. Installing the guide requirements downloaded pypdf 6.19.0. `scripts/install_skills.py` then copied both complete packages into that project's `.agents/skills`; a separate `independent/.agents/skills` contained only paper-tutor. The installer was also exercised through independent guide/tutor public-command tests and an existing customization collision.

Actual successful host: **Codex desktop Agent on Windows, PowerShell**, explicitly reading and following installed entry files and using the fresh Python executable. This current implementation Agent performed the guide and initial teaching cases; these were not an external CLI model run. No user-wide skill directory or Agent configuration was changed. Global installation and automatic host discovery are not claimed as validated.

Codex CLI 0.154.0 was separately attempted. The authenticated account rejected gpt-6.1-sol, gpt-5.4 and gpt-5.3-codex before content generation. These failed attempts do not establish CLI compatibility. Account credentials were not inspected or published; only the model-support failure is recorded. Other operating systems and hosts remain unverified.

## Visible first-use cases

| Case | Observed result |
| --- | --- |
| Local PDF | Installed extractor read the six physical pages of the original 2005 Ioannidis PDF. The Agent selected the baseline model on pages 1–2, inspected original page 1 with Poppler and rendered a Chinese guide using the installed package. Table 1, later extensions and correction excluded explicitly. |
| Live DOI | Installed HTTP helper requested DOI10.1371/journal.pmed.0020124, followed the publisher route and obtained its readable printable PDF. Retrieval: 2026-10-04T20:52:31+08:00. The selected text matched the local PDF; the Agent rendered an English guide of the same scoped model. |
| Copy to teaching | Real Edge Ctrl+C / Ctrl+V copied a chapter and a term prompt. The Agent followed installed paper-tutor using the copied chapter goal and a scripted direct-explanation/pause request. It explained odds versus probability and saved paused-progress.json without asserting mastery. |
| Direct teaching | The tutor was installed separately with no guide package. A scripted direct PPV request used readable paper text without generating or requiring a guide. The direct-entry record preserved explained_unverified. |
| Resume helper | The installed progress helper loaded paused-progress.json together with source.txt, preserving the position and unverified status. Fresh-Agent resumption is checked separately during the specification review; a helper success alone is not fresh-conversation teaching evidence. |

The [published artifacts](../../examples/first-use10/README.md) include two actual HTML files and renderer inputs, source text, provenance, real screenshot, copied prompts and actual Agent-authored teaching responses. Researcher inputs are scripted acceptance requests; no human learning-gain measurement or answer-supported mastery is claimed. The original paper retains its stated Creative Commons Attribution terms. The current model equation was checked against page 1: R−βR+α was reformatted algebraically to (1−β)R+α; evidence quotes retain extraction glyphs and line breaks.

## Browser checks

Edge through installed Playwright, offline: both final saved guides rendered six KaTeX expressions without errors or source-text transformation; nine expansion controls, twenty-one evidence/navigation anchors, four teaching prompts, no network requests or mobile overflow. Clipboard fallback and no-JavaScript keyboard alternatives passed. The clipboard-API success branch is a stub test; real copy/paste is established separately by the keyboard check. The actual screenshot was inspected.

## Installation and release surface

English and Chinese README share install commands, capacity and verified-host limits. The bilingual installation document records Python/PDF dependencies, online access requirements, offline embedded KaTeX, no-JavaScript alternatives, reading failures and unsaved-file fallback. MIT covers original project work; KaTeX and papers retain notices in THIRD_PARTY_NOTICES.md. CONTRIBUTING.md specifies public-input/output tests, original-source review and a real fresh-install acceptance path. ASD references are independent of runtime. Optional interaction remains the implemented bounded softmax demonstration; arbitrary simulations are unsupported.

The public installer tests observed failures before the first independent installation implementation and before collision preflight was added, then passed after the corresponding fixes. The guide asset test protects package self-containment. Syntax checks passed during implementation. The complete suite passed **42 tests** under the fresh Python/pypdf environment. Both skill validators passed with Python UTF-8 mode (the first Anaconda default-GBK invocation failed to decode UTF-8 instructions). The two-axis review is recorded after final checks.
