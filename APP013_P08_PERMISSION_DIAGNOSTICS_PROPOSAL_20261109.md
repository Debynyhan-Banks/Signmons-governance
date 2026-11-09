# APP-013 / 3A / P08 — bounded permission diagnostic correction proposal

Status: PENDING_OWNER_APPROVAL. Local implementation only; no fresh qualification, credentials, provider reads or IAM change. Section R1-W01 / 3A / P08 remains unchanged. Backend source759a130164ae86237b5ee8a5fe540e935cc5d4d9; evidence HEADd16ba2d; Q4 closeout governancefc59450. User continuation authorized investigation, not this proposed implementation expansion.

## Demonstrated gap and customer relevance

Q4 immutable result OWNER_PERMISSION_NOT_READY has27CLI/7HTTPS/2SQL/1cache reservations and no candidate. Fixed sequential source places the refusal at project_permissions after six successful service checks. CurrentAdapter.read_access line740 collapses non200, unexpected keys, missing/null/wrong-type permissions, duplicate entries and permission-set mismatch into one error. NativeIO returns bounded response bytes to the adapter in memory, but no sanitized permission diagnostic survives. All27CLI returned. Missing permission names, HTTP status and cause remain UNKNOWN. Q4 cannot be diagnosed by replaying its consumed authority; private identifiers are already purged.

Google documents POST projects/{resource}:testIamPermissions and a returned subset of requested permissions. This supports retaining a safe requested-minus-returned result after strict shape validation; it does not establish Q4's actual cause. Sources inspected November9:
- https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/testIamPermissions
- https://docs.cloud.google.com/resource-manager/reference/rest/Shared.Types/TestIamPermissionsResponse

One existing focused test CurrentProofTests.test_each_permission_resource_missing_never_qualifies passed November9 through the actual composed adapter with synthetic IO. It confirms refusal and cleanup for empty permission results; it does not prove live permissions. No provider calls during investigation. Customer connection: resolving this exact prerequisite permits assessing the existing same-job Sandbox payment workflow; it adds no customer feature or acceptance section.

## Alternatives and proposed owner decision

1. Recommended: approve this bounded local diagnostic correction, then separately review any smallest fresh external qualification proposal after readiness. Do not repeat full recovery/qualification merely to obtain the same opaque error.
2. Defer with Q4 closed and all private material purged.

Granting broad IAM roles, dropping required permissions, accepting malformed responses, or blind retry are not justified by the evidence. No claim that diagnostics fix the underlying permission issue.

## Exact section card before coding

Acceptance: the existing permission-check boundary must retain only a bounded, allowlisted diagnostic sufficient to distinguish HTTP refusal, invalid response shape, missing requested permissions and complete match. Existing qualification success/refusal semantics and cleanup behavior stay unchanged. Never label malformed or non200 output as proven missing permission. Unknown fields/permission strings must never be copied to evidence.

Reuse CurrentAdapter.read_access/_https, QualificationIO/NativeIO, existing durable reservation/model.reserve and CURRENT_MARKERS/root inspection, _produce_current result/cleanup, existing permission fixtures and actual owned PostgreSQL/TLS crash tests. No new module, command, service, endpoint or standalone diagnostic transport.

Expected files: existing qualification_launch.py and test_qualification_launch.py; test_qualification_launch_postgres.py only if required to extend the existing crash fixture; source-manifest.json hashes; bounded section/result/governance evidence. SDK/locked dependencies, request descriptors, existing required permission lists and budgets unchanged.

Data contract: only existing permission descriptors (project, identity, seven secret checks, run) may generate diagnostics; at most one immutable outcome per descriptor. Bind operation and cleanup-scope hashes. Retain descriptor ID, validated HTTP status or null, a fixed outcome enum, and missing permission names drawn exclusively from that descriptor's source-pinned request list. Count bounds follow existing descriptors. For malformed/non200 replies, missing permissions must be null/UNKNOWN. No raw URL, project number, user UUID, response body, arbitrary permission/error text, tokens, credentials, headers or provider messages. Valid match produces an empty missing list. No recovery binding values are added to public evidence.

Durability: publish bounded diagnostics before raising the existing permission refusal; root allowlist and exclusive marker rules must account for these files. Failure to preserve diagnostics must fail closed with a fixed diagnostic-write error while independent cleanup still runs. Original failure must not be misrepresented as a permission denial. Interrupted records mean UNKNOWN, never fabricated completion. No change to raw-data purge/guard ownership or deadlines. Public sanitized evidence retention follows existing receipts.

Finite checklist:
1. Record actual owner decision before implementation. Complete exact schema/enums and source card, inspect existing coordinator failure/cleanup seams.
2. Add bounded permission outcome persistence through the existing actual parser/IO boundary, retaining all qualification predicates.
3. Test complete/partial/empty results, missing/null/wrong types, duplicates, foreign strings, extra keys, non200, malformed JSON/UTF8, output oversize and transport failure. Inject secret canaries; prove no raw data in markers/results/errors.
4. Test exclusive-write/duplicate concurrency, diagnostic-write failure and interrupted process recovery using existing harnesses. Prove no second dispatch, no candidate on failure, independent cleanup and owned private purge. Preserve failed-result distinctions; no invented HTTP status after transport refusal.
5. Run full existing producer/recovery/model/owned PostgreSQL TLS tests with pinned Python; governance frozen baseline, complete consistency,25 governance tests; backend architecture and both whitespace checks. No browser/app changes; later same-job browser/payment gates remain required for acceptance.
6. Record source/hash, actual tests, UNKNOWNs and disabled state. Prepare no external operation automatically.

Test command: pinned Python3.14 -B -m unittest test_qualification_launch test_composed_qualification test_qualification_launch_postgres in existing source directory. Existing November4 138 runtime/local tests remain historical until rerun after approved changes.

Dependencies and owners: implementer owns source/schema/privacy/concurrency tests and readiness; owner approves local change; credential/DB/provider roles separately approve any future external scope; admin permission change requires separate demonstrated need and explicit authorization. No outside account read is a prerequisite to this local correction.

Rollback: revert only the approved correction files to759a130 bytes; preserve immutable receipts and unrelated AGENTS.md. External entries remain disabled without fresh exact source-bound approval. No merge/push/deploy/billing/runtime activation or payment.

Observable finish: all local diagnostic cases pass at actual parser/transport boundary; finite evidence identifies what a later failure can safely report. This is locally tested observability, not current access proof or completed3A. No section/dependency/acceptance-count change; modest bounded instrumentation/test work, duration not yet verified. Accepted1A/1B/2A/2B4/8; R1newlyclosed0/27. Q4 cleanup verified; owner decision is next. **No scope deviation implemented; bounded correction proposed before coding.**
