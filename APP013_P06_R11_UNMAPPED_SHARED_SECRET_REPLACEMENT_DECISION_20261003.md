# APP-013 / 2B / P06-R11 — unmapped shared-secret replacement and credential containment decision

## Decision requested

Choose **Alternative 1** to replace the unmapped shared database secret from the current Neon production branch and contain the exposed administrator credential in one attended operation, or choose **Alternative 2** to keep all live Signmons work stopped. Alternative 1 is recommended.

No credential reset, password display, secret version, tag, revision, traffic, job definition, database session or other external state change is authorized by this proposal. Alternative 1 requires exact owner approval and a future 90-minute Eastern window before an executable package may be prepared.

## Section, acceptance criterion and demonstrated gap

- **Approved section:** APP-013/2B/P06-R11 security prerequisite. P06 remains 12/14; R11 still requires one correlated protected phone, eligible-address and reviewed-submit journey that creates exactly one job. Full R12 closeout and owner acceptance remain open. Accepted walkthrough milestones remain 3/8.
- **Demonstrated gap:** shared Secret Manager version `signmons-staging-database-url:2` contains an exposed `neondb_owner` credential, but consumed operation `e13000fe-7d13-4e9c-9e39-a164873c98ce` proved its hostname matches neither the direct nor pooled canonical hostname of either current endpoint in the only visible Neon project. That result is terminal; never rerun it.
- **Connected workflow impact:** normal Cloud Run traffic, eight historical tagged origins and the migration-job definition reference the unmapped shared secret. A future controlled intake journey must not depend on that exposed/unmapped value. This replacement restores a current, numerically pinned production database reference before any new R11 attempt.
- **No acceptance change:** credential containment is a prerequisite, not a new section or accepted milestone.

## Verified current evidence

### Source and reusable controls

- Preparation baseline: backend `3cf8a9dc53d0282a35e6263a36d749c5b32f8e2e`; governance `8d7c644ecc8e65ec139bcfcc3fef055ad5d423cd`. Both focused worktrees are dirty with prior user/governed work and must be preserved.
- Runtime source of truth: immutable normal revision `signmons-calldesk-staging-app013bounds` and its exact image digest/configuration, not the dirty checkout and not the current enabled35 service template.
- Reuse the existing owner-hidden-input boundary in `scripts/p06_private_input.py`, one-use reservation/no-retry patterns in the P06 coordinators, existing Cloud Run exact-revision/configuration validators, `HealthService.isDatabaseReady()` through `/health/readiness`, and the existing secret-pattern/architecture/governance checks.
- Proposed local files after approval: one execution-disabled coordinator `scripts/p06-r11-unmapped-secret-replacement.py`, one focused fictional test `scripts/test_p06_r11_unmapped_secret_replacement.py`, one private window-bound package outside the repository, and updates to this decision/current-status evidence. No application `src/`, schema, migration or dependency file is expected to change.

### Neon

Authenticated read-only console inventory on October 3, 2026 shows one visible project, `soft-smoke-54063480` (`signmons-staging`), in AWS US East 2:

- production branch `br-young-term-ayfi7ist`, primary endpoint `ep-nameless-frog-ayk5gr5y`, role `neondb_owner`, database `neondb`;
- isolated child branch `br-sparkling-sun-ay6gr5e8`, primary endpoint `ep-jolly-flower-ayc6w9hv`, owner role plus the three P06 roles `p06_migration_owner`, `p06_migration_runner` and `p06_intake_runtime`.

Official Neon role documentation states that roles belong to branches, parent roles are copied when a child is created, password resets are branch-scoped, a reset takes effect for the next connection, and existing sessions are not thereby proven closed. The production and child `neondb_owner` credentials must therefore be reset separately. The three limited P06 roles are not reset.

Official Neon material also states that pooled hostnames add `-pooler` to the endpoint ID and that current Neon pooling supports Prisma migrations. The replacement can retain the existing one-secret/one-URL design using the current production pooled endpoint; no second migration secret or IAM expansion is proposed.

### Google Cloud

- normal traffic is 100 percent on immutable baseline revision `signmons-calldesk-staging-app013bounds`;
- that revision uses image digest `sha256:37286933d882466b8592120f48eb69c34e14cdb5a23c1f37480e39a1e6ff933a`, runtime service account `signmons-calldesk-runtime@signmons.iam.gserviceaccount.com`, concurrency 40 and timeout 60;
- its database reference is `signmons-staging-database-url:latest`; its readiness endpoint performs a database check;
- the current service template is enabled35 and uses the isolated child secret, so it must never be cloned for normal traffic;
- migration job `signmons-calldesk-migrate` uses `signmons-staging-database-url:latest`; its last execution was September 7 and it must not run in this operation;
- shared secret version 2 is enabled and version 1 disabled;
- child secret `signmons-staging-p06-child-database-url:2` is enabled and must remain unchanged;
- no enabled intake tag exists. Tagged `p06-intake-disabled` uses the child secret and remains. Eight other historical tags reference the shared secret.

