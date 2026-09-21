# Agent Skills

Personal collection of [Cursor Agent Skills](https://cursor.com/docs), organized as separate projects in one repository.

## Projects

| Project | Purpose |
|---------|---------|
| [`projects/sdlc`](./projects/sdlc/) | Portable software-development lifecycle skills for coding agents |
| [`projects/chief-of-staff`](./projects/chief-of-staff/) | Cross-channel operational awareness, commitments, and executive briefings |

Install and validate from each project's README. Projects do not share skill folders; shared authoring conventions live at the repository root.

## Repository layout

```text
projects/
  sdlc/                 # SDLC suite, docs, and evals
  chief-of-staff/       # Chief of Staff skill
templates/              # Shared SKILL.md starter
CONTRIBUTING.md         # Conventions for every project
```

## Shared conventions

* One skill per folder: `projects/<project>/skills/<kebab-case-name>/`
* Required file: `SKILL.md` with `name` and `description` frontmatter
* Keep `SKILL.md` lean; put deep detail in optional `reference.md` / `examples.md`
* Start from [`templates/SKILL.template.md`](./templates/SKILL.template.md)
* Keep projects public-safe: no secrets, employer-specific process, or private URLs

See [CONTRIBUTING.md](./CONTRIBUTING.md).

## License

MIT — see [LICENSE](./LICENSE).
