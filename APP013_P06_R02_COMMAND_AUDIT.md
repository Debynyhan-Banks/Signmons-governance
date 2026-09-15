# R02 execution-command audit and fixed wiring proposal

Implementation result: the approved three-item wiring scope is implemented; same-core local26-table proof and20 Node/4private-input tests passed. See backend p06-r02-once-result.md and APP013_P06_R02_RUNBOOK.md. Live adapter/actual handoff/export unexecuted; no acceptance increase. Historical audit below explains why this wiring was required.

## Approved implementation card — before code

Owner explicitly reviewed/approved and said proceed. Entry backend d4dad75/governance27c8b11; fetched/clean, frozen/full consistency passed. Implement the three finite wiring items below in scripts/p06-backup-once.mjs and scripts/p06-backup-once.test.mjs; reuse existing guard module/private-input helper and extend existing local migration rehearsal only to exercise the same new backup core. No new dependency or source migration.

Interface: fixed-target CLI takes only a private approval packet path; validates packet/revision/UTC/quotas, exact mounted-image identity/ownership/private passfile before network. Shared core accepts connected clients/command callbacks for disposable local testing; CLI offers no alternate-host or fixture mode. Source SQL read-only, one exported snapshot, full26-table/history/two-schema catalog comparison, one archive/local restore. Dedicated local cluster under run directory; preserve private restore/archive together for seven-day approved retention. All diagnostics fixed codes/counts. Persistent exclusive attempt marker forbids rerun after success/failure. Live privileges/role-expiry and administrator revocation remain external approval/console actions; no inherited administrator password.

Test commands: node --test scripts/p06-backup-once.test.mjs scripts/p06-backup-guards.test.mjs; python3 -B scripts/test_p06_private_input.py; existing P06_MANAGED_REHEARSAL/ROLE/BACKUP with new private PG18 socket for actual same-core dump/restore/catalog/row and refusal tests. Cover invalid packet/window/target/storage before connect, exclusive marker, synthetic success/drift/row mismatch/cleanup failures; inherited guard limits and signal cases retained. Run npm lint/build/architecture, touched-JS syntax/Prettier, full governance/frozen/21 regression and whitespace. No UI change: browser QA not applicable; no live backend/credential/backup action.

Observable finish is a checked-in guarded invocation with same-core local proof plus explicit remaining live gates, not a live recovery claim. Rollback is tooling revert; no external change. Cleanup tests must not drop unowned resources. Larger design change means stop before implementation; no additional R02 task or ETA promise.

2026-09-15; owner proceeded with finalizing the exact execution packet. Entry backend eaebc04/governance02e197a; remotes fetched, worktrees clean, frozen/full consistency passed. No cloud or mounted-image action. APP-013/2B and P06-R02 unchanged.

## Result: packet cannot yet be represented as executable

scripts/p06_backup_guards.mjs exports tested primitives only, explicitly no CLI/target/activation. Its only checked-in caller, scripts/verify-p06-migration-upgrade.mjs, creates databases, seeds rows, updates rows to simulate concurrency/mismatch, and runs migrations. Never substitute a Neon URL into this caller. The mounted private-input check proves storage behavior, not an integrated source-to-private-restore execution command.

This is the previously disclosed real-invocation binding gap, not a newly discovered product requirement. Earlier next-step wording under-described the implementation work as filling a packet. No complete command, live recovery result or execution-ready status claimed.

## Proposed finite implementation inside existing R02

Use a single source-specific one-shot entry point and its local integration tests, reusing BackupBudget, compareTables, sameMetadata, p06_private_input.py and the existing managed-role local restore setup. Do not create a general backup scheduler/framework, provision another service, replace Neon, add dependencies, change migrations or move the frozen finish line.

1. **Bind the invocation and preflight.** Proposed files scripts/p06-backup-once.mjs and scripts/p06-backup-once.test.mjs (not implemented by this audit). Require named approval/window input, exact project/child/direct-host/database/runner, current13 migration checksums and two-schema26-table inventory; no parent/shared URL or inherited administrator password. Verify exact encrypted image UUID, ownership enabled, private run directory/passfile, fresh storage bounds. Fail before any network connection on missing/mismatched/expired input. One exclusive attempt marker prevents automatic rerun. Accepting command-line values is not proof of owner authorization: executor must bind the reviewed packet and source revision.
2. **Wire the existing one-shot path.** Start one remaining-window budget, read-only source connection using the scoped encrypted passfile and certificate/hostname verification, export one source snapshot, one full custom dump, one private local restore, full table/history/catalog/security comparison, sanitized result. Explicitly include both schemas in constraints/index/type/owner comparisons, not just public. Prepare only local NOLOGIN role stand-ins and extension ownership. No fixture generation/source write/migration in the real entry point. Keep source snapshot alive until comparison completes; no retry or new budget per phase.
3. **Prove shutdown and refusal together.** Reuse disposable fictional PG fixtures to call this same entry-point core, not another substitute demo. Test success, preflight rejection before connect, wrong/expired identity/window, duplicate invocation, limit/cancellation/failure at each I/O boundary, source drift/concurrent updates, mismatch/partial archive and cleanup. Report only counts/status/codes. Source query privileges remain read-only; administrator-only runner NOLOGIN/session termination is a separately specified console closeout action, never silently performed with parent credentials. Stop local server, remove only owned passfile and eject exact image; record failure if any cleanup cannot complete. Preserve encrypted archive for approved seven-day retention, not a public/temp copy.

This is a wiring proposal, not authorization for a larger subsystem. Complete the source-specific implementation card before code; resolve any substantial deviation with owner first. The existing helpers and tests are retained, not repeated as new acceptance. No promise of one turn or a date.

## Exact resources already fixed; do not re-ask

Project soft-smoke-54063480; child br-sparkling-sun-ay6gr5e8; direct ep-jolly-flower-ayc6w9hv.c-5.us-east-2.aws.neon.tech; database neondb; proposed runner p06_migration_runner; proposed owner p06_migration_owner. Existing encrypted image UUID A0020084-32EC-412A-B96B-1AA68A2CE61F. Proposed private run directory /Volumes/Signmons-P06/r02-backup-v1. Defaults maximum20minutes,64MiB archive,768MiB monitored workspace; no claim of hard disk/billing quota.

Owner already accepted private new-role password participation. Do not ask that willingness question again. Before live approval, document exact role creation/read-only grants, conditional Console reset/handoff route, LOGIN expiry and administrator closeout SQL. If the new role lacks the expected UI route, stop; no substitute parent password. Actual role creation/reset/export still require explicit approval.

Absolute UTC start/end, live quotas and retention expiry cannot truthfully be filled as current execution facts during this unimplemented audit. Bind them at the reviewed run; an expired window must refuse, not be silently shifted.

## Validation and reporting

This audit changes documentation only. Full governance consistency/frozen checks,21 regression tests, backend architecture/governance baseline and whitespace checks required. No runtime test/build/browser/backup rerun claimed.

R02 remains open; R01 closed; R02-R12 open11, added0; accepted5/60 and3/8 unchanged; ETA unvalidated. No scope deviation implemented. The owner-facing blocker is missing source-specific execution wiring, owned by the implementer, not another Google/Neon support wait or a customer-input problem. Do not request real credential/export authority until that wiring is tested.
