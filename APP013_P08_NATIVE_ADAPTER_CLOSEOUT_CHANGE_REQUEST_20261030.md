# APP-013 / 3A / P08 — native-adapter and authoritative-closeout change request

## Current section and decision boundary

Section R1-W01 / APP-013 / 3A / P08 remains the unchanged same-job Sandbox payment acceptance. The owner-approved disabled coordinator is locally verified at backend `293de2f0b912e4ba0591b8fbee3dc8530c6cb4a8`; it is a prerequisite only and does not accept 3A. R10 and every earlier external operation remain consumed or expired. This change request asks only whether to implement and test the next disabled local prerequisite. It does **not** authorize a provider read or mutation, credentials, IAM/key/account/runtime action, database connection, deployment, payment, spending, attended window or external operation card.

## Inspected source and demonstrated gap

The review inspected backend coordinator SHA256 `1eecc5241794cfed6d892db4385039274539e47b183f1d934899549eb5560f70`, bridge SHA256 `58835555ea5d062bd84af91ace67c71762b9332a2f6fd9bf31ecec08c7a7dfce`, restoration SHA256 `a0bf4bc90cca0bd52935915d710ccb44e065dd3deed841a12ab49cb3ac4a1cb9` and authentication handoff SHA256 `252e88f5659b7e5f3f8e4d0cabf5b5b06a1a90902ec66df6c230026aa992aec5`.

The current coordinator is deliberately injected-only and `native()` refuses. Its local matrix proves one journal, mutation ordering, unknown-outcome retention and independent closeout, but the two final closeout facts are supplied callbacks. `bridge.Ports.account_closeout()` accepts an exact four-boolean callback object, and `runtime_closeout()` accepts an exact four-boolean callback object; neither method obtains those facts from the actual account/session/runtime/private-plan interfaces. The local authentication handoff also requires an injected clients factory and returns `liveAuthorization:false` / `authProofReady:false`. The historical restoration `NativeAdapter` can issue exact runtime/SQL commands and has a separate authentication child, but directly invoking that historical controller would recreate a second journal and mutation owner. Private-plan purge is likewise owned by the historical restoration root rather than the coordinator journal.

Therefore no current source can truthfully claim all of the following under the coordinator's one journal: exact disabled test account and Firebase revocation, token revocation, database/session absence, owned-key deletion, both temporary IAM binding removals, temporary runtime/database/secrets retirement, normal traffic, and absence of every operation-private plan/binding/result file. A green injected callback cannot fill that gap.

## Recommended Alternative 1 — disabled source-pinned adapter and readback matrix

Approve one local-only implementation card that adds a fresh disabled adapter beside the coordinator. It may reuse the historical restoration command/SQL serialization and the bridge's bounded CLI/HTTPS request contracts, but the coordinator remains the sole mutation and journal owner. The adapter must expose only the existing coordinator port methods; it must not run either historical controller as a nested operation.

The adapter must source-pin every reused module and accept injected runners/clients for isolated tests. It must map the owned-key receipt into the actual authentication handoff without granting live authority, and it must implement independent readback functions that derive fixed sanitized booleans from exact interfaces rather than accept caller assertions. The account readback must bind the exact disabled test ADMIN, Firebase record, token-valid-since/revocation state and zero sessions. The runtime readback must bind the exact candidate revision/identity, retired database role, secret versions/bindings, normal traffic, and a finite allowlist of operation-private paths whose absence is verified. Unknown, malformed, ambiguous, lost or late results remain named residuals. No raw password, key string, token, account ID, environment value or private plan content may enter the journal or sanitized result.

The local card must keep `native()` and all credential resolution disabled. It must not create a future live plan, approval, command or attended window. API Keys service retention stays `RETAIN_ENABLED_AFTER_KEY_DELETE` under the already approved decision; only the exact owned key is eligible for deletion/readback in a later separately approved operation.

Required local matrix: exact positive injected lifecycle; source/plan/approval/identity/path refusal before transport; account/Firebase/token/session disagreement; private-path symlink/FIFO/mode/foreign-file refusal; runtime/role/traffic drift; lost auth/key/IAM/runtime responses; cleanup residuals; independent closeout after cutoff without mutation replay; journal privacy; concurrent one-use reservation; deadline, clock rollback and SIGINT/SIGTERM behavior. Run unchanged coordinator, bridge, restoration and authentication-handoff suites plus backend lint/build/architecture, governance frozen-baseline/consistency/safeguard checks and both repository whitespace checks. Browser and disposable PostgreSQL proof are required only if those surfaces change.

Observable finish: a source-pinned local result that reports the exact tested readback matrix, all remaining UNKNOWNs and `liveAuthorization:false` / `authProofReady:false`. It may support a later external-operation proposal; it cannot itself request or authorize that operation. Rollback is deletion of the fresh disabled adapter/test/result copy. Expected effort is a medium bounded local task with no direct provider cost.

## Alternative 2 — staged adapter proofs

Approve two local cards: first authoritative account/session/private-path readbacks, then runtime/IAM/key readbacks and coordinator binding. This reduces each review diff but leaves the coordinator non-launchable between cards and adds another approval/reconciliation boundary. Neither card authorizes external action.

## Alternative 3 — defer P08

Make no additional adapter or closeout implementation. Preserve the current local coordinator result and accepted 4/8 milestones. The same-job 3A payment proof remains blocked on an authenticated operator path.

## Decision requested

Approve Alternative 1 for disabled local implementation and isolated tests only, choose staged Alternative 2, or defer under Alternative 3. Any future qualification, provider access, IAM/key/account/runtime mutation, credential handling, payment or spending still requires a new exact operation contract, current evidence, a finite future Eastern window and separate owner approval. Accepted walkthrough remains 4/8; R1 newly closed 0/27, legacy 6/60 and intelligence 0/13. **Explicit material prerequisite proposal; nothing implemented and no scope deviation adopted.**
