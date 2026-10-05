# npx installation acceptance — 2026-10-05

Windows / PowerShell; Node.js/npm from the host; Vercel Skills CLI **1.7.0**.
The checkout has no configured Git remote. This acceptance uses an independent
temporary target project, not the user's current installed skills.

## Discovery and local installation

Actual `npx --yes skills@1.7.0 add . --list` from the checkout discovered exactly
`paper-guide` and `paper-tutor`. The existing `skills/<name>/SKILL.md` layout is
compatible; no custom npm publication or root package.json is needed.

From the temporary target, the actual command was:

```powershell
npx --yes skills@1.7.0 add "D:/Practice/work/project/github_project/paper-reading-skills" --skill paper-guide paper-tutor --agent codex --copy --yes
```

Both packages appeared under the target's `.agents/skills/`. `skills list --agent
codex` listed both, and `skills-lock.json` recorded `sourceType: local` and hashes.
All source package files except Python bytecode/cache were compared against the
installed copies by SHA-256: every comparison passed. Each package now carries
the project MIT LICENSE, matching the root license. KaTeX retains its own license.

The guide's installed `render_guide.py` rendered the checkout's actual
`attention-excerpt-guide.json` into the target project. Render succeeded and the
saved HTML contained embedded mathematical rendering code. This checks installed
helpers/assets, not a fresh agent paper-reading session or browser interaction.

## Local refresh

A disposable marker was appended to the temporary installed guide's SKILL.md.
Re-running the same `add` command reported replacement of both Codex copies.
The marker disappeared and all package hashes matched the current checkout,
including the newly added package LICENSE files. This verifies local re-add
refresh, and also establishes that direct edits to installed copies are replaced.

Actual `skills update paper-guide paper-tutor --project --yes` reported no matching
installed skills despite the local lock entries. Therefore the documented local
refresh is re-running `add`; a zero exit code from `update` is not proof of refresh.

## Remote path and boundaries

The CLI's [official documentation](https://github.com/vercel-labs/skills) supports
GitHub `OWNER/REPO` sources and named updates. README and installation docs carry
explicit placeholders until the repository is published. This project's remote
install/update path is untested; no repository was created or uploaded here.

The CLI installs skill packages, not Python, pypdf or an agent runtime. It also
does not migrate the Python copy installer's untracked installations into remote
update tracking. Users switch to an npx-managed installation by adding from their
chosen source. Automatic skill discovery/execution by the agent is separate from
CLI package discovery and was not newly claimed by this check.
