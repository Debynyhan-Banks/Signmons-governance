# CT5 — prospective local deadline-composition correction

Status: OWNER APPROVED for local implementation and tests. Direct owner reply: "i approve" on November17,2026. Implementation pending. Section APP-013 / 3A / P08; no new acceptance section.

## Traceability and observed gap
Source c57cb9c86c8f06dac70c856ea6bc7de9887715e7. R54 immutable result is APP013_P08_R54_RESULT_20261117.json (governance6321b77). Acceptance remains APP013_REMAINING_EXECUTION_CONTRACT.md section3A: same admitted-job Sandbox Checkout and matching authentic event clear the payment gate; no substitute capability or acceptance.

Inspected November17: packet.py copies prospectiveWindow into native plan.window. native_child.mjs passes that plan unchanged to coordinator-auth authority.mjs authorize(). Its line112 checks run entry strictly before window.cutoff. Native entry.py CT4 require_work checks work/payment horizon, not this child cutoff. R54 child2 refused AUTHORITY/START_CUTOFF after settling, before authentication journal creation. Independent cleanup requires that journal (sequence.mjs load) and recorded AUTH_JOURNAL_REQUIRED/REVOCATION_READBACK. This is demonstrated boundary mismatch, not proof of Google signing denial.

## Alternatives and preferred bounded change
Do not remove the child's cutoff or extend consumed R54 authority. Packet timing alone could avoid this one failure but would leave admission able to accept another impossible schedule. Preferred: add child-entry cutoff admission to existing CT4 Coordinator, using the same existing420-second wait and960-second reserve, while retaining existing work/payment checks. Require420+960 seconds available against BOTH horizons before first forward mutation and before settling; require960 seconds against BOTH after settling. Anchor the child cutoff to wall and monotonic time, preserving rollback/freeze/interruption checks. This deliberately conservative admission reuses existing reserves; it does not guarantee provider success. Work already admitted still uses its existing work/payment deadline; cleanup keeps its separate deadline.

Future packets must explicitly show the effective earliest admission deadline (cutoff minus1380 seconds, further reduced by work/payment reserves) and enough setup allowance. A later child cutoff in a new packet requires explicit future live approval. No R54 packet or historical receipt may be rewritten. Current R54 shape must be refused before any mutation.

## Files, reuse and boundaries
Only runtime edit: evidence/APP-013/p08-native-entry-local-20261101/source/entry.py. Tests: its existing test_entry.py, reusing CT4TimingTests, NativeFixture, actual Node child/authority seams and subprocess fixtures. Derived hashes only in the same seven CT4 manifests: native-entry source/source-manifest.json and test-manifest.json; p08-key-correction-20261110/source-manifest.json; connected-packet account-containment-read-source-manifest.json, account-containment-source-manifest.json, iq1-source-manifest.json and sq1-source-manifest.json. Any additional source/interface requirement is a stop for review, not implicit expansion. Local evidence and governance completion/readiness documents included.

No change to child authorization, identity pins, resource ownership, source verification, permissions, provider requests, payment amount, credentials, retries, cleanup behavior, retention or sixty-minute envelope. Synthetic identifiers only in local fixtures, removed after checks. No production/user data, browser session, provider/cache access, IAM action, payment, sign-in, support contact, deployment or spending. Rollback: leave live entry disabled; proposed source is unused until separately qualified/approved.

## Finite checklist and observable finish
1. Reproduce R54's exact public timing through existing parent timing and actual Node authorization boundary using synthetic local fixture; preserve original refusal.
2. Implement dual-horizon admission only at existing CT4 boundaries; preserve all existing cleanup/work semantics.
3. Positive: sufficient parent/child horizon passes actual child authority after simulated420 seconds. Negative: R54 timing, cutoff equality, short setup/wait/post-wait reserve and delayed child refusal remain safe.
4. Recovery/concurrency: repeated wait, foreign/missing IAM ownership, rollback/frozen clocks, interruption and concurrent operation refusal; independent cleanup stays available after forward cutoff. Reuse existing real worker interruption test. No actual seven-minute sleep in routine fixtures.
5. Verify source manifests and actual nested source guard. Run existing full native suite, connected suite and Node child/auth suites, not a constants-only substitute. Record exact invocations/results and any existing failures before claiming PASS. Standard commands include pinned Python unittest discovery in native-entry/source and connected-packet directories, pinned Node --test for existing native child/auth test files, backend governance-baseline/architecture/diff checks, governance frozen-baseline/docs-consistency/25 governance tests/diff checks.
6. Readiness must run actual composed parent and child at proposed admission/wait/child-dispatch timestamps. Label live access and payment UNKNOWN. Finish is a reviewed source/evidence commit with local regression proof, not another live attempt or 3A acceptance.

## Readiness / ownership / outstanding blockers
Local inspected source and R54 receipt establish the mismatch. Implementation/tests/manifests remain PENDING, owned by implementer after owner approval. No readiness claim beyond diagnosis. Any synthetic passing result is local only. Current provider state remains UNKNOWN.

R54 residuals ACCOUNT_SESSION, AUTH_OUTCOME_UNKNOWN, AUTH_REVOKE, PAYMENT_ENDPOINT_UNCONFIRMED remain unresolved. Existing CT3 action/policy/resources are expressly pinned to R51 in account_containment_read.py; they cannot be substituted for R54. Cloud/database/Stripe custodians require a separately prepared exact containment decision; CT5 does not authorize or implement that adaptation. No new full payment run until containment is verified and composed timing readiness passes.

Accepted1A/1B/2A/2B remain4/8;3A OPEN;R1newlyclosed0/27. Explicit prospective CT5 admission change; no implementation or external action performed.

## Owner decision requested
Approve CT5 local deadline-composition correction, listed tests, derived manifests and local evidence only. No attendance, password or live window is needed. This approval would not authorize containment actions or payment.
