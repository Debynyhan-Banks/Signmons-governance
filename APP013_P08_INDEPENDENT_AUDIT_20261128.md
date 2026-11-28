# APP-013 / 3A / P08 — independent audit

Completed November 28, 2026, at the owner's request to perform the independent review here. Three parallel reviewers examined the application, execution scripts and operating procedure; the primary agent reconciled their findings against source and retained evidence. This is a local audit, not a new execution packet or authority for external actions.

Source baseline: backend `5bc936c3d13f42ebda7289688d6ec1cea67ada38`; governance `2b2eb40981bedf2c09d9a23990c7d9ae34d05a03`, branch `codex/p06-r08-recovery-20260918`. Preserve the pre-existing backend AGENTS.md edit and historical untracked artifacts. The companion JSON binds the inspected evidence and records the timing calculation and checks.

## Conclusion

Keep the existing application and payment integration. No inspected evidence establishes a Stripe defect explaining the last two failed attempts. QSR1 repairs SQL error reporting; AP2 improves authentication diagnosis; AQ1 prevents payment during authentication qualification. These are meaningful local changes, but none proves that the historical live failure is fixed.

**Do not copy R68's timing into another session.** Its separate stage allowances do not fit the composed workflow. Fix the local scheduling/readiness assessment before requesting attendance. Do not repeat a full payment attempt to discover an authentication failure.

## Evidence and ranked findings

### 1. Required local correction: stage timing does not compose

R68 permits sign-in to begin just before S+3 minutes and last 300 seconds, but recovery must dispatch before S+5. Qualification can read until S+17 and clean up until S+22, while native dispatch must occur before S+14. The packet waits for qualification and both cleanup observations before asking for native approval. A stage may therefore finish within its own permitted window after the next stage has become unavailable.

The prior readiness proof exercises the native tail with 480 seconds of assumed setup, 45 seconds of identity reconciliation and 420 seconds of settling. It retains 976 seconds against the required 960: only 16 seconds of margin in that scenario. Adding the retained 660-second cleanup and 120-second purge reserves gives a conservative 2,685-second tail. Starting it at S+22 requires at least S+66m45s, before owner/commit latency, versus the existing 3,600-second recovery custody limit. This is a planning defect, **not proof that every fast run is impossible or that timing caused R68's SQL refusal**.

Evidence: `APP013_P08_R68_TIMING_TEMPLATE_20261127.json:48-78`; `APP013_P08_R68_OPENING_REVIEW_20261127.md:27-38,64`; `APP013_P08_R68_LOCAL_READINESS_20261127.json`. Backend `evidence/APP-013/p08-connected-packet-20261110/packet.py:95-102`; `evidence/APP-013/p08-https-output-category-local-20261029/source/qualification_launch.py:1048-1061,1548-1551`; `evidence/APP-013/p08-native-entry-local-20261101/source/entry.py:468-470,598-612`.

Required outcome: one composed timing calculation through the actual interfaces, covering sign-in, hidden inputs, review/commit latency, qualification, setup, settling and independent cleanup. It must either fit the retained constraints with explicit margin or identify the smallest concrete amendment. Merely moving a cutoff, increasing attendance or extending retention is not a fix. Existing runtime gates still fail closed; this audit does not claim that a composed-schedule blocking check already exists.

The targeted follow-up found a smaller repair direction: the 960-second post-settle allowance was inherited from the full connected-payment window, explicitly described as conservative rather than derived (`APP013_P08_CT4_CONNECTED_SETTLING_PROPOSAL_20261116.md:15-17`). AQ1 retains it while excluding Checkout. However, AQ1's child still receives the remaining work time (`handoff.py:138-159`), and native password waits use phase deadlines. Work after settling also includes effective-access checks, key operations and account closeout. Therefore no smaller number is yet justified. Derive and test a purpose-specific authentication admission budget through those existing interfaces, preserving the 420-second settle, cleanup horizons, custody ceiling and no-retry rules. Do not simply lower 960.

### 2. Historical causes remain unknown; current diagnostics are materially better

R67 reached runtime authentication and returned `ADAPTER_REFUSED_OR_UNKNOWN`; authentication and payment were not observed. R68 failed earlier at database qualification with `PROCESS_REFUSED`, after 27 CLI and 19 HTTPS reservations. Its raw cause was discarded. SD4 later verified the database/user and absence of relevant sessions at its November 27 observation; that does not explain R68 or establish today's provider state.

QSR1 now passes SQL failures through the actual process/reducer boundary into at most four finite slot/phase/query/category records. Its prior 23 new tests use harmless child processes, rather than only testing a classifier in isolation. AP2/AQ1 tests also execute the Node child under the Python parent and check journal preservation through cleanup and lost output. Those results are synthetic, not proof of current runtime access.

Evidence: `APP013_P08_R67_CLOSEOUT_REVIEW_20261127.json`; `APP013_P08_R68_CLOSEOUT_REVIEW_20261127.json`; `APP013_P08_SD4_CLOSEOUT_20261127.json`; QSR1/AP2/AQ1 local completion records. Current SQL result projection: `qualification_launch.py:1088-1095,1377-1393,1416-1450`. Current authentication diagnostics: `evidence/APP-013/p08-coordinator-auth-local-20261031/source/client.mjs:26-90`.

### 3. Operator reporting and prompt release create avoidable friction

