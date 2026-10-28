# APP-013 / 3A / P08 — corrected exact read-only custom-role inventory operation R01

Status: PROPOSED, NOT AUTHORIZED. R1-W01 / APP-013 / 3A remains unchanged.

Corrected source is backend `5dd0618`, `role_qualifier.py` SHA256 `7b0f85d3b760838f4752dd55c5d31eb7ec42ba195d3b585a40ee69c4d9b428d4`. Local observability result is complete; the consumed operation `83bdf433-98dd-45c9-8b42-fb90494219ce` is not reused. Fresh operation ID: `7212ade4-3500-421f-832b-d9738eb0b324`.

## Exact scope and window

October 28, 2026, 6:15–6:45 p.m. Eastern; start strictly before 6:30. The private one-use plan sets a command deadline four minutes after reservation and never later than 6:35. Reads/result by 6:35; process/child closeout by 6:40; private plan/approval absence by 6:45. One attempt, no retry. USD 0 incremental allowance. No attendance or password.

Exactly three existing-owner gcloud reads:

1. active owner account value, requiring `debynyhan@signmons.com`;
2. configured project value, requiring `signmons`;
3. Signmons project custom-role metadata limited to `name,includedPermissions,deleted,stage`.

The source cannot represent a fourth or mutation command. Raw role output remains in memory. Saved evidence contains only aggregate count, exact zero/broader/unique/multiple classification, at most two exact candidate role IDs/permissions/stages/definition hashes, sanitized command progress/reason and private-input absence. Provider text, titles, descriptions and unrelated role details are not saved.

Success returns `P08_ROLE_CANDIDATES_UNIQUE` or `P08_ROLE_CANDIDATES_DECISION_REQUIRED`. Any owner/project/command/JSON/classification/deadline/signal/output issue returns a sanitized fixed stop with started/completed stage evidence. No result authorizes a role choice, role creation, binding or Stage B action.

## Exclusions and closeout

No API/service enablement, IAM role or binding creation/change, Firebase action, signing/token, API-key access/create/delete, database/identity/secret/tag/runtime action, deployment, Stripe/payment, customer action or spending. Policy Troubleshooter remains unchanged. The separate browser-restricted exchange-key incompatibility remains open.

SIGINT/SIGTERM cancels the child. Private plan/approval inputs purge on return. Sanitized attempt/result remain. Never retry this operation after any result or stop.

## Decision requested

Approve this corrected exact read-only operation for today 6:15–6:45 p.m. Eastern, starting strictly before 6:30, or defer. Approval covers only these three reads and mandatory closeout.

Accepted counts remain unchanged. **No scope deviation.**
