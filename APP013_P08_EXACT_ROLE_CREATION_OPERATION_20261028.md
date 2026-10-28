# APP-013 / 3A / P08 — exact stable unbound role-creation operation

Status: CONSUMED; STOPPED BEFORE HTTPS OR MUTATION; CONTAINMENT VERIFIED; NO RETRY. R1-W01 / APP-013 / 3A remains unchanged.

Result: The operation started once at 7:20 p.m. Eastern and stopped on CLI call 4, the IAM service-state read, with sanitized reason `COMMAND_FAILED`. Zero HTTPS and zero mutation requests occurred; created and unknown counts are both zero. Private inputs and processes are absent. See `APP013_P08_EXACT_ROLE_CREATION_STOP_RESULT_20261028.md`.

Owner decision: On October 28, 2026, the owner approved operation `ee86cf8f-078d-42da-a4bd-04b95909e32c` against this document's pre-decision SHA256 `e854db8b760e000fb2c4448343923a99e83fc537e166832583600d6348da7270`. Authority is limited to the exact resources, calls, window, cutoff, no-retry rule and contingent read-only closeout below.

## Exact operation

- operation ID: `ee86cf8f-078d-42da-a4bd-04b95909e32c`
- source: backend `7650009`; helper SHA256 `a7134a14c0d1f1a1027fae4f61cecc2f5016876011ebdddb4d8d19ac9727ec1b`
- window: October 28, 2026, 7:20–7:50 p.m. Eastern
- start cutoff: strictly before 7:35 p.m. Eastern
- normal work and any provider mutation end: 7:42 p.m.; mandatory private-input/process closeout by 7:47 p.m.; contingent read-only ownership closeout by 7:50 p.m.
- allowance: USD 0; existing owner gcloud authorization/cache refresh only; no Terminal attendance or password
- attempt policy: one creation attempt, no retry

The bound controller makes at most six CLI calls and seven HTTPS requests in this order: exact active owner, exact project, memory-only OAuth bearer, IAM service state, project policy and dedicated service-account policy; one four-permission `testIamPermissions` request; two exact-ID role GETs accepting only 404 as absence; two fixed create POSTs; and two exact readback GETs. Both create POSTs are impossible unless all four permissions are returned, IAM is enabled, both policies contain neither target role and both exact IDs are absent in the same attempt.

The only permitted mutations are creation of these two durable project custom roles, retained unbound:

1. `signmonsP08FirebaseUserLookup`, GA, exactly `firebaseauth.users.get`;
2. `signmonsP08ServiceAccountSignBlob`, GA, exactly `iam.serviceAccounts.signBlob`.

There is no update, undelete, delete, IAM binding, account/database/Firebase-user action, signing or user-token exchange, API-key action, runtime restoration/deployment, Stripe/payment/customer action or spending. Raw bearer, policy bodies, error bodies and private inputs are never retained. Sanitized evidence contains only stages, status classifications, counts, hashes and ownership state.

If a create response is lost, partial or interrupted, the controller stops without retry and records unknown ownership. This approval, if granted, also includes at most one independently bound read-only closeout invocation before 7:50 p.m.: five CLI reads and two exact role GETs, with no permission probe or mutation, solely to classify each target as exact retained, absent or unresolved and verify both policies remain unbound. It cannot adopt, update or delete a role.

## Decision requested

Owner approved this exact operation. It does not authorize later role bindings or Stage B authentication/runtime/payment work. Accepted counts remain unchanged. **No scope deviation; execute once only within the bound window.**
