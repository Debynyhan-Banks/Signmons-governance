# APP-013 / 3A — CT3 combined containment correction proposal

PROPOSED; LOCAL IMPLEMENTATION APPROVAL PENDING. Preparation only, November 15, 2026. Backend source 72f0390a5ba3b1336cd870f0d701eb599e5d02cb; governance starting source 3e780c5fed34ca8f77f8ad89cfb71ab26e6d7932. Both focused worktrees use codex/p06-r08-recovery-20260918. Unrelated backend AGENTS.md changes and renewal artifacts remain untouched.

## Decision and purpose

Approve one bounded LOCAL extension of the existing CT2 checker, including tests and the exact dependency updates below. It will support one later, separately approved operation that checks account/session/revocation and the existing Sandbox webhook together, conditionally refreshes revocation or disables that exact webhook when the stated predicates allow, and independently verifies the final state. Local approval authorizes none of those live reads or changes, credential access, sign-in or payment. No attendance or time window is requested now.

This is an internal 3A prerequisite correction, not another acceptance section or replacement payment stack. The existing 3A criterion remains: “owner completes Sandbox payment for that same job; matching mode/account/amount/currency signed event clears its gate” (APP013_REMAINING_EXECUTION_CONTRACT.md, 3A). CT3 resolves current containment prerequisites so the same admitted-job journey can eventually continue; it cannot establish historical authentication, demonstrate payment or accept 3A. DATA_CONTRACTS.md approved local payment policy and job-binding semantics remain unchanged.

## Demonstrated gaps and alternatives

- CT1 account_containment.validate hard-binds R47's operation, journal hash and November 14 revocation intent. Applying it unchanged to R51 would prove the wrong cutoff. R51's surviving journal cannot supply a trustworthy original revocation intent after the pre-JC1 merge defect.
- CT2's actual SQL transport accepts only shared descriptors. Their session predicates omit R51's native administrator application names. A fixture-only predicate change would not execute through NativeIO.sql's allowlist.
- key_check.mjs performs account-list, balance and endpoint GETs, not an endpoint-only operation. Its launcher additionally performs broader qualification. createPaymentPorts retrieves a Google secret first. Neither is the required narrow path.
- CT2's _owned_run uses stdin=DEVNULL. The hidden Stripe key and endpoint ID require the existing native_io.NativeIO.child bounded stdin/process-group interface. The existing IQ1 coordinator has exactly five steps, so it must not be silently stretched.
- CT2 discards per-condition flags into mainComplete. A generic UNKNOWN would leave the next decision ambiguous. CT3 must retain bounded per-condition observations and preserve the original failure alongside closeout results.

Alternatives considered: another full payment run (unnecessary activation and scope); unchanged CT2 (wrong historical cutoff and incomplete sessions); read-only checks followed by a second proposal if correction is needed (avoidable extra cycle); a new standalone endpoint launcher (duplicate custody and cleanup). Recommended: extend the existing composition, with conditional corrective actions predeclared in its eventual live packet. No change is implemented by this proposal.

## Exact scope: nine existing backend files

Under evidence/APP-013/p08-connected-packet-20261110:

1. account_containment.py — separate R51 current-policy validator; preserve the existing R47 entry and predicates.
2. test_account_containment.py — policy, identity, final-state and historical-compatibility tests.
3. account_containment_read.py — explicit CT3 mode/authority, local SQL/HTTPS adapters, independent final observations, bounded endpoint worker composition and safe results.
4. test_account_containment_read.py — actual composition/transport/process/authority/recovery tests.
5. account-containment-source-manifest.json — affected hashes and the two immutable R51 provenance references.
6. account-containment-read-source-manifest.json — affected hashes, those provenance references and endpoint worker dependencies.

Under evidence/APP-013/p08-key-correction-20261110:

7. key_check.mjs — one-request endpoint worker mode; existing checkKey and local input-inspection mode remain compatible.
8. test_key_check.mjs — one-request endpoint worker and compatibility tests.
9. source-manifest.json — hashes for the two changed key-check files only.

The read manifest adds key_check.mjs, test_key_check.mjs and the key-correction source manifest; existing plan, authority_bridge.mjs, connected_payment.mjs, native_io.py and native dependency pins are reused. Both containment manifests add r51-live-20261115/native-result.json and local-closeout-verification.json. Inspect and verify the complete dependency closure before publishing; do not alter unrelated manifests or their purpose/baseline fields. No current manifest references the key-correction manifest digest. If a further source change or protected baseline change is required, stop and disclose the specific scope gap before implementing it.

