# P06 remaining-work reconciliation — review baseline v1

## Current: R02 recovery accepted — migration credential decision pending

Owner said "Great proceed" after the successful recovery evidence and manual closeout. Record recovery-area acceptance, not whole R02 acceptance. Read-only child inspection on 2026-09-15 confirmed neondb_owner can CREATE in public, owns all26tables and37enums, other sessions0 at query time, and both migration roles remainNOLOGIN. Cloud48revision and migration-job DATABASE_URL references remain signmons-staging-database-url:latest, no inline values; payloads not inspected, so reference checks are not exhaustive proof of consumer isolation. Encrypted image remains detached.

Proposed mechanism amendment, NOT approved or implemented: reuse the existing administrator privately for one supervised child-only migration instead of enabling a new runner/password and transferring ownership. This avoids the failed credential-provisioning route, but the inherited credential retains parent access; endpoint guards do not make it least-privileged. Owner must approve this exception before implementation. No password reset, privilege change, migration or backup repeat here. Details and finite next steps: APP013_P06_R02_CLOSEOUT_REVIEW.md (governance). Existing R03 execution-packet approval and R04 execution remain separate; live runner is not yet qualified.

R02 has one remaining acceptance area: migration connection and consumer boundary. No added task IDs or acceptance criteria; R01closed,R02-R12open11,added0; accepted5/60(8.3% tracked plan),walkthrough3/8(37.5%),ETAunvalidated. This is a proposed security-mechanism deviation only, not an adopted scope change.

## Historical: R02 real recovery demonstrated — manual closeout verified

Owner-approved admin-v2 attempt from backend20a3110 completed one real child backup/local restore:26tables/633rows matched,13migration checksums and catalog checked; archive198833bytes with independently matched SHA256. Dump2026-09-15T14:01:19.919Z, encrypted retention through2026-09-22T14:01:19.919Z. Wrapper reported refusal at final cleanup; retained result says PENDING, not auto-clean success. Independent checks found password file absent/local server stopped; read-only result review followed by manual exact-image detach succeeded, source backup sessions0, both migration rolesNOLOGIN. See backend evidence/APP-013/p06-r02-admin-v2-retry.md. No second export, password reset, source mutation, migration or release. Recovery-area technical evidence ready for owner acceptance; remaining R02 migration-access/consumer boundary separate. Do not repeat recovery proof without invalidating drift/expiry. R01closed,R02-R12open11,added0; accepted5/60 and3/8 unchanged; ETAunvalidated. No scope deviation.

## Historical: R02 stalled private-input cycle repaired — cancelled attempt preserved

Owner-approved local repair removes the backup CLI/password-helper circular import by sharing readPipe from the existing dependency-leaf guards module. Regression failed before fix and passes after; real PythonTTY-to-Node dummy transport/cancellation and bounded READY-line tests pass. Current33Node/10Python tests pass, prior opt-in database test skipped; no real credential/mount/export/retry. Admin-v1 live attempt cancelled with no pgpass/archive/result observed, helper processes stopped and image ejected; preserve approval/attempt/closeout records. See backend evidence/APP-013/p06-r02-private-prompt-repair.md and existing exception card. Next freshly authorized unused-path packet/private readiness, not support email or reuse of cancelled attempt. R02 still two acceptance areas; R01closed,R02-R12open11,added0; accepted5/60 and3/8 unchanged; ETAunvalidated. No scope deviation.

## Historical: R02 existing-administrator backup mode locally qualified

Owner approved one supervised backup using the existing administrator credential instead of provisioning/resetting a runner password. Explicit fixed-child mode implemented in the existing backup/input helpers; 32 Node and8 Python tests pass, one prior opt-in integration skipped. No real credential, mount, export or provider change. See APP013_P06_R02_EXISTING_ADMIN_EXCEPTION.md and backend evidence/APP-013/p06-r02-existing-admin-backup.md. Next owner private readiness, fresh bound execution packet and one backup/restore; no support-email dependency or password SQL. Temporary encrypted0600 administrator passfile is removed at closeout; inherited credential remains broadly privileged. R02 still two acceptance areas; recovery unproven and migration-access boundary remains separate. R01closed,R02-R12open11,added0; accepted5/60 and3/8 unchanged; ETAunvalidated. Approved credential-mechanism deviation only; no additional scope deviation.

