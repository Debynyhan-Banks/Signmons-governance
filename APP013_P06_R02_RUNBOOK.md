# R02 private handoff and one-shot backup — live approval still required

## Current state

Local private-administrator adapter and v2 backup binding exist and are locally qualified. See APP013_P06_R02_PRIVATE_ADMIN_PROCEDURE.md and backend p06-r02-private-admin-local.md. Actual Neon logging/administrator authority, existing-password private retrieval, TLS handoff and backup/restore remain unexecuted. Local results are not live approval or recovery evidence.

The first window2026-09-15T12:22–12:42UTC was cancelled before credential handoff. The two roles already exist and were last verifiedNOLOGIN; do NOT rerun CREATE ROLE. Preserve encrypted v1 approval/closeout records through2026-09-22T12:22:00Z; no v1 adoption, deletion or automatic retry. v2 changes are implemented in source only; no v2 directory or live packet exists.

## Before asking for the next live window

Read-only, no passwords: refresh exact child/project/endpoint, PostgreSQL18,13migration checksums,26tables/two schemas, both roles/administrator ADMIN OPTION, consumers/sessions, quota and storage evidence. Read the exact LOGGING_SQL and extension-name/version query from scripts/p06-private-role-password.mjs. Evaluate assertLogging against those values; compute loggingFingerprint over exact ordered arrays only after reviewing effective settings and provider handling. Do not call runAdmin or obtain administrator input for this metadata work.

Unsafe/hidden/unknown settings, audit/utility logging or unresolved provider handling mean stop. No global/session logging modifications, added permissions, new roles, replacing Neon or repeat synthetic backup by inference. Fingerprint is a change detector; providerLoggingReviewApproved is an owner/operator attestation, not proof of absent internal logging. Document review source/scope/limitations rather than inventing an approval ID/hash.

## Fresh future packet (not filled here)

Only fixed project soft-smoke-54063480, child br-sparkling-sun-ay6gr5e8, host ep-jolly-flower-ayc6w9hv.c-5.us-east-2.aws.neon.tech, database neondb, role p06_migration_runner. Owner Debynyhan Banks; unique approvalId beginning P06-R02-; exact reviewed clean sourceRevision40hex; runDirectory /Volumes/Signmons-P06/r02-backup-v2; retentionDays7; administratorCloseoutAcknowledged true; noOtherConsumersConfirmed true.

Require canonical millisecond UTC startUtc/endUtc/verifiedAtUtc, maximum20minute window, current verification<=5minutes at each entry, remainingCUh>=1 and remainingTransferBytes>=134217728 from fresh account readback. Usage telemetry may lag, not a hard billing cap. Add explicit administratorPasswordAssignmentApproved and inheritedCredentialRiskAcknowledged, plus providerLoggingReviewApproved, providerLoggingReviewId and loggingFingerprint from the actual reviewed logging qualification. Never set these true merely to get past a refusal.

Separate owner approval must name administrator credential use only at this child, one runner password assignment whileNOLOGIN, later LOGIN with exact expiry, one backup/restore and mandatory closeout. Administrator credential itself may work on parent/siblings; fixed destination does not make it child-scoped. No inherited password reset, source ownership transfer, grants, migration, deployment, new cloud resource or paid plan.

After approval, mount the existing verified image/UUID with ownership; enforce exclusion/free space, exclusively create new current-owner0700 v2 directory and private0600 approval.json. Existing directory/attempt is a stop, not permission to reuse/delete it. No password in JSON.

## Owner-assisted private handoff

Automation stops all screenshot/DOM/accessibility/clipboard capture before the owner reveals the existing child's administrator password. Owner closes the secret display before automation resumes. No reset, SQL Editor password, chat input or captured agent PTY. If existing retrieval is unavailable, stop rather than improvise. Do not launch the60second input prompt until owner is ready.

From the clean reviewed backend checkout, in the owner's private terminal:

```sh
python3 -B scripts/p06_private_input.py --administrator
```

The fixed child process validates packet/storage/exclusive handoff marker before prompting. Only anonymous-pipe input; administrator secret remains in process memory, never a file/environment/argument or backup process. <=120second handoff inside the same absolute20minute window. No elevated-role/password reset fallback.

Helper checks logging/authority/identity, writes generated runner-only0600 scoped passfile and makes one runner password/expiry assignment preservingNOLOGIN. Administrator closes before handoff.json records ASSIGNED_NOLOGIN. Success intentionally retains mounted runner passfile for the immediately following approved backup stage; it is not full closeout. Failure may be indeterminate; no automatic resubmission. handoff-attempt.json persists.

## One backup, only after handoff and LOGIN readback

Using existing authorized child administrator Console, enable runner LOGIN with VALID UNTIL exactly the approved endUtc and read back restricted flags/expiry. Do not renew the20minute window or use expired metadata. The non-secret LOGIN statement is separate from password handling.

```sh
node scripts/p06-backup-once.mjs /Volumes/Signmons-P06/r02-backup-v2/approval.json
```

No alternate host/path/admin password/retry flag. Backup requires matched handoff receipt, then uses runner credential only: fixed TLS source, remaining budget, one snapshot/custom dump, one local private PG18 restore, exact13history and26table/two-schema catalog/row comparisons. No source business write or migration. Existing limits64MiBarchive/768MiBmonitoredworkspace retained; scan guard is not a disk quota.

## Mandatory whole-window closeout on success, failure or owner abort

The administrator stage never grants LOGIN. After any later LOGIN, independently commit this non-secret statement in the exact child Console:

```sql
ALTER ROLE p06_migration_runner NOLOGIN;
```

Then terminate only this runner's sessions and verifyNOLOGIN/zero; never touch other users:

```sql
SELECT pg_terminate_backend(pid)
FROM pg_stat_activity
WHERE usename='p06_migration_runner' AND datname='neondb' AND pid<>pg_backend_pid();
SELECT rolname,rolcanlogin,rolvaliduntil FROM pg_roles WHERE rolname='p06_migration_runner';
SELECT count(*) FROM pg_stat_activity WHERE usename='p06_migration_runner' AND datname='neondb';
```

Verify owned local PG server stopped, scoped passfile removed and exact image ejected/mount absent. Backend backup cleanup performs these local actions after an owned attempt; returned localCleanup PASSED does not establish administrator revocation. result.json has localCleanup PENDING before ejection. Handoff failure attempts its own connection/file/image cleanup but can fail; a preflight refusal before ownership, or owner abort after successful handoff and before backup, requires explicit operator cleanup. Do not label these closed merely from expiry or a generic refusal. Retain non-secret failure/attempt evidence; never reset markers to retry. No forensic-memory/host-compromise/provider-log guarantees.

Seven-day retention applies to encrypted archive/local restored data/logs and non-secret run records, from dump completion or approved start for partial records. Administrator secret has no intentional persistence; runner file removed at closeout, not retained7days. Destructive deletion/extension needs separate owner approval; no automation created.

## Acceptance and review

Review private input/adapter/v2 receipt diff and local evidence. Next is read-only live metadata/logging qualification, then fresh specifically approved execution if requirements pass. Actual recovery plus remaining migration-access boundary must pass before R02 acceptance; R03/R04 remain separate. R02 still has two acceptance areas; R01closed,R02-R12open11,added0; accepted5/60 and3/8 unchanged; ETAunvalidated. Approved mechanism amendment implemented locally only; no additional scope deviation.
