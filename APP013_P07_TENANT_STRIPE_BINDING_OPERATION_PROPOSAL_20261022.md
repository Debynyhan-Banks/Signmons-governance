# APP-013 / 3A / P07 tenant Stripe binding operation proposal

Status: **approved, attempted once and consumed; controlled stop before database access**.

## Exact operation

- Plan: `8ba2a1c8-d845-4111-b1f7-27e636b0fd1a`
- Packet: `13471d52-2195-4620-b6a4-b6282e4a70c6`
- Operation: `aff460dd-740b-40c4-8fcc-ea6dbc21057e`
- Package: `/private/tmp/p07-tenant-stripe-binding-correction-20261022-prep1`
- Manifest SHA-256: `85ef0344c9ae9bb21d074ef67b5637b172e44c023760b78d2c35c07b845a52e8`
- Binding SHA-256: `bf14a7fe525d3f11372c6068a177425fdf3e0da9558c7fb5d05e01d0fc350abc`
- Window: October 22, 2026, **7:15–8:00 a.m. Eastern**
- Strict start cutoff: **7:25 a.m. Eastern**
- Mutation deadline: **7:45 a.m. Eastern**
- Closeout deadline: **7:55 a.m. Eastern**
- Automatic retry: **false**
- Cost allowance: **USD 0**

## Allowed actions

1. Read the signed-in Stripe Sandbox only to confirm Sandbox/Test mode, administrator access, exactly one enabled connected account and destination absence; retain only its SHA-256.
2. Ask Debynyhan Banks for the current CHILD administrator password and the current Sandbox connected-account ID twice through hidden Terminal input.
3. Run the exact read-only tenant/job/payment/calendar/policy preflight.
4. If every prerequisite matches, execute one serializable conditional transaction that updates only the exact tenant's connected-account value, `chargesEnabled` and required `updatedAt`, and inserts the exact sanitized audit row in the same transaction.
5. Run the separate sanitized readback and zero-session closeout. If the commit response is uncertain, recovery may only read the exact post-state and close sessions; it cannot repeat the update.

The raw account identifier remains only in process memory and SQL stdin. It may not enter chat, command arguments, files, logs, exceptions, receipts or audit metadata.

## Forbidden actions

No other database mutation, role/grant, secret/IAM, Stripe configuration, destination, deployment, Checkout, payment, refund, booking, customer contact, message, merge, push or retry is allowed. Any drift, already-valid account, account/hash mismatch, concurrent change, failed audit, uncertain readback or closeout failure produces one fixed stop.

## Command and expected result

At or after 7:15 a.m. and strictly before 7:25 a.m. Eastern, run once:

```bash
cd "/private/tmp/p07-tenant-stripe-binding-correction-20261022-prep1" && python3 controller.py --run
```

Expected entry marker:

```text
P07_TENANT_BINDING_STRIPE_PREFLIGHT_READY
```

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

No retry is allowed. Leave Terminal open until the terminal result and containment line appear.

## Local readiness and decision

Fourteen focused controller tests and five real disposable PostgreSQL 16.11 cases pass after binding. Syntax, manifest, file inventory/private modes and no-action checks pass. Both live modes refuse before hidden input because exact approval is absent. Backend evidence: `evidence/APP-013/p07-tenant-stripe-binding-window-preparation-20261022.md`.

Approve or refuse this one exact operation before **7:25 a.m. Eastern**. Approval covers only the allowed actions inside this window. It does not authorize Stripe configuration, destination/deployment work, P08 payment or 3A acceptance.

Accepted progress remains **0/27 newly closed R1 packages; 6/60 legacy packages; 4/8 walkthrough milestones; 0/13 full-intelligence rows**. **No scope deviation.**

## Result — October 22, 2026

Debynyhan Banks approved the exact operation. It reserved at 7:15:18 a.m. Eastern and passed fresh Stripe Sandbox/Test mode, administrator access, exactly one enabled connected account and destination absence. The two hidden Terminal entries matched and had valid `acct_...` format, but their hash did not match the verified enabled connected account. The controller stopped `P07_TENANT_BINDING_STOP_CONNECTED_ACCOUNT_HASH_MISMATCH` and returned `CONTAINMENT_VERIFIED`.

Receipts prove `possibleMutation:false`, `commitState:NOT_STARTED`, no mutation intent, no database transaction, no result/recovery path and zero operation sessions. The operation is consumed and must not be rerun. Backend evidence: `evidence/APP-013/p07-tenant-stripe-binding-hash-mismatch-stop-20261022.md`.

P07/3A remains active. A fresh separately identified package and explicit authority are required for another attempt. Progress remains **0/27 newly closed R1 packages; 6/60 legacy packages; 4/8 walkthrough milestones; 0/13 full-intelligence rows**. **No scope deviation.**
