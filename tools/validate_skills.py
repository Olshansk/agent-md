#!/usr/bin/env python3
"""Validate Agent Skills frontmatter and basic repository conventions."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def strip_quotes(value: str) -> str:
    value = value.strip()
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]
    return value


def parse_frontmatter(text: str, file_path: Path) -> dict[str, str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        raise ValueError(f"{file_path}: missing YAML frontmatter block")

    block = match.group(1)
    fields: dict[str, str] = {}

    for raw_line in block.splitlines():
        if not raw_line or raw_line.lstrip().startswith("#"):
            continue
        if raw_line.startswith(" ") or raw_line.startswith("\t"):
            continue
        if ":" not in raw_line:
            continue
        key, value = raw_line.split(":", 1)
        fields[key.strip()] = strip_quotes(value)

    return fields


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []

    if not skill_dir.is_dir():
        return errors

    skill_name = skill_dir.name
    skill_file = skill_dir / "SKILL.md"

    if not skill_file.exists():
        errors.append(f"{skill_dir}: missing SKILL.md")
        return errors

    text = skill_file.read_text(encoding="utf-8")
    line_count = len(text.splitlines())

    try:
        fields = parse_frontmatter(text, skill_file)
    except ValueError as exc:
        errors.append(str(exc))
        return errors

    name = fields.get("name", "").strip()
    description = fields.get("description", "").strip()
    compatibility = fields.get("compatibility", "").strip()

    if not name:
        errors.append(f"{skill_file}: required field 'name' is missing")
    else:
        if len(name) > 64:
            errors.append(f"{skill_file}: name must be <= 64 characters")
        if not NAME_RE.match(name):
            errors.append(
                f"{skill_file}: name must match ^[a-z0-9]+(?:-[a-z0-9]+)*$"
            )
        if name != skill_name:
            errors.append(
                f"{skill_file}: name '{name}' must match directory '{skill_name}'"
            )

    if not description:
        errors.append(f"{skill_file}: required field 'description' is missing")
    else:
        if len(description) > 1024:
            errors.append(f"{skill_file}: description must be <= 1024 characters")

    if compatibility and len(compatibility) > 500:
        errors.append(f"{skill_file}: compatibility must be <= 500 characters")

    if line_count > 500:
        errors.append(f"{skill_file}: SKILL.md should stay under 500 lines")

    return errors


def main() -> int:
    if not SKILLS_DIR.exists():
        print("skills/ directory not found", file=sys.stderr)
        return 1

    all_errors: list[str] = []
    skill_dirs = sorted([p for p in SKILLS_DIR.iterdir() if p.is_dir()])

    if not skill_dirs:
        all_errors.append("No skills found in skills/")

    for skill_dir in skill_dirs:
        all_errors.extend(validate_skill(skill_dir))

    if all_errors:
        print("Skill validation failed:", file=sys.stderr)
        for err in all_errors:
            print(f"- {err}", file=sys.stderr)
        return 1

    print(f"Validated {len(skill_dirs)} skill(s) successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
