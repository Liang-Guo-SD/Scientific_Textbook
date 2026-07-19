#!/usr/bin/env python3
"""Validate the public scientific-textbook skill package."""

from __future__ import annotations

import json
import re
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]
REPO_DIR = SKILL_DIR.parents[1]
SKILL_FILE = SKILL_DIR / "SKILL.md"


def validate() -> list[str]:
    errors: list[str] = []
    text = SKILL_FILE.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append("SKILL.md is missing YAML frontmatter")
    frontmatter = text.split("---", 2)[1] if text.count("---") >= 2 else ""
    if not re.search(r"^name:\s*scientific-textbook\s*$", frontmatter, re.MULTILINE):
        errors.append("SKILL.md has an invalid name")
    if not re.search(r"^description:\s*\S.+$", frontmatter, re.MULTILINE):
        errors.append("SKILL.md is missing a description")

    for relative in sorted(set(re.findall(r"`((?:references|scripts)/[^`]+)`", text))):
        if not (SKILL_DIR / relative).is_file():
            errors.append(f"SKILL.md references missing file: {relative}")

    metadata = SKILL_DIR / "agents" / "openai.yaml"
    if not metadata.is_file():
        errors.append("missing agents/openai.yaml")
    elif "$scientific-textbook" not in metadata.read_text(encoding="utf-8"):
        errors.append("agents/openai.yaml default prompt does not name the skill")

    plugin = REPO_DIR / ".claude-plugin" / "plugin.json"
    if plugin.is_file():
        try:
            json.loads(plugin.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"invalid plugin.json: {exc}")

    readme = REPO_DIR / "README.md"
    if not readme.is_file():
        errors.append("missing public README.md")

    stale_phrases = (
        "locked 8-section",
        "initializes a 9-file",
        "YOUR_USERNAME",
        "scientific-textbook@claude-plugins-official",
        "any scientific textbook",
    )
    public_files = [SKILL_FILE, readme, plugin]
    for path in public_files:
        if not path.is_file():
            continue
        lowered = path.read_text(encoding="utf-8").lower()
        for phrase in stale_phrases:
            if phrase.lower() in lowered:
                errors.append(f"stale or overbroad phrase in {path.relative_to(REPO_DIR)}: {phrase}")
    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("PACKAGE VALIDATION: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("PACKAGE VALIDATION: PASS")
    print("- frontmatter, references, metadata, plugin JSON, README, and stale claims checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
