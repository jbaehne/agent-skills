---
name: repository-archaeology
description: >-
  Discover repository structure, local instructions, canonical commands, and
  the Git change boundary before planning or editing. Use when entering a
  repository, when conventions are unknown, or when asked to map the repo or
  inspect working-tree state. Do not use to implement changes, write the
  implementation plan, or rule on merge readiness.
---

# Repository archaeology

Establish what this repository actually is before planning or editing. Report observed facts. Mark inferences and unknowns. Do not invent paths, tools, branches, or commands.

Repository-local instructions override this skill. If those instructions conflict, or the canonical place to change cannot be determined, stop and state the smallest decision needed.

## Inspect before concluding

Read the instructions that exist. Do not assume a file is missing until you have looked. Typical sources, when present:

- `AGENTS.md`, `CLAUDE.md`, Cursor rules, and other agent instruction files
- contribution guides, README, skill or coding standards
- package manifests, task runners, CI config, and existing validation scripts
- templates and tests that show the real layout

Then inspect the tree, Git status, and recent history far enough to name:

- the skill or code layout this repo actually uses
- build, test, lint, and validation commands that are documented or scripted
- the diff boundary for the requested work
- unrelated working-tree changes, which you must leave untouched
- architectural patterns that constrain the change
- uncertainties that would change the plan

Prefer commands the repository already documents. Do not install tools or run formatters as a side effect of discovery.

## Do not

- treat this survey as a plan or as permission to edit
- modify files, including to "tidy" unrelated dirty paths
- claim a command succeeded unless you ran it and saw the result
- assume GitHub or GitLab, or a language, from habit

## Output

Lead with the map, not a transcript.

```markdown
## Repository map
- Purpose and canonical locations (paths you confirmed)

## Applicable instructions
- Path and the rule that overrides generic defaults
- Conflicts, if any

## Commands
- Documented or scripted: `command` — source
- Not established: what you still do not know

## Git
- Revision, branch, and status
- Unrelated dirty or untracked paths to preserve

## Patterns that constrain the change
- Observed pattern — where you saw it

## Uncertainties
- Item that would change planning or editing
```

Omit empty sections. Separate what you opened or ran from what you inferred.

When handing off, fill only known fields from [`../_sdlc/evidence.yaml`](../_sdlc/evidence.yaml). Set `state.discovered` only after this survey. Leave `state.planned` and `state.authorized` false.

Suite boundaries: [`../_sdlc/LIFECYCLE.md`](../_sdlc/LIFECYCLE.md).
