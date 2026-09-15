# P06 item 3 — one staging migration change set

## Current target amendment and qualification handoff — 2026-09-15

R01 upgrade rehearsal and R02 target/access/consumer/recovery qualification are complete; see backend p06-r02-qualified.md. Owner approved preparing existing neondb_owner for one supervised migration of child br-sparkling-sun-ay6gr5e8 / ep-jolly-flower-ayc6w9hv.c-5.us-east-2.aws.neon.tech / neondb/public only. This supersedes the older shared-secret-version2 target below: NEVER use signmons-staging-database-url or the old Cloud Run migration job for this child migration. No parent credential reset, shared-secret replacement or new-role ownership transfer. Credential retains parent access; exact endpoint guards constrain the process, not credential power.

R03 remains the exact tested executable packet/owner approval gate. R04 remains one separately authorized migration. Reuse accepted admin-v2 recovery through its documented expiry unless invalidated by drift; no repeated backup as another section. R03 must verify actual connection timeouts, manifest, current recovery, child-exclusive maintenance, cost and absolute window before asking for execution. This document is NOT an executable command and does not assert runner qualification. Preserve all existing13SQL files and failure/rollback restrictions below.

## Authority and finish

Owner requested preparation after the approved read-only check. **Plan only: no staging migration, backup/branch creation, data copy, deployment, secret change or paid action authorized.** Source SQL: backend 53037fbd118cc4547061dfaf373c45b20a05962b, unchanged at cab1df4; image digest ea47a8371a04f773a5c51fc4f939250b7045eba92d3cbbeb68e49ceb0240be35. Governance entry dd05b88. Same APP-013 / 2B / P06 item 3; these are 13 existing files, not 13 new sections. No scope deviation.

Observable finish for this change set: exact staging target has all 26 expected successful migration records with matching checksums and expected schema/constraints/triggers, existing synthetic-data invariants survive, baseline application remains compatible, new intake stays disabled. Owner-approved execution and actual readback are required; this plan does not satisfy that finish.

## Inspected ordered SQL and effects

Apply the following exact existing directories in lexicographic migration order; do not edit, squash, skip or mark them applied. Two directories share 20260909190000; full directory names determine order.

| # | Directory suffix after date/time | Effect and review concern |
| --- | --- | --- |
| 1 | 20260908120000_add_sms_enqueue_intents | Creates SMS intent enum/table, bounded attempts, tenant/job/event foreign keys, unique/indexes. No historical enqueue/backfill. |
| 2 | 20260908180000_add_calendar_operation_journal | Creates calendar enums/journal, state/shape checks and partial unique unfinished-job index. No calendar writes or historical recovery generated. |
| 3 | 20260909190000_add_appointment_email_intent | Creates intent table/indexes and immutable-update function/trigger. Function is reused by #5. |
| 4 | 20260909190000_add_calendar_readback_deadline | Adds nullable readbackNotBefore to the newly created journal. Depends on #2. |
| 5 | 20260909200000_extend_appointment_email_events | Creates cancellation snapshot/immutable trigger; drops and replaces two checks on the new email intent table. Depends on #3; do not call the whole set purely additive. |
| 6 | 20260909210000_add_appointment_email_consent_evidence | Creates scope/evidence/binding, immutable triggers and serialized revision trigger. RESTRICT relations affect future retention; no consent or sending authority created by DDL. |
| 7 | 20260911120000_add_address_operation_liability | Creates operation/request liability ledger, checks and indexes. Does not grant provider authority or reset holds. |
| 8 | 20260911130000_add_address_execution_deadline | Adds nullable executionDeadline to #7. |
| 9 | 20260912150000_fixture_sms_consent_evidence | Creates fixture-only state/prompt tables and revision trigger. Empty storage does not enable fixture routes; keep fixture runtime disabled. |
| 10 | 20260912160000_tenant_sms_policy_registry | Creates policy version/head, FKs and immutable UPDATE/DELETE trigger. Future referenced records can restrict deletion; no policy publication. |
| 11 | 20260912170000_sms_consent_revision | **Existing SmsConsentRecord**: adds required revision default1 and positive check; installs increment-on-every-update trigger. Existing rows acquire revision1 semantics; existing writers invoke new behavior. Must rehearse on old-schema synthetic rows. |
| 12 | 20260912180000_sms_policy_capture | Creates dry-run capture, FKs/indexes and immutable provenance trigger; depends on #10. Does not allow live sending. |
| 13 | 20260913180000_nullable_property_location | **Existing PropertyAddress**: removes NOT NULL from googlePlaceId/latitude/longitude. No value rewriting; new nulls would be incompatible with assumptions in older readers. Keep intake disabled and prohibit new null writes until version compatibility is accepted. |

All 13 files were read. No top-level INSERT/UPDATE/DELETE/TRUNCATE or table/column drop appears in this set; the default/trigger and constraint changes above still have real behavioral effects. Foreign keys, checks, unique indexes and immutable triggers must not be disabled to make application succeed. No hard-coded provider/customer data is introduced by these files.

## Execution prerequisites — explicit pass/fail, not new scope

