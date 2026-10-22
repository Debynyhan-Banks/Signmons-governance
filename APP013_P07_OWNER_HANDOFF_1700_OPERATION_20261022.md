# R1-W01 / APP-013 / 3A / P07 approved 5 p.m. replacement operation

Status: **same exact browser/owner-clipboard/database action explicitly approved by owner for the replacement window; locally validated; approval record installation precedes owner command**.

## Authority and exact identities

Debynyhan Banks explicitly approved the same operation for **October 22, 2026, 5:00–5:40 p.m. Eastern**. Decision/pre-code card: `APP013_P07_OWNER_HANDOFF_1700_REPLACEMENT_DECISION_20261022.md` at commit `5078f6f8c1d4c16e07786a71863907dc6adcccfa`. The 3 p.m. package expired unstarted and is preserved unchanged. This fresh replacement is not a retry of any attempted operation.

- Package: `/private/tmp/p07-tenant-stripe-binding-owner-handoff-20261022-1700`.
- Plan: `ccab5857-fa54-4343-adef-a0c28502da3d`.
- Packet: `69e50ac6-3db3-473b-9940-2825d9595540`.
- Operation: `d618b826-72d9-412f-8d9f-08482a457088`.
- Audit: `e833940c-4a93-439b-b0a2-001ed6c0acbe`.
- Manifest SHA-256: `dcba1e35ad4f243fe0d607cdd2aa36b59c608af3650dda9d343a99be008eba2f`.
- Binding SHA-256: `578c600f0a44e72cb411b9a00896fe3d0187d8718524d48bce4bf4a36c7042b6`.
- Controller SHA-256: `13d603d80ae39b4e83d9d2cf0aaa777ea399393effc508f02385c9b2946a2e4a`.
- Window: **5:00–5:40 p.m. Eastern** (`21:00–21:40 UTC`).
- Strict start cutoff: **5:10 p.m.** (`21:10 UTC`).
- Transaction deadline: **5:25 p.m.** (`21:25 UTC`).
- Closeout deadline: **5:35 p.m.** (`21:35 UTC`).
- USD 0; automatic retry false.

## Same allowed actions and exact boundaries

1. Owner starts the controller in-window and enters the current CHILD administrator password through hidden input.
2. Read signed-in Stripe Sandbox to confirm Sandbox/Test, administrator access, exactly one Enabled connected account and destination absence. Open that row's account detail and visibly confirm its exact account-ID control. Save only booleans/status and SHA-256; no raw identifiers/screenshots containing them.
3. Only after qualification, the owner copies the ID from that exact account-detail control into both hidden Terminal prompts, then clears the clipboard entry outside Terminal. The owner-only clipboard exception is retained. Automation may not operate Terminal or read/write clipboard. Personal-details membership/platform URL IDs are invalid sources. Stop if the control is unavailable.
4. Unchanged format/double-entry/browser-hash gates precede read-only exact tenant/job/payment/calendar/policy preflight. Run one guarded serializable exact-tenant update of `stripeConnectAccountId`, `chargesEnabled=true` and `updatedAt`, with the exact sanitized audit in the same transaction.
5. Perform sanitized exact readback and zero-session closeout. Uncertain commit recovery is read-only and cannot repeat the write.

Tenant/job, SQL/predicates/audit/readback/recovery and all privacy safeguards remain those reviewed in `APP013_P07_OWNER_OPERATED_ACCOUNT_OPERATION_PROPOSAL_20261022.md`. The only behavioral change is the explicitly requested 40-minute window validator with earlier transaction/closeout/end deadlines; no allowance or scope expansion. No account replacement if the stored value is already valid.

No other mutation, session termination, grant, secret/IAM, Stripe configuration/destination, deployment, Checkout, charge/payment/refund, booking, customer contact, message, merge, push or retry. Passwords/raw IDs remain excluded from chat/files/arguments/logs/saved screenshots/receipts/audit metadata. Fixed failures and truthful containment remain mandatory.

## Command and finish

After the approval record validates, at/after **5:00** and strictly before **5:10 p.m. Eastern**, owner runs once:

```bash
cd "/private/tmp/p07-tenant-stripe-binding-owner-handoff-20261022-1700" && python3 -B controller.py --run
```

Enter current CHILD administrator password only. At `P07_TENANT_BINDING_STRIPE_PREFLIGHT_READY`, report that status and leave Terminal open. Wait for account-control qualification before any account-ID copy/paste. Success: `P07_TENANT_STRIPE_BINDING_COMPLETE` and `CONTAINMENT_VERIFIED`; failure: fixed `P07_TENANT_BINDING_STOP_<CODE>` with truthful containment. Do not retry.

Seventeen controller/timing and five disposable PostgreSQL tests pass; old 45-minute/extended timings refuse. Syntax, exact private inventory, hashes/no-action and pre-approval refusal pass. Evidence: backend `evidence/APP-013/p07-owner-handoff-1700-preparation-20261022.md`. No live action occurred in preparation. Readiness/closeout is not payment acceptance. Progress stays **0/27 R1; 6/60 legacy; 4/8 walkthrough; 0/13 intelligence**. **Owner-approved replacement timing/procedure; no additional scope deviation.**
