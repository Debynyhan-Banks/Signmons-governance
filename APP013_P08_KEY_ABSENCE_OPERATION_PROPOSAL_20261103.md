# APP-013 / 3A / P08 — exact three-read key-absence packet

**BLOCKED/DO NOT LAUNCH: prerequisite token qualification stopped CACHED_TOKEN_EXPIRED14:20:17. Current packet unapproved and unstarted. Credential remedy and fresh qualification/window require separate authority.**

**QUALIFICATION-ONLY. PREPARED; BLOCKED ON CACHED-TOKEN VALIDITY. External decision PENDING; no launch requested yet.** Owner “proceed” authorized preparation from backendce36c1195acf31726e560e97b2c05432d19e79d1/governance357b97e. No runtime changes, real credential reads, provider requests or operational private root/plan. No key creation authority.

## Exact source, target and time

- Operation 651d475e-9344-47f1-b08c-abba317e17d9; draft APP013_P08_KEY_ABSENCE_DRAFT_PLAN_20261103.json, SHA256 0175bc7831f819d1d71f77101293a8ba7e3c1d7ddd9148d25e641ccfd5099630.
- Scope 7dcc5b18be3727df5598ec4da97b8eaf78a4aa74d207d541faf54e55e53d6605; V4 contract 668095072a9d6baae2360a64b898fc807393a6e9d3a013d90354feb97d3112f4.
- Runtime SHA256 495258008e1e6454fda779724a3c3cfc85b27459af7e217ba39dd2ab24472d9e; manifest 3db5e61e6ec460a8425819c6ea0272dda8cf63606230ee9dd1fb63e1fa31528b; test manifest 3815633210d40882110dd19b21026eaa26ab41df6881d6514a2badc1e7eef73f. All four source/test/manifest files match committed source ce36c1195acf31726e560e97b2c05432d19e79d1.
- Owner debynyhan@signmons.com, project signmons, identity signmons-calldesk-p07-runtime@signmons.iam.gserviceaccount.com is a pin only. Project-number fingerprint 37d4aa0f46ca5b8f0b81b1148bda235a0f4a9a424b6b4638ec993d889563be54; derive numeric resource only from the exact ACTIVE project response, never caller input.
- Prospective authentication b3bd682f-1a85-48ab-a242-879169e93571; exact derived key signmons-p08-b3bd682f1a8548aba242879169e93571, global location. Point-in-time absence only; no reservation, reuse/deleted-key exception, create/getKeyString permission or future availability claim.
- Exact executable /opt/homebrew/Cellar/python@3.14/3.14.2/Frameworks/Python.framework/Versions/3.14/bin/python3.14, SHA256 2cbb3ee843d8abcf93ed35bb9102391f18eefccb03d47908547bd8db67bc395c, -I -B; macOS/Python3.14.2/SQLite3.51.1.

November3,2026 only:

| Boundary | UTC | Eastern EST |
| --- | --- | --- |
| Start | 14:25:00 | 9:25 a.m. |
| Strict start cutoff | 14:27:00 | 9:27 a.m. |
| Read end | 14:29:00 | 9:29 a.m. |
| Independent closeout end | 14:34:00 | 9:34 a.m. |
| Private-plan purge end | 14:35:00 | 9:35 a.m. |

Proposed pins only. If prerequisite/approval/preparation is late, expire unstarted. Never slide the window, retry or reuse consumed authority. Decision APP013_P08_KEY_ABSENCE_OPERATION_20261103.json is PENDING_OWNER_APPROVAL.

## Exact action, output and exclusions

One cached-token read, at most three HTTPS GETs, zero CLI/refresh/retry/provider SQL/mutations. Cache implementation uses its tested local read-only SQLite query boundary, not application/provider SQL. Fixed ordered descriptors: Resource Manager projects/signmons?fields=projectId,projectNumber,lifecycleState; Service Usage projects/{verified-number}/services/apikeys.googleapis.com; API Keys v2 projects/{verified-number}/locations/global/keys/signmons-p08-b3bd682f1a8548aba242879169e93571. API state must be ENABLED; disabled/unknown stops without enabling. Fixed googleapis.com hosts from source, empty bodies, x-goog-user-project=signmons; memory-only bearer, no proxy/redirect, eight-second total per call clipped to read deadline and65536-byte body bound.

OnlyHTTP404/object error/exact status NOT_FOUND with absent or integer404 code yields KEY_ABSENCE_OBSERVED. Exact matching200 name yields KEY_PRESENT_STOP even with deleteTime.401/403 yield KEY_ACCESS_DENIED. Other status/name/error/missing/null/malformed/encoding/oversize responses are UNKNOWN/stopped, never absence. No alternate target or retries. Keep only sanitized result/counts/classification/target hash; no token/expiry/numeric project/metadata/provider messages retained.

No getKeyString/list/lookup/create/delete/undelete/update, IAM/service/billing/configuration changes, runtime/database/Firebase/job/payment, customer data/contact, deployment/merge/push or spending authority. Prior enablement remains historical ENABLED13:50:28, not current proof; this exact operation checks service again. Full nine-gate native qualification remains UNKNOWN.

## Shift-left readiness