## Alternative 1 — coordinated replacement and containment

### Exact intended changes

1. Reset `neondb_owner` separately on the current production and isolated child branches through the owner-operated Neon Console. Neon generates each replacement. The owner stores both in a password manager; neither value enters chat, shell history, argv, repository files, screenshots or agent-visible DOM.
2. Use only the new production password to construct a percent-encoded pooled URL for `ep-nameless-frog-ayk5gr5y-pooler.us-east-2.aws.neon.tech`, database `neondb`, SSL required. Add exactly one new numeric version to existing secret `signmons-staging-database-url`. Do not create a new secret and do not touch `signmons-staging-p06-child-database-url:2`.
3. Clone the exact immutable `app013bounds` revision configuration, changing only `DATABASE_URL` from shared `latest` to the new numeric shared-secret version. Preserve image digest, runtime identity, ingress, resources, scaling, concurrency, timeout, all other secret references and every non-database environment value. Deploy under a fresh reviewed revision name at zero normal traffic.
4. Require Cloud Run Ready plus HTTP `/health/readiness` success against the zero-traffic tagged candidate. Readiness must prove a database connection through the new numeric secret; a liveness-only result is insufficient.
5. Change only the migration job's `DATABASE_URL` secret reference from shared `latest` to the same new numeric version. Do not change its image, service account, retries, timeout, command or arguments, and do not execute the job.
6. Move 100 percent normal traffic atomically to the verified replacement and bind `app013-bounds` to it. Remove the eight obsolete shared-secret tags: `app009`, `app012-candidate`, `phone-preflight`, `app013-sms-test`, `be008-bounds`, `be008-noquiet`, `be008-candidate` and `be008-twilio`. Preserve `p06-intake-disabled` on its child-secret revision. Do not create an enabled intake tag.
7. After the replacement serves normally, inspect database sessions with metadata-only projections. Terminate only sessions proven to use `neondb_owner` from pre-replacement application revisions or the consumed helpers. Unknown ownership stops broad termination. Read back normal readiness and the absence of old tagged traffic.
8. Disable shared secret version 2 only after the replacement revision, traffic, tag set and migration-job numeric reference all read back correctly. Do not destroy version 2 in this operation. Preserve version metadata for audit and later retention review.
9. Verify both current branch owner resets are complete, the child limited runtime secret/version and three P06 roles are unchanged, normal traffic is 100 percent on the replacement, the enabled tag is absent, old shared-secret tags are absent, the migration job remains unexecuted, and no secret pattern appears in saved artifacts.

### Preparation before any reset

The implementer must prepare a one-use package bound to a fresh fixed window and current read-only inventory. It must contain:

- exact source revision export and redacted one-field configuration diff;
- fixed replacement revision/tag names and complete tag disposition;
- fixed expected old/new numeric version metadata, without values;
- owner handoff points for the two Neon resets and one Secret Manager value entry;
- guarded commands for zero-traffic deploy, database-backed readiness, job metadata update, atomic traffic/tag change, exact session closeout, old-version disable and final readback;
- one-use reservations for every mutation, no automatic retry, sanitized fixed receipts and a final secret-pattern scan;
- positive, refusal, drift, partial-reset, secret-add, startup/readiness, job-diff, traffic, tag, session, rollback and closeout checks.

Local validation must include Python compilation/focused tests, an actual disposable fictional coordinator sequence with no cloud/provider calls, architecture, the backend-to-governance baseline check, governance frozen-baseline/consistency/21 tests and `git diff --check` in both repositories. Browser testing is not applicable to the credential/configuration change; the exact HTTP `/health/readiness` probe is the runtime gate.

No package may read the old secret payload again. The consumed identity and mapping helpers remain immutable and consumed.

### Order and stop rules

Preparation and every read-only preflight complete before the first reset. At execution:

1. remove the eight obsolete shared-secret tags;
2. owner resets production and child owner passwords privately;
3. owner adds one new production pooled URL as a numeric shared-secret version;
4. deploy and prove the zero-traffic replacement with database-backed readiness;
5. update and read back the migration-job reference without running it;
6. cut normal traffic and `app013-bounds` to the replacement;
7. contain proven old sessions and read back service readiness;
8. disable old version 2 and perform final closeout.