## Historical: R02 private handoff locally qualified — live logging review pending

Owner-approved private handoff adapter and v2 backup receipt binding implemented and locally qualified. Seven Python tests and28Node regressions pass; actual private PG18 dummy-role password proof passed, objects removed and server stopped. No real credential/Neon connection/password/backup or image mount. See backend p06-r02-private-admin-local.md and APP013_P06_R02_PRIVATE_ADMIN_PROCEDURE.md. Next review code and READ-ONLY Neon logging/extension/administrator-authority qualification; provider review/fingerprint and fresh explicit live packet remain absent. Never weaken logging checks or reuse cancelledv1. R02 still has two acceptance areas; R01closed,R02-R12open11,added0; accepted5/60 and3/8 unchanged; ETAunvalidated. Approved credential-mechanism amendment implemented locally only; no additional scope deviation.

## Historical: R02 private administrator procedure prepared — not executed

Owner approved preparation only of a private child-administrator password-setting procedure after the Console runner handoff failed. APP013_P06_R02_PRIVATE_ADMIN_PROCEDURE.md records the proposed memory-only administrator exception, fixed child/runner, NOLOGIN preservation, logging qualification, fresh v2 packet/path, failure cleanup and finite local test card. No helper implemented, administrator credential retrieved, password changed, mount or new backup attempted. Existing roles last verified NOLOGIN; prior window remains cancelled. Next review/approve local implementation and qualification, not live execution. R02 still has two acceptance areas; R01closed,R02-R12open11,added0; accepted5/60 and3/8 unchanged; ETAunvalidated. No scope deviation implemented; credential-mechanism amendment proposed only.

## Historical: R02 live test stopped at Console credential handoff

Owner explicitly approved the live staging backup test. Exact child-only two-role/read-only grant transaction committed; both roles remain NOLOGIN with no administrative flags/memberships, and runner has SELECT on26tables with no table-write privileges. The new SQL-created roles do not appear in Neon Console Roles after revisiting, so the approved new-runner reset route could not be verified. Stopped before password reset/handoff, LOGIN, executor or export. Final both-role sessions0; no pgpass/attempt/archive/local cluster; exact encrypted image ejected. Window12:22–12:42UTC cancelled, no automatic reuse/retry. See backend evidence/APP-013/p06-r02-live-handoff-stop.md. Next resolve the demonstrated Console credential-route gap read-only, then review any changed action/packet; never use inherited neondb_owner credentials. R01 closed,R02-R12 open11,added0; accepted5/60 and3/8 unchanged; ETA unvalidated. No scope deviation.

## Historical: R02 one-shot wiring locally tested — live approval pending

Owner-approved fixed-target one-shot CLI implemented with existing guards, exclusive attempt marker, scoped private input, snapshot/full backup/restore/two-schema comparisons and explicit cleanup. Same core passed local restricted-reader26-table/20fictional-row restore;20 Node tests and4 private-input tests passed. See backend evidence/APP-013/p06-r02-once-result.md and APP013_P06_R02_RUNBOOK.md. No real Neon adapter/handoff/export executed; next review and freshly bound explicit live packet, including administrator revocation. Do not repeat standalone tests without drift or claim R02 accepted. R01 closed,R02-R12 open11,added0; accepted5/60 and3/8 unchanged; ETA unvalidated. No scope deviation.

## Historical: R02 command audit — real invocation wiring incomplete

