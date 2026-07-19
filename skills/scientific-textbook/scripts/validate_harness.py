#!/usr/bin/env python3
"""Baseline validation for a scientific-textbook project harness."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


CORE_FILES = (
    "PRD.md",
    "BOOK_ARCHITECTURE.md",
    "TOC.md",
    "STYLE_GUIDE.md",
    "CODEX.md",
    "NOTATION.md",
    "GLOSSARY.md",
    "DECISIONS.md",
    "QUALITY_GATES.md",
    "PROGRESS.md",
    "RESUME.md",
)

LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
STATUS_RE = re.compile(r"\b(planned|drafting|evidence-ready|review|complete)\b|\[[ xX]\]")
PROGRESS_FIELDS = ("currently", "next", "blocker")


def local_target(raw: str) -> str | None:
    target = raw.strip().split(maxsplit=1)[0].strip("<>")
    if not target or target.startswith(("#", "http://", "https://", "mailto:")):
        return None
    return target.split("#", 1)[0]


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    for name in CORE_FILES:
        if not (root / name).is_file():
            errors.append(f"missing core file: {name}")

    toc = root / "TOC.md"
    if toc.is_file() and not STATUS_RE.search(toc.read_text(encoding="utf-8")):
        errors.append("TOC.md contains no recognized status")

    progress = root / "PROGRESS.md"
    if progress.is_file():
        lowered = progress.read_text(encoding="utf-8").lower()
        for field in PROGRESS_FIELDS:
            if field not in lowered:
                errors.append(f"PROGRESS.md does not identify {field} state")

    for markdown in root.rglob("*.md"):
        if any(part in {".git", ".venv", "node_modules"} for part in markdown.parts):
            continue
        text = markdown.read_text(encoding="utf-8")
        for raw in LINK_RE.findall(text):
            target = local_target(raw)
            if target is None or any(ch in target for ch in "{}*"):
                continue
            resolved = (markdown.parent / target).resolve()
            if not resolved.exists():
                errors.append(f"broken local link: {markdown.relative_to(root)} -> {target}")
    return sorted(set(errors))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_dir", type=Path)
    args = parser.parse_args()
    root = args.project_dir.expanduser().resolve()
    if not root.is_dir():
        print(f"ERROR: not a directory: {root}", file=sys.stderr)
        return 2
    errors = validate(root)
    if errors:
        print("HARNESS VALIDATION: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("HARNESS VALIDATION: PASS")
    print(f"- core files present: {len(CORE_FILES)}")
    print("- TOC status, progress bookmark, and local Markdown links checked")
    print("- project-specific scientific and profile gates still require separate validation")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
