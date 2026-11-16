# APP-013 / 3A — SQ1 local implementation and verification

LOCAL IMPLEMENTATION VERIFIED; QUALIFICATION ONLY. This record does not authorize live execution. Owner decision ffe2913d6ffb12c8c5489435a58ef902204e8ef0 approved the three-file implementation in APP013_P08_SQ1_SIGNING_DIAGNOSTIC_PROPOSAL_20261116.md, starting from backend b51631b1aca881cfe8f820c46ff75ac4dd167a5c. The implemented source is committed at bf2d2c1cc5e6c73dde5e6247d9ee610fd04f0eb4.

## Requirement and scope

Section 3A still requires a Sandbox payment on the admitted job, its authentic matching event and the application payment gate, followed by owner acceptance. R52 stopped before that journey at SIGN / HTTP 403; AL2 found no matching audit records. SQ1 supplies one isolated, non-authentication signing diagnostic. It does not establish R52's historical denial reason, clear AUTH_OUTCOME_UNKNOWN, demonstrate application authentication or accept payment.

The implementation adds only sq1_signing_boundary.py, test_sq1_signing_boundary.py and sq1-source-manifest.json under evidence/APP-013/p08-connected-packet-20261110. Existing runtime code, allowlists, manifests, historical receipts and acceptance criteria remain unchanged. Verification artifacts are confined to sq1-local-verification; governance records and pointers are synchronized separately. The unrelated AGENTS.md change and historical untracked renewal artifacts are preserved.

## Implemented behavior

- A committed exact scope and a separate committed external decision are required by the native CLI. Imports and injected test interfaces have no live transport defaults. This local approval is insufficient for that decision.
- Exact owner/project/UID, role, service, permission, configuration, source and deadline checks precede dispatch. Main and cleanup have separate consumed phases and fixed call slots: at most 25 CLI, 14 direct HTTPS and 2 explicit cache reads overall. No slot can be reused for a mutation or SIGN retry.
- The signing request contains only a fixed public non-JWT challenge. The response projector retains bounded HTTP status, finite classifications and equality flags. Credentials, raw policy/error bodies, signature and key ID are not retained. Malformed or conflicting evidence remains UNKNOWN.
- Direct REST performs the exact conditional policy edit and identity state changes. Cleanup reads a fresh policy etag and removes only the operation-owned binding, preserving unrelated current bindings. Policy cleanup and identity disable are independent branches.
- The worker closes its main phase and execs a fresh cleanup interpreter while retaining the validated identity lease. The supervisor has a fallback if the worker dies before entering cleanup. The SDK read process has its own bounded watchdog, independent of the caller and SDK alarm handlers. Lost acknowledgements and missing process proof remain explicit residuals.
- Safe receipt validation rejects arbitrary fields and strings before merging a retained main result. Final evidence distinguishes an unmutated attempt from authoritative restoration observations.

## Local review corrections

Review found and corrected the role query's missing title/description fields and the assumption that every policy read returns version 3. The scoped adapter now accepts the documented condition-free policy versions and requests version 3 when adding a conditional binding. Existing validators and old manifests were not weakened.

Review also corrected exact empty enable/disable responses, unobserved cleanup-state assertions, timeout classification, strict Boolean authority fields, interrupt delivery across process registration, catchable-signal handling during independent cleanup, and safe retained-result validation. An actual early-worker-loss test reproduced a missing entry lock: cleanup now creates that lock only after validating the original operation root, and a late main phase refuses an already-entered cleanup phase under the same lock. These are within the approved output, recovery and privacy checklist; no additional file, operation ceiling or acceptance section was introduced.

Initial synthetic test failures included incorrectly hashed fixture project numbers, a fixture service name containing the query string, an assertion against sleep-call chunks rather than the required observation times, and a temporary HOME incompatible with the existing fixed HOME guard. Fixtures were aligned with the inspected existing interfaces. Production checks were not relaxed to make those fixtures pass. The local sandbox initially denied loopback server binding; the authorized local tests then passed with the necessary execution permission. No automatic approval-review rejection occurred.

## Verification and readiness

The pinned Python interpreter ran the final focused suite: 80/80 PASS in 7.861 seconds. The complete connected-packet suite passed 402/402 in 31.262 seconds, including those 80 tests. Coverage includes seven actual process cases, five real loopback HTTP cases, orphan SDK termination after owner SIGKILL, exact maximum call traces, strict authority, foreign identities/policies, lost acknowledgements, independent branch failures, source/configuration/clock faults and receipt-tamper privacy. No test was skipped. The full log's `fatal: not a git repository` is the expected negative case in test_approval_wait.ApprovalWaitTests.test_repository_error_is_not_treated_as_absent_approval, not a regression.

The committed source guard passed at 2026-11-16T13:17:02.705153Z in 0.944 seconds: 51 repository files and 61 SDK files, new manifest SHA256 34ae6ef74c6bd1195e82b6599073c2d27daa402ef12bc92612b28d697f56a9d9. Final runtime SHA256 is 45b3724ae1949153d8c640245aced45798c526bbe6c3e13603bbeccbcac2ccbb; test SHA256 is 768b4bd6b50087225541bebd286d854db1527d2364c3d64e10f28379c003bbd9. Only extra blank lines at test-file EOF were removed after the passing runs; no test or runtime logic changed. Staged whitespace then passed.

Safe test logs, source-guard receipt, required check results and independent review are committed in backend e402d077a22da02162e7b23c14b23dd4b5d9935c under sq1-local-verification. No commit or artifact is evidence of live signing or payment.

Independent source/API/privacy/lifecycle review identified no remaining concrete local blocker after the reproduced fixes. Backend architecture passed. Required frozen-baseline, cross-repository consistency, 25 governance tests and whitespace checks are recorded in backend sq1-local-verification/checks.json. Node application build, database and browser behavior were not changed or newly claimed tested by this Python diagnostic work.

The finite local checklist is complete: source/authority graph, finite composition, real HTTP boundary, exact policy ownership, error/privacy cases, failure matrix, process/concurrency/recovery cases, and final verification. APP013_P08_SQ1_IMPLEMENTATION_READINESS_20261116.json maps these results to the source and retained logs. This is local readiness for a separately authorized qualification; it is not current live execution readiness.

Current provider permissions, enabled services, credential coverage, effective signing access, identity state and policy state remain UNKNOWN for a future SQ1 operation. Local tests cannot resolve those facts. No credential/cache read, provider action, sign-in, IAM mutation, signing request, payment or spending occurred during this implementation.

## Remaining work and ownership

The local implementation section is complete. The implementer owns preparation of a separately reviewed, source-bound live qualification and its current prerequisite checks. The next observable external result would be one bounded signing response and independent restoration evidence. The owner/cloud and credential custodians retain that decision; no session or live time window is scheduled here. A useful provider denial reason is not guaranteed.

Host loss or loss of both supervisor and worker remains unverified restoration. The identity lease coordinates participating IQ/SQ operations; it does not enforce the absence of every other Signmons operation. These limits must remain explicit in any future live packet.

Accepted 1A/1B/2A/2B remain 4/8; 3A OPEN; R1 newly closed 0/27. No scope deviation beyond the explicitly approved SQ1 local prerequisite expansion.
