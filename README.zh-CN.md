# PaperUnfold

**把论文的逻辑展开，把难懂的地方讲清楚。**

[English](README.md) · [简体中文](README.zh-CN.md)

PaperUnfold 基于一套通用论文阅读方法，面向全球各学科研究人员，根据每篇论文的研究问题、论证、方法与证据调整讲解。阅读体验先提供轻量 HTML 导读，再按需通过对话深入学习。

**ticket01–10 已实现。** 支持粘贴原文、本地 PDF、可访问网页、在线 PDF 与 DOI 定位材料生成有原文依据的 HTML 导读；可直接教学或复制导读提示词进入教学，并结合可读原文保存、续接进度。可选交互仅为限定范围的 softmax 教学示例。已在 Windows 的 Codex 桌面 Agent 中完成全新本地安装与明确读取已安装入口的调用验收。CLI 与其他平台尚未验证。见[安装说明](docs/installation.md)和[首次使用验收](docs/validation/ticket-10.md)。

## 阅读体验

1. 粘贴论文章节，或提供本地 PDF、可访问网页、在线 PDF 或 DOI。
2. 获得单文件 HTML 导读：所提供材料的地图、章节解释、必需术语和必要图示。
3. 根据原文位置核对关键解释。
4. 选择一个章节、公式或问题，在 Agent 对话中深入学习。

讲解默认跟随用户的对话语言，用户可以指定其他语言。关键术语保留原文名称。DOI 用于定位论文，导读只覆盖实际读取到的材料。

导读直接呈现论文主线，在有助于理解时补充背景。用户无需先选择学科模板或接受基础知识测试。深入教学时，再检查当前问题必需的前置知识。

## 两个独立 Skill

| 能力 | 使用场景 | 输出 |
| --- | --- | --- |
| `paper-guide`：论文导读 | 先了解全貌，讲清从研究问题到结论的路径。 | 轻量 HTML 阅读页面。 |
| `paper-tutor`：论文教学 | 深入理解一个概念、机制或论证。 | 聚焦问题的教学与可携带的学习进度文件。 |

教学可以直接从原论文开始，也可以接续导读。教学在 Agent 对话中进行。可以复制 HTML 中的章节或术语提示词，也可以直接从原文开始。章节结束或暂停时保存进度；在新对话中提供进度和可读原文即可续学，进度记录不能代替论文证据。

## 安装与试用

在仓库根目录打开 PowerShell，安装到选定的相邻项目：

```powershell
python -m venv ..\my-paper-project\.venv
& ..\my-paper-project\.venv\Scripts\python.exe -m pip install -r skills/paper-guide/requirements.txt
& ..\my-paper-project\.venv\Scripts\python.exe scripts/install_skills.py --dest ..\my-paper-project\.agents\skills
```

只安装一个技能时，加 `--skill paper-guide` 或 `--skill paper-tutor`。安装器拒绝覆盖已有包，保留定制内容。在 Codex 打开目标项目，明确要求读取 `.agents/skills/paper-guide/SKILL.md` 或 `.agents/skills/paper-tutor/SKILL.md`；必要时指定该项目的 `.venv/Scripts/python.exe`。[双语安装说明](docs/installation.md)包含教学、新对话续学、依赖与失败替代路径。

已验证环境为 Windows 的 Codex 桌面 Agent、Python 3.12.14、pypdf 6.19.0，采用明确读取入口文件的调用。Codex CLI 调用被模型兼容错误挡住，未验证自动发现或 CLI 首次使用。其他宿主与系统未验证。HTML 与文本教学助手使用 Python 3.10+ 标准库；PDF 提取另需 pypdf 6.x，不提供 OCR。图表与公式需查看原始页面。远程获取需要网络，不登录、不执行网页 JavaScript；仅有摘要时限定导读覆盖范围。已保存 HTML 内嵌数学资源，无需网络；禁用 JS 时保留公式源码与静态、键盘替代。Skill 是 Agent 的指令包，论文分析由 Agent 执行。

示例请求：

- “读取已安装的 .agents/skills/paper-guide/SKILL.md 并执行，根据这个论文链接、DOI、粘贴原文或本地 PDF 用中文讲解并保存 HTML 导读。”
- “读取已安装的 .agents/skills/paper-tutor/SKILL.md 并执行，帮我理解这段论文的证据如何支持结论。”

可以查看[实际 Agent 生成的中文导读](examples/paper-guide/agent-invocation-zh.html)、[原文与 renderer 输入](examples/paper-guide/agent-invocation-zh.json)及[教学对话验收片段](examples/paper-tutor/actual-session.md)。另有[实际暂停记录](examples/paper-tutor/ticket07-actual-progress.json)和[导读到教学再到续学的验收对话](examples/paper-tutor/ticket06-07-actual-session.md)。

