---
description: Capture learnings from the current session and update `AGENTS.md`
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash
  - LS
  - AskUserQuestion
---

# Session Commit <!-- omit in toc -->

Analyze the current conversation to extract best practices and valuable learnings to the project's `AGENTS.md` file. This file is primarily targeted at agents, and serves to scale effectiveness across sessions.

`AGENTS.md` is a **style and taste guide** — it captures patterns, conventions, and judgment calls. Specific file paths, function names, and implementation details belong in code comments and PR descriptions, not here.

## Preconditions

Before starting, ensure the following files exist in the project root:

- `AGENTS.md` — if missing, use `/init` to create it, then move any guidance found in pointer files into `AGENTS.md`
- `CLAUDE.md`, `GEMINI.md`, `CODEX.md` — if any are missing or empty, recreate them as symlinks to `AGENTS.md`:

```bash
ln -sfn AGENTS.md CLAUDE.md
ln -sfn AGENTS.md CODEX.md
ln -sfn AGENTS.md GEMINI.md
```

## Step 1: Analyze Existing `AGENTS.md`

Read the entire `AGENTS.md`. Before proposing any changes, perform a thorough review:

1. **Build a Mental Map** — list all major sections and their purposes; note the organizational pattern
2. **Catalog Existing Content** — key topics, conventions, commands, and workflows already documented
3. **Flag Potential Conflicts** — topics that might overlap with session learnings; sections already comprehensive enough to skip
4. **Identify Update Targets** — for each candidate learning, find the existing section most likely to absorb it; only flag as needing a new section if no existing one is a reasonable home

This analysis MUST inform what changes are proposed in Step 3.

## Step 2: Extract Session Learnings

Review the conversation for:

- Coding patterns and preferences discovered
- Architecture decisions made
- Gotchas or pitfalls encountered
- Project conventions established
- Debugging insights
- Workflow preferences
- Anything useful for another AI agent or human developer to be productive in this project

If nothing meaningful was learned this session, say so and stop. Don't force updates.

## Writing Guidelines for `AGENTS.md`

Apply these when composing proposed changes in Step 3.

- **Bullet points over prose** — use bullets and sub-bullets, not paragraphs
- **Keep lines short** — aim for ~120 characters per line (soft limit)
- **Update existing sections first** — new headers are a last resort
- **Avoid specific paths and function names** unless they:
  - Serve as an example of a general pattern
  - Are truly global defaults (e.g. config files, entry points)
  - Test: "Would this guidance survive a file rename?" If no, leave it out
- **No duplicate content** — if it's already in `AGENTS.md`, skip it
- **When in doubt, leave it out** — only capture guidance not obvious from the code itself

## Step 3: Propose Changes

**Do NOT apply changes yet.**

**Exhaust updates before proposing additions.** Each learning should first be evaluated as a modification to an existing section. Only propose a new section/header when no existing section is a plausible home.

Present proposed changes using this format:

````markdown
## Proposed Changes to `AGENTS.md`

> **Summary:** X additions, Y modifications, Z removals

---

### ➕ Additions (X)

> **Section: [Section Name]**
>
> ```diff
> + The new content being added
> ```

---

### Modifications (Y)

> **Section: [Section Name]**
>
> **Before:**
>
> ```diff
> - The old content
> ```
>
> **After:**
>
> ```diff
> + The new content
> ```

---

### ❌ Removals (Z)

> **Section: [Section Name]**
>
> ```diff
> - Content being removed
> ```
>
> **Reason:** [Why this is being removed]
````

**Format requirements:**

- Use blockquotes to create visual boxes
- Include a summary line with counts
- Use `diff` code blocks: `+` for additions, `-` for removals
- Show Before/After for modifications
- Require a reason for every removal

Then ask: **"Do you want me to apply these changes to `AGENTS.md`?"**

Wait for explicit confirmation before proceeding.

## Step 4: Apply Changes

Only after the user confirms, apply the approved changes to `AGENTS.md`.

Merge with existing content — don't overwrite unrelated sections.

## Step 5: Review `AGENTS.md` (Optional)

After changes are applied, ask: **"Would you like me to review the entire `AGENTS.md` for cleanup opportunities?"**

If accepted, review for:

- **Duplicates** — same or near-identical instructions in multiple places
- **Stale content** — references to old patterns, removed files, or outdated practices
- **Consolidation** — related items scattered across sections that belong together
- **Clarity** — unclear instructions or verbose content that could be tightened

Present findings using the same format from Step 3. Wait for explicit confirmation before applying cleanup.
