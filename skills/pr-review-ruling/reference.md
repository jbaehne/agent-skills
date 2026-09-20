# PR Review Ruling — Reference

Load this when assigning severity, validating findings, or mapping the ruling to GitHub or GitLab review UI.

## Severity labels

| Label | Use when | Effect on ruling |
|-------|----------|------------------|
| `Blocking` | Specific, substantiated defect makes merge unsafe or fails an explicit requirement | Requires `REQUEST CHANGES` |
| `Non-blocking` | Real improvement that is optional for this merge | May accompany `APPROVE` |
| `Nit` | Editorial or stylistic preference with no material impact | May accompany `APPROVE` |

## Finding checklist

Before publishing a finding, confirm:

1. The issue is introduced or exposed by this change (not pre-existing noise).
2. It is not already prevented by another path, guard, or test you observed.
3. You can describe a realistic failure path (user, system, data, security, or ops impact).
4. The citation points to the narrowest useful file and line or diff hunk.
5. The requested correction is the smallest acceptable behavior change, not a preferred rewrite.

If any of these fail, convert the finding into a question or omit it.

## What does not justify REQUEST CHANGES

- Personal style preference without a correctness, safety, or requirements impact
- Speculative concerns without a plausible failure path
- Missing unrelated cleanup elsewhere in the codebase
- Optional refactors that would improve maintainability but are not required for this change
- Incomplete material for a meaningful review — say what is missing instead of inventing a ruling

## Platform mapping

| Ruling | GitHub review | GitLab review |
|--------|---------------|---------------|
| `APPROVE` | Approve | Approve |
| `REQUEST CHANGES` | Request changes | Request changes |

Repository branch protection, required reviewers, and permissions decide whether the UI selection actually blocks merge. State the ruling clearly; do not claim enforcement you have not verified.

## Suggested section order

1. Ruling line (`APPROVE` or `REQUEST CHANGES`)
2. One- or two-sentence rationale
3. `## Findings` (omit if empty; blocking first)
4. `## Verification` (commands run / not run)
5. `## Residual risks` (only if material)
