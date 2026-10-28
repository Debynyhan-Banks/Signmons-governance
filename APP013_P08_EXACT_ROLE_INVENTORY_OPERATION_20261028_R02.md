# APP-013 / 3A / P08 — IAM FULL-view exact role inventory operation R02

Status: PROPOSED, NOT AUTHORIZED. R1-W01 / APP-013 / 3A remains unchanged.

Corrected source is backend `56b90a7`, `role_qualifier.py` SHA256 `86253263a046e080a7d49cb1e2da6a1b2e39610008bdf428084c780031187856`. Consumed operations are not reused. Fresh operation ID: `9725da4a-51e7-439d-aa79-fe48c62229dc`.

## Exact scope and window

October 28, 2026, 6:30–7:00 p.m. Eastern; start strictly before 6:45. The one-use plan sets a command/request deadline four minutes after reservation and never later than 6:50. Reads/result by 6:50; process/child closeout by 6:55; private plan/approval absence by 7:00. One attempt, no retry. USD 0 incremental allowance. No attendance or password.

Exact read sequence:

1. active owner account value, requiring `debynyhan@signmons.com`;
2. configured project value, requiring `signmons`;
3. owner OAuth access token, process memory only;
4. one GET to `https://iam.googleapis.com/v1/projects/signmons/roles?view=FULL&pageSize=200`.

The source permits exactly three CLI commands and one HTTPS request. It rejects redirects, alternate request components, non-200/oversize/invalid output and any next-page token. Raw response and bearer are never retained. Saved evidence contains only aggregate/classification, at most two exact candidate IDs/permissions/stages/definition hashes, safe CLI/HTTPS progress/reason and private-input absence.

Success returns `P08_ROLE_CANDIDATES_UNIQUE` or `P08_ROLE_CANDIDATES_DECISION_REQUIRED`. No result authorizes selection, role creation, binding or Stage B action.

## Exclusions and closeout

No API/service enablement, IAM role or binding creation/change, Firebase action, signing/token exchange, API-key access/create/delete, database/identity/secret/tag/runtime action, deployment, Stripe/payment, customer action or spending. Policy Troubleshooter remains unchanged. The exchange-key incompatibility remains open.

SIGINT/SIGTERM cancels children. Private plan/approval inputs purge on return. Sanitized attempt/result remain. Never retry after any result or stop.

## Decision requested

Approve this exact FULL-view read-only operation for today 6:30–7:00 p.m. Eastern, starting strictly before 6:45, or defer. Approval covers only the three CLI reads, one exact HTTPS read and mandatory closeout.

Accepted counts unchanged. **No scope deviation.**
