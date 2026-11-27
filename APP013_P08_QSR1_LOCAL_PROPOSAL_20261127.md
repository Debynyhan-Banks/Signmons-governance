# QSR1 — qualification SQL failure reporting: local correction proposal

PROPOSED; IMPLEMENTATION NOT AUTHORIZED. APP-013 / 3A / P08. Backend source `06bb7125004eb8a16bc0a190faae8a882ec92858`; governance handoff `91038c1`. This card proposes one bounded reporting change in two existing source/test files and nine derived manifests. No new subsystem or acceptance section.

## Requirement and demonstrated gap

3A acceptance remains the same admitted-job Sandbox payment, authentic matching signed event and cleared application payment gate. Current database qualification is an existing prerequisite. R68 stopped at database PROCESS_REFUSED, with normal and independent session observations unconfirmed. SD4 subsequently verified matched database/user, sessions absent and independent closeout; it cannot establish R68's cause. Both immutable evidence records and their receipt hashes must remain unchanged.

Inspected qualification_launch.py NativeIO._owned_run currently sends qualification stderr to DEVNULL and emits PROCESS_REFUSED for every nonzero process exit. NativeIO.sql reserves classifier/LC_ALL=C/VERBOSITY=sqlstate for the existing version5 SQL_CONNECTION diagnostic only. QualificationIO.sql and _produce_current retain no SQL cleanup failure category. packet.execute_connected only accepts CURRENT_EVIDENCE_OBSERVED with failure=None and no residuals; diagnostic details must never substitute for those checks.

APP013_P08_QSR1_LOCAL_REVIEW_20261127.json records current source hashes, exact transitive manifest dependencies and six harmless local process executions through the actual process runner. Synthetic authentication and permission errors both became PROCESS_REFUSED through the qualification mode; the existing diagnostic returned SQL_AUTHENTICATION_REFUSED and SQL_PERMISSION_REFUSED. An unrecognized canary became SQL_ERROR_UNKNOWN. Every owned child closed. This reproduction used no credentials, psql/database fixture, network/provider, browser, sign-in or payment and did not modify source. It demonstrates the reporting defect, not R68's historical cause.

## Proposed exact behavior and interfaces

1. Reuse sql_error_category for current QualificationIO SQL only. Permit the classification switch only for an exact source-derived allowed SQL argv and QualificationIO capability, in addition to the existing RoleDiagnosticIO path. Add only LC_ALL=C and psql VERBOSITY=sqlstate for this path. Preserve executable/host/user/database/query pins, PGPASSWORD in-memory handling, verify-full TLS, statement/lock/connect/process deadlines, output limit, process ownership and no retry. Other CLI, recovery and role/correction behavior remains unchanged.
2. Drain bounded stderr and stdout with the existing shared aggregate output cap; classify before discarding raw data. Persist only existing finite SQL error categories and allowlisted process/deadline/output/validation categories. Unknown/multiline/malformed errors remain SQL_ERROR_UNKNOWN or the existing generic safe fallback; never save raw message, SQLSTATE, host, password, query result, credential hash or password characteristics. Do not expand provider-specific parser patterns in this change.
3. Retain a bounded `sqlFailures` list in the current qualification result and its independent recovery result when applicable. Maximum four entries, each containing only reserved slot number, fixed phase (READ, NORMAL_CLOSEOUT, INDEPENDENT_CLOSEOUT), exact source-known query label and an allowlisted failure category. No unbounded error strings. Track only actual reserved attempts; pre-reservation refusal must not fabricate one. Fresh independent cleanup receives only its own retained labels; an interrupted prior attempt remains UNKNOWN. Normal and independent residual/status predicates remain unchanged. No new request, receipt family or private payload retention.
4. Successful result/candidate behavior, immutable old receipts and packet.execute_connected's acceptance checks stay unchanged. Diagnostics cannot qualify failed work or clear residuals. Update only the exact current source/test hashes and transitive manifests below; do not rebaseline governance or historical operation evidence.

## Expected files

- `evidence/APP-013/p08-https-output-category-local-20261029/source/qualification_launch.py`
- `evidence/APP-013/p08-https-output-category-local-20261029/source/test_qualification_launch.py`
- `evidence/APP-013/p08-connected-packet-20261110/account-containment-read-source-manifest.json`
- `evidence/APP-013/p08-connected-packet-20261110/account-containment-source-manifest.json`
- `evidence/APP-013/p08-connected-packet-20261110/iq1-source-manifest.json`
- `evidence/APP-013/p08-connected-packet-20261110/sq1-source-manifest.json`
- `evidence/APP-013/p08-connected-packet-20261110/vm2-source-manifest.json`
- `evidence/APP-013/p08-https-output-category-local-20261029/source/source-manifest.json`
- `evidence/APP-013/p08-key-correction-20261110/source-manifest.json`
- `evidence/APP-013/p08-native-entry-local-20261101/source/source-manifest.json`
- `evidence/APP-013/p08-native-entry-local-20261101/source/test-manifest.json`