Command audit confirms tested helpers have no real-backup entry point; their sole caller creates/mutates fictional databases and must not run against Neon. See APP013_P06_R02_COMMAND_AUDIT.md and backend evidence/APP-013/p06-r02-command-audit.md for fixed source-specific wiring proposal. Earlier packet-only wording understated implementation; no completed command/window invented. Next implementer outcome is tested preflight/snapshot/restore/cleanup wiring, then explicit real handoff/export approval. Storage proof retained; no external action. R01 closed,R02-R12 open11,added0; accepted5/60 and3/8 unchanged; ETA unvalidated. No scope deviation implemented.

## Historical: R02 ownership-enabled mounted input qualified

Owner-approved administrator ownership change succeeded for the exact Signmons-P06 UUID. Four existing private-input tests passed inside verified ownership-enabled encrypted image using dummy values; test directories removed, existing artifacts preserved, exact image ejected and mount absent. See backend evidence/APP-013/p06-r02-mounted-input.md and APP013_P06_R02_MOUNT_CHECK.md. Next bind tested tooling to exact real invocation/window/cleanup packet before specific new-role/handoff/export approval. No Neon action or real backup. R02 open; R01 closed,R02-R12 open11,added0; accepted5/60 and3/8 unchanged; ETA unvalidated. No scope deviation.

## Historical: R02 local backup limits and private comparison tested

Owner-approved safety code implemented in existing local backup rehearsal. Shared20minute budget, pre-write64MiB archive ceiling, monitored768MiB workspace and privacy-safe bounded cursor comparison passed;26tables/20fictional rows matched, concurrent snapshot and refusal tests passed. See backend evidence/APP-013/p06-r02-safety-result.md and APP013_P06_R02_SAFETY_CARD.md. No live credential/export or image change. Next existing R02 gate: ownership-enabled encrypted storage/actual private handoff qualification and filled execution packet, then separately approved real recovery proof. R01 closed; R02-R12 open11,added0; accepted5/60 and3/8 unchanged; ETA unvalidated. No scope deviation.

## Historical: R02 legacy metadata verified; proposal corrected

Read-only child catalog inspection on2026-09-15 confirmed public23tables/34enums plus legacy_2025 three tables/three enums:26tables,37enums total. Proposed backup allowlist now includes both schemas and exactly those26tables; no live grants, credentials or export. See backend evidence/APP-013/p06-r02-legacy-metadata.md. Next qualify aggregate20minute/storage limits and sanitized streaming comparisons for the real runner, then separately approve credential/backup execution. R02 remains open; R01 closed; R02-R12 open11, added0; accepted5/60 and3/8 unchanged; ETA unvalidated. No scope deviation implemented.

## Historical: R02 local tooling works — legacy-schema omission found

Owner-approved private input helper/PTTY tests and managed metadata full synthetic restore implemented. Initial restricted dump exposed omitted legacy_2025 privileges; corrected local proof compares26tables and passes. See backend p06-r02-tooling-result.md and APP013_P06_R02_TOOLING_CARD.md. Public-only live grant proposal blocked pending non-public schema inventory; no live grants/export. Synthetic harness is not real-data executor. R01 closed; R02-R12 open11, added0; accepted5/60 and3/8 unchanged; ETA unvalidated. Missed prerequisite disclosed within R02; no scope deviation implemented.

## Historical: handoff method accepted

Owner accepts privately handling the future new-role password. Console reset route documented and existing role action menu inspected without reset; no new role exists, so actual handoff is untested. See APP013_P06_R02_EXECUTION_PROPOSAL.md and backend p06-r02-execution-proposal.md. Next consolidate dummy-secret/private-input and managed restore/comparison/limit executor qualification; do not repeat willingness approval. No live credential/export actions. R01 closed; R02-R12 open11, added0; accepted5/60 and3/8 unchanged, ETA unvalidated. No scope deviation.

## Historical: execution proposal drafted

See APP013_P06_R02_EXECUTION_PROPOSAL.md and backend p06-r02-execution-proposal.md. Proposed backup-before-ownership order, exact23-table/two-role template, limits and cleanup documented. Not execution-ready: secure new-role credential handoff and concrete managed-role restore/comparison/limit enforcement remain unqualified; UTC window unbound. No external actions. R01 closed; R02-R12 open11, added0; accepted5/60 and3/8 unchanged; ETA unvalidated. Sequence refinement proposed for review; no scope deviation implemented.

