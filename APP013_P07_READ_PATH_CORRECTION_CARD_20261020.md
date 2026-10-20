# APP-013 / 3A / P07 — approved local read-path correction

Status: preparation/testing only. Owner selected October 20, 4:00–5:15 p.m. Eastern availability; this is not execution approval. Owner explicitly approved the narrow correction: direct restricted CHILD connection for Job/Tenant checks; CHILD administrator connection only for exact-job, read-only Payment/CalendarOperation absence checks. No grants or memberships are approved.

## Traceability and inspected gap

Section: existing APP-013/3A/P07; existing acceptance remains authentic same-job Sandbox settlement and persisted gate clearance under the unchanged 3A card. Backend source `c426c319c240879dfb7c7ebf2f5aabfa5161c9d7`; governance source `0a27a0fe5ef23f89a8b2718417e3997d295c0c9e`. No application/image source changes.

Expired private repair3 controller lines 145–148 always connect as the administrator, while lines 184–200 attempt SET LOCAL ROLE for the exact job query. Its proposal promises the existing numeric-version-2 restricted connection. The reviewed fixture scripts/fixtures/p06-runtime-role-review.sql and negative tests scripts/verify-p06-runtime-role.mjs forbid Payment/CalendarOperation SELECT and role memberships. Preserve those restrictions. This correction makes the diagnostic connection agree with its described identity; it does not make the payment runtime usable.

## Finite approved behavior

1. Preserve all historical packages/receipts unchanged. Make a distinct, non-launchable local correction copy.
2. Reuse authenticated Cloud subprocess environment, fixed-error/hidden-input patterns, exact job/tenant/query identities, existing numeric child secret version 2, role controls and containment.
3. Read that one child URL only in memory under a later exact external approval. Preserve the documented schema=public and sslmode=verify-full format from APP013_P06_INITIAL_PASSWORD_REVIEW.md; use the existing Node pg certificate-validation pattern (rejectUnauthorized true and exact hostname). Validate scheme, host, port, database, restricted username, password presence, TLS query and absence of unknown query/fragment before connecting. Never expose URL/password in arguments, files, stdout or evidence.
4. Connect as the restricted role itself, verify both current_user and session_user plus database identity, then read only the exact Job/Tenant facts in a repeatable-read read-only transaction and roll back.
5. Use a separate repeatable-read, read-only administrator transaction solely for exact-job/tenant Payment and CalendarOperation zero-count checks; roll back. No role switching, grant, membership, write, token or broad customer lookup.
6. Keep the role lifecycle and mandatory NOLOGIN/limit-zero/expiry/session closeout unchanged. Retain only bounded counts and booleans. Separate connections do not share a database snapshot; these are point-in-time diagnostics, not authorization for later payment mutation. P08 must revalidate its own transactional guards.

Expected local files: controller.py, existing test_controller.py, a restricted-query Node helper/test reusing the existing certificate-validated pg transport, README and manifest in a new private directory. No application interface/schema change. Entry point must refuse external execution; no operation approval file is created.

## Verification and dependencies

Run the existing 19 mocked controller regressions plus meaningful direct-role identity, malformed/foreign credential-target refusal, forbidden-table separation, fixed error privacy, and query/identity mismatch tests. Capture subprocess arguments to prove no credential appears in argv and the direct connection selects the restricted username. Existing one-use and containment tests remain. No live browser/database/provider result is claimed. Required governance frozen-baseline, cross-repository consistency, 25 safeguards, backend governance/architecture and both whitespace checks remain applicable.

Owner owns any later exact external approval and 3A acceptance; implementer owns local correction and evidence. Runtime-role permission planning is a separate newly demonstrated prerequisite: reviewed intake grants exclude policy/pricing updates, Payment and StripeEvent operations required by the current application. No new readiness operation may be called executable until that mismatch is resolved through explicit change control and applicable proof.

Observable local finish: source-hashed correction with passing focused mocks, preserved historical source hashes and a non-executable entry point. Rollback: discard only the new local copy; existing runtime and repositories' application code remain unchanged. No payment, deployment, grants, secrets/provider configuration, charge, customer action or milestone acceptance is included.

Scope status: owner-approved narrow local access-plan deviation only. Larger payment-runtime prerequisite is disclosed and remains unapproved. Counts stay 0/27 newly closed R1 packages, 6/60 legacy packages, 4/8 walkthrough milestones and 0/13 full-intelligence rows.

## Local result

Completed only the explicitly approved correction. Twenty-five Python mocked regressions and three Node certificate-validation/cleanup/refusal tests pass. The source-hashed non-launchable copy and archived source-only diff are indexed by backend evidence/APP-013/p07-read-path-correction-20261020.md. Historical packages are unchanged. Governance frozen-baseline/consistency/25 safeguards, backend governance/architecture and whitespace checks pass. No external action or new permission grant occurred; the dedicated payment-runtime prerequisite remains a separate unapproved proposal.
