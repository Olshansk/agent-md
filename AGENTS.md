# AGENTS.md <!-- omit in toc -->

- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [Supported Tools](#supported-tools)
- [Skill Authoring Standards](#skill-authoring-standards)
- [Documentation Standards](#documentation-standards)

## Project Overview

- Multi-skill catalog for agentic CLIs
- Canonical distribution path: `npx skills add olshansk/agent-skills`
- Primary skill in this repo: `skills/session-commit`
- Purpose: preserve durable project learnings in `AGENTS.md` across sessions and tools

## Project Structure

- `skills/` — installable skills
- `skills/session-commit/SKILL.md` — spec-compliant instruction file for the session-commit skill
- `skills/session-commit/scripts/preflight.sh` — validates required instruction files and can repair missing/empty files
- `skills/session-commit/references/` — additional docs loaded on demand
- `skills/session-commit/assets/` — reusable templates (for example pointer file template)
- `tools/validate_skills.py` — validates skill frontmatter and naming constraints
- `.github/workflows/skills-validate.yml` — CI workflow for skill validation
- `commands/` — legacy manual-install command files for fallback paths
- `.claude-plugin/`, `gemini-extension.json` — legacy fallback metadata for tool-specific installs

## Supported Tools

| Tool        | Preferred install path                         | Fallback path in this repo |
| ----------- | ---------------------------------------------- | -------------------------- |
| Claude Code | `npx skills add olshansk/agent-skills`         | `.claude-plugin/`          |
| Codex CLI   | `npx skills add olshansk/agent-skills`         | `commands/session-commit.md` |
| Gemini CLI  | `npx skills add olshansk/agent-skills`         | `commands/session-commit.toml` |
| OpenCode    | `npx skills add olshansk/agent-skills`         | `commands/session-commit.md` |

## Skill Authoring Standards

- Every skill directory must include `SKILL.md`
- `SKILL.md` must begin with YAML frontmatter containing at least:
  - `name`
  - `description`
- `name` must match the skill directory name and be kebab-case
- Keep `SKILL.md` concise; move extended content to `references/`
- Use `scripts/` for reusable or complex command logic
- Scripts must be non-interactive and safe for agent execution
- Prefer structured stdout and diagnostic stderr in scripts

## Documentation Standards

- Code blocks must be comment-free and directly copy-pastable
- No `#` comments inside fenced code blocks
- Quickstart instructions come before explanatory content
- Use bullet points over paragraphs
