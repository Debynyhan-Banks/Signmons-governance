# APP-013 / 3A / P07 database TLS diagnostic correction proposal

Status: **owner decision pending; no implementation or external action authorized**.

## Demonstrated gap

Consumed repair-3 operation `0ae8a2a9-530f-47c6-80da-3bcd740a821d` passed Cloud and sanitized Stripe preflight, then stopped at database preflight with `P07_STOP_COMMAND_FAILED`. Receipts prove no mutation and verified containment, but the controller intentionally discarded raw `psql` stderr and therefore cannot distinguish connection, TLS, authentication, schema/query or expected-state failures.

Local inspection after closeout found:

- Homebrew `psql` is PostgreSQL 16.11 with OpenSSL;
- `$HOME/.postgresql/root.crt` is absent;
- the controller sets `PGSSLMODE=verify-full` but does not set `PGSSLROOTCERT`;
- installed PostgreSQL 16 documentation states that operating-system trust is selected with `sslrootcert=system`, which enforces `verify-full`;
- the repository's existing backup path explicitly pairs `PGSSLMODE=verify-full` with `PGSSLROOTCERT=system`;
- the Node closeout connected successfully using system certificate trust and the same private administrator password.

This is strong evidence of a missing libpq system-root setting, but it is not live proof of the exact repair-3 failure because raw error text was not retained and the consumed operation cannot be replayed.

## Alternatives

| Alternative | Effect | Recommendation |
| --- | --- | --- |
| 1. Add explicit system-root verification and sanitized failure classification | Set `PGSSLROOTCERT=system` on every controller `psql` call while retaining `PGSSLMODE=verify-full`; classify raw stderr only in memory into fixed TLS, connection, authentication, schema/query or generic codes, then discard it. | **Recommended** |
| 2. Weaken TLS to `require` | Avoids root-certificate validation but loses hostname/CA verification already required by the reviewed design. | Reject |
| 3. Create and manage a private root-certificate file | Adds local certificate-file lifecycle and permission scope when PostgreSQL 16 already supports system trust explicitly. | Reject |

## Exact proposed local change

- Create a fresh disabled package with new plan, packet and operation IDs; preserve all consumed packages unchanged.
- Add `PGSSLROOTCERT=system` to both administrator and generated restricted-role `psql` environments. Retain `PGSSLMODE=verify-full`; do not add a fallback.
- Keep passwords and raw stderr only in process memory. Never display or persist either.
- Convert recognized stderr patterns to fixed stop codes only:
  - `DATABASE_TLS_CONFIGURATION`
  - `DATABASE_CONNECTION`
  - `DATABASE_AUTHENTICATION`
  - `DATABASE_SCHEMA_OR_QUERY`
  - `COMMAND_FAILED` for unclassified errors.
- Preserve exact job/tenant/account-hash checks and existing receipt fields.
- Add tests for system-root presence on both `psql` paths, no TLS downgrade, every classified error, unclassified fail-closed behavior, and absence of raw stderr/private values from terminal output and receipts.
- Run package, syntax, no-action/refusal, governance, architecture and whitespace checks.

No database connection, role/grant/secret/IAM/Stripe/deployment action, payment, booking, customer action or new acceptance credit is included. After local implementation review, a fresh attended window and separate exact external approval would still be required.

## Decision requested

Approve or refuse Alternative 1 for local correction and testing only. Approval does not authorize a live database diagnostic or another readiness attempt.

Accepted progress remains **0/27 newly closed R1 packages; 6/60 legacy packages; 4/8 walkthrough milestones; 0/13 full-intelligence rows**. **Proposed correction to a newly demonstrated database-client diagnostic gap; implementation pending owner approval.**
