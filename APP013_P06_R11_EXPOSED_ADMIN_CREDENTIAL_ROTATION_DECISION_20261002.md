# APP-013 / 2B / P06-R11 — exposed administrator credential rotation decision

## Owner decision and window

The owner answered the combined Alternative 1 approval/window request with **9:30 p.m. until Eastern today**. This records Alternative 1 approval and the requested fixed 90-minute attended window as October 2, 2026, 9:30–11:00 p.m. Eastern (October 3, 01:30–03:00 UTC). Preparation does not move the start, end or stop time. Any incomplete or uncertain external sequence closes safely by 11:00 p.m. without reusing the window or exposed credential.

Preparation/qualification is 9:30–9:50, owner-private provider reset and secret entry 9:50–10:20, normal replacement/job-reference cutover 10:20–10:40, session/version containment 10:40–10:55, and mandatory closeout by 11:00. These phase times are maximum bounds, not permission to skip prerequisites or continue after uncertainty.

## Approved implementation card

- **Section and criterion:** APP-013/2B/P06-R11; remove the exposed administrator credential as a prerequisite to any future connected acceptance journey while preserving the frozen R11 acceptance criterion and counts.
- **Source/evidence of gap:** owner pasted the inherited administrator password during consumed enabled35; `p06-r11-enabled35-preview-disabled-closeout-20261002.md` and `p06-r11-exposed-admin-credential-qualification-20261002.md` establish closeout and secret/consumer separation.
- **Source baseline:** preserve the current dirty focused worktree. Reuse `scripts/p06_private_input.py` hidden-input principles and the existing Google secret adapter/no-retry patterns. Normal replacement source is immutable revision `signmons-calldesk-staging-app013bounds`, image digest `sha256:37286933d882466b8592120f48eb69c34e14cdb5a23c1f37480e39a1e6ff933a`; never use the current enabled35 template.
- **Expected local files:** new `scripts/p06-r11-shared-secret-identity.py` and focused `scripts/test_p06_r11_shared_secret_identity.py`; this decision and backend qualification/preparation evidence. No application `src/`, schema, migration or dependency change.
- **Helper behavior:** one fixed operation `0580681c-e4c7-4ac1-a08d-b5f2756bfb80` under plan `bda2718d-9f8d-4701-9913-c9c95609eae4`, root `/Volumes/Signmons-P06/r11-credential-rotation-20261002-2130`. It validates exact owner approval/window/source/hash, reserves once, accesses only shared secret version2, parses in memory and writes only role/host/database/scheme match booleans plus fixed status. It never prints/persists payload, password, URL, hash or raw exception. Any attempt or uncertainty consumes it.
- **Identity/data/state boundary:** fixed project `signmons`, shared secret version2, expected parent host `ep-nameless-frog-ayk5gr5y.us-east-2.aws.neon.tech`, database `neondb`, role `neondb_owner`. No customer/business row read. Secret payload exists only in process memory and is overwritten where practical; no claim of forensic memory erasure.
- **External change boundary:** only after exact identity match and fresh Neon branch inventory: owner-private resets on each affected branch, one shared parent secret version, one exact `app013bounds`-derived no-traffic revision, one traffic cutover, one migration-job reference update without execution, reviewed tag disposition, exact session containment, old shared version disable and closeout. Child secret version2 remains unchanged.
- **Tests:** valid fictional URL; wrong scheme/role/host/database; absent password; oversized/malformed/multiline value; wrong approval keys/IDs/window/hash; early/late; existing attempt/result; gcloud refusal/timeout/ambiguous output; no secret in stdout/stderr/result; concurrent reservation; `--check` no action. Run focused Python tests, syntax, secret-pattern scan, governance baseline/consistency/21 tests and both whitespace checks.
- **Dependencies/owners:** owner operates authenticated Neon and Secret Manager value screens and keeps replacements in a password manager; implementer runs sanitized qualification, exact configuration diff/readbacks and closeout. Google/Neon availability and all known consumers must qualify. Unknown branch, session, payload identity, permission or mutation outcome stops.
- **Exclusions:** no P06 child runtime password/secret change, app code change, migration job execution, customer journey, phone/address/provider request, limit reset, data migration, IAM expansion, new role or automatic retry.
- **Rollback/disabled state:** exposed password is never a rollback. Before traffic cutover, normal traffic remains `app013bounds`; after cutover, roll back only to a separately verified revision using the new credential. On any failure, no enabled intake tag, limited runtime remains disabled, migration job unexecuted and old secret version retained enabled until a safe replacement is proven. Disable the old version only after all readbacks pass.
- **Observable finish:** every affected branch password replaced, normal service and migration job reference the verified new numeric shared version, old sessions resolved, old shared version disabled, normal traffic100%, enabled intake tag absent, child secret version2 unchanged, sanitized receipts saved and no secret pattern in artifacts.

