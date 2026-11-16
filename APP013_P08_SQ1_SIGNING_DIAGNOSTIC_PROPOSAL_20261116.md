# APP-013 / 3A — SQ1 signing-only diagnostic change proposal

LOCAL IMPLEMENTATION DECISION PENDING. This proposal prepares one isolated signing diagnostic after R52's retained SIGN/HTTP403 and AL2's empty audit query. It authorizes no code or live action by itself. No attended session or deadline is scheduled. R52 and AL2 are consumed; AUTH_OUTCOME_UNKNOWN remains unchanged.

## Demonstrated gap, alternatives and requested change

Section3A requires the admitted job's Sandbox payment, authentic matching event and application payment gate, followed by owner acceptance (APP013_REMAINING_EXECUTION_CONTRACT.md:62–70). R52 never reached that journey. Its safe error proves SIGN/HTTP403 but not Google's reason; AL2 returned no matching records. This supplies no evidence for an IAM or credential correction.

Backend source b51631b1aca881cfe8f820c46ff75ac4dd167a5c, unchanged runtime e4212d9. The inspected client.mjs:9 rejects a non-2xx result before parsing its bounded body; :15 creates a JWT and continues into key retrieval/exchange. Existing Python HTTPS capabilities exclude IAM Credentials; Node createPorts requires full authentication/database authority. IQ1's exact action/limits prohibit signing. Therefore a signing-only operation cannot be obtained by parameter substitution or a fabricated existing capability.

Alternatives reviewed: repeating the full workflow adds unrelated activation/password/payment stages; changing the connected client's retained-error schema also changes exact-extraction, parent merge and multiple locked manifests; another audit query lacks a discriminating new scope. Recommend one isolated diagnostic composition, using existing identity/state, source/configuration, credential, strict-JSON, owned-process and cleanup primitives. It signs a fixed public non-authentication challenge once and immediately discards any signature. Its purpose is a current safe denial classification or a bounded successful/unknown response, not historical-cause proof or payment acceptance.

The installed SDK can retry mutation HTTP requests after transient errors: BaseApiClient defaults feed http_wrapper.MakeRequest without a method/idempotency guard. This is source inspection, not evidence that an earlier operation retried. To preserve strict no-repeat mutation semantics, SQ1 uses an explicitly scoped single-dispatch REST adapter for identity enable/disable and conditional policy add/remove, rather than SDK mutation commands. Existing production allowlists and retry rules stay untouched.

## Exact local file scope and interfaces

Create exactly these three files under backend evidence/APP-013/p08-connected-packet-20261110:

1. sq1_signing_boundary.py — exact outer scope/decision validation, pure safe-response projection, bounded descriptor dispatcher, finite main/independent cleanup composition, source/configuration checks, journal/reservations and disabled-by-default CLI.
2. test_sq1_signing_boundary.py — focused pure, actual-adapter, process/phase and privacy tests using injected transports/local fake servers only.
3. sq1-source-manifest.json — hashes for those sources and the reused source/SDK graph; no replacement of existing manifests.

No edit to packet.py, IQ1/KQ1, native/client code, old allowlists, schema/extraction/merge rules or historical receipts. Local verification artifacts and synchronized governance records may be added under sq1-local-verification and APP013_P08_SQ1_* only. If another source file or material prerequisite is needed, stop with that exact gap before extending scope.

Pure preparation/classification APIs have no native defaults. The live CLI accepts only a committed exact scope and separately committed owner decision; internal main/cleanup worker modes bind the same operation/source/scope and cannot accept arbitrary descriptors. Importing or running tests never constructs live transports. Main and cleanup have separate one-use reservations; the parent/independent worker boundary is retained so stopping a coordinator does not silently abandon provider restoration. Host power loss or loss of both supervisor and worker cannot be called verified cleanup.

## Existing components to reuse

