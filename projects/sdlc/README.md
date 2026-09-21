# SDLC

Portable software-development lifecycle skills for coding agents (Cursor, Claude Code, Codex, and similar).

Covers discovery → planning → authorized implementation → test design → independent PR/MR review. Does not merge, deploy, or approve on a human's behalf.

## Skills

| Skill | Description |
|-------|-------------|
| [`repository-archaeology`](./skills/repository-archaeology/) | Repo map, local instructions, commands, and Git boundary before planning or editing |
| [`change-planning`](./skills/change-planning/) | Bounded implementation plan without authorization to edit |
| [`implement-change`](./skills/implement-change/) | Smallest authorized change, preserving unrelated work |
| [`test-design`](./skills/test-design/) | Risk-based tests and an honest record of what ran |
| [`pr-review-ruling`](./skills/pr-review-ruling/) | Verdict-first PR/MR reviews with `APPROVE` or `REQUEST CHANGES` |

Shared lifecycle and evidence rules live in [`skills/_sdlc/`](./skills/_sdlc/) (not a skill). Full suite notes: [docs/sdlc-suite.md](./docs/sdlc-suite.md).

## Install

Copy the suite so relative `_sdlc` links keep working:

```bash
# From this repository root
mkdir -p ~/.cursor/skills
for name in _sdlc repository-archaeology change-planning implement-change test-design pr-review-ruling; do
  cp -R "projects/sdlc/skills/$name" ~/.cursor/skills/
done

# Project-scoped
mkdir -p .cursor/skills
for name in _sdlc repository-archaeology change-planning implement-change test-design pr-review-ruling; do
  cp -R "projects/sdlc/skills/$name" .cursor/skills/
done
```

Or symlink:

```bash
git clone https://github.com/jbaehne/agent-skills.git
cd agent-skills
mkdir -p ~/.cursor/skills
for name in _sdlc repository-archaeology change-planning implement-change test-design pr-review-ruling; do
  ln -s "$(pwd)/projects/sdlc/skills/$name" ~/.cursor/skills/"$name"
done
```

Cursor product discovery of this layout was not re-tested when the project was split. Claude Code and Codex adapters are not generated.

## Validate

From the repository root:

```bash
python3 projects/sdlc/evals/validate.py
```

Requires PyYAML already installed. The script does not install packages and does not call a model.

## Layout

```text
projects/sdlc/
├── README.md
├── docs/sdlc-suite.md
├── evals/
│   ├── validate.py
│   └── scenarios/
└── skills/
    ├── _sdlc/                 # shared contract (not a skill)
    ├── repository-archaeology/
    ├── change-planning/
    ├── implement-change/
    ├── test-design/
    └── pr-review-ruling/
```