Stop on inventory drift, unexpected role/branch, value-entry uncertainty, failed reset, ambiguous secret version, non-one-field revision/job diff, failed database readiness, traffic/tag mismatch, unknown session ownership or incomplete readback. Never rerun a consumed mutation automatically.

The normal service may experience a short staging database interruption after the production password reset and before the replacement becomes Ready. The child limited runtime remains disabled and unchanged.

### Identity, data and retention boundaries

- Credential handling is owner-private. The implementer may see only branch/role/version identifiers and fixed success/refusal states.
- No customer, phone, address, job, payment or provider data is read or changed.
- Session inspection projects only PID, role, application/client metadata and timestamps necessary for exact ownership. It never records query text or customer data.
- Version 2 is disabled, not destroyed. Generated replacement passwords stay only in the owner's password manager and the approved secret-entry surface.
- The old hostname remains unidentified. This operation contains current visible Neon branches and all known Google consumers; it does not claim deletion or rotation of an inaccessible provider object that is not present in the authenticated inventory.

### Dependencies and owners

- **Owner:** exact Alternative 1 approval; future 90-minute Eastern window; authenticated Neon and Google Console availability; private password-manager custody; both Neon reset clicks; one Secret Manager value entry.
- **Implementer:** fresh metadata preflight, immutable config diff, package/tests, guarded Cloud Run/job/tag/session/version steps, readbacks, sanitized evidence and mandatory closeout.
- **External dependencies:** Neon and Google availability. Any sign-out, permission prompt, unexpected project/branch, billing request or provider warning stops at that boundary.

### Rollback and disabled state

- Before the first reset, rollback is no action.
- After a reset, the exposed password is never a rollback credential.
- Before traffic cutover, normal traffic may remain on `app013bounds` only while the operation is actively producing the replacement within the fixed window; failure closes with the shortest safe interruption and no new R11 attempt.
- After traffic cutover, rollback is only to a separately verified revision that uses the new numeric credential. Never route to a revision using version 2 or `latest`.
- The migration job remains unexecuted; controlled intake remains disabled; no customer journey follows automatically.

### Observable finish

Alternative 1 finishes only when sanitized evidence proves:

- separate production and child `neondb_owner` resets completed;
- one new numeric shared-secret version exists and version 2 is disabled, not destroyed;
- normal traffic and `app013-bounds` use the exact `app013bounds` clone pinned to the new numeric version and database-backed readiness passes;
- the migration job is pinned to that numeric version and has no new execution;
- all eight obsolete shared-secret tags are absent; `p06-intake-disabled` and child secret version 2 are unchanged; no enabled intake tag exists;
- proven old sessions are absent, unknown sessions were not terminated, and artifacts contain no credential.

Only then may a later decision return to fresh liability qualification and a future R11 journey. This operation itself does not complete R11 or R12.

## Alternative 2 — retain the safe stop

Make no credential, secret, revision, traffic, tag, job or session change. Keep all live Signmons work blocked because the exposed shared value remains unresolved and current normal consumers are not pinned to a verified current endpoint.

## Scope statement

Alternative 1 is a proposed security-containment deviation within APP-013/2B: two branch-scoped owner resets, one numeric version of the existing shared secret, an exact baseline-derived normal revision, one migration-job reference-only change, eight tag removals, exact-session containment and old-version disable. It adds no application feature, schema, dependency, IAM grant, acceptance section, provider message, customer action, migration execution or new live journey. It is not implemented or authorized until the owner explicitly selects it and provides the attended window.

## Owner decision and prepared package

The owner explicitly approved Alternative 1 and selected October 3, 2026, 7:30–9:00 a.m. Eastern (11:30–13:00 UTC). Fixed plan `b90fd97f-2c71-4b19-a897-f2b8733824c0`; operation `d9412e4d-5fe7-4a3f-bf79-a37bafd5e880`; external stages must begin before 8:15 a.m. Eastern and all work stops by 9:00.

The final self-contained coordinator SHA-256 is `fc41cfb57cb24b3be188be5643546df1766d1a9920c32231690df485f1f59de2`. It is installed 0700/0600 at `/private/tmp/r11-unmapped-secret-replacement-20261003-0730-v2` and returns `R11_REPLACEMENT_CHECK_PASSED_NO_ACTION`. Four focused fictional tests, Python compilation, architecture and whitespace pass. The first package was superseded before action because its private-input module was not hash-bound; its approval file was renamed, it has no action markers and it cannot pass approval validation. Never use it.

The owner approval authorizes the finite external sequence in this card during the fixed window. Browser credential resets remain owner-operated handoffs. No external mutation occurred during package preparation.
