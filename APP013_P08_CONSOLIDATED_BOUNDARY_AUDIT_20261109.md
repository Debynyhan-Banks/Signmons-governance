# APP-013 / 3A / P08 — consolidated qualification boundary audit

Status: OWNER APPROVED LOCAL CORRECTION on November 9 ("i approve" following the consolidated proposal). Implementation and local validation complete; see completion below. Live-attempt hold remains. Owner's proceed authorized this review, not a new operation. No new attendance or password requested.

## Traceability and evidence

Section 3A/P08 existing prerequisite: current exact cloud/access/database/Firebase qualification before the same-job Sandbox payment journey. This review supports truthful prerequisite validation; it does not accept 3A or create a new section. Runtime source 99a4ef3aa340f5a4272787300dc3c499ea88a0aa; backend evidence HEAD 759e9fd; governance starting HEAD 798d3bc. Q8 result is CURRENT_EVIDENCE_UNQUALIFIED/CURRENT_READ_UNCONFIRMED, candidate absent; R16 purge verified. Q8's exact live role/SQL cause remains UNKNOWN. Source-order inference is not an ACL-drift diagnosis.

Inspected existing qualification_launch.py, test_qualification_launch.py, test_qualification_launch_postgres.py, access_check.py classifiers and current receipts. Reused CurrentProofTests and run_proof with synthetic overrides through the existing full reducer; no provider, CLI credential cache, private input or password read. All eight runs cleaned their synthetic roots and returned empty residuals.

| Synthetic input | Actual result at pinned source | Finding |
|---|---|---|
| Valid baseline | LOCAL_VERIFIED, candidate present | Positive control |
| Retired ACL empty | UNQUALIFIED, CURRENT_READ_UNCONFIRMED | acl.Stop category lost |
| Retired role missing expired field | Same refusal | acl.Stop category lost |
| Retired role login true | Same refusal | acl.Stop category lost |
| Firebase users contains null | Same refusal | Untyped user object causes generic exception |
| Duplicate role owner then admin in customAttributes | LOCAL_VERIFIED, candidate present | Duplicate JSON keys accepted |
| testOnly numeric 1 | LOCAL_VERIFIED, candidate present | Python equality treats 1 as True |
| Job intakeAdmission null | UNQUALIFIED, CURRENT_READ_UNCONFIRMED | Nested object lacks type check |

These are synthetic proofs of implementation gaps, not claims about live stored data. Existing actual-PostgreSQL ACL-drift test asserts candidate absence and session/process cleanup, but not failure category; therefore it misses error translation loss.

## Boundary coverage and limits

| Boundary | Inspected evidence and disposition |
|---|---|
| Source/authority/config/resource pins | Existing manifest, locked-source, capability and dynamic revision/environment checks reused; no relaxation proposed. Current live config/permissions UNKNOWN. |
| CLI serialization and cache | Existing strict_json and CLI diagnostics; cache translation already corrected at source99a4ef3. Historical tests reused, not newly rerun. Nested cloud shapes still need systematic negative test coverage in proposed correction. |
| HTTPS/service/permission/key | Existing status/body/size/deadline and descriptor checks; prior projection and NOT_FOUND fixes retained. Q8 ten permission receipts COMPLETE historically. No refetch of discarded bodies. |
| SQL projection/identity/job | Exact field/count checks and read-only query retained. Nested intakeAdmission null reproduced; target extraction and retired-role object must be checked before indexing. |
| Retired role helper | acl.Stop differs from model.Stop; specific safe categories lost at reducer. Reproduced three conditions. Never infer authority to alter roles/grants. |
| Firebase REST output | User object type, duplicate claims and exact boolean gaps reproduced. Keep exact identity, disabled state, claims keys, and revocation threshold. |
| Deadlines/no-retry/concurrency | Existing root reservation, lock, time gates and transport limits inspected; no change proposed. Existing tests must be rerun after correction. |
| Interruption/cleanup/persistence | Normal plus independent cleanup retained. Final inventory/expiry/candidate validation occurs after inner catch and can refuse without ordinary result; do not bypass these guards to force a success/result. Existing independent closeout remains authoritative. Require explicit negative regression for this path. |
| Safe diagnostics | Current generic result does not identify failing stage. Propose a fixed stage enum in existing result, no new command or raw-output receipt. Unexpected exceptions remain sanitized. |

Public primary schema cross-check: https://docs.cloud.google.com/identity-platform/docs/reference/rest/v1/projects.accounts/lookup and https://docs.cloud.google.com/identity-platform/docs/reference/rest/v1/UserInfo. REST users is an array of UserInfo; customAttributes is a JSON string, disabled boolean, validSince an int64 string in seconds. Keep seconds conversion; do not substitute SDK tokensValidAfterTime. Public documentation is not live account evidence.

## Approved finite local correction card

Acceptance criterion: malformed qualification output never yields a candidate; expected helper refusals preserve an explicitly allowlisted safe category; unexpected failures identify only a fixed stage and safe generic category; cleanup, pins, caps and one-attempt boundaries remain unchanged. This advances the connected payment journey by making its qualification trustworthy and actionable.

