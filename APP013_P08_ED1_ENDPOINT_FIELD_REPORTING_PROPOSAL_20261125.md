# APP-013 / 3A / P08 — ED1 endpoint-field reporting correction

Current status: local ED1 continuation and implementation are complete; see APP013_P08_ED1_LOCAL_DECISION_20261125.md and APP013_P08_ED1_LOCAL_COMPLETION_20261125.md. The proposal and pending-decision language below is the preserved pre-implementation record, not current status or external authority.

PROPOSED, NOT APPROVED. Local implementation and synthetic tests only. Current backend head `badc26fbe79ed87523a944d813db1bee856f6caf`; executable R58 source `2f13f90ae4cda3a61e719308d54cc19c1dd3c0d1`. R58 operation `46930f3d-edaf-48c0-a633-66b24b2af018` is consumed and must not be replayed. No provider read, credential action, endpoint mutation, payment, browser action or fresh connected session is authorized by this proposal.

## Requirement traceability and demonstrated gap

Section `3A` requires the same admitted job's Sandbox payment, authentic matching signed event, application gate clearance and owner acceptance. `APP013_REMAINING_EXECUTION_CONTRACT.md` requires exact mode, account, amount, currency and signed-event evidence; redirect or Checkout presentation alone is insufficient. `DATA_CONTRACTS.md` keeps the approved payment policy fail-closed with webhook validation required. ED1 advances that connected workflow only by making the existing preflight's next failure reviewable before another attended payment attempt. It does not satisfy any 3A exit criterion.

R58 stopped before authentication, browser opening or Checkout at aggregate `PAYMENT_ENDPOINT_DRIFT`. Retained evidence intentionally omits the provider body, so the mismatched endpoint field remains `UNKNOWN`. Inspected source shows the current predicate checks object type, exact endpoint identity/fingerprint, Sandbox mode, exact URL, API version, exact enabled-event set, recognized status and the initially required disabled status. The existing one-request `endpointOnce` / `--endpoint-once` seam in `evidence/APP-013/p08-key-correction-20261110/key_check.mjs` safely performs the pinned GET, but line 54 collapses every predicate failure back to the same aggregate code. Existing tests require that aggregate result. Repeating the unchanged seam cannot produce the required field-specific observation.

## Proposed bounded behavior

Add one pure, finite endpoint comparison projection beside the existing `endpoint` predicate in `evidence/APP-013/p08-native-entry-local-20261101/source/connected_payment.mjs`. The production-equivalent predicate must consume the same projection, so ED1 cannot create a looser diagnostic definition. Reuse that projection only in the existing `endpointOnce` OBSERVE path. Do not add a second provider request, new provider client, ambient credential resolution or a broad logging branch.

The safe result may contain only these fixed labels, each with `MATCH`, `MISMATCH` or `TYPE_INVALID`: `objectType`, `endpointIdentity`, `sandboxMode`, `url`, `apiVersion`, `enabledEvents`, `recognizedStatus`, and `disabledStatus`. `endpointIdentity` covers both exact ID equality and its pinned digest without returning either value. `enabledEvents` compares the exact sorted set without returning event names. The result may retain the existing bounded request count, HTTP status, phase, aggregate code and `scope`; it must not retain raw response fields, IDs, URLs, event lists, account data, request headers, secret material, hashes derived from provider values or exception text. Multiple mismatches remain multiple finite labels; missing/null/wrong-type values are `TYPE_INVALID`, not stringified.

The native acceptance predicate, its aggregate `PAYMENT_ENDPOINT_DRIFT` code, one-attempt/no-retry behavior, initial-disabled requirement, cleanup, deadlines and all existing refusal semantics remain unchanged. ED1 must not retrospectively identify R58's mismatch. Its local finish proves only that a future separately authorized one-GET observation can identify safe comparison categories.

## Expected files and reuse

Expected backend changes are limited to:

- `evidence/APP-013/p08-native-entry-local-20261101/source/connected_payment.mjs`
- `evidence/APP-013/p08-native-entry-local-20261101/source/test_connected_payment.mjs`
- `evidence/APP-013/p08-key-correction-20261110/key_check.mjs`
- `evidence/APP-013/p08-key-correction-20261110/test_key_check.mjs`
- affected current source guards/manifests and a new local-only ED1 verification record

Current SHA256 pins inspected for the two implementation files are `c6f11db3b9eb833bc742d1afed694f4ef2ce4414ff831264f77d84cc0b9a90d9` for `connected_payment.mjs` and `4553225c8ef3b70512b91ee7a8cb2b60ac631d98f63091e8a709d197203543fe` for `key_check.mjs`. Any source drift requires renewed inspection before implementation. Historical receipts, R58 evidence and raw private artifacts are immutable and excluded.

## Finite implementation and test checklist

1. Add the pure finite projection and make the existing endpoint predicate consume it without changing its pass/fail set.
2. Add the projection to the existing one-request OBSERVE result only after bounded HTTP/JSON handling; preserve one request, input clearing and generic transport/output refusal.
3. Test every field independently as `MATCH`, `MISMATCH` and, where structurally applicable, `TYPE_INVALID`; test multiple simultaneous failures without raw values.
4. Test missing/null/array/object/string/boolean confusion, duplicate and reordered event lists, unrecognized status, enabled-versus-required-disabled status, malformed JSON, non-200 response, timeout, interruption and secret/input clearing.
5. Prove the native endpoint acceptance matrix is byte-for-behavior equivalent: all prior valid cases still pass and every prior invalid case still raises aggregate `PAYMENT_ENDPOINT_DRIFT`.
6. Run the affected key-correction, native payment, source-guard and manifest checks; record local evidence and stop before any external action.

Required validation after approval: focused Node suites for both files; complete affected native/key-correction suites; committed source guards and manifest verification; backend governance baseline, architecture and whitespace; governance frozen baseline, complete cross-repository consistency, all 25 safeguard tests and whitespace. Build, lint, database and browser gates are inapplicable unless implementation inspection finds a compiled application, schema, database or UI change; such a finding exceeds this card and requires a new decision rather than silent expansion.

## Boundaries, ownership and decision

No endpoint status change, event-list change, URL/API-version change, Stripe Dashboard/API observation, credential renewal/sign-in, payment retry, Checkout, webhook resend, provider configuration, deployment, billing change or customer data action is included. No new section, subsystem, acceptance criterion, denominator or queue transition is proposed. Rollback is a reviewable git revert of the local classifier/reporting change; all live paths remain separately authority-gated.

Implementer owns the local code, tests, source pins and evidence only after approval. The product owner decides whether to approve this exact local ED1 scope. The Stripe custodian separately owns any future one-GET observation or configuration decision; local approval would not authorize either. The next observable local result is a review-ready ED1 correction proving finite field labels without changing endpoint acceptance. The later external result, if separately approved, must identify the mismatched category or explicitly retain `UNKNOWN`.

Accepted `1A/1B/2A/2B` remain **4/8**; `3A` remains OPEN; R1 newly closed remains **0/27**. Explicit bounded correction proposal recorded before implementation; owner decision **PENDING**. No scope deviation has been implemented.
