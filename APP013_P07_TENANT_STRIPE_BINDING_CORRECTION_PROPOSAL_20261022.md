# APP-013 / 3A / P07 tenant Stripe binding correction proposal

Status: **owner decision pending; no local implementation or external mutation authorized**.

## Requirement traceability and demonstrated gap

- Approved section: R1-W01 / APP-013/3A/P07.
- Unchanged acceptance criterion: the accepted job opens one authorized Stripe Sandbox Checkout from its approved payment policy, and only an authentic signed event for the exact stored Stripe resource may clear that job's payment gate.
- Inspected evidence: consumed diagnostic operation `8f71217a-d384-4a0c-87da-3d3703a4201f` passed current Stripe Sandbox qualification, returned all three corrected database rows, then stopped `P07_DIAGNOSTIC_STOP_CONNECTED_ACCOUNT_FORMAT` with verified containment.
- Missing prerequisite: the exact tenant exists, but its stored `stripeConnectAccountId` is absent or malformed. Because format validation failed first, the current `chargesEnabled` value remains unknown.
- Source boundary: `TenantOrganization.stripeConnectAccountId` is nullable and `chargesEnabled` defaults false. Payment creation requires both; webhook tenant resolution uses the stored account. No current product service owns their setup.
- Customer-workflow connection: correct tenant-to-Sandbox binding is required before policy enforcement can create a Checkout or a signed event can settle the same job.

## Alternatives

| Alternative | Effect | Recommendation |
| --- | --- | --- |
| 1. Prepare one guarded, audited tenant-binding correction | Build and locally test a disabled one-use controller that can bind only the exact tenant to the current enabled Sandbox account and set `chargesEnabled=true`, with hidden input, exact hash matching, conditional update, same-transaction audit and readback. A later mutation still requires a fresh window and separate exact approval. | **Recommended** |
| 2. Run another read-only diagnostic | Could reveal the Boolean flag but cannot repair the already-proven invalid account binding and would consume another attended window. | Reject |
| 3. Build full Stripe Connect onboarding/configuration UI now | Creates a product inside the product: onboarding states, capability polling, account replacement, error UX, authorization, audit and recovery. Preserve this architecture for a later release rather than making it a 3A prerequisite. | Defer beyond R1 |

## Exact proposed local preparation and tests

Create a fresh disabled private package with new plan, packet and operation identifiers. It may contain only the controller, tests, manifest, README and sanitized evidence needed for this correction.

The future operator path must:

1. require a fresh signed-in Stripe Sandbox read showing administrator access, exactly one connected account, account status Enabled and destination absence;
2. accept the account identifier twice through hidden Terminal input, require exact equality and `acct_[A-Za-z0-9]{8,}` format, compare its SHA-256 with the sanitized browser receipt, and clear it from memory after use;
3. never place the raw identifier in chat, command arguments, files, logs, exceptions, receipts or audit metadata;
4. use the current CHILD administrator connection only inside one bounded transaction for the exact plan-bound tenant and accepted job;
5. lock and recheck one active tenant, one undeleted `CREATED` job, no Payment row, no calendar event or operation, the controlled-admission digest, and a currently absent/malformed tenant account; stop before write on any drift;
6. update only that tenant's `stripeConnectAccountId`, `chargesEnabled` and required `updatedAt` value;
7. create a same-transaction `AuditLog` row with the operation ID, actor type, exact tenant entity, the new account SHA-256 and fixed before/after classifications, without either raw account value;
8. require exactly one conditional update and one audit row, then commit and perform a separate sanitized readback of account-hash equality, `chargesEnabled=true` and audit presence;
9. treat an uncertain commit as consumed and allow recovery to read the exact post-state only, never repeat the update; and
10. close all database sessions and retain fixed receipts with `automaticRetryAllowed:false`.

Local tests must cover positive commit, malformed/different/double-entry account refusal, browser-hash mismatch, already-valid binding refusal, missing or changed tenant/job, payment/calendar/policy drift, conditional-update loss, audit failure rollback, competing update, uncertain-commit recovery, deadlines/signals, receipt privacy, no retry and zero-session cleanup. At least the commit, rollback, concurrency and recovery paths must run against a disposable local PostgreSQL database with synthetic rows.

No application source, production configuration UI, role/grant, secret/IAM, Stripe setting, destination, deployment, Checkout, payment, booking, customer contact, message, merge or push is included in Alternative 1 local preparation.

## Dependencies, rollback and later external gate

Local preparation depends only on the current schema, accepted job/tenant identifiers, the sanitized diagnostic result and disposable synthetic PostgreSQL. It must remain disabled without a window and an exact owner-approval record.

A later external proposal must separately bind the reviewed package hashes, fresh attended window, strict cutoff, exact tenant/account digest, hidden inputs, zero-dollar allowance, no retry, audit/readback and containment. Before commit, any failure rolls back. After a verified commit, rollback means a separately reviewed corrective transaction; the controller must not automatically restore an invalid prior value.

Successful tenant binding would remove one P07 prerequisite only. The disabled webhook destination, dedicated runtime credential/identity, zero-traffic deployment, P08 authentic Sandbox payment and owner acceptance would remain open.

## Decision requested

Approve or refuse **Alternative 1 for local preparation and testing only**. Approval would not authorize a live database connection, tenant mutation, Stripe change, deployment or payment.

Accepted progress remains **0/27 newly closed R1 packages; 6/60 legacy packages; 4/8 walkthrough milestones; 0/13 full-intelligence rows**. **Proposed prerequisite correction; not implemented.**
