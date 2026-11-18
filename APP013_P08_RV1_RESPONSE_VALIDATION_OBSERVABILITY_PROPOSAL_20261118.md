# APP-013 P08 RV1 response-validation observability proposal

Status: **prospective local correction; owner decision pending**. This proposal grants no implementation, credential, provider, replay, payment or live-execution authority.

## Demonstrated gap and acceptance connection

APP-013 Section 3A remains active: the same admitted job must complete authentic Sandbox payment and the matching event must clear its gate. R56 did not reach payment. Its safe journal retained `EXCHANGE / RESPONSE_VALIDATION / httpStatus=null`, a stopped-and-closed authentication child, and verified cleanup, but the current allowlisted diagnostic cannot distinguish the exact response-validation predicate. That missing local distinction blocks a responsible decision about any future qualification; it does not change the 3A acceptance criterion or prove the R56 authentication outcome.

Source/evidence inspected:

- backend checkpoint `a72c5a6c4681dc65468aed98359cd886f9d030fb`; R56 execution source `ce9bccfd71a989b20a0323e0d047dbd81332a59e`;
- backend `R56_CHILD_RESULT_LOCAL_DIAGNOSIS_20261118.md`;
- current `client.mjs`, `recovery-sequence.mjs`, bound-handoff schema, native entry handoff/coordinator and their tests;
- R56 safe journal/result and all six parent-owned child observations.

## Proposed bounded behavior

If the owner approves RV1, prepare and implement one local-only card that:

1. Adds one allowlisted `responseValidationCode` only when `failureCode=SIGN_EXCHANGE_REFUSED` and `failureCategory=RESPONSE_VALIDATION`.
2. Distinguishes only the current source predicates: bounded-body refusal, invalid JSON, provider error envelope, post-response authority/deadline refusal, or exchange identity/token-shape refusal. It retains no body, field value, token, key, URL, request payload, exception message or stack.
3. Carries that code through the existing safe child journal and exact parent merge. It must not populate the authentication proof digest, set `authenticated`, clear `AUTH_OUTCOME_UNKNOWN`, authorize retry or change cleanup.
4. Leaves TRANSPORT and HTTP diagnostics, one-attempt/no-retry behavior, request serialization, identity predicates, provider endpoints, deadlines, resource lifecycle and payment behavior unchanged.

Expected executable interfaces are limited to the existing response classifier in `p08-coordinator-auth-local-20261031/source/client.mjs`, the safe journal projection in `p08-real-client-binding-local-20261031/source/recovery-sequence.mjs`, and the exact allowlist/merge boundary in `p08-real-client-binding-local-20261031/source/bound_handoff.py`. Update only their direct tests and source/test manifest references proven necessary by an exact reference inventory. Do not change the native payment path, business application, schema, dependencies or UI.

## Required verification after approval

- Positive: every existing response-validation predicate maps to exactly one safe code through the real local child/journal/parent boundary.
- Negative: raw bodies, duplicate keys, oversized bodies, unknown codes, partial diagnostic groups, extra fields, private sentinels, wrong operation/version and parent drift refuse without entering the parent journal.
- Concurrency/recovery: one child attempt only; lost output, timeout, exit, interruption, journal merge failure and independent closeout preserve current uncertainty and cleanup semantics.
- Regression: current success proof, TRANSPORT/HTTP cases, cleanup/readback, payment containment, source guards and call ceilings remain unchanged.
- Commands: affected Node/Python suites, full connected/native packet suites required by the final card, architecture, frozen baseline, complete consistency, 25 governance tests and both whitespace checks.
- Browser/build/lint/database: browser is inapplicable to this internal local diagnostic. Build, lint and database gates are required only if the exact approved implementation touches their compiled/runtime surfaces; the implementation card must state and justify applicability before coding.

## Authority, exclusions and rollback

- Product owner: approve or decline the exact local observability scope before code changes.
- Implementer: after approval, complete the exact reference inventory, source pinning, tests and evidence. No live facts may be inferred from local tests.
- Cloud/credential/database/Stripe custodians: retain every future external decision. RV1 cannot authorize a provider read, sign-in, mutation, replay or payment.
- Excluded: R56 replay, another connected packet, changes to authentication/payment semantics, raw response retention, weakened proof predicates, deployment, IAM/secrets, billing and real data.
- Rollback: revert only the approved safe-code/schema/test/manifest delta. Existing disabled-by-authority state and conservative unknown outcome remain the baseline.

Observable finish after a future approval is a locally verified, source-pinned safe diagnostic that still reports R56 as historically unknown. Accepted remains 4/8, Section 3A OPEN, R1 newly closed 0/27. Overall CallDesk/MVP completion remains unquantified by canonical evidence.

No scope deviation in this proposal; RV1 itself is an explicit prospective diagnostic-only deviation requiring owner approval.