Safe generated test/readiness evidence may be added under evidence/APP-013/p08-connected-packet-20261110/ct3-local-verification/; approval/completion and the four current governance pointers may be updated. No historical receipt is edited. No application, schema, shared transport, shared coordinator, production wiring, package or SDK change.

## Current-policy binding and account branch

R51 operation: cc2c1ce5-640f-41f4-a993-31063630207c. Bind immutable native-result.json SHA256 920b2c641716482ebbc8dffea8a08f9d31e1519b9e99e53e6bd89fdb80cee26c and local-closeout-verification.json SHA256 9109229c263c1aa9dcf777aad5f01cece1a60981ead47d6894e49b38ded01d7e.

The latter records local process absence at 2026-11-15T22:02:02.312864Z. Proposed current verification policy uses its next whole second, 2026-11-15T22:02:03Z / 1794780123. This is a newly approved post-process-observation policy, NEVER a reconstructed R51 revocation intent. Local process absence does not bound completion of a remote in-flight request. Current disabled state and cutoff evidence do not prove historical authentication outcome or global invalidation of every token.

Reuse the existing five-step sandboxed coordinator unchanged: owner CLI, project CLI, token CLI, account SQL, initial Firebase lookup. CT3's parent then owns additional individually reserved actions. Owner remains debynyhan@signmons.com and project signmons, with existing project/target fingerprints and SDK/configuration pins. No sign-in account fallback is added.

The two CT3 SQL descriptors retain the existing read-only account projection, timeouts, database host, neondb_owner/neondb, verify-full TLS/root certificate and self-PID exclusion. BOTH main and independent closeout predicates include the existing p07_payment_runtime role and signmons_p08_qualification_% applications, plus exactly:

- p08-auth-cc2c1ce5-640f-41f4-a993-31063630207c
- p08-runtime-cc2c1ce5-640f-41f4-a993-31063630207c
- p08-probe-cc2c1ce5-640f-41f4-a993-31063630207c

Use an explicit CT3-local SQL allowlist/argv/environment path over the existing owned-process primitive. Do not smuggle changed SQL through the shared descriptor allowlist. Preserve raw bytes and strict duplicate/type/UTF-8 checks before existing account validators. The ONE independent SQL closeout also reprojects operatorCount and the same exact account fields, alongside sessionsAbsent. Strictly validate the same target fingerprint/UUID and current DISABLED app status there; do not infer final app containment solely from the initial SQL. This stays one read-only statement/one closeout call and does not change another consumer's SQL contract. No session termination or SQL write. Retain only checks, not SQL rows or recovered identifiers.

Only after exact disabled app account, absent scoped sessions, fingerprint/UUID, exact Firebase identity/claims, disabled:true and emailVerified:false are established may conditional revocation be eligible. If initial validSince meets the proposed policy, skip the update. Otherwise reserve ONE accounts:update request before dispatch, setting only localId and validSince to a fresh whole-second operation intent. The intent must meet policy and never lower the observed cutoff; reject missing, malformed, inconsistent or future timestamps. No enable, profile/claim change or token issuance.

The final lookup has its own reservation, transport and cleanup deadline, even if update output is lost or refused. Maximum three Firebase requests: initial lookup, optional update, final lookup. Final acceptance requires exact disabled identity/claims and validSince >= max(policy second, initial observed validSince, requested validSince if update was attempted). Never retry an update. A successful acknowledgement alone is insufficient. The existing shared HTTPS allowlist does not permit this update; add only the exact CT3-local descriptor/host/body path with existing bounded no-proxy/no-redirect/response-close mechanics. Keep raw tokens and bodies in memory.

