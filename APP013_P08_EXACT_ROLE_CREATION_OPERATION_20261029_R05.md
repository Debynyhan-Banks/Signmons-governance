# APP-013 / 3A / P08 — root-null-corrected stable unbound role-creation operation R05

Status: OWNER APPROVED FOR THIS EXACT EXTERNAL OPERATION. R1-W01 / APP-013 / 3A remains unchanged.

Owner decision: On October 29, 2026, the owner approved operation `bdbbbe2c-3142-4b3f-8acf-98414f3e35a9` against this document's pre-decision SHA256 `b5260cb277238c60a9c797e68e8b0371d15e128155337225b0d3eb41bedb18db`. Authority is limited to the exact resources, calls, window, cutoff, no-retry rule and contingent read-only closeout below.

## Exact operation

- operation ID: `bdbbbe2c-3142-4b3f-8acf-98414f3e35a9`
- source: backend `c165a92`; helper SHA256 `44735e0f90de00e8062ab08cefe20e33448e732d3181f55c515ae5ad5e2b636d`
- window: October 29, 2026, 7:00–7:30 a.m. Eastern
- start cutoff: strictly before 7:15 a.m. Eastern
- normal work and any provider mutation end: 7:22 a.m.; mandatory private-input/process closeout by 7:27 a.m.; contingent read-only ownership closeout by 7:30 a.m.
- allowance: USD 0; existing owner gcloud authorization/cache refresh only; no Terminal attendance or password
- attempt policy: one fresh creation attempt, no retry

The bound controller makes exactly five CLI calls and at most nine HTTPS requests on success: active owner, exact configured project, memory-only bearer and the two exact policy reads; exact Resource Manager project metadata; exact Service Usage IAM state; one six-permission caller probe; two exact-ID role absence reads; two fixed create POSTs; and two exact readbacks. Project number exists only in process memory for the Service Usage resource and is discarded before later calls and evidence. Policy results retain only fixed shape classifications. Root/field null, absent and empty-list bindings are equivalent empty projections; malformed roots/values and either target-role binding fail closed.

Both create POSTs remain impossible unless project identity/lifecycle, IAM enabled state, all six permissions, both unbound policies and both exact-ID absences pass in the same attempt. The only permitted mutations are creation of the same two durable project custom roles, retained unbound:

1. `signmonsP08FirebaseUserLookup`, GA, exactly `firebaseauth.users.get`;
2. `signmonsP08ServiceAccountSignBlob`, GA, exactly `iam.serviceAccounts.signBlob`.

There is no update, undelete, delete, IAM binding, account/database/Firebase-user action, signing or user-token exchange, API-key action, runtime restoration/deployment, Stripe/payment/customer action or spending. Failures save only fixed stages, safe categories and fixed policy-shape classifications. If a create response is lost, partial or interrupted, stop without retry and record unknown ownership. Approval, if granted, also includes at most one independently bound read-only closeout before 7:30 a.m., solely to classify each target as exact retained, absent or unresolved and verify both policies remain unbound.

## Decision requested

Owner approved this exact root-null-corrected operation. It does not authorize later role bindings or Stage B authentication/runtime/payment work. Accepted counts remain unchanged. **No scope deviation; execute once only within the bound window.**
