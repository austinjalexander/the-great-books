#!/usr/bin/env python3
"""Check local agent configuration and export a study handoff without answer keys."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
GUIDES = (
    "AGENTS.md",
    "CLAUDE.md",
    "docs/agents/PROFILE.md",
    "docs/agents/README.md",
    "docs/agents/CHATGPT-START.md",
    "docs/agents/tutoring.md",
    "docs/agents/module-structure.md",
    "docs/agents/writing-style.md",
    "docs/agents/math-and-code-style.md",
)
SKILLS = (
    "author-module",
    "discussion-session",
    "diagnose-prereqs",
    "grade-solution",
    "grade-composition",
    "thesis-advisor",
)
KEY = re.compile(r"(?:^|[-_])(solutions?|answers?)(?:[-_.]|$)", re.I)


def check() -> int:
    errors: list[str] = []
    paths = [ROOT / name for name in GUIDES]
    paths += [ROOT / ".agents/skills" / name / "SKILL.md" for name in SKILLS]
    paths += list((ROOT / ".cursor/rules").glob("*.mdc"))
    for path in paths:
        relative = path.relative_to(ROOT)
        if not path.is_file():
            errors.append(f"missing {relative}")
            continue
        body = path.read_text()
        for target in re.findall(r"(?<!!)\[[^\]]*\]\(([^)]+)\)", body):
            if ":" in target or target.startswith("#"):
                continue
            resolved = (path.parent / unquote(target.split("#", 1)[0])).resolve()
            if not resolved.exists():
                errors.append(f"broken link in {relative}: {target}")
    for name in SKILLS:
        path = ROOT / ".agents/skills" / name / "SKILL.md"
        if not path.is_file():
            continue
        body = path.read_text()
        match = re.match(r"---\n(.*?)\n---\n", body, re.S)
        metadata = (
            dict(re.findall(r"^(name|description):\s*(.+)$", match[1], re.M)) if match else {}
        )
        if metadata.get("name") != name or not metadata.get("description"):
            errors.append(f"invalid skill metadata: {name}")
        if ".cursor/" in body:
            errors.append(f"tool-specific reference in canonical skill: {name}")
        alias = ROOT / ".claude/skills" / name
        if (
            not alias.is_symlink()
            or alias.readlink().is_absolute()
            or alias.resolve() != path.parent.resolve()
        ):
            errors.append(f"incorrect relative Claude skill link: {name}")
        if (ROOT / ".cursor/skills" / name).exists():
            errors.append(f"duplicate Cursor skill: {name}")
    for name, guide in (
        ("tutor-persona", "tutoring"),
        ("module-structure", "module-structure"),
        ("writing-style", "writing-style"),
        ("math-and-code-style", "math-and-code-style"),
    ):
        adapter = ROOT / ".cursor/rules" / f"{name}.mdc"
        if not adapter.is_file() or f"@docs/agents/{guide}.md" not in adapter.read_text():
            errors.append(f"missing canonical rule adapter: {name}")
    claude = ROOT / "CLAUDE.md"
    if claude.is_file() and "@AGENTS.md" not in claude.read_text():
        errors.append("CLAUDE.md must import @AGENTS.md")
    profile = ROOT / "docs/agents/PROFILE.md"
    if profile.is_file():
        match = re.search(r"Reference module: `([^`]+)`", profile.read_text())
        for name in (
            "README.md",
            "notes.md",
            "discussion.md",
            "reflection.md",
            "problems.md",
            "solutions.md",
            "learner-work.md",
        ):
            if not match or not (ROOT / match[1] / name).is_file():
                errors.append(f"reference module missing {name}")
    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors), file=sys.stderr)
        return 1
    print(
        f"OK: {len(SKILLS)} canonical skills; guides, adapters, links, and reference module checked"
    )
    return 0


def study_text(path: Path) -> str:
    relative = path.resolve().relative_to(ROOT)
    if any(KEY.search(part) for part in relative.parts):
        raise ValueError("answer-key files are excluded")
    body = path.read_text()
    # Older exercises may contain folded or headed keys. Exclude the entire fold,
    # and everything after an explicit answer-key heading, rather than leak it.
    body = re.sub(
        r"<details\b[^>]*>.*?</details>", "[Folded content omitted.]", body, flags=re.S | re.I
    )
    body = re.split(r"^#{1,6}\s+(?:Answer key|Solutions)\b", body, maxsplit=1, flags=re.M | re.I)[0]
    return body.rstrip()


def export(skill: str, module: str) -> int:
    if skill not in SKILLS:
        raise ValueError("choose an installed skill")
    supplied = Path(module)
    if supplied.is_absolute():
        raise ValueError("use a repository-relative module path")
    folder = (ROOT / supplied).resolve()
    relative = folder.relative_to(ROOT)
    if not relative.parts or relative.parts[0] != "notes" or not folder.is_dir():
        raise ValueError("module must be a directory under notes/")
    if not (folder / "README.md").is_file():
        raise ValueError("module must have a README.md")
    files = [ROOT / name for name in GUIDES if name != "CLAUDE.md"]
    files += [ROOT / ".agents/skills" / skill / "SKILL.md", ROOT / "PROGRESS.md"]
    files += [
        folder / name
        for name in (
            "README.md",
            "notes.md",
            "discussion.md",
            "problems.md",
            "exercises.md",
            "learner-work.md",
            "reflection.md",
        )
        if (folder / name).is_file()
    ]
    # Read everything before printing so a bad path cannot produce a partial packet.
    sections = [(str(path.relative_to(ROOT)), study_text(path)) for path in files]
    print("# Great Books study handoff\n")
    print(
        "Snapshot of guidance and recorded evidence. "
        "Linked files are not automatically accessible. "
        "Do not claim file edits, reading, timing, or learner success not evidenced here. "
        "Give proposed log updates for the learner to save. Separate keys are excluded; "
        "notes can contain teaching examples, so this is not a closed-book assessment packet.\n"
    )
    for name, body in sections:
        print(f"---\n\n## Source: {name}\n\n{body}\n")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("check")
    packet = sub.add_parser("export")
    packet.add_argument("--skill", choices=SKILLS, required=True)
    packet.add_argument("--module", required=True)
    args = parser.parse_args()
    try:
        return check() if args.command == "check" else export(args.skill, args.module)
    except (ValueError, OSError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
