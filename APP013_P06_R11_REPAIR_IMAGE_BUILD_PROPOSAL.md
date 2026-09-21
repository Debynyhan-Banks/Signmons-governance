# APP-013 / P06 R11 repair-image build proposal

Status: owner decision required. This is not build, packet or execution authority.

## Demonstrated prerequisite

Read-only refresh for the owner-selected 9:15–9:45 AM Eastern block found no immutable registry image containing backend repair `1819e84b232bf98112c44fc52641b788b35b8b38`. The newest image is the September 15 artifact from source `53037fbd118c`; enabled11 uses it and therefore lacks the category-ID repair. Binding a fresh R11 packet to that image would repeat the proven pre-address 409.

## Proposed bounded action

- Build exactly clean committed backend source `1819e84b232bf98112c44fc52641b788b35b8b38` with existing `cloudbuild.deploy.yaml` and `Dockerfile`.
- Push only `us-east5-docker.pkg.dev/signmons/signmons/signmons-calldesk-backend:p06-r11-1819e84b232b`; do not deploy it.
- Use existing enabled `signmons-build@signmons.iam.gserviceaccount.com`, `E2_HIGHCPU_8`, 1,200-second timeout, existing `signmons_cloudbuild` source bucket and a USD1 operational allowance. The allowance is not an invoice or hard billing cap.
- Temporarily grant only `roles/storage.objectViewer` on `signmons_cloudbuild`, `roles/artifactregistry.writer` on repository `us-east5/signmons`, and `roles/logging.logWriter` on project `signmons`. Remove and read back all three immediately after terminal success or failure.
- One submission only. No automatic retry. Retain only source/build/image provenance and privacy-safe cost/status evidence.
- After a successful immutable digest readback, the already authorized preparation may create a fresh R11 packet only if its preparation window is still current; otherwise stop for a new window.

## Verified source and current state

Backend is clean at `1819e84`; focused 145 tests, full 2,360 tests/3 skips, build, lint, architecture and disposable PostgreSQL 18/browser checks pass. The local Docker-input archive has 618 entries, 4,710,400 bytes and SHA-256 `2132b8c0e1f8904a2afd9ca92cb78e2e06439af52c24403dfa3e9aa7c14d8ad5`; it has not been uploaded. Current build identity is enabled and has no direct matching project binding, bucket grant or repository binding.

## Exclusions and stop rules

No deployment, Cloud Run traffic/tag/configuration change, secret access/change, database LOGIN or mutation, activation, provider request, verification code, browser/customer action, job creation, payment, booking, dispatch or message. A failed submission or incomplete cleanup stops; it is not retried. Packet and execution authority remain separate.

## Owner decision

Approve this exact one-attempt build and temporary IAM sequence for the current window, choose a later window, or decline. P06 remains 12/14 with R11/full R12 open. No scope deviation proposed.
