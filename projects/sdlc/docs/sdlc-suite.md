# SDLC skill suite

Portable instructions for coding agents. The suite covers discovery, planning, implementation, test design, and independent review. It does not deploy, merge, or approve on a human's behalf.

This document belongs to the **SDLC project** at `projects/sdlc/`. Chief of Staff lives in a separate project and is not part of this lifecycle.

Canonical skill text is `skills/<name>/SKILL.md` under this project. Shared rules that must not be copied into every skill live in [`skills/_sdlc/`](../skills/_sdlc/). `_sdlc` is not a skill.

Repository-local instructions override this suite. The suite overrides an agent's generic habits.

## Included skills

| Order | Skill | Role in the lifecycle |
|-------|--------|------------------------|
| Discover | [`repository-archaeology`](../skills/repository-archaeology/SKILL.md) | Map the repo, commands, and Git boundary |
| Plan | [`change-planning`](../skills/change-planning/SKILL.md) | Bound the work without authorizing it |
| Implement | [`implement-change`](../skills/implement-change/SKILL.md) | Apply an explicit authorization, smallest change |
| Verify | [`test-design`](../skills/test-design/SKILL.md) | Map risks to tests; record what actually ran |
| Review | [`pr-review-ruling`](../skills/pr-review-ruling/SKILL.md) | `APPROVE` or `REQUEST CHANGES` for one revision |

## Lifecycle

```text
REQUEST → DISCOVER → PLAN → AUTHORIZE → IMPLEMENT → VERIFY → REVIEW → HUMAN DECISION → RELEASE → OBSERVE
```

Normative invariants, role compositions, and the split between judgment and deterministic checks are in [`skills/_sdlc/LIFECYCLE.md`](../skills/_sdlc/LIFECYCLE.md).

Roles are documentation, not a multi-agent runtime:

- **Change Agent** discovers, plans, implements, and designs tests. It cannot approve its own work.
- **Independent Reviewer** re-reads the revision and rules on it. It does not copy the implementer's conclusions.
- **Release Steward** is specified only. Release and infrastructure skills are deferred, and this role cannot deploy without explicit authorization.
- **SDLC Maintainer** keeps this contract and the evaluations. It does not redefine another repository's policies.

## Evidence

[`skills/_sdlc/evidence.yaml`](../skills/_sdlc/evidence.yaml) is the authoritative field contract.

A filled record is authoritative for revision ids, commands, and `state` flags. The review's first line is authoritative for the ruling a person reads and must match `review.ruling`. `state.human_approved` is true only when a human decision was observed.

Passed, failed, and not-run checks stay distinct. Missing evidence is not a pass.

## How repositories override this suite

Agents read the consuming repository's own instructions first (`AGENTS.md`, `CLAUDE.md`, Cursor rules, contribution guides, CI, and documented commands, when those files exist). Use this suite for the lifecycle and the review shape only where the repository does not define one. Do not import another organization's planning cadence, authority model, or governance terms into that repository.

## Tool compatibility

| Tool | Status |
|------|--------|
| Cursor | Layout matches this repo's skill convention: a folder with `SKILL.md` frontmatter. Install with the commands in [../README.md](../README.md). Not exercised inside the Cursor product in the change that added the suite. |
| Claude Code, Codex, other Markdown agents | No separate adapter. Use the same `SKILL.md` files. Native discovery in those products was not tested. Do not assume a vendor-specific path works. |

There is one canonical copy of each policy. Do not hand-maintain a second copy per tool.

## Validate

From the repository root:

```bash
python3 projects/sdlc/evals/validate.py
```

The script checks skill frontmatter, relative links, the evidence contract, and evaluation-fixture shape. It uses PyYAML if that library is already installed. It does not install packages and it does not call a model.

## Evaluations

Behavioral fixtures live in [`evals/`](../evals/README.md). They state invariants such as ruling, claims to avoid, and prohibited actions. `evals/validate.py` checks that the fixtures are well formed. It does not score model output.

## Contributing

Extend an existing skill when the behavior belongs there. Put shared policy in `skills/_sdlc/` instead of pasting it into each `SKILL.md`. See [CONTRIBUTING.md](../../../CONTRIBUTING.md) at the repository root.

## Deferred

| Candidate | Why it is not in this version |
|-----------|--------------------------------|
| `release-readiness` | The implemented path stops at a human review decision. This repository has no release tooling to ground a readiness skill. |
| `infrastructure-review` | Only matters when infrastructure changes are in the diff. Nothing in this repository demonstrates that pattern. `pr-review-ruling` already ranks operational risk when those files appear. |
| `documentation-maintenance` | Not required to finish discover through review. `implement-change` already updates authoritative docs when behavior changes. |
| Generated tool adapters | Would fork the canonical text before any tool-specific loading was tested. |
| A multi-agent runtime | This repository does not have one, and roles are compositions of skills. |