Implementation of the local helper/card is approved by the owner's response. External mutation begins only inside the recorded window after every fresh preflight passes.

### Pre-window refusal classification

At approximately 8:35 and 8:37 p.m. Eastern, the owner invoked the installed helper before the fixed start and reported its generic refusal status. Immediate readback after each found no attempt, result or stop marker and unchanged installed hashes and modes. Reviewed helper control flow validates `START <= now < START_BEFORE` before reserving the attempt or accessing Secret Manager. The reported invocations therefore stopped at the deterministic `WINDOW` guard, accessed no payload and did not consume operation `0580681c-e4c7-4ac1-a08d-b5f2756bfb80`.

The approved helper and approval remain unchanged. Its one initial invocation remains authorized only from 9:30 p.m. through 9:49:59 p.m. Eastern. This classification does not extend the window or authorize a second in-window attempt: any in-window attempt marker, result, stop or uncertain outcome consumes the operation and stops further use.

### Terminal identity mismatch

The single in-window invocation reserved operation `0580681c-e4c7-4ac1-a08d-b5f2756bfb80` at 9:32:52 p.m. Eastern and completed at 9:32:53 with `MISMATCH`. The sanitized receipt reports that the scheme, `neondb_owner` role, password presence, port and `neondb` database matched, while the host did not match the fixed expected parent endpoint. Attempt/result records exist, no stop record exists, and installed hashes/modes remain correct. No raw host, URL, password, payload or payload hash was persisted or printed.

This operation is consumed and must never be rerun. The approved card explicitly requires exact identity before external mutation, so the remaining Alternative 1 mutation sequence is stopped: no provider reset, shared-secret version, revision deployment, traffic cutover, migration-job reference update, session termination or old-version retirement is authorized. The exposure remains unresolved. A new, separately approved metadata-only decision must map the existing shared-secret endpoint to the current Neon branch inventory before any revised containment mutation can be considered.

## Demonstrated gap

During the consumed enabled35 attended helper, the owner pasted the existing `neondb_owner` administrator password into conversation. The value is now exposed and must not be reused or recorded. It is omitted from every repository record.

This is not the limited P06 runtime password. Fresh read-only Google metadata confirms enabled35 and `p06-intake-disabled` use `signmons-staging-p06-child-database-url:2`, the limited `p06_intake_runtime` URL. That version remains enabled and must stay unchanged during administrator rotation.

Normal traffic is 100 percent on `app013bounds`. That revision, eight other reachable historical tags and the migration job use `signmons-staging-database-url:latest`. Shared-secret version 2 is enabled and version 1 disabled. No payload was read, so current metadata alone does not prove whether version 2 embeds the exposed owner password. Prior governed evidence privately mapped it to the parent and warned that inherited `neondb_owner` credentials may authenticate on parent and child branches.

Cloud Run resolves secret environment variables at instance startup. Adding a new version does not replace values already present in running instances. Changing a PostgreSQL password does not terminate established sessions. The current service template is enabled35 and uses the child runtime secret; it cannot safely be cloned for normal traffic.

## Acceptance criterion and source evidence

Section APP-013/2B/P06-R11 still requires one contained connected customer journey and verified closeout. Future live evidence cannot safely use an exposed administrator credential. Backend evidence `evidence/APP-013/p06-r11-enabled35-preview-disabled-closeout-20261002.md` proves containment but no acceptance; `evidence/APP-013/p06-r11-exposed-admin-credential-qualification-20261002.md` records the current consumer/secret separation.

The credential incident adds a security prerequisite, not a new acceptance section or accepted milestone. P06 stays 12/14; R11/full R12 stay open; accepted 1A/1B/2A stay 3/8.

