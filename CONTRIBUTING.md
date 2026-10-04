# Contributing

Keep the two skills independent. Changes should preserve paper evidence, conversation-language explanations, researcher controls and honest coverage. Read [the specification](docs/spec.md) and the relevant [local ticket](.scratch/paperunfold/README.md) before changing behavior.

Verify observable behavior through skill inputs, saved artifacts, teaching feedback and portable progress. Do not test internal prompt wording as a substitute for behavior. For code changes, add a regression at the relevant public command boundary when it protects a meaningful failure.

From the checkout root, use Python 3.10+ with the PDF requirement installed:

```powershell
python -m pip install -r skills/paper-guide/requirements.txt
python -m unittest discover -s tests -v
git diff --check
```

For installation changes, start in an empty project and virtual environment. Run [the installation steps](docs/installation.md); check separate `--skill` installations, existing-package preservation, local PDF and live online material. Ask a working Agent to follow the installed entry files, generate a guide, copy a chapter prompt into teaching, start teaching directly without a guide, pause/save, and resume from the record plus source in a fresh conversation. Record the host, versions, source route, actual coverage and any skipped or failed step. A helper test alone does not establish Agent compatibility.

For HTML changes, open the actual saved output offline and check navigation, expansion, math, mobile overflow and clipboard fallback. The optional browser checks accept your own installed Playwright module and browser executable; they are QA dependencies, not skill runtime dependencies:

```text
node tests/check_guide_browser.cjs <playwright-module> <browser-executable> <guide.html>
node tests/check_handoff_keyboard.cjs <playwright-module> <browser-executable> <guide.html> <copied-prompts.json>
```

The first script exercises a simulated clipboard-success branch and fallback; the second performs real keyboard copy/paste. Check factual explanations separately against the original source, including quantities, assumptions, version and visual notation. Scripted learner inputs are acceptable for behavior checks, but label them; they do not demonstrate human learning gains. Preserve unverified understanding unless a substantive answer supports the specific learning point.

Include a concise validation record and relevant source provenance with your change. Run a review against a fixed starting commit along standards and specification axes, then address actionable findings. Do not claim an untested platform, host or arbitrary interactive mechanism.

Original contributions are under the project's [MIT license](LICENSE). Preserve [third-party notices](THIRD_PARTY_NOTICES.md), paper attribution and applicable reuse terms. Do not add full copyrighted papers or private account logs as fixtures. ASD references remain optional design references.

中文贡献者可先阅读[双语安装说明](docs/installation.md)、[规格](docs/spec.md)与[任务索引](.scratch/paperunfold/README.md)。验收实际输入与可见结果；标记脚本化学习者输入；原文、公式与许可需要独立核验。新增代码采用 MIT，论文等材料保留自身许可。
