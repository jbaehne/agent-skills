---
name: implement-change
description: >-
  Implement an explicitly authorized plan as the smallest coherent change,
  preserving unrelated work and local conventions. Use when the user asks to
  implement, apply, or make a specified change. Do not use for planning-only
  requests, merge approval, commits, pushes, or deploys.
---

# Implement change

Make the authorized change and nothing beyond it. Implementation is not verification, review, or permission to publish.

## Authorization

Proceed only when the user has explicitly asked you to implement. A plan, a review comment, or access to the repo is not authorization.

If repository conventions or the change boundary are unclear, use `repository-archaeology` before editing. If a written plan exists, follow its in-scope list. If new work appears mid-change, stop and report it instead of absorbing it.

Repository-local instructions override this skill.

## While editing

- Match local conventions you have actually seen.
- Preserve unrelated working-tree changes. Do not revert, reformat, or commit them.
- Prefer the smallest coherent change that meets the acceptance criteria.
- When behavior changes, update the tests and the authoritative docs that this repository already uses for that behavior. Do not create new doc systems.
- When the risk mapping is unclear, use `test-design` before adding a large test surface.
- Do not add dependencies, services, accounts, or credentials unless the authorized scope says so.

## After editing

Run the narrowest relevant checks the repository already provides, when that is permitted and practical. Record the exact command and whether it passed, failed, or did not run. An environment failure is `not_run` or a limitation, not a pass.

Do not commit, push, open a pull or merge request, merge, deploy, or approve the change unless the user explicitly asks for that action in addition to implementation. Even then, do not approve work you just implemented.

## Output

```markdown
## Files changed
- `path` — why it changed

## Behavior changed

## Validation
- `command`: passed — what it verified
- `command`: failed — what failed
- Not run: `command` — reason

## Limitations and unresolved decisions

## Git status
- Paths this change touched
- Unrelated dirty paths left untouched

This implementation is not approval, and it was not committed unless you asked for a commit.
```

When handing off, record files, behavior, verification, and `state.implemented` from [`../_sdlc/evidence.yaml`](../_sdlc/evidence.yaml). Set `state.verified` only for checks that actually ran and passed for this revision. Leave `state.reviewed` and `state.human_approved` false.

Suite boundaries: [`../_sdlc/LIFECYCLE.md`](../_sdlc/LIFECYCLE.md).
