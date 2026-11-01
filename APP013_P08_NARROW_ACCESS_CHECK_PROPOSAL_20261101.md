# APP-013 / 3A / P08 — narrow access qualification and entry decision

**Owner decision / local result:** Owner approved the bounded local adapter and tests with “yes i agree”. Implementation and 29 local cases are complete; see `APP013_P08_NARROW_ACCESS_LOCAL_RESULT_20261101.md`. Native execution remains blocked on the inspected SDK retry contract. The original preimplementation proposal below is retained as history; pending-approval language there is superseded only for local implementation. No external action was approved.

**Decision-ready local change proposal; NOT launch-ready.** Owner requested preparation with “let proceed” after the November 1 next-step explanation. That authorizes this source inspection and proposal, not new runtime code or an external operation. No credential, account read, provider change, operation UUID or live time window was created.

## Fixed purpose and current evidence

Section R1-W01 / APP-013 / 3A retains the same-admitted-job Sandbox Checkout → authentic matching signed settlement → failure/replay → owner acceptance criterion. This check answers which access prerequisite needs owner/provider-administrator action before that connected workflow. It cannot qualify payment, the runtime or the customer journey. Accepted 1A/1B/2A/2B remain 4/8; newly closed R1 0/27. R10 remains consumed/no retry.

Resolved checkouts: backend `/Users/debynyhanbanks/Web Projects/signmons-backend-r08-recovery`, governance `/Users/debynyhanbanks/Web Projects/signmons-governance-r08-recovery`. Both branch `codex/p06-r08-recovery-20260918`; HEADs `d5f1f876e8f17f8236d2262d1856a6fa323a86a4` and `996cc7fb5be906ddf64d1d337c7fa6dc24a3a001`. Remotes match the backend and Signmons-governance repositories; remote tips were not refreshed. Existing dirty changes are preserved. Inspection and actual source validators completed November 1, 2026, by 13:51 UTC. Before-change frozen baseline and cross-repository consistency passed.

Historical R10 evidence says API Keys disabled, prospective key absence denied, exact roles not matched, dedicated bindings absent; Cloud 13/13 and read-only closeout passed then. Those are October 29 observations, not current facts. Role normalization was subsequently corrected locally. The November 1 native integration has passing local evidence, but no live qualification or external authority. All current account/provider facts remain UNKNOWN.

## Demonstrated execution gap

The earlier handoff identified a narrow check as the next deliverable but did not establish a callable narrow read entry. This inspection resolves that uncertainty:

- Existing `qualification_launch.Adapter.read_access()` calls `_prime_access_http()`, which calls `_prime_cli()` and runs **all 26** CLI descriptors: billing, Cloud Run, identity, secret state/policies, IAM policies and roles. Calling it directly is not a narrow access check.
- `validate_binding()` requires exactly 26 CLI / 10 HTTPS / 2 SQL limits. Its `native()` requests a CHILD password before constructing the coordinator; its closeout uses SQL. Changing only a limit or skipping `_prime_cli` would bypass its tested contract.
- New `p08-native-entry-local-20261101/source/entry.py --run` owns mutations, and its outer `Capability` requires already-qualified database/Firebase/runtime/job/billing facts. Its `NativeIO` also pins the database and omits the Resource Manager/IAM permission-test hosts. It cannot be repurposed by forging qualification booleans or invoking private transport methods without its authority.
- Existing `composed_qualification.PERMISSIONS` lists nine permissions but omits `serviceusage.services.get`, `serviceusage.services.enable`, and `serviceusage.services.use`. Those cover the selected service read, possible later enablement and explicit quota-project header. Their inclusion below is a proposed read-contract change, not a silent edit to historical source or authorization to enable anything.

**Consequence:** no current validated command enforces the requested narrower scope. Do not run the 26-command launcher, the mutation entry, or an ad hoc bearer script as a workaround. The missing behavior is a small, explicit read-only entry around existing parsers and bounded I/O patterns. No such entry has been implemented in this task.

