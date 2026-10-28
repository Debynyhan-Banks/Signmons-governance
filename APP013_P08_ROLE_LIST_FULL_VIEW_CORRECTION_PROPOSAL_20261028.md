# APP-013 / 3A / P08 — IAM role-list full-view correction proposal

Status: PROPOSAL ONLY. No implementation or external retry is authorized. R1-W01 / APP-013 / 3A remains unchanged.

## Demonstrated gap

Consumed R01 completed owner, project and role-list commands, then stopped at `PERMISSION_SHAPE`. IAM `roles.list` defaults to `BASIC`, which omits `includedPermissions`; `FULL` is required. The current gcloud list projection cannot change the API view. Therefore the exact role definitions remain unknown.

## Alternatives

1. **Recommended — exact in-memory OAuth HTTPS full-view read.** Keep the owner and project checks, acquire one owner OAuth access token in process memory, then make one HTTPS GET to `iam.googleapis.com/v1/projects/signmons/roles?view=FULL&pageSize=200`. Parse only `roles` and optional `nextPageToken`; any token stops at the page cap without pagination. Reuse the existing role classifier, privacy, one-attempt, stage evidence and closeout.
2. List names and describe every role. Reject: variable command count and output volume, with no verified small upper bound.
3. Treat omitted permissions as empty. Reject: would create a false “no exact role” result.
4. Defer. Keep role facts unknown and 3A blocked.

## Bounded local card

Source is backend `5dd0618`; immutable R01 stop evidence is `d82a4d4`. Expected changes remain limited to the evidence-contained qualifier/tests/manifest/README/new sanitized result and logs.

Finite checklist:

- replace only the third gcloud role-list command with owner `auth print-access-token` as the third CLI command and one exact HTTPS GET;
- allow only host `iam.googleapis.com`, path `/v1/projects/signmons/roles`, method GET and exact query `view=FULL&pageSize=200`; reject redirects and alternate hosts/paths/query/methods;
- keep bearer only in process memory and authorization header; never arguments, files, stdout/stderr, result, exception text or test logs;
- record safe stages `OWNER_CHECK`, `PROJECT_CHECK`, `BEARER_ACQUISITION`, `ROLE_LIST_FULL`, distinguishing CLI and HTTPS started/completed counts;
- accept response object only with `roles` and optional `nextPageToken`; refuse a nonempty token as `ROLE_PAGE_CAP` and never paginate;
- retain maximum 200 roles, canonical project role IDs, active/exact one-permission classifier, aggregate/sanitized candidate retention and raw-output suppression;
- preserve exact source/decision/owner approval, one attempt/no retry, deadline, signal child cancellation, atomic stop evidence, private-input purge and native-unbound refusal;
- fake-provider tests cover exact serialized request/header handling, success/zero/broader/multiple, bearer/HTTP failure and unknown outcome, redirect/host/path/query/method/page-token/output-shape refusal, token non-retention, every stage, write/purge/concurrency and unchanged restoration-role compatibility;
- run source manifest, architecture, governance baseline/consistency/25 safeguards and both whitespace checks. No browser/database tests apply.

Rollback removes only the local correction/evidence. R01 evidence remains immutable. No external command/request is included. A passing local result must be followed by a fresh exact operation ID/window and separate owner approval.

## Decision requested

Approve Alternative 1 for bounded local full-view request correction and isolated tests only, or defer. No Google Cloud command/request, IAM role/grant, Firebase action, signing/token exchange, API-key action, database/runtime action, Stripe/payment, deployment or spending is authorized.

References: [IAM roles.list view contract](https://docs.cloud.google.com/iam/docs/reference/rest/v1/roles/list), [RoleView BASIC/FULL](https://docs.cloud.google.com/iam/docs/reference/rest/v1/RoleView), [gcloud list reference](https://docs.cloud.google.com/sdk/gcloud/reference/iam/roles/list).

Accepted counts unchanged. **Explicit output-contract correction proposed; no implementation.**
