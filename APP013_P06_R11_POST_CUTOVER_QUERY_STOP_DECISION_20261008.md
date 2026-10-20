# APP-013 / 2B / P06-R11 — post-cutover query-stage stop decision

## Decision status

Prepared for owner review; **no replacement execution is approved**. The October 8 operation is consumed and must never be rerun.

## Demonstrated result

Owner-approved plan `35bc028b-5583-481c-b9c1-a3e583d212e5`, operation `f896949c-680d-4826-bc26-7c8c1d15a943`, reserved at `2026-10-08T11:15:33.236Z` and stopped at `2026-10-08T11:15:46.171Z` in `CAPACITY_READ_ONLY_QUERY`. Database connection, exact `neondb_owner` identity, PostgreSQL 18 check and `REPEATABLE READ READ ONLY` transaction succeeded before the stop. The runner rolled back and closed in `finally`. No success receipt exists.

Phase B did not run. No Cloud Run, Artifact Registry or Twilio metadata was read; no provider request, message, build, deployment, traffic/tag, secret, IAM, migration, database write, hold, customer, job or browser action occurred.

The saved stage covers phone aggregate parsing, address aggregates and approval/role/session reads, so it does not identify the failing substage or prove current liability/runtime state. The package suppressed private stderr by design. Do not infer drift, headroom, a runtime problem or a database defect from this stop.

## Local repair

The demonstrated observability gap is repaired locally in `scripts/p06-r11-post-cutover-query.mjs`. It:

- marks the phone, address, approval, role and session substages separately;
- counts malformed phone-liability rows instead of throwing while parsing them;
- returns only aggregate counts, held micros, invalid counts and fixed runtime classifications;
- classifies active approval, open role, active session, invalid liability data and shape drift without exposing rows; and
- never returns execution authority.

Eleven fictional focused tests cover closed state, historical ceiling, both approvals, LOGIN, connection limit, expiry, active session, invalid liability rows and runtime shape drift. This is local diagnostic hardening only; it does not authorize another read.

## Alternatives

### Alternative 1 — one fresh replacement qualification

Approve one new 35-minute Eastern window. After approval the implementer may create a new operation identity and one-use package using the repaired substage reader. It repeats only the original read-only Phase A. Phase B may run only after a complete closed-runtime Phase A receipt and remains limited to fixed Cloud Run, immutable artifact, Twilio Verify and approved-recipient metadata. Any attempt, stop or uncertainty consumes the replacement; no automatic retry.

### Alternative 2 — pause

Retain the verified database-recovery checkpoint and consumed query-stage stop. Perform no new database, cloud or provider read.

## Exclusions and finish

No replacement operation identity, package or window exists. Excluded actions remain database writes, hold/ceiling changes, session cleanup, provider transactions, messages/codes, builds/uploads, IAM, secrets, deployment, traffic/tags, migration execution, browser/customer activity and job/payment/appointment actions.

P06 remains 12/14; R11 and full R12 remain open; accepted milestones remain 3/8. No scope deviation.
