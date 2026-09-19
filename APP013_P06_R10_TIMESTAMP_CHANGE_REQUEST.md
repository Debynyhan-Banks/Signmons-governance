# APP-013 / P06 / R10 timestamp-boundary change request

## Demonstrated gap

Two owner-approved activation attempts stopped before any write. The first retained the combined `ACTIVATION_SNAPSHOT` stage. After safe stage splitting and moving the snapshot immediately after reservation, the 4:05 PM attempt returned `ACTIVATION_UPDATED_AT`. The broad `TenantOrganization.updatedAt` changed between the immediate read and the locked transaction; the controlled approval comparison was never reached. Mandatory containment returned `CLOSED`, and no deployment/provider/customer action occurred.

## Alternatives

1. **Replace the broad pre-transaction timestamp comparison with the controlled approval-pair comparison.** Keep the row lock, current tenant/status/organization/payment/category checks, exact runtime and phone digests, final database-clock authorization, in-transaction `updatedAt` compare-and-set update, audit commit, rollback, readback and no-retry behavior. This directly guards the authority being installed while allowing unrelated tenant-row timestamp movement.
2. Preserve the broad timestamp comparison and investigate every writer of `TenantOrganization.updatedAt`. This requires another separately authorized live diagnostic and may still leave legitimate unrelated updates capable of blocking activation.
3. Add a new preflight digest spanning broader tenant policy state. This duplicates the existing in-transaction authority checks and introduces a new contract and more race surfaces.

## Proposed decision

Approve alternative 1 for local controller/operator repair and tests only. The expected activation input changes from `{updatedAt, approvals}` to `{approvals}`. This does not authorize a new packet, LOGIN, activation, deployment, provider request, verification code or customer action.

## Acceptance and validation

- Activation refuses changed, active or partial controlled approvals before any write.
- Locked-row tenant status and current organization/payment/category authority checks remain unchanged.
- The existing in-transaction `updateMany({id, updatedAt})` compare-and-set and audit remain atomic and rollback on failure.
- Concurrent activation still commits once; replay, stale approvals and foreign digests refuse.
- Fixed stage evidence retains `ACTIVATION_APPROVALS`; the historical timestamp stop remains recorded but is no longer an executable pre-transaction gate.
- Controller failure still performs mandatory closeout with no retry.
- Disposable PostgreSQL 18, focused/full P06, build, lint, architecture and governance checks must pass before any future packet is proposed.

## Impact

R10 remains open and P06 remains 11/14. Task count, dependency order, provider caps, participant binding and connected journey are unchanged. Rollback is the single local repair commit. Owner decision: **pending**.
