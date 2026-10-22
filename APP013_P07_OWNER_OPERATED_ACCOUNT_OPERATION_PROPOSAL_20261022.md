# R1-W01 / APP-013 / 3A / P07 owner-operated tenant-binding operation

Status: **owner decision pending; no external action authorized**.

## Exact package and window

- Package: `/private/tmp/p07-tenant-stripe-binding-owner-handoff-20261022-prep1`.
- Plan: `e13cca1d-b51d-44f0-bcc9-dcbe0b281f8e`.
- Packet: `852a8b36-2780-4003-85ec-14ad7491eb79`.
- Operation: `f0af9aa6-f83b-4557-a0cb-cfd9900fbb42`.
- Audit ID: `46971952-f8e7-455a-a48a-fb084b5e836a`.
- Manifest SHA-256: `4ccd327f942a593c3cbd7ea32c51a6c6908a9dc746a55c44828223977820d14b`.
- Binding SHA-256: `aeee47af34113ff8caff8800f37a12be7b2b4f5afb10bd1a70e593ce402bdf6f`.
- Controller SHA-256: `9bba476439b77ee24bd695b209d03ba21a8d894e96f0f4359f1c33b1b032f823`.
- Window: **October 22, 2026, 3:00–3:45 p.m. Eastern** (`19:00–19:45 UTC`).
- Strict start cutoff: **3:10 p.m. Eastern** (`19:10 UTC`).
- Transaction deadline: **3:30 p.m. Eastern** (`19:30 UTC`).
- Closeout deadline: **3:40 p.m. Eastern** (`19:40 UTC`).
- Automatic retry: **false**. Allowance: **USD 0**.

## Allowed actions

1. Owner starts the one-use controller in-window and enters the current CHILD administrator password privately through hidden input.
2. Read the signed-in Stripe Sandbox to confirm Sandbox/Test mode, administrator access, exactly one Enabled connected account and destination absence. Open only that row's account detail to identify its exact account-ID control. Retain only sanitized mode/status/booleans and SHA-256; do not log/save raw account identifiers or screenshots containing them.
3. Only after that control is visibly confirmed, the owner copies its connected-account ID and pastes it into both existing hidden Terminal prompts, then clears the clipboard entry by copying harmless text outside Terminal. This is the exact owner-only clipboard exception approved in the handoff proposal. Automation may not read/write the clipboard or operate Terminal. Personal-details membership IDs and the platform URL ID are invalid sources. Stop if the exact control cannot be confirmed.
4. The unchanged format/double-entry/browser-hash guards run before read-only database preflight. On a match and exact tenant/job/payment/calendar/policy prerequisites, run one serializable conditional transaction updating only the exact tenant's `stripeConnectAccountId`, `chargesEnabled=true` and required `updatedAt`, with the exact sanitized AuditLog row inserted in the same transaction.
5. Perform separate sanitized readback and zero-session closeout. An uncertain commit is consumed; any authorized recovery reads the exact post-state and closes sessions only, never repeats the write.

The tenant remains `a1adcfd4-15be-404b-9ac3-5edb1fda20f0`; accepted job remains `9180bef4-561d-47a0-869f-925e6a3dfd96`. No account replacement is allowed if the existing binding is already valid. The reviewed same-job/policy/no-payment/no-calendar/concurrent-change guards and audit rollback are preserved.

Passwords and raw account IDs must not enter chat, files, arguments, saved screenshots, logs, exceptions, receipts or audit metadata. The owner clipboard exception applies only to this one ID during this operation; passwords remain directly owner-entered and hidden. Automation uses hash-only account evidence.

## Exclusions and failure behavior

No other database mutation, role/grant, secret/IAM, Stripe configuration/destination, deployment, Checkout, charge/payment/refund, booking, customer contact, message, session termination, merge, push or retry. Any drift, mismatched input, unavailable control, already-valid binding, concurrent change, audit/readback failure or missed deadline stops. Mandatory closeout remains required. Existing fixed database-error classification remains unchanged; unclassified database failures must not be presented as a known root cause.

## One-use command after approval

At or after **3:00 p.m.** and strictly before **3:10 p.m. Eastern**, owner runs once:

```bash
cd "/private/tmp/p07-tenant-stripe-binding-owner-handoff-20261022-prep1" && python3 -B controller.py --run
```

Enter only the current CHILD administrator password initially. At `P07_TENANT_BINDING_STRIPE_PREFLIGHT_READY`, report only that status and leave Terminal open. Wait for the attended account-detail/control qualification before copying/pasting any account ID.

Success: `P07_TENANT_STRIPE_BINDING_COMPLETE` plus `CONTAINMENT_VERIFIED`. Failure: `P07_TENANT_BINDING_STOP_<FIXED_CODE>` plus truthful verified/unconfirmed containment. Share only final status lines. No retry or re-entry after a terminal stop.

## Readiness and decision

After binding: fourteen controller and five disposable PostgreSQL tests pass; syntax, exact seven-file inventory/private modes, hashes and no-action pass. Both live modes refuse without exact owner approval. Backend evidence: `evidence/APP-013/p07-owner-operated-account-window-preparation-20261022.md`. No live browser, clipboard, database or provider action occurred in preparation.

Approve or refuse this **one exact attended browser/owner-clipboard/database operation** before the strict 3:10 cutoff. Availability/local-preparation approval is not external execution approval; the approved handoff proposal and repository AGENTS.md require this separate decision.

Successful binding removes one P07 prerequisite only. Runtime readiness, authentic Sandbox payment and 3A owner acceptance remain open. Measures stay **0/27 R1; 6/60 legacy; 4/8 walkthrough; 0/13 intelligence**. **Owner-approved procedural deviation only; no additional scope deviation.**