## Inspected source pins and reuse

Paths relative to backend `evidence/APP-013/`; these hashes were recomputed during this task.

| Source | SHA256 | Reuse / constraint |
| --- | --- | --- |
| `p08-role-contract-local-20261029/source/qualification_launch.py` | `76722d3265cda655b6b2433bc83d3bbcee06c12c6d0f66c07cad9fe2ae2e7e18` | Bounded JSON/HTTPS error classification and exact projected read contracts; do not call broad adapter/native entry. |
| `p08-role-contract-local-20261029/source/composed_qualification.py` | `2c2f9603cb71957239816f4942549be8277c446cbcc5f2b7bae1f139fd552df4` | Fixed project/owner/identity and nine permission strings; its broad coordinator is excluded. |
| `p08-exact-role-provisioning-local-20261028/source/role_provisioner.py` | `e1fbc15d95450da7662db684e2cfe6f063c8a60fd7c8243053e5431fc3f973f9` | Reuse `ROLES` and strict `definition_shape`; no role writes. |
| `p08-restoration-local-20261028/source/restore.py` | `a0bf4bc90cca0bd52935915d710ccb44e065dd3deed841a12ab49cb3ac4a1cb9` | Existing environment/config guard and canonical identity; no restoration controller. |
| `p08-native-entry-local-20261101/source/authority.py` | `763dd24f5dac70b3ec87d350ab2efc6d0fe110aae9f261708aba8c54e481e365` | Source/committed-decision hashing pattern; existing mutation capability remains unchanged and cannot authorize this read. |
| `p08-native-entry-local-20261101/source/native_io.py` | `4eca2d6a66b3616db59380d635be8937291b4dd50fd290e727caf578c2c8f498` | Bounded owner/override/token, timeout, redirect refusal and in-memory credential patterns; class cannot be directly reused with fabricated authority. |
| `p08-native-entry-local-20261101/source/private_inventory.py` | `7996957c8cab7374b683f4db5d46c6536d8ba4023d8395edd1ed163a3bc03b78` | Exclusive reservation, private mode/link and owned-file inventory pattern. |
| `p08-native-bridge-local-20261029/source/bridge.py` | `58835555ea5d062bd84af91ace67c71762b9332a2f6fd9bf31ecec08c7a7dfce` | Exact project/role projection and `key_service_get` contract. |

Actual old `verify_local_manifest()` / `verify_locked_sources()` and new `authority.verify_sources()` PASS today; old `cli_contract()` returned its exact 26 descriptor IDs. No native entry, credentials or transport was invoked by these validations. Earlier runtime test results are historical for this documentation task, not newly rerun results.

## Proposed finite read contract

Eight CLI invocations maximum, each once; three direct HTTPS calls maximum, each once. Source and exact authority must validate and the attempt must be reserved before CLI use. CLI executable `/opt/homebrew/bin/gcloud`; exact active owner `debynyhan@signmons.com`; project `signmons`; service account `signmons-calldesk-p07-runtime@signmons.iam.gserviceaccount.com`. Numeric project number is discovered only from the exact project read and compared in memory to SHA256 `37d4aa0f46ca5b8f0b81b1148bda235a0f4a9a424b6b4638ec993d889563be54`; it is never guessed or written to public evidence.

| Order | CLI arguments after the pinned executable | Required classification |
| --- | --- | --- |
| 1 | `auth list --filter=status:ACTIVE --format=value(account)` | Exact single owner; no alternate account, login or fallback. |
| 2 | `config get-value auth/impersonate_service_account` | Empty or `(unset)` only. |
| 3 | `config get-value auth/credential_file_override` | Empty or `(unset)` only. |
| 4 | `config get-value auth/access_token_file` | Empty or `(unset)` only. |
| 5 | `projects describe signmons --format=json(projectId,projectNumber,lifecycleState)` | Exact active project and matching numeric-project fingerprint. |
| 6 | `iam roles describe signmonsP08FirebaseUserLookup --project=signmons --format=json(name,title,description,includedPermissions,stage,deleted,etag)` | Strict existing role validator: explicit false or omitted `deleted`; null/deleted/broader/wrong/extra fields refuse. |
| 7 | `iam roles describe signmonsP08ServiceAccountSignBlob --project=signmons --format=json(name,title,description,includedPermissions,stage,deleted,etag)` | Same strict definition validator for signing role. Metadata alone does not prove effective access. |
| 8 | `auth print-access-token --account=debynyhan@signmons.com` | One token retrieval, memory only, after identity/project/role gates; no token in argv/log/result/private file. |

