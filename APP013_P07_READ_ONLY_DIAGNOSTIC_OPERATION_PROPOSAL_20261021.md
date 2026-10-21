# APP-013 / 3A / P07 exact read-only diagnostic operation proposal

Status: **owner decision pending; no browser or database action authorized**.

## Exact operation

- Plan: `55d7dc3a-4fe3-4f09-8ada-bcbd7ef3ad02`
- Packet: `3acd1d03-07bf-4007-a399-03ff2d30a9b4`
- Operation: `c15a9092-f421-4c5b-94bd-4e7b158c6595`
- Package: `/private/tmp/p07-read-only-diagnostic-20261021-prep1`
- Manifest SHA-256: `1df3777e3c73eb14124c9f170241c3267d5521cac00c156853dc5b467270b9a5`
- Binding SHA-256: `9b6e197f6424041d63c878fc1f6869edc648a122244fdd8c982c83fccb5a5b8a`
- Window: October 21, 2026, **1:45–2:15 p.m. Eastern**
- Strict start cutoff: **1:55 p.m. Eastern**
- Diagnostic deadline: **2:05 p.m. Eastern**
- Closeout deadline: **2:10 p.m. Eastern**
- Support/containment end: **2:15 p.m. Eastern**
- Automatic retry: **false**
- Cost allowance: **USD 0**

## Allowed actions

1. Read the currently signed-in Stripe Sandbox interface only to confirm Sandbox mode, administrator access, exactly one enabled connected account and destination absence, and compare the connected-account SHA-256 in memory. Persist only the sanitized fixed receipt; discard the raw identifier.
2. Ask Debynyhan Banks for the current CHILD administrator password through hidden Terminal input.
3. Execute the reviewed exact-job/role/tenant `SELECT` statements inside one PostgreSQL `REPEATABLE READ READ ONLY` transaction, followed by `ROLLBACK`.
4. Emit one fixed predicate classification or a fixed transport/TLS/authentication/closeout stop.
5. Run the separate read-only closeout query and retain only whether operation-scoped sessions are absent.

## Forbidden actions

No database mutation, role or grant change, secret or IAM change, Stripe configuration, webhook destination, deployment, Checkout creation, payment, refund, booking, customer contact, message delivery, retry, merge or push is allowed. No raw password, account identifier, SQL output, database error, job/customer field, database URL or private browser link may be placed in chat or evidence.

The controller contains no callable mutation/provider-resource path. Recovery can verify/close an uncertain connection only and cannot rerun the diagnostic.

## Expected outcomes

Success produces:

```text
P07_READ_ONLY_DIAGNOSTIC_COMPLETE
<ONE_FIXED_CLASSIFICATION>
CONTAINMENT_VERIFIED
```

A controlled stop produces:

```text
P07_DIAGNOSTIC_STOP_<FIXED_CODE>
CONTAINMENT_VERIFIED
```

If closeout cannot be verified, the final line is `CONTAINMENT_UNCONFIRMED`; no further diagnostic attempt is allowed. The operation is consumed once reserved regardless of result.

## Local readiness evidence

Twenty-two focused tests, Python syntax, manifest/no-action verification and exact-window binding pass. `--run` currently refuses `P07_DIAGNOSTIC_REFUSED_OWNER_APPROVAL_INVALID` before hidden input or external access. Backend evidence: `evidence/APP-013/p07-read-only-diagnostic-window-preparation-20261021.md` and `evidence/APP-013/p07-read-only-diagnostic-package-preparation-20261021.md`.

## Decision requested

Approve or refuse this one exact read-only operation before **1:55 p.m. Eastern**. Approval authorizes only the allowed actions above within the bound window. It does not authorize a P07 readiness mutation, Stripe configuration, deployment, payment or P08.

Accepted progress remains **0/27 newly closed R1 packages; 6/60 legacy packages; 4/8 walkthrough milestones; 0/13 full-intelligence rows**. **No scope deviation from the approved P07-specific narrowing.**
