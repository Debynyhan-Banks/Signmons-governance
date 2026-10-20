# APP-013/P06 R11 correction-continuation image build proposal

Status: Alternative 1 completed once during the approved October 11 window. Immutable image/source verified; all three temporary grants removed and independently read back absent. No deployment or live journey authorized.

## Section and acceptance traceability

Section: existing APP-013/2B, P06-R11. The unchanged customer criterion is one protected journey that obtains current phone and eligible-address evidence, preserves the reviewed draft and creates exactly one job only through controlled admission. The approved local repair makes the correction continuation portable across instances. An immutable image is the next prerequisite for later deployment review; it is not acceptance, a deployment or a new section.

Acceptance criterion advanced: a corrected, explicitly re-reviewed address can retain the provider continuation across a process replacement while strict binding, privacy, ledger and two-operation limits still fail closed. Inspected evidence: `APP013_P06_R11_CORRECTION_CONTINUATION_DECISION_20261010.md` and backend `evidence/APP-013/p06-r11-correction-continuation-diagnosis-20261010.md`. Local evidence passed 187 focused tests, the full 2,495-test backend suite with three intentional skips, build/lint/architecture, 52 browser cases and the complete disposable PostgreSQL 18 HTTP/browser harness. Those are local results only.

## Exact reviewed source

The tested checkout is intentionally mixed and dirty. Git HEAD `3cf8a9dc53d0282a35e6263a36d749c5b32f8e2e` alone does not identify it. The exact current Docker/build inputs were frozen locally as a deterministic archive:

- archive: `/private/tmp/r11-correction-continuation-review-20261011/source.tar`
- manifest: `/private/tmp/r11-correction-continuation-review-20261011/manifest.json`
- 576 files; 4,599,000 source bytes; 5,048,320 archive bytes
- archive SHA-256: `48ea0a9bb31c439a1fa5f1f8e543c4ecc582edfb21a9e8e741ca2d652b7911e1`
- proposed candidate: `us-east5-docker.pkg.dev/signmons/signmons/signmons-calldesk-backend:p06-r11-cont-48ea0a9bb31c`

Inputs are `.dockerignore`, `Dockerfile`, `cloudbuild.deploy.yaml`, `eslint.config.mjs`, locked package files, Prisma/config, TypeScript/Nest config, `prisma/`, `scripts/` and `src/`. The archive excludes `.git`, environment files, evidence, UI, `node_modules`, `dist`, temporary/private results, `__pycache__` and bytecode. It contains no symlinks or non-regular files; uid/gid/mtime/modes are normalized. An independent verifier matched every archived file to the current checkout. An extracted copy passed `npm run build`, `npm run lint` and `npm run arch:check` using a local copy-on-write dependency tree. The existing Dockerfile and Cloud Build file are unchanged.

The proposed tag is only a name derived from the archive hash. A fresh external preflight must prove it absent before any mutation. If the local archive or current-file match is lost, changed or uncertain, stop and prepare a new review rather than reconstructing this approval.

## Alternative 1 — one immutable image build

After explicit owner approval and a future 45-minute Eastern window:

1. Bind a one-use controller to this document, archive hash/size/file count, candidate tag, exact window and fresh operation identity. Its no-action tests must cover early/late window, existing attempt, source drift, tag collision, failed grant, uncertain submission and cleanup failure.
2. Run one fresh read-only preflight in project `signmons`: existing enabled build identity `signmons-build@signmons.iam.gserviceaccount.com`; bucket `signmons_cloudbuild`; repository `us-east5/signmons`; candidate tag absent; and the three temporary memberships below absent. Any mismatch stops before mutation.
3. Apply only these temporary memberships for that build identity: `roles/storage.objectViewer` on bucket `signmons_cloudbuild`, `roles/artifactregistry.writer` on repository `us-east5/signmons`, and `roles/logging.logWriter` on project `signmons`. Journal each possibly applied grant before mutation.
4. Upload only the reviewed archive and submit exactly one existing `cloudbuild.deploy.yaml` build using the existing Dockerfile, `_IMAGE` set to the candidate, `E2_HIGHCPU_8`, timeout 1,200 seconds and a USD 1 operational allowance. This allowance is an owner decision limit, not a provider-enforced invoice cap. No automatic retry or substitute identity/source/tag.
5. Record build ID, terminal status and the immutable registry digest. Require the submitted source to match the reviewed archive. Do not deploy, tag a Cloud Run service or change traffic.
6. In a mandatory `finally` path after success, failure or uncertainty, remove every possibly applied temporary membership and independently read back all three as absent. Cleanup continues after the normal window if necessary. Preserve a sanitized result and stop.

