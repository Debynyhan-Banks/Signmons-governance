# R02 one-shot command — review before live authorization

The owner approved implementation only. The command now exists; the real Neon adapter, actual new-role Console reset/handoff and real restore have NOT been executed. Local same-core evidence is backend p06-r02-once-result.md. Do not run this document as a script or infer live approval from code review.

## Fixed command

From the clean, owner-reviewed backend checkout at the packet's exact sourceRevision:

```sh
node scripts/p06-backup-once.mjs /Volumes/Signmons-P06/r02-backup-v1/approval.json
```

No alternate URL, parent-password argument, fixture flag or retry argument. No arguments/wrong path refuses. Never use verify-p06-migration-upgrade.mjs for real data.

## Before requesting the live window

1. Confirm owner explicitly authorizes the existing child-only two-role/read-only-grant proposal, one new-role reset/private handoff, one full private backup/restore and closeout. No ALTER OWNER, schema migration, application binding, deploy, extra cloud resource or paid plan. Owner participation already accepted; do not ask willingness again.
2. Refresh exact child target, no other consumers/sessions,13 original migration checksums,26tables/two schemas and quota/storage. A readback is not authorization. Stop if drift. Use fixed project/branch/host/role in APP013_P06_R02_EXECUTION_PROPOSAL.md.
3. Mount existing image, verify exact UUID/Owners Enabled/exclusion and available space. Exclusively create /Volumes/Signmons-P06/r02-backup-v1 as current owner0700; existing directory/attempt means stop and reconcile, not adopt or remove it. Create private0600 approval.json only after exact owner approval. No private input in that JSON.

## Approval packet fields (no live values filled here)

Required fixed values: owner Debynyhan Banks; approvalId matching P06-R02- plus a unique reviewed label; sourceRevision exact clean backend40-character SHA; project soft-smoke-54063480; branch br-sparkling-sun-ay6gr5e8; host ep-jolly-flower-ayc6w9hv.c-5.us-east-2.aws.neon.tech; database neondb; role p06_migration_runner; runDirectory /Volumes/Signmons-P06/r02-backup-v1; retentionDays7; administratorCloseoutAcknowledged true; noOtherConsumersConfirmed true.

Execution-bound fields: startUtc/endUtc/verifiedAtUtc canonical YYYY-MM-DDTHH:mm:ss.sssZ strings. End-start maximum20minutes; run must start within window; metadata/quota verification no older than5minutes. remainingCUh numeric >=1 and remainingTransferBytes numeric >=134217728 from fresh owner-account readback. These are operator attestations, not automated billing proof or cryptographic approval. Do not fill dummy values or silently extend an expired window. Absolute retention expiry is emitted from actual dump completion; partial-artifact retention is conservatively anchored to approved start.

## Conditional credential sequence inside that approval

Use only the existing reviewed exact26-table SQL allowlist/two-role template. Both roles start NOLOGIN, non-superuser, no createDB/createRole/replication/bypassRLS, no managed-role membership. Collision refuses. Keep original object ownership unchanged.

Verify newly created p06_migration_runner appears in the correct child. Owner handles its Console reset privately while all screen/clipboard capture is paused. If that new role lacks the expected action, stop and close out; never reset neondb_owner or switch to an administrator credential.

Owner enters only the generated new-role value into the existing non-echoing helper:

```sh
python3 -B scripts/p06_private_input.py
```

The helper writes the exact scoped0600 pgpass in the run directory. No password in SQL/history/chat/arguments. Then authorize LOGIN with VALID UNTIL equal to the packet's exact endUtc, using the child administrator console; read back all restricted flags and expiry. No sample expiry SQL is executable here. Budget starts from remaining approved window, including elapsed setup/handoff time; no fresh20minute grant.

## What the command does and does not do

Exclusive attempt.json prevents automatic second execution. Fixed TLS source connection, role-expiry/session checks, remaining-window budget, one snapshot/custom dump, local private PG18 cluster, NOLOGIN metadata stand-ins/extension-owner mapping, one transactional restore,13-history and complete two-schema catalog/row comparison. No source business-data writes; no fixture generation or migration in this command. Node TLS verifies certificates; libpq uses verify-full/system roots. Actual Neon certificate/role access remains to be demonstrated in the approved run.

Output is counts/status/hash/retention only. All archive, local restored data, local logs and packet remain in encrypted private run storage, subject to the same approved retention. Source values only exist in comparison memory and private database/archive. Workspace guard is scan-based, not a hard quota; standard PostgreSQL error/statement logging is suppressed. No forensic memory erasure or administrator isolation guarantee.

After an attempt, close clients, stop only this run's local server, remove only the same inode passfile and eject verified exact image. Cleanup has its own bounded shutdown allowance after work deadline. A cleanup failure returns CLEANUP_FAILED; do not label it closed or force-eject a running server. result.json records data comparison before ejection with localCleanup PENDING; only successful returned localCleanup PASSED establishes local closeout. Preserve evidence of failed/partial attempts; never reset attempt.json to retry.

## Mandatory administrator closeout, success OR failure

The script has no administrator password and explicitly reports administratorRevocation REQUIRED. After confirming the exact child and newly created role, execute as its authorized administrator:

```sql
ALTER ROLE p06_migration_runner NOLOGIN;
```

Commit that statement independently before attempting session termination, so a termination-permission error cannot roll back NOLOGIN. Then:

```sql
SELECT pg_terminate_backend(pid)
FROM pg_stat_activity
WHERE usename='p06_migration_runner'
  AND datname='neondb'
  AND pid<>pg_backend_pid();
SELECT rolname,rolcanlogin,rolvaliduntil
FROM pg_roles WHERE rolname='p06_migration_runner';
SELECT count(*) FROM pg_stat_activity
WHERE usename='p06_migration_runner' AND datname='neondb';
```

Require NOLOGIN and zero runner sessions, plus local server stopped/passfile absent/image ejected. If privileges fail, report the exact administrator action needed; do not terminate other users or borrow parent credentials. Password expiry alone does not terminate existing sessions. Preflight refusal before taking ownership of the passfile does not remove it: operator must close out the private helper file/image and any role provisioned earlier.

Retain encrypted run contents for the recorded seven-day expiry; separate owner authority is needed for destructive removal/extension. Do not claim R02 accepted from helper tests. After actual recovery proof and closeout, review the existing R02 access/consumer/recovery criterion; R03/R04 migration approval/execution remain separate.
