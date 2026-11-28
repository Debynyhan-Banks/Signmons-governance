# APP-013 / 3A / P08 — local timing and authentication contract work

Owner instruction: **“proceed”**, following the independent audit and the stated local repair path (complete timing budget, actual application authentication contract, authentication before payment). Source baseline: backend `5bc936c3d13f42ebda7289688d6ec1cea67ada38`; governance `2b2eb40981bedf2c09d9a23990c7d9ae34d05a03` plus the retained November 28 audit. This card records that instruction before implementation; it does not invent a new milestone or external authority.

## Acceptance trace and demonstrated gap

Existing 3A criterion: payment on the admitted job, authentic matching Sandbox event, and cleared application gate. Protected access to that exact job is the existing prerequisite. The independent audit found disconnected local authentication coverage and stage allowances that do not compose. R67 runtime cause and R68 SQL cause remain UNKNOWN; local fixtures cannot resolve those historical facts.

Authorized local work: derive the complete timing budget against existing interfaces; perform the bounded application contract tests below; repair the existing declared request-duration enforcement as specified below. No fresh operation is scheduled. Do not lower the inherited960-second reserve, extend credential/retention limits, or grant new stage authority merely to make a schedule fit. Any such material amendment must be concretely reviewed before implementation.

## Reuse, files and exact behavior

Add one test file: backend `src/auth/__tests__/authenticated-job-contract.spec.ts`. Reuse actual `requestContextMiddleware`, `RequestAuthGuard`, `TenantGuard`, `DispatchAccessGuard`, `ParseUUIDPipe`, `JobsController.getDispatchJob` and `DispatchBoardService.get`. Inject only Firebase verification and read-only Prisma ports; do not construct the real Firebase/Prisma clients or boot a server. Assert actual controller route/guard/pipe metadata to bind the direct driver to registration. Reuse patterns from existing dispatch access/service tests. No application endpoint, success predicate, permission, dependency, schema or response changes.

Timing investigation uses existing connected packet/qualification/native coordinator/transport/child sources and public reviewed timing artifacts. No executable timing patch is authorized by a newly invented number. Record actual request/child/password bounds and dependencies, distinguishing socket inactivity from absolute wall deadlines and latest cleanup deadlines from mandatory waits. Reuse existing validators rather than reconstructing only constants. Current unresolved fact: a safe authentication-specific reserve has not been derived.

### Source-confirmed duration defect, clarified before implementation

NativeIO.https supplies a socket timeout of at most8seconds but reads/closes the response without an absolute wall deadline. This violates the declared bounded-request intent and makes summing request budgets unsound. Repair this existing boundary under the owner's local timing-repair instruction; this is not a new external permission or a numerical reserve reduction. Exact additional files: `evidence/APP-013/p08-native-entry-local-20261101/source/native_io.py` and `test_child_cleanup.py` in that directory. Reuse the already source-pinned `load_acl().http_deadline` around open/read/normal-close. Retain the existing at-most8-second request and phase deadline, resource/descriptor pins, counts, redirects, no request retries and finite error categories. Ensure an unsuccessful primary operation cannot become success or be masked by a later close failure. A leftover response gets only a bounded local close attempt (at most1second within the remaining phase time); inability to close remains unconfirmed. This cleanup allowance must be counted separately in timing analysis, never described as a provider retry. Preserve active timers/handlers or refuse before I/O. No raw provider error retention.

Refresh only derived hashes in the nine current manifests already used for QSR1/AQ1: native `source-manifest.json`/`test-manifest.json`; qualification `source-manifest.json`; key-correction `source-manifest.json`; connected packet `iq1`, `sq1`, `vm2`, `account-containment` and `account-containment-read` source manifests. No source guard algorithm or historical manifest changes. The new application test needs no native runtime-manifest entry.

Governance changes are limited to this card, its result/verification artifacts and concise current-pointer updates. Preserve prior audit, immutable receipts, frozen criteria, backend AGENTS.md and historical untracked files.

## Data, identity, state and retention boundaries

Use fictional tokens, users, tenants and jobs in memory. Exercise the real middleware/guard/controller/service chain with injected read-only Firebase/database ports. No provider call, SQL query, credential/cache read, network listener, browser, sign-in, payment, deployment or support contact. No real customer values enter fixtures or output. Concurrency must preserve AsyncLocal context per request; failed requests must not inherit prior identity. Preserve current generic public authentication errors without leaking mock private details. No durable test data or residual service.

## Finite checklist and verification

1. Reconcile source/current authority and pass baseline/consistency before changes — completed.
2. Implement the single contract test file. Cover positive exact-job response; invalid/expired/revoked token; runtime lookup refusal; wrong issuer/audience; missing tenant/role; tenant isolation and absent job; malformed UUID; interleaved concurrent requests; context recovery after refusal; actual metadata/response shape. Reuse existing isolated cases without unnecessary duplication.
3. Run only these four inspected mock-only Jest files with `npm test -- --runInBand --runTestsByPath src/auth/__tests__/authenticated-job-contract.spec.ts src/auth/__tests__/request-auth.guard.spec.ts src/jobs/dispatch-access.guard.spec.ts src/jobs/dispatch-board.service.spec.ts`. Run ESLint on the new file and `npm run arch:check`. No PostgreSQL or browser gate applies; do not run broad discovery.
4. Repair/test native request duration via `test_child_cleanup.ResponseCleanupTests`, patched opener and synthetic response objects only. Cover success, HTTP error, body/encoding/size refusal, slow/dripping/hanging read, hanging close, timeout/interruption and failure precedence, phase exhaustion, active-timer conflict/restoration and no extra open/reservation. Run the existing harmless owned-child cleanup cases for regression. Independently review source and verify affected current/committed manifest dependencies. Retain all existing provider and mutation counts.
5. Complete source-derived timing analysis, retaining every cleanup/custody/no-retry bound. Either demonstrate a compatible composed budget or produce one exact minimal correction review; never claim a safe numerical reduction without proof. The auth child still lacks a distinct reduced duration; do not claim full schedule repair from the HTTPS fix alone.
6. Review the diffs independently; run frozen baseline, complete consistency, backend governance wrapper, the three required governance test files and whitespace checks in both repositories. Record new results separately from historical runtime test evidence.

Browser behavior and real database/provider access remain excluded. The HTTPS correction enforces its previously declared duration; no other interruption/recovery/one-attempt policy changes. Any further executable expansion must be reviewed before implementation.

## Owners, finish and rollback

Implementer owns local derivation, exact contract tests, independent review and evidence. Owner retains material scope decisions, future external actions/hidden inputs and 3A acceptance. Observable local finish: the real application contract passes the stated safe tests, and the timing issue has a concrete source-derived disposition rather than another invitation to attend Terminal. This does not establish live authentication/payment. Remove the new test and restore these documentation edits to roll back; no provider rollback is required.

Accepted 1A/1B/2A/2B remain4/8;3A OPEN;R1newlyclosed0/27. No scope deviation within the owner's local follow-up instruction. Further material changes remain prospective, not authorized by this card alone.

## Item5 disposition — November28 follow-up

Completed source-derived whole-path timing review in APP013_P08_TC1_TIMING_CLOSEOUT_REVIEW_20261128.md/json. The concrete prospective amendment includes child/setup limits, actual wait bounds, composed admission and safe normal-to-independent cleanup handoff. Existing cleanup-intent ordering and detached-child ownership prevent a timeout-only fix. No new runtime change or live readiness is claimed. The owner decision is required for the material phase/supervision change; all previously completed proof remains intact.
