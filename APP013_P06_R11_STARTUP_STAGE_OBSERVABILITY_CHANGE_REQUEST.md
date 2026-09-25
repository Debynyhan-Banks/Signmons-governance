# APP-013/P06 R11 startup-stage observability change request

Status: owner-approved alternative1 locally implemented, tested and independently reviewed at backend fe9b066. The source-bound card was completed before coding. No external execution is authorized.

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

Owner replied “Approve alternative 1 for local implementation and testing only” to the exact proposal. This approves the local code and disposable synthetic tests only. No image build, packet, live database, LOGIN, activation, deployment, provider or customer action is authorized.

## Pinned implementation card — before coding

Source: backend ed6c20de479fc4895377e614780d89dc76ee5ab2; governance963f9869cfd32cf378fd408d9c9cce1e0b2f25fd. Both focused worktrees were clean. Baseline and cross-repository consistency passed. Requirement, demonstrated source gap, existing acceptance criterion, scope and rollback are specified above and unchanged.

Implementation reuses the existing controlled-intake-refusal.ts WeakMap marking pattern. A tiny controlled-intake-startup-diagnostic.ts module defines a fixed stage union, private WeakMap error-to-stage association, mark/read helpers and a failure recorder. No raw cause is copied or inspected. The recorder accepts only a privately marked error and allowlisted stage, emits exactly `CONTROLLED_INTAKE_STARTUP_FAILURE stage=<fixed-stage>` through LoggingService.warn, and swallows logging failures. No new field is added to an exception or its public response. Main records once in its existing controlled-startup catch before app.close. Startup wraps the inner error with the same generic ServiceUnavailableException, carrying only its fixed stage in the private WeakMap; retirement and buffer cleanup remain enforced. Runtime tags its existing sanitized refusal at the construction stage. No per-request stage diagnostics or retries are added.

Fixed stages and boundaries:

| Stage | Existing boundary |
| --- | --- |
| CONFIGURATION | Startup envelope/hosted facts parsing |
| INJECTED_MATERIAL | Injected secret object shape/reference/value validation |
| PACKAGED_ASSETS | Read and validate the two fixed assets |
| RESOURCE_CONSTRUCTION | Resolve existing Nest resources |
| RUNTIME_LOADING | Fallback for an unmarked loader failure/no runtime |
| RUNTIME_CONFIGURATION | Loader configuration parsing |
| RUNTIME_RESOURCES | Loader resource/project/logging validation |
| RUNTIME_APPROVAL | Initial current-runtime-approval transaction |
| RUNTIME_KEY_MATERIAL | Exact refs, distinct copied keys and token checks |
| RUNTIME_SERVICES | Existing service/authority construction |
| RUNTIME_AUTHORITY | Existing initial current-authority transaction |
| RUNTIME_BINDING | Existing provider-adapter/browser-binding construction; no calls |
| REGISTRATION | Existing session/page handlers after successful loader |

Expected files: the two existing startup/runtime modules and specs, main.ts; new typed diagnostic module/spec; narrowly scoped assertions in existing verify-controlled-runtime.mjs and/or verify-loaded-intake-browser.mjs. No new harness. Tests must cover truthful stage propagation, original public messages, unmarked/forged/private errors ignored by recorder, zero logs on success/disabled paths, logger failure preserving close/zeroization/refusal, and the actual loaded disposable workflow. Runtime configuration errors keep their existing public response. The private WeakMap contains only fixed stages, does not extend persistent retention, and cannot be populated by HTTP input. No diagnostic includes the original exception object.

Disposable test prerequisites verified read-only: PostgreSQL18.6 binaries, Node24.12, existing Playwright/Chromium cache, OpenSSL and existing UI export. Use a fresh /private/tmp/signmons-runtime-role-XXXXXX cluster and private Unix socket with TCP disabled. Install a cleanup trap before starting; stop only that exact owned cluster and preserve evidence. Never reuse an old wrapper that deletes a historical evidence directory. The existing organization harness creates/drops its own calldesk_org_* database; validate disposable database and role cleanup before stopping the cluster. No live credentials, providers or external browser navigation.

Pinned finite work (recorded before implementation): implement the mappings; focused stage/privacy/cleanup regressions; required full local unit/lint/build/architecture/schema tests; disposable actual loader/browser regression with synthetic providers; governance/whitespace checks; independent review and evidence/handoff. Completion is recorded below. No new acceptance credit and no authority beyond alternative1.

Implementation review found Nest's existing bufferLogs:true would retain the failure record because startup refuses before listen flushes the buffer. Within the approved main/logging seam, the recorder temporarily detaches buffering only for its fixed synchronous warning and restores buffering in finally; it never flushes unrelated initialization records. Its production caller is exclusively the known buffered startup catch. Real LoggingService/Nest Logger regressions verify immediate fixed-stage emission, untouched queued records, restored buffering and close/refusal after sink failure. This is a necessary connection correction within alternative1, not a new sink, feature flag or scope expansion.

Existing regression qualification found a stale legacy fixture after the actual loader and all eight loaded-browser cases passed. verify-controlled-intake-connected-browser.mjs omits the controlledVerification port and attempts Preview without browser phone verification; its caller verify-operator-intake-admission.mjs preprovisions proof, which cannot set the current UI's accepted-phone state. Both fixture files and the UI match pre-change runtime6d8ba54; this is not caused by stage logging. The current disabled-Preview guard is correct and remains intact. Completing checklist4/5 requires routine alignment of those two existing test files: reuse the existing real ControlledCustomerVerification/current-authority/durable service seam, skip preprovisioning only for browser cases, and perform the existing browser NOTICE/START/CHECK flow before Preview. Preserve all assertions, service-only cases, actual loaded harness and production/UI behavior. No fake browser state, bypass, new harness, provider access or acceptance change. This bounded test-fixture correction is within the approved local regression work; no additional customer feature or live prerequisite is introduced.

## Local completion — 2026-09-25

- [x] 1. Source, criteria, exact stages, interfaces and finite local card pinned before coding.
- [x] 2. Thirteen fixed stages carried privately; one sanitized startup warning; existing guards and cleanup retained.
- [x] 3. All 56 focused startup/runtime/diagnostic tests pass, including real buffered Nest logger failure and private-cause protection.
- [x] 4. Complete existing disposable PostgreSQL 18/browser harness passes: actual loader, all eight loaded cases, all eight legacy connected cases and subsequent operator/browser-review assertions. Synthetic provider ports only. Both disposable clusters verified zero test databases/runtime roles and stopped.
- [x] 5. Full unit regression: 131 suites / 2,400 tests pass; existing one suite / three tests skipped. Lint, local build, architecture, schema, baseline/docs, 21 safeguards and whitespace pass.
- [x] 6. Independent review clear; evidence and canonical handoff reconciled; separate external authority preserved.

Backend fe9b066 contains the code/tests and evidence/APP-013/p06-r11-startup-stage-observability.md. The initial sandbox unit failure was local listen EPERM; the local-network regression passed. The initial disposable failure revealed the documented pre-existing fixture mismatch; after its test-only correction the full harness passed. Evidence and cleanup records are retained, not replaced. No live startup cause is claimed.

Remaining: original enabled27 startup cause unresolved; R11/full R12 remain open at P06 12/14. Accepted 1A/1B/2A unchanged. Implementer owns any next reviewable image-build decision; owner separately approves a fresh build/window and any subsequent packet/execution. No image build, packet or external action occurred; prior shutdown remains last live evidence. No scope deviation.
