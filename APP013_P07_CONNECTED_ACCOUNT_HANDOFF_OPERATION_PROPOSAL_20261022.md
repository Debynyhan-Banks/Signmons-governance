# APP-013 / 3A / P07 connected-account handoff operation proposal

Status: **approved, attempted once and consumed; interrupted before database preflight with closeout unconfirmed**.

## Exact operation

- Plan: `0add40ae-f062-417f-8cab-aa7b7943f562`
- Packet: `c1ba7f8c-8e93-4264-9551-02072df99f7e`
- Operation: `bfc0bb5b-1564-4991-a446-3960caa67d49`
- Package: `/private/tmp/p07-tenant-stripe-binding-handoff-repair-20261022-prep1`
- Manifest SHA-256: `1b9dd0a8b12966e460f8d84c8c72c405ff2b433339d64b34849c1310deb55b76`
- Binding SHA-256: `c7b3e40f8311ad48e653f6ea9b5d8e03d058bbf5715411745a7a24601def21bd`
- Window: October 22, 2026, **7:45–8:30 a.m. Eastern**
- Strict start cutoff: **7:55 a.m. Eastern**
- Mutation deadline: **8:15 a.m. Eastern**
- Closeout deadline: **8:25 a.m. Eastern**
- Automatic retry: **false**
- Cost allowance: **USD 0**

## Allowed actions

1. Read the signed-in Stripe Sandbox only to confirm Sandbox/Test mode, administrator access, exactly one enabled connected account and destination absence; retain only the account SHA-256.
2. After the owner enters the current CHILD administrator password and Terminal prints the preflight marker, read the identifier only from that unique Enabled connected-account row and type it directly from volatile browser process memory into both existing hidden Terminal prompts. Do not use chat, clipboard, files, environment variables, arguments, logs, exceptions, receipts, audit metadata or screenshots for the raw value; clear it immediately afterward.
3. Run the exact read-only tenant/job/payment/calendar/policy preflight.
4. If every prerequisite matches, execute one serializable conditional transaction that updates only the exact tenant's connected-account value, `chargesEnabled` and required `updatedAt`, and inserts the exact sanitized audit row in the same transaction.
5. Run the separate sanitized readback and zero-session closeout. If the commit response is uncertain, recovery may only read the exact post-state and close sessions; it cannot repeat the update.

## Forbidden actions

No other database mutation, role/grant, secret/IAM, Stripe configuration, destination, deployment, Checkout, payment, refund, booking, customer contact, message, merge, push or retry is allowed. Any drift, already-valid account, account/hash mismatch, concurrent change, failed audit, uncertain readback or closeout failure produces one fixed stop.

## Command and attended handoff

At or after 7:45 a.m. and strictly before 7:55 a.m. Eastern, Debynyhan Banks runs once:

```bash
cd "/private/tmp/p07-tenant-stripe-binding-handoff-repair-20261022-prep1" && python3 controller.py --run
```

Debynyhan Banks enters only the current CHILD administrator password in the hidden prompt. Expected entry marker:

```text
P07_TENANT_BINDING_STRIPE_PREFLIGHT_READY
```

After that marker, leave Terminal open. The automation performs the exact browser qualification and types the enabled-row identifier into both hidden prompts without displaying or retaining it.

Success:

```text
P07_TENANT_STRIPE_BINDING_COMPLETE
CONTAINMENT_VERIFIED
```

Controlled stop:

```text
P07_TENANT_BINDING_STOP_<FIXED_CODE>
CONTAINMENT_VERIFIED
```

No retry is allowed.

## Readiness and decision

Fourteen controller regressions, two handoff-boundary checks and five disposable PostgreSQL 16.11 cases pass after binding. Syntax, exact inventory/private modes, manifest and no-action checks pass. Both live modes refuse before hidden input because exact approval is absent. Backend evidence: `evidence/APP-013/p07-connected-account-handoff-repair-window-preparation-20261022.md`.

Approve or refuse this one exact operation before **7:55 a.m. Eastern**. Approval covers only the allowed actions inside this window. It does not authorize Stripe configuration, destination/deployment work, P08 payment or 3A acceptance.

Accepted progress remains **0/27 newly closed R1 packages; 6/60 legacy packages; 4/8 walkthrough milestones; 0/13 full-intelligence rows**. **No scope deviation.**

## Result — October 22, 2026

The owner approved and reserved the exact operation at 7:47:45 a.m. Eastern. Fresh Stripe qualification passed, but computer-use safety controls prohibited the approved direct macOS Terminal handoff. The volatile account value was cleared before input. The owner interrupted once; the controller returned `P07_TENANT_BINDING_STOP_INTERRUPTED` and `CONTAINMENT_UNCONFIRMED`.

Receipts prove `possibleMutation:false`, `commitState:NOT_STARTED`, no mutation intent, no database preflight/transaction and no result/recovery path. Host inspection found no controller or PostgreSQL client process, but the database zero-session query did not complete. The operation is consumed and must not be rerun. Backend evidence: `evidence/APP-013/p07-handoff-interrupted-closeout-unconfirmed-20261022.md`.

`APP013_P07_MANDATORY_CLOSEOUT_RECOVERY_PROPOSAL_20261022.md` is the next decision. Progress remains **0/27 newly closed R1 packages; 6/60 legacy packages; 4/8 walkthrough milestones; 0/13 full-intelligence rows**. **Unintended execution-channel drift disclosed.**
