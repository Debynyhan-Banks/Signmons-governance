# P06-R02 consolidated closeout review

## Latest: real recovery area technically demonstrated — 2026-09-15

Owner-approved admin-v2 backup from20a3110 restored locally with26tables/633rows/fullcatalog/13migration-history comparison passing. Encrypted archive checksum independently matched; retention through2026-09-22T14:01:19.919Z. Automatic wrapper did not report cleanup success; manual closeout verified password file absent, local server/helpers stopped, source backup sessions0, both migration rolesNOLOGIN and exact image ejected. Read backend p06-r02-admin-v2-retry.md; historical missing-recovery assertions below are superseded.

Do not repeat this backup as a new section while valid. R02's other acceptance area remains migration-capable access and consumer boundary; no migration/ownership/role change authorized or performed by the backup exception. Existing admin credential was used only for this supervised read-only backup, not silently adopted for future migration. Owner review of the recovery evidence next; R02 and package percentages do not auto-close. Two areas unchanged, no added scope.

## Update: local preparation approved and completed

Owner reviewed and said "i reviewed proceed". APP013_P06_R02_LOCAL_CARD.md bounds this execution; backend p06-r02-local-qualification.md records actual passing local role/restore tests and cleanup. APP013_P06_R02_EXTERNAL_PACKET.md consolidates exact metadata queries and remaining external approval fields. No Neon change or actual backup performed. Proposal wording below is historical; do not repeat completed local qualification without evidence invalidating it.

## Authority and outcome — 2026-09-15

Owner approved a consolidated review after R02 took too long. This is documentation only, not approval for credentials, export, migration or deployment. Entry backend43fce7f/governance301779a; focused remotes fetched, worktrees clean. Existing runtime source53037fb remains unchanged. No scope deviation; frozen twelve-task inventory unchanged.

R02 has TWO unresolved acceptance areas, not a promise of two turns: (1) isolated migration access and consumer boundary; (2) usable pre-migration recovery. Supporting local work is grouped below, not added P06 tasks. R02 remains blocked, not complete.

## Why it ran long

The earlier child-branch six-hour recovery recommendation was incorrect and required replacement. Subsequent work split synthetic backup, encrypted storage and backup exclusion into many small approval turns. Current ticket/baseline headings also lagged behind newer accepted progress. These are planning/reporting faults, not new customer features. Preserve completed evidence; do not repeat the recovery-method choice or container creation.

## Completed evidence versus missing proof

| Requirement | Existing evidence | Exact missing result |
| --- | --- | --- |
| Target/version | Child br-sparkling-sun-ay6gr5e8 in soft-smoke-54063480; direct ep-jolly-flower-ayc6w9hv.c-5.us-east-2.aws.neon.tech, neondb, PG18; fixed0.25CU | Fresh identity/schema/size/activity and consumer readback before action |
| Migration feasibility | PG18 synthetic old13-to26 migration, no-op, constraint and lock-failure tests passed | Privilege test using the proposed migration role, not local administrator |
| Credential isolation | Endpoint isolated; only inherited neondb_owner observed | Exact child-only role/ownership SQL, secure delivery, expiry/revocation and successful authorized connection; no parent password reset or shared secret replacement |
| Backup tooling | Synthetic full custom archive/restoration, rows/history/catalog/ACL comparison and corrupt-archive rollback passed | Managed-role/extension mapping and real child backup restored successfully |
| Private workspace | AES256 outer container; owner reopen/checksum; future Time Machine exclusion verified | Synthetic database archive AND restore cluster inside mounted container; mounted access/key procedure and capacity qualification |
| Recovery policy | Private logical-backup preparation selected; no child self-PITR reliance | Actual archive checksum, checkpoint, successful restore comparisons, UTC expiry, owner and exact recovery procedure |