Observable finish: either one unused immutable image bound to the exact archive plus all temporary memberships verified absent, or one preserved safe stop plus cleanup readback. A successful image advances only release readiness; P06 stays 12/14, R11/full R12 stay open and accepted milestones stay 3/8.

## Alternative 2 — retain the local result

Do not perform cloud work. Keep the local implementation and exact archive review-ready. Runtime stays closed and no acceptance changes.

## Boundaries and next gate

The build reads no application database, secret payload, provider, participant, customer, request or job data. Intended external outputs are one source upload, Cloud Build logs and, on success, one registry image. It creates no runtime identity or customer data. Existing consumed operations and holds remain unchanged.

Excluded: deployment, Cloud Run revision/tag/traffic change, runtime IAM, secret access/version change, database access/write/migration, provider/Twilio read or transaction, verification code/message, browser journey, job/customer action, phone/address hold release or ceiling change, billing-account change, merge and retry.

The current phone ceiling is exhausted at 17 holds / USD 8.50. This proposal neither changes that ceiling nor authorizes a journey. After a successful build, deployment/readiness and any later journey require separate current-state review and explicit approval. A journey also requires an owner-approved prospective phone-ceiling change and a new exact window.

Rollback/disabled state: the candidate remains unused. Mandatory permission cleanup restores the pre-build IAM state. No runtime rollback is needed because this proposal cannot deploy or route traffic.

Owner decision: approve Alternative 1, the exact reviewed archive/tag, one source upload and image creation, the three temporary memberships with mandatory removal/readback, the USD 1 allowance, one submission/no retry and a future 45-minute Eastern window; or choose Alternative 2.

No scope deviation.

## October 11 completed build

The owner approved Alternative 1 and the exact 9:00–9:45 a.m. Eastern window. Plan `3149c991-cdf8-4da0-979c-7c6fe77fd906` / operation `656aa309-c204-4f5f-a9a3-023394097759` passed archive/approval binding plus nine synthetic stop/cleanup tests. Fresh preflight at 9:01:52 a.m. confirmed the existing build identity enabled, source bucket and Docker repository present, candidate tag absent and all three temporary grants absent.

Exactly one submission created Cloud Build `44569641-ba52-4302-bb02-e4194006c979`. It returned `SUCCESS`. Candidate `p06-r11-cont-48ea0a9bb31c` resolved to immutable digest `sha256:69ef032639e5dcfa2bcaaa5d88d0e438ec62903f08cb44fc5572af1209e332d3`, matching the build result and registry readback. Source provenance remained archive SHA-256 `48ea0a9bb31c439a1fa5f1f8e543c4ecc582edfb21a9e8e741ca2d652b7911e1`.

The controller removed storage, artifact-registry and logging memberships and read all three absent at 9:05:58 a.m. An independent post-controller Cloud readback again confirmed build `SUCCESS`, matching registry digest and all three memberships absent. No retry. Actual invoice cost is not verified; USD1 was the approved operational allowance.

The build checklist is complete. The image remains unused. No Cloud Run revision/tag/traffic change, database/secret/provider/customer action, hold/ceiling change, deployment or journey occurred. Deployment/readiness is a separate decision. The last verified pre-enabled39 aggregate was17/USD8.50; enabled39 then exercised the approved18th hold, so17/USD8.50 is stale and a fresh aggregate is required before prospective work. P06 remains12/14, R11/fullR12 remain open and accepted milestones remain3/8. No scope deviation.