内容自适应验收采用选取的原文片段：[Attention 计算步骤](examples/paper-guide/adaptive-method-zh.html)、[实证调查证据](examples/paper-guide/adaptive-empirical-zh.html)，以及同一理论模型的[中文](examples/paper-guide/adaptive-theory-zh.html)与[英文](examples/paper-guide/adaptive-theory-en.html)导读。[来源记录](examples/paper-guide/adaptive-source-notes.md)说明覆盖范围与归属。这些片段示例验证不同推理结构。[发布示例](examples/release09/README.md)进一步提供完整主文阅读后的导读：中文算法论文、英文实证研究，以及同一理论论证的英文与中文版本。包括真实截图、原文对照评审、脚本化研究者回答驱动的实际教学、保存进度后新会话续学，以及[相同段落的表达对照](examples/release09/conventional-comparison.md)。这些案例不代表所有学科的质量验证，也未测量学习效果。[全新安装示例](examples/first-use10/README.md)补充本地 PDF 导读、实时 DOI 导读、键盘复制与独立安装的教学，包含原文与真实截图。

[可选机制示例](examples/mechanism08/run.md)提供使用明确教学数值的[限定范围 softmax 温度实验](examples/mechanism08/attention-guide.html)；当原文不足以支持所请求的单篇论文复现概率预测时，提供[静态实证解释](examples/mechanism08/empirical-guide.html)。其他机制按原文提供静态讲解，尚未实现任意机制的交互模拟。

## 设计原则

- **先理清研究逻辑。** 解释每章的作用，以及证据如何支持结论。根据论文的研究与论证方式组织讲解，按实际需要呈现方法步骤、图表或公式。
- **按问题选择图示。** 流程用流程图，差异用对照表，公式按步骤拆解。
- **首次导读保持轻量。** 主线优先，细节按需展开。用户主动要求，或交互确实有助于解释机制时，再提供小实验。
- **讲解可回到原文。** 保留数字、条件和不确定性，区分作者陈述、补充背景、讲解者推断与类比。
- **通过回答判断理解。** 识别知识缺口，卡住时提供解释；用户可以直接问答案、跳过、暂停或结束。

## 后续计划

- [x] 明确受众、阅读路径、语言策略与教学原则。
- [x] 实现粘贴原文的 `paper-guide` 与 HTML renderer。
- [x] 实现独立的 `paper-tutor` 对话教学。
- [x] 读取本地 PDF，保留页位置与提取缺口。
- [x] 获取可访问网页、在线 PDF 与 DOI 定位材料，说明实际覆盖范围及访问限制。
- [x] 根据方法、实证证据与理论论证调整研究逻辑讲解和按需图示。
- [x] 从 HTML 复制章节与术语教学提示词。
- [x] 保存学习进度并结合原文续学。
- [x] 发布串联导读、教学与续学的算法、实证研究、理论或人文论证代表性示例，包含英文与中文输出。
- [x] 提供真实截图与原文来源。
- [x] 提供可选的限定机制演示与静态替代。
- [x] 验证本地安装、Windows Codex 桌面明确读取入口调用、首次使用与许可证（ticket10）。
- [x] 使用相同原文材料，展示普通文字解释与 PaperUnfold 导读的差异。

## 灵感来源

项目参考清晰技术写作，以及为复杂内容生成定制视觉产物的思路。相关讨论见 [Karpathy 的帖子](https://x.com/karpathy/status/2105819303471976479) 与 [asd-ste100-skill](https://github.com/danyuchn/asd-ste100-skill)。

PaperUnfold 采用术语一致、主体明确与保留原意的讲解原则。本项目独立开发，参考仓库不是运行依赖。

## 项目文档

- [实现任务](.scratch/paperunfold/README.md)：10 项已批准任务、依赖关系与验收条件。
- [实现规格](docs/spec.md)：用户故事、能力契约与验收场景（英文）。
- [设计方案](docs/design.md)：已确认的范围、导读结构、教学流程与输出检查。
- [术语表](CONTEXT.md)：统一的领域概念。
- [项目评审](docs/project-review.md)：已确认定位与发布优先级。
- [原始教学 prompt](docs/source/socratic-ddd-prompt.txt)：保留原始材料供对照，实际行为以设计方案为准。

## 许可证与贡献

项目原创代码、技能与文档采用 [MIT](LICENSE)。论文与内嵌 KaTeX 保留各自[许可及署名](THIRD_PARTY_NOTICES.md)。贡献前请查看[验收步骤](CONTRIBUTING.md)。
