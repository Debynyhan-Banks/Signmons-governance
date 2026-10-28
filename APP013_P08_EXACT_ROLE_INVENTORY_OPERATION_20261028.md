# APP-013 / 3A / P08 — exact read-only custom-role inventory operation

Status: PROPOSED, NOT AUTHORIZED. R1-W01 / APP-013 / 3A remains unchanged.

## Purpose and binding

Stage A proved two exact access gaps. The owner-approved local qualifier is complete at backend `c51dd78`, source `evidence/APP-013/p08-role-candidate-qualifier-local-20261028/source/role_qualifier.py`, SHA256 `4b74ba1b778a3f3cbed2a466049fa5cb2100fd2db71c2d48634476ae2e3bcef3`. Fourteen tests pass; its bound path uses exactly three read-only commands and purges private plan/approval inputs. Governance proposal/decision commits are `6548f05` / `0f9197b`.

Operation ID: `83bdf433-98dd-45c9-8b42-fb90494219ce`.

The operation answers only whether the Signmons project already contains zero, one or multiple active custom roles whose permission list is exactly one of:

- `firebaseauth.users.get`;
- `iam.serviceAccounts.signBlob`.

It does not choose a role when multiple exact candidates exist and does not create, change, bind or delete a role.

## Exact window and command ceiling

Date: October 28, 2026. Start at or after 6:00 p.m. and strictly before 6:15 p.m. Eastern. The local plan sets its command deadline to four minutes after reservation and never later than 6:20 p.m. Reads and sanitized result must finish by 6:20; process/child closeout by 6:25; private plan and approval inputs must be absent immediately on return and no later than 6:30.

One attempt, no retry. USD 0 incremental allowance. No attendance or password is required. Existing owner gcloud authorization/cache refresh is allowed. The exact three commands are:

1. active owner account value;
2. current configured project value;
3. Signmons project custom-role list with only `name,includedPermissions,deleted,stage` fields.

Owner must equal `debynyhan@signmons.com`; project must equal `signmons`; otherwise stop before the role-list command. No bearer export or raw policy read. The controller refuses any fourth command and has no mutation command builder.

## Output, retention and closeout

Raw role-list output remains in process memory only. Saved evidence contains aggregate role count, per-permission classification, and at most two unique exact candidate role IDs with permission, active stage, deleted=false and canonical definition SHA256. Titles, descriptions, unrelated role names/permissions and provider error bodies are not saved. Zero, broader-only or multiple-exact results return `P08_ROLE_CANDIDATES_DECISION_REQUIRED`; two unique exact results return `P08_ROLE_CANDIDATES_UNIQUE`. Both are facts, not grant approval.

The operation stops safely on malformed/foreign/inactive/duplicate/over-cap output, owner/project drift, deadline, signal, command failure or unknown outcome. SIGINT/SIGTERM cancels the child. Private mode-0600 plan/approval files are removed on success or refusal; the sanitized attempt/result remain for audit. Do not rerun after any result or stop.

## Exclusions

No API/service enablement, IAM role or binding creation/change, Firebase user action, signing/token exchange, API key access/create/delete, database action, identity/secret/tag/runtime restoration, deployment, Stripe/payment, customer action, spending or acceptance advancement. Policy Troubleshooter remains as already enabled. The separate browser-restricted exchange-key incompatibility remains open regardless of this result.

## Decision requested

Approve this exact read-only operation for October 28, 6:00–6:30 p.m. Eastern, starting strictly before 6:15, or defer. Approval authorizes only the three reads and mandatory closeout above. It does not authorize later role creation, IAM binding or Stage B action.

Accepted 1A/1B/2A/2B remain 4/8; 0/27 newly closed R1, 6/60 legacy and 0/13 intelligence remain unchanged. **No scope deviation.**

## Owner decision

Debynyhan Banks replied “I approve the exact 6:00–6:30 read-only operation.” against committed proposal `2742153`, pre-decision document SHA256 `3c83bc2d677e251e680be074b1d68d7160c8c54622cc8d7b88c0f54003f3c4b3`. Exact operation `83bdf433-98dd-45c9-8b42-fb90494219ce` is authorized only within the stated October 28 window and command/closeout limits. No later role/grant or Stage B action is authorized.
