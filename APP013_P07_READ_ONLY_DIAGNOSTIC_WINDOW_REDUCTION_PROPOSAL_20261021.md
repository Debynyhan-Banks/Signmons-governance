# APP-013 / 3A / P07 read-only diagnostic window reduction proposal

Status: **Alternative 1 owner-approved and locally completed; no external action authorized**.

## Demonstrated process gap

The current 90-minute P07 window was designed for a mutation-capable readiness operation that could create a database role, secrets, a service identity, IAM bindings, a disabled Stripe destination and a zero-traffic revision, followed by mandatory containment and later retirement. That duration remains appropriate for such an operation.

Repair 5 has a narrower immediate purpose: identify one failed database-preflight predicate through read-only Stripe Sandbox inspection and one exact read-only database transaction. It must not create or change a role, grant, secret, identity, binding, destination, revision, job, payment, calendar record or customer record. Applying the mutation-capable 90-minute envelope to this diagnostic delays R1-W01 without adding corresponding containment value.

This proposal changes only the next P07 diagnostic. It does not create a general exception for provider, deployment, payment or customer actions and does not alter any MVP section, package, acceptance criterion, dependency or denominator.

## Alternatives

| Alternative | Effect | Recommendation |
| --- | --- | --- |
| 1. Thirty-minute P07 diagnostic window | Prepare a diagnostic-only package with a 10-minute start cutoff, read-only completion by minute 20, verified connection closeout by minute 25 and support/containment through minute 30. | **Recommended** |
| 2. Forty-five-minute diagnostic with a transport retry | Allows one retry after a claimed pre-query connection failure, but proving that no statement reached the server adds ambiguity and controller complexity. | Reject |
| 3. Keep the 90-minute envelope | Preserves the mutation-capable schedule for an operation that cannot mutate, continuing avoidable owner wait time. | Reject for this diagnostic only |

## Exact Alternative 1 contract

After approval, local preparation may create one fresh disabled diagnostic-only package derived from the reviewed Repair 5 classifier. It must have new plan, packet and operation identifiers and must preserve Repair 5 and every consumed package unchanged.

The future attended window is exactly 30 minutes:

- window opens at the owner-selected start time;
- strict start cutoff is 10 minutes after opening;
- the read-only inspection and database classification must finish by minute 20;
- database connection closure and sanitized receipt readback must finish by minute 25;
- containment/support ends at minute 30.

The package must:

1. Require the current CHILD administrator password through hidden Terminal input and never store, echo or transmit it through chat.
2. Allow only fresh read-only Stripe Sandbox qualification needed to produce the sanitized mode, administrator-access, enabled-account-count, destination-absence and connected-account SHA-256 fields. The raw connected-account identifier remains in browser/process memory only and is discarded.
3. Execute only the reviewed exact-job/role/tenant `SELECT` statements inside `BEGIN TRANSACTION ISOLATION LEVEL REPEATABLE READ READ ONLY` and always issue `ROLLBACK` before connection closure.
4. Retain `PGSSLMODE=verify-full`, `PGSSLROOTCERT=system`, a bounded connection timeout and a unique operation-scoped application name.
5. Emit only one fixed Repair 5 classification or a fixed transport/TLS/authentication/closeout stop. Persist no raw SQL output, database error, role row, job/customer field, account identifier, database URL or private browser link.
6. Contain no callable role, grant, secret, IAM, destination, deployment, payment, booking, message or customer-mutation path. Tests must prove those commands/resources are absent from the diagnostic controller, not merely disabled by flags.
7. Reserve at most one diagnostic attempt. Automatic retry remains false. Recovery may close or verify an uncertain connection but may not rerun the diagnostic query.
8. Produce a mandatory sanitized closeout receipt proving rollback requested, connection terminated, operation-scoped sessions absent and no mutation path present. A truthful closeout failure remains a stop.

The local preparation must test positive classification, every fixed predicate, malformed output, first-failure ordering, timeout/interrupt behavior, start cutoff, live-clock deadlines, hidden input, absence of mutation functions/commands, secret leakage, rollback and truthful closeout. `--run` must refuse until an exact window binding and separate owner approval are installed.

## Boundaries retained

The 90-minute-or-longer envelope remains required when an operation can create or change database roles/grants, secrets, IAM, Stripe configuration, Cloud resources, deployments, payments, appointments, messages or customer data. No later operation inherits this 30-minute exception automatically.

This proposal does not authorize local package implementation, browser or database access, a Stripe action, deployment, payment, booking, customer contact, retry, merge or push. Approval of Alternative 1 would authorize only the diagnostic-only local package and tests. The bound 30-minute external diagnostic would still require a separate exact proposal and owner approval.

## Impact and next decision

R1-W01 / APP-013/3A/P07 remains active. Repair 5 remains disabled and unchanged. P08 and the authentic same-job Sandbox payment remain separate. Accepted progress remains **0/27 newly closed R1 packages; 6/60 legacy packages; 4/8 walkthrough milestones; 0/13 full-intelligence rows**.

**Owner decision:** Debynyhan Banks approved Alternative 1 for local diagnostic-only package preparation and testing. The approval did not authorize browser or database access.

## Local preparation result

Fresh private package `/private/tmp/p07-read-only-diagnostic-20261021-prep1`, plan `55d7dc3a-4fe3-4f09-8ada-bcbd7ef3ad02`, packet `3acd1d03-07bf-4007-a399-03ff2d30a9b4` and operation `c15a9092-f421-4c5b-94bd-4e7b158c6595`, implements the exact 30-minute envelope in a diagnostic-only controller. Its manifest SHA-256 is `1e5aced9a7aded528bbb60e0402cb65b67bf30bb4cdb5f71706832535788510b`.

Twenty-two focused tests, syntax and no-action verification pass. Run and recovery refuse before hidden input because no window is bound. Tests cover timing, live-clock enforcement, exact approval, no retry, every predicate, malformed output, ordering, hidden input, TLS, timeout/interrupt, read-only SQL, rollback, absence of mutation/provider-resource functions, zero-session closeout, closeout-only recovery and private-value non-disclosure.

Backend evidence: `evidence/APP-013/p07-read-only-diagnostic-package-preparation-20261021.md`. No application or external state changed. A fresh attended 30-minute window, binding/retest and separate exact external approval remain required.

Accepted progress remains **0/27 newly closed R1 packages; 6/60 legacy packages; 4/8 walkthrough milestones; 0/13 full-intelligence rows**. **No scope deviation from the approved P07-specific narrowing.**