No application payment code, backend endpoint, database schema, runtime target, IAM role, provider setting, dependency version or source guard algorithm changes are proposed. If an additional executable file/interface or broader retention change is discovered, stop before expanding this list.

## Boundaries, readiness and owner responsibilities

Sequence remains hidden password → existing cloud/access checks → database reads → existing Firebase checks if eligible → normal session closeout → fresh independent session check → safe result → private purge. All current tenant/actor/job/policy identities and DATA_CONTRACTS.md payment bindings remain unchanged. No query, query count, resource pin, runtime enablement or successful-qualification definition changes. No customer data or credentials enter diagnostic records.

Readiness: current source and actual process/error-classifier boundary inspected and reproduced; dependency hashes traced transitively; baseline/consistency passed before proposal. New behavior/tests are NOT implemented or claimed passed. Configuration/effective access/provider state from old runs is not promoted to current readiness. No live operation is prepared or scheduled. Implementer owns local correction, safe-category review, complete tests and source-manifest validation after approval. Owner must explicitly approve this diagnostic/retention scope expansion before implementation and retains all future external decisions. No Terminal attendance or deadline is needed.

## Finite checklist and verification commands

Completed: reconcile canonical ticket/contract/current evidence; identify exact error-loss boundary and consumers; reproduce actual local process behavior; trace exact two-file/nine-manifest scope; prepare this proposal. Pending after approval: implement guarded classifier reuse and bounded result projection; add focused tests; refresh only derived current hashes; run relevant tests and guards; record completion/limitations. No further subsystem or full live retry is included.

Use pinned Python3.14 with -I -B and explicit source sys.path. Existing unittest modules/classes to reuse: test_qualification_launch.CurrentProofTests, ExternalBindingTests, OwnedProcessTests and SqlConnectionDiagnosticTests, plus a focused qualification SQL reporting class in the same test file; connected test_packet.RetainedScopeTests for unchanged failure/cleanup handoff. Run via unittest.TextTestRunner with an explicit TestLoader selection; never automatic PostgreSQL test discovery.

Required new cases: unchanged positive qualification and exact SQL/environment assertions; main and normal/independent failure categories; password/permission/connection/TLS/name-resolution/unknown output; missing/null/malformed response; wrong command/capability refused before Popen; concurrent stdout/stderr and aggregate overflow; deadline/interruption/child reaping; no retry or slot reuse; failed main still independent cleanup; independent failure preserves residual; crash recovery never manufactures prior diagnostics; canary exclusion from every persisted file. Exercise actual QualificationIO → NativeIO.sql → _owned_run and result reducer with injected ports/harmless child processes, not only a direct classifier test. No real psql, PostgreSQL fixture, cloud, credential/cache, browser or network test. Browser behavior is excluded and unchanged; packet regressions verify no next-stage dispatch on failure.

Run source/locked-source/committed-source validators and affected current manifest validators, backend `SIGNMONS_GOVERNANCE_REPO=<focused governance> node scripts/check-governance-baseline.mjs`, `npm run arch:check`; governance `node scripts/frozen-baseline-check.mjs`, `SIGNMONS_BACKEND_REPO=<focused backend> node scripts/docs-consistency-check.mjs`, and `node --test scripts/frozen-baseline-check.test.mjs scripts/execution-placement.test.mjs scripts/intelligence-alignment-check.test.mjs`; `git diff --check` in both. Preserve unrelated AGENTS.md and renewal evidence. Full application build/lint/database/browser gates are not affected by this isolated Python evidence-runner change; do not claim them newly passed.

## Alternatives, finish and rollback

Another full attended retry would retain the same ambiguity. Repeating SD4 alone would test current sessions again without reproducing the actual qualification query failure. Reusing the existing classifier on the actual boundary is the smaller correction. Effort is confined to two source/test files and nine hash manifests; no reliable elapsed-time estimate or live-success promise. Accepted milestones remain4/8, 3A OPEN, R1newlyclosed0/27.

Finish: all selected synthetic/process tests and blocking source/governance checks pass, all primary/cleanup faults retain safe categories without changing outcomes/calls, old R68/SD4 receipt hashes remain identical, and a local-only completion record is reviewable. This is implemented/local proof only, never live authentication/payment or owner acceptance. Rollback is reverting this isolated local change and matching derived hashes before any future separately approved packet; no provider rollback required. No scope deviation in investigation; explicit prospective local reporting/retention amendment only. Owner decision pending.