## Historical: source metadata verified

Owner-authorized child metadata read completed: PG18.6,11,165,696bytes,13matching successful migration records,23tables/34enums and managed ACL inventory. Known tagged/job consumers and delayed quota metrics refreshed. See backend p06-r02-source-metadata.md and APP013_P06_R02_EXTERNAL_PACKET.md. Next finalize the one credential/private-backup execution proposal; no repeat metadata approval or external mutations. R01 closed; R02-R12 open11, added0; accepted5/60 and3/8 unchanged; ETA unvalidated. No scope deviation.

## Historical: consolidated local qualification

Owner reviewed and approved local preparation. Restricted-role migration/no-op, table-grant refusal and encrypted synthetic archive/restore passed; five fixture databases and two roles removed, PG stopped and image locked. See backend p06-r02-local-qualification.md, APP013_P06_R02_LOCAL_CARD.md and APP013_P06_R02_EXTERNAL_PACKET.md. Exact external packet remains non-executable pending authorized child metadata/consumer/quota inspection, actual role mapping and resource bounds. No real export, credential/provider change or migration. R01 closed; R02-R12 open11, added0; accepted5/60 and3/8 unchanged; ETA unvalidated. No scope deviation.

## Historical: consolidated closeout review

See APP013_P06_R02_CLOSEOUT_REVIEW.md for the finite credential/consumer and usable-backup requirements, grouped preparation proposal, exact approval boundaries and R02 pass test. Completed synthetic/storage work is retained; no new recovery-method choice or container creation requested. Documentation audit only; no external actions authorized or performed. R01 closed, R02-R12 open11, added0; accepted5/60 and3/8 unchanged, ETA unvalidated. No scope deviation.

## Historical: R02 recovery recommendation corrected — migration blocked

Owner approved preparation using six-hour recovery, but fresh specific Neon restore documentation says PITR supports root branches only. Current target br-sparkling-sun-ay6gr5e8 is a child; earlier console source was production. Retention is not proof of child self-history recovery. See backend evidence/APP-013/p06-r02-recovery-policy-correction.md. No credentials or provider/database changes. Owner must choose a separately qualified recoverable-root or private logical-backup approach; neither is authorized by the six-hour-policy approval. R02 remains open, R01 closed, R02-R12 open (11), added0; accepted5/60 and3/8 unchanged, ETA unvalidated. Recovery-method deviation proposed, not implemented.

## Historical: prior credential/recovery qualification


Read-only inspection of the created P06 child found only inherited `neondb_owner` (created/updated 18 days ago) and no independent Postgres migration credential. Official Neon behavior confirms an unprotected normal child inherits role passwords; this Free-plan parent cannot use paid protected-branch separation. Backup & Restore exposes only a moving six-hour history window sourced from `production`, while snapshots are root-only. No credential, snapshot, restore, migration, connection or data action occurred. R02 remains open pending approval of an exact child-only migration role/secret boundary and one destructive recovery policy; see backend `evidence/APP-013/p06-r02-credential-recovery-qualification.md` and `APP013_P06_ISOLATED_BRANCH_PROPOSAL.md`. R01 closed; R02-R12 open (11), added 0. Accepted 5/60 (8.3%), walkthrough 3/8 (37.5%), P06 unaccepted, ETA unvalidated. No scope deviation.

## Historical: R02 branch created and capped — no migration or credential authority

