# Install and use PaperUnfold / 安装与使用

## Verified environment / 已验证环境

Verified on 2026-10-04: **Codex desktop Agent on Windows, PowerShell, Python 3.12.14, pypdf 6.19.0**, with explicit filesystem access to the installed `SKILL.md`. A new project and virtual environment were used, with no existing PaperUnfold packages. Edge and Playwright checked the generated HTML offline. See the [first-use record](validation/ticket-10.md).

2026-10-04 已验证：**Windows 上的 Codex 桌面 Agent、PowerShell、Python 3.12.14、pypdf 6.19.0**，通过明确读取已安装 `SKILL.md` 使用技能。测试使用全新项目与虚拟环境，未预装 PaperUnfold。Edge 与 Playwright 验证离线 HTML。见[首次使用记录](validation/ticket-10.md)。

The helpers require Python 3.10+. Other Agent hosts and operating systems have not passed this installation acceptance. Codex CLI 0.154.0 was attempted but its authenticated account rejected the selected models before a skill ran; CLI first use is **unverified**. The project does not require its own model API key; your Agent must already be usable and able to read files and run commands.

助手需要 Python 3.10+。其他 Agent 宿主与操作系统尚未完成安装验收。Codex CLI 0.154.0 曾尝试调用，但账户在技能执行前返回模型不支持，CLI 首次使用**未验证**。本项目无需单独的模型 API key；宿主 Agent 需要已能正常使用，并能读取文件、执行命令。

## npx installation and updates / npx 安装与更新