Before these invocations, use the inspected local environment/configuration checks: refuse alternate Cloud SDK config root, inherited credential overrides, `PG*`/`DATABASE_URL`; verify persisted auth override absence. Explicit project selection and `x-goog-user-project: signmons` bind routing/quota. No environment variable may authorize execution. Installed gcloud resolves to version-directory `583.0.0`; the actual executable/runtime must be pinned at implementation/launch. CLI limits count invocations, not underlying SDK HTTP attempts: internal refresh/retry behavior remains an explicit local implementation verification obligation, not an assumed no-retry guarantee. No unsupported global retry setting is proposed.

HTTPS allowlist, in this order after gates:

1. `POST https://cloudresourcemanager.googleapis.com/v1/projects/{verifiedNumber}:testIamPermissions`, body exactly `{"permissions":["resourcemanager.projects.getIamPolicy","resourcemanager.projects.setIamPolicy","apikeys.keys.create","apikeys.keys.get","apikeys.keys.getKeyString","apikeys.keys.delete","serviceusage.operations.get","serviceusage.services.get","serviceusage.services.enable","serviceusage.services.use"]}`.
2. `POST https://iam.googleapis.com/v1/projects/-/serviceAccounts/signmons-calldesk-p07-runtime@signmons.iam.gserviceaccount.com:testIamPermissions`, body exactly `{"permissions":["iam.serviceAccounts.getIamPolicy","iam.serviceAccounts.setIamPolicy"]}`.
3. `GET https://serviceusage.googleapis.com/v1/projects/{verifiedNumber}/services/apikeys.googleapis.com`, no body; require exact resource name and state `ENABLED` or `DISABLED`.

POST permission tests only inspect the caller's current permission set; they do not grant permissions. Return only requested permission names and classifications. Valid empty permission results mean no tested grant; null, malformed lists, duplicates, nonstrings, foreign permission names, wrong status/encoding or oversized output are UNKNOWN and stop. Parse missing repeated `permissions` according to the documented empty response contract, with a specific fixture; do not treat it as all granted. A successful project read is required separately from a permission response. Successful permission tests are current observations only; they do not prove later conditional IAM evaluation, usable signing, native key restrictions or end-to-end authentication.

Abort on the first identity/source/config/role/output/deadline/permission failure and record remaining checks NOT_RUN. A valid DISABLED service observation is a resolved blocker, not UNKNOWN or permission to enable it. If all specified permissions are observed and the service is ENABLED, report only `NARROW_ACCESS_OBSERVED`; full P08 remains unqualified. If DISABLED, next owner decision concerns the already-designed service-enablement/retention operation. No automatic remediation or repeated read follows either result.

**Excluded:** key absence/getKeyString/create/delete, IAM policies/bindings/writes, API enable/disable, Policy Troubleshooter, billing, runtime/secrets/traffic, CHILD/SQL, Firebase account reads/writes, signing/custom-token exchange, application calls, Stripe/payment, customer data, deployment, spending and broad qualification. The unresolved historical key-absence denial is intentionally not retried here; it remains a later exact-key gate after an access/service decision.

## Timing, ownership, privacy and closeout requirements

