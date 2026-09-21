# APP-013 / P06 R11 phone-admission-state diagnostic

Status: executed once; account ceiling exceeded; consumed.

The owner approved the exact operation. It reserved once at 14:56:52Z and returned `R11_PHONE_ADMISSION_STATE_DIAGNOSTIC_ACCOUNT_CEILING_EXCEEDED` at 14:57:16Z. One valid staging hold and one valid controlled hold total 1,000,000 USD micros; enabled13 required another 500,000 micros under a 1,000,000-micro ceiling. Current approval is disabled with the exact digest after verified closeout, packet reuse is false and invalid-row count is zero. The operation is consumed and must not be rerun. `APP013_P06_R11_PHONE_CEILING_CHANGE_REQUEST.md` is the next owner decision.

## Requirement traceability

- Approved section: P06-R11 controlled acceptance execution.
- Exact criterion: one protected participant journey must complete phone verification, eligible-address review and one reviewed submit, with an authoritative correlated result and exactly one job or a truthful refusal.
- Inspected gap: operation `ee81f95c-698c-40fd-949c-2560d2880c72` proved enabled13 stopped before durable phone reservation and before any provider call. The exact runtime uses `ControlledCustomerAdmission`, whose pre-reservation gate counts retained staging and controlled phone liabilities for the bound provider account and refuses malformed, reused-packet, same-session or over-ceiling state.
- Source/evidence: backend `ed9da09`; `src/communications/controlled-customer-admission.ts`; `src/communications/staging-phone-admission.ts`; exact private enabled13 runtime packet; backend evidence `evidence/APP-013/p06-r11-verification-outcome-result.md`; current pointer, board, handoff, ticket, remaining baseline, execution contract and data contracts.
- Customer workflow advanced: the result will prove or exclude retained admission liability as the cause before any repair or new supervised journey. It does not release a hold, change a ceiling or request a code.

## Fixed operation

- Operation: `bd6a6f3e-6681-4c24-803b-e6ed44248511`.
- Owner-attended window: 10:55–11:10 AM Eastern, equal to `2026-09-21T14:55:00.000Z` through `2026-09-21T15:10:00.000Z`.
- Policy source: the exact mode-0600 enabled13 runtime packet. The helper verifies its fixed hash and extracts only the controlled phone policy required to mirror admission. Policy identifiers/digests remain private.
- Identity: owner-operated hidden input connects as existing `neondb_owner`; readback confirms configured database, exact role and PostgreSQL 18.
- Transaction: `BEGIN TRANSACTION ISOLATION LEVEL REPEATABLE READ READ ONLY`, fixed tenant/approval and account-hold queries, then `ROLLBACK` and connection close.
- Query allowlist: the fixed tenant's current `controlledPhoneApproval` enabled/digest fields, plus `AuditLog` rows whose action is `conversation.staging_phone_held` or `conversation.controlled_phone_held` and whose metadata account matches the exact private policy. Read only action, tenant-equality flag, metadata version/state/currency/reserved amount, packet-equality flag and counts. Session, conversation, phone, participant, operation and provider identifiers must not enter the result.
- Output allowlist: diagnostic operation ID, one sanitized admission classification, approval state/digest-match booleans, staging/controlled/total hold counts, held/flow/ceiling micros, packet-reuse boolean, invalid-row count and timestamp.
- Single-use: create one exclusive attempt marker before hidden input/database access. Any stop or uncertainty consumes the operation; no automatic retry.

## Classification

- `ACCOUNT_CEILING_EXCEEDED`: all rows match the gate's retained-hold shape and held plus enabled13 flow upper bound exceeds its account ceiling.
- `PACKET_ALREADY_HELD`: a controlled hold already uses enabled13's packet ID.
- `INVALID_HELD_STATE`: a selected row violates the exact gate's required version/state/currency/positive-safe-integer amount shape, or the bounded row limit is exceeded.
- `CAPACITY_AVAILABLE_OTHER_GATE`: the retained ledger would admit enabled13 under its account ceiling. The remaining cause is outside this query, such as request binding/consent or live approval/window evaluation.
- `STOPPED_OR_UNCONFIRMED`: identity, read-only transaction, query, validation, rollback or result persistence did not finish.

Current approval is expected to be inactive after verified closeout and is context only; it cannot reconstruct the earlier live instant. Existing activation/readback evidence remains authoritative for the live approval state.

## Checklist, tests and boundaries

1. Verify exact clean backend, policy-packet hash, private ownership/modes, helper hashes, absent attempt/result and absent authorization before approval.
2. Run synthetic classifier cases for zero holds, mixed valid holds below/over ceiling, reused packet, malformed row and row-limit refusal.
3. After exact owner approval only, install the private helper/authorization and run the no-action check.
4. During the fixed window, accept one password through hidden TTY/anonymous FIFO, verify identity, perform the one read-only transaction, roll back, close and persist one sanitized result.
5. Reconcile the result. Hold release, ceiling change, code request, packet preparation and live execution each remain separately gated.

No LOGIN change, activation, deployment, traffic change, database write, hold release, ceiling change, provider request/mutation, verification code, browser/customer action, retry, secret/IAM change or billing change. R11 and full R12 remain open; P06 remains 12/14.

No scope deviation.
