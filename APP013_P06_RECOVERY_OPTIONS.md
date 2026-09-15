# P06-R02 recovery options — owner review, not execution authority

## Decision and fixed boundary

Owner authorized this comparison after the unsupported child-PITR assumption was corrected. Recommendation: retain p06-isolated-staging-v1 / br-sparkling-sun-ay6gr5e8 in soft-smoke-54063480 and qualify a private logical backup for the staging migration. This is an engineering recommendation, not a tested recovery capability or authorization to export data. R01 closed, R02-R12 open (11), added0. Accepted5/60 (8.3%), walkthrough3/8 (37.5%), ETA unvalidated.

## Comparison

| Question | Recoverable root target | Private logical backup of existing child |
| --- | --- | --- |
| Existing target | Requires a new root and rebinding later migration/release packets; never reuse or overwrite serving production root | Retains current child, endpoint and existing13 migration history |
| Documented construction | New project root, or schema-only root in current project. No verified in-place child-detach path found in reviewed docs | PostgreSQL18 pg_dump custom archive over verified unpooled connection; pg_restore to separately approved empty destination |
| Data preparation | Schema-only root has no row data or migration-history rows; requires carefully reconciled import/bootstrap. New project likewise requires import. Not an automatic full-data clone | Full database archive includes schema/data/history, but not cluster roles; privilege/role mapping needs separate evidence |
| Recovery | Root-only own-history PITR, moving six-hour window on Free; restore overwrites all branch databases and can create a backup branch | Restore exact saved database state, independent of Neon six-hour expiry, while archive/key remain usable; not continuous recovery |
| Privacy | Import still requires private data-transfer handling; root/credential separation not automatic for schema-only route | Archive and restored copy contain inherited private data; explicit export/storage/access/retention authorization required |
| Cost | Free quotas may cover resources, but root/data copies and automatic restore backups consume quota; snapshots separately priced | No Neon snapshot fee if no snapshot used; dump consumes compute/egress, restore consumes local or approved target resources/storage |
| Effort/risk | More target changes, bootstrap/import and credential/recovery checks; no reliable turn/time estimate | Fewer target changes, but encrypted artifact lifecycle, role mapping and restore proof remain required |

Free pricing currently lists100CU-hours/project,0.5GB/project,5GB transfer and10 branches; root allowance3/project. Usage was NOT refreshed in console in this comparison. Do not infer archive size from the earlier35MB physical storage or promise zero cost. Snapshot count1 is not a free-storage allowance: published snapshot storage USD0.09/GB-month. Free quota exhaustion can suspend compute; no upgrade authorized. Costs and headroom must be checked before any execution.

## Recommended bounded qualification, if approved

1. Reuse installed PostgreSQL18 and existing synthetic migration fixture. Prove full dump -> empty disposable restore -> existing13 history/catalog/row invariants before any real export. Ordinary dump excludes global roles; no pg_dumpall or password-hash export. Define explicit owner/ACL mapping and audit security-definer functions/extensions. Do not suppress restore errors or call --no-owner/--no-acl equivalent to security preservation.
2. Prepare exact real-data approval: source child endpoint/neondb, authorized read credential, local encrypted non-synced destination, key holder Debynyhan, access restricted to owner/executor, size/compute/egress limits and fixed retention deadline. No Desktop/Downloads/repository/cloud-sync/LaCie destination assumed. Custom archive compression is NOT encryption. Directory permissions alone are NOT encryption. Storage/key mechanism must be verified before data leaves Neon.
3. Under separate approval only: quiesce child writers, make one full consistent archive, verify success/checksum/private permissions, restore once to an approved empty isolated destination and verify matching history/schema, aggregates and selected invariants without displaying private rows. A readable archive/listing is not restore proof. Preserve a consistent source checkpoint and prohibit intervening writes before migration; recapture needs approval if drift occurs.
4. Only then complete R02/R03 with exact archive identity, credential-role plan, restore target/method, Debynyhan restore authority, Codex executor and retention/reconciliation owner. A failed migration does NOT authorize restore/retry. Recovery must preserve failure evidence and account for all post-backup writes; never erase accepted jobs/audits/holds.

No generic backup platform, production backup strategy, automatic schedule, paid snapshot, target deletion or application feature is included. Local restore of copied data still requires authorization. For actual recovery, prefer a separately approved empty destination and validation before cutover: pg_restore --clean alone is not proof that post-backup objects absent from the archive are removed. No destructive recovery command is approved here.

## Root alternative and stop conditions

Choose root if the owner prioritizes provider-native PITR and keeping backup storage managed by Neon over minimal setup changes. Qualify an exact new target/import and costs first; preserve the original parent/child. Do not treat changing the default designation as making a child a root. No root-only capability inferred from the generic branch page. If private data export/storage is unacceptable, stop and revisit the root alternative rather than silently downloading.

## Sources and validation

Read2026-09-15: https://neon.com/docs/manage/branches (root types/counts); https://neon.com/docs/guides/branch-restore (root-only PITR); https://neon.com/pricing (limits/snapshot charges); https://neon.com/docs/import/migrate-from-postgres (unpooled connections, no pg_dumpall or --create); https://www.postgresql.org/docs/18/app-pgdump.html and https://www.postgresql.org/docs/18/app-pgrestore.html (archive/restore behavior).

Documentation research only; no live connection, export, new target, role, secret, restore or migration. Provider-directory CLI unavailable; used official documentation without installations. Frozen/full consistency,21 governance regressions, backend architecture and whitespace checks apply. Source entry backend354cd1b, governancecfb0c9d. Proposed recovery-method amendment only; no deviation implemented.
