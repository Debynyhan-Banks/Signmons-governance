# P06 remaining-work reconciliation — review baseline v1

## Current: R02 target qualification partial — no execution authority

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
