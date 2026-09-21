# APP-013 / P06 R11 verification-outcome diagnostic

Status: executed once; no durable reservation; consumed.

The owner approved the exact operation. It reserved once at 14:35:35Z and returned `R11_VERIFICATION_OUTCOME_DIAGNOSTIC_NO_RESERVATION` at 14:35:50Z, with zero matching reservation/observation rows in the fixed enabled13 evidence interval. Because the durable service commits its reservation before adapter invocation, no Twilio Verify SDK request occurred. The operation is consumed and must not be rerun. The smallest next step is a separately reviewed read-only fixed-policy admission-state diagnostic; retained-hold exhaustion is a source-supported candidate, not yet a confirmed result.

## Requirement traceability

- Approved section: P06-R11 controlled acceptance execution.
- Exact criterion: one protected participant journey must complete phone verification, eligible-address review and one reviewed submit, with an authoritative correlated result and exactly one job or a truthful refusal.
- Inspected gap: repaired enabled13 reached one phone-code request, but the owner received no code and the browser retained an unconfirmed verification outcome. The plan was closed safely and consumed. The durable verification service records a reservation before any provider invocation and a sanitized observation after the invocation, so their fixed-window audit pair is the smallest authoritative read that can distinguish no reservation, reserved/unobserved, and an observed adapter outcome.
- Source/evidence: backend `e6e0ea3`; `src/communications/durable-verification.service.ts`; `src/communications/twilio-verify.adapter.ts`; `prisma/schema.prisma`; backend evidence `evidence/APP-013/p06-r11-1000-verification-unconfirmed-closeout.md`; current execution pointer, board, handoff, ticket, remaining baseline, remaining execution contract and data contracts.
- Customer workflow advanced: the result determines whether a later reviewed R11 packet may address a provider refusal/rate limit, reconcile an unknown request, or investigate a pre-provider reservation failure. It does not resend a code or resume the customer journey.

## Fixed operation

- Operation: `ee81f95c-698c-40fd-949c-2560d2880c72`.
- Owner-attended window: 10:35–10:50 AM Eastern, equal to `2026-09-21T14:35:00.000Z` through `2026-09-21T14:50:00.000Z`.
- Evidence interval: `2026-09-21T14:06:30.000Z` through `2026-09-21T14:22:40.000Z`, covering enabled13 activation through verified closeout.
- Fixed tenant: the existing isolated P06 tenant. Its UUID remains only in the private operation files and query binding.
- Identity: owner-operated hidden input connects as existing `neondb_owner`; readback must confirm the configured database, exact role and PostgreSQL 18 before the evidence query.
- Transaction: `BEGIN TRANSACTION ISOLATION LEVEL REPEATABLE READ READ ONLY`, one fixed query, then `ROLLBACK` and connection close.
- Query allowlist: `AuditLog` rows for the fixed tenant, entity type `Conversation`, actor `verification-session`, actions `conversation.verification_reserved` and `conversation.verification_observed`, and the fixed evidence interval. The helper may read only action, created timestamp and metadata fields `operationId`, `attemptId`, `kind`, `outcome`, `sdkInvocations` and `billing`.
- Output allowlist: operation ID for this diagnostic, one sanitized classification, zero-to-two matching row count, matching opaque verification operation/attempt IDs, kind, observed outcome, SDK invocation count, billing class and minimal timestamps. It must not retain entity/conversation IDs, phone/address/name/code/session values, provider identifiers or raw metadata.
- Single-use: reserve one `attempt.json` before hidden input/database access; any stop or uncertainty consumes the operation. No automatic retry.

## Classification

- `NO_RESERVATION`: no matching durable row exists.
- `RESERVED_UNOBSERVED`: exactly one valid reservation exists and no matching observation exists. A provider invocation may have occurred; retain the unknown billing hold and do not retry.
- `OBSERVED_PENDING`, `OBSERVED_APPROVED`, `OBSERVED_EXPIRED`, `OBSERVED_REFUSED`, `OBSERVED_RATE_LIMITED` or `OBSERVED_UNKNOWN`: one valid reservation and its one valid observation share operation ID, attempt ID and kind; report only the allowlisted outcome metadata.
- `INCONSISTENT_OR_MULTIPLE`: any unmatched observation, duplicate, unexpected shape/value or more than one verification operation in the interval. Stop without choosing a provider conclusion.
- `STOPPED_OR_UNCONFIRMED`: identity, transaction, query, validation, rollback or evidence persistence did not finish. Do not rerun.

## Finite checklist

1. Confirm clean exact backend source, private directory/file ownership and modes, fixed hashes, absent attempt/result and absent authorization before approval.
2. After exact owner approval only, install the private helper and exact authorization, then run its no-action check.
3. During the fixed window, accept one password through the existing hidden-TTY/anonymous-FIFO handoff. Do not expose or persist it.
4. Verify database/user/PostgreSQL 18 identity, enter the read-only repeatable-read transaction, run the one allowlisted query, validate and classify, roll back, close and write the sanitized result once.
5. Record the result in governance/evidence and decide the smallest next repair or reconciliation. Any later packet, provider console read, code request or journey requires separate review and approval.

## Tests and boundaries

- Positive local tests: prepared review passes without authorization; approved no-action check validates hashes/authorization but makes no database connection; synthetic row fixtures cover each permitted classification.
- Negative tests: wrong source/hash/mode/owner/window/authorization/identity, an existing attempt/result, unexpected action/metadata/value, duplicate or unmatched rows, query/rollback failure and non-FIFO input all stop closed.
- Concurrency/recovery: one exclusive attempt file prevents duplicate execution. A reserved/unobserved result remains uncertain and cannot grant retry authority. Rollback and connection close are mandatory in success and failure cleanup.
- Browser/provider tests: none. This operation must not open a browser, call Twilio, request/check a code or contact a customer.
- Data/retention: private credentials remain transient; sanitized opaque evidence is retained for the governed decision; no raw provider response or participant data is retained.

## Exclusions and finish

No LOGIN change, activation, deployment, traffic change, database write, provider request or mutation, verification code, browser/customer action, job, payment, booking, dispatch, message, secret/IAM change or billing change. Observable finish is one sanitized classification or an explicit consumed unconfirmed stop, followed by documentation. R11 and full R12 remain open; P06 remains 12/14.

No scope deviation.
