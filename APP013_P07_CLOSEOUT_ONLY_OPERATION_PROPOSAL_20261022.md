# R1-W01 / APP-013 / 3A / P07 exact closeout-only operation

Status: **owner-approved, executed once and consumed; mandatory closeout verified**.

## Exact package and window

- Package: `/private/tmp/p07-closeout-only-20261022-prep1`.
- Plan: `76a8f82d-1d34-44e9-8a5f-0234c48b8052`.
- Packet: `6504f835-2c15-4268-bc5b-16c9ee8f6bb6`.
- Closeout operation: `0d2f9eca-c8e8-49b6-b3c5-182416164a90`.
- Consumed operation being checked: `bfc0bb5b-1564-4991-a446-3960caa67d49`.
- Manifest SHA-256: `bf50b94c8039827e530944c4fa7bad664c3d8279f6627a05687b833afcb7c117`.
- Binding SHA-256: `986c3d118ec37ee86c86ec56262e7c90703af6f0ce33bdc33ccefc91228a7146`.
- Helper SHA-256: `2c57be00422d776365adadbc30a3d955df921d80467ad16cee9afaf611cbfee9`.
- Window: October 22, 2026, **2:35–2:50 p.m. Eastern** (`18:35–18:50 UTC`).
- Strict start cutoff: **2:40 p.m. Eastern** (`18:40 UTC`).
- Hidden-input/query deadline: **2:48 p.m. Eastern** (`18:48 UTC`).
- Allowance: **USD 0**. Automatic retry: **false**.

## Allowed action and data boundary

The owner runs the one-use helper and enters only the current CHILD administrator password through hidden Terminal input. The helper uses the existing CHILD administrator connection with verify-full/system roots to execute this one exact read-only query:

```sql
BEGIN TRANSACTION ISOLATION LEVEL REPEATABLE READ READ ONLY;
SELECT count(*) FROM pg_stat_activity WHERE application_name LIKE 'signmons_p07_tenant_binding_bfc0bb5b%' AND pid<>pg_backend_pid();
ROLLBACK;
```

It requires process exit zero plus exact output `0`. It closes its client and writes a private sanitized receipt. The password never enters chat, arguments or logs; no Stripe identifier or browser/Terminal automation is involved. Connection/query/process/input deadlines remain enforced. Any failed check records a fixed reason and stage; raw database errors and SQL output are discarded. Unknown errors stay unknown.

No session termination, tenant/account access, write transaction, main-operation retry, grant, secret/IAM change, provider configuration, Stripe action, deployment, Checkout, payment, booking, customer contact, message, merge or push is authorized.

## Command and observable finish

After exact approval, at or after **2:35** and strictly before **2:40 p.m. Eastern**, run once:

```bash
cd "/private/tmp/p07-closeout-only-20261022-prep1" && python3 -B helper.py --run
```

Enter only the current CHILD administrator password in the hidden prompt; keep Terminal open. Success prints:

```text
P07_MANDATORY_CLOSEOUT_VERIFIED
CONTAINMENT_VERIFIED
```

Failure prints a fixed `P07_CLOSEOUT_ONLY_STOP_<REASON>`, `P07_CLOSEOUT_FAILURE_STAGE_<STAGE>` and `CONTAINMENT_UNCONFIRMED`. Share only those status lines. Do not retry. A failure remains unconfirmed and consumed; it does not authorize another query or killing a session.

## Readiness and decision

The bound package retains the unchanged tested helper/manifest. Twenty-one helper tests, two disposable PostgreSQL cases, syntax, exact seven-file private inventory and hashes, no-action check and no-approval refusal are recorded in backend `evidence/APP-013/p07-closeout-only-window-preparation-20261022.md`. Run refuses `P07_CLOSEOUT_ONLY_REFUSED_OWNER_APPROVAL_INVALID` before hidden input or database access.

Approve or refuse this **one exact read-only closeout operation** before the strict 2:40 p.m. cutoff. The local-preparation approval and supplied availability are not external execution approval. This separate approval is required by the owner-approved recovery proposal and repository `AGENTS.md` instruction that planning/implementation approval does not imply external action approval.

Actual containment remains unconfirmed until the approved read succeeds. Account binding/handoff, runtime readiness and Sandbox payment remain open. Accepted progress remains **0/27 R1; 6/60 legacy; 4/8 walkthrough; 0/13 intelligence**. **No scope deviation.**

## Result — October 22, 2026

Debynyhan Banks approved this exact operation. It reserved once at **2:35:46 p.m. Eastern** and completed at **2:36:05 p.m. Eastern** inside all deadlines. Terminal returned `P07_MANDATORY_CLOSEOUT_VERIFIED` / `CONTAINMENT_VERIFIED`. The correlated private result records `status:VERIFIED`, `reason:VERIFIED`, `stage:SESSION_READBACK`, `operationSessionsAbsent:true`, `possibleMutation:false` and no retry. Receipt SHA-256: `78c9bc50b7eb4453763c06ffad40471c57f072e81bdd77ad5eb49bfea1d11f9a`.

Mandatory session closeout for consumed target `bfc0bb5b-1564-4991-a446-3960caa67d49` is now verified by this later readback. The original interrupted stop stays immutable with its historical unconfirmed value. No tenant, account, payment or provider state changed. Both operations are consumed and must not be retried. Backend evidence: `evidence/APP-013/p07-closeout-only-live-result-20261022.md`.

Account handoff/binding and the remaining P07/payment gates remain open. Accepted measures remain **0/27 R1; 6/60 legacy; 4/8 walkthrough; 0/13 intelligence**. **No scope deviation.**
