# APP-013 / 2B / P06-R11 — post-cutover qualification decision

## Decision status

Prepared for owner review; **not approved for execution**. The verified database credential cutover is complete and consumed. This card does not reopen or reuse that operation.

The recommended next section is one fresh, read-only qualification that stops before any build, deployment, provider transaction, verification message, browser journey, allowance change, database write or customer/job action. The owner must choose Alternative 1 and supply a future 35-minute Eastern window before a new operation identity, helper or external query is prepared.

## Approved section and acceptance criterion

- Section: APP-013 / 2B / P06-R11, with R12 containment and reconciliation.
- Criterion: one correlated protected phone-verification, eligible-address and reviewed-submit journey creates exactly one job and returns an authoritative receipt; invalid, stale or ineligible input returns a truthful no-job result while preserving recoverable progress.
- This decision advances only the prerequisite state review. It does not accept R11/2B, add an acceptance section, change the denominator, or authorize a journey.

## Current immutable checkpoint

- Credential recovery plan `ffcaf1f0-6c0d-4ac8-9358-52bdae15f000`, operation `3db3aa7d-974f-466e-a536-b5330be53afa`, ended `R11_DB_AUTH_RECOVERY_VERIFIED` at `2026-10-08T00:20:58.000137Z`.
- Shared database secret version 4 is enabled and pinned numerically by normal revision `signmons-calldesk-staging-app013dbrot2` and migration job `signmons-calldesk-migrate`; versions 2 and 3 are disabled, not destroyed.
- Normal traffic and `app013-bounds` are 100 percent on `app013dbrot2`; `p06-intake-disabled` remains zero-traffic; no enabled or temporary recovery tag remains.
- Migration execution count remains seven and latest execution remains September 7 `signmons-calldesk-migrate-jrq7h`; pre-reset owner sessions were zero; readiness was HTTP 200; child secret version 2 was unchanged.
- Every cutover stage is consumed and must never be rerun. No credential reset, new secret version, migration execution or database recovery action belongs to this decision.

## Source and release evidence to preserve

- Focused backend branch baseline: `3cf8a9dc53d0282a35e6263a36d749c5b32f8e2e`, with pre-existing reviewed local APP-013 changes preserved.
- Last connected-journey release candidate: commit `37f156f220507ac3bb97e73dc46c9d4dc33db727`, tree `7c3428d8851dd313b9c28882bf7c33aa703e1e05`, archive SHA-256 `a60a00e2380cd66c9f1b63e9222223ad7cf2512e687d465a2e1bbae8728e35ee`.
- Its one successful build was `5fed9c20-0d5f-46f6-853d-a6fe4aa850fa`, image digest `sha256:0fd8185f496861902bef3bfad76e081aec21b0d573b25ab08de6a340d666b70a`.
- The enabled35 execution and its packages are consumed. A future qualification may verify immutable artifact existence and identity; it may not reuse an old plan, approval, operation ID, revision suffix or runtime packet.

## Demonstrated unknowns

The last verified pre-LOGIN enabled35 balance was 15 phone holds / USD 7.50 and nine overlapping address operations / USD 0.90 for each account and tenant scope. Enabled35 reached a pending phone-code state and closed without preview, submit, request reference or job receipt. Current post-run phone/address liabilities were never read. Current runtime approval/role/session state has historical closeout evidence but needs one fresh snapshot before another release decision.

The October 7 cutover verified database connectivity and consumer pinning only. It did not refresh liability totals, Twilio/test-recipient readiness, immutable journey-image availability or future zero-traffic release eligibility.

## Alternative 1 — one stop-gated read-only qualification

Approve one future 35-minute Eastern window for these ordered phases. The implementer prepares a new one-use operation only after approval. Any attempt, uncertainty or terminal receipt consumes the operation; there is no automatic retry.

### Phase A — liability and runtime snapshot

1. Bind a fresh operation identity, exact production database target, fixed tenant/account identities, source hashes and approved window.
2. After a hidden owner prompt, accept the current production Connect credential without displaying, logging or persisting it.
3. In one repeatable-read, read-only transaction, return only:
   - valid phone hold count and held micros;
   - overlapping address account and tenant operation counts and held micros, plus invalid-row count;
   - controlled phone/runtime approval booleans;
   - `p06_intake_runtime` login, connection-limit and expiry state;
   - active `p06_intake_runtime` session count.
4. Exclude phone numbers, addresses, verification codes, customer fields, protected payloads, provider responses, job contents and unrelated rows.
5. Roll back, close the connection, remove temporary credential material and then save a fixed sanitized receipt.
6. Any active approval, open runtime role, nonzero runtime session, invalid row, query drift, authentication failure or missing receipt stops before Phase B.

Phase A records current state only. Historical ceilings are comparison context, not renewed allowance. No headroom result authorizes a phone/address call or journey.

### Phase B — provider and release metadata

Run only if Phase A produced a complete closed-runtime receipt:

1. Read current Cloud Run service/revision/traffic/tag metadata and require normal traffic 100 percent on `app013dbrot2`, numeric database secret version 4, preserved `p06-intake-disabled`, and no enabled/candidate tag.
2. Read Artifact Registry metadata for the exact immutable journey image digest and verify its source binding; do not upload or build.
3. Reuse the existing allowlisted provider-readiness collectors to classify current Twilio Verify service/settings and the approved test recipient, without sending a message, starting a verification, changing settings or returning provider secrets.
4. Record fixed classifications only. Any missing artifact, configuration drift, unapproved recipient state, traffic/tag mismatch or ambiguous provider result stops with `QUALIFICATION_DRIFT_STOP`.

Observable finish is `POST_CUTOVER_QUALIFICATION_REVIEWABLE`, `LIABILITY_DECISION_REQUIRED`, `QUALIFICATION_DRIFT_STOP`, or a truthful consumed stop. Even `POST_CUTOVER_QUALIFICATION_REVIEWABLE` authorizes only a later exact release/journey proposal.

## Alternative 2 — pause

Retain the verified credential recovery checkpoint. Perform no database, cloud or provider read and prepare no release or journey operation.

## Required implementation and validation after approval

- Reuse the existing balance/runtime reader projections and hidden-input/no-retry guards; create a new wrapper, plan, approval and operation identity rather than modifying consumed packages.
- Add focused fictional tests for closed-state success, exhausted/changed liabilities, active approval, open role, active session, invalid row, authentication stop, Phase B skip, provider drift and consumed-operation refusal.
- Validate Python/JavaScript syntax as applicable, source/approval hashes, exclusive file set/modes, no-action `--check`, architecture, governance baseline/consistency, 21 governance tests and whitespace.
- No browser QA, application build or full runtime suite is required for preparation because the section changes no application behavior. Any later release proposal must independently restore the appropriate build/lint/test/browser gates.

## Owners, exclusions and finish

- Owner: choose Alternative 1 or 2; for Alternative 1 provide the future window and privately enter the current credential only after the hidden prompt.
- Implementer: after approval, prepare/test the exact one-use qualification package, execute only the approved read phases, inspect sanitized receipts and stop for a separate release/allowance decision.
- Excluded: database writes, hold release/reset, ceiling or allowance increase, session cleanup, provider transaction, message/code, build/upload, IAM, secret/version change, deployment, traffic/tag mutation, migration execution, browser/customer action, job/appointment/payment action and retry.
- Rollback/disabled state: read-only transaction rolls back; runtime and controlled approvals remain disabled; normal traffic and tags remain unchanged.

P06 remains 12/14; R11 and full R12 remain open; accepted 1A/1B/2A remain 3/8. No scope deviation.
