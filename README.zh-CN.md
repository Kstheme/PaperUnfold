# PaperUnfold

**把论文的逻辑展开，把难懂的地方讲清楚。**

[English](README.md) · [简体中文](README.zh-CN.md)

PaperUnfold 基于一套通用论文阅读方法，面向全球各学科研究人员，根据每篇论文的研究问题、论证、方法与证据调整讲解。阅读体验先提供轻量 HTML 导读，再按需通过对话深入学习。

**ticket01、02、03、06、07 已实现。** 支持粘贴原文或本地 PDF 生成 HTML 导读、复制章节与术语教学提示词，以及保存学习进度并结合原文续学。链接/DOI 获取与安装验收仍在后续计划中。见[本轮验收记录](docs/validation/tickets-03-06-07.md)。

## 阅读体验

1. 粘贴论文章节或提供本地 PDF；链接与 DOI 获取将在后续实现。
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

## 使用当前版本

在有文件读取与命令执行能力的 Agent 中，明确要求读取仓库里的 [paper-guide](skills/paper-guide/SKILL.md) 或 [paper-tutor](skills/paper-tutor/SKILL.md)，再提供可读原文。HTML renderer 与进度助手需要 Python 3.10+，只使用标准库。本地 PDF 提取另需 `pypdf` 6.x，可运行 `python -m pip install -r skills/paper-guide/requirements.txt`。已验证的 PDF 环境为 Python 3.12.14、pypdf 6.10.0。提取器不提供 OCR；涉及图表或公式时仍需查看原始 PDF 页面。Skill 是 Agent 的指令包，论文分析由 Agent 执行。

示例请求：

- “使用仓库里的 paper-guide，根据这段原文或本地 PDF 用中文讲解并保存 HTML 导读。”
- “使用 paper-tutor，帮我理解这段论文的证据如何支持结论。”

可以查看[实际 Agent 生成的中文导读](examples/paper-guide/agent-invocation-zh.html)、[原文与 renderer 输入](examples/paper-guide/agent-invocation-zh.json)及[教学对话验收片段](examples/paper-tutor/actual-session.md)。另有[实际暂停记录](examples/paper-tutor/ticket07-actual-progress.json)和[导读到教学再到续学的验收对话](examples/paper-tutor/ticket06-07-actual-session.md)，完整本地 PDF 与不可读输入检查见本轮记录。跨学科代表性示例属于 ticket09；不同宿主的技能发现和安装流程属于 ticket10。

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
- [x] 从 HTML 复制章节与术语教学提示词。
- [x] 保存学习进度并结合原文续学。
- [ ] 提供算法、实证研究、理论或人文论证的代表性示例，包含英文与中文输出。
- [ ] 补齐真实截图、原文来源、经验证的安装步骤与许可证。
- [ ] 使用相同原文材料，展示普通文字解释与 PaperUnfold 导读的差异。

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
