# APP-013 / 2B / P06-R11 — child read-only qualification decision

## Decision status

Owner confirmed current child `neondb_owner` password custody without disclosing it. Local preparation is decision-ready. No operation identity, private package, execution window or external read exists.

## Section and observable finish

- Section: APP-013 / 2B / P06-R11 with R12 containment.
- Criterion served: establish current retained phone/address liability and disabled child runtime state before any later controlled connected journey.
- Finish: one fixed child-target `REPEATABLE READ READ ONLY` receipt containing only aggregate counts/micros, invalid counts and approval/role/session classifications, followed by rollback and connection close.
- This does not accept R11/2B, authorize provider/release Phase B, or increase the 3/8 denominator.

## Exact target and source binding

- Backend HEAD: `3cf8a9dc53d0282a35e6263a36d749c5b32f8e2e` with preserved reviewed dirty APP-013 work.
- Project: `soft-smoke-54063480`.
- Branch: `br-sparkling-sun-ay6gr5e8`.
- Direct endpoint: `ep-jolly-flower-ayc6w9hv.c-5.us-east-2.aws.neon.tech:5432`.
- Database/role: `neondb` / owner-private `neondb_owner`.
- Query source: backend `scripts/p06-r11-post-cutover-query.mjs`, SHA-256 `8c2214a7acfe76c8add13c99b77324f74acd7150c6a2696a10249adaa7704da3` at decision preparation.
- Target source: backend `scripts/p06-backup-once.mjs`, SHA-256 `46a29de169dd32725b313bf57dcf870d990f30f497d42f535cef893583d0bf26`.
- Explicitly forbidden target: production parent `ep-nameless-frog-ayk5gr5y...` and any pooled/shared application URL.

## Finite execution

1. After owner approval of a future 25-minute Eastern window, create fresh plan/operation identities and one private 0700 package with 0600 files.
2. Bind exact source hashes, child target, owner approval/window, no retry and absence of prior markers. Reject parent/pooler/override inputs before prompting.
3. Accept the saved child owner password through the existing hidden TTY to anonymous-pipe transport. Never display, log, persist or pass it in argv/environment.
4. Connect only to the fixed direct child; verify `neondb`, `neondb_owner`, PostgreSQL18 and read-only mode.
5. Begin one `REPEATABLE READ READ ONLY` transaction and read:
   - fixed-account phone hold total/valid/invalid counts and held micros;
   - fixed-account/fixed-tenant address counts, held micros and invalid-row count;
   - child controlled-phone/runtime approval booleans;
   - child `p06_intake_runtime` LOGIN, connection-limit, expiry and active-session count.
6. Return fixed aggregate classifications only. Never return account SID, tenant/account UUID, phone/address/code/customer values, audit rows or payloads.
7. Roll back and close before writing a success receipt. Any authentication, target, identity, query, shape, runtime-open or uncertainty condition saves a consumed sanitized stop with no retry.

## Tests and stop rules

Existing fourteen fictional tests cover valid/invalid phone rows, closed state, historical ceiling, approvals, LOGIN, connection limit, expiry, active session, invalid liability rows, runtime-shape drift, full-reader stage progression, negative invalid data and address parse failure. Preparation must rerun them plus syntax, formatting, exact target/source binding, no-action check, governance baseline/consistency, 21 governance tests and whitespace.

No Cloud Run, Artifact Registry, Twilio, provider, browser or release read belongs to this operation. Even a clean child receipt stops for a separate Phase B decision. A stop is terminal; no automatic replacement.

## Exclusions and owner gate

Excluded: production-parent connection, child-secret access, password trial/reset, LOGIN change, hold/ceiling change, database write, migration, provider call/message, build, IAM, secret/version change, deployment, traffic/tag, browser/customer/job/payment/appointment action.

Owner must approve the exact decision and supply a future 25-minute Eastern window before operation/package preparation or database access. P06 remains 12/14; R11/full R12 remain open; accepted milestones remain 3/8. No scope deviation.
