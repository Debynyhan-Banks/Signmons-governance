# APP-013 / 3A / P08 — fresh exact key-absence qualification

**CONSUMED AND CLOSED:** KEY_ABSENCE_OBSERVED after15:00 UTC; independent cleanup15:00:42 PASS/no residuals. See APP013_P08_KEY_ABSENCE_RESULT_20261103.md. No repeat authorized. Earlier pending/start language is historical.

**OWNER APPROVED:** “i approve”, observed November3 14:44:50 UTC, for exact operationf5f91122-d2b6-4dc2-8af2-ef59acf7351c,15:00–15:10 UTC window/strict15:02 start, one cache/three read-only GETs/zero refresh-retry-mutations and mandatory cleanup. No key creation or broader qualification. Earlier pending language is historical.

**QUALIFICATION-ONLY; READY FOR EXACT OWNER DECISION, NOT AUTHORIZED.** Renewalc4ce8e9 ran once14:40:33–14:40:34, exit0, one postcheck valid strictly beyond15:10; independent owned-process/receipt cleanup14:41:04 PASS. No resource requests. Actual qualification rechecks credential/configuration drift.

Fresh operationf5f91122-d2b6-4dc2-8af2-ef59acf7351c replaces unapproved/unstarted651d475e-9344-47f1-b08c-abba317e17d9; earlier14:25–14:35 packet must not be used. Date-named decision/draft JSON now contain this new operation and remain PENDING. Prior versions are preserved in Git atc4ce8e9186652774d9dbf8a08e84372a3adc19cc; commit-specific reader prevents old/new mixing. Target remains the same uncreated prospective key; no creation authorized. Preparation at2026-11-03T14:41:48Z: no operational root/private plan/new credential/provider read.

## Exact source, target and time

- Operation f5f91122-d2b6-4dc2-8af2-ef59acf7351c; draft APP013_P08_KEY_ABSENCE_DRAFT_PLAN_20261103.json, SHA256 7a41f61ee1750f645979c90c439b8dc30b7d198e8f29a2bdcc69b8db4100825e.
- Scope c8a31d634dffbba3471681e2e98c0df08e2563a4915c93d9e03f227c3d5a1967; V4 contract 668095072a9d6baae2360a64b898fc807393a6e9d3a013d90354feb97d3112f4.
- Runtime SHA256 495258008e1e6454fda779724a3c3cfc85b27459af7e217ba39dd2ab24472d9e; manifest 3db5e61e6ec460a8425819c6ea0272dda8cf63606230ee9dd1fb63e1fa31528b; test manifest dc12ace939abfa306fbf5672b3e40a744e18c8c3ca1ddbc8f77765d8e320031d. All four source/test/manifest files match committed source 5be6d5772394062395f735e23c7ae32423180d14.
- Owner debynyhan@signmons.com, project signmons, identity signmons-calldesk-p07-runtime@signmons.iam.gserviceaccount.com is a pin only. Project-number fingerprint 37d4aa0f46ca5b8f0b81b1148bda235a0f4a9a424b6b4638ec993d889563be54; derive numeric resource only from the exact ACTIVE project response, never caller input.
- Prospective authentication b3bd682f-1a85-48ab-a242-879169e93571; exact derived key signmons-p08-b3bd682f1a8548aba242879169e93571, global location. Point-in-time absence only; no reservation, reuse/deleted-key exception, create/getKeyString permission or future availability claim.
- Exact executable /opt/homebrew/Cellar/python@3.14/3.14.2/Frameworks/Python.framework/Versions/3.14/bin/python3.14, SHA256 2cbb3ee843d8abcf93ed35bb9102391f18eefccb03d47908547bd8db67bc395c, -I -B; macOS/Python3.14.2/SQLite3.51.1.

November3,2026 only:

| Boundary | UTC | Eastern EST |
| --- | --- | --- |
| Start | 15:00:00 | 10:00 a.m. |
| Strict start cutoff | 15:02:00 | 10:02 a.m. |
| Read end | 15:04:00 | 10:04 a.m. |
| Independent closeout end | 15:09:00 | 10:09 a.m. |
| Private-plan purge end | 15:10:00 | 10:10 a.m. |

Proposed pins only. If prerequisite/approval/preparation is late, expire unstarted. Never slide the window, retry or reuse consumed authority. Decision APP013_P08_KEY_ABSENCE_OPERATION_20261103.json is PENDING_OWNER_APPROVAL.

## Exact action, output and exclusions

One cached-token read, at most three HTTPS GETs, zero CLI/refresh/retry/provider SQL/mutations. Cache implementation uses its tested local read-only SQLite query boundary, not application/provider SQL. Fixed ordered descriptors: Resource Manager projects/signmons?fields=projectId,projectNumber,lifecycleState; Service Usage projects/{verified-number}/services/apikeys.googleapis.com; API Keys v2 projects/{verified-number}/locations/global/keys/signmons-p08-b3bd682f1a8548aba242879169e93571. API state must be ENABLED; disabled/unknown stops without enabling. Fixed googleapis.com hosts from source, empty bodies, x-goog-user-project=signmons; memory-only bearer, no proxy/redirect, eight-second total per call clipped to read deadline and65536-byte body bound.

OnlyHTTP404/object error/exact status NOT_FOUND with absent or integer404 code yields KEY_ABSENCE_OBSERVED. Exact matching200 name yields KEY_PRESENT_STOP even with deleteTime.401/403 yield KEY_ACCESS_DENIED. Other status/name/error/missing/null/malformed/encoding/oversize responses are UNKNOWN/stopped, never absence. No alternate target or retries. Keep only sanitized result/counts/classification/target hash; no token/expiry/numeric project/metadata/provider messages retained.

No getKeyString/list/lookup/create/delete/undelete/update, IAM/service/billing/configuration changes, runtime/database/Firebase/job/payment, customer data/contact, deployment/merge/push or spending authority. Prior enablement remains historical ENABLED13:50:28, not current proof; this exact operation checks service again. Full nine-gate native qualification remains UNKNOWN.

## Shift-left readiness

| Prerequisite | Inspected evidence at 2026-11-03T14:41:48Z | Owner / result |
| --- | --- | --- |
| Committed source/executable/dependencies | Actual committed reader byte match for four files, executable and5 runtime SDK hashes plus21 SDK review hashes PASS; --check-source localTransportReady=true, ready=false | Implementer rechecks immediately before launch |
| Serialization/parser/missing-null/errors |101 tests at corrected5be6d57 include actual native transport and synthetic cache, strict metadata classification and source authority; not rerun as preparation | Implementer; future provider outputs UNKNOWN |
| Actual proposed packet binding | Five local checks PASS: actual committed source/synthetic exact approval, target drift, budget drift, strict cutoff, actual pending plan refused before root; no NativeIO | Implementer; operational root remains absent |
| Config/identity/access/API compatibility | Same actual environment/config/cache guard; pinned exact project and service before exact GET. Historical owner permissions/API state not usable-access proof | Executor/provider administrator; denied/unknown stops |
| Token valid strictly beyond15:10 | PASS: one SDK-renewal postcheck14:40:34; independent cleanup14:41:04, renewal consumed. Actual entry rechecks cache/config validity | Credential custodian/executor |
| Deadlines/one attempt/concurrency/interruption/cleanup | Source-pinned101 cases include each reservation, lock, independent cleanup, purge and persistent filesystem failure | Attended executor; manual fallback below, no automatic purge timer |
| Exact external authority | PENDING_OWNER_APPROVAL; local/preparation authority insufficient | Owner only after token prerequisite PASS |
| Full native/P08 prerequisites | Current billing/runtime/DB/Firebase/job and nine-gate qualification UNKNOWN/excluded | Existing owners, later scopes |

