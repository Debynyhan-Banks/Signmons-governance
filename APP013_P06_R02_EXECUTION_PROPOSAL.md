# R02 credential and backup proposal v1 — owner review, NOT execution-ready

## Latest safety implementation checkpoint

Owner-approved local safety tooling now passes per backend p06-r02-safety-result.md and APP013_P06_R02_SAFETY_CARD.md. Shared budget (up to20minutes), pre-write64MiB archive ceiling, monitored768MiB workspace, fixed diagnostics and bounded cursor comparisons are implemented and exercised in the existing26-table synthetic snapshot restore. Historical claims below that these helpers are unimplemented are superseded. Workspace monitor is stop-on-detection, not a disk quota; scans and event-loop latency permit overshoot.

No real-data executor invoked. Actual ownership-enabled encrypted mount/new-role handoff and filled UTC/resource/retention/cleanup packet remain gated. Bind the helper to the remaining absolute approved window and all private run roots before real use; do not run the synthetic fixture harness against Neon. No new prerequisite or task; R02 still requires approved real recovery proof.

## Current correction: full source inventory verified; NOT execution-ready

Read-only child catalog inspection2026-09-15 confirmed legacy_2025 owns three retained tables and three enums, all neondb_owner-owned with default ACLs, no RLS. Backend p06-r02-legacy-metadata.md records the full metadata evidence. The amended template now covers USAGE on both schemas and SELECT on all26tables. No live grant executed. Earlier public-only proposal superseded; never omit legacy data.

Private TTY, managed-metadata, aggregate-limit and sanitized cursor helper tests now pass. Ownership-enabled encrypted mount, actual new-role credential handoff and exact execution-window binding remain gated. This is still a proposal, not authorization.

## Historical stop correction: public-only backup grants were incomplete

Owner-approved local tooling now exists and passed its corrected tests; backend p06-r02-tooling-result.md records actual results. The initial restricted full dump failed: migration3 retains legacy_2025.Tenant/Job/CallLog, so23public tables are NOT the whole database. The template below is historical/incomplete and must not execute. No live grants changed. Verify all non-system source schemas (including legacy ownership/ACLs) before proposing the amended allowlist. Do not exclude legacy data to make pg_dump pass.

Private TTY helper and actual pseudo-terminal tests passed; managed metadata/26fictional-table snapshot restore passed, including extension-owner/default ACL preservation. The synthetic harness is not a real-data executor: aggregate storage/time enforcement and sanitized streaming comparisons remain unimplemented, and encrypted mount/live password handoff remain separate gates. No acceptance uplift. This exposes a missed prerequisite within R02, adds0tasks, and preserves the requirement for a full backup.

## Update: owner-assisted password method accepted

Owner answered yes to privately handling only the future new child role password. This settles the participation choice, not role creation/reset/export authority. Do not ask that choice again.

