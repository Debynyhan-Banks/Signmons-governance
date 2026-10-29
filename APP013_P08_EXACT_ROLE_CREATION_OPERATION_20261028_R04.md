# APP-013 / 3A / P08 — normalized stable unbound role-creation operation R04

Status: CONSUMED, CONTAINED, NO RETRY. R1-W01 / APP-013 / 3A remains open.

Result: R04 started once at 9:00 p.m. Eastern and stopped at `CLI_5_IDENTITY_POLICY` with identity policy classification `INVALID` and `ROLE_DRIFT`, before any HTTPS or mutation request. Created and unknown counts are zero; private inputs and processes are absent. See `APP013_P08_R04_IDENTITY_POLICY_STOP_RESULT_20261028.md`.

Owner decision: On October 28, 2026, the owner approved operation `743447a5-f14f-4a48-8dd0-f674d024a94c` against this document's pre-decision SHA256 `cb543f36e4448f2909ef02977a6cde6e196fcb0d4cd00a59907e1d545419d119`. Authority is limited to the exact resources, calls, window, cutoff, no-retry rule and contingent read-only closeout below.

## Exact operation

- operation ID: `743447a5-f14f-4a48-8dd0-f674d024a94c`
- source: backend `334a7a3`; helper SHA256 `fffd3617c93bc14e6341eb0104abe253e7109925b4e6da10c98f10d367d41e00`
- window: October 28, 2026, 9:00–9:30 p.m. Eastern
- start cutoff: strictly before 9:15 p.m. Eastern
- normal work and any provider mutation end: 9:22 p.m.; mandatory private-input/process closeout by 9:27 p.m.; contingent read-only ownership closeout by 9:30 p.m.
- allowance: USD 0; existing owner gcloud authorization/cache refresh only; no Terminal attendance or password
- attempt policy: one fresh creation attempt, no retry

The bound controller makes exactly five CLI calls and at most nine HTTPS requests on success: active owner, exact configured project, memory-only bearer and the two exact policy reads; exact Resource Manager project metadata; exact Service Usage IAM state; one six-permission caller probe; two exact-ID role absence reads; two fixed create POSTs; and two exact readbacks. Project number exists only in process memory for the Service Usage resource and is discarded before later calls and evidence. Policy results retain only fixed shape classifications; absent, null and empty-list bindings are equivalent empty projections, while malformed values and either target-role binding fail closed.

Both create POSTs remain impossible unless project identity/lifecycle, IAM enabled state, all six permissions, both unbound policies and both exact-ID absences pass in the same attempt. The only permitted mutations are creation of the same two durable project custom roles, retained unbound:

1. `signmonsP08FirebaseUserLookup`, GA, exactly `firebaseauth.users.get`;
2. `signmonsP08ServiceAccountSignBlob`, GA, exactly `iam.serviceAccounts.signBlob`.

There is no update, undelete, delete, IAM binding, account/database/Firebase-user action, signing or user-token exchange, API-key action, runtime restoration/deployment, Stripe/payment/customer action or spending. CLI and HTTPS failures save only fixed stages, safe categories and fixed policy-shape classifications. If a create response is lost, partial or interrupted, stop without retry and record unknown ownership. Approval, if granted, also includes at most one independently bound read-only closeout before 9:30 p.m., solely to classify each target as exact retained, absent or unresolved and verify both policies remain unbound.

## Decision requested

Owner approved this exact normalized operation. It does not authorize later role bindings or Stage B authentication/runtime/payment work. Accepted counts remain unchanged. **No scope deviation; execute once only within the bound window.**
