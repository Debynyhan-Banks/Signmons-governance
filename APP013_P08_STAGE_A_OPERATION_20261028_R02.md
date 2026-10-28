# APP-013 / 3A / P08 — exact native-handoff-corrected Stage A operation

Status: PROPOSED; owner decision: PENDING. R1-W01 / APP-013 / 3A / P08. Operation ID `dbd958ce-d0d6-43fe-a8b9-c5aef89334ab`; decision ID `625f96c7-97d2-48b4-928b-db6211f25e5f`. Backend source `03fccb41f6f40dd77b966b6d76764ec0bd3d8448`; launcher source manifest SHA256 `88d152858b6002b0fac32ced0b8a4ff05e4c082f56c2e946a36439006993d27a`; native-handoff proposal/result governance `eb7da75` / `4974b44`, backend `03fccb4`.

This exact document preselects the operation UUID before owner approval. Approval authorizes only this October 28 window, retention decision, one attempt and exclusions. Approval supersedes and cancels unstarted operations `40c0b189-d440-42d9-826e-b9117b40d938` and `5b04cb0d-ecbc-44c5-a026-d3b8c814f1d5`; neither may ever be built or run afterward.

<!-- P08_OPERATION_BINDING
{"automaticRetryAllowed":false,"backendCommit":"03fccb41f6f40dd77b966b6d76764ec0bd3d8448","decisionId":"625f96c7-97d2-48b4-928b-db6211f25e5f","mode":"P08_STAGE_A_EXTERNAL","operationId":"dbd958ce-d0d6-43fe-a8b9-c5aef89334ab","ownerPrincipal":"debynyhan@signmons.com","projectId":"signmons","proposalCommit":"e758c79","service":"policytroubleshooter.googleapis.com","serviceRetention":"RETAIN_IF_ENABLED","sourceManifestSha256":"88d152858b6002b0fac32ced0b8a4ff05e4c082f56c2e946a36439006993d27a","stageBAllowed":false,"tuples":[["signmons-calldesk-p07-runtime@signmons.iam.gserviceaccount.com","//cloudresourcemanager.googleapis.com/projects/signmons","firebaseauth.users.get"],["debynyhan@signmons.com","//cloudresourcemanager.googleapis.com/projects/signmons","firebaseauth.users.get"],["debynyhan@signmons.com","//cloudresourcemanager.googleapis.com/projects/signmons","firebaseauth.users.update"],["debynyhan@signmons.com","//iam.googleapis.com/projects/signmons/serviceAccounts/signmons-calldesk-p07-runtime@signmons.iam.gserviceaccount.com","iam.serviceAccounts.signBlob"]],"window":{"cleanupEnd":"2026-10-28T21:57:00Z","cutoff":"2026-10-28T21:45:00Z","purgeEnd":"2026-10-28T22:00:00Z","start":"2026-10-28T21:30:00Z","workEnd":"2026-10-28T21:52:00Z"}}
-->

## Exact window and authority

- Today, October 28, 2026, 5:30–6:00 p.m. Eastern.
- Start at or after 5:30 and strictly before 5:45; normal work ends 5:52; process closeout by 5:57; private-plan purge before 6:00.
- One attempt/no retry. Start, refusal, interruption, success or unknown provider outcome consumes it.
- No attendance, Terminal input or password. Existing signed-in owner host authorization/cache refresh only.
- Incremental spending allowance USD 0. Stop if a paid requirement or incompatible dependency appears.
- Approval supersedes/cancels both previously approved unstarted operations; no second authority survives.

## Exact sequence

At or after 5:30, the source-locked coordinator reads current owner and exact project once, constructs the private plan from this committed approved `_R02` document, and reuses those two in-memory values during launcher qualification. Only the bearer request delegates afterward: exactly three actual CLI commands total—owner, project and bearer—with no duplicate project read.

The launcher verifies source/document/plan and canonical project fingerprint, then performs one exact Policy Troubleshooter service-state GET. If already `ENABLED`, it does not mutate. If exactly `DISABLED`, it submits one enable request, polls only its returned operation at most six times, requires exact enabled response/readback and retains the service enabled as `RETAIN_IF_ENABLED`. It never disables, forces, bypasses dependencies or resubmits an ambiguous mutation.

It submits exactly four pinned diagnostics for runtime/owner Firebase Auth access and owner service-account signing. Only four `CAN_ACCESS` results make Stage A a Stage B candidate; Stage B remains unauthorized. Maximum three actual CLI commands and thirteen HTTPS requests, or five HTTPS requests when preenabled.

Closeout clears the bearer, terminates children, purges model scratch, writes sanitized result and deletes the private plan with absence readback. A lost enable response is `ENABLE_OUTCOME_UNKNOWN`, never retried. Unconfirmed closeout reports `CONTAINMENT_UNCONFIRMED` and stops.

No API Keys/key lifecycle, Firebase user action, signing/token exchange, IAM grant/role, database/runtime/secret, Stripe/payment/event/customer action, deployment, billing change or extra allowance. No consumed operation/document/plan may be reused or rewritten.

Observable result: four current diagnostic verdicts plus verified local closeout, or an exact safe stop. Success authorizes only preparation of the separately governed Stage B card. Accepted 1A/1B/2A/2B, 4/8; 0/27 newly closed R1, 6/60 legacy, 0/13 intelligence unchanged. **No scope deviation.**
