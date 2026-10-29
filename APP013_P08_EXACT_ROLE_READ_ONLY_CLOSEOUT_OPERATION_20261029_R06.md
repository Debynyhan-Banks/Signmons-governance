# APP-013 / 3A / P08 — exact role read-only closeout operation R06

Status: OWNER DECISION REQUIRED FOR THIS EXACT READ-ONLY EXTERNAL OPERATION. R1-W01 / APP-013 / 3A remains unchanged.

## Exact operation

- operation ID: `e9124155-47a9-4478-a8de-3e435d67459a`
- source: backend `feb7540`; helper SHA256 `e1fbc15d95450da7662db684e2cfe6f063c8a60fd7c8243053e5431fc3f973f9`
- window: October 29, 2026, 7:15–7:45 a.m. Eastern
- start cutoff: strictly before 7:30 a.m. Eastern
- all reads end: 7:37 a.m.; mandatory private-input/process closeout by 7:42 a.m.; operation ends 7:45 a.m.
- allowance: USD 0; existing owner gcloud authorization/cache refresh only; no Terminal attendance or password
- attempt policy: one fresh read-only closeout attempt, no retry

The bound closeout makes exactly five CLI reads and at most two HTTPS GETs: active owner, exact configured project, memory-only bearer, project policy and dedicated-identity policy; then one GET for each exact role. It requires both policies to contain neither target role. Each role must be absent or match its exact name, title, description, one permission and GA stage. Omitted `deleted` normalizes to false; explicit true/non-boolean and every other definition mismatch fail closed. Evidence retains only fixed classifications, hashes and counts.

This operation has no role create/update/delete/undelete path and no IAM binding, API/secret/account/database/Firebase-user action, signing or token exchange, runtime restoration/deployment, Stripe/payment/customer action or spending. It does not reuse or retry R05 creation. Private plan/approval inputs are mandatory, mode-0600, exact-hash/window bound and deleted with absence readback.

## Decision requested

Approve or defer this exact read-only closeout. Approval would authorize only the exact reads, window, cutoff and no-retry rule above. It would not authorize creation, role binding, Stage B authentication/runtime/payment work or milestone acceptance. Counts remain unchanged. **No scope deviation.**
