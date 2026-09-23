# APP-013 / P06 R11 controlled-refusal observability change request

Status: owner decision required. No implementation or external action has occurred.

Decision ID: `4c905715-6259-446b-be7b-1e2e6240125e`

## Requirement traceability

- Approved section: APP-013/2B, P06 R11 supervised connected-browser acceptance.
- Acceptance criterion: one protected journey verifies phone access, confirms an eligible address, explicitly submits the reviewed draft and creates exactly one job only when all current evidence and policy checks pass; refusal must be truthful and progress retained.
- Demonstrated gap: enabled21 returned a synchronous HTTP 409 before address reservation, with no job. The route catches the internal exception before the global filter, and its unwired diagnostic seam retains only operation/status, so the failing gate cannot be identified.
- Connected-workflow value: identify the exact server gate before another paid/customer-operated run, repair that gate locally, and preserve a future live attempt for actual R11 acceptance rather than another blind diagnostic.

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
