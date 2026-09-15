# P06-R02 isolated branch proposal — not authorized for execution

Owner approved investigation of costs/setup after old-reader incompatibility was demonstrated. This document is the proposed change record, not authority to create resources, copy data, reset passwords, migrate or deploy. Existing v1 remains12 tasks; R01 closed, R02 open. No scope deviation implemented.

## Verified pricing and account evidence

Neon official pricing read this turn: Free includes10 branches/project,100 CU-hours/project/month,0.5GB/project storage and5GB egress; five-minute scale-to-zero. Earlier signed-in account observation: Signmons Free, one project signmons-staging, one branch, approximately1.84CU-hours and0.04GB usage. Those usage figures are historical and must refresh before creation. A second branch within these allowances is expected to add USD0 Neon plan charges, conditional on staying Free and within limits; no upgrade/payment authorized. Shared quota exhaustion can suspend compute and affect the original staging project. This is not cost or resource isolation.

Proposed compute cap0.25CU fixed, five-minute idle suspension. One hour active consumes0.25CU-hours plus any additional active time; no always-on setting. If UI cannot enforce this size/Free constraints, stop rather than accept defaults silently. Snapshot count allowance is NOT proof of free snapshot storage: pricing lists USD0.09/GB-month for snapshots. No snapshot is included in this proposal. Cloud Run/Secret Manager/provider fees are outside this branch-only estimate and remain separately approved.

Sources: https://neon.com/pricing ; https://neon.com/docs/introduction/plans ; https://neon.com/docs/manage/branches ; https://neon.com/docs/guides/branching-schema-only . Retrieved directly as Markdown after web reader rejected content type. Directory CLI unavailable; no tooling installation. Documentation examples disagree on arithmetic for paid extra branches; no reliance on those examples or paid-plan pricing here.

## Exact proposed setup

- Existing project soft-smoke-54063480 (signmons-staging), Ohio, PostgreSQL18. Parent br-young-term-ayfi7ist (named production, dedicated to Signmons per owner).
- Proposed unique name p06-isolated-staging-v1. Check collision first, never overwrite. Record new branch ID, endpoint and creation timestamp from actual result; none exist yet.
- Standard current-data child branch preserves schema,13 applied migration records and existing records/holds. Explicit data-copy authorization required: inherited customer/test/consent/audit/provider-related records remain private, not exported to repository or displayed. No copied consent, proof, integration or tenant setting becomes new send/activation authority.
- Branch inherits database roles AND passwords according to Neon docs. Branch-only credential separation must be approved and completed before application use; never reset parent passwords or replace the shared staging DATABASE_URL. Do not assume endpoint separation is credential isolation. Inventory inherited roles/integrations without displaying secrets; unexpected inherited executable services are a stop.
- Do not change default branch, parent state, existing tags, existing migration job, provider webhooks or any app connection. Branch begins unconnected to application/provider workflows. Later R03/R04 must bind this new exact target before any migration; R07–R10 must bind separate numeric secret, candidate, policies and allowance before application use.
- Do not accept automatic24-hour deletion for a branch intended to hold owner-accepted test evidence. Propose no auto-delete, with explicit closeout review before deletion; record owner Debynyhan and implementer cleanup responsibility. This retains storage until reviewed deletion and is not a hidden backup claim. If owner wants a disposable rehearsal-only branch instead, choose explicit TTL and do not use it for accepted live-job evidence.

## Why not schema-only by default

Schema-only copies structure/roles but no row data. Inference: it also omits _prisma_migrations rows, so running the existing13-pending migration plan would not be valid without a separately reviewed baseline/bootstrap procedure. It would require fresh tenant/policy/identity setup too. Standard branching avoids that additional bootstrap work but requires explicit inherited-data and credential approval. Neither is silently selected or created.

## Recovery and fixed-plan impact

Isolation protects parent records from branch writes; it does NOT prove recovery of new branch test records. Before a paid connected run, R02 still needs an actual usable checkpoint/expiry and restore owner/procedure for this branch. Six-hour history is time-limited; no automatic reset/retry or deletion of accepted records. Migration failure stops with evidence, not reset-from-parent/resolve. Do not mark R02 done just by creating a branch.

Changes proposed to existing tasks: R02 qualifies child instead of shared parent; R03/R04 migration manifest targets child; R07/R08 use child-only numeric connection credential; R09 candidate uses child; R10–R12 approvals/retention/closeout bind child. No new feature/package or acceptance criteria; additional setup effort must be tracked as approved R02/R08 work, not zero-cost effort. If implementation exceeds these boundaries, disclose delta before proceeding.

## Owner decision

Approve this standard-child direction and explicit private inheritance of existing staging data, or choose schema-only with a separately scoped bootstrap proposal. Creation, branch-only credential changes and future deletion require the exact external action approval; this investigation grants none. Before any creation refresh Free-plan usage, name availability, compute controls and data/role inheritance; stop if charges/upgrade/unknown services appear.

Review: compare proposed name/parent/data inheritance/credential boundary/retention and fixed-task impacts. Docs/architecture/frozen/full consistency/21 regression/whitespace checks apply; no new application tests or live proof claimed. Accepted5/60 and3/8 unchanged; ETA unvalidated.
