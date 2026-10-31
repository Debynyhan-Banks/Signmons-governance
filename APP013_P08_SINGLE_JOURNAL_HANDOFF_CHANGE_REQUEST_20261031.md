# APP-013 / 3A / P08 — single-journal Python/JavaScript handoff decision

## Current section and demonstrated gap

R1-W01 / APP-013 / 3A / P08 remains the same-admitted-job Sandbox Checkout and matching signed-settlement criterion. Backend `9ae1dc9` proved a disabled coordinator-specific JavaScript authentication capability and same-journal activation/closeout sequence, but the Python coordinator still calls `access.authenticate()` synchronously through `bridge.Ports` and the local `BoundReadbacks` passes a fake JavaScript handoff callback. The historical `realClients` remains bound to its separate authentication capability. No current source launches the new JavaScript sequence as a bounded child under Python's one-use journal, resolves real clients under the new capability, or guarantees exact private-root and process/session cleanup. This is the remaining demonstrated integration gap, not evidence of live readiness.

Source pins: Python coordinator `1eecc5241794cfed6d892db4385039274539e47b183f1d934899549eb5560f70`, bridge `58835555ea5d062bd84af91ace67c71762b9332a2f6fd9bf31ecec08c7a7dfce`, disabled readback adapter `c463671302f8d858d51063e94d7baaa6c0c72a395f505f5fa0a502674d8e532c`, historical auth launcher `180346d1874efa61986ea79575407af8669e940ec076639f828bbf2b65c0516a`, historical auth adapters `ee4906f969ae40e40b4c4a066829afc63257c62a8e9e60fcdbc1ea376b91855a`. New backend `9ae1dc9` manifest pins `authority.mjs`, `client.mjs`, `sequence.mjs` and tests. R10 and prior windows are consumed.

## Recommended Alternative 1 — one disabled handoff completion

Approve one **local-only** implementation card that gives the Python coordinator a source-locked, bounded child-process handoff to the extracted JavaScript sequence. The coordinator reserves the sole attempt and journal before the child starts; the child may write only its namespaced auth state in that exact journal and must return a fixed, sanitized result. No second auth plan, approval, attempt, journal or native launcher is allowed. The parent must enforce its deadline, signal cancellation, child exit/readback and an independent after-cutoff closeout path. A lost child response remains `AUTH_OUTCOME_UNKNOWN`; the parent cannot turn it into proof by reading a status file alone. Reconcile actual operation-private roots and purge/readback ownership before claiming containment. Both entrypoints remain native-disabled and all real transports must be injected fakes in this card.

Finite tests: exact positive activation/authentication/disable/revoke/session closeout through the serialized Python-to-Node boundary; wrong source/plan/approval/key/operator/job; duplicate/concurrent attempt; child timeout/exit/signal; lost stdout after mutation; journal tamper/foreign child; late cleanup; private symlink/foreign file; refusal of an unbound real-client factory; and no token/key/password/raw account content in parent journal or result. Reuse the 11 new auth-client, eight readback, 12 coordinator, 13 bridge, five owned-handoff and five disposable PostgreSQL contract cases. Backend lint/build/architecture and governance gates must pass. Browser applies only if UI changes; none planned.

Expected files are a fresh disabled handoff and tests beside the coordinator, a source manifest, section card and sanitized result. No production app/auth/payment source, schema or provider configuration changes. Rollback is deletion of that fresh copy. Observable finish is one source-pinned local serialized lifecycle with explicit residuals, `liveAuthorization:false`, `authProofReady:false`, native entry disabled and all current external facts UNKNOWN. Effort is one bounded medium-to-large integration card, no direct provider cost. It does not authorize credentials, provider/database reads or mutations, IAM/key/account/runtime action, deployment, Stripe/payment, spending or a time window.

## Alternative 2 — existing application operator assessment

Pause this handoff and determine, through current source and separately approved exact read-only account evidence, whether an already authorized Signmons application operator can perform the same-job Sandbox payment test. The earlier exact-tenant diagnostic found zero eligible ACTIVE OWNER/ADMIN application rows, so this is not yet a working path. Firebase project membership alone is not application authorization. If a valid operator path exists, temporary key/IAM and test-account work may be avoided; otherwise return to a specific handoff decision.

## Alternative 3 — defer 3A

Preserve all local evidence and accepted 4/8 walkthrough milestones; make no further local or external attempt.

## Decision and boundaries

Choose Alternative 1 for disabled local implementation/tests only, Alternative 2 for a source-backed operator assessment only, or Alternative 3 to defer. This card does not adopt a choice. Any later real-client credential binding, current-state qualification, resource mutation, Sandbox Checkout, signed settlement, booking or owner acceptance needs its own exact gate. R1 newly closed remains 0/27; legacy 6/60 and intelligence 0/13. **Explicit material prerequisite proposal; no handoff implementation or scope deviation adopted.**
