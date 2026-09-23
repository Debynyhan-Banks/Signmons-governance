# APP-013 / P06 R11 controlled-refusal observability change request

Status: alternative 1 locally implemented and verified on 2026-09-23. No external action is authorized.

Decision ID: `4c905715-6259-446b-be7b-1e2e6240125e`

## Requirement traceability

- Approved section: APP-013/2B, P06 R11 supervised connected-browser acceptance.
- Acceptance criterion: one protected journey verifies phone access, confirms an eligible address, explicitly submits the reviewed draft and creates exactly one job only when all current evidence and policy checks pass; refusal must be truthful and progress retained.
- Demonstrated gap: enabled21 returned a synchronous HTTP 409 before address reservation, with no job. The route catches the internal exception before the global filter, and its unwired diagnostic seam retains only operation/status, so the failing gate cannot be identified.
- Connected-workflow value: identify the exact server gate before another paid/customer-operated run, repair that gate locally, and preserve a future live attempt for actual R11 acceptance rather than another blind diagnostic.

## Approved implementation card

- Source: backend `34efe187a4897723a40e114936a1eb8b88579adf`; governance `9316fdc7cb4444ad84d42f6999ae405d865ad340`.
- Reuse: `CustomerConsentBrowserTransport`'s existing diagnostic callback and failure isolation; `CustomerIntakeContinuationService` current-state gates; `ControlledIntakeVerificationService` current-verification gates; `LoggingService`; existing controlled transport/runtime, disposable-database and packet verification tests.
- Behavior: attach one internal non-enumerable/fixed-enum refusal stage to server-created controlled 409 errors; preserve it across intake/verification boundaries; expose it only to the internal diagnostic callback; log only a fixed marker, operation `submit`, HTTP 409 and the allowlisted stage. Browser status/body/headers remain generic and unchanged.
- Expected interfaces/files: one small controlled-refusal module; controlled continuation and verification construction points; browser diagnostic type/catch; runtime logging resource/wiring; main startup injection; focused unit and existing runtime/browser verification harnesses; evidence and synchronized governance status.
- Data/state/identity/retention: no new database field, row, migration, browser field, identifier, provider datum or retained customer input. No request/session/tenant ID, phone, code, address, token, draft, provider body, exception text or stack enters the diagnostic. The fixed stage is process output subject to existing Cloud logging retention; it grants no authority and changes no admission state.
- Finite checklist: define and validate enum carrier; tag intake-state, life-safety and current-verification 409s; propagate only the enum to the existing callback; require enabled runtime logger and emit the fixed marker; update harness resources; add privacy/failure-isolation/positive-negative tests; run focused and full required gates; record evidence and commit.
- Tests: positive stage extraction and logging; untagged/non-submit/non-409 suppression; generic browser response; no private serialization; logger/diagnostic failure isolation; missing current phone before address dispatch; accepted submit unchanged; malformed/unauthorized paths unchanged; existing concurrency/recovery/loaded-browser/disposable-database suites; build, lint, architecture and governance checks.
- Dependencies/owners: implementation owner is Codex under decision `4c905715-6259-446b-be7b-1e2e6240125e`; the owner separately controls every build or live action. No provider, secret or production dependency is needed locally.
- Exclusions: packet/image build, live database, LOGIN, activation, deployment, provider request, verification code, browser/customer action, hold release, secret/IAM or billing change, live execution and acceptance claim.
- Rollback/disabled state: removing the new internal carrier/wiring restores the prior generic response path; disabled runtime remains closed and touches neither logger nor secrets. A diagnostic callback or logger failure cannot change the response or application outcome.
- Observable finish: all specified tests/checks pass; evidence lists exact files/commands; backend and governance commits are clean. This completes only the local observability repair, not R11 acceptance. P06 remains 12/14.

## Alternatives

### Alternative 1 — recommended: local fixed-enum stage observability

Implement a bounded internal diagnostic contract for controlled submit only. It will classify failures using fixed non-private enums at existing server-owned checkpoints, pass only `{ operation, status, refusalStage }` through the existing diagnostic seam, and wire the enabled runtime to the existing logging service. It must never include exception text, request identifiers, phone, code, address, token, draft, provider response, stack or database content.

Expected files are limited to the controlled intake verification/composition or continuation boundary, browser transport diagnostic type, enabled runtime wiring and focused tests. Tests must prove each allowlisted stage, generic browser output, zero private fields, diagnostic failure isolation, success behavior, no job on refusal, and no provider/database behavior change. Run focused suites, full test/lint/build/architecture gates, governance checks and `git diff --check`. This approval would cover local implementation and testing only.

After local review, any image build, packet, LOGIN, activation, deployment, provider request, verification code, browser action or live execution would require separate approval. A future supervised attempt may still reveal a real gate that needs repair; this change ensures it will produce a precise, privacy-safe result instead of another blind 409.

### Alternative 2 — historical database reconstruction

Prepare another owner-operated read-only database diagnostic to infer historic pre-address gates. This is weaker: the phone operation ledger is encrypted, transient runtime/process state is gone, and closeout changed current session state. It may require secret access or remain inconclusive. Not recommended.

### Alternative 3 — rerun unchanged

Create another packet and repeat the browser journey without new observability. The same generic HTTP 409 can recur with no branch evidence and consume more provider/customer effort. Rejected.

## Decision requested

Approve or refuse alternative 1. Approval does not authorize a packet, build, LOGIN, activation, deployment, provider request, verification code, browser/customer action, database write, hold release, secret/IAM change, billing change or live execution. Existing holds remain unchanged. P06 remains 12/14 with R11/full R12 open. No scope deviation has been implemented.

## Implementation result

The approved fixed-enum carrier, browser diagnostic propagation and enabled-runtime logging connection are complete. The browser continues to receive the same generic response. Only tagged controlled submit 409s can emit `CONTROLLED_INTAKE_REFUSAL` with one of three allowlisted stages; no private or identifying value is included. Disabled startup still avoids resource access, and logging failure cannot alter the application outcome.

Five focused suites passed 275 tests. The full suite passed 2,363 tests with three existing skips. Build, lint, architecture, packet tests, the 16-check/26-migration disposable PostgreSQL 18 verifier, and the full restricted-role/eight-scenario loopback browser/database harness passed with synthetic providers and zero live calls. See backend `evidence/APP-013/p06-r11-controlled-refusal-observability.md`.

Local implementation is complete; R11 remains open. No image, packet or external action is authorized. Approved observability deviation only; no other scope deviation.
