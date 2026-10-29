# APP-013 / 3A / P08 — HTTPS-corrected stable unbound role-creation operation R03

Status: PROPOSED, NOT AUTHORIZED. R1-W01 / APP-013 / 3A remains unchanged.

## Exact operation

- operation ID: `d45f0618-c8a9-4c85-910a-c60c9352e9cc`
- source: backend `a64e933`; helper SHA256 `8512c89144280b8d97cacd0aca91883322948d920d14052ef08a9558756e3ec7`
- window: October 28, 2026, 8:40–9:10 p.m. Eastern
- start cutoff: strictly before 8:55 p.m. Eastern
- normal work and any provider mutation end: 9:02 p.m.; mandatory private-input/process closeout by 9:07 p.m.; contingent read-only ownership closeout by 9:10 p.m.
- allowance: USD 0; existing owner gcloud authorization/cache refresh only; no Terminal attendance or password
- attempt policy: one fresh creation attempt, no retry

The bound controller makes exactly five CLI calls and at most nine HTTPS requests on success: active owner, exact configured project, memory-only bearer and the two exact policy reads; exact Resource Manager project metadata; exact Service Usage IAM state; one six-permission caller probe; two exact-ID role absence reads; two fixed create POSTs; and two exact readbacks. The project number exists only in process memory for the Service Usage resource and is discarded before later calls and evidence.

Both create POSTs remain impossible unless project identity/lifecycle, IAM enabled state, all six permissions, both unbound policies and both exact-ID absences pass in the same attempt. The only permitted mutations are creation of the same two durable project custom roles, retained unbound:

1. `signmonsP08FirebaseUserLookup`, GA, exactly `firebaseauth.users.get`;
2. `signmonsP08ServiceAccountSignBlob`, GA, exactly `iam.serviceAccounts.signBlob`.

There is no update, undelete, delete, IAM binding, account/database/Firebase-user action, signing or user-token exchange, API-key action, runtime restoration/deployment, Stripe/payment/customer action or spending. CLI and HTTPS failures save only fixed stages and safe categories. If a create response is lost, partial or interrupted, stop without retry and record unknown ownership. Approval, if granted, also includes at most one independently bound read-only closeout before 9:10 p.m., solely to classify each target as exact retained, absent or unresolved and verify both policies remain unbound.

## Decision requested

Approve this exact HTTPS-corrected operation, or defer it. Approval authorizes only the facts and window above. It does not authorize later role bindings or Stage B authentication/runtime/payment work. Accepted counts remain unchanged. **No scope deviation; R03 external action remains pending owner approval.**
