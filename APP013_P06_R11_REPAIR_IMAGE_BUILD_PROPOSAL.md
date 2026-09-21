# APP-013 / P06 R11 repair-image build proposal

Status: owner-approved build completed once; cleanup verified; fresh packet prepared under separate read-only authority. Execution remains unapproved.

## Result

The owner approved the exact proposal for 9:15–9:45 AM Eastern. Cloud Build `91773a6b-70dd-4df4-bef6-5cba98b6f5df` was submitted once from the recorded 618-entry source archive and finished `SUCCESS` at `2026-09-21T13:21:35.009490Z`. Registry readback binds tag `p06-r11-1819e84b232b` to immutable digest `sha256:9e9039a3978108067be710532d40b4881a06842b80edd71c029d76632ef11f32`.

The exact three temporary memberships were removed after the terminal result. Bucket, repository and project policy readback found all three absent. No retry, deployment, LOGIN, activation, secret access, provider request or customer action occurred.

The still-current read-only preparation authority then produced fresh private plan `349fb681-ffe6-46dc-8b83-202ebf3cdf71` for enabled12, one 9:25–9:40 AM supervised runtime and closeout by 9:45 AM. Only three mode-0600 preparation files exist; no helper or execution authorization was created. Exact owner execution approval or refusal is next. P06 remains 12/14 with R11/full R12 open. No scope deviation.

## Pre-execution demonstrated prerequisite

Read-only refresh for the owner-selected 9:15–9:45 AM Eastern block found no immutable registry image containing backend repair `1819e84b232bf98112c44fc52641b788b35b8b38`. The newest image is the September 15 artifact from source `53037fbd118c`; enabled11 uses it and therefore lacks the category-ID repair. Binding a fresh R11 packet to that image would repeat the proven pre-address 409.

## Approved bounded action

- Build exactly clean committed backend source `1819e84b232bf98112c44fc52641b788b35b8b38` with existing `cloudbuild.deploy.yaml` and `Dockerfile`.
- Push only `us-east5-docker.pkg.dev/signmons/signmons/signmons-calldesk-backend:p06-r11-1819e84b232b`; do not deploy it.
- Use existing enabled `signmons-build@signmons.iam.gserviceaccount.com`, `E2_HIGHCPU_8`, 1,200-second timeout, existing `signmons_cloudbuild` source bucket and a USD1 operational allowance. The allowance is not an invoice or hard billing cap.
- Temporarily grant only `roles/storage.objectViewer` on `signmons_cloudbuild`, `roles/artifactregistry.writer` on repository `us-east5/signmons`, and `roles/logging.logWriter` on project `signmons`. Remove and read back all three immediately after terminal success or failure.
- One submission only. No automatic retry. Retain only source/build/image provenance and privacy-safe cost/status evidence.
- After a successful immutable digest readback, the already authorized preparation may create a fresh R11 packet only if its preparation window is still current; otherwise stop for a new window.

## Pre-execution verified source and state

Before execution, backend was clean at `1819e84`; focused 145 tests, full 2,360 tests/3 skips, build, lint, architecture and disposable PostgreSQL 18/browser checks passed. The local Docker-input archive had 618 entries, 4,710,400 bytes and SHA-256 `2132b8c0e1f8904a2afd9ca92cb78e2e06439af52c24403dfa3e9aa7c14d8ad5`; it had not yet been uploaded. The build identity was enabled and had no direct matching project binding, bucket grant or repository binding.

## Exclusions and stop rules

No deployment, Cloud Run traffic/tag/configuration change, secret access/change, database LOGIN or mutation, activation, provider request, verification code, browser/customer action, job creation, payment, booking, dispatch or message. A failed submission or incomplete cleanup stops; it is not retried. Packet and execution authority remain separate.

## Owner decision (completed)

The owner approved the exact one-attempt build and temporary IAM sequence for the current window. The Result section records the completed outcome. Packet execution remains a separate decision. P06 remains 12/14 with R11/full R12 open. No scope deviation.