Read-only qualification2026-09-15: exact child Roles page still contains only neondb_owner; its action menu exposes Reset password and Delete role. Neither selected; menu dismissed. Never test this on inherited neondb_owner. Official [Manage roles](https://neon.com/docs/manage/roles#reset-a-password) documents Console Reset generating a password and displaying it in a subsequent modal; SQL-created roles avoid automatic neon_superuser membership. This supports a proposed UI route, not proof for a nonexistent NOLOGIN SQL-created runner.

Future approved handoff: verify exact new p06_migration_runner row/child, then pause all screenshots, accessibility/DOM reads, clipboard reads and terminal capture while owner handles the reset-result modal and private non-echoing input. Owner closes the password modal before automation resumes. Do not type a password into SQL Editor, persist it in query history or send it in chat. No custom password needed; use the generated value. Clipboard avoidance by private manual entry is preferred; if owner chooses copy/paste, disclose clipboard history/sync exposure and clear only that copied secret with owner authority, without inspecting clipboard contents.

Private input must terminate in the exact encrypted0600 passfile through a reviewed non-echoing local helper; no password-bearing process arguments/environment dumps. The helper and synthetic secret-capture tests now pass per backend p06-r02-tooling-result.md; actual encrypted live handoff remains untested. Reject until ownership-enabled mount/private directory and input disposal are tested. The generator route is documented; the full handoff is NOT yet demonstrated. If new role does not expose the action or the result would be captured, stop before mutation; do not substitute parent credentials or console-created administrator roles.

Next work remains the already identified local executor qualification, including dummy-secret handoff and managed metadata restore/comparison/limits together. No new P06 tasks, no live credentials and no scope deviation.

## Authority and fixed outcome

Owner requested packet preparation after verified metadata. Entry backend723d850/governance04df44d; both focused remotes fetched and clean. Documentation only. Existing R02 pass test remains isolated migration access plus usable current recovery proof. No tasks added or acceptance awarded. This proposal refines the existing credential/backup boundary; it does not authorize it.

Reuse backend p06-r02-source-metadata.md, p06-r02-local-qualification.md and scripts/verify-p06-migration-upgrade.mjs. Runtime source53037fb unchanged. Do not repeat completed source inventory or synthetic tests absent drift.

## Exact scope

- Only project soft-smoke-54063480, child br-sparkling-sun-ay6gr5e8, endpoint ep-jolly-flower-ayc6w9hv.c-5.us-east-2.aws.neon.tech, neondb/public, PostgreSQL18.
- Owner/key custodian Debynyhan; executor Codex under named approval. Never parent/shared DATABASE_URL, provider-managed roles, existing passwords, production or other products.
- Only proposed cloud identities: p06_migration_owner (NOLOGIN) and p06_migration_runner (initially NOLOGIN). Collision is a stop, never reuse or replace.
- Existing encrypted image /Users/debynyhanbanks/Library/Application Support/Signmons/P06/signmons-p06.dmg.sparsebundle; UUID A0020084-32EC-412A-B96B-1AA68A2CE61F. Proposed run directory /Volumes/Signmons-P06/r02-backup-v1, created only if absent. No /tmp real-data copy.
- No migration files applied, deployment, sends, customer contact, new cloud resources or plan change.

## Proposed sequence and gates

1. Before mutation, bind approved start/end as absolute UTC and read back unchanged target,13checksums, ownership and consumers. Record T0;20minute total active execution deadline, no automatic retry. Establish at least1GiB free inside the verified image and2GiB host free, source no larger than32MiB, at least1CUh and128MiB transfer allowance remaining. These are conservative admission limits, not predicted usage or enforced billing caps. Abort for stale/unknown quota. Fixed0.25CU and existing5minute scale-to-zero unchanged.
2. Unlock privately; mount with ownership enabled, verify0700 run directory and current-user ownership, private socket, no TCP. Do not claim Owners Disabled plus chmod proves multiuser protection. Confirm actual run mount options; refusal means stop, not broad sudo/global disk changes.
3. Create only the two named restricted roles in one child-console transaction, with no password literal, no managed-role membership and no ownership transfer. Grant runner CONNECT on neondb, USAGE public and legacy_2025 and SELECT on exactly the26 inventoried tables. No CREATE/schema ownership/write grants at this stage. Capture resulting ACL metadata and original metadata separately.
4. Set a unique password through a verified owner-assisted secure credential handoff; enable LOGIN with expiry T0+20minutes only after that handoff is qualified. Explicit issue below prevents executing this step today. Store any necessary PG passfile only within encrypted0700 directory,0600 file, scoped exact host/5432/neondb/runner, never wildcard; sslmode=verify-full. No parent credential or plaintext URL payload access.
5. One full custom pg_dump using PG18.6 through exact direct child, no-owner/ACL stripping prohibited. Before backup, require no other authorized child writers; capture consistent snapshot/checkpoint metadata. Archive path run/source.dump; logs/temp run-local. Statement/lock/process deadlines bound by remaining overall window. Stop if archive exceeds64MiB or run workspace exceeds768MiB; retain partial evidence, never truncate and call it a backup. One dump only.
6. Restore once into a new private no-TCP local cluster/database using UTF8/C.UTF-8, preserve archive ownership/ACL statements and compare actual source/restore privately. Matching locale names across macOS/Linux alone do not prove equal sort semantics: validate collation-sensitive index creation and ordering needed by schema; any mismatch fails qualification. Do not substitute C/SQL_ASCII silently.
7. Require exact13 successful history records/checksums,26table/37enum/two-schema catalog inventory, full row comparison for all tables, constraints/index definitions and explicit security metadata comparison. No customer values in repository/log output; emit counts/pass/fail/checksums only. Consistent source comparison must use the backup snapshot or proven stable source; a later moving source comparison is not adequate.
8. Only after backup passes may the reviewed ownership manifest become eligible for a separately bound child transaction. No broad REASSIGN OWNED. This transaction is NOT authorized by this document. Preserve neondb_owner's prior object access explicitly if ownership changes; rollback map restores original owners and exact ACLs. Runner stays disconnected until migration R03/R04 approval; revocation must account for new objects later created by runner.
9. On every outcome stop local server, revoke LOGIN and terminate only this newly created runner's sessions, remove private credential file, eject image and verify inaccessible. Do not terminate other sessions or drop roles with unexpected dependencies. Retain archive/evidence encrypted seven days from dump completion, record absolute UTC expiry; request extension before expiry if recovery/acceptance unresolved. No silent retention reset, historical Time Machine deletion or destructive live restore.

## Role creation template — proposal only

Executed as authorized child-console administrator after identity/collision gates. No password embedded. Exact SELECT allowlist below must match inspected inventory before execution.

```sql
BEGIN;
SET LOCAL lock_timeout='5s';
SET LOCAL statement_timeout='10s';
CREATE ROLE p06_migration_owner NOLOGIN NOSUPERUSER NOCREATEDB NOCREATEROLE NOREPLICATION NOBYPASSRLS;
CREATE ROLE p06_migration_runner NOLOGIN NOSUPERUSER NOCREATEDB NOCREATEROLE NOREPLICATION NOBYPASSRLS;
GRANT CONNECT ON DATABASE neondb TO p06_migration_runner;
GRANT USAGE ON SCHEMA public,legacy_2025 TO p06_migration_runner;
GRANT SELECT ON TABLE public."AuditLog",public."CommunicationContent",
public."CommunicationEvent",public."Conversation",public."ConversationJobLink",
public."Customer",public."CustomerCoverageCheck",public."Job",public."JobOffer",
public."LedgerEntry",public."Payment",public."PropertyAddress",public."RoutingRule",
public."ServiceArea",public."ServiceCategory",public."SmsConsentRecord",
public."StripeEvent",public."TenantOrganization",public."TenantSubscription",
public."User",public."UserAvailabilityBlock",public."UserServiceCapability",
public."_prisma_migrations",
legacy_2025."Tenant",legacy_2025."Job",legacy_2025."CallLog"
TO p06_migration_runner;
COMMIT;
```

This is a proposed staging order change from immediate owner-capable access: get a verified recovery archive before ALTER OWNER. No live change implemented. The two identities remain within the same proposed R02 role boundary; owner must review the order and its resulting backup ACLs.

## Security metadata restoration

The real source has cloud_admin-owned plpgsql and two cloud_admin/public default ACLs granting neon_superuser rights. pg_dump does not include roles. Never recreate a real provider administrator as a login or grant it host/cloud powers. An isolated local restore may need NOLOGIN metadata stand-ins for neondb_owner/cloud_admin/neon_superuser plus exact applicable memberships and ACLs. The purpose is to preserve and inspect database metadata, not emulate Neon's platform security.

The corrected local fixture tested managed-role mapping, extension ownership and a restricted read-only dump role across26fictional tables. It does not prove live provider parity or all cross-OS collation semantics. Preserve original catalog evidence and compare the restored database to the intended mapping; explicitly distinguish exact object/ACL preservation from provider-environment parity. If pg_restore does not restore extension owner, report the difference and qualify an explicit local-only correction before claiming success. No --no-owner/--no-acl shortcut. Actual recovery/cutover on Neon remains separately approved and cannot be inferred from a local restore.

## Readiness gaps — no blanket action approval requested

The inventory and proposed sequence are complete, but this is NOT an executable card yet:

- **Secure new-role password path:** must verify that the console can set/reset only the newly SQL-created role without retaining a password in SQL history, and that owner can deliver it privately to encrypted storage. Do not assume this UI capability. Alternative direct administrator psql would require separate authority to use an inherited credential, which is not selected.
- **Real invocation binding:** local managed-role restore, synchronized comparison and limit helpers are tested. Bind them to the qualified ownership-enabled encrypted mount, exact26-table allowlist and remaining approved UTC window with mandatory cleanup. Existing synthetic script creates and mutates fixtures: never run it on Neon.
- **Execution-time fields:** exact approved UTC window, retention deadline and fresh limits must be bound before changes. T0 formulas here are policy proposals, not filled execution records.

These are unresolved implementation details of existing R02 requirements, not new packages or claims of completed safeguards. No broad execution approval should be solicited while they remain. Do not silently build a new backup subsystem: reuse existing tooling, and stop for a material design deviation.

## Owner review and next concrete decision

Review the backup-before-ownership order, two-role boundary, no-parent-password rule,20minute/one-attempt limits and seven-day retention. The smallest choice is whether the owner accepts an assisted secure password handoff for only the new child role. Acceptance of that method permits planning/qualification, NOT role creation, password reset or export until its exact route and other card gaps pass.

No new product decisions, recovery-provider choice or repeat source inspection needed. Finish the outstanding qualification together, then present ONE filled execution card. R03 migration approval stays separate.

## Progress

R01 closed; R02-R12 open11; added0. Accepted packages5/60 and walkthrough3/8 unchanged, P06 unaccepted, ETA unvalidated. No scope deviation implemented. Sequence refinement above proposed for review before execution.
