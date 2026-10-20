# APP-013 / 2B / P06-R11 — pooled-host mapping correction decision

## Demonstrated gap

Consumed mapping operation `57d87c24-2f4b-4575-87f2-0480afce77bb` returned `NO_MATCH` after comparing shared secret version 2 only to the two direct hostnames derived from current Neon endpoint IDs. The receipt is valid and terminal; never rerun it.

Official Neon documentation states that a pooled connection inserts `-pooler` after the compute endpoint ID. The approved inventory/helper omitted the two pooled variants. Therefore `NO_MATCH` establishes only **no direct-host match**. It does not establish no current-branch match, and it does not prove the secret is pooled. This is our implementation-card omission.

## Alternative 1 — one corrected read-only mapping

Recommended. Plan `78800c38-11fd-4b5b-89a7-865e4a9f7b2c`; proposed operation `e13000fe-7d13-4e9c-9e39-a164873c98ce`.

- **Section/criterion:** APP-013/2B/P06-R11 security prerequisite; map shared secret version 2 to the current Neon branch and connection mode before any containment mutation. No frozen criterion/count/milestone change.
- **Source/gap:** consumed direct-only receipt above; official Neon pooled-host format; authenticated October 3 inventory of project `soft-smoke-54063480`, production branch/endpoint and isolated child branch/endpoint.
- **Expected files:** one new local helper/test/evidence set or a reviewed minimal successor to the consumed mapper; governance current-status updates. Never edit or reuse the consumed installed package. No application `src/`, schema, migration or dependency change.
- **Exact candidates:** for each of the two fixed endpoint IDs, generate exactly its direct hostname and documented `endpoint-id-pooler` hostname under verified `us-east-2.aws.neon.tech`. Compare the secret hostname in memory against exactly four unique candidates.
- **Output:** `MATCHED_UNIQUE` with branch ID, endpoint ID and connection mode `DIRECT` or `POOLED`; otherwise `NO_MATCH`, `AMBIGUOUS` or a fixed consumed stop. Never output/persist raw host, URL, password, payload or their hashes. A match supports only a later mutation proposal.
- **Authority/data/state:** access only `projects/signmons/secrets/signmons-staging-database-url/versions/2` once during a fresh fixed window. No Neon credential screen, database connection/query, customer/business row or mutation.
- **Tests:** unique direct and pooled match for each branch; no match; ambiguity; exact candidate count; suffix normalization; identity/payload refusal; approval/source/inventory/window/mode guards; concurrency/one-use; access refusal/timeout; redaction; `--check` no action.
- **Checklist:** implement/test; fresh console metadata readback without Connect; create fixed private inventory; bind exact source/inventory/approval/window; install 0700/0600; no-action check; invoke once; verify sanitized receipt; record stop.
- **Owners/dependencies:** owner approves this corrected operation, supplies one future 30-minute Eastern window and confirms authenticated Neon availability. Implementer owns local correction, fixed metadata inventory, package/readback and evidence.
- **Exclusions:** no credential reset, secret version, IAM, deployment, traffic/tag/job/session action, database access, provider request, customer journey, limit change or automatic retry.
- **Rollback/finish:** read-only has no external rollback. Any attempt/uncertainty consumes the new operation. Finish is one sanitized direct/pooled mapping result with no external state change.

## Alternative 2 — pause containment work

Perform no new read. Keep all credential rotation, shared-secret, deployment, traffic, job, session and live-journey work blocked because the exposed administrator credential remains unresolved.

## Approval required

Choose Alternative 1 and provide a future 30-minute Eastern window with authenticated Neon Console availability, or choose Alternative 2. No correction implementation, installation, secret access or mutation is authorized by this proposal. P06 remains 12/14; R11/full R12 remain open; accepted milestones remain 3/8. No scope deviation implemented.

## Owner decision and local preparation

The owner replied **yes i approve**, selecting Alternative 1. This authorizes the exact local correction and one later read-only operation, but no external read may occur until a fresh 30-minute Eastern window and authenticated Neon availability are recorded.

The successor helper now generates exactly direct and documented pooled candidates for each fixed endpoint and projects connection mode only on a unique match. Ten focused tests, compilation, architecture, governance and whitespace pass. Prepared SHA-256 is `271b812d980e00f80937d0a8934b9ade07861ee0a9c410e0948e1bd215fe74b1`. PENDING root, zero inventory hash and 2099 window deliberately prevent live use. No external action occurred. No scope deviation.

The owner then supplied October 3, 2026, 7:00–7:30 a.m. Eastern (11:00–11:30 UTC). The one-use helper must start before 7:20 a.m. The root/window binding may be prepared now, but authenticated Neon metadata must be refreshed within 30 minutes of execution before the inventory hash, source hash, approval and installed package are finalized. No stale inventory substitution.