Proposed duration only, not a scheduled operation: `T0` start; start cutoff `T0+2m`; read deadline `T0+4m`; independent closeout deadline `T0+9m`; private-input purge deadline `T0+10m`. The future operation record must contain absolute UTC values, one preselected operation UUID, exact source/request hashes and owner approval before any private input exists. No rolling/rebased start time and no retry. At most eight seconds per CLI/direct HTTP call, further capped by remaining read time; output maximum 65,536 bytes, redirects refused. These bounds require implementation tests before approval for execution.

Proposed one private root `/private/tmp/p08-access-check-<operationId>`, mode 0700, regular single-link 0600 files only: `plan.json`, `attempt.json`, `journal.json`, `journal-next.json`, `closeout.json`, `independent-closeout.json`, `entry.lock`, `result.json`. Exact inventory and atomic-update rules must be tested; reject foreign/symlink paths without sweeping them. Reserve once before credentials; lock entry for concurrency. Retain only sanitized operation/source hashes, ordinal call reservations, timestamps, classification and cleanup receipts. No raw owner/provider responses, token, numeric project number or configuration contents in retained journal/result.

Independent cleanup must be executable after the start/read cutoff using its own one-use reservation and the same owned inventory. Stop/reap owned subprocesses, close response bodies, clear in-memory token references and purge the exact plan/unfinished owned private temporary inputs with absence readback. Do not claim secure erasure of immutable process-memory copies. Never kill unrelated PIDs or infer process death from a reused PID; lack of verifiable ownership is CONTAINMENT_UNCONFIRMED. Abrupt process termination requires independently verifiable cleanup, not an optimistic finally block. No database/provider mutation occurs, so cleanup requires zero provider/SQL calls. It may not retry any read or refresh a token. A pending or failed cleanup remains explicitly unconfirmed.

## Readiness record and smallest decision

Evidence inspected at the timestamp/source pins above. The present proposal is documentation-only. No live execution approval is requested while local entry prerequisites are missing.

| Prerequisite | Result now | Responsible owner / next observable evidence |
| --- | --- | --- |
| Frozen baseline, queue and acceptance scope | PASS before edits; final governance gates required below | Implementer; unchanged section/denominator. |
| Existing source validators/read contracts | PASS; exact broad fan-out confirmed | Implementer; source inspection above. |
| Exact narrow entry/approval/request allowlist | MISSING — neither current launcher enforces this read set | Owner decides bounded local adaptation below; implementer proves it through its actual entry. |
| Service get/enable/quota permission coverage | Three omissions found in old list; exact proposed additions traced to provider docs | Owner approves this proposed contract; implementation tests exact arrays. |
| Missing/null/oversized response and error behavior | Reusable parsers inspected; new assembled path NOT TESTED | Implementer; positive/negative serialized fixtures at actual entry. |
| One attempt, internal retry behavior, deadlines, interruption and independent purge | Patterns exist; new path NOT TESTED, CLI internal behavior UNKNOWN | Implementer resolves locally before execution approval. |
| Current owner/role/permission/service facts | UNKNOWN; historical observations not refreshed | Owner authorizes exact future read; provider administrator owns any denied access/remediation. |
| Committed narrow source, operation/decision/time pins | ABSENT | Implementer prepares after local proof; owner approves exact external action last. |
| Full P08 billing/runtime/database/Firebase/job/key/auth readiness | UNKNOWN and excluded from this check | Later bounded qualification/operation; no broad R10 replay. |

**Recommended decision:** approve local-only implementation/testing of one narrow read adapter, not execution. Expected fresh directory `evidence/APP-013/p08-narrow-access-check-local-20261101/`; one runtime module `access_check.py`, one focused `test_access_check.py`, separate runtime/test manifests, section card and result. Reuse the source-pinned parsers/role definition/environment checks. Adapt the bounded owner/HTTP primitives only as needed for the explicit read capability, exact three-host allowlist, one attempt and local-only cleanup. No second authentication/mutation coordinator, package, schema, application feature or rewrite of historical/new native source. The exact request inventory above is the ceiling; larger dependencies or permission/resource changes require a new decision before implementation.

