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

## Revision binding

Record the base revision and the reviewed revision when Git can provide them. Conclusions do not carry forward to a later commit that changes the diff. If the implementer of this change is the same session, do not issue `APPROVE`.

Name the revision in the evidence record at [`../_sdlc/evidence.yaml`](../_sdlc/evidence.yaml):

- human first line `APPROVE` matches `review.ruling: approve`
- human first line `REQUEST CHANGES` matches `review.ruling: request_changes`
- no ruling matches `review.ruling: not_reviewed`

`state.human_approved` stays false until a person decides. Selecting a review button is not something this skill does unless the user explicitly asks, and asking still does not make the agent the human approver of record.

## Insufficient material

Withhold the ruling when any of these are missing and would change the result:

- the diff or the revision it belongs to
- the stated requirement, when the risk is about intent rather than an obvious defect
- whether a cited check actually ran

Say what is missing. Do not fill the gap with a plausible finding.
