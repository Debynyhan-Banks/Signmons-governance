# APP-013/P06 R11 startup-stage repair image decision

Status: review-ready decision; exact owner build approval and a future window are absent. No build, upload, cloud read, IAM change, deployment, packet or live action is authorized by this document.

## Section and acceptance traceability

Section: existing APP-013/2B, P06-R11. The user-observable criterion remains one protected customer journey that obtains current phone access and eligible address evidence, preserves the reviewed draft and creates exactly one job only through the existing controlled admission. Enabled27 failed before serving that journey. The locally complete fixed-stage diagnostic is a prerequisite for identifying a future startup failure; it is not a new acceptance section, a repair of the original unknown gate or live customer evidence.

Current source: backend `fe9b0661224a24969679dea5606dadbdc033c224`; governance `bc97bb7d73e1f73e28577a1427e700b7ce9e6ae0`. Backend evidence `evidence/APP-013/p06-r11-startup-stage-observability.md` records 56 focused tests, 2,400 full unit tests with three existing skips, lint/build/architecture/schema, the complete disposable PostgreSQL/browser regression, 21 governance safeguards and independent review. Those are prior local results and are not restated as new runtime validation.

## Exact candidate and local input review

Candidate tag: `us-east5-docker.pkg.dev/signmons/signmons/signmons-calldesk-backend:p06-r11-fe9b0661224a`.

The exact source revision was locally archived from Git using only `.dockerignore`, `Dockerfile`, `cloudbuild.deploy.yaml`, `package.json`, `package-lock.json`, `prisma/`, `prisma.config.ts`, `tsconfig.json`, `tsconfig.build.json`, `nest-cli.json`, `scripts/` and `src/`. The review archive contains 557 files / 4,343,122 bytes and has SHA-256 `2d6742d399cf97aeda131988af1f28e152c8588f7ba0c8dc5b7e5f691b9856d4`. It excludes `.git`, untracked `tmp/`, evidence, UI, `node_modules`, `dist`, environment files and private operation results. The archive is local review material only; nothing was uploaded.

The existing Dockerfile uses Node 22 Bookworm slim, installs from the locked package files, validates/builds the application and copies only the production package, pruned dependencies, compiled application, Prisma files and the two reviewed customer-intake assets into the runtime stage. The existing Cloud Build file performs one Docker build/push of the supplied `_IMAGE` with Cloud Logging only. No new dependency, schema, startup setting, secret reference, route, provider call or runtime authority is introduced.

## Alternative 1 — one fixed-source diagnostic image build

After the owner selects a future bounded window and explicitly approves this alternative:

1. Run a fresh read-only preflight for the existing build identity, `signmons_cloudbuild` bucket, `us-east5/signmons` repository, exact candidate tag and the three temporary memberships below. Require the source SHA/archive hash above, enabled build identity, candidate tag absent and temporary memberships absent. Any mismatch stops before mutation.
2. Submit exactly one build from the reviewed archive, existing `cloudbuild.deploy.yaml` and `Dockerfile`, with `E2_HIGHCPU_8`, timeout 1,200 seconds and a USD 1 operational allowance. The allowance is a decision ceiling, not a provider-enforced billing cap. Do not start unless the selected window leaves time for mandatory cleanup.
3. Push only the candidate tag above. Record the build ID, exact source/archive provenance, terminal result and immutable digest. Do not deploy, tag a Cloud Run service or change traffic.
4. Temporary grants only for the existing build identity: `roles/storage.objectViewer` on bucket `signmons_cloudbuild`, `roles/artifactregistry.writer` on repository `us-east5/signmons`, and `roles/logging.logWriter` on project `signmons`. Track success or ambiguity for each mutation; remove and read back all three after success, failure or uncertain submission. Cleanup remains mandatory after the normal window expires.
5. One submission, no automatic retry. Preserve the result and stop on uncertainty. Do not reuse any consumed operation, packet, helper, revision suffix or approval.

Finish: either one immutable image/source binding plus verified removal of all temporary grants, or a preserved safe stop with cleanup readback. Image success would make the fixed startup stage observable in a separately authorized future startup; it would not prove enabled27's original cause, a successful runtime or APP-013 acceptance.

## Alternative 2 — retain the local result

Do not build. Keep `fe9b066` and its local evidence review-ready while the runtime remains closed.

## Boundaries, tests and next gate

Data/state/identity/retention: a build reads no database, provider, participant, customer or secret value. It uploads only the reviewed tracked source archive and writes build logs plus one registry image if successful. Existing project/build identity is reused; no runtime identity is activated. No customer retention rule changes. Mandatory cleanup removes only the three temporary memberships applied for this exact build.

Positive path: exact preflight, one successful build, exact tag/digest readback and zero remaining temporary memberships. Negative/recovery paths: source/tag/identity/membership mismatch stops before mutation; failed or uncertain build still executes grant cleanup and records one-attempt evidence; cleanup ambiguity stops every later action. Browser/database/runtime tests are not applicable to this documentation-only decision and must not be represented as newly run. Before any approved build, the execution controller/helper must be source-, archive-, approval- and window-bound and pass local no-action tests.

After any successful image build, a separately approved read-only qualification must refresh Cloud target/baseline, provider, participant, policy, approval, closed-role/session and retained-liability state before a new packet can even be proposed. A packet, LOGIN, activation, deployment, traffic/tag change, provider request/code, browser/customer action and closeout are each outside this decision.

Exclusions: database access or migration, secret access/change, runtime IAM, billing-account changes, hold release or ceiling change, packet preparation, deployment, activation, provider configuration/request, verification code, browser QA against a live revision, customer/job action, retry and merge. Preserve all prior holds and consumed operations.

Rollback/disabled state: no repository runtime behavior changes in this decision. If alternative 1 is later approved, the candidate image remains unused unless a different exact approval authorizes deployment. Prior verified shutdown remains the last runtime evidence.

Relative size/confidence: small, high-confidence one-build operation after fresh preflight; external state and cleanup still require current readback. Owner decides alternative 1 or 2 and, for alternative 1, supplies the exact future window. Implementer owns the bounded build and cleanup only after that approval.

P06 remains 12/14; R11 and full R12 remain open; accepted 1A/1B/2A remain 3/8 (37.5%). This is not an overall MVP completion percentage. No scope deviation.
