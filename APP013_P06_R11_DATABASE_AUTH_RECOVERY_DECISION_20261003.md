# APP-013 / P06-R11 staging database-auth recovery decision

## Status

The approved 5:00-6:15 p.m. operation stopped at its private authentication stage before creating a secret version. The owner disclosed that the entered value came from Notepad rather than directly from Neon. That operation is consumed. The owner approved the fresh direct-copy recovery operation for 5:25-6:40 p.m. Eastern.

## Section and demonstrated gap

- Approved section: APP-013 / P06-R11 credential containment inside the accepted 2B walkthrough.
- Acceptance criterion advanced: the disabled P06 posture remains preserved while the connected staging runtime and migration job use a verified, current production database credential.
- Evidence inspected on 2026-10-03:
  - consumed operation `d9412e4d-5fe7-4a3f-bf79-a37bafd5e880` created `signmons-calldesk-staging-app013dbrot1` at zero traffic but stopped at database readiness;
  - revision logs reported PostgreSQL `28P01` for `neondb_owner`;
  - an owner-operated hidden direct check refused the only saved production password;
  - both the serving `app013bounds` revision and the zero-traffic candidate returned readiness `503`;
  - shared secret versions 2 and 3 remain enabled but neither authenticates after the Neon production-role reset;
  - normal traffic remains 100% on `signmons-calldesk-staging-app013bounds`; `p06-intake-disabled` remains present; no enabled P06 tag exists.

## Proposed bounded recovery

- Plan ID: `4a5083b6-9a3f-4731-b790-857631fde2e6`
- Operation ID: `b7fd54f3-f321-4d8e-9f41-df5d7f1118c1`
- Owner-approved Eastern window: 2026-10-03 5:25-6:40 p.m.; first external stage must begin before 5:35 p.m.
- Owner handoff: reset production-branch `neondb_owner` once more and use Neon's Copy control to paste the generated value directly into the hidden coordinator prompt. Notepad is excluded from the credential path.
- The coordinator accepts the password once through a hidden terminal prompt, proves it with direct `SELECT 1`, and only then creates one new numeric secret version.
- Deploy distinct revision `signmons-calldesk-staging-app013dbrot2` with zero traffic; preserve the baseline image and configuration; require exact-spec readback and HTTP 200 database readiness.
- Pin migration job `signmons-calldesk-migrate` to the new numeric version without executing it.
- Move normal traffic and `app013-bounds` only after candidate readiness succeeds; preserve `p06-intake-disabled`.
- Wait up to 15 minutes for pre-reset owner sessions to drain, prove none remain, disable invalid secret versions 2 and 3 without destroying them, and perform final readback.

## Tests and stop rules

- Positive: private password authenticates; new version exists; candidate is ready at zero traffic; readiness is 200; job is pinned but not executed; cutover and final inventory match exactly.
- Negative: wrong password creates no secret version; failed readiness prevents job update and cutover; unexpected traffic, revision, image, tag, secret state, or job execution stops the stage.
- Concurrency/recovery: every mutating stage reserves an immutable attempt marker before action; a result or stop marker makes that stage non-retriable. A stopped stage requires a new decision and operation.
- Browser: credential entry, confirmation, and reset submission remain owner-operated; passwords never enter chat or evidence.
- Rollback/disabled state: until readiness succeeds, traffic remains on the current revision. P06 stays disabled throughout.
- Observable finish: `R11_DB_AUTH_RECOVERY_VERIFIED` plus Cloud Run, job, secret-version, session, and tag readbacks.

## Expected files and interfaces

- Backend coordinator: `scripts/p06-r11-db-auth-recovery.py`
- Focused tests: `scripts/test_p06_r11_db_auth_recovery.py`
- Private approved package: `/private/tmp/r11-db-auth-recovery-20261003-1725`
- External interfaces: Neon production role reset UI, direct PostgreSQL TLS authentication, Secret Manager version add/disable, Cloud Run service replace/traffic update, and Cloud Run job configuration update. No job execution, customer request, message, appointment, charge, or production deployment is included.

## Checklist

- [x] Demonstrated gap and current external state captured.
- [x] Fresh one-use coordinator and focused tests prepared locally.
- [x] Owner approved the fresh exact operation and 5:25-6:40 p.m. window.
- [ ] Read-only preflight passes.
- [ ] Owner resets production again and copies the generated value directly from Neon.
- [ ] Password authenticates before a new secret version is created.
- [ ] Candidate readiness passes at zero traffic.
- [ ] Migration job is pinned without execution.
- [ ] Traffic cutover and session check pass.
- [ ] Invalid versions 2 and 3 are disabled, not destroyed.
- [ ] Final readback and governance closeout are recorded.

No scope deviation.
