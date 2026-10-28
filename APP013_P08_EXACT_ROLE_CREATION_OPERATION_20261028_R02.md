# APP-013 / 3A / P08 — corrected exact stable unbound role-creation operation R02

Status: OWNER APPROVED FOR THIS EXACT CORRECTED OPERATION. R1-W01 / APP-013 / 3A remains unchanged.

Owner decision: On October 28, 2026, the owner approved operation `2f413783-9c32-4ed5-89d1-875f383e3bca` against this document's pre-decision SHA256 `bb7530fd9f13dbdbaccce852841b0e748df111c9a0d5377ac1063b8ba5998e8f`. Authority is limited to the exact resources, calls, window, cutoff, no-retry rule and contingent read-only closeout below.

## Exact operation

- operation ID: `2f413783-9c32-4ed5-89d1-875f383e3bca`
- source: backend `0714c39`; helper SHA256 `7e5cbd4e6f68f42314bac2d12cd07cda33ed016986db646a61668d465871f430`
- window: October 28, 2026, 7:35–8:05 p.m. Eastern
- start cutoff: strictly before 7:50 p.m. Eastern
- normal work and any provider mutation end: 7:57 p.m.; mandatory private-input/process closeout by 8:02 p.m.; contingent read-only ownership closeout by 8:05 p.m.
- allowance: USD 0; existing owner gcloud authorization/cache refresh only; no Terminal attendance or password
- attempt policy: one fresh creation attempt, no retry

The corrected bound controller makes at most six CLI calls and seven HTTPS requests in the same fixed order as R01. Both create POSTs remain impossible unless the exact owner/project, IAM enabled state, all four permissions, both unbound policies and both exact-ID absences pass in the same attempt. A CLI failure now saves only its fixed stage and one safe enumerated category; raw stdout/stderr remain memory-only.

The only permitted mutations are creation of the same two durable project custom roles, retained unbound:

1. `signmonsP08FirebaseUserLookup`, GA, exactly `firebaseauth.users.get`;
2. `signmonsP08ServiceAccountSignBlob`, GA, exactly `iam.serviceAccounts.signBlob`.

There is no update, undelete, delete, IAM binding, account/database/Firebase-user action, signing or user-token exchange, API-key action, runtime restoration/deployment, Stripe/payment/customer action or spending. If a create response is lost, partial or interrupted, stop without retry and record unknown ownership. Approval, if granted, also includes at most one independently bound read-only closeout before 8:05 p.m., solely to classify each target as exact retained, absent or unresolved and verify both policies remain unbound.

## Decision requested

Owner approved this exact corrected operation. It does not authorize later role bindings or Stage B authentication/runtime/payment work. Accepted counts remain unchanged. **No scope deviation; execute once only within the bound window.**
