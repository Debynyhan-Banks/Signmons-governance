# APP-013/P06 R11 startup-stage observability change request

Status: proposed; owner decision pending. No application change is implemented.

## Demonstrated gap and traceability

Approved read-only diagnostic a087c5c8-8162-4d95-96ef-4739de9e0198 completed with14 historical records. Enabled27 emitted CONTROLLED_INTAKE_STARTUP_UNAVAILABLE and BOOTSTRAP_INITIALIZATION_FAILED at13:00:20Z, followed by listener failure at13:00:31Z. Source shows startup.ts101–106 and runtime.ts278–280 discard all underlying causes. Thus the failing startup check is unavailable even after a successful log query. The exact startup cause remains unknown. Evidence: backend `evidence/APP-013/p06-r11-enabled27-startup-classification.md`.

Section: existing APP-013/2B, P06-R11, serving the current connected-runtime criterion in APP013_P06_RUNTIME_WIRING_CARD.md: one protected customer journey obtains current phone access and eligible address evidence, preserves the reviewed draft and creates exactly one job only through existing controlled admission. This diagnostic change unblocks investigation of the startup prerequisite; it is not customer acceptance or a new acceptance section.

Source inspected: backend4cd5392/governance041893d; actual runtime6d8ba54. main.ts, controlled-intake-startup.ts/runtime.ts, startup/runtime specs and loaded-browser harness have no diff from that runtime source.

## Alternative 1 — local implementation and tests only

Add fixed, allowlisted startup-stage evidence through the existing startup/logging seam. Distinguish envelope/configuration, injected-material validation, packaged assets, resource construction/runtime loading, first current-runtime-approval transaction, current-authority transaction, later binding construction and registration. Select a small fixed representation; do not serialize an exception or expose its cause. Preserve the existing generic public exception, startup refusal before listen, key-buffer clearing, runtime retirement and application close behavior.

Reuse `src/communications/controlled-intake-startup.ts`, `controlled-intake-runtime.ts`, their existing specs and the LoggingService/main startup seam. Expected edits are those two modules/specs, with a narrowly scoped main/logging connection only if needed. A tiny shared typed stage definition is permitted if required; no general telemetry system, dependency, database schema, API/route, new harness or feature flag. The implementation card must pin source and the final fixed stage names before coding. Do not weaken any identity, digest, current-policy, expiry, approval or budget check to make startup pass.

Data/state/identity/retention: diagnosis is emitted only on startup failure, before customer ingress. It contains a fixed event and fixed stage only, without runtime IDs, tenant/participant/account identifiers, paths, environment values, digests, keys, phone/address/email, SQL, error strings or stack/cause data. No customer state is read or written for diagnosis. Reuse existing configured log handling; add no sink, retention setting, secret lookup or provider call. Logger failure must not expose the original cause, bypass refusal or prevent zeroization/closeout.

Finite checklist:

1. Complete the source-bound section card, exact stage mapping and expected interface before implementation.
2. Implement the smallest stage-only failure reporting in existing startup/runtime seams; preserve all guards and failure behavior.
3. Reuse and extend startup/runtime tests for disabled/success behavior and each failure stage, including logger failure, stale/refused authority and secret-bearing synthetic errors. Verify no raw private values, causes or paths are emitted; verify cleanup and no listener/provider action after failure.
4. Exercise actual loader and current authority through the existing disposable local PostgreSQL/loopback browser harness with synthetic providers. No live database or real credentials. Preserve existing race/revocation/recovery behavior; add focused tests only where the diagnostic change affects it. Repeated startup failures must not become retries or customer operations.
5. Run relevant focused tests, full unit regression, lint, local build, architecture, schema validation and existing local database/browser gates; required governance baseline/docs/21 safeguard tests and both whitespace checks. Record local evidence without asserting live acceptance.
6. Present the reviewed code/tests and exact next prerequisite. Stop before any image build, packet, runtime activation or deployment decision.

Commands after approval: `npm test -- --runInBand src/communications/controlled-intake-startup.spec.ts src/communications/controlled-intake-runtime.spec.ts`; `npm test -- --runInBand`; `npm run lint`; `npm run build`; `node scripts/architecture-check.mjs`; local `npx prisma validate`; existing `ORGANIZATION_EVIDENCE_DIR=/private/tmp/<fresh-task-directory> node scripts/verify-organization-profile.mjs`, which invokes verify-controlled-runtime and verify-loaded-intake-browser against a freshly named disposable Unix-socket database. Qualify its local-only prerequisites first; never substitute a live DATABASE_URL or owner credential. Use synthetic provider ports only. The governing cross-repository checks remain required.

Dependencies/owners: owner approves this local code/test scope; implementer performs and reports it. Existing database/socket/browser tooling is reused, with a disposable database allowed solely for these tests. Missing local prerequisites are reported, not replaced by live access. No provider/Cloud approval is granted. No new live window is needed for local work.

Exclusions: no live database access/write, LOGIN, activation, deployment, traffic change, image build, fresh packet, provider request/mutation, verification code, live browser/customer action, job creation/retry, hold release, secret/IAM/billing change or live execution. Preserve consumed operations, current unrelated changes and the original dirty APP-010 checkout.

Rollback/disabled state: retain existing default-closed behavior; local stage-only changes can be reverted without data migration. Observable finish is locally verified fixed-stage reporting with no private leakage and unchanged refusal/cleanup behavior. It does not establish enabled27's exact original cause or repair application startup. No live test is authorized by completing this work.

Impact: no new section, acceptance criterion, task denominator, subsystem or dependency. This is a bounded diagnostic prerequisite within R11; it awards no acceptance. P06 remains12/14, R11/fullR12 open; accepted1A/1B/2A unchanged. Future image or execution authority remains separately reviewable.

## Alternative 2 — remain closed

Retain the successful sanitized diagnostic and verified shutdown. Make no code change or new live attempt.

## Owner decision

Pending. The completed read-only diagnostic approval does not authorize application code changes. No scope deviation has been implemented; alternative1 is the proposed bounded change.
