# PR Review Ruling — Examples

## Sample APPROVE

```markdown
APPROVE

The change satisfies the stated requirements, and I found no merge-blocking defects. The focused tests covering the changed behavior pass.

## Findings

- **Non-blocking — Cache key omits tenant id** (`src/cache.ts:88`): Cross-tenant cache hits are unlikely today because keys are namespaced by route, but including `tenantId` would make the invariant explicit. Optional if you expect shared cache infra later.

## Verification

- `npm test -- cache`: passed — unit tests for the key builder and invalidation
- Not run: full e2e suite — not required for this scoped cache change

## Residual risks

- Invalidation still depends on the existing TTL path; no new failure mode introduced.
```

## Sample REQUEST CHANGES

```markdown
REQUEST CHANGES

Merging would allow unauthenticated callers to delete other users' drafts via the new endpoint.

## Findings

- **Blocking — Missing authorization on delete** (`api/drafts.ts:142-156`): `DELETE /drafts/:id` loads the draft by id and deletes it without checking `draft.ownerId === req.user.id`. Any authenticated user who guesses or obtains an id can delete another user's draft. Require an ownership (or equivalent) check before delete, and add a test that a non-owner receives 403/404.

- **Non-blocking — Soft-delete vs hard-delete** (`api/drafts.ts:150`): The handler hard-deletes. If product expects recoverability, switch to the existing soft-delete helper; otherwise document the hard-delete choice in the PR.

## Verification

- `npm test -- drafts`: failed — no authorization coverage for delete; existing create and list tests pass
- Not run: staging smoke — blocked on the authorization fix

## Residual risks

- The same missing ownership check may exist on `PATCH` if it follows the same pattern. That is out of scope unless this pull request touches `PATCH`.
```
