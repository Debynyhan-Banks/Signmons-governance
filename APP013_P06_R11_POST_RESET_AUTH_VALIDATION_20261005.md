# APP-013 / P06-R11 post-reset authentication validation

Prepared only; not approved. Plan `1f681cc1-bf0a-4ace-a4b6-f4dc806a46ec`, operation `c61dba09-5f4c-4bc4-932c-dfc2575b57cd`, proposed for 8:25-8:50 a.m. Eastern on 2026-10-05 with an 8:35 a.m. start deadline.

The owner completed the separately authorized Neon Console production `neondb_owner` reset and saved the generated password privately. The exact remaining evidence is whether that generated password authenticates at the current direct and pooled production endpoints.

The owner-operated helper accepts the generated password once through a hidden terminal and runs only `SELECT 1` against both endpoints. It stores fixed classifications only, deletes its temporary pgpass file, zeroes its mutable password buffer, and marks every invocation terminal. It performs no database write, secret access/change, deployment, traffic/tag/session change, migration-job action, customer action, message, appointment, payment, or retry.

Observable finish is one immutable direct/pooled classification result or one terminal stop. If both endpoints return `ACCEPTED`, the result supports a later separately approved credential cutover; it does not authorize that cutover.

Section APP-013/P06-R11 within 2B controlled-acceptance preparation. Accepted baseline remains 1A/1B/2A, 3/8. No scope deviation.

## Consumed result

The approved operation ran once at `2026-10-05T12:28:53.076396Z` and returned `R11_DB_AUTH_DIAGNOSTIC_CAPTURED`. Both the direct and pooled endpoint probes classified the privately supplied generated password as `AUTH_REFUSED`. Attempt and result markers exist, the temporary pgpass file is absent, and this operation must not be rerun.

The result proves that the private value entered after the console reset did not authenticate against the two fixed hosts used by the diagnostic. It does not prove whether the Neon Connect panel currently maps the selected production branch to those hosts, or whether a different clipboard value was entered. The next smallest step is a metadata-only visual comparison of the production Connect hostname to `ep-nameless-frog-ayk5gr5y.us-east-2.aws.neon.tech`; no credential should be exposed.

No external mutation occurred during validation. No additional reset, authentication attempt, secret/version change, deployment, traffic/job/session action, customer action, message, appointment, or payment is authorized.