Expected files: existing qualification_launch.py, test_qualification_launch.py, test_qualification_launch_postgres.py and source-manifest.json; bounded evidence/handoff documentation. Reuse strict JSON duplicate-key rejection, existing classifiers, CurrentProofTests, actual PostgreSQL/TLS fixture, capability gates and closeout. No new subsystem.

Finite implementation checklist:
1. Validate nested database and Firebase objects before indexing; use exact claim key/value types, including testOnly is True, and reject duplicate claim keys through the existing strict parser.
2. Translate retired-role helper exceptions through an explicit fixed allowlist (ROLE_OUTPUT_UNKNOWN, ROLE_IDENTITY_UNKNOWN, ROLE_NOT_READY, ROLE_ACL_UNKNOWN, ROLE_ACL_DRIFT, ROLE_EXPECTATION_DRIFT); unknown exception content never persisted.
3. Record fixed stage only in existing sanitized result for preparation/cloud/access/database/Firebase/finalization, with consumer compatibility tests. Preserve refusal semantics when finalization cannot safely write a receipt; do not swallow inventory/authority failures.
4. Exercise all boundaries together: positive; missing/null/wrong-type nested structures; duplicate keys; bool-versus-number; role refusal categories; unexpected exception secret canary; no later reads after failure; exact reservation limits; interruption, concurrent entry, finalization refusal, normal and independent cleanup. Assert exact failure/stage, not only candidate absence. Actual PostgreSQL ACL drift must verify the category end to end.
5. Update manifest; run full existing three-module qualification suite, governance tests/checks, architecture and whitespace; record source SHA and results. Independently reconcile the whole matrix before lifting local readiness hold. No timed attempt as a substitute for missing local coverage.

Data/state/retention: same target/tenant/job/resource binding; synthetic tests only. No raw SQL/HTTP/user/claim/token/exception text persisted; stage and fixed categories only. Existing purge and independently verified cleanup unchanged. Exclusions: live recovery/qualification, role/IAM/resource changes, credential renewal, billing/payment calls, deployment, acceptance-count changes, and retries. Rollback/disabled state: keep current live hold; any failed local gate blocks readiness. Browser/customer journey code unchanged; browser acceptance remains later, not claimed by these tests.

Commands after implementation: pinned Python -B -m unittest test_qualification_launch test_composed_qualification test_qualification_launch_postgres from existing source directory; backend governance baseline and npm run arch:check; governance frozen baseline, cross-repo docs consistency and three required governance test files; git diff --check in both repositories. Tests must include actual existing transport/SQL boundaries, not replacement expectations copied from constants.

Owner roles/dependencies: implementer owns local correctness and complete test evidence; owner must approve this consolidated correction before implementation under AGENTS change-control instructions. Credential custodian/DB role have no action now. Any later external-only UNKNOWN requires separately scoped qualification-only authority, not an execution-ready claim. Proposed correction changes diagnostics/validation only; no section/dependency/count expansion.

## Handoff

Completed: consolidated source/schema review, eight synthetic reducer reproductions, finite correction card. Remaining: owner decision on this single local correction; implementation and full validation if approved; then current qualification, same-job Sandbox signed-event payment, negative/duplicate/replay and owner acceptance. Observable next result: one corrected local suite proving strict rejection, useful safe failure categories/stages and unchanged cleanup, before considering live work. Accepted 1A/1B/2A/2B remain 4/8; 3A OPEN; R1 newly closed 0/27. No scope deviation implemented; consolidated validation/diagnostic correction proposed before coding.

Audit recorded UTC: 2026-11-09T18:43:32.213895+00:00

Documentation validation: frozen baseline, cross-repository consistency, backend governance check, architecture and both whitespace checks PASS; 25 governance tests PASS. Eight synthetic audit cases newly executed; full runtime suite not rerun for this documentation-only review. Backend unrelated AGENTS.md preserved.

## November 9 — approved consolidated boundary correction complete locally

Owner approved the consolidated audit proposal before implementation. Backend f939224 (manifest9b0dd95a2549d0af4a42f90c6d28a1b56da4b99d8c9fb9a288830ef078fd675c) P08_CONSOLIDATED_BOUNDARY_CORRECTION_20261109.md records strict Firebase claims/duplicate-key/type rejection, nested database checks, fixed retired-role exception translation and failureStage in existing result. Finalization failures clear candidates; unsafe inventory/deadline still refuse publication. Pins, descriptors, limits, no-retry and independent cleanup unchanged. Eight new test methods plus strengthened actual PostgreSQL ACL test; full179tests PASS82.136s,then2new focused byte-boundary/preparation tests PASS(runtime unchanged),181distinct local tests plus25governance=206PASS. TLS server reaped/scratch absent/providerCalls0. No fixture promoted to live evidence; Q8 exact cause UNKNOWN.

All five approved local checklist items complete. Live-attempt hold retained; no new window/password/recovery/provider operation. Next observable result: owner review of consolidated local evidence; any later qualification must separately resolve current external UNKNOWNs under exact authority. Remaining full qualification and same-job Sandbox signed-event payment/negative/duplicate/replay/owner acceptance. 3A OPEN,accepted4/8,R1newlyclosed0/27. No scope deviation.