Owner explicitly approved one standard child and then the brief default-compute interval before immediate capping. Created p06-isolated-staging-v1 (br-sparkling-sun-ay6gr5e8), endpoint ep-jolly-flower-ayc6w9hv, in soft-smoke-54063480 from br-young-term-ayfi7ist. Browser readback: 0.25 CU fixed, five-minute inactivity suspension, expiry Never; parent remains production/default at 0.25–2 CU. No application connection, password/secret change, migration, deployment or paid-plan upgrade. See backend evidence/APP-013/p06-isolated-branch-created.md and APP013_P06_ISOLATED_BRANCH_PROPOSAL.md. R02 remains open for credential/connection isolation and recovery qualification; R01 closed, R02–R12 open (11), added0. Accepted5/60 (8.3%), walkthrough3/8 (37.5%), P06 unaccepted, ETA unvalidated. No scope deviation beyond the expressly approved branch/setup amendment.

## Historical: prior qualification observations


Direct Neon endpoint identified from hidden-password connection UI. Baseline b6f1d13 requires non-null location fields; new null writes cannot be assumed compatible with older shared readers. See backend p06-direct-connection-compatibility.md. Proposed isolated-branch investigation versus coordinated shared-target maintenance requires owner direction; no branch/config/data action authorized or performed. R02 open,11 remaining,added0; no acceptance or ETA change.

PostgreSQL18 local qualification passed under explicit owner approval; see backend p06-pg18-rehearsal.md and APP013_P06_R02_PG18_CARD.md. Installed18.6 without changing existing16/17 services; private no-TCP cluster stopped after unchanged migration rehearsal passed. R02 still open for migration connection, consumer/write isolation and recovery checkpoint/owner. Closed R01; open R02–R12 (11), added0. Accepted5/60 and3/8 unchanged, ETA unvalidated. No staging/resource/provider action; no scope deviation.

Read-only consumer review found nine tagged revisions and an existing migration job referencing the staging database secret; baseline scheduling and old SMS-test sending flags remain enabled. No actual activity inferred. Neon UI reports PostgreSQL18 versus local rehearsal16.11 and six-hour history without snapshots. Exact evidence: backend p06-target-consumers-recovery.md. R02 stays open pending version/connection, consumer maintenance and recovery qualification; no resource changes. Closed R01, open R02–R12 (11), added0; acceptance5/60 and3/8 unchanged, ETA unvalidated. Stop for material installation/maintenance/recovery decisions. No scope deviation.

## Historical: R01 completion checkpoint

Owner approved with "ok great lets proceed if any questions stop to ask proceed". Original twelve IDs and deliverables below are frozen; no tasks added. R01 is locally complete per backend evidence/APP-013/p06-migration-upgrade-rehearsal.md and APP013_P06_R01_REHEARSAL_CARD.md. **Closed: R01 (1/12). Open: R02–R12 (11/12).** No acceptance increase or ETA inferred. Next R02 qualification; stop for material questions/authority. The proposal wording below is the retained reviewed baseline, not a request to approve it again.

## Original reviewed authority and status

Owner requested a finite reconciliation after repeated misleading "two sections left" reports, then said "thanks proceed". This authorizes this documentation audit only. **Proposed baseline: awaiting owner review.** No implementation, migration, provisioning, deployment or paid test is authorized here.

Entry: backend 27f02e6, governance d9044c9; both focused origins fetched and matching their focused HEADs. Backend PR21 remains open; governance open PR5 is a different branch, not this change. Saved backend user changes are preserved. Runtime source remains 53037fb; existing built image digest ea47a8371a04f773a5c51fc4f939250b7045eba92d3cbbeb68e49ceb0240be35.

P06 still means the existing APP-013 / 2B finish: one protected phone verification → eligible address → explicit reviewed submission → exactly one job, followed by safe closeout and owner acceptance. Payment, scheduling and confirmation sending are later walkthrough sections, not P06.

## Reporting correction

The old two labels were broad containers, not two executable work sections. They hid material prerequisites and gave a misleading impression of remaining effort. They must not be used as a remaining-task count. This document supersedes that wording and stale next-action/estimate paragraphs in earlier evidence; history is preserved, not new authority.

