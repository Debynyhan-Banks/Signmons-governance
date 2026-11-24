# RV1 implementation card — approved local work

Owner decision: “Approve clarified RV1 local implementation and tests”, in response to APP013_P08_RV1_REVIEW_ADDENDUM_20261124.md at governance7d9f035. This records existing direct approval, not new authority. Backend base55fa194e7b6cf14cca802bbbfc05f2f1f1bc5544. Active APP-013/3A/P08 acceptance unchanged: same admitted-job Sandbox payment, authentic signed matching event and gate clearance. R56 failure evidence and current proposal provide requirement traceability; this diagnostic-only change improves future explanation, not customer acceptance.

## Fixed contract before coding

Only behavioral files: coordinator-auth/source/client.mjs and authority.mjs; real-client-binding/source/recovery-sequence.mjs and bound_handoff.py. Reuse actual client call()/issue(), exact transformed-source equality, CoordinatorAuthSequence journal and BoundPorts._merge_child. No new route/helper subsystem. Add responseValidationCode only with SIGN_EXCHANGE_REFUSED + RESPONSE_VALIDATION and recognized SIGN/KEY_READ/EXCHANGE stage.

Literal enum: BODY_BOUND, JSON_PARSE, RESPONSE_SHAPE, PROVIDER_ERROR (all three stages); SIGN_RESPONSE_SHAPE (SIGN only); KEY_RESPONSE_MISMATCH (KEY_READ only); EXCHANGE_RESPONSE_MISMATCH (EXCHANGE only). Set a literal immediately before the existing predicate and reset across calls/gates. Preserve predicates, ordering and truthiness; for existing v.error property access, retain one access before selecting PROVIDER_ERROR. Valid JSON null remains refused under RESPONSE_SHAPE. Unknown, TRANSPORT, HTTP, post-response gate/closed failures carry no code. No provider JSON parser/duplicate-key policy change.

Projection uses explicit literal allowlists, never error messages or payload fragments. Invalid/foreign diagnostics are omitted at projection and refused if inserted into the parent merge; valid code must match failure/category/stage with the complete existing diagnostic triple. Historical journals without the new field remain readable; no synthesized code. Merge checks parent/version/operation first and never adopts private/unknown fields. No proof digest on stopped child, no clearing AUTH_OUTCOME_UNKNOWN, no changed cleanup/retry/resource/time/payment behavior.

## Data, state and ownership

Data flow: injected/live existing transport response stays in memory -> existing classifier rejects -> safe literal diagnostic -> existing child journal -> existing parent merge. Only code retained; no body/token/key/URL/request/exception text/stack. Existing operation/tenant/job identity, file custody, no-retry, interruption, cleanup, purge and concurrency boundaries unchanged. Current live state and R56 historical response predicate UNKNOWN. Owner approved local work only; all external custodians retain future decisions. No Terminal session or deadline.

## Finite checklist and verification

1. Pin base and inventory direct/transitive current references before edits. Hash-only embedded source-lock constants are derived manifest references, not new behavior; serialized-handoff/source/handoff.py is a confirmed dependent. Preserve historical source blobs/receipts and governance frozen anchor. Record full inventory before refresh; refuse ambiguous or mismatched old hashes.
2. Implement fixed diagnostic map and exact extraction-guard transformations. Validate all predicates with actual injected client, preserving second-issue refusal and existing successful auth.
3. Project safe codes and validate parent merge; test actual Node child journal -> Python merge, plus unknown/private/stage mismatch/partial fields, wrong identity/version/parent drift. Keep existing stdout duplicate/size rejection; no journal parser expansion.
4. Refresh only proved current dependency hashes; validate every referenced path/hash through existing guards. No unrelated manifest promotion.
5. Run coordinator-auth node --test test_client.mjs; real-client node --test test_bound.mjs and python -B -m unittest test_bound; native Python local unit/process suites and test_connected_payment.mjs/test_transports.mjs; connected Python test discovery; source guards; backend architecture/governance/whitespace; governance baseline/consistency/25 tests/whitespace. Inspect database/browser test entrypoints first and omit provider/disposable-database/browser drivers where unrelated; record exact applicability. All executed transports synthetic/local. Build/lint/database/browser inapplicable to this standalone diagnostic-only scope with no compiled app/SQL/schema/UI change.
6. Independent diff review, safe-sentinel checks, immutable R56 evidence hashes unchanged, exact evidence and handoff.

Direct test files authorized: coordinator-auth/source/test_client.mjs; real-client/source/test_bound.mjs and test_bound.py; native-entry/source/test_entry.py. Any discovered change to business predicates, new runtime component or unapproved interface stops for scope review. Routine enum/hash/test choices above are included in this approval.

Finish: complete reviewed four-file behavior delta, required source-pin references and regressions pass; future diagnostic identifies only existing refused predicate, with no secret leakage or change to outcomes. Rollback only approved delta, leave disabled authority/no live operation. Accepted4/8;3A OPEN;R1 newlyclosed0/27. No scope deviation beyond explicitly approved RV1 local diagnostic change.
