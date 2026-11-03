# APP-013 / 3A / P08 — fresh six-read access qualification

**OWNER APPROVED — November 3, 2026:** owner said “i approve the fresh six read qualification” in response to the exact 8:15–8:25 a.m. EST packet, strict 8:17 start cutoff, one attempt/no refresh/no retry/no configuration changes/spending. Approval observed 13:07:28 UTC. The new decision JSON records APPROVE_EXACT_P08_NARROW_ACCESS_READ with unchanged operation, scope, source and time pins. Earlier pending language below is historical. No private operation plan or qualification request has been made; start awaits 13:15 UTC. This is qualification-only, not payment/runtime authority.

Renewal evidence committed at backend `b2d610aa0d3dd37154bf87a2900a8226269deed5`; final packet source/binding/baseline/consistency/architecture/whitespace checks and 25 governance safeguards PASS. Exact new external decision remains PENDING.

**PENDING EXACT OWNER APPROVAL. Qualification-only, not broader runtime/payment execution.** The SDK renewal finished and the cached-token prerequisite passed; that approval does not launch this new operation. No new operation-private root or plan exists.

## Exact decision and window

Approve one attempt for **29e9ebff-2b7c-43a5-b459-217910a1475f** on **November 3, 2026**, under the unchanged cached-only/no-retry six-read source:

| Boundary | UTC | Eastern (EST) |
| --- | --- | --- |
| Start | 13:15:00Z | 8:15 a.m. |
| Strict start cutoff | 13:17:00Z | 8:17 a.m. |
| Read deadline | 13:19:00Z | 8:19 a.m. |
| Independent closeout deadline | 13:24:00Z | 8:24 a.m. |
| Private-plan purge deadline | 13:25:00Z | 8:25 a.m. |

No start before 13:15 or at/after 13:17; no rolling window, retry or renewal. If not approved/prepared in time, expire unstarted. Executor must remain available through verified closeout. No unattended scheduler is installed. USD 0 incremental spending authority, no resource/configuration changes, customer/payment action, merge, push or deployment.

## Source, request and identity pins

- Source commit `8e35617dc178ac8ce757548fac830b0013108ad7`; runtime `evidence/APP-013/p08-narrow-access-check-local-20261101/source/access_check.py`, SHA256 `861b0f549488fa3c281d2c4a7b3807c6c83bfa6f2a4d0a535367d2c2f0164b4d`.
- Runtime manifest `dc687b5bc36264c57c75154122d406393d2e3711853332e5e57112c881ec9597`; separate test manifest `007d40ec05a27e755c606b1f1e13054462ea01e6fe90194e503afbd0a339df53`; prior 49 local cases at unchanged hashes, not new live proof.
- Version-2 contract hash `0141eada196370aadab786cd84339e4adea5df0d94b0a2410a60e99de8e5dea9`.
- New exact scope hash `05223c525eed846f721607601639844945719f34816014ef1f595ede19cb216b`.
- `APP013_P08_ACCESS_READ_DRAFT_PLAN_20261103.json`, file SHA256 `4daaea31284038e4c15e469db84440348b34d0331003880b0696f698a7648384`.
- `APP013_P08_ACCESS_READ_OPERATION_20261103.json` currently PENDING_OWNER_APPROVAL, file SHA256 `7a67771b7b5ad1ed4bae9befe254877fa7ec4916591ba6e50f5f0e83962c90a4`. No synthetic or old approval can authorize it.
- Exact Python executable `/opt/homebrew/Cellar/python@3.14/3.14.2/Frameworks/Python.framework/Versions/3.14/bin/python3.14`, SHA256 `2cbb3ee843d8abcf93ed35bb9102391f18eefccb03d47908547bd8db67bc395c`, invoked with `-I -B`; macOS/Python 3.14.2/SQLite 3.51.1.
- Owner debynyhan@signmons.com; project signmons; identity signmons-calldesk-p07-runtime@signmons.iam.gserviceaccount.com. Derived project number must match fingerprint `37d4aa0f46ca5b8f0b81b1148bda235a0f4a9a424b6b4638ec993d889563be54`; no numeric project supplied by the caller or retained in receipts.