Completed work is retained: browser journey and startup locally tested (p06-loaded-browser-journey.md, p06-startup-wiring.md); image built and digest verified (p06-release-packet-review.md); read-only schema inventory and migration proposal documented (p06-staging-schema-readonly.md, p06-staging-migration-plan.md). These do not establish live acceptance. Previously reported runtime tests are historical, not rerun in this audit.

## Fixed proposed inventory: 12 open tasks

All IDs below are internal P06 tasks, not new packages or acceptance sections. Each row is open, including rows with supporting partial evidence. Dependencies are task IDs. Implementer = Codex; owner = Debynyhan; cloud/database authority = owner or expressly designated administrator. No task promises one turn or one day.

| ID | Type / responsible role | Bounded deliverable and pass/fail exit | Depends on / current blocker |
| --- | --- | --- | --- |
| P06-R01 | Local engineering / implementer | Synthetic old-schema upgrade rehearsal: first 13 migrations, fictional existing consent/property rows, pending 13 via pinned Prisma7.10; preservation, revision/nullability, constraints/triggers, history/checksums, second-run no-op and timeout/failure cleanup evidence. No live clone. | Existing migration plan; not performed. |
| P06-R02 | Read-only qualification / implementer + database authority | Identify exact staging project/branch/endpoint/PG major/migration connection, every consumer and baseline compatibility; document usable recovery point, expiry, restore owner/method and maintenance need. All fields verified or explicit blocked result. | Access and recovery evidence not yet qualified. Backup/branch creation is NOT silently included. |
| P06-R03 | Approval gate / owner | Approve exact 13-file migration manifest, target, tested runner/timeouts, recovery, maintenance and cost/one-attempt boundary. No blanks accepted. | R01,R02. |
| P06-R04 | Authorized staging action / implementer | Fresh metadata/lock/drift gate; one approved migration attempt; verify all26 successful records/checksums and catalog, baseline health and intake disabled. Stop on partial failure; no automatic repair/resolve/reset. | R03; no execution approval yet. |
| P06-R05 | Design qualification / implementer + owner reviewer | Resolve exact private-material delivery into current startup JSON, numeric version provenance/key separation, runtime facts/HTTPS origin and approval activation/revocation method; produce exact commands or interfaces, tests and resource diff. Explicitly identify any missing implementation. | Startup expects injected JSON; mapping and approval writer are not qualified. Design output, NOT blanket coding authority. |
| P06-R06 | Read-only run qualification / implementer | Refresh exact tenant/integration/category/organization/payment policies, exception identity, provider ownership/restrictions/rates, prior liabilities, participant notice/eligibility; set finite request caps and itemize verification AND infrastructure costs. Private inputs stay private. | Current account/state evidence must be refreshed under applicable access authority; no sends or resets. |
| P06-R07 | Approval gate / owner | Review exact release/configuration/provisioning diff, numeric bindings, maintenance/rollback, enabled-run procedure and itemized allowance. Approve only named external changes, not a future unknown patch. | R04,R05,R06; no unresolved design/implementation allowed. |
| P06-R08 | Authorized provisioning / implementer | Execute only R07-approved purpose-key/material/least-privilege configuration; verify provenance/separation and revocation path without logging values. Existing liabilities/evidence unchanged. | R07; no new secrets or IAM authority from this plan. |
| P06-R09 | Authorized disabled release / implementer | Deploy exact approved digest with intake disabled/no normal traffic; read back revision/tag/origin/flags; verify closed intake and baseline health/webhooks. Preserve unrelated tags/traffic. | R04,R07; R08 may follow if disabled release needs no new material. |
| P06-R10 | Final run approval / owner + implementer | Bind actual deployed revision, packet digest, approved current policies/caps, participant readiness and fresh absolute UTC window; owner explicitly authorizes one connected run and defined shutdown. All prior gates rechecked. | R08,R09,R06 current; no inherited paid-test approval. |
| P06-R11 | Controlled acceptance execution / implementer + participant | Execute authorized activation and same-session phone → address → explicit submit. Correlate actual results and exactly one job or truthful refusal; never auto-resend/retry beyond packet. Record sanitized evidence, no payment/booking/send activation. | R10. Failure does not count as acceptance or authorize a rerun. |
| P06-R12 | Closeout and acceptance / implementer + owner | On success OR failure: stop authority, close/purge permitted session material, revoke temporary access, restore inactive state/read back, retain job/audit/unknown holds and assign billing reconciliation. Owner accepts 2B only with successful connected evidence and closeout. | R11 or early abort; cleanup is mandatory even when acceptance fails. |

