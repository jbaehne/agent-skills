# Agent Skills

Personal collection of [Cursor Agent Skills](https://cursor.com/docs) shared publicly. Each skill is a self-contained folder you can copy into your Cursor skills directory.

## Skills

| Skill | Description |
|-------|-------------|
| [`chief-of-staff`](./skills/chief-of-staff/) | Cross-channel commitments, open loops, prioritization, and executive briefings |
| [`pr-review-ruling`](./skills/pr-review-ruling/) | Verdict-first PR/MR reviews with evidence-based APPROVE or REQUEST CHANGES |

## Install

Copy a skill folder into your personal or project skills directory:

```bash
# Personal (available across all projects)
cp -R skills/chief-of-staff ~/.cursor/skills/
cp -R skills/pr-review-ruling ~/.cursor/skills/

# Project-scoped (shared with anyone using that repo)
mkdir -p .cursor/skills
cp -R skills/chief-of-staff .cursor/skills/
cp -R skills/pr-review-ruling .cursor/skills/
```

Or clone this repo and symlink:

```bash
git clone https://github.com/jbaehne/agent-skills.git
ln -s "$(pwd)/agent-skills/skills/chief-of-staff" ~/.cursor/skills/chief-of-staff
ln -s "$(pwd)/agent-skills/skills/pr-review-ruling" ~/.cursor/skills/pr-review-ruling
```

## Skill layout

```text
skills/<skill-name>/
├── SKILL.md       # Required — frontmatter + instructions
├── reference.md   # Optional — detailed reference loaded on demand
├── examples.md    # Optional — sample inputs/outputs
└── scripts/       # Optional — helper scripts
```

## Add a skill

1. Copy [`templates/SKILL.template.md`](./templates/SKILL.template.md) into `skills/<name>/SKILL.md`
2. Fill in `name`, `description` (what + when), and instructions
3. Add optional `reference.md` / `examples.md` if the main file would get long
4. Add a row to the skills table above

See [CONTRIBUTING.md](./CONTRIBUTING.md) for conventions.

## License

MIT — see [LICENSE](./LICENSE).
