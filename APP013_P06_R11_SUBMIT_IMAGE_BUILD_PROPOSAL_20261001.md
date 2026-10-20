# APP-013 / 2B / P06-R11 — one submission-feedback image build

Status: exact local package prepared; external build decision pending. The owner's latest "i approve" accepts the completed local repair and continuation of preparation. It is not recorded as approval of an unspecified new charge, permission grant, deployment, or another customer journey. No new application implementation is proposed.

## Requirement, artifact and reused evidence

Section2B of APP013_REMAINING_EXECUTION_CONTRACT.md requires reviewed intake with truthful outcome/uncertainty. The approved local feedback repair is complete; the current immutable image lacks it. Packaging those exact tested bytes advances the same connected workflow, but an image alone does not satisfy R11 or prove the historical job outcome.

Archive: /private/tmp/r11-submit-release-review-20261001/source.tar, SHA256 **c7b7312b2b059b5d7bd5ebf2714fe74a3eba17aa5fbb69159556e1f841ab5544**, 4,823,040bytes,558safe sorted regular files. Source checkout /private/tmp/signmons-submit-release-source-20261001, clean commit **a997917892983645fb06d37b1079ed51b31ffb11**. Original archive baseline remains3cf8a9dc53d0282a35e6263a36d749c5b32f8e2e, distinct from this source commit.

556files are byte-identical to previous image-source archive3a28d41ab679add264d3a2c9e930539242a6ecc4d3c5fbb3f2a3c083aa3e2787. Two overlays only: scripts/fixtures/customer-intake-journey.js and scripts/verify-controlled-intake-ui.mjs. Docker runtime copies only the journey JS from that delta; the synthetic test server is not a runtime image asset. No env/private evidence, credentials, dependencies, .git, dist, UI output or unrelated maintenance changes are included.

All archive bytes match this clean source. All runtime/test source matches the validated d7128435f55421438b64150a522c44ddea209df7 snapshot, except the two unchanged historical host coordinator Python files excluded from this image delta and not copied into the runtime stage. No runtime exception. Manifest, exact two-file delta and source-correspondence.json sit beside the archive.

Reuse completed matching-source evidence: native Safari18.6 before/after one synthetic native-click receipt;38UI cases;2467unit tests/three existing skips; build/lint;14loaded connected cases and disposable cleanup. Historical Safari cause remains unconfirmed. No repeat full tests merely for repackaging identical runtime bytes. Backend evidence/APP-013/p06-r11-safari-submit-repair-20261001.md.

Candidate image: **us-east5-docker.pkg.dev/signmons/signmons/signmons-calldesk-backend:p06-submit-c7b7312b2b05**. An immutable digest does not yet exist; no existing digest may be substituted.

## Proposed external action and finite execution card

One build-only window: **October1,2026,12:00p.m.–12:30p.m. America/New_York (16:00–16:30UTC)**. Start before12:05, preserving the existing25minute reserve for a20minute build timeout plus cleanup. If the start cutoff is missed, do not execute or infer an extension. Owner need not provide a password/code or attend a customer journey for this build.

Requested additional operating allowance: **USD1.00** for one source upload, Cloud Build and image publication. This is an operational allowance, not a provider-enforced billing cap or an invoice quote. No increase to phone/address ceilings and no paid customer test.

1. After exact owner approval, bind the existing reviewed build_once.py and its eight synthetic guard tests from /private/tmp/r11-format-build-control-20261001 to this source/archive/tag/window and a fresh exclusive root /Volumes/Signmons-P06/r11-submit-build-20261001-1200. Never reuse the consumed earlier build root. Re-run bound guard tests and local source/approval checks before any external action. If checks fail, stop; no new helper subsystem or safety exception.
2. Fresh bounded read-only preflight: exact project signmons; existing service account signmons-build@signmons.iam.gserviceaccount.com enabled; existing bucket signmons_cloudbuild; existing Docker registry us-east5/signmons; candidate tag absent; all three temporary memberships absent. No secret-value, database, provider or customer-data read. A mismatch stops rather than changing configuration by inference.
3. Explicit proposed temporary grants to that existing identity only: roles/storage.objectViewer on gs://signmons_cloudbuild; roles/artifactregistry.writer on us-east5/signmons; roles/logging.logWriter on project signmons. Journal possible grants before mutation; verify each. No new identity/resource or unrelated membership.
4. Upload only the checked archive contents into the existing source-staging bucket. Run existing Dockerfile/cloudbuild.deploy.yaml once using e2-highcpu-8, timeout1200s and one build submission. Preserve submission attempt and returned build ID. Unconfirmed submission cannot trigger another submit. Poll only that build; match its output digest to the registry candidate digest.
5. On success, failure or uncertainty, remove and independently read back all possibly applied memberships, including cleanup after the window if required. Cleanup failure is a blocker, not authorization to leave access silently. Record final image/source/build/digest and cleanup verdict. No automatic rebuild or allowance reset.

Required checks: eight rebound synthetic build-control cases covering existing window/approval/source/consumed/failure/cleanup guards; actual local no-action source/archive review; governance frozen baseline and complete cross-repository consistency before/after changes; three safeguard test files; backend architecture and whitespace in both repos. Reuse matching runtime evidence above. A frozen-baseline failure is a stop, never an anchor update.

## Boundaries, rollback and finish

Data/state/identity/retention: only the listed source files and existing build identity/resources. Preserve previous images, jobs, audits, request references, holds and consumed operation evidence. Source/upload/build records remain as evidence. Rollback is permission cleanup and leaving the successfully published image unused; no image deletion is required or authorized.

No Cloud Run deployment or traffic/tag change, database LOGIN/activation/read, secret change, Twilio/Google verification, SMS/email, appointment, payment, customer submission, hold release, browser journey or merge. Enabled31 remains closed. The unavailable historical request reference is not manufactured and no broad outcome query is substituted. Any later deployment/test is a separate concrete decision after its requirements are known.

Preparation checklist complete: artifact/inventory/delta, exact source correspondence, existing validation, resource/action/budget/window/cleanup specification. Remaining: owner's scoped build decision, implementer exact binding/checks and one build/cleanup result. Observable finish is a source-matched immutable image with all temporary grants removed/read back absent, or a truthful consumed failure with cleanup evidence. This is build readiness, not a customer capability or acceptance. P0612/14,R11/fullR12open; accepted1A/1B/2A3/8 unchanged.

Explicit proposed scope addition: one USD1.00 build/upload/publication and the three enumerated temporary grants with mandatory removal. None executed. The reviewed local repair is accepted; no scope deviation implemented beyond local packaging.
