# APP-013 / P06-R11 production role password reset

Owner authorized one owner-operated Neon Console password reset on 2026-10-05. Plan `71088eb4-a6c8-444f-84e1-eb84b750eb3e`, operation `570c2856-64d1-40ab-a4af-8a7c0ebe6c91`.

## Exact target and action

- Neon branch: `production`, branch ID `br-young-term-ayfi7ist`
- Primary compute: `ep-nameless-frog-ayk5gr5y`
- Database: `neondb`
- Role: `neondb_owner`
- Action: one use of Neon Console **Connect -> Reset password**, followed by private capture of the generated password in Apple Passwords.

The owner must confirm all four target identifiers in the console before clicking Reset. Any mismatch stops the operation. The password must not enter chat, repository files, shell history, evidence, screenshots, or the existing Google secret. Only the owner handles and saves it.

## Boundaries and finish

The operation authorizes exactly one production role password reset. It does not authorize a child-branch reset, SQL `ALTER ROLE`, Google Secret Manager change, Cloud Run deployment, traffic/tag/session change, migration-job update or execution, database row change, customer action, message, appointment, payment, or retry.

Observable finish is Neon displaying the newly generated password once and the owner confirming it was saved privately. Authentication validation will be a later fresh one-use read-only operation. If the console refuses, the target differs, or the password is lost, stop without another reset.

This advances APP-013/P06-R11 database-backed staging recovery within 2B controlled-acceptance preparation. Accepted baseline remains 1A/1B/2A, 3/8.

No scope deviation.

## Owner completion

The owner returned `PRODUCTION_ROLE_RESET_SAVED`, confirming that the one authorized production reset completed and the Neon-generated password was saved privately. No password entered evidence or chat. This operation is complete and must not be repeated under this authorization.
