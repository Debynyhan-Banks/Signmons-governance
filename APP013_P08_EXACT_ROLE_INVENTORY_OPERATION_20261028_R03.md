# APP-013 / 3A / P08 — IAM FULL-view exact role inventory operation R03

Status: OWNER APPROVED, NOT STARTED. R1-W01 / APP-013 / 3A remains unchanged.

Owner decision: Debynyhan Banks approved this exact operation in the governed conversation on October 28, 2026, before the 6:55 p.m. Eastern start cutoff. The decision binds operation `02aa2053-4985-487d-b7b8-aaf67d6bfb21` to this document's pre-decision SHA256 `a55e975f7582faa32c32070af584cf14ce08758aca703038c7c7ce0311ce9f85`, backend source `fed5efb` and the window below. Approval is consumed by one attempt and does not authorize a retry, role/grant change or Stage B action.

Corrected source is backend `fed5efb`, `role_qualifier.py` SHA256 `b164717be48a45e2c6be86d4c3968d636f028dded95af8d0597d580f9af8083b`. Consumed operations are not reused. Fresh operation ID: `02aa2053-4985-487d-b7b8-aaf67d6bfb21`.

## Exact scope and window

October 28, 2026, 6:40–7:10 p.m. Eastern; start strictly before 6:55. The one-use plan sets a command/request deadline four minutes after reservation and never later than 7:00. Reads/result by 7:00; process/child closeout by 7:05; private plan/approval absence by 7:10. One attempt, no retry. USD 0 incremental allowance. No attendance or password.

Exact read sequence:

1. active owner account value, requiring `debynyhan@signmons.com`;
2. configured project value, requiring `signmons`;
3. owner OAuth access token, process memory only;
4. one GET to `https://iam.googleapis.com/v1/projects/signmons/roles?view=FULL&pageSize=200`.

The source permits exactly three CLI commands and one HTTPS request. It rejects redirects, alternate request components, non-200/oversize/invalid output, unknown Role fields and any next-page token. Documented string `etag` is discarded. Raw response and bearer are never retained. Saved evidence contains only aggregate/classification, at most two exact candidate IDs/permissions/stages/definition hashes, safe CLI/HTTPS progress/reason and private-input absence.

Success returns `P08_ROLE_CANDIDATES_UNIQUE` or `P08_ROLE_CANDIDATES_DECISION_REQUIRED`. No result authorizes selection, role creation, binding or Stage B action.

## Exclusions and closeout

No API/service enablement, IAM role or binding creation/change, Firebase action, signing/token exchange, API-key access/create/delete, database/identity/secret/tag/runtime action, deployment, Stripe/payment, customer action or spending. Policy Troubleshooter remains unchanged. The exchange-key incompatibility remains open.

SIGINT/SIGTERM cancels children. Private plan/approval inputs purge on return. Sanitized attempt/result remain. Never retry after any result or stop.

## Decision requested

Approve this exact corrected FULL-view read-only operation for today 6:40–7:10 p.m. Eastern, starting strictly before 6:55, or defer. Approval covers only the three CLI reads, one exact HTTPS read and mandatory closeout.

Accepted counts unchanged. **No scope deviation.**
