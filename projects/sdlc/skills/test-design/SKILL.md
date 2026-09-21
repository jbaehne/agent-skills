---
name: test-design
description: >-
  Design risk-based tests for changed behavior and separate meaningful gaps
  from tests that only mirror the implementation. Use when asked which tests
  to add or how to verify a change. Do not use to issue a merge ruling or to
  claim checks passed without running them.
---

# Test design

Tie tests to risks in the change. A test that only restates the current implementation is not evidence the behavior is right.

Repository test layout, frameworks, and commands override this skill. If you do not yet know them, use `repository-archaeology` first. Do not introduce a second test stack when the repository already has one.

## Map risk to evidence

Prioritize, in order: correctness, security and privacy, data loss, compatibility and migrations, operational failure, then lesser gaps.

For each material risk, say which level can actually catch it. Use a level only when it fits the repository:

- unit — isolated behavior and boundaries
- integration — real collaborators the change depends on
- contract — an interface another system relies on
- migration — data or schema transformation, including rollback
- property — invariants across inputs, when examples would miss them
- performance — only when the change has a performance requirement
- end-to-end — a user or operator path that lower levels cannot see

For each risk worth testing, name the critical positive case, the negative or failure case, and the boundary that would invalidate the approach. Skip levels that would not change confidence.

## Recommend or add tests

If the user authorized test changes, add the smallest tests that fail when the intended behavior breaks. Otherwise recommend them and do not edit.

Do not weaken, skip, or delete existing checks to make a run pass. Do not claim a command passed unless you ran it and saw the result. If the environment cannot run a command, record it as not run and why.

Testing is not a merge ruling. Do not issue `APPROVE` or `REQUEST CHANGES` from this skill.

## Output

```markdown
## Risk to test
- Risk — level — case that would catch it

## Cases
- Positive:
- Negative or failure:
- Boundary:

## Tests
- Added: `path` — risk it covers
- Recommended, not added: what and why it was not added

## Commands
- `command`: passed — what it verified
- `command`: failed — what failed
- Not run: `command` — reason

## Coverage gaps
- Remaining risk and why it is still open
```

When handing off, record `verification` in [`../_sdlc/evidence.yaml`](../_sdlc/evidence.yaml). Do not set `state.verified` because tests were designed. Set it only when the relevant commands ran and passed for this revision.

Suite boundaries: [`../_sdlc/LIFECYCLE.md`](../_sdlc/LIFECYCLE.md).
