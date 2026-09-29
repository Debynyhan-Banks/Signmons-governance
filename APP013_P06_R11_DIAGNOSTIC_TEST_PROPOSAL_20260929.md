# APP-013 / 2B / P06-R11 diagnostic-image controlled-test proposal

Status: review-only proposal. Owner selected September 29, 2026, 8:00–8:45 AM Eastern for attendance; timing selection is not execution approval. No new runtime packet, private execution helper, activation or deployment has been created. The owner requested this proposal after the completed readiness check.

## Purpose and exact acceptance criterion

Use the existing protected phone → eligible address → reviewed submit journey to create exactly one controlled job, followed by verified closeout and correlated R11/R12 evidence. This remains section 2B; accepted 1A/1B/2A and the remaining 2B → 3A → 3B → 3C → 3D order are unchanged.

Enabled27 failed before the browser journey. The new image adds thirteen fixed startup-stage diagnostics; it does not prove that the original failure is fixed. A successful startup permits one connected journey. A failed startup stops browser handoff and requires mandatory closeout. Neither successful deployment nor a diagnostic stage alone is customer acceptance.

## Fixed source, target and evidence

- Preparation checkpoint: backend a83e57e2a0385c5ed883b879758ef2d672110be9; governance c9eba6cfcb1e9371ea7a2de6ad84592adbfd5d0f. No source differences from diagnostic source fe9b0661224a24969679dea5606dadbdc033c224 in src, scripts, package/lock, Prisma, Dockerfile or cloudbuild configuration.
- Image: us-east5-docker.pkg.dev/signmons/signmons/signmons-calldesk-backend@sha256:0457ff3bb38cad13bd73d79f2d140c5bcbac024915b77cf59c9de744765e6356. Build c2803a9a-829c-47f3-b47f-1c6092ac21d9; no rebuild proposed.
- Cloud Run: project signmons, region us-east5, service signmons-calldesk-staging. Proposed fresh revision signmons-calldesk-staging-app013p06enabled28, suffix app013p06enabled28, protected tag p06-intake-enabled. Its absence must be checked before any deployment; absence is not yet claimed.
- Normal traffic stays 100% on signmons-calldesk-staging-app013bounds. Existing unrelated tags stay unchanged. Zero normal traffic does not mean the protected test URL is unreachable.
- September 29 database read at 11:14:09Z passed policy, participant binding, inactive approvals, closed/expired runtime role and zero sessions. Exact retained phone count nine / 4500000 micros; address four / 400000 micros at EACH account and tenant scope.
- Cloud read at 11:21:26Z: desired/latestCreated enabled27, latestReady enabled25; normal traffic preserved, enabled tag absent, diagnostic image present. Preserve this distinction in the new controller; do not require latestCreated to equal latestReady.
- Safari: active account, approved primary business profile, SMS/Fraud Guard enabled, Voice disabled, U.S. SMS monitored and all other geographic channel settings disabled (1 monitored / 487 disabled). Sole verified recipient visually confirmed by owner; private binding remains HMAC-only. No fresh cryptographic comparison with the displayed number is claimed.

## Proposed schedule — America/New_York, September 29

| Phase | Eastern | UTC | Result required |
| --- | --- | --- | --- |
| Owner-attended login support and preflight | 8:00–8:15 AM | 12:00–12:15Z | Source, authority, image, target, policy, participant, capacity and closed-state guards pass |
| One deployment and connected browser window | 8:15–8:30 AM | 12:15–12:30Z | Verified Ready/no-normal-traffic result before browser handoff; then at most one journey |
| Mandatory closeout | Immediately after DONE, STOP or failure; by 8:45 AM | By 12:45Z | Revocation, role closure, zero sessions, tag removal and normal traffic read back |

Runtime validity is only 8:15–8:30. Database LOGIN expires by 8:45. Start the coordinator at 8:00 with password ready; existing four-minute start reserve and deadline guards remain enforced. Do not extend a window or retry if setup consumes the available time. Cleanup remains mandatory if the ordinary window expires, and unverified cleanup blocks further work.

## Proposed costs and retained liabilities

These are proposed operational allowances, not renewed authorization or guaranteed invoice caps. No live price query or invoice reconciliation was performed during this documentation step.

| Item | Proposed new allowance | Retained-state / maximum after this session |
| --- | --- | --- |
| One phone flow | USD0.50 (500000 micros) | Prior USD4.50 retained; account ceiling USD5.00 (5000000 micros) |
| Address validation | At most two requests, USD0.10 each; USD0.20 total | Prior four requests/USD0.40 at each scope; account and tenant ceilings six requests/USD0.60 each |
| Infrastructure for this bounded session | USD2.00 operational allowance | Separate from verification holds and pre-existing recurring costs; stop initiation on observed/estimated exhaustion |

Total proposed incremental operating allowance: USD2.70. Account and tenant address ceilings track the same operations; do not add them as duplicate charges. Other historical external holds remain intact. No new secret versions are proposed; existing secret/storage charges remain separate. Existing disabled versions can continue to accrue costs. Do not promise an invoice maximum or silently treat historical infrastructure allowances as unused credit.

Existing coordinator limits remain one phone START, up to five code CHECKs, no resend; two address requests total including any correction; one session with existing operation/in-flight limits. All current holds are preserved. Changed, decreased, malformed or insufficient retained capacity stops before activation; no cap increase or hold reset.

## Connected execution and data boundaries

After separate exact execution approval, reuse the existing attended coordinator and guarded controller. Owner enters the existing administrative password privately only after READY; anonymous pipe, hidden input, timeout and cleanup remain. Runtime uses the existing restricted child role and pinned purpose-secret versions. No password, phone, address or verification code goes into chat, repository evidence or shell arguments.