- iq1_identity_boundary.py:118–215,280,314–557 and NativeTransport: exact owner/project/UID checks, identity lease, disabled baseline, existing bounded readback predicate and interval rules, owned process/signal handling and independent final same-UID disabled proof. Its ACTION/LIMITS/validate remain unchanged; SQ1 reports actual outer CLI/HTTPS counts, not misleading inner command counts after REST translation.
- qualification_launch.py NativeIO._owned_run/close, sdk_environment and strict_json: bounded SDK reads, process cleanup, exact environment, UTF-8/duplicate-key/nonfinite/size validation.
- access_check.py read_cached_token and bounded HTTP/deadline/close pattern: one cache read per phase and memory-only current token/coverage comparison. Reuse the primitives under SQ1's own exact authority; do not bypass another capability's descriptor checks or instantiate a fake full native capability.
- role_provisioner.definition_shape/policy_shape, bridge.py:95–129 and restore.command: exact preexisting signing role and operation-conditioned sole-member binding semantics. Policy projection/update is scoped to that binding; whole historical policy restoration is forbidden.
- diagnostics_stage.RequestAdapter.diagnostic: only the existing owner/runtime/signBlob tuple, with current request-time condition context. Never call the four-tuple full stage.
- client.mjs:8–15 and transports.mjs:80–96: exact signing URL/headers/body encoding and bounded response contract as reference; do not call issue() or createPorts for this purpose.

## Data, identity and state boundaries

Pin owner debynyhan@signmons.com, project signmons and existing project-number hash, runtime email signmons-calldesk-p07-runtime@signmons.iam.gserviceaccount.com and retained UID hash, and the exact existing custom signBlob role. Fresh main metadata must prove the same identity disabled. Match UID again immediately before SIGN and independently before cleanup. UID/project number are transient; keep hashes/match flags only.

The exact SIGN request is POST https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/signmons-calldesk-p07-runtime@signmons.iam.gserviceaccount.com:signBlob. Headers match the real caller: owner Bearer token, x-goog-user-project signmons, application/json. Body has only payload: base64 of fixed public text `Signmons P08 signing diagnostic <operation UUID> not authentication`. No dots, JWT header/claims, subject/user/tenant/job, delegates, custom token or exchange follows. On success, validate only bounded response shape and drop keyId/signedBlob immediately; do not persist their values or hashes.

Direct identity/policy mutations use the freshly matched numeric UID in projects/signmons/serviceAccounts/<UID>. Enable/disable request bodies are empty. Policy reads are POST :getIamPolicy with options.requestedPolicyVersion=3. Require a nonempty current etag and validated policy before either :setIamPolicy call. Add only the exact role/member and operation-specific start/workEnd condition. Cleanup re-reads the current policy, removes only that exact owned binding, retains unrelated bindings/fields and uses the fresh etag; never reinstate an earlier entire policy. A conflict, foreign/ambiguous ownership or uncertain write is not retried. Initial absence plus durable exact intent and current exact binding are required to reconcile a lost acknowledgement.

Both phases independently obtain the owner token using the inspected five-call owner/config/token sequence. One guarded cache read per phase must match that token in memory and prove coverage strictly beyond purgeEnd before that phase's provider mutation. No token/cache contents or raw expiry are retained. Failure before main mutation stops safely; no automatic sign-in, re-read or renewal is implied. SDK read/auth refresh/cache behavior needs explicit later live approval. Direct requests never invoke an SDK retry after dispatch.

The two exact service descriptors are iamcredentials.googleapis.com and policytroubleshooter.googleapis.com. Project permission input is limited to resourcemanager.projects.get, serviceusage.services.get and serviceusage.services.use; identity permission input is limited to iam.serviceAccounts.get, iam.serviceAccounts.getIamPolicy, iam.serviceAccounts.setIamPolicy, iam.serviceAccounts.enable and iam.serviceAccounts.disable. These exact descriptor sets are validated in the disabled scope before any transport is created. Services, consumer permission and identity-management permissions must pass current reads. The single exact Policy Troubleshooter result must be CAN_ACCESS before SIGN; this prediction does not guarantee signing success. The existing enabled-state missing-field handling is preserved; an omitted false field is not replaced with an invented explicit-false requirement. A current diagnostic result cannot establish why R52 failed under an earlier credential/state/timing context.

## Finite prospective sequence and ceilings

These are implementation targets, NOT tested execution readiness or live authority. Actual construction and fault traces must prove them before a live proposal; do not silently enlarge them.

| Phase | SDK CLI maximum | Direct HTTPS maximum | Explicit cache reads |
| --- | ---: | ---: | ---: |
| Main | 13 | 10 | 1 |
| Independent cleanup | 12 | 4 | 1 |
| Total | 25 | 14 | 2 |

Main CLI slots: owner/project/initial identity3; exact role definition1; inspected owner/config/token acquisition5; at most3enabled-state observations; immediate pre-SIGN UID/state metadata1. Main HTTPS slots: two service reads; project and identity permission reads2; current policy read1; enable1; conditional policy-add1; authoritative policy readback1; exact signBlob access prediction1; SIGN1.

