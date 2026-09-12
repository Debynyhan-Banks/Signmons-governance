# Disabled phone-only deployment proposal — 2026-09-12

Status: PROPOSED, RELEASE NOT AUTHORIZED. Owner-approved worker correction is implemented in backend d33ecd0 (existing PR #21). This supersedes the historical source and implementation-approval recommendation below. Build the corrected commit, not 16e0af8/ad909c8, and require BACKGROUND_WORKERS_ENABLED=false on the candidate before startup. Code tests passed; deployed settings and behavior remain unverified. Build/IAM/spend/deployment approval is still required.

## Fixed target and intended operation

Backend source 16e0af8 (runtime implementation ad909c8), existing focused PR #21. Project signmons, region us-east5, service signmons-calldesk-staging, existing signmons-calldesk-runtime service account. Build one image through cloudbuild.deploy.yaml, record its digest and deploy by digest as a separately tagged candidate with zero normal traffic. Proposed tag phone-preflight; do not move current traffic or webhook URLs. Confirm source/branch has not changed before execution.

Pin signmons-staging-phone-session-key/1 and signmons-staging-phone-digest-key/1. Do not rotate existing credentials. Candidate STAGING_PHONE_TEST_ENABLED=false, SMS_DELIVERY_ENABLED=false, SCHEDULING_ENABLED=false, DEV_AUTH_ENABLED=false; retain Stripe test-mode enforcement. Operator stays disabled and isolated tenant suspended. No test policy, session token or provider request. No migration or database-schema change authorized.

## Newly identified blocker: background database writers

Backend src/logging/call-log.cleanup.ts registers an unconditional EVERY_30_MINUTES job. It scans communication content across tenants and can create session_closed events/content. It is not controlled by SCHEDULING_ENABLED.

src/communications/sms-delivery.worker.ts registers a 60-second interval and calls intents.processDue() before delivery.processDue(). The delivery flag guards delivery.processDue(), not the worker's prior enqueue-recovery operation. Therefore a candidate using the shared staging database can perform unrelated database writes despite zero normal traffic, a suspended test tenant and disabled outbound SMS.

This corrects earlier statements that no additional deployment-safety code was needed. No adverse event was observed; the issue was found by read-only code inspection. No candidate was built or deployed. Do not bypass this with extreme timer values, invalid database credentials, or an assumption that zero traffic means no background execution.

Recommended smallest correction: one explicit candidate background-worker disable control covering both registered scheduled services, checked before any database operation. Preserve existing behavior for current deployments. Add focused tests proving the disabled candidate makes zero worker database/provider calls and existing enabled behavior remains unchanged. This is a bounded release-safety correction within current APP-013/2B, not a new feature or milestone. Seek owner approval before implementation because this turn prepares a proposal, not a new code section. An isolated database is an alternative but is a larger infrastructure change, not assumed approved.

## Proposed temporary permissions, not granted

The existing signmons-build@signmons.iam.gserviceaccount.com is disabled. Its project-role bindings and Artifact Registry resource grants are absent; source bucket signmons_cloudbuild has only legacy project-level groups in the inspected policy.

For one separately approved build: temporarily enable that build account; grant roles/logging.logWriter at project signmons, roles/artifactregistry.writer only on repository signmons in us-east5, and roles/storage.objectViewer only on bucket signmons_cloudbuild. Use the existing authorized submitting/deploying principal; no new broad Owner/Editor or token-signing grant. If submitter actAs or another permission is missing, stop and name it rather than widening access. Remove only grants added by this operation and disable the build account afterward. Preserve any newly discovered pre-existing grants.

## Cost proposal

Official Cloud Build pricing checked September 12 lists e2-highcpu-8 default-pool build compute at USD 0.0156/minute. A single explicitly selected build with a 20-minute timeout has up to USD 0.312 of that compute component; no automatic retry. This excludes storage, transfer, logs, taxes and candidate runtime costs. Do not claim the free allowance remains available. Source: https://cloud.google.com/build/pricing

Proposed overall incremental deployment allowance: USD 2.00, subject to owner approval. This is an operational budget, not a provider-enforced invoice cap. Use request-based Cloud Run billing, no candidate minimum instances and a candidate maximum of one where supported without altering serving revisions. Inspect effective settings before proceeding. Startup/readiness requests and image/source retention can still cost money; no exact all-in guarantee. Sources: https://cloud.google.com/run/pricing and https://cloud.google.com/artifact-registry/pricing

## Acceptance and stop

After the worker blocker is resolved and explicit build/deployment/IAM/spend approval is obtained: rerun applicable gates; build once; verify immutable digest; deploy only the disabled tagged candidate; check liveness/readiness, refusal of phone operations, no background writes and unchanged normal traffic/webhooks. No database migration, identity activation, session issuance, OTP, payment, appointment or production action. Capture rollback disposition and remove temporary build access.

The paid phone test remains a later explicit activation approval with private participant ending 3183 and exact short UTC window. Walkthrough remains 3/8 accepted (37.5%), not overall MVP completion. This proposal neither adds a milestone nor authorizes future product work.
