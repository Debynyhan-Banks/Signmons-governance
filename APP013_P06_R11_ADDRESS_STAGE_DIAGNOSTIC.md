# APP-013 / P06 R11 address-stage diagnostic

Status: executed once; request failed before address reservation; consumed.

## Requirement traceability

- Approved section: P06-R11 controlled acceptance execution.
- Exact criterion: one protected participant journey must correlate to exactly one created job; the confirmed no-job refusal does not close R11.
- Inspected gap: the exact-revision Cloud Logging diagnostic returned zero matching records and is consumed. The refusal remains unclassified.
- Source/evidence: backend `bd8e668`; `AddressVerificationRequest` and `AddressVerificationOperation` schema; `AddressOperationLedger.perform`; `ControlledIntakeVerificationService.run`; no-job receipt and unconfirmed log diagnostic evidence.
- Workflow advance: determine the latest durable address stage for the exact request before deciding whether a local repair is required.

## Exact bounded action

Operation `afd29a7b-b2aa-4c12-b894-76e85265dbec` is proposed for 8:30–8:45 AM Eastern on September 21, 2026. Using owner-operated hidden `neondb_owner` input, connect once to the fixed P06 child database, verify exact database/user/PostgreSQL 18 identity, begin a repeatable-read read-only transaction and look up only `AddressVerificationRequest.id = 2f284c84-c8be-42e7-a8e7-c6a7febd6392` joined to its same-tenant `AddressVerificationOperation`. Return only row count, opaque operation ID, state, created timestamp and whether an execution deadline exists; then roll back and close.

The owner approved the operation exactly. It reserved once at 12:31:32Z and returned `R11_ADDRESS_STAGE_DIAGNOSTIC_BEFORE_ADDRESS_RESERVATION` at 12:31:44Z. Zero rows prove the request failed before any address reservation or provider call. The operation is consumed and must not be rerun. Static comparison then demonstrated the category-name/customer-enum mismatch recorded in `APP013_P06_R11_CATEGORY_BINDING_CHANGE_REQUEST.md`.

Classify zero rows as `BEFORE_ADDRESS_RESERVATION`; one valid row as `ADDRESS_RESERVED`, `ADDRESS_DISPATCH_CLAIMED`, `ADDRESS_OBSERVED`, `ADDRESS_UNCERTAIN` or `ADDRESS_CANCELLED` from the allowlisted state. More than one row, wrong tenant, malformed state/ID/timestamp or connection ambiguity is unconfirmed. The lookup must not read phone proof, encrypted conversation data, participant fields, provider payloads, request bodies, secrets or unrelated rows.

## Finite checklist and tests

1. Bind exact operation, tenant, request, window, source/schema/target hashes and one-use authorization.
2. Validate hidden-input string framing, private modes and absence of an attempt/result before authorization.
3. Execute one read-only lookup during the approved window; no retry.
4. Fail closed on unexpected identity, count, state, shape or timing.
5. Persist only the allowlisted stage receipt, reconcile governance and run required checks.

Positive: zero or one structurally valid fixed-request row produces one stage class. Negative and recovery: any other outcome is unconfirmed and consumed. Concurrency is bounded by exclusive attempt creation. No application/schema change is part of this diagnostic.

## Dependencies, exclusions and finish

The owner approves or refuses the exact operation and enters the existing database-owner password only in the hidden local prompt. No runtime LOGIN change, activation, deployment, traffic change, provider request/mutation, verification code, browser/customer action, write, retry, payment, booking, dispatch, message, secret/IAM or billing change is authorized.

Rollback is transaction rollback and connection close. Observable finish is one durable address-stage class or an explicit unconfirmed result, followed by a local-repair decision or separately reviewed future R11 packet. R11/full R12 remain open and P06 remains 12/14. No scope or acceptance change.
