# Contributing

Thanks for improving this collection. Keep skills public-safe, focused, and easy to install.

## Conventions

* **One skill per folder** under `skills/<kebab-case-name>/`
* **Required file:** `SKILL.md` with YAML frontmatter:
  * `name` — lowercase letters, numbers, hyphens; max 64 chars
  * `description` — what the skill does **and** when to use it (trigger phrases); max 1024 chars; third person
* **Keep `SKILL.md` lean** — prefer under ~500 lines; put deep detail in `reference.md`
* **No secrets** — strip personal areas, employer specifics, credentials, private URLs, and internal process that others cannot use
* **Optional companions:** `examples.md`, `reference.md`, `scripts/`

## Adding a skill

1. `mkdir skills/my-skill`
2. Copy `templates/SKILL.template.md` → `skills/my-skill/SKILL.md`
3. Write clear instructions; add examples if the output format matters
4. Update the skills table in `README.md`
5. Open a PR with a short description of when someone would use the skill

## Description checklist

* States **what** the skill does
* States **when** to apply it (user phrases / situations)
* Written in third person (injected into agent context)
* Specific enough to avoid false triggers

## PR tips

* Prefer small, focused changes (one skill or one fix per PR)
* Use conventional commits: `feat`, `fix`, `docs`, `chore`
* If adapting a private workflow, generalize it before publishing
