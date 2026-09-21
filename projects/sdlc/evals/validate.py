#!/usr/bin/env python3
"""Validate SDLC skill structure and evaluation fixtures.

Checks frontmatter, relative links, the evidence contract, and scenario
shape. Does not invoke a model or score generated prose.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
SCENARIOS = ROOT / "evals" / "scenarios"
EVIDENCE = SKILLS / "_sdlc" / "evidence.yaml"

SUITE = {
    "repository-archaeology",
    "change-planning",
    "implement-change",
    "test-design",
    "pr-review-ruling",
}

REQUIRED_IDS = {
    "clean-change-approve",
    "subtle-correctness-defect",
    "style-only-nonblocking",
    "environment-blocked-command",
    "dirty-worktree-preserve",
    "scope-exceeded",
    "unrun-command-claim",
    "review-invalidated-by-commit",
    "security-data-loss-priority",
    "insufficient-evidence",
}

EVIDENCE_KEYS = {
    "task",
    "scope",
    "requirements",
    "changes",
    "verification",
    "risk",
    "review",
    "state",
}

RULINGS = {"approve", "request_changes", "withhold"}
LIST_FIELDS = (
    "must_identify",
    "must_not_claim",
    "prohibited_actions",
    "must_preserve",
)

REPO_ROOT = ROOT.parents[1]
LINK_ROOTS = [
    ROOT / "README.md",
    ROOT / "docs" / "sdlc-suite.md",
    ROOT / "evals" / "README.md",
    REPO_ROOT / "README.md",
    REPO_ROOT / "CONTRIBUTING.md",
]


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def load_yaml():
    try:
        import yaml
    except ImportError:
        print(
            "PyYAML is required for evals/validate.py and was not imported. "
            "This script does not install it.",
            file=sys.stderr,
        )
        raise SystemExit(2)
    return yaml


def parse_frontmatter(text: str):
    if not text.startswith("---\n"):
        return None, "missing opening frontmatter"
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, "missing closing frontmatter"
    return text[4:end], None


def strip_fences(text: str) -> str:
    lines = []
    fenced = False
    for line in text.splitlines():
        if line.startswith("```"):
            fenced = not fenced
            continue
        if not fenced:
            lines.append(line)
    return "\n".join(lines)


def markdown_links(text: str):
    import re

    body = strip_fences(text)
    return re.findall(r"\[[^\]]*\]\(([^)]+)\)", body)


def check_link(source: Path, target: str, errors: list[str]) -> None:
    path = target.split("#", 1)[0].strip()
    if not path or path.startswith(("http://", "https://", "mailto:")):
        return
    resolved = (source.parent / path).resolve()
    if not resolved.exists():
        fail(errors, f"{source.relative_to(ROOT)}: broken link {target}")


def check_skills(yaml, errors: list[str]) -> None:
    found = set()
    for skill_dir in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
        if skill_dir.name == "_sdlc":
            if (skill_dir / "SKILL.md").exists():
                fail(errors, "skills/_sdlc must not contain SKILL.md")
            for companion in skill_dir.glob("*.md"):
                for link in markdown_links(companion.read_text()):
                    check_link(companion, link, errors)
            continue
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            fail(errors, f"{skill_dir.name}: missing SKILL.md")
            continue
        text = skill_md.read_text()
        raw, parse_error = parse_frontmatter(text)
        if parse_error:
            fail(errors, f"{skill_dir.name}: {parse_error}")
            continue
        meta = yaml.safe_load(raw) or {}
        name = meta.get("name")
        description = meta.get("description")
        found.add(skill_dir.name)
        if name != skill_dir.name:
            fail(errors, f"{skill_dir.name}: name is {name!r}")
        if not isinstance(name, str) or not re.fullmatch(r"[a-z0-9-]{1,64}", name or ""):
            fail(errors, f"{skill_dir.name}: name must match [a-z0-9-]{{1,64}}")
        if not isinstance(description, str) or not description.strip():
            fail(errors, f"{skill_dir.name}: description is empty")
        elif len(description) > 1024:
            fail(errors, f"{skill_dir.name}: description is {len(description)} chars")
        if len(text.splitlines()) > 500:
            fail(errors, f"{skill_dir.name}: SKILL.md exceeds 500 lines")
        for link in markdown_links(text):
            check_link(skill_md, link, errors)
        for companion in skill_dir.glob("*.md"):
            if companion.name == "SKILL.md":
                continue
            for link in markdown_links(companion.read_text()):
                check_link(companion, link, errors)
        if skill_dir.name in SUITE and "../_sdlc/evidence.yaml" not in text:
            fail(errors, f"{skill_dir.name}: suite skill must link to ../_sdlc/evidence.yaml")
    missing = SUITE - found
    if missing:
        fail(errors, f"missing suite skills: {', '.join(sorted(missing))}")


def check_evidence(yaml, errors: list[str]) -> None:
    if not EVIDENCE.exists():
        fail(errors, "skills/_sdlc/evidence.yaml is missing")
        return
    if not (SKILLS / "_sdlc" / "LIFECYCLE.md").exists():
        fail(errors, "skills/_sdlc/LIFECYCLE.md is missing")
    data = yaml.safe_load(EVIDENCE.read_text())
    if not isinstance(data, dict):
        fail(errors, "evidence.yaml must be a mapping")
        return
    missing = EVIDENCE_KEYS - set(data)
    if missing:
        fail(errors, f"evidence.yaml missing keys: {', '.join(sorted(missing))}")
    verification = data.get("verification") or {}
    for key in ("commands_run", "passed", "failed", "not_run"):
        if key not in verification:
            fail(errors, f"evidence.yaml verification.{key} is required")


def check_scenarios(yaml, errors: list[str]) -> None:
    if not SCENARIOS.is_dir():
        fail(errors, "evals/scenarios is missing")
        return
    seen = set()
    for path in sorted(SCENARIOS.glob("*.yaml")):
        data = yaml.safe_load(path.read_text())
        if not isinstance(data, dict):
            fail(errors, f"{path.name}: scenario must be a mapping")
            continue
        sid = data.get("id")
        if sid != path.stem:
            fail(errors, f"{path.name}: id {sid!r} does not match filename")
        seen.add(sid)
        skill = data.get("skill")
        skill_md = SKILLS / str(skill) / "SKILL.md"
        if not skill_md.exists():
            fail(errors, f"{path.name}: unknown skill {skill!r}")
        if not isinstance(data.get("given"), str) or not data["given"].strip():
            fail(errors, f"{path.name}: given is empty")
        expected = data.get("expected")
        if not isinstance(expected, dict):
            fail(errors, f"{path.name}: expected must be a mapping")
            continue
        ruling = expected.get("ruling")
        if ruling is not None and ruling not in RULINGS:
            fail(errors, f"{path.name}: ruling {ruling!r} is not allowed")
        for field in LIST_FIELDS:
            if field not in expected:
                continue
            value = expected[field]
            if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
                fail(errors, f"{path.name}: expected.{field} must be a list of strings")
    missing = REQUIRED_IDS - seen
    if missing:
        fail(errors, f"missing scenarios: {', '.join(sorted(missing))}")


def check_docs(errors: list[str]) -> None:
    for path in LINK_ROOTS:
        if not path.exists():
            fail(errors, f"missing {path.relative_to(ROOT)}")
            continue
        for link in markdown_links(path.read_text()):
            check_link(path, link, errors)


def main() -> int:
    yaml = load_yaml()
    errors: list[str] = []
    check_skills(yaml, errors)
    check_evidence(yaml, errors)
    check_scenarios(yaml, errors)
    check_docs(errors)
    if errors:
        print(f"FAILED {len(errors)} check(s):")
        for error in errors:
            print(f"- {error}")
        return 1
    print(
        "OK skill frontmatter, suite links, evidence contract, "
        f"{len(REQUIRED_IDS)} scenario fixtures, and documentation links"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
