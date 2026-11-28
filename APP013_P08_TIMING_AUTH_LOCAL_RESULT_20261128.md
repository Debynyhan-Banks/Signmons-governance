# APP-013 / 3A / P08 — local timing and authentication result

Backend implementation: `4470996ad3c94467c752dddbeb7cd66cdfbaedf1`. Authority is the owner's “proceed” after the independent audit's local repair path; `APP013_P08_TIMING_AUTH_LOCAL_CARD_20261128.md` records the finite work before coding, including the source-confirmed deadline correction before that implementation. Three source/test files and eight derived manifests changed. The ninth permitted manifest needed no change. No new acceptance section, provider action or operation window.

## Implemented and tested

**Native HTTPS duration now has an absolute bound.** Previously, the socket timeout allowed a slowly arriving response body to exceed the intended eight-second request limit. NativeIO now reuses the source-pinned deadline context around open, read, validation and normal close. It refuses an existing alarm before owner I/O and restores the previous handler on exit. An outstanding response gets at most one second of local disposal within the remaining phase; that is a separately counted cleanup allowance, not another provider request. Failure stays failure, primary errors/interruption survive disposal failure, and expired-phase response closure remains unconfirmed. Resource pins, request counts, redirect refusal, no-retry behavior and finite public errors are preserved.

**The real application authentication contract is covered.** Fourteen new in-memory cases exercise actual request context, authentication/tenant/access guards, the registered UUID pipe, JobsController and DispatchBoardService. Firebase verification and read-only Prisma ports are injected; no real clients/server/database are started. Tests cover exact-job response, invalid/expired/revoked tokens, runtime permission refusal, invalid identity claims, foreign tenant/absent job, malformed job ID, concurrent context isolation and recovery after rejection. Metadata assertions bind the driver to current route/guard/pipe registration. This does not prove deployed HTTP behavior or current Firebase/IAM/database access.

Fresh results:

- Four application suites: **39/39 passed**, including14 new cases; targeted ESLint passed; no-emit TypeScript check reported zero test/imported diagnostics.
- Native response/owned-child suites: **22/22 passed**, including8 new duration/closure cases. Synthetic opener/response objects and harmless owned child processes only; no socket/provider/credential/database activity.
- Existing key-lifecycle and CT4/CT5 timing suites: **51/51 passed**. These specifically check the affected HTTP boundary, key ownership/cleanup and unchanged settling/cutoff behavior.
- Governance suites: **25/25 passed**. Frozen baseline, complete consistency, backend wrapper, architecture and whitespace checks passed.
- Current and committed native/qualification/locked-source, renewal, IQ1/SQ1/VM2, containment and manifest guards passed at `4470996`.

Independent review found no blocking issue in either the application contract test or the HTTPS patch. The only initial fixture correction was the test enum value STANDARD instead of NORMAL; final Jest, lint and TypeScript results are after that correction. Final commands/results are retained in the verification log and companion JSON. Historical runtime tests are not presented as new results.

## Timing disposition — a new session is still not ready

The audit's sequential deadline conflict remains a real planning issue. This patch fixes an unbounded primitive; it does not silently lower the inherited960-second post-settle reserve or claim the complete schedule fits.

Inspected maximum parent work after settling is21 HTTPS calls and100 seconds of polling pauses, followed by the authentication child and a separate account-readback child capped at30seconds. With the repaired request primitive, successful parent requests have an intended upper allowance of `21*8+100=268seconds`; separately allowing one second of disposal per request gives a conservative289seconds. These figures exclude local processing and the child. They are not a complete admission budget.

The remaining local blocker is precise: AQ1's `--run` child still receives the remaining work window (`native-entry/source/handoff.py:138-159`), and its stream cancellation has no separate duration (`native-entry/source/transports.mjs:95-100`). Native password entry is also bounded by its phase, not by a fixed120seconds. The sixteen-minute allowance originated as a conservative full-payment reservation, not an authentication derivation. Therefore an exact smaller authentication reserve cannot honestly be certified from current interfaces.

The next bounded local review should define a purpose-specific child duration through the existing Handoff process boundary and account for native password/preflight and both approval handoffs. Its tests must cover actual-child timeout, retained safe failure stage, process-group removal and independent account/resource cleanup. A composed readiness check must use the real recovery/qualification/native windows and distinguish packet enforcement from opening/sign-in fields that the packet does not currently receive. Do not add another framework, silently extend custody, weaken cleanup or choose a shorter constant solely to fit one hour. No numeric reserve change or new execution authority is implemented here.

## Handoff

Completed: source-derived diagnosis, absolute HTTPS deadline repair, real application contract coverage, independent reviews, derived manifests, focused regressions and committed-source validation. Remaining: the authentication child/admission duration contract; feasible complete schedule; fresh current authentication evidence; then the same-job Sandbox payment, authentic matching event, cleared application gate, cleanup and owner acceptance.

Implementer owns the remaining local duration/readiness review. Owner retains material scope decisions, future external actions and hidden inputs. No attendance is scheduled. The old R67/R68 causes remain UNKNOWN; old SD4 evidence is historical. Existing audit/receipts and unrelated backend AGENTS.md/untracked files are preserved.

Accepted 1A/1B/2A/2B remain **4/8**; **3A OPEN**; R1 newly closed **0/27**. No scope deviation within the local repair instruction and completed card. No sign-in, credential/cache read, real SQL, PostgreSQL fixture, browser, provider mutation, payment, deployment or support contact occurred.