Installed request-auth.guard.ts uses verifyIdToken(token,true); the installed Firebase Admin path rejects disabled users and checks revocation. SQL DISABLED alone is therefore insufficient. The policy preserves this distinction. Public contract references inspected November 15: [Identity Platform accounts.update](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v1/projects.accounts/update) (validSince seconds, firebaseauth.users.update), [Firebase session management](https://firebase.google.com/docs/auth/admin/manage-sessions). Effective live permission and credential usability remain UNKNOWN until separately authorized observations.

## Endpoint branch and actual worker boundary

Use the already pinned endpoint SHA256 dbaae6448069a186dc4b9e2fc6182707dda7b61218376e9e97cd21b20b4bfeae, plan.json origin + /webhooks/stripe, existing exact EVENTS and API version 2026-03-25.dahlia. Do not adopt the newer documentation example version. Enter the existing we_ ID and sk_test_ key at hidden prompts; validate exact fingerprint and decodeStripeTestSecret before any request. No account list, balance read, Google secret access, new endpoint or secret reactivation.

CT3's parent invokes at most THREE one-request workers through native_io.NativeIO.child: OBSERVE (GET); DISABLE (POST body exactly disabled=true, only after exact scope MATCH and ENABLED); VERIFY (GET under independent cleanup). Use only https://api.stripe.com/v1/webhook_endpoints/{exact ID}, fixed Stripe-Version, no Stripe-Account header, redirects or automatic retries. Reuse boundedPaymentResponse and endpoint validators. The [Stripe endpoint update contract](https://docs.stripe.com/api/webhook_endpoints/update) supports this exact disabled parameter; [retrieve](https://docs.stripe.com/api/webhook_endpoints/retrieve) is the separate current-state observation. This check does not establish connected-account membership or charges capability.

Each worker receives bounded stdin, one exact action and its deadline; argv/environment contain no secret. The parent reserves every worker/call before launch, never launches the same phase twice, and validates exact safe stdout shape/types, empty stderr and exit consistency. Workers return only fixed phase/status/code, request count, nullable HTTP status and scope MATCH/DRIFT/UNKNOWN plus state DISABLED/ENABLED/UNKNOWN. Raw endpoint/key/body/error strings never leave the worker. Existing provider decoding uses JSON.parse followed by exact endpoint validation; it rejects malformed JSON but does not reject duplicate member names. Do not claim otherwise or silently replace shared decoding. Parent safe stdout uses q.strict_json, including duplicate rejection. Parent-only state grants DISABLE eligibility; no arbitrary URL, method, body or resource input is accepted.

The inspected Stripe API has no documented conditional If-Match/etag update parameter. The first GET and POST are not atomic against another actor changing configuration. Require the no-overlap assurance and exact ID; revalidate all pins on final GET and retain DRIFT/UNKNOWN on mismatch. Do not claim the local lease prevents outside mutations. Key shape is not evidence of read/update permission; effective access remains UNKNOWN.

Separate workers are essential: if the POST worker crashes after dispatch, the parent can use its independently reserved final GET without replaying the change or accidentally making a fourth request. A single three-request worker cannot reliably provide that guarantee after lost stdout. Before launching a later endpoint phase, confirm the preceding owned child/group is absent; otherwise stop that branch and retain UNKNOWN. Final confirmation requires exact scope and disabled state. A refused/lost change remains recorded separately even when the final observation proves containment. Foreign/malformed scope never authorizes a write.

Use a narrow adapter exposing existing child/_finish_child/_child_group_alive mechanics, without constructing the native database/owner capability. Bind cap.clock, cleanupEnd and gate to CT3's actual authority/deadlines; aggregate CLI/SQL and Node owned-group closure. Test this real stdin/process interface, not only a fake worker. Preserve the existing five-step coordinator and its process closure.

## Finite limits, independent cleanup and retained results

The later operation's maximum explicit work is 3 CLI calls (owner/project/token), 1 account SQL, 3 Firebase HTTPS, 3 Stripe HTTPS in at most3 owned Node workers, and 1 independent SQL closeout. At most1 Firebase update and1 webhook disable; no mutation retry or extra provider lookup. No explicit credential-cache read is added. The token CLI may refresh credentials and use the SDK cache under a separately stated exception; these counts do not claim a hard bound on SDK internal network requests.

There are three hidden inputs in one future attended session: Neon password, existing Sandbox key and existing endpoint ID. Gather them after a visible READY gate and before provider work. Preserve exact cutoff/read-or-work/cleanup/purge deadlines, monotonic checks and sufficient reserve for both final provider reads, SQL closeout and group closure. Final observations cannot silently reuse the expired main deadline. At live preparation, bind actual argv/source/config/resources, exact finite timing and separate external authority. No automatic renewal, attendance scheduling or payment follows local completion.

Use CT2's existing exclusive lease and immutable operation/step reservations. The inspected Journal allows main-0..6 and cleanup-0..7: keep main-0..4 for the coordinator, main-5 for endpoint OBSERVE, main-6 for conditional DISABLE, cleanup-0 for SQL, cleanup-1 for endpoint VERIFY, cleanup-2 for conditional Firebase revoke intent and cleanup-3 for final Firebase lookup. These are distinct storage slots; the revoke still obeys the main work cutoff and explicit conditional-write authority. Test all branches for receipt uniqueness and never broaden the shared Journal. It serializes this composition only, not every Signmons/cloud actor; owner must confirm no overlapping operation in the future packet. Keep mutation intent consumed even on failure. Independently attempt Firebase final lookup when a proven UID/token exists, endpoint VERIFY when its inputs and authority permit, SQL closeout with final exact DISABLED app-account and scoped-session checks, and all owned process closure. One branch failure must not erase the other's observable result or skip its independently authorized final read. Source/authority/identity drift blocks any affected provider action; local process closure/private-reference clearing still proceeds. No reconstruction/adoption of orphan PIDs or automatic restart after machine loss.

Retain explicit observed/matched/mismatched/unknown status for each account/session/identity/revocation/endpoint condition, bounded stage/code/HTTP categories, attempted-vs-skipped actions, source/config checks and local closure. Preserve original work failures separately from final current-containment observations. Password/key/token/UID/raw payload references are cleared after their final possible use; mutable buffers are cleared where supported. This is not a claim that immutable runtime strings are cryptographically erased. Persist only public scope, immutable safe intents and safe results. A crash, exhausted deadline, unavailable credential, unconfirmed process/session closure or unreadable final state remains UNKNOWN.

Historical R51 AUTH_OUTCOME_UNKNOWN and the original four residuals remain immutable. New results may reconcile current containment only. No success predicate accepts missing/null fields, fixtures, an update acknowledgement, or historical observations as current proof.

## Shift-left readiness record — preparation state

Inspection timestamp: 2026-11-15T22:47:43Z (source inspection during this preparation; not a live observation). Source SHA is the backend SHA above. Responsible implementer owns all local rows; owner/cloud/DB/Stripe custodians own subsequent live authority.

| Prerequisite | Inspected source/evidence | Current verification / owner |
| --- | --- | --- |
| Canonical scope and preserved work | Four current pointers, active APP-013, remaining contract3A, payment DATA_CONTRACTS; both git statuses | Resolved; frozen/cross-repo checks PASS before edits; implementer |
| Original failure and fresh cutoff basis | R51 native-result and local-closeout hashes above; JC1 completion | Historical evidence pinned; current policy PROPOSED; owner |
| SQL descriptors and raw output | qualification_launch.py:155–169,594–616; CT2 Transport.sql | Gap demonstrated through actual allowlist; CT3 not implemented/tested yet; implementer/DB custodian |
| Firebase shape, permissions and cutoff | account_containment._payloads/validate, shared HTTPS path, installed auth guard/Admin path, official API | Parser/adapter gaps identified; effective permission/current account/token UNKNOWN; implementer/cloud custodian |
| Endpoint configuration/client compatibility | plan.json, endpoint/decodeStripeTestSecret/boundedPaymentResponse; key_check modes | Exact pins and reusable methods inspected; new one-request mode unimplemented; key usability/current state UNKNOWN; implementer/Stripe custodian |
| Process/coordinator contracts | IQ1 coordinator fixed5 steps; q._owned_run stdinDEVNULL; native_io.child and group closure | Explicit composition selected; actual-boundary tests REQUIRED before live review; implementer |
| Timing, concurrency, interruption and recovery | CT2 authorize/Driver/run/native_main, IQ1 Journal/lease | Existing mechanisms reusable; new independent provider slots and limits unverified; no window/authority now; implementer/owner |
| Privacy and observable outcomes | CT2 generic result and purge; JC1 safe diagnostic conventions | Safe per-condition result and final-use lifecycle proposed; no private data read; implementer |

This record is qualification/containment preparation only, NOT execution-ready. It does not claim automated enforcement of the proposed changes. Replace pending local rows with actual source-pinned test evidence before proposing a live operation; label live-only facts UNKNOWN rather than creating further preparatory actions implicitly.

## Finite checklist and verification commands

1. Record owner decision for this exact nine-file scope and proposed current policy; preserve CT1/CT2 compatibility and old immutable results.
2. Implement local SQL/current-policy/conditional-update boundaries and safe per-condition results through actual adapters.
3. Implement the one-request endpoint modes and three-phase parent composition, including independent provider reads and aggregate process cleanup.
4. Verify the full matrix below, repair within scope, and obtain independent review; no live access.
5. Update only approved dependency pins; run affected full suites and governance/architecture/whitespace gates; record exact new SHA, results and any failures.
6. Deliver one complete local completion/readiness record. Only then prepare the exact combined live packet for separate approval; no automatic launch or new full payment run.

Matrix: successful already-contained state; each permitted conditional correction; exact cutoff equality/whole-second rounding/nondecreasing final cutoff; initial/final account identity/claims/status mismatch, including an app account that becomes ACTIVE before the independent SQL read; stale/missing/null/future timestamps; duplicate/invalid SQL JSON and types; each of the3 R51 sessions present separately; current PID excluded; disposable TLS PostgreSQL executing the actual descriptors; malformed/foreign/live/wrong URL/version/events endpoint; wrong endpoint hash/live key refused before a request; HTTP403/404/429/5xx, redirect, invalid UTF-8/JSON, oversized output and timeout; lost mutation response followed by independent final observation without retry; first-branch failure with remaining independent cleanup; expired/replayed/foreign authority/source/config, concurrency and clock rollback; interruption/hung process/descendant closure and receipt failure; combined Firebase/Stripe receipt uniqueness; key/password/token sentinel absent from stdout/stderr/files; CT2/checkKey compatibility. Browser negative gate: zero browser opening or payment route invocation.

Run focused tests first, then affected full suites once after final changes, using existing pinned installations:

```sh
python3 -B -m unittest discover -s evidence/APP-013/p08-connected-packet-20261110 -p 'test_account_containment*.py'
node --test evidence/APP-013/p08-key-correction-20261110/test_key_check.mjs
python3 -B -m unittest discover -s evidence/APP-013/p08-connected-packet-20261110 -p 'test_*.py'
python3 -B -m unittest discover -s evidence/APP-013/p08-native-entry-local-20261101/source -p 'test_*.py'
node --test evidence/APP-013/p08-native-entry-local-20261101/source/test_transports.mjs evidence/APP-013/p08-native-entry-local-20261101/source/test_connected_payment.mjs
npm run arch:check
```

Reuse the existing disposable PostgreSQL harness for query/session/TLS verification; record teardown. Run each changed manifest's existing source/dependency guard against the committed result. Required backend governance baseline, governance frozen-baseline/consistency/25 governance checks and git diff --check in both repositories remain mandatory. No new TypeScript build/lint result is claimed for this Python/Node evidence composition; application/schema edits are excluded. Current proposal-only validation is documentation/architecture/whitespace, not a rerun of JC1's runtime tests.

## Boundaries, finish and handoff

Rollback/disabled state: CT3 remains an unregistered opt-in command requiring its own exact external decision; old CT2 authority cannot invoke its mutation mode. Revert only these focused changes if necessary. Never restore a revoked session or re-enable an endpoint as rollback. No deployment, IAM changes, secret/key creation or reactivation, sign-in, SQL mutation/termination, account enabling, real charges, payment/refund/booking/message/support contact, new spending, retry, full-run replay or acceptance change.

Completed now: source/interface/cutoff/session review, finite combined design and dependency scope. Remaining: owner local decision, implementation and local matrix, then separately approved live containment qualification. Implementer owns local completion; owner/cloud/DB/Stripe custodians own exact subsequent authority and unresolved live facts. Next observable result after local approval: nine-file implementation with actual-boundary proof and safe, discriminating results, or a specific demonstrated blocker. A successful later containment check would still leave same-job Sandbox Checkout/event/gate demonstration, cleanup and owner acceptance outstanding.

Accepted1A/1B/2A/2B remain4/8; 3A OPEN; R1 newly closed0/27. JC1 is locally verified; payment is not live-demonstrated or accepted. Explicit prospective deviation proposal: CT3 current-policy/SQL scope, conditional containment actions, endpoint worker composition and safe result fields. No deviation implemented and no live action taken. Owner decision: PENDING.

## Proposal preparation verification

Independent read-only review passed after correcting the final SQL projection: the final read now checks the exact DISABLED account as well as sessions. Review verified the fixed five-step coordinator, available immutable Journal slots, actual child stdin/group interface, endpoint pins and both R51 provenance hashes. No remaining material proposal blocker was identified. This is design review, not implementation or live qualification.

Preparation checks passed: frozen baseline, cross-repository documentation consistency, backend governance baseline, architecture, all25 required governance tests and whitespace in both repositories. The four current pointers now identify this proposal and pending owner decision. Backend runtime files and immutable receipts are unchanged; no new runtime test result is claimed. Only this proposal and those four governance pointers changed.