One reserved local cache read, zero CLI, up to six HTTPS, zero application/provider SQL/mutations/retries. Configuration/cache guard, exact existing role definitions, twelve permission names, eight-second per-call total bound, 65536-byte output limit, redirect/proxy refusal and independent local cleanup remain unchanged. The SDK renewal exception is not used here.

Ordered descriptors:

1. GET Resource Manager V1 `projects/signmons?fields=projectId,projectNumber,lifecycleState`.
2. GET IAM V1 `projects/signmons/roles/signmonsP08FirebaseUserLookup?fields=name,title,description,includedPermissions,stage,deleted,etag`.
3. GET IAM V1 `projects/signmons/roles/signmonsP08ServiceAccountSignBlob?fields=name,title,description,includedPermissions,stage,deleted,etag`.
4. POST Resource Manager V1 `projects/{verified-number}:testIamPermissions`, exactly resourcemanager.projects.getIamPolicy/setIamPolicy; apikeys.keys.create/get/getKeyString/delete; serviceusage.operations.get, serviceusage.services.get/enable/use.
5. POST IAM V1 `projects/-/serviceAccounts/signmons-calldesk-p07-runtime@signmons.iam.gserviceaccount.com:testIamPermissions`, exactly iam.serviceAccounts.getIamPolicy/setIamPolicy.
6. GET Service Usage V1 `projects/{verified-number}/services/apikeys.googleapis.com`.

Hosts are respectively cloudresourcemanager.googleapis.com, iam.googleapis.com and serviceusage.googleapis.com. Permission-test POSTs do not modify permissions. Requests use in-memory bearer and x-goog-user-project=signmons. Short-circuit on refusal; disabled service never permits enablement. No OAuth refresh, metadata/ADC fallback, new auth scopes, key creation, billing, Cloud Run, database, Firebase user/session, job or payment probe.

## Current readiness and responsibility

| Prerequisite | Evidence/status | Responsible role |
| --- | --- | --- |
| SDK renewal and usable cached token | Approval c9ab51d; one SDK command exited 0 at 13:01:07 UTC; one existing-cache postcheck VALID_THROUGH_CUTOFF for 13:30; owned leader reaped/group absent, no raw output retained | Completed by executor under separate one-time exception |
| Exact source/dependencies/executable | Original approved hashes and all 21 SDK review hashes match; actual source gate passes with localTransportReady=true and ready=false | Implementer rechecks immediately before launch |
| Request output contracts, serialization, errors, concurrency/deadlines/cleanup | Existing source-pinned 49 local cases; unchanged six-read entry and strict role/project parsers. Fixtures are not current provider evidence | Implementer |
| Fresh packet/committed binding | New UUID/scope/window and pending record; local validation must show pending refusal, actual committed source binding and exact cutoff rejection without NativeIO | Implementer; no real operation root until approval/start |
| Current configuration/token at launch | Postcheck was valid through 13:30; fresh operation still guards configuration/cache drift and requires expiry beyond 13:25 | Executor; renewal observation does not rule out revocation/change |
| Effective owner access/roles/API availability | UNKNOWN; purpose of this qualification | Owner/provider administrator for remediation if refused |
| Billing/runtime/Firebase/job/key/payment/full qualification | UNKNOWN and excluded | Later separately approved work |
| Exact external owner decision | PENDING | Owner |

Renewal evidence: backend `evidence/APP-013/p08-narrow-access-check-local-20261101/CREDENTIAL_RENEWAL_RESULT_20261103.md` and `renewals/20261103-1300/`. Source/execution observations are timestamped there. Fresh packet-binding evidence is `APP013_P08_ACCESS_READ_PACKET_CHECK_20261103.json`. This readiness record is linked from the current backend section card. Final documentation/baseline/consistency/architecture/whitespace and 25 governance checks are recorded at packet closeout; no runtime retest is claimed for unchanged code.