The detailed SQL result is retained, but `packet.py:97-99` converts failure to `PACKET_QUALIFICATION_UNCONFIRMED`. `connected_launcher.py:69-77` prints a generic failure and publishes a public result only on success. Native final output also omits detailed authentication diagnostics although the accepted journal retains them (`entry.py:867-882`). The operator should inspect those safe records and explain the precise result; the owner should not have to interpret a generic Terminal label.

The decision watcher polls committed approval every second (`packet.py:45-65`); qualification then starts a hidden password prompt with a maximum 120-second window (`qualification_launch.py:1031,1485-1497`). Prepare the review, obtain the stage decision/readiness, and focus standalone Terminal **before releasing the committed decision**. Use saved status to monitor progression and ask about input only when necessary. Do not request an already-granted approval again. AQ1 currently forbids Terminal delegation (`connected_launcher.py:35`); do not silently enable it.

These operating improvements require no new subsystem or provider action. A future Terminal projection of existing safe failure fields is optional; it is not a prerequisite to inspecting them now.

### 4. Application contract coverage needs a focused check; runtime cause is still unproved

The runner's token claims and exact protected-job route match the inspected application. The application uses runtime `applicationDefault()` credentials and `verifyIdToken(token, true)`. Installed Firebase code performs a runtime user lookup for the revocation check. Owner-side lookup or direct IAM membership cannot substitute for a successful protected request from the actual runtime.

`src/auth/request-auth.guard.ts:91-104` converts all Firebase verification exceptions into the same HTTP 401. Thus even AP2's future `AUTH_RUNTIME_READ / HTTP / 401` would not distinguish a rejected token from runtime credential, permission or network failure. This is a proven observability limitation, not evidence that any particular one occurred.

The existing guard spec has three cases and mocks Firebase; the successful coordinator exchange test injects the protected-job response. Neither alone covers the real guard → tenant context → dispatch response composition. A narrowly scoped local contract check should reuse existing Nest test seams, with injected Firebase/database ports and no PostgreSQL/browser/provider launch. Preserve authentication predicates and generic public errors. Do not add server diagnostics or deploy a change speculatively; first establish whether this branch is implicated.

Evidence: `src/auth/__tests__/request-auth.guard.spec.ts:6-82`; `src/auth/firebase-admin.service.ts:27-37`; `src/auth/request-auth.guard.ts:91-104`; `evidence/APP-013/p08-coordinator-auth-local-20261031/source/test_client.mjs:478-500`. The effective authentication transport limit is five seconds (`evidence/APP-013/p08-native-entry-local-20261101/source/transports.mjs:31-40,90-91`), despite the reader's nominal eight seconds. Cold start/dependency latency remains a hypothesis; do not increase the timeout without evidence.

## Finite route forward

1. **Local, implementer-owned:** resolve the composed timing defect and bound the application contract check above. Reuse existing validators/tests; record exact changed files and any material amendment before implementation. Do not schedule attendance until the whole proposed sequence fits. This audit itself changes no executable, deadline, retention, authority or acceptance rule.
2. **One separately authorized authentication qualification:** reuse QSR1/AP2/AQ1, keep payment/webhook enabling/Checkout blocked, and inspect safe qualification results and native journals at every stop. Finish with either proven exact protected-job authentication plus cleanup, or a specific retained failure and cleanup status. Another generic UNKNOWN ends that attempt and requires local analysis, not automatic replay.
3. **Only after authentication proof:** use the existing same-job Sandbox Checkout and authentic matching event to demonstrate the application payment gate, followed by cleanup and owner acceptance.

The application payment components already provide policy binding, idempotent request/recovery, Checkout, mode/account/signature validation, event deduplication and settled-state protection. Reuse them; do not create a replacement payment stack.

Optional optimizations are deliberately outside the required repair list: move the two existing SQL qualification reads ahead of cloud/access reads after unchanged capability checks; expose existing safe diagnostics in Terminal; compact duplicated documentation. None explains a historical failure. They must not become another prerequisite project.

## Verification, handoff and limits

Completed: three independent reviews, primary-agent source/evidence reconciliation, deterministic timing-conflict calculation, existing baseline/consistency/architecture/whitespace checks and governance tests. The companion JSON contains actual results. Prior QSR1/AP2/AQ1 test results are inspected historical evidence; runtime suites were not rerun during this documentation-only audit. No credential/cache reads, sign-in, provider calls, SQL, PostgreSQL fixture, browser, payment, deployment or support contact occurred.

To reduce token use immediately, read only the current top entry and directly linked artifacts, then targeted contract/source ranges. Before this audit, the four canonical files totaled 6,318,292 bytes and 25,755 lines. Historical content is preserved; no archive, deletion or frozen-baseline reanchor is part of this audit.

Remaining blocker: trustworthy current authentication evidence. **Implementer** owns timing readiness, local contract analysis and precise failure interpretation; **owner** retains fresh external-action decisions, hidden input and final acceptance. The next observable result is a reviewed feasible local timing/contract repair, not another sign-in invitation.

Section **3A remains OPEN**. Accepted **1A/1B/2A/2B = 4/8**; R1 newly closed **0/27**. The unchanged finish is owner-completed Sandbox payment on the admitted job, authentic matching signed event, cleared application payment gate, verified cleanup and owner acceptance. No scope deviation in this audit; recommendations are not implemented or external authority.
