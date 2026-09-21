# Chief of Staff

Cross-channel operational awareness for commitments, open loops, prioritization, and executive briefings.

This project is separate from the [SDLC](../sdlc/) suite. It does not participate in that lifecycle.

## Skills

| Skill | Description |
|-------|-------------|
| [`chief-of-staff`](./skills/chief-of-staff/) | Briefings, commitment tracking, open-loop review, and next-action recommendations |

## Install

```bash
# From this repository root
cp -R projects/chief-of-staff/skills/chief-of-staff ~/.cursor/skills/

# Project-scoped
mkdir -p .cursor/skills
cp -R projects/chief-of-staff/skills/chief-of-staff .cursor/skills/

# Symlink
git clone https://github.com/jbaehne/agent-skills.git
cd agent-skills
ln -s "$(pwd)/projects/chief-of-staff/skills/chief-of-staff" ~/.cursor/skills/chief-of-staff
```

## Layout

```text
projects/chief-of-staff/
├── README.md
└── skills/
    └── chief-of-staff/
        ├── SKILL.md
        ├── reference.md
        └── examples.md
```