The [Vercel Skills CLI](https://github.com/vercel-labs/skills) discovers both packages
under `skills/` from their `SKILL.md` frontmatter. No custom npm package is needed.
Install Node.js/npm first; `npx` obtains the third-party CLI. The commands below
were checked with `skills` 1.7.0 on Windows on 2026-10-05. Use
`npx skills@1.7.0` instead of `npx skills` to repeat that CLI version.

[Vercel Skills CLI](https://github.com/vercel-labs/skills) 根据 `SKILL.md` 发现仓库
`skills/` 中的两个包，无需我们额外发布 npm 包。先安装 Node.js/npm，`npx` 会获取
该第三方 CLI。2026-10-05 在 Windows 使用 skills 1.7.0 完成了本地安装验证；需要
复用相同 CLI 版本时，将命令前缀改成 `npx skills@1.7.0`。

### Local checkout / 本地仓库

From this checkout root, install into the current project:
在本仓库根目录安装到当前项目：

```powershell
npx skills add . --list
npx skills add . --skill paper-guide paper-tutor --agent codex --copy --yes
```

To install into another project, open a terminal there and replace `.` with the
absolute checkout path (quote paths containing spaces). `--agent codex` targets
Codex and the packages appear under `.agents/skills/`. `--copy` avoids requiring
symlink permissions on Windows; `--yes` skips the selection dialog. Omit it for
interactive selection. Add `--global` to choose a user-wide installation.

安装到其他项目时，在目标项目运行命令，把 `.` 换成仓库绝对路径，有空格的路径
加引号。`--agent codex` 指定 Codex，技能包位于 `.agents/skills/`；`--copy` 使用
副本，无需 Windows 符号链接权限。`--yes` 跳过选择对话框，省略可交互选择；加
`--global` 可选择用户级安装。

For a **local-source update**, rerun the same `add` command from the target
project after editing the source. It replaces installed copies. The tested CLI's
`update --project` did not match the local-source entries, so it is not the local
refresh path. Keep customizations in the source, and preserve `skills-lock.json`
with the target project; the CLI records source type and hashes there.

**本地来源更新**：修改源文件后，在目标项目重新运行同一条 `add` 命令，会替换
已安装副本。实测 `update --project` 未匹配本地来源记录，因此本地刷新使用 `add`。
把定制保存在源目录，并保留目标项目的 `skills-lock.json`，其中记录来源类型与哈希。

### GitHub source / GitHub 来源

After publishing the repository, substitute the actual `OWNER/REPO`:
仓库发布后，将占位符替换为实际地址：

```powershell
npx skills add OWNER/REPO --skill paper-guide paper-tutor --agent codex --copy --yes
npx skills update paper-guide paper-tutor --project
```

The update command follows the installed remote source; it requires published
changes. Use `--global` instead of `--project` for globally installed skills.
The repository currently has no configured remote, so PaperUnfold's GitHub
install/update path has not yet been exercised. Local install and re-add refresh
are recorded in [npx validation](validation/npx-installation.md).

更新命令跟随已记录的远程来源，源仓库需要已发布新修改；用户级安装使用
`--global` 替代 `--project`。当前项目尚无 Git remote，因此还没有执行本项目的
GitHub 安装/更新；已验证本地安装与重新 `add` 刷新，见[npx 验证记录](validation/npx-installation.md)。

These commands install instruction packages, scripts, references, offline math
assets and package licenses. They do not run a paper-reading agent or install
Python dependencies. For PDF extraction, run in the target project:

这些命令只安装技能指令、脚本、参考文档、离线数学资源与许可证，不执行论文
解读，也不安装 Python 依赖。读取 PDF 时，在目标项目执行：

```powershell
python -m pip install -r .agents/skills/paper-guide/requirements.txt
```

## Python copy installer / Python 副本安装器

Download or obtain this checkout, open PowerShell at its root, and choose an empty sibling project directory. Replace `my-paper-project` with your chosen directory. These commands put the Python environment and both independent skill packages in that project:

取得项目文件后，在仓库根目录打开 PowerShell。将 `my-paper-project` 替换为选定的相邻项目目录；命令会把 Python 环境与两个独立技能包放入该目录：

```powershell
python -m venv ..\my-paper-project\.venv
& ..\my-paper-project\.venv\Scripts\python.exe -m pip install -r skills/paper-guide/requirements.txt
& ..\my-paper-project\.venv\Scripts\python.exe scripts/install_skills.py --dest ..\my-paper-project\.agents\skills
```

To install only one skill, append `--skill paper-guide` or `--skill paper-tutor` to the last command. The tutor needs no PDF package when its input is readable text. Each installed package includes its scripts, references and license; the guide also includes offline math assets. The installer refuses an existing selected package before copying anything, preserving customizations. For an update, choose another empty destination or separately back up and manage your existing package; automatic replacement is not implemented.

只安装一种技能时，在最后一条命令后加 `--skill paper-guide` 或 `--skill paper-tutor`。教学输入是可读文本时，无需 PDF 依赖。每个技能包包含脚本、参考资料与许可证；导读还包含离线数学资源。若选定的技能目录已存在，安装器会在复制前拒绝操作，保留定制内容。更新时选择新的空目录，或自行备份并管理已有包；未实现自动覆盖更新。

Open `my-paper-project` in Codex. [Codex's skill documentation](https://learn.chatgpt.com/docs/build-skills) describes project `.agents/skills` discovery and `$skill-name` invocation. Automatic discovery was not established by our blocked CLI run. The **verified route** is to explicitly ask the desktop Agent to read the installed entry file; supply the project's `.venv/Scripts/python.exe` as its Python executable if needed:

在 Codex 打开 `my-paper-project`。[Codex 官方技能文档](https://learn.chatgpt.com/docs/build-skills)说明了项目 `.agents/skills` 发现与 `$skill-name` 调用。被阻止的 CLI 调用没有验证自动发现。**本次验证的方式**是明确要求桌面 Agent 读取已安装的入口文件；必要时指定项目 `.venv/Scripts/python.exe` 为 Python：

```text
Read .agents/skills/paper-guide/SKILL.md and follow it. Explain inputs/paper.pdf in English and save outputs/guide.html. Use .venv/Scripts/python.exe.
读取 .agents/skills/paper-guide/SKILL.md 并按其执行。用中文导读 DOI 10.1371/journal.pmed.0020124，保存 outputs/guide.html。使用 .venv/Scripts/python.exe。
```

Supply your own PDF or lawful accessible locator. The cited DOI is an open-access example, not a guarantee of access for every DOI. Guides follow the conversation language unless you specify one.

提供自己的 PDF 或可合法访问的链接。示例 DOI 为开放获取材料，不代表所有 DOI 都能取得正文。讲解默认跟随对话语言，也可以明确指定。

## Teaching and resumption / 教学与续学

Open the saved HTML, expand a chapter or term's teaching panel, then copy its prompt into an Agent conversation with `paper-tutor` available. Read `.agents/skills/paper-tutor/SKILL.md` explicitly if the host has not discovered it. If the Copy button fails, select the textarea and press Ctrl+C; teaching takes place in the Agent chat.

打开 HTML，展开章节或术语的教学面板，将提示词复制到有 `paper-tutor` 的 Agent 对话。宿主未发现技能时，明确要求读取 `.agents/skills/paper-tutor/SKILL.md`。复制按钮失败时，选中文本框按 Ctrl+C；教学在 Agent 对话中进行。

Direct teaching is independent: supply readable paper text and request `paper-tutor` with a focused question, without generating a guide. Say “explain directly” to skip a compulsory quiz, or “pause and save progress” to stop. In a **new conversation**, provide the saved progress JSON and relevant readable source (or their accessible paths), then ask the tutor to resume. Move the source together with its record, or supply a new source path. A progress file preserves learning context, not source evidence or automatic mastery.

独立教学：提供可读论文原文和具体问题，请 `paper-tutor` 讲解，无需先生成导读。可以要求“直接讲解”或“暂停并保存进度”。在**新对话**中提供进度 JSON 与相关可读原文（或可访问路径），再要求续学。移动进度时一起移动原文，或提供新的原文路径。进度保留学习上下文，不能代替论文证据，也不会自动标记掌握。

## Dependencies and fallback / 依赖与替代

| Operation / 操作 | Requirement and fallback / 要求与替代 |
| --- | --- |
| Generate guides; save/resume text teaching / 生成导读与保存、续接文本教学 | Agent + Python standard library. If writing is unavailable, the Agent supplies a copyable output and labels it unsaved. / Agent 与 Python 标准库；无法写文件时提供可复制内容并标记未保存。 |
| Extract local/downloaded PDF / 提取本地或下载 PDF | `pypdf` 6.x; install with the requirement above. No OCR. Scans or unreadable material need readable text or a host's verified reading facility. / 需要上述 PDF 依赖，无 OCR；扫描件或不可读材料需可读文本或宿主已验证的读取功能。 |
| Verify figures/equations / 核验图表与公式 | A host PDF viewer or page renderer; this acceptance used Poppler. If unavailable, disclose the limit and avoid claims dependent on unreadable visuals. / 宿主 PDF 查看或页面渲染工具；本次使用 Poppler。不可用时说明限制，不讲解依赖不可读图表的结论。 |
| Acquire URLs/DOIs / 获取链接与 DOI | Internet access; no sign-in, webpage JavaScript or access bypass. Abstract-only results yield limited guides; failures need a readable PDF or pasted passage. / 需要网络，不登录、不执行网页 JS、不绕过访问限制；只有摘要就限定覆盖范围，失败时改用可读 PDF 或粘贴原文。 |
| View saved HTML / 查看已保存 HTML | No network, CDN or model API. KaTeX, fonts and supplied source images are embedded. Without browser JavaScript, formulas retain notation and controls have static/keyboard fallbacks. / 无需网络、CDN 或模型 API；数学、字体与原文图片内嵌；禁用 JS 时保留公式源码与静态、键盘替代。 |

The optional mechanism is a bounded softmax temperature teaching example. Arbitrary simulations are not implemented; other mechanisms use source-grounded static explanations. ASD-STE100-inspired writing and `asd-ste100-skill` are references, not runtime dependencies. Project code is [MIT](../LICENSE); [third-party notices](../THIRD_PARTY_NOTICES.md) preserve paper and KaTeX attribution.

可选机制仅实现限定范围的 softmax 温度教学示例，未实现任意模拟；其他机制提供原文支持的静态讲解。ASD-STE100 与相关 skill 是设计参考，不是运行依赖。项目代码采用 [MIT](../LICENSE)，论文与 KaTeX 保留[第三方许可及署名](../THIRD_PARTY_NOTICES.md)。