1. **Target and authority:** privately pin existing staging database secret version2 to the previously confirmed Neon host/neondb/public. Record provider project/branch/endpoint identity and PostgreSQL major version; a hostname alone does not establish isolation from all other consumers. Use an approved migration-capable connection; do not derive a direct endpoint by editing a pooler hostname or create credentials. Confirm no production consumer shares the target.
2. **Recovery:** identify an existing usable recovery point and authorized restore method. Record checkpoint/time, retention expiry, restore target, responsible operator and restore verification. No assumed Neon retention window or backup entitlement. Any cloud branch/backup creation, customer-data copy, storage charges or restore requires its own exact approval. Stop if recovery cannot be demonstrated.
3. **Upgrade rehearsal:** local disposable PostgreSQL only, synthetic rows only. Apply the 13 already-recorded migrations first, seed representative old-schema consent/property rows, then execute the pending 13 with the pinned Prisma7.10 toolchain. Compare row values and tested read/write behavior before/after; verify revision default/increment, nullable locations, all FK/check/unique/trigger behaviors, migration checksums and idempotent second deploy. Rehearse failure/lock timeout and cleanup. Existing fresh-database browser tests are supporting evidence, **not** this old-state upgrade proof. No real database clone or new provider resource is needed for the synthetic rehearsal.
4. **Baseline and maintenance:** qualify the currently serving revision's use of SmsConsentRecord and PropertyAddress, and all consumers of the same database. Keep six safety flags false and controlled intake disabled. If writes cannot be safely quiesced under existing authority, propose the exact maintenance action for approval; do not move traffic or stop services by inference.
5. **Fresh metadata gate:** immediately before execution, verify exact same 13 missing names, matching prior checksums, zero unfinished rows, expected object absence and target/schema. Stop on any drift, partial object, new migration, unknown consumer or active conflict. Review aggregate relation sizes/locks only with approved metadata access; no customer rows needed for this gate.

## Proposed execution procedure — NOT authorized to run yet

- Export only the reviewed migration/schema/config/lock inputs, with a SHA-256 manifest. Preserve their checksums. Pin installed Prisma7.10; do not use @latest, Prisma8 workflow, migrate dev, db push or reset.
- Run the existing `prisma migrate deploy` through an isolated one-shot process, not app startup. Inject the connection privately into that child process; no shell history/command-line credentials, connection logs or committed env files. Rehearsal must demonstrate how session lock/statement timeouts reach every migration connection; an operator-side SET on a different connection is insufficient.
- Proposed safety limits: lock_timeout5s, statement_timeout60s, one executor, overall operator deadline10min. Validate these against rehearsal/metadata before execution approval. No automatic timeout increase/retry or backend termination of another session. These limits bound waits, not guarantee all-or-nothing rollback.
- Record completed/failed migration names and sanitized status. Do not assume one atomic transaction across all files: source files do not declare an encompassing transaction and runner behavior must be rehearsed. A failure may leave partial DDL/history; stop immediately, preserve evidence, keep intake closed.
- Exit only after all26 successful records/checksums, zero pending/failed entries, catalog comparison of models/columns/types/nullability/indexes/FKs/checks/triggers/functions and unchanged baseline health. New consent revision and nullable-location acceptance must be proven synthetically, not by creating real customer rows. No job/payment/booking/provider test here.

## Recovery / rollback

An application rollback is **not** a database rollback. Do not drop new tables, remove consent evidence, set NOT NULL blindly, reset history, or run migrate resolve merely to make status green. In a partial migration, identify exactly which statements committed and reconcile under a separate reviewed repair/restore decision. Existing state and immutable evidence take precedence over rerun convenience. Restoring a shared target can discard writes after the recovery point; scope and maintenance must be approved first. If data/schema are safe but only candidate code fails, leaving expanded schema in place while keeping the existing app/intake disabled may be safer than reversing DDL; verify baseline compatibility rather than assuming it.

## Approval request after preparation passes

One explicit owner approval must name: exact staging project/branch/database/schema, SQL manifest/source, executable runner/version/timeouts, verified recovery point/owner, maintenance window/consumer isolation, expected costs and one-attempt stop conditions. It authorizes only those13 migrations on that staging target. Release of the image and the paid connected test stay separate. **Not ready to request migration execution today:** upgrade rehearsal and recovery/target qualification have not been performed in this planning turn.

## Evidence and checks

Read-only baseline: backend evidence/APP-013/p06-staging-schema-readonly.md (13/26 recorded;14 missing tables;1 missing column; no checksum mismatch). Built image record remains valid; no rebuild required for this plan. This planning turn reads source and changes docs only: architecture, governance frozen/full consistency,21 regressions and whitespace checks; no new runtime/rehearsal claim.

The [Prisma7 migration workflow](https://github.com/prisma/web/blob/main/apps/docs/content/docs/orm/v7/prisma-migrate/workflows/development-and-production.mdx) documents that migrate deploy is not a drift detector; use explicit catalog checks. [PostgreSQL ALTER TABLE](https://www.postgresql.org/docs/current/sql-altertable.html) documents lock behavior and nullability constraints; validate against the actual server major version before execution. No provider backup capability is assumed from generic documentation.

Next observable result: one synthetic old-schema-to-new-schema rehearsal report plus qualified recovery/target inputs, then exact staging execution approval. Same two fixed P06 items remain; accepted5/60 (8.3%), walkthrough3/8 (37.5%); provisional4–8 weeks plus external waits, low confidence, unchanged. No scope deviation.