| Prerequisite | Inspected evidence at 2026-11-03T14:13:12Z | Owner / result |
| --- | --- | --- |
| Committed source/executable/dependencies | Actual committed reader byte match for four files, executable and5 SDK review hashes PASS; --check-source localTransportReady=true, ready=false | Implementer rechecks immediately before launch |
| Serialization/parser/missing-null/errors |99 tests at unchanged ce36c11 include actual native transport and synthetic cache, strict metadata classification and source authority; not rerun as preparation | Implementer; future provider outputs UNKNOWN |
| Actual proposed packet binding | Five local checks PASS: actual committed source/synthetic exact approval, target drift, budget drift, strict cutoff, actual pending plan refused before root; no NativeIO | Implementer; operational root remains absent |
| Config/identity/access/API compatibility | Same actual environment/config/cache guard; pinned exact project and service before exact GET. Historical owner permissions/API state not usable-access proof | Executor/provider administrator; denied/unknown stops |
| Token valid strictly beyond14:35 | UNKNOWN. Prior qualification proved only beyond14:00; not proof of expiry or adequacy now | Owner/credential custodian; separate one-read qualification below |
| Deadlines/one attempt/concurrency/interruption/cleanup | Source-pinned99 cases include each reservation, lock, independent cleanup, purge and persistent filesystem failure | Attended executor; manual fallback below, no automatic purge timer |
| Exact external authority | PENDING_OWNER_APPROVAL; local/preparation authority insufficient | Owner only after token prerequisite PASS |
| Full native/P08 prerequisites | Current billing/runtime/DB/Firebase/job and nine-gate qualification UNKNOWN/excluded | Existing owners, later scopes |

## Approval, launch and mandatory closeout

1. Complete only separately approved APP013_P08_KEY_ABSENCE_TOKEN_CHECK_PROPOSAL_20261103.md. On failure, stop; no refresh. On PASS with time remaining, request exact three-read external decision. Commit only decision change to APPROVE_EXACT_P08_KEY_ABSENCE_READ in pending operation JSON; all target/scope/source fields unchanged.
2. Read draft and approved decision through existing committed reader. Replace only decision commit/path/byte hash in memory. Compare actual command/source/dependencies/executable/resource pins/limits/scope/authority/time with this readiness record. At14:25 and strictly before14:27 exclusively create /private/tmp/p08-access-check-651d475e-9344-47f1-b08c-abba317e17d9 at0700; collision stops. Validate actual KeyAbsenceCapability with actual clock/committed reader, reserve plan.json at0600. If pre-plan validation fails remove only newly created empty root. Do not bypass a guard or silently rebaseline.
3. Invoke once. Any launch consumes authority even pre-marker refusal. No retry/refresh or alternate ID. Normal closeout closes handles, clears private references and purges plan; no secure-memory-erasure claim.
4. After parent exit independently acquire exact operation lock nonblocking. Verify owned root/allowed regular-single-link0600 files, source/operation/plan hashes, CLOSED journal, pending/outcome/residuals/result and absence of plan.json/journal-next.json before14:35. Preserve sanitized receipts/hashes and independent verification in backend evidence.
5. Interrupted matching attempt/journal/plan: confirm parent exit and exclusive lock, invoke --closeout-key-absence before14:34. It makes no credential/provider reads or replay; PROCESS_OUTCOME_UNKNOWN remains UNKNOWN. Never infer absence from incomplete transport.
6. Missing/unusable journal or persistent writes: after confirmed parent exit/exclusive lock, exact owned root/modes/inventory and original plan-byte hash, purge only owned plan and inventoried journal-next.json before14:35. Preserve original sanitized markers, report missing evidence/outcome UNKNOWN. Do not promote scratch, delete foreign files or claim automatic cleanup. Ownership/process uncertainty blocks manual deletion and must be reported. Never copy or purge original gcloud configuration/cache.

Commands only after exact approval and prerequisite PASS, from backend recovery:

```sh
/opt/homebrew/Cellar/python@3.14/3.14.2/Frameworks/Python.framework/Versions/3.14/bin/python3.14 -I -B evidence/APP-013/p08-narrow-access-check-local-20261101/source/access_check.py --key-absence /private/tmp/p08-access-check-651d475e-9344-47f1-b08c-abba317e17d9/plan.json
```

Interrupted local closeout only:

```sh
/opt/homebrew/Cellar/python@3.14/3.14.2/Frameworks/Python.framework/Versions/3.14/bin/python3.14 -I -B evidence/APP-013/p08-narrow-access-check-local-20261101/source/access_check.py --closeout-key-absence /private/tmp/p08-access-check-651d475e-9344-47f1-b08c-abba317e17d9/plan.json
```

Completed: exact draft/target/source binding, five local packet checks/readiness/cleanup. Remaining owner: token qualification decision first; executor: result/closeout only if approved; owner later: separate exact three-read decision. Accepted1A/1B/2A/2B4/8, R1 newly closed0/27, 3A open. **No scope deviation.**

Preparation checks PASS: baseline/cross-repository/docs consistency, architecture,25 governance safeguards and both whitespace checks. Actual source gate and five packet checks PASS. Documentation-only preparation; no fresh runtime-suite claim.
