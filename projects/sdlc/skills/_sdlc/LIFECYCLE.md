# SDLC suite contract

Shared rules for the portable skills in the SDLC project (`projects/sdlc`). This is not a runtime. `_sdlc` is not a skill: it has no `SKILL.md`.

Repository-local instructions override this file. This file overrides an agent's generic habits. Do not rewrite a consuming repository's policy from here.

## Lifecycle

```text
REQUEST → DISCOVER → PLAN → AUTHORIZE → IMPLEMENT → VERIFY → REVIEW → HUMAN DECISION → RELEASE → OBSERVE
```

| Stage | Skill | Does not mean |
|-------|--------|----------------|
| DISCOVER | `repository-archaeology` | a plan or permission to edit |
| PLAN | `change-planning` | authorization to implement |
| AUTHORIZE | human | the agent may not grant this to itself |
| IMPLEMENT | `implement-change` | verification, approval, commit, or deploy |
| VERIFY | `test-design` plus commands actually run | a merge ruling |
| REVIEW | `pr-review-ruling` | human approval or permission to merge |
| HUMAN DECISION | person | an agent field named approval |
| RELEASE / OBSERVE | not in this version | a successful production outcome |

## Invariants

- Discovery is not planning.
- Planning is not authorization.
- Implementation is not verification.
- Verification is not approval.
- An implementer must not approve its own change.
- Review evidence applies to a specific revision.
- A materially changed revision invalidates earlier review conclusions.
- `REQUEST CHANGES` returns work to implementation.
- Deployment does not imply operational success.
- Missing evidence is not passing evidence.
- Access is not authorization.

## Evidence

The field contract is [`evidence.yaml`](evidence.yaml). That file is authoritative for what fields mean.

When a filled record exists, it is authoritative for revision ids, which commands ran, and the `state` flags. Human-readable output must not contradict it. The review's first line (`APPROVE` or `REQUEST CHANGES`) is authoritative for the ruling a reader sees and must match `review.ruling`.

`state.human_approved` stays false unless a human decision was observed. Do not set `state.verified` or `state.reviewed` for a revision that was not actually checked or reviewed.

Emit a filled record when handing off between roles or when the user asks for one. Otherwise keep the same distinctions in prose: passed, failed, not run, inferred, and unknown stay separate.

## Roles

These are compositions, not processes to launch.

### Change Agent

Uses `repository-archaeology`, `change-planning`, `implement-change`, and `test-design`.

It cannot approve its own work, merge, push, or deploy.

### Independent Reviewer

Uses `repository-archaeology`, `pr-review-ruling`, and inspection of test evidence. Uses infrastructure or release review only when those skills exist and the change needs them.

It re-reads the diff at the recorded revision. It does not copy the implementer's conclusions.

### Release Steward

Would use release readiness, infrastructure review when applicable, evidence validation, and post-release checks.

Those skills are not in this version. Do not deploy without explicit authorization. Do not treat this role as available tooling.

### SDLC Maintainer

Keeps this contract, compatibility notes, and skill evaluations. May propose changes to the suite. Must not silently redefine another repository's policies.

## Judgment versus deterministic checks

Deterministic checks establish facts when they are actually run: format, lint, types, tests, schema validation, links, secret scanning, dependency scanning, infrastructure validation, required metadata, generated-file drift.

Agent judgment includes whether the request was understood, whether the change meets intent, whether tests cover meaningful behavior, whether a failure path is realistic, whether rollback is credible, and whether residual risk is acceptable.

Record the command and the outcome you observed. A script that searches review prose for headings is not one of these checks.

## Priority

Spend attention in this order: correctness; security and privacy; data loss and irreversible change; compatibility and migrations; operational reliability; test coverage; maintainability; performance when it matters; style.

Style alone is not a merge blocker.
