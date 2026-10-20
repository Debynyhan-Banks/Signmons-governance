# APP-013 / P06-R11 verified production credential cutover decision

## Status

The owner approved the narrowed cutover scope on 2026-10-07. Package preparation may proceed after an attended 90-minute Eastern window is supplied. No cutover mutation is authorized until the finished window-bound package receives exact execution approval.

The current Neon production Connect credential was validated once at `2026-10-07T23:20:06.069806Z`: exact metadata match, direct `ACCEPTED`, pooled `ACCEPTED`. The one-use diagnostic is consumed and no pgpass remains.

## Current read-only inventory

Fresh Google Cloud readback on 2026-10-07 shows:

- normal traffic and `app013-bounds` are 100 percent on `signmons-calldesk-staging-app013bounds`;
- `app013-db-rotation` points at failed revision `signmons-calldesk-staging-app013dbrot1` with zero traffic;
- `p06-intake-disabled` points at `signmons-calldesk-staging-app013p06disabled` with zero traffic;
- no enabled P06 tag exists;
- baseline image/digest remains `us-east5-docker.pkg.dev/signmons/signmons/signmons-calldesk-backend@sha256:37286933d882466b8592120f48eb69c34e14cdb5a23c1f37480e39a1e6ff933a`;
- baseline `DATABASE_URL` and migration-job `DATABASE_URL` both reference `signmons-staging-database-url:latest`;
- shared versions 2 and 3 are enabled and version 1 is disabled;
- child secret version 2 remains enabled and version 1 destroyed;
- latest migration execution is still `signmons-calldesk-migrate-jrq7h`, created `2026-09-07T22:42:05.899388Z` and completed `2026-09-07T22:42:33.570408Z`.

No secret payload was read. No cloud setting changed during reconciliation.

## Narrowed recommended operation

The demonstrated password and host ambiguity is resolved. Previous owner resets and obsolete-tag removal are not repeated. The next operation is limited to:

1. Run a fresh exact read-only preflight against the inventory above and bind the latest migration execution identifier/timestamp.
2. Through hidden owner input, accept the complete current production pooled Connect URL. Revalidate exact scheme, current `.c-5` pooled host, port, role, database, TLS/query metadata and `SELECT 1` before mutation.
3. Add that exact URL as one new numeric version of existing secret `signmons-staging-database-url`. Never display, log or persist the URL outside Secret Manager input; do not change the child secret.
4. Clone immutable `app013bounds`, changing only `DATABASE_URL` from `latest` to the new numeric version. Deploy a fresh named revision at zero normal traffic with a temporary candidate tag.
5. Require Cloud Run Ready, exact configuration diff and HTTP 200 database-backed `/health/readiness` on the zero-traffic candidate.
6. Pin only the migration job's `DATABASE_URL` reference to the same numeric version. Preserve its image, command, arguments, service account, retries and timeout; prove execution identity/count/timestamp did not change.
7. Move normal traffic and `app013-bounds` to the verified revision; remove the temporary candidate and stale `app013-db-rotation` tags; preserve `p06-intake-disabled`; create no enabled intake tag.
8. Use the verified credential for metadata-only session inspection. Wait for or terminate only sessions proven to predate the production reset and belong to stale application revisions; unknown ownership stops broad termination.
9. Disable shared versions 2 and 3 only after all service/job/traffic/session readbacks pass. Do not destroy any version.
10. Final readback proves numeric secret pinning, readiness, unchanged job execution, normal traffic, exact tags, child secret preservation, disabled old versions, and no credential in artifacts.

## Stop and rollback boundaries

- Any inventory drift, URL mismatch, auth refusal, ambiguous secret version, non-one-field revision/job diff, failed readiness, job execution, traffic/tag mismatch, session uncertainty, or incomplete readback consumes that stage and stops without retry.
- Before traffic cutover, normal traffic remains on the baseline. A newly added secret version or zero-traffic candidate may be left enabled/tagged only long enough for explicit reconciliation; no blind cleanup.
- After cutover, rollback may use only a separately verified revision pinned to the new numeric version. Never return traffic to a `latest`, version 2 or version 3 consumer.
- Controlled intake remains disabled. No customer request, phone/address call, message, appointment, payment, charge, migration execution, IAM grant or production deployment is included.

## Owners and observable finish

- Owner has approved the narrowed scope; owner still supplies a future attended 90-minute Eastern window, exact finished-package execution approval, copies the current Neon URL only after the hidden prompt appears, and retains credential custody.
- Implementer prepares/tests the one-use coordinator, performs fresh preflight, executes only approved Google mutations, records sanitized receipts and completes mandatory closeout.
- Finish is `R11_DB_AUTH_RECOVERY_VERIFIED` plus exact Cloud Run, job, secret-version, session and tag readbacks. This restores the staging prerequisite only; APP-013/2B remains unaccepted and the walkthrough remains 3/8.

No scope deviation from the approved credential-containment purpose. The sequence is narrowed to current demonstrated state.

## Approved preparation window and package binding

The owner selected 7:45-9:15 p.m. Eastern on 2026-10-07, with the first external preflight starting before 8:15 p.m. Plan `ffcaf1f0-6c0d-4ac8-9358-52bdae15f000`; operation `3db3aa7d-974f-466e-a536-b5330be53afa`; private root `/private/tmp/r11-db-auth-recovery-20261007-1945`; replacement revision `signmons-calldesk-staging-app013dbrot2`; temporary tag `app013-db-recovery`.

The coordinator reuses the current exact baseline clone/readiness/job/cutover/session/version controls. It accepts the complete pooled Connect URL twice through hidden input: once to authenticate both endpoints and add one secret version, and once for the metadata-only old-session check. The URL is never placed in argv, logs, evidence or repository files and is overwritten after each stage. Every mutation has an exclusive attempt/result/stop marker and no automatic retry.

Package preparation and checks do not authorize execution. The installed source hash, modes, test results and exact stage commands must be presented for fresh finished-package approval before preflight or mutation.

## Prepared package evidence

The final coordinator SHA-256 and installed copy SHA-256 are both `d70c4090cf49676d8282bea6614b3ad355dd332925bf1e0967803d5f212504c7`. The private root is mode 0700; coordinator mode is 0700; test, procedure and proposed-approval files are 0600. No action/result/stop marker exists.

Five focused fictional tests, Python compilation, architecture, backend governance-baseline/consistency, governance frozen-baseline/consistency/21 tests and whitespace checks pass. Exact stages are check, preflight, verify/add secret, zero-traffic deploy/readiness, job reference update, traffic cutover, session check, disable invalid versions and final readback. Execution remains unapproved pending exact owner approval of this installed package.

## Verified execution and independent closeout

The owner approved the exact installed package. Every stage completed once without a stop marker, ending `R11_DB_AUTH_RECOVERY_VERIFIED` at `2026-10-08T00:20:58.000137Z`.

- new shared version4 enabled; versions2/3 disabled-not-destroyed; version1 remains disabled;
- exact baseline clone `signmons-calldesk-staging-app013dbrot2` references numeric version4 and returned readiness200;
- normal traffic and `app013-bounds` are100% dbrot2; only preserved `p06-intake-disabled` remains at zero traffic;
- migration job references version4, execution count remains7, latest execution remains September7 `signmons-calldesk-migrate-jrq7h`;
- pre-reset owner session count is0;
- child secret version2 remains enabled and unchanged;
- independent live readiness returned200 and JSON artifact credential-pattern scan returned absent.

The package/stages are consumed and must never be rerun. Credential containment is complete. R11/2B and full R12 remain open; accepted baseline remains3/8. No scope deviation.