Cleanup CLI slots: fresh owner/project/UID3; independent owner/config/token acquisition5; at most3disabled-state observations; final same-UID disabled metadata1. Cleanup HTTPS slots: fresh policy read1; conditional owned-binding removal1; authoritative final policy read1; identity disable1. Unneeded slots are skipped, never repurposed. Maximum one enable, one disable, one policy-add, one policy-remove and one SIGN dispatch. No SDK mutation command, redirect, HTTP retry, mutation retry or operator replay. SDK read/auth internal behavior is separately bounded by the process deadline and explicitly described at live review.

Reuse8-second individual request/process and65536-byte response bounds. Reuse the identity readback's maximum3 observations with0/5/10-second spacing and45-second phase cap; do not add IAM/SIGN propagation retries. Preserve at least11minutes for independent cleanup and2minutes for purge. Absolute UTC cutoffs, monotonic bounds, source/configuration checks and sufficient remaining time must block each dispatch. No live window is set until implementation and all readiness tests pass.

## Safe result and privacy contract

Always preserve an observed HTTP status through body-read timeout, output-limit, decoding and parsing failures. Retain a body error.code only when it is a non-boolean integer100..599 consistent with the observed HTTP status; other/conflicting numeric shapes remain UNKNOWN. Status strings use a fixed standard error-status enum, never an arbitrary string. Use strict JSON after bounded streaming read/response close. Retain only fixed failure-category labels, HTTP code, an exact numeric error code/finite status label, and allowlisted google.rpc.ErrorInfo reason/domain. Use the existing AL2 finite reason/domain lists as the initial allowlist. Relevant metadata may yield only equality flags against the exact approved permission/service/consumer/target; do not keep arbitrary values, message, raw details or URLs. Unknown/new/conflicting detail, absent ErrorInfo, malformed UTF-8/JSON, duplicate keys, nonfinite numbers, deep/oversized bodies or truncation remain UNKNOWN with the status intact. No assertion that a useful reason will exist.

Never save credentials, full policies/other principals, raw error/success bodies, signature, key ID, payload response, account identifiers, auth tokens or credentials in argv/environment/logs. Only public scope, safe UID/source hashes, ordered call/intent reservations, bounded timestamps, matches, safe result and closeout remain. Memory-only raw policy/token/body values are dropped at phase end; private-file inventory must remain empty and be independently checked. SDK cache itself is not deleted.

## Concurrency, interruption and independent recovery

Acquire the existing exact identity lease before provider work; refuse overlap/replay by source-bound operation root/attempt/phase reservations. This coordinates participating IQ/SQ operations only; do not claim every Signmons process uses that lease. A later live approval must also confirm no overlapping Signmons operation. Current project/configuration/UID/source drift blocks further main work.

Write mutation/SIGN intents before dispatch. Defer interruption across spawn/registration/owned close, then stop before the next main action. Independently supervise ownership and closure of SDK/HTTP workers. Independent cleanup authority survives the main cutoff and uses fresh owner/token/config/UID checks plus the original safe intents. Test coordinator termination, worker termination, request timeout and lost acknowledgement through the actual phase boundary. Do not replay consumed writes while reconciling.

Policy removal failure must not suppress the independent identity-disable branch, and identity-disable failure must not erase policy readback evidence. Each branch receives its reserved calls and final result; foreign policy/UID is never modified. Always close owned processes and check final source/configuration/custody/lease/private inventory. If either restoration or process/retention check fails, preserve that residual and stop; cleanup success is not inferred from a successful signature or an empty residual array assembled by skipping work.

## Finite local checklist and tests

