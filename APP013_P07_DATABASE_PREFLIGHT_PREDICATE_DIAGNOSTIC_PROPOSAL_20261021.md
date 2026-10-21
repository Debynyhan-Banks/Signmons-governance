# APP-013 / 3A / P07 database-preflight predicate diagnostic proposal

Status: **owner decision pending; no implementation or external action authorized**.

## Demonstrated gap

Owner-approved repair 4 proved the TLS correction: the administrator connection and exact database query completed far enough to evaluate expected state. It then stopped `P07_STOP_DATABASE_PREFLIGHT_DRIFT`. Receipts prove `possibleMutation:false` and verified containment.

Source inspection shows that `db_preflight` collapses multiple independent checks into the same stop code:

- exact database and administrator identity;
- absence of the proposed P07 role;
- closed P06 role state and zero sessions;
- exact job count, `CREATED` state and undeleted state;
- absence of payment and calendar activity;
- controlled-admission digest and absence of a payment-policy binding;
- tenant connected-account format, sanitized hash match and charges-enabled state.

The controller intentionally clears raw query output and the account identifier. This is correct for privacy, but the current fixed code cannot identify which predicate drifted. Another unchanged readiness attempt would be blind and is rejected.

## Alternatives

| Alternative | Effect | Recommendation |
| --- | --- | --- |
| 1. Add secret-safe per-predicate classification locally | Prepare a fresh disabled diagnostic package that maps each exact predicate to a fixed allowlisted result, retains no raw values, proves output sanitization and refuses live use without a new window and exact approval. | **Recommended** |
| 2. Retry the full readiness operation unchanged | Repeats a consumed operation pattern without learning which prerequisite differs and may waste another attended window. | Reject |
| 3. Remove or loosen the preflight | Could allow role, job, payment, calendar, policy or tenant-account drift to reach mutations. | Reject |

## Exact proposed local change

- Create a fresh disabled private package with new plan, packet and operation identifiers. Preserve repair 4 and every earlier package unchanged.
- Keep `PGSSLMODE=verify-full` and `PGSSLROOTCERT=system` on every `psql` path.
- Parse only the existing exact preflight fields in process memory and return one fixed code for the first failed predicate. Candidate codes are limited to database identity, P07-role collision, P06-role state, exact-job count/state/deletion, payment activity, calendar event/operation activity, controlled-admission policy, account format/hash and charges-enabled failures.
- Never emit or persist a password, hostname, username, role row, job/customer field, account identifier, database URL, raw SQL output or raw exception.
- Add positive, negative, malformed-output, multi-failure ordering and secret-leak tests for every fixed code.
- Run the focused suite, syntax, no-action/refusal, governance, architecture and whitespace checks.

This local change may touch only the fresh private controller/test/manifest/README and evidence/governance records. It changes no application source, database state, role, grant, secret, IAM binding, Stripe configuration, deployment, payment, booking or customer data.

## Dependency and next external gate

After local correction review, a separate owner-approved read-only diagnostic with a fresh attended window would be required. That future action would use the current CHILD administrator password through hidden input, run a repeatable-read read-only exact-job/role/tenant predicate check, roll back, close the connection and retain only one fixed classification. It would not create or alter any role, record, secret, provider resource or deployment.

## Decision requested

Approve or refuse Alternative 1 for local correction and testing only. Approval would not authorize a database connection, another readiness attempt, Stripe action, deployment, payment or customer action.

Accepted progress remains **0/27 newly closed R1 packages; 6/60 legacy packages; 4/8 walkthrough milestones; 0/13 full-intelligence rows**. **Proposed diagnostic correction to a newly demonstrated observability gap; not yet implemented.**