## Approval, launch and mandatory closeout

1. Prerequisite PASS as above. Obtain owner approval of this exact fresh three-read packet, then commit only the pending decision string to APPROVE_EXACT_P08_KEY_ABSENCE_READ; keep exact new operation/source/scope/target unchanged. Renewal approval alone is insufficient.
2. Read draft and approved decision through existing committed reader. Replace only decision commit/path/byte hash in memory. Compare actual command/source/dependencies/executable/resource pins/limits/scope/authority/time with this readiness record. At15:00 and strictly before15:02 exclusively create /private/tmp/p08-access-check-f5f91122-d2b6-4dc2-8af2-ef59acf7351c at0700; collision stops. Validate actual KeyAbsenceCapability with actual clock/committed reader, reserve plan.json at0600. If pre-plan validation fails remove only newly created empty root. Do not bypass a guard or silently rebaseline.
3. Invoke once. Any launch consumes authority even pre-marker refusal. No retry/refresh or alternate ID. Normal closeout closes handles, clears private references and purges plan; no secure-memory-erasure claim.
4. After parent exit independently acquire exact operation lock nonblocking. Verify owned root/allowed regular-single-link0600 files, source/operation/plan hashes, CLOSED journal, pending/outcome/residuals/result and absence of plan.json/journal-next.json before15:10. Preserve sanitized receipts/hashes and independent verification in backend evidence.
5. Interrupted matching attempt/journal/plan: confirm parent exit and exclusive lock, invoke --closeout-key-absence before15:09. It makes no credential/provider reads or replay; PROCESS_OUTCOME_UNKNOWN remains UNKNOWN. Never infer absence from incomplete transport.
6. Missing/unusable journal or persistent writes: after confirmed parent exit/exclusive lock, exact owned root/modes/inventory and original plan-byte hash, purge only owned plan and inventoried journal-next.json before15:10. Preserve original sanitized markers, report missing evidence/outcome UNKNOWN. Do not promote scratch, delete foreign files or claim automatic cleanup. Ownership/process uncertainty blocks manual deletion and must be reported. Never copy or purge original gcloud configuration/cache.

Commands only after exact approval and prerequisite PASS, from backend recovery:

```sh
/opt/homebrew/Cellar/python@3.14/3.14.2/Frameworks/Python.framework/Versions/3.14/bin/python3.14 -I -B evidence/APP-013/p08-narrow-access-check-local-20261101/source/access_check.py --key-absence /private/tmp/p08-access-check-f5f91122-d2b6-4dc2-8af2-ef59acf7351c/plan.json
```

Interrupted local closeout only:

```sh
/opt/homebrew/Cellar/python@3.14/3.14.2/Frameworks/Python.framework/Versions/3.14/bin/python3.14 -I -B evidence/APP-013/p08-narrow-access-check-local-20261101/source/access_check.py --closeout-key-absence /private/tmp/p08-access-check-f5f91122-d2b6-4dc2-8af2-ef59acf7351c/plan.json
```

Completed: fresh operation/draft/target/source binding, five local packet checks/readiness/cleanup; credential-validity prerequisite PASS. Remaining owner: exact fresh three-read decision; executor afterward: one bounded classification and independent cleanup. Accepted1A/1B/2A/2B4/8, R1 newly closed0/27, 3A open. **No scope deviation beyond approved renewal and evidence correction.**

Preparation checks PASS: baseline/cross-repository/docs consistency, architecture,25 governance safeguards and both whitespace checks. Actual source gate and five packet checks PASS. Documentation-only preparation; no fresh runtime-suite claim.

Evidence backend461d078185bff0c7ef84d1497ffa6dfca4ff7562. Final source/packet, architecture, baseline/cross-repository/docs consistency,25 governance safeguards and whitespace checks PASS. Prior101 runtime cases are unchanged-source evidence, not a new runtime-suite claim.
