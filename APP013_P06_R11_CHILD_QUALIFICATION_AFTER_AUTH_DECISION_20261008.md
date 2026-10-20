# APP-013 / 2B / P06-R11 — child qualification after verified authentication

## Verified prerequisite

Connection-only plan `a72ec2f2-3308-4a97-b532-3a3b4702d408`, operation `bc83b9bd-5dcd-4fe8-81f9-f836090a5390`, returned `AUTH_ACCEPTED` at `2026-10-08T12:12:05.075Z` against the fixed direct child endpoint. Its receipt states `sqlExecuted:false`; no stop exists. The diagnostic is consumed and must never be rerun.

This verifies the owner-saved child `neondb_owner` password and exact endpoint at that instant. It does not qualify database identity, liabilities, approval, role, session or runtime state and does not explain the earlier terminal connection stop.

## Proposed bounded qualification

Alternative 1 is one fresh 25-minute child read-only qualification:

1. Bind new identities to backend HEAD `3cf8a9dc53d0282a35e6263a36d749c5b32f8e2e`, child project `soft-smoke-54063480`, branch `br-sparkling-sun-ay6gr5e8`, direct endpoint `ep-jolly-flower-ayc6w9hv.c-5.us-east-2.aws.neon.tech`, `neondb` / `neondb_owner`, query source `scripts/p06-r11-post-cutover-query.mjs` SHA-256 `8c2214a7acfe76c8add13c99b77324f74acd7150c6a2696a10249adaa7704da3` and target source `scripts/p06-backup-once.mjs` SHA-256 `46a29de169dd32725b313bf57dcf870d990f30f497d42f535cef893583d0bf26`.
2. Reject production parent, pooled and override targets before hidden owner-private password input.
3. Make one connection attempt with a ten-second timeout; verify `neondb`, `neondb_owner`, PostgreSQL18 and server-enforced read-only transaction state.
4. In one `REPEATABLE READ READ ONLY` transaction, read only fixed-account phone aggregates, fixed-account/fixed-tenant address aggregates, controlled phone/runtime approval booleans and child `p06_intake_runtime` LOGIN/connection-limit/expiry/active-session classifications.
5. Return aggregate counts/micros, invalid counts and classifications only; never return identifiers, customer/contact/address/code values, audit rows or payloads.
6. Roll back and close before saving a receipt. Stop after Phase A regardless of outcome. Cloud Run, Artifact Registry, Twilio, browser and release Phase B remain unauthorized.

Any attempt, unexpected condition or uncertainty consumes the operation. No automatic retry. Alternative 2 is pause.

## Required checks and exclusions

Preparation reruns the fourteen fictional reader tests, syntax, formatting, exact source/target binding, no-action check, governance baseline/consistency, 21 governance tests and whitespace. Excluded: password reset, secret access, LOGIN/hold/ceiling change, write, migration, provider/cloud read, build, IAM, deployment, traffic/tag, message, browser/customer/job/payment/appointment action.

Owner approval of Alternative 1 plus a future 25-minute Eastern window is required before package preparation or database access. P06 remains 12/14; R11/full R12 remain open; accepted milestones remain 3/8. No scope deviation.

Owner approved Alternative 1 for October 8, 8:25–8:50 a.m. Eastern. Fresh plan `cc12e321-8a24-4223-b13b-a08859ffd80b`, operation `aef7930e-99ff-4a9c-bb71-09453e35640e`, is privately prepared at `/private/tmp/r11-child-qualification-20261008-0825`. Exact source/target/approval/window bindings, private modes, no-action preflight, formatting and fourteen focused tests pass; no marker or external read exists. Invoke once in-window. Any attempt or uncertainty consumes it.