Finite implementation checklist under that approval:

1. Complete the new section card with these source/interface/state/retention boundaries before coding; bind a committed exact read-only owner decision and source. Missing/local-only authority must refuse native transport before owner/token lookup. Local tests inject all external primitives.
2. Implement only this read selection and strict classifications; no broad adapter/coordinator calls, database password prompt, mutation route or generic command/URL passthrough.
3. Prove final entry + independent closeout with serialized synthetic outputs: exact roles with omitted/explicit deleted; empty/null/missing/foreign permissions; wrong owner/project/config/source; service disabled; denial/non-JSON/oversize/redirect; expiry/clock rollback; duplicate/concurrent attempt; interruption around every call reservation; owned child cleanup; symlink/foreign file; purge and secret non-disclosure; native refusal without exact external authority. Resolve SDK retry behavior explicitly. Browser/SQL gates are inapplicable because those interfaces are excluded.
4. Finalize manifests before actual source/entry validation. Run focused tests, architecture and required baseline/consistency/25 governance safeguard/whitespace gates. Record failed attempts and corrections without weakening expectations. Then prepare the exact separately approved external operation, or report the specific remaining blocker. No extra local subsystem is implied.

Impact: one internal prerequisite adapter, moderate bounded engineering effort; no new acceptance section, dependency reordering, customer feature or external cost authority. Rollback discards only the fresh adapter and its handoff references. Observable local finish is a source-pinned narrow entry with tested refusal/closeout and zero provider calls. Native execution remains unavailable without separate exact external authority.

Alternative: the owner/provider administrator supplies current source-identifiable evidence for the same project/service/permission questions; inspect its scope/time/identity and mark missing facts UNKNOWN. This avoids new adapter code but does not substitute screenshots or role membership for effective permissions. No outreach is authorized. Another alternative is to defer the selected native path. Repeating broad R10 or weakening its validator is rejected.

## Public contract verification

Official documentation read November 1, 2026. Only public documentation was accessed; no authenticated project endpoint was called.

- [Service Usage services.get](https://docs.cloud.google.com/service-usage/docs/reference/rest/v1/services/get) requires `serviceusage.services.get` and returns service configuration/state.
- [Service Usage services.enable](https://docs.cloud.google.com/service-usage/docs/reference/rest/v1/services/enable) requires `serviceusage.services.enable`; the enable method is excluded from this read proposal.
- [Quota-project permissions](https://docs.cloud.google.com/docs/quotas/set-quota-project) identifies `serviceusage.services.use` for the explicit quota-project header.
- [Project permission test](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/testIamPermissions) and [service-account permission test](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/testIamPermissions) define the two caller-permission read contracts. No wildcard permissions are proposed.

## Task completion and authority

Final documentation verification on November 1, 2026, at 13:51 UTC: frozen baseline, cross-repository/docs consistency, backend architecture and both whitespace checks PASS; 25 governance safeguard tests PASS. Existing actual source validators also PASS. No runtime test of a proposed narrow adapter is claimed.

Completed now: reconciled governance/source/dirty worktrees, inspected actual read/authorization/cleanup interfaces, verified source gates, defined finite requests/output/timing/retention, documented the missing entry and alternatives. Remaining/owner: decide this local adaptation or administrator-evidence alternative. Remaining/implementer after that decision: only the selected bounded deliverable, then exact external operation approval. No code or provider action was taken to fill the gap.

Repository `AGENTS.md` requires: “Do not change scope, dependencies, section IDs/counts, acceptance criteria or substantial prerequisites without explicit owner approval BEFORE implementation.” This proposal adds a distinct qualification entry and modifies the permission read set, so implementation approval must precede that work. The user's preparation instruction is not recorded as approval of this newly discovered prerequisite. No execution approval is sought now.

**Explicit prerequisite change proposal; no deviation implemented.** 3A open; accepted 4/8; newly closed R1 0/27. Local native integration remains complete on its recorded scope; the new narrow check is unimplemented and unapproved.