Evidence: backend p06-pg18-rehearsal.md, p06-synthetic-backup-restore.md, p06-encrypted-container-check.md, p06-r02-credential-recovery-qualification.md and p06-r02-recovery-policy-correction.md. These are prior observations, not fresh provider readbacks in this audit.

## One consolidated preparation packet — proposed next execution

Complete all preparation together and return one result, not an approval request for every command:

- Reuse scripts/verify-p06-migration-upgrade.mjs and PG18.6. Demonstrate exact required ownership/ALTER/REFERENCES/history privileges with fictional data; granting table privileges alone cannot authorize ALTER. Do not conceal inherited neon_superuser privileges behind a least-privilege claim. Record unresolved managed-provider differences.
- Use existing encrypted image, with owner private unlock if needed. Place the synthetic archive, restore data directory, database logs and temporary files inside it; private socket/access, no TCP; compare restored fixture/history/security metadata, stop database and lock image. No real data or credentials.
- Assemble exact metadata-only source queries and child-only credential changes, source/destination identities, role mapping, expiry/revocation, maintenance and stop conditions. No role creation or metadata SQL connection under this documentation approval.
- Reconcile storage sizing: actual volume capacity1,999,982,592bytes is less than2GiB. The old2GiB total proposal is not executable. Measure free space and estimated full archive plus expanded restore, logs and headroom. Reject insufficient capacity; do not resize or omit data without approval.
- Produce a single reviewed external-action packet covering required credential setup, metadata checks and ONE child-only backup/private restore validation. Include exact secure credential delivery, timeout, quota/cost bounds and retention dates. Unknown SQL/size/cost fields mean NOT ready for approval.

The local qualification above is a proposed next card, not performed or authorized by this audit. It introduces no new feature or P06 task. If it exposes a new subsystem or incompatible role requirement, stop with a visible change proposal instead of silently expanding R02.

## External approval envelope — cannot execute yet

Source only the named child; never parent/shared staging. Owner Debynyhan; executor Codex in an approved absolute UTC window. No password values in chat, repository, command arguments or logs. Only reviewed child-local credential/privilege changes; no blanket IAM/secret authority.

Then one full logical export and one isolated private restore, verified for migration history, data and required security/extension behavior without publishing customer rows. Proposed seven-day retention must become an absolute UTC deadline at execution; unresolved failure requires explicit extension before deletion. Check quota/headroom immediately before starting. Stop on target drift, unexpected writers, insufficient storage, privilege mismatch, timeout or failed comparison. No automatic retry, live restore, cutover or migration.

## R02 completion test

R02 may pass only when the exact connection/consumer boundary is verified AND a current usable recovery checkpoint has actual successful restore evidence, owner, expiry and recovery method. If source state changes or the checkpoint expires before migration, R03/R04 must reject stale evidence. Document necessary maintenance; do not disable parent consumers merely because they exist.

This leads to original R03 migration approval, then R04 one authorized migration. It does not authorize either.

## Explicitly NOT additional R02 blockers

- Runtime injection/key provisioning belongs to R05/R08; release approval/deployment to R07/R09.
- Provider rates, participant readiness and connected run belong to R06/R10/R11; closeout R12.
- Production backup automation, HA, new root projects or paid snapshots are not this staging safeguard.
- Searching/deleting historical Time Machine copies is not a new requirement: only synthetic content has entered this image. Future exclusion is already verified. Qualify the actual real-data storage boundary without claiming universal forensic proof that no copies or swap can exist.
- No repeat of completed R01, image build or container setup unless concrete evidence invalidates it.

## Review and tracking

Review this card against unchanged R02/R03 rows and private backup packet. Accept or amend the consolidated local preparation boundary; real export remains a separate exact approval, followed by existing R03. No repeated micro-approvals for routine commands inside an approved card.

R01 closed; R02-R12 open11; added0. Packages accepted5/60 (8.3% of tracked plan), walkthrough3/8 (37.5%); neither is total MVP completion. No validated ETA or promise that two acceptance areas mean two sections/days.
