# APP-013 / 2B / P06-R11 — refusal-category release proposal

## Decision status

Decision-ready proposal prepared October 2, 2026. It is not executable authority. No cloud query, database connection, build, source upload, IAM change, image publication, deployment, provider request, verification message, browser journey, allowance change or customer/job action occurred during preparation.

The consumed enabled33 operation remains closed and may not be retried. This proposal describes one new source-bound build and, only after every gate passes, one new attended staging journey followed by mandatory shutdown. The owner must approve the complete fixed scope and provide a future 75-minute Eastern window before execution artifacts may be prepared.

## Approved section and acceptance criterion

- Section: APP-013 / 2B / P06-R11, with R12 containment and reconciliation.
- Existing criterion: one correlated protected phone-verification, eligible-address and reviewed-submit journey creates exactly one job and returns an authoritative receipt; invalid, stale or ineligible input returns a truthful no-job result while preserving recoverable customer progress.
- Purpose: release the already owner-approved four-category refusal repair so a new connected result identifies the safe refusal class instead of collapsing recoverable causes into generic `REFUSED`.
- This does not add an acceptance section, change service-area policy, authorize a customer claim or award R11 acceptance in advance.

## Exact source and artifact

- Deployed parent source: `0a857edcc88a6da36dc6669382a74546173e480b`.
- Isolated candidate: `/private/tmp/signmons-refusal-category-release-candidate-20261002`.
- Candidate commit: `8f27952ceaae4f68d5ea7244ccc9b7dbdbcf6d7f`.
- Candidate tree: `2e2087088f8ec4089f6ce528e0f5e617054017d0`.
- Candidate archive: `/private/tmp/signmons-refusal-category-release-8f27952.tar.gz`.
- Archive SHA-256: `d8e9e4d5488ca86820497916581c634b8613703996774b7efa3b46b2d0b79250`.
- Archive size: `1000310` bytes; an independent readback archive is byte-identical.
- Proposed image tag: `us-east5-docker.pkg.dev/signmons/signmons/signmons-calldesk-backend:p06-r11-refusal-d8e9e4d5488c`.

The candidate has exactly six changed files versus the deployed parent, 156 insertions and 12 deletions:

- `src/communications/controlled-intake-verification.service.ts`
- `src/communications/controlled-intake-verification.service.spec.ts`
- `src/communications/controlled-intake-browser-result.ts`
- `src/communications/controlled-intake-browser-result.spec.ts`
- `scripts/fixtures/customer-intake-journey.js`
- `scripts/verify-controlled-intake-ui.mjs`

All six candidate files byte-match the locally tested repair. The committed archive contains 561 tracked files and excludes `.git`, dependencies, compiled output, evidence, temporary files, environment files and private key material. Standard tracked modes were verified. The archive must be rehashed immediately before upload; mismatch stops.

## Existing components and expected interfaces

- Reuse the existing `Dockerfile`, `cloudbuild.deploy.yaml`, controlled-intake service, browser result projector, same-page customer journey, controlled runtime configuration, liability readers, database window controller, provider qualification, no-traffic deployment, attended coordinator and mandatory closeout.
- Normal revision remains at 100% traffic; the candidate receives a unique zero-traffic tag only.
- Existing tenant, session, phone-proof, request and job identities remain correlated. Private credentials and phone codes stay in owner-operated hidden entry and never enter receipts.
- The repair adds only four allowlisted responses: `ADDRESS_REVIEW_UNAVAILABLE`, `SERVICE_AREA_NOT_CONFIRMED`, `OUTSIDE_SERVICE_AREA` and `ADDRESS_CORRECTION_STATE_UNAVAILABLE`.
- It does not retain provider payloads, county values, tokens or response identifiers; change admission, coverage, retry, matching or retention policy; release historical holds; or grant delivery, dispatch, payment or appointment authority.

One new journey may create at most one job. A no-job, uncertain or ambiguous result stops without a second submission. Existing operation/liability history remains retained. Closeout revokes approval, removes the test tag, returns the database role to `NOLOGIN`/limit zero/zero sessions and reads normal traffic back at 100%.

## Proposed build and temporary access

After approval and inside the future window, use one Cloud Build only in project `signmons`, region `us-east5`, with the existing build files, machine `e2-highcpu-8`, timeout 1200 seconds and service account `signmons-build@signmons.iam.gserviceaccount.com`.

The build may temporarily receive only:

1. `roles/storage.objectViewer` on `gs://signmons_cloudbuild/source`.
2. `roles/artifactregistry.writer` on Artifact Registry repository `us-east5/signmons`.
3. `roles/logging.logWriter` on project `signmons`.

