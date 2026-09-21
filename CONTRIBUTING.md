# Contributing

Thanks for improving this collection. Keep skills public-safe, focused, and easy to install.

## Repository shape

This repo hosts **multiple projects**. Put new work in the project it belongs to:

| Project | Path | When to use it |
|---------|------|----------------|
| SDLC | `projects/sdlc/` | Discovery, planning, implementation, test design, PR/MR review |
| Chief of Staff | `projects/chief-of-staff/` | Briefings, commitments, open loops, prioritization |

Do not mix Chief of Staff content into the SDLC suite, or the reverse.

## Skill conventions

* **One skill per folder** under `projects/<project>/skills/<kebab-case-name>/`
* **Required file:** `SKILL.md` with YAML frontmatter:
  * `name` — lowercase letters, numbers, hyphens; max 64 chars
  * `description` — what the skill does **and** when to use it (trigger phrases); max 1024 chars; third person
* **Keep `SKILL.md` lean** — prefer under ~500 lines; put deep detail in `reference.md`
* **No secrets** — strip personal areas, employer specifics, credentials, private URLs, and internal process that others cannot use
* **Optional companions:** `examples.md`, `reference.md`, `scripts/`
* **Shared starter:** [`templates/SKILL.template.md`](./templates/SKILL.template.md)

## Adding a skill

1. Choose the project (`sdlc` or `chief-of-staff`)
2. `mkdir projects/<project>/skills/my-skill`
3. Copy `templates/SKILL.template.md` → `projects/<project>/skills/my-skill/SKILL.md`
4. Write clear instructions; add examples if the output format matters
5. Update that project's `README.md` (and the root README project table only if you add a new project)
6. For SDLC changes, run `python3 projects/sdlc/evals/validate.py`

## Description checklist

* States **what** the skill does
* States **when** to apply it (user phrases / situations)
* Written in third person (injected into agent context)
* Specific enough to avoid false triggers

## SDLC project notes

Lifecycle skills share one contract in `projects/sdlc/skills/_sdlc/`. Do not paste that policy into each `SKILL.md`.

* Extend an existing SDLC skill when the behavior belongs there
* Add a skill only when it is a separate stage with its own trigger and exclusion
* Keep consuming-repository instructions higher priority than the suite
* Do not claim a tool adapter works until that tool has loaded the skill
* Add a scenario under `projects/sdlc/evals/scenarios/` when you add an invariant; do not assert exact prose

See [projects/sdlc/docs/sdlc-suite.md](./projects/sdlc/docs/sdlc-suite.md).

## PR tips

* Prefer small, focused changes (one skill, one project concern, or one fix per PR)
* Use conventional commits: `feat`, `fix`, `docs`, `chore`
* If adapting a private workflow, generalize it before publishing