## Alternative 1 — coordinated containment and rotation

Recommended. One reviewed attended operation would perform the following finite sequence:

1. **Fresh read-only inventory.** In Neon, enumerate every current branch and the `neondb_owner` role metadata without revealing passwords. In Google, re-read service traffic/tags, every reachable revision's database-secret reference, migration-job reference, both secret version lists and current IAM. Drift stops.
2. **Private shared-secret identity qualification.** A reviewed local process accesses only `signmons-staging-database-url:2`, parses it in memory and returns only scheme validity, role name, fixed parent host match and database name. It emits no payload, password, hash or raw exception. A non-owner role or unexpected host stops shared-secret mutation while branch credential containment still remains necessary.
3. **Prepare the exact normal replacement before reset.** Export the immutable `app013bounds` revision configuration, pin its image and every non-database setting, and prepare a new no-traffic revision changing only `DATABASE_URL` from shared `latest` to the numeric version that the rotation will create. Never derive this revision from the enabled35 service template. Prepare a migration-job metadata update that changes only the database secret reference to the same numeric version; do not execute the job. Inventory and decide the disposition of the eight old reachable shared-secret tags before mutation.
4. **Owner-private Neon reset.** The owner uses Neon's authenticated role-reset flow and handles each generated replacement only in private password/secret-entry fields. Reset `neondb_owner` on every branch where the exposed credential is valid; do not assume a reset on one unprotected branch changes its parent or siblings. No replacement value enters chat, shell history, argv, repository files, screenshots or agent-visible DOM.
5. **Immediate Secret Manager update.** For the active parent mapping, construct the complete percent-encoded parent connection URL privately and add exactly one new version to `signmons-staging-database-url`. Record only the numeric version and metadata. Do not touch `signmons-staging-p06-child-database-url:2`.
6. **Normal service cutover.** Deploy the pre-reviewed `app013bounds` clone as a new no-traffic revision pinned to the new numeric shared-secret version. Require readiness, then move normal traffic atomically to it while preserving approved ingress and unrelated settings. Do not restore the enabled35 tag or runtime.
7. **Other consumers.** Update the migration job definition to the new numeric version without executing it. Remove or explicitly retain each reachable historical tag according to the reviewed inventory; no tag may be silently left with an unresolved running-instance credential state.
8. **Connection containment.** After the replacement is ready and serving, enumerate database sessions using metadata only. Close only sessions proven to belong to pre-rotation application instances or the consumed helper. Unknown ownership stops broad termination. Verify new normal readiness and no controlled runtime activation.
9. **Retire exposed versions.** Disable the old shared-secret version only after the new normal revision and job reference read back correctly and all known old sessions/instances are resolved. Destruction is a later retention decision, not part of the first containment pass. Preserve metadata/audit evidence without payloads.
10. **Closeout.** Verify normal traffic 100 percent on the replacement, no enabled intake tag, child runtime secret version 2 unchanged, P06 runtime role disabled, no unexpected branch/session/reference drift and no password in artifacts. Save a fixed result and do not retry uncertain mutations automatically.

This procedure may cause a short staging database interruption between provider reset and the new secret/revision becoming ready. The operation must name a future attended window and rollback boundaries. The exposed password cannot be a rollback credential.

## Alternative 2 — stop all live Signmons work

Perform no credential or cloud mutation. Keep all future database/provider/deployment journeys blocked because the administrator credential remains exposed. This avoids immediate staging cutover risk but does not contain the credential incident.

## Required implementation card before execution

- exact current Neon branch list and role-reset behavior;
- exact shared-secret identity-check helper, output schema and no-secret tests;
- exact `app013bounds` export/diff and replacement revision name;
- complete reachable-tag disposition;
- exact job one-field diff;
- owner-private input surfaces and password-manager custody;
- positive/negative/uncertain/reset/secret-add/deploy/traffic/session/closeout checks;
- one attempt, fixed window, responsible owner/implementer steps and stop times;
- explicit rollback state that never restores the exposed credential;
- evidence locations and final secret-pattern scan.

No source, password, secret, role, revision, tag, traffic, job or session change occurred in preparing this decision. Explicit owner approval of Alternative 1 and a future attended window are required before implementation or external mutation. No scope deviation implemented.