Every grant is journaled, removed on success, failure or uncertainty, and read back absent. Ambiguous build submission consumes the attempt and does not authorize another. Save the immutable digest, build ID/status, source hash, build identity and grant-removal evidence before release qualification.

## Fresh gates and proposed bounds

Before any grant, upload, build, database `LOGIN`, activation or provider message, read-only qualification must confirm project/service/region, normal revision and 100% traffic, absent target collision, disabled runtime, exact secret versions, approved provider account/service and approved test recipient.

The last saved pre-LOGIN enabled33 baseline was 13 phone holds/USD 6.50 and overlapping address account/tenant 8 operations/USD 0.80. Enabled33 then accepted one phone code and reached a generic no-job result. Therefore 14/USD 7.00 phone and 9/USD 0.90 address are expected post-run values, not confirmed current facts. A fresh exact liability read is mandatory; unexplained mismatch stops before build or mutation.

Subject to exact qualification, proposed prospective limits retain all history and permit only one new journey:

- phone: 15 holds/USD 7.50, one new phone flow, no resend;
- overlapping address account and tenant: 11 operations/USD 1.10;
- address session: existing 2 operations/USD 0.20;
- operating allowance: USD 3.70 total — build 1.00, staging runtime 2.00, phone 0.50 and up to two address checks 0.20.

These are stop limits, not an invoice claim or provider billing guarantee. No hold reset, deletion, balance rewrite or implicit increase is allowed.

## Finite 75-minute sequence

1. Recheck hashes, clean manifest and governance gates.
2. Perform fresh read-only cloud/provider/liability qualification; stop on drift or uncertainty.
3. Add/journal three build grants, submit exactly one build and capture immutable success evidence.
4. Remove/read back all three grants even on failure or uncertainty.
5. Qualify the image and bind a fresh packet to proposed unused suffix `enabled34`; collision requires a new proposal, not silent renaming.
6. Owner privately enters the database password. Activate the bounded plan, enable runtime and deploy the candidate with zero traffic; read back config, image and readiness.
7. Owner uses the approved test phone, privately enters the code, reviews the address/request and submits once. No resend, replacement request or automatic retry.
8. Save only the allowlisted correlated outcome: authoritative one-job receipt or truthful fixed refusal/uncertainty category.
9. Revoke approval/ceilings, remove tag, restore `NOLOGIN`/limit zero/zero sessions and normal traffic 100%, reconcile liabilities and save `CLOSED`. Closeout runs on success, refusal, timeout, error or uncertainty.

Allocate 30 minutes to qualification/build and 45 minutes to the coordinator, including a 15-minute runtime and at least 15 minutes for shutdown. Exact Eastern/UTC timestamps, cutoffs and operation IDs are created only after a future window is approved.

## Tests and evidence

Full repair validation already passed: focused 136, full Jest 2,486 with three existing skips, 46 browser cases at 390/1440, complete disposable PostgreSQL18/database/browser harness, lint, build, architecture, syntax, formatting and verified cleanup.

Candidate validation passed exact six-file byte comparison, focused 136, lint, architecture, syntax/formatting and build. The first candidate build check failed only because a temporary symlink resolved TypeScript types outside the candidate; a candidate-local dependency tree made unchanged source pass. This setup artifact is disclosed and is not a source fix.

Before execution repeat archive/manifest checks, focused tests, build, architecture, governance baseline/consistency, whitespace and packet/controller bindings. During execution save build/IAM readbacks, digest, pre/post liability/runtime readbacks, browser result, authoritative job reference if any and closeout receipt.

## Owners, exclusions, rollback and finish

- Owner: approve/reject the complete operation, choose a future 75-minute Eastern window, confirm approved test phone, enter private password/code and operate browser review.
- Implementer: preserve artifact/limits, perform gates, prepare the checked one-shot package, supervise outcome, stop on ambiguity and complete/read back shutdown.
- Excluded: production traffic, other customer contact, payment/Stripe, appointments, Eternity work, provider-setting changes, production migration, secret rotation, training, hold release/reset and any second journey.
- Rollback: remove temporary grants/artifacts as applicable and leave normal traffic/runtime unchanged on pre-runtime failure. After deployment remove the zero-traffic tag, revoke activation/ceilings, disable runtime access and preserve the prior normal revision at 100%.

Observable finish is one authoritative correlated job or fixed truthful refusal, followed by exact reconciliation and verified `CLOSED`. Only an authoritative job can satisfy R11; owner review remains required. Approval is pending. P06 remains 12/14; R11/full R12 remain open; accepted 1A/1B/2A remain 3/8. Explicit prospective external scope is proposed before action; no scope deviation implemented.
