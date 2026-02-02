# AGENTS.md <!-- omit in toc -->

- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [Supported Tools](#supported-tools)
- [Documentation Standards](#documentation-standards)

## Project Overview

- Claude Code plugin that captures session learnings to `AGENTS.md`
- Cross-tool: works with Claude Code, OpenCode, Codex CLI, Gemini CLI
- Each tool reads its own instruction file, all point back to `AGENTS.md`

## Project Structure

- `AGENTS.md` — project guidelines (this file)
- `README.md` — user-facing documentation with quickstart and how-it-works
- `CLAUDE.md`, `CODEX.md`, `GEMINI.md` — minimal pointers to `AGENTS.md`
- `.claude-plugin/plugin.json` — plugin manifest (name, version, author)
- `.claude-plugin/marketplace.json` — marketplace listing metadata
- `gemini-extension.json` — Gemini CLI extension manifest
- `commands/session-commit.md` — the `/session-commit` command for Claude Code
- `commands/session-commit.toml` — the `/session-commit` command for Gemini CLI
- `templates/` — pointer file templates (CLAUDE.md, CODEX.md, GEMINI.md)

## Supported Tools

| Tool        | Reads                | Pointer file needed? |
| ----------- | -------------------- | -------------------- |
| Claude Code | `CLAUDE.md`          | Yes                  |
| OpenCode    | `AGENTS.md` (native) | No                   |
| Codex CLI   | `AGENTS.md` (native) | No                   |
| Gemini CLI  | `GEMINI.md`          | Yes                  |

- OpenCode also falls back to `CLAUDE.md` for Claude Code compatibility
- Codex optionally reads `CODEX.md` via `project_doc_fallback_filenames` config

## Documentation Standards

- Code blocks must be comment-free and directly copy-pastable
- No `#` comments inside fenced code blocks
- Quickstart instructions come before explanatory content
- Use bullet points over paragraphs
