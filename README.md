# agent-skills <!-- omit in toc -->

[![Codex CLI](https://img.shields.io/badge/Codex%20CLI-00A67E)](#)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-D27656)](#)
[![Gemini CLI](https://img.shields.io/badge/Gemini%20CLI-678AE3)](#)
[![OpenCode](https://img.shields.io/badge/OpenCode-3B82F6)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-red.svg)](https://opensource.org/licenses/MIT)

- Multi-skill catalog for agentic CLIs
- Primary distribution: `npx skills add olshansk/agent-skills`
- Also published for Agent Skills ecosystem discovery: https://agentskills.io/home

## Table of Contents <!-- omit in toc -->

- [Quickstart](#quickstart)
- [Available Skills](#available-skills)
- [Validation](#validation)
- [Star History](#star-history)

## Quickstart

```bash
npx skills add olshansk/agent-skills
```

Then ask your agent to run any installed skill (e.g., "close the loop", "generate skills dashboard").

## Available Skills

| Skill              | What it does                                                    | Trigger examples                                               |
| ------------------ | --------------------------------------------------------------- | -------------------------------------------------------------- |
| `session-commit`   | Captures session learnings and updates `AGENTS.md` safely       | "run session commit", "close the loop", "update AGENTS.md"     |
| `skills-dashboard` | Scrapes skills.sh and generates an interactive HTML dashboard   | "generate skills dashboard", "show skills ecosystem"           |

See each skill's README for detailed usage and manual install instructions.

## Validation

CI runs skill validation on changes under `skills/**`.

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=olshansk/agent-skills&type=date&legend=top-left)](https://www.star-history.com/#olshansk/agent-skills&type=date&legend=top-left)
