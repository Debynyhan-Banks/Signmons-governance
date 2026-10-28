# APP-013 / 3A / P08 — exact corrected Stage A diagnostic operation

Status: PROPOSED; owner decision: PENDING. R1-W01 / APP-013 / 3A / P08. Operation ID `5b04cb0d-ecbc-44c5-a026-d3b8c814f1d5`; decision ID `6c5fd85d-d447-4fc3-8d0c-b2f3bdb450fb`. Backend source `4511b63487890f9bc437600225cc8c4f70fb634b`; launcher source manifest SHA256 `869cc37faab44ed294e5625c75075e2cb26ee4ceaf8d7d0459a1457db9be667e`; correction proposal/result `832407d` / backend `4511b63`.

This exact document preselects the operation UUID before owner approval. It is not authority while status/owner decision remain pending. Separate approval must be recorded and committed before the deterministic builder may create a private plan.

<!-- P08_OPERATION_BINDING
{"automaticRetryAllowed":false,"backendCommit":"4511b63487890f9bc437600225cc8c4f70fb634b","decisionId":"6c5fd85d-d447-4fc3-8d0c-b2f3bdb450fb","mode":"P08_STAGE_A_EXTERNAL","operationId":"5b04cb0d-ecbc-44c5-a026-d3b8c814f1d5","ownerPrincipal":"debynyhan@signmons.com","projectId":"signmons","proposalCommit":"e758c79","service":"policytroubleshooter.googleapis.com","serviceRetention":"RETAIN_IF_ENABLED","sourceManifestSha256":"869cc37faab44ed294e5625c75075e2cb26ee4ceaf8d7d0459a1457db9be667e","stageBAllowed":false,"tuples":[["signmons-calldesk-p07-runtime@signmons.iam.gserviceaccount.com","//cloudresourcemanager.googleapis.com/projects/signmons","firebaseauth.users.get"],["debynyhan@signmons.com","//cloudresourcemanager.googleapis.com/projects/signmons","firebaseauth.users.get"],["debynyhan@signmons.com","//cloudresourcemanager.googleapis.com/projects/signmons","firebaseauth.users.update"],["debynyhan@signmons.com","//iam.googleapis.com/projects/signmons/serviceAccounts/signmons-calldesk-p07-runtime@signmons.iam.gserviceaccount.com","iam.serviceAccounts.signBlob"]],"window":{"cleanupEnd":"2026-10-29T12:27:00Z","cutoff":"2026-10-29T12:15:00Z","purgeEnd":"2026-10-29T12:30:00Z","start":"2026-10-29T12:00:00Z","workEnd":"2026-10-29T12:22:00Z"}}
-->

## Exact window and authority

- October 29, 2026, 8:00–8:30 a.m. Eastern.
- Start strictly before 8:15; normal work ends 8:22; process closeout by 8:27; private-plan purge before 8:30.
- One attempt/no retry. Start, refusal, interruption, success or unknown provider outcome consumes it.
- No attendance, Terminal input or password. Existing signed-in owner host authorization/cache refresh only.
- Incremental spending allowance USD 0. Stop if a paid requirement or incompatible dependency appears.

## Exact sequence

The deterministic builder must read the committed approved document, verify its SHA256 and copy the preselected operation/decision IDs unchanged into one private `0600` plan. The unchanged launcher then verifies source/document/plan, current owner, exact Signmons project and canonical project-number fingerprint before acquiring one memory-only bearer.

The launcher performs one exact Policy Troubleshooter service-state GET. If already `ENABLED`, it does not mutate. If exactly `DISABLED`, it submits one enable request, polls only its returned operation at most six times, requires exact enabled response/readback and retains the service enabled as `RETAIN_IF_ENABLED`. It never disables, forces, bypasses dependencies or resubmits an ambiguous mutation.

It then submits exactly the four pinned diagnostics for runtime/owner Firebase Auth access and owner service-account signing. Only four `CAN_ACCESS` results make Stage A a Stage B candidate; Stage B action remains unauthorized. Maximum three gcloud commands and thirteen HTTPS requests, or five HTTPS requests when preenabled.

Closeout clears the bearer, terminates children, purges model scratch, writes sanitized result and deletes the private plan with absence readback. A lost enable response is `ENABLE_OUTCOME_UNKNOWN`, never retried. Unconfirmed closeout reports `CONTAINMENT_UNCONFIRMED` and stops.

No API Keys/key lifecycle, Firebase user action, signing/token exchange, IAM grant/role, database/runtime/secret, Stripe/payment/event/customer action, deployment, billing change or extra allowance. No consumed operation/document/plan may be reused or rewritten.

Observable result: four current diagnostic verdicts plus verified local closeout, or an exact safe stop. Success authorizes only preparation of the separately governed Stage B card. Accepted 1A/1B/2A/2B, 4/8; 0/27 newly closed R1, 6/60 legacy, 0/13 intelligence unchanged. **No scope deviation.**
