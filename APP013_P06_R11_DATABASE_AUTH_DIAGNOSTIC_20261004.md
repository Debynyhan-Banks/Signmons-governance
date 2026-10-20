# APP-013 / P06-R11 database-auth diagnostic proposal

Prepared only; not approved. Plan `2ce87c95-6e25-4528-843a-0438546bbece`, operation `80157d3d-27c0-4241-96ae-524c85692f4c`, proposed for 8:35-9:00 p.m. Eastern on 2026-10-04 with an 8:45 p.m. start deadline.

The prior direct-copy recovery stopped before adding a secret. The saved value begins with Neon's `npg_` password prefix, and the production compute confirms endpoint `ep-nameless-frog-ayk5gr5y`. The missing evidence is the sanitized PostgreSQL failure category.

The proposed owner-operated helper accepts the saved password once through a hidden terminal, runs only `SELECT 1` against the direct and pooled production endpoints, stores only fixed classifications, deletes its temporary pgpass file, and zeroes its mutable password buffer. It performs no reset, secret access/change, deployment, traffic update, job execution, customer action, message, appointment, or charge. One-use markers forbid retry.

Acceptance: one immutable result with `ACCEPTED`, `AUTH_REFUSED`, `DNS_REFUSED`, `TIMEOUT`, `TLS_REFUSED`, `CONNECTION_REFUSED`, or `OTHER_REFUSED` for each endpoint. This advances APP-013/P06-R11 credential containment without changing the frozen acceptance baseline. No scope deviation.

## Follow-up proposal

The first diagnostic captured `AUTH_REFUSED` for both endpoints. Neon confirmed the production role reset timestamp, and the owner then set a new private password explicitly with `ALTER ROLE` in Neon SQL Editor. A fresh read-only validation is proposed for 8:45-9:10 p.m. Eastern, starting before 8:55 p.m.: plan `06ba0777-6527-41cf-ba41-6c822e1f5f12`, operation `14d29718-d33c-4cf9-ace9-6657777973ab`, package `/private/tmp/r11-db-auth-diagnostic-20261004-2045`. It has the same read-only boundaries and is not yet approved.

That proposal was revoked before action while clarifying that SQL Editor does not display the chosen password. The owner confirmed a private value was used. A fresh read-only validation is proposed for 8:55-9:20 p.m. Eastern, starting before 9:05 p.m.: plan `2d5e146b-6318-45be-bce1-cb05114de092`, operation `7210e148-9e3f-48a5-b396-1bd307bbf3a0`, package `/private/tmp/r11-db-auth-diagnostic-20261004-2055`.
