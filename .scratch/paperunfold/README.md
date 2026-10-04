# PaperUnfold 本地任务索引

发布日期：2026-10-04。用户已批准 10 项任务的粒度与依赖；每个任务独立发布为 Markdown 文件。

## 开始工作

**01–09 已完成验收。** **10 的直接依赖已解除，可以开始实施。** 按需机制演示与代表性发布示例见[本轮记录](../../docs/validation/tickets-08-09.md)及[示例入口](../../examples/release09/README.md)。未完成任务维持 ready-for-agent；该状态表示任务已明确，不表示依赖已解除。

任务状态、阻塞项与验收结果以各任务文件为准。执行者先核对 Blocked by，再开展实现；完成时应提供实际调用、原文核验与产物操作的验收证据。

## 任务清单

| 任务 | 直接前置任务 | 发布范围 |
| --- | --- | --- |
| [01：粘贴原文生成首个轻量 HTML 导读](issues/01-first-section-guide.md) | 无 | 轻量发布路径 |
| [02：从原文直接开展问题驱动教学](issues/02-direct-paper-tutor.md) | 无 | 轻量发布路径 |
| [03：本地 PDF 生成全文或覆盖范围明确的导读](issues/03-local-pdf-guide.md) | 01 | 轻量发布路径 |
| [04：论文链接、网页与 DOI 定位到真实材料并生成导读](issues/04-url-doi-guide.md) | 03 | 轻量发布路径 |
| [05：按论文内容生成研究逻辑与必要图示](issues/05-adaptive-visual-explanations.md) | 03 | 轻量发布路径 |
| [06：从 HTML 导读复制提示词进入教学](issues/06-guide-to-teaching.md) | 01、02 | 轻量发布路径 |
| [07：暂停后保存真实学习进度并跨会话续学](issues/07-learning-progress-resume.md) | 02 | 轻量发布路径 |
| [08：按需提供聚焦一个机制的小实验与静态替代](issues/08-optional-mechanism-interaction.md) | 05 | 可选增强 |
| [09：发布跨论文类型的中英文导读与教学续学示例](issues/09-representative-end-to-end-examples.md) | 03、05、06、07 | 轻量发布路径 |
| [10：完成从安装到首次阅读的可验证发布体验](issues/10-verified-first-use-release.md) | 04、09 | 轻量发布路径 |

08 的限定 softmax 机制交互与静态替代已验收。该增强仍为可选，不阻塞 09 或 10。其他机制按原文提供静态解释，不宣称支持任意交互模拟。

## 来源与约定

来源：[实现规格](../../docs/spec.md)与[领域术语表](../../CONTEXT.md)。任务发布时未修改或关闭来源规格；2026-10-04 随后实现并验收了 01–09。

本项目已选择本地 Markdown tracker。每个任务独立保存，编号按依赖顺序排列；Blocked by 记录直接阻塞项，Status 记录分流状态，复选框记录验收进展。讨论可追加在各文件的 Comments 标题下。

本轮发布使用 to-tickets 规定的 ready-for-agent 状态。完整设置流程中的其他标签映射与 Agent 入口文件仍未确认，不能将本次任务发布视为完整设置已经完成。