## Exact approval-to-launch and closeout procedure

1. After actual approval of this packet, change only the new decision JSON's `decision` to APPROVE_EXACT_P08_NARROW_ACCESS_READ and commit the owner's decision. Derive that exact commit/byte hash with the existing committed reader. Replace only the draft plan's decision reference; non-decision fields/scope above must remain identical. Never reuse the November 1 record or the SDK-renewal exception.
2. Before launch compare actual command, source/dependencies/executable, committed decision/scope, UTC clock and unused root. Drift or missing evidence stops. At/after 13:15 and before 13:17, exclusively create `/private/tmp/p08-access-check-29e9ebff-2b7c-43a5-b459-217910a1475f` (0700). Validate the in-memory plan against it using actual `ReadCapability`, clock and default committed reader; exclusively write plan.json (0600) using existing reserve. If validation fails while the newly owned root is empty, remove only that empty root. Collision never permits deletion/reuse.
3. Invoke the exact read command below once. First launch consumes authority, even refusal before a runtime marker; do not repeat. The existing journal reserves cache/HTTP events before dispatch. Token stays memory-only; no raw outputs/numeric project/expiry in receipts.
4. Normal closeout must close handles, clear references and purge plan.json, then verify absence. If interrupted with attempt/journal evidence, confirm parent exit and obtain exclusive operation lock; invoke the closeout command before 13:24. It performs zero credential/provider reads and reports pending events UNKNOWN rather than replaying them.
5. If no usable attempt/journal exists, verify exact owned inventory/plan hash/source/operation, parent exit and exclusive lock, and purge only the matching private plan before 13:25. Preserve sanitized markers and report missing/unconfirmed evidence; never manufacture success. Foreign files, uncertain ownership or active parent blocks cleanup and must be reported. This is a manual bounded closeout duty, not an automatic timer claim.
6. Verify final allowed inventory and private plan/temporary-journal absence before deadline; retain sanitized attempt/journal/closeout/result and independent verification, record consumed or expired-unstarted. No memory secure-erasure promise. Original credential cache is neither copied nor purged by this qualification.

After approval/preparation only, from the backend recovery checkout:

```sh
/opt/homebrew/Cellar/python@3.14/3.14.2/Frameworks/Python.framework/Versions/3.14/bin/python3.14 -I -B evidence/APP-013/p08-narrow-access-check-local-20261101/source/access_check.py --read /private/tmp/p08-access-check-29e9ebff-2b7c-43a5-b459-217910a1475f/plan.json
```

Independent command only if step 4 requires it:

```sh
/opt/homebrew/Cellar/python@3.14/3.14.2/Frameworks/Python.framework/Versions/3.14/bin/python3.14 -I -B evidence/APP-013/p08-narrow-access-check-local-20261101/source/access_check.py --closeout /private/tmp/p08-access-check-29e9ebff-2b7c-43a5-b459-217910a1475f/plan.json
```

Allowed private inventory remains plan.json, attempt.json, journal.json, journal-next.json, closeout.json, independent-closeout.json, entry.lock and result.json. No scheduler/new helper/source change. Observable finish: sanitized NARROW_ACCESS_OBSERVED, SERVICE_DISABLED, NARROW_ACCESS_STOPPED or CONTAINMENT_UNCONFIRMED plus independently verified cleanup; all retain executionReady=false. If approval/cutoff is missed, no launch.

Renewal complete; exact new qualification approval/attempt/closeout remain. 3A open; accepted 1A/1B/2A/2B **4/8**; R1 newly closed **0/27**. Prior operation/R10 and renewal invocation are consumed and cannot be reused. **No scope deviation.**
