# APP-013 / P06-R11 production database-auth validation

Prepared only; not approved. Plan `99aff7e4-f8bd-43db-87d5-ca1b82ab477d`, operation `9f77eff4-0388-4de4-93a4-feaf909b4417`, proposed for 8:00-8:25 a.m. Eastern on 2026-10-05 with an 8:10 a.m. start deadline.

## Demonstrated gap and acceptance criterion

The owner reports that `ALTER ROLE neondb_owner WITH PASSWORD '<private value>';` succeeded in the Neon production branch SQL Editor. The prior saved-password diagnostic returned `AUTH_REFUSED` for both production endpoints, so the new password has not yet been authenticated from the local PostgreSQL client.

The exact missing evidence is one sanitized read-only result for both the direct and pooled current production endpoints. Acceptance is an immutable result containing only one fixed classification per endpoint: `ACCEPTED`, `AUTH_REFUSED`, `DNS_REFUSED`, `TIMEOUT`, `TLS_REFUSED`, `CONNECTION_REFUSED`, or `OTHER_REFUSED`.

## Bounded operation

The owner-operated helper accepts the newly saved password once through a hidden terminal and runs only `SELECT 1` against the direct and pooled production endpoints. It writes no database data, stores no password or server text, deletes its temporary pgpass file, and zeroes its mutable password buffer. A reservation marker makes every invocation terminal; there is no automatic retry.

It does not access or change Google Secret Manager, Cloud Run, the migration job, traffic, tags, sessions, customer data, messages, appointments, payments, or billing. A successful result supports a later, separately prepared credential cutover proposal; it does not authorize that mutation.

## Traceability and state

- Section: APP-013 / P06-R11, within 2B controlled-acceptance preparation.
- Connected workflow: restore database-backed staging readiness needed before any controlled intake acceptance journey.
- Source: `scripts/p06-r11-db-auth-diagnostic.py` plus focused tests.
- Rollback/disabled state: no application or external state changes; the current disabled P06 tag and normal Cloud Run traffic remain untouched.
- Observable finish: one one-use classified result or one terminal stop marker.
- Accepted baseline remains 1A/1B/2A, 3/8.

No scope deviation.

## Consumed result

The approved operation ran once at `2026-10-05T12:02:34.039593Z` and returned `R11_DB_AUTH_DIAGNOSTIC_CAPTURED`. Both the direct and pooled endpoints classified the supplied private credential as `AUTH_REFUSED`. The reservation and result records exist, no temporary pgpass file remains, and the operation is consumed. It must not be rerun.

This result does not disprove the reported SQL `ALTER ROLE` success. It proves that the private value supplied to this diagnostic did not authenticate as production `neondb_owner` at either current production endpoint. No secret, deployment, traffic, job, database row, customer, message, appointment, or payment state changed.

The next smallest diagnostic is to verify the SQL Editor's selected branch and session identity without exposing credentials, then prepare any credential correction as a new operation. No mutation is authorized by this result.
