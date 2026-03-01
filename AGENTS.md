# AGENTS.md <!-- omit in toc -->

- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [Supported Tools](#supported-tools)
- [Skill Authoring Standards](#skill-authoring-standards)
- [Documentation Standards](#documentation-standards)

## Project Overview

- Multi-skill catalog for agentic CLIs
- Canonical distribution path: `npx skills add olshansk/agent-skills`
- Skills: `session-commit`, `skills-dashboard`

## Project Structure

- `skills/` — installable skills
- `skills/session-commit/` — captures session learnings and updates `AGENTS.md`
- `skills/skills-dashboard/` — scrapes skills.sh and generates an interactive HTML dashboard
- `.github/workflows/skills-validate.yml` — CI workflow for skill validation
- `.claude-plugin/`, `gemini-extension.json` — legacy fallback metadata for tool-specific installs

## Supported Tools

| Tool        | Preferred install path                         | Fallback path in this repo |
| ----------- | ---------------------------------------------- | -------------------------- |
| Claude Code | `npx skills add olshansk/agent-skills`         | `.claude-plugin/`          |
| Codex CLI   | `npx skills add olshansk/agent-skills`         | `skills/session-commit/commands/session-commit.md` |
| Gemini CLI  | `npx skills add olshansk/agent-skills`         | `skills/session-commit/commands/session-commit.toml` |
| OpenCode    | `npx skills add olshansk/agent-skills`         | `skills/session-commit/commands/session-commit.md` |

## Skill Authoring Standards

Directory pattern:

```text
skills/<skill-name>/
  SKILL.md
  scripts/        # optional
  references/     # optional
  assets/         # optional
  commands/       # optional — legacy per-tool command files
```

`SKILL.md` requirements:

- YAML frontmatter is required with at least `name` and `description`
- `name` must match the skill directory name and be kebab-case
- `description` should say what it does and when to use it
- Keep `SKILL.md` concise; move extended content to `references/`

Scripts:

- Use `scripts/` for reusable or complex command logic
- Scripts must be non-interactive and safe for agent execution
- Prefer structured stdout and diagnostic stderr in scripts

## Documentation Standards

- Code blocks must be comment-free and directly copy-pastable
- No `#` comments inside fenced code blocks
- Quickstart instructions come before explanatory content
- Use bullet points over paragraphs
