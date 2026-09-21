---
name: change-planning
description: >-
  Turn a requested change into a bounded plan with acceptance criteria, risks,
  validation, and stop conditions. Use when the user asks for a plan, approach,
  or design and has not asked to edit code. Do not use to implement, commit,
  or approve the change.
---

# Change planning

Convert the request into a plan that someone else could implement without expanding it. Planning is not authorization to implement.

If repository conventions are not already established, use `repository-archaeology` first. Repository-local instructions override this skill. If they conflict, stop and name the conflict.

## Bound the work

- Restate the objective in the user's terms. Do not add goals they did not ask for.
- Split requested work from optional improvements. Optional work stays out of scope.
- Name acceptance criteria that can be checked, including behavior that must stay the same.
- Name the components the change is expected to touch, based on the survey, not a guessed layout.
- Order the implementation in the smallest coherent sequence.
- Name the validation to run, using repository commands when they exist, and what would count as not run.
- State risks, rollback needs, and stop conditions. Stop conditions include missing authority, conflicting instructions, and unrelated dirty work you cannot safely preserve.

State material assumptions. Distinguish facts you observed from inferences.

## Do not

- edit files while planning
- treat the plan as approval to commit, push, merge, deploy, or spend money
- turn style preferences or drive-by cleanup into acceptance criteria
- claim tests or builds passed because they are listed in the plan

## Output

End with an explicit non-authorization line.

```markdown
## Objective

## In scope

## Out of scope

## Acceptance criteria

## Affected components

## Sequence

## Validation plan
- `command` — what it would verify
- Not planned: `command` — why

## Risks and stop conditions

This plan is not authorization to implement.
```

Omit sections that do not apply, except the non-authorization line.

When handing off, record scope, unresolved requirements, and `state.planned: true` using [`../_sdlc/evidence.yaml`](../_sdlc/evidence.yaml). Leave `state.authorized` false until the user explicitly authorizes implementation.

Suite boundaries: [`../_sdlc/LIFECYCLE.md`](../_sdlc/LIFECYCLE.md).