Fresh preflight checks the exact approved account/project/service, disabled flags, pinned secret-version metadata, policy/category/identity, role/session state, retained liabilities, image and unused revision/operation identities. Only then may the guarded path open bounded LOGIN, activate the matching packet digests and deploy once with --no-traffic. Reuse the existing protected route and health/readiness readbacks. No provider request occurs simply because startup succeeds.

Owner opens the returned protected URL, reads the existing participant notice, fills Customer name and all required fields, completes phone verification and waits for Code accepted, confirms the eligible address, reviews the draft and submits once. Invalid or uncertain outcomes remain refusals; do not double-submit. At completion or any error, owner types DONE or STOP in the same Terminal and leaves it open for closeout.

Closeout revokes only matching runtime/phone approvals, closes/purges transient session material through the existing approved path, preserves admitted job/audit and held liabilities, restores runtime NOLOGIN/connection limit0/expired validity, verifies zero sessions, removes only p06-intake-enabled and verifies baseline traffic100%. No unrelated secret/resource deletion. Report actual correlated outcome separately from owner acceptance.

If startup fails, no browser handoff or verification request is permitted. Retain the sanitized stop and complete closeout. A bounded read of fixed startup-stage logs is a subsequent read-only diagnostic decision; this proposal does not introduce a new log reader or authorize unrestricted logs, a second deployment or a repair by guesswork.

## Finite preparation card and local checks

Existing components to reuse: scripts/p06-runtime-packet.mjs and its production reviewer; scripts/p06-r10-controller.mjs; scripts/p06_r11_attended_coordinator.py; existing private controller/hidden-input templates; fixed participant binding and policy digests; original private build-binding format; existing shutdown and sanitized evidence paths. Consumed templates are read-only inputs, never rerun or overwritten.

Expected changes after preparation approval: one fresh private review directory containing runtime-packet.json, r10-review-plan.json and packet-preparation-result.json; fresh plan/packet/operation UUIDs; exact selected times; diagnostic source/image and current compiled-file hashes. No execution authorization or runnable helper installation during preparation. Do not reuse the old 716-file binding or invent new counts: generate and verify the complete current compiled inventory against the diagnostic source. Any material source/helper change needs its own traceable decision.

1. Reconcile the selected window, fixed source and image; inspect old/current packet interfaces and preserve the original scope. Exit: no unnamed policy, identity, secret-version or retention assumption.
2. Construct one private review packet with new identities and exact 9/4 retained-liability baseline, ceilings and limits above. Exit: production packet/controller/suffix validation passes and no prior attempt/identity collision exists.
3. Validate installed review bytes/hashes/ownership (0700 directory,0600 files), full current compiled binding, and actual-plan coordinator using synthetic ports only. Exit: positive review plus mismatch/expired/consumed/duplicate/recovery guards pass without external actions. No production browser test at this stage.
4. Present the exact plan ID, packet digest, windows, costs, intended mutations and closeout authority for owner execution approval. Exit: concrete reviewable result; no inferred authorization from timing selection.
5. After exact execution approval only, install/check one set of fresh guarded helpers, perform window-bound preflight and one attended run. Preserve exclusive markers before each action; failure/uncertainty consumes the attempt and triggers closeout, never automatic retry.
6. Record actual R11 journey and full R12 closeout evidence; request owner acceptance only for demonstrated criteria. If stopped, report the specific gate and responsible role without awarding acceptance.

Local commands for packet preparation: node --test scripts/p06-runtime-packet.test.mjs scripts/p06-r10-controller.test.mjs; python3 -B -m unittest discover -s scripts -p test_p06_r11_attended_coordinator.py; production reviewPacket/reviewR10ControllerPlan/deriveR10CloudRunRevisionSuffix and review_run_directory against the newly bound packet, with synthetic execution ports. Retain existing private-input tests if that seam changes. Do not represent old full application/browser tests as new evidence. No application code change is proposed.

Required documentation gates before/after governed edits: backend check-governance-baseline.mjs with SIGNMONS_GOVERNANCE_REPO set to the focused governance checkout; governance frozen-baseline-check.mjs, docs-consistency-check.mjs with SIGNMONS_BACKEND_REPO set to the focused backend, and the three mandated governance test files; backend npm run arch:check; git diff --check in both repositories.

## Decision and handoff

The requested decision is permission to prepare exactly one private review packet for the schedule and proposed ceilings above, including bounded read-only target/secret-version metadata qualification required to finish that packet. It does not authorize LOGIN, activation, deployment, paid verification, browser submission or a new job. The finished packet will be presented for separate exact execution approval, as required by the existing remaining execution contract and the prior controlled-test workflow.

Owner selected timing only. Preparation decision: PENDING. Implementer owns packet preparation and evidence; owner owns preparation/execution decisions, private input and attended browser steps. Missing or changed source/identity/retention/capacity evidence stops the dependent action. If the selected window becomes infeasible, remain closed and request a new prospective window rather than silently moving it.

Completed now: inspected source/reuse/evidence, concrete schedule/cost/sequence proposal and bounded preparation card. Remaining: owner preparation decision, actual packet/hash validation, exact execution decision, one attended run and correlated closeout/acceptance. Relative size: bounded packet adaptation; local preparation confidence high, startup success uncertain because the prior failing gate is unknown. No ETA or success guarantee.

Exclusions: payment or Stripe, appointments/dispatch/confirmation messages, production customer traffic, unrelated IAM/secrets/provider changes, new builds, schema/code changes, hold releases, cap expansion, automatic retries and Eternity marketing. No scope deviation in this proposal. Prior cloud-target error and its expressly approved correction remain disclosed in readiness evidence.

P06 remains12/14; R11/fullR12 open; accepted1A/1B/2A remain3/8. No new acceptance section.