1. Bind the exact three-file source graph and strict outer scope/decision schema; reject missing authority, drift, wrong owner/project/UID, stale windows and unsupported commands before native construction.
2. Implement the isolated phase composition with explicit descriptor slots and budgets; prove no full connected auth, key, SQL, Firebase, Stripe, runtime-secret/tag or browser path can be reached.
3. Implement the bounded single-dispatch REST boundary and safe projector; use actual urllib/HTTP-error response semantics with local fake responses, not only a preprocessed fixture.
4. Implement fresh-etag owned-binding edits and independent identity restoration with durable intents; preserve unrelated policy entries and separate branch failures.
5. Test successful SIGN shape with discarded signature; structured403; absent/unknown/conflicting detail; malformed/duplicate/nonfinite/deep/oversized/invalidUTF8 bodies; redirect, delayed headers/body, timeout and private sentinels. Assert one POST only and the exact non-JWT challenge/headers.
6. Test invalid initial state, UID change, role/service/permission failure, CAN_ACCESS refusal, stale/missing etag, concurrent policy change, lost add/remove acknowledgements, cache mismatch/insufficient horizon and source/config drift. Pre-mutation qualification failures must cause zero mutations. Failures after an intent/dispatch stop subsequent main work and trigger independent cleanup with the original outcomes preserved.
7. Test exact maximum-call traces, overlapping operations, restart/consumed phases, SIGINT/TERM/KILL boundaries, detached worker/coordinator closure, cleanup after every partial-main state, cleanup branch independence and final UID/policy absence. Include denial of SDK mutation commands even when a vector resembles an old allowed operation.
8. Run focused tests and the relevant connected-packet suite, independent source/privacy/cleanup review, source-manifest guard, governance/baseline/architecture/whitespace checks; record initial failures and final results. Prepare a live qualification packet only after actual-interface readiness passes or report the smallest unresolved blocker.

Planned commands from backend: `python3 -B -m unittest discover -s evidence/APP-013/p08-connected-packet-20261110 -p 'test_sq1_signing_boundary.py'`; then `python3 -B -m unittest discover -s evidence/APP-013/p08-connected-packet-20261110 -p 'test_*.py'` with the same repository-required environment and no live defaults; `SIGNMONS_GOVERNANCE_REPO=<resolved governance> node scripts/check-governance-baseline.mjs`; `node scripts/architecture-check.mjs`; `git diff --check`. Governance: frozen-baseline, docs-consistency with exact backend path, the three required governance test files and whitespace. No Node/build/database/browser behavior changes are proposed; preserve prior results as historical and test unreachable exclusions locally rather than claiming a new browser/SQL gate.

## Readiness, ownership and finish

APP013_P08_SQ1_LOCAL_READINESS_20261116.json records current source/SDK inspection and the confirmed gaps. Local code/tests, actual runtime descriptor trace, no-repeat transport proof, fault recovery and source manifest are NOT IMPLEMENTED and therefore UNKNOWN. Current provider permissions, services, credentials and state are also UNKNOWN; AL2's earlier observation is not a fresh SQ1 gate. No execution approval or attendance is requested at this stage.

Observable local finish: exactly the scoped files, successful actual-boundary and failure/recovery tests, verified source graph, explicit remaining live UNKNOWNs and independent review. Responsible implementer owns this work; owner approves the material local diagnostic addition. Cloud/IAM and credential custodians retain separate later authority for any temporary state change, token/cache read and SIGN. Rejected or insufficient proof stops locally, not in another full payment run. Disabled/rollback state is no live transport without exact scope; remove only new unlaunched SQ1 artifacts if abandoned, never change existing runtime/historical evidence.

Requested decision: approve SQ1 local implementation and tests in these three files plus bounded verification/governance evidence. No credentials, cache access, provider action, sign-in, IAM change, signature, payment or spending is authorized by that decision. This is a prospective bounded prerequisite expansion inside3A, with no new acceptance section or denominator change. Expected effort is one local diagnostic implementation/test section, not a product feature; stop if the three-file scope or finite ceilings prove insufficient. A separate exact live packet follows only after readiness is demonstrated.

Repository AGENTS.md requires explicit owner approval before a material prerequisite expansion and says not to treat a newly written plan as prior authority. This proposal records that pending decision rather than claiming approval. Accepted1A/1B/2A/2B remain4/8;3A OPEN;R1newlyclosed0/27. Explicit prospective SQ1 deviation proposal; no implementation or external deviation performed.

## Primary API/source references

Google documents the [SIGN request and response](https://docs.cloud.google.com/iam/docs/reference/credentials/rest/v1/projects.serviceAccounts/signBlob), [enable](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/enable), [disable](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/disable) and [conditional policy update interface](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/setIamPolicy). Inspected installed SDK generated IAM methods confirm POST policy reads with requested version3. These contracts do not prove current permission, usability, body detail availability or historical cause.

Preparation review: two independent source/design reviews found the isolated scope feasible. The pre-/post-mutation failure wording was clarified; safe status preservation, numeric consistency and exact service/permission descriptors are explicit. No implementation proof is claimed. Required documentation checks pass; code and live gates remain pending.