Source traceability: R01–R04 = APP013_P06_STAGING_MIGRATION_PLAN.md and schema evidence; R05,R08 = APP013_2B_ACTIVATION_PACKET.md enabled bindings plus startup evidence; R06,R07,R09,R10 = activation packet release/run gates; R11,R12 = frozen 2B finish and packet closeout. No new feature is inferred from these rows.

**Task count: 0/12 closed, 12 open in this proposed remaining-work inventory.** This does not erase previously completed P06 work. Four are external execution tasks (R04,R08,R09,R11), three are owner approval gates (R03,R07,R10), three are engineering/qualification tasks (R01,R05,R06), one combines qualification and administrator evidence (R02), and one is mandatory closeout/acceptance (R12). No equal-effort percentage is implied.

## Known uncertainty — not hidden additional work

R02 may reveal unavailable recovery or incompatible consumers. R05 may require a startup/approval-management correction; its implementation is **not** pre-authorized or concealed inside design qualification. R11 may fail. These are known decision points, not claims that twelve tasks guarantee success.

If any requires work outside a row's deliverable: STOP the affected path; record U01/U02/etc with evidence, cause (missed prerequisite, defect, external change or owner scope), alternatives, proposed files/actions, added effort/tasks and dependency impact. Obtain owner approval before implementation. Preserve v1 and show delta (for example: original12, completed3, approved-added1, remaining10). Never replace "12" silently or rename discovered work as routine cleanup. No automatic retry or substitute demonstration.

Required defect fixes within an already approved implementation card retain their task ID and disclose rework; a new interface, subsystem, material prerequisite or external action needs an explicit change record. Closed tasks reopen only with evidence and visible reason. No task is closed merely because a document was written unless that task's specified deliverable is documentation.

## Execution and tracking rules after review

For every handoff report: baseline version; task IDs completed this turn; closed/open IDs; owner/external blocker; evidence SHA; next observable result; scope deviation or proposed change. Record active work minutes separately from approval/external waiting and rework. Do not convert turns, commits or tasks into productive days.

Before coding/action, complete the existing required section card with exact source/files/interfaces/tests and authority. Run relevant full build/lint/tests/architecture/DB/browser gates for code; governance/architecture/whitespace for docs. R01 uses synthetic local DB only. R04 and R09 require actual target readback. R11 requires actual correlated journey evidence; prior synthetic tests cannot substitute.

Acceptance remains **5/60 packages (8.3%) and 3/8 walkthrough milestones (37.5%)**, not overall MVP completion. P06 is unaccepted. The previous **4–8 week forecast is unvalidated and withdrawn as a current estimate** pending remaining-work sizing; do not repeat it as unchanged. The next ten-accepted-package timing review remains a checkpoint, not a deadline guarantee.

The approved 60-package denominator and 2B → 3A → 3B → 3C → 3D sequence remain unchanged. Before each later package begins, expose its finite tasks/dependencies/exit tests and review substantial uncertainty; do not fabricate detailed future implementation lists without entry inspection.

## Review decision and stop

Review this twelve-task inventory and the explicit R02/R05 uncertainties. Approval freezes the reporting baseline; it does not authorize migration, secrets, deployment, charges or live customer actions. First implementation candidate after baseline review is R01, with its exact executable rehearsal card completed first.

This turn: documentation correction only; no runtime or external change. **No scope deviation implemented.** Proposed reporting decomposition is awaiting review; protected acceptance text and baseline-check anchors are unchanged.
