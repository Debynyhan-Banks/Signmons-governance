# APP-013 / 3A / P08 — exact six-read access qualification

**OWNER APPROVED — November 1, 2026:** owner replied “proceed” to the explicit final request for this exact November 1 10:30–10:40 a.m. EST window, strict 10:32 cutoff, one cached-token read/up to six fixed requests, zero refresh/retry/configuration changes/spending. Approval was observed at 15:11:38 UTC. The decision JSON now records APPROVE_EXACT_P08_NARROW_ACCESS_READ with unchanged operation/scope/source pins. The original pending proposal below is retained as history and superseded only by this exact approval. No operation has started; root/private plan/cache/provider access remain absent. Readiness remains qualification-only, not broader P08/payment authorization.

**PENDING OWNER APPROVAL. Qualification-only; not execution-ready for P08 or payment.** The owner authorized committing the reviewed local amendment and preparing this packet. That instruction did not authorize real configuration/cache access or authenticated provider reads. No operation-private root, plan, credential read or provider request has been created/performed.

## Decision requested

Approve exactly one access-qualification attempt for operation **dff9307d-e7fb-4e5a-873c-22179faf0958**, using the committed source below and this absolute window on **November 1, 2026**:

| Boundary | UTC | America/New_York (EST, UTC-5) |
| --- | --- | --- |
| Earliest start | 15:30:00Z | 10:30 a.m. |
| Strict start cutoff | 15:32:00Z | 10:32 a.m. |
| Read deadline | 15:34:00Z | 10:34 a.m. |
| Independent closeout deadline | 15:39:00Z | 10:39 a.m. |
| Exact private-plan purge deadline | 15:40:00Z | 10:40 a.m. |

Start must be at or after 15:30 and strictly before 15:32. No rolling window, automatic retry, refresh/login, API enablement, permission change or repaired rerun. If approval/preflight cannot finish before cutoff, do not launch; mark expired-unstarted and seek a fresh concrete decision. No unattended schedule is installed by this proposal. Executor must remain available through verified closeout; otherwise do not begin. This needs no password/token supplied by the owner.

Authorization sought: read the fixed local active configuration and one exact owner's cached token, then at most six fixed Google HTTPS requests. **USD 0 incremental spending authority**; no billable resource creation, charge, payment, subscription or increase in allowance. This is not a statement of current billing/account health.

## Exact source and authority pins

- Backend source commit: `8e35617dc178ac8ce757548fac830b0013108ad7` (local, not pushed). It contains the reviewed amendment, source-verified native-entry dependency and its previously approved test fixtures/evidence. Separate dirty AGENTS.md edit was excluded.
- Runtime: `evidence/APP-013/p08-narrow-access-check-local-20261101/source/access_check.py`, SHA256 `861b0f549488fa3c281d2c4a7b3807c6c83bfa6f2a4d0a535367d2c2f0164b4d`.
- Runtime manifest SHA256: `dc687b5bc36264c57c75154122d406393d2e3711853332e5e57112c881ec9597`.
- Test manifest SHA256: `007d40ec05a27e755c606b1f1e13054462ea01e6fe90194e503afbd0a339df53`.
- Version-2 contract SHA256: `0141eada196370aadab786cd84339e4adea5df0d94b0a2410a60e99de8e5dea9`.
- Exact scope SHA256 (draft plan excluding decision reference): `3b9651755344bfb504e886d62a3647d176eb4396feed75ec0f1910219577b44e`.
- Draft plan: `APP013_P08_ACCESS_READ_DRAFT_PLAN_20261101.json`; file SHA256 `d9d8231b95090c4f424761592f259e5ad5be152478492d87a8c38d3948df4549`.
- Owner-decision record: `APP013_P08_ACCESS_READ_OPERATION_20261101.json` currently says **PENDING_OWNER_APPROVAL**; current bytes SHA256 `a3ac7eafeaed7a428519fcbe949e58dfbcd2c9eb23ff391a7171fa2a8b3e76ed`. This is not an approval receipt.
- Python executable: `/opt/homebrew/Cellar/python@3.14/3.14.2/Frameworks/Python.framework/Versions/3.14/bin/python3.14`, SHA256 `2cbb3ee843d8abcf93ed35bb9102391f18eefccb03d47908547bd8db67bc395c`; supported macOS/Python 3.14.2/SQLite 3.51.1. Invoke with `-I -B`.

After actual owner approval of this packet, change only the decision record's `decision` value to `APPROVE_EXACT_P08_NARROW_ACCESS_READ` and commit it with the session decision recorded in governance. Derive its exact commit and byte hash using the existing committed reader. Replace only the private plan's `decision` reference with that committed reference; all non-decision fields and the scope hash above must remain identical. Never fabricate an approval commit or use the synthetic authority from packet tests. Revalidate the committed source, decision, executable, clock and actual command before launch. No merge, push or deployment is requested.

## Exact permitted observations

Fixed owner `debynyhan@signmons.com`; project `signmons`; identity `signmons-calldesk-p07-runtime@signmons.iam.gserviceaccount.com`; default SDK root `/Users/debynyhanbanks/.config/gcloud`. Numeric project is derived only from the first response and matched to the existing SHA256 fingerprint `37d4aa0f46ca5b8f0b81b1148bda235a0f4a9a424b6b4638ec993d889563be54`; never supplied by a caller or retained in evidence.

One locally journaled cache reservation comes first. Read only the existing fixed active/named configuration and exact-owner cached access token/expiry/restriction fields. Reject unsupported configuration, overrides, missing/expired/restricted tokens, schema/runtime drift, unsafe files, active writers and journal/WAL/SHM. No conversion, migration, cache update, renewal, credentials.db, refresh/RAPT/ID token, other-account query, ADC or metadata fallback. Token must expire strictly after 15:40:00Z. Configuration/cache compatibility is intentionally an UNKNOWN to be resolved by this qualification; refusal is an acceptable result, not authority to fix it.

The six HTTPS descriptors, in order (short circuit on failure):

1. GET `https://cloudresourcemanager.googleapis.com/v1/projects/signmons?fields=projectId,projectNumber,lifecycleState`.
2. GET `https://iam.googleapis.com/v1/projects/signmons/roles/signmonsP08FirebaseUserLookup?fields=name,title,description,includedPermissions,stage,deleted,etag`.
3. GET `https://iam.googleapis.com/v1/projects/signmons/roles/signmonsP08ServiceAccountSignBlob?fields=name,title,description,includedPermissions,stage,deleted,etag`.
4. POST `https://cloudresourcemanager.googleapis.com/v1/projects/{verified-number}:testIamPermissions` with exactly resourcemanager.projects.getIamPolicy, resourcemanager.projects.setIamPolicy, apikeys.keys.create, apikeys.keys.get, apikeys.keys.getKeyString, apikeys.keys.delete, serviceusage.operations.get, serviceusage.services.get, serviceusage.services.enable, serviceusage.services.use.
5. POST `https://iam.googleapis.com/v1/projects/-/serviceAccounts/signmons-calldesk-p07-runtime@signmons.iam.gserviceaccount.com:testIamPermissions` with exactly iam.serviceAccounts.getIamPolicy and iam.serviceAccounts.setIamPolicy.
6. GET `https://serviceusage.googleapis.com/v1/projects/{verified-number}/services/apikeys.googleapis.com`.

The two POSTs test permissions; they do not grant or alter them. All requests use the in-memory bearer and x-goog-user-project=signmons, strict output/role parsers, an eight-second total per-call bound capped by readEnd, 65536-byte output ceiling, explicit no-proxy/redirect and no retry. No broad launcher, application/provider SQL, Cloud Run, billing, Firebase user/session, key creation, customer/job, Stripe or payment call is included. Full runtime/key/client compatibility, billing and payment remain outside these observations.

## Readiness record at preparation

Source SHA/evidence hashes above apply to this table. Timestamp: 2026-11-01 15:04:17 UTC; exact packet-check result is `APP013_P08_ACCESS_READ_PACKET_CHECK_20261101.json`.

| Prerequisite | Evidence / status | Responsible role |
| --- | --- | --- |
| Committed source and dependencies | Actual Git bytes/manifests and transitive validators PASS at 8e35617; approved source unchanged | Implementer |
| Provider outputs/serialization/null/errors | Previously completed 49 focused tests at exact unchanged hashes; strict actual native entry with synthetic cache and injected HTTP, six descriptors, role/project/null/denial coverage | Implementer; current provider facts UNKNOWN |
| Local cache/config identity and no-write behavior | Existing section-card evidence: strict schema/config; competing SQLite writer; no cache/sidecar mutation; expiry/overrides/privacy and timeout closure PASS | Implementer; actual config/token usability UNKNOWN |
| One attempt, cutoff, interruption, recovery | Existing 49 tests cover seven event reservations, duplicate/concurrent refusal and zero-I/O independent closeout; UNKNOWN pending events never replay | Implementer/executor |
| Actual invocation and source checker | Pinned Python `-I -B .../access_check.py --check-source` PASS; returns ready=false/localTransportReady=true, EXTERNAL_QUALIFICATION_NOT_AUTHORIZED | Implementer |
| Exact packet binding | Fresh five local checks PASS: pending commit/decision refused; real committed source with synthetic authority accepted; exact cutoff and absent source commit refused. No NativeIO constructed or actual operation root created | Implementer; synthetic authority is not owner approval |
| External owner decision / window | PENDING; exact proposed window above, no schedule/launch/private plan | Owner |
| Current permissions, roles and API availability | UNKNOWN; target of this qualification only | Owner/provider administrator for any remediation |
| Billing/full runtime/Firebase/job/key/payment | UNKNOWN and excluded | Later approved sections and same-job owner acceptance |

Fresh preparation checks: source hashes, actual source gate, backend/governance baseline and consistency, architecture and whitespace; 25 governance safeguard tests at final packet closeout. The prior 49 runtime tests are recorded at unchanged hashes, not represented as rerun during documentation-only preparation. No baseline or requirement anchor changed.

## Execution and independent closeout procedure after approval only

1. Confirm actual owner decision and committed exact record; verify draft/non-decision scope, source/dependency/executable hashes and private-root absence. Compare actual command and UTC clock with this packet. Missing evidence or any drift stops. Do not suppress an inherited credential/proxy/environment override to get through a refusal.
2. At or after start, before cutoff, form the exact private plan from the committed draft plus the committed approved decision reference. Exclusively create the exact empty root below (0700); validate the in-memory plan against that root using the existing `ReadCapability`, actual clock and its default committed reader; only after validation, exclusively write `plan.json` (0600) using the existing `reserve`. A root collision is a stop, not permission to delete/reuse it. If validation fails while the newly created root is empty, remove only that newly owned empty root and record the refusal. No private input is created before actual approval.
3. Invoke `--read` **once** with the exact command below. Owner authority is consumed on the first launch even if refusal occurs before the runtime attempt marker; do not rerun it. The runtime reserves a single attempt and each cache/HTTP event before dispatch. Retain sanitized result/journal; never raw provider output, token or project number.
4. Normal run closes response/cache handles, purges plan.json and verifies absence. If interrupted after attempt/journal creation, confirm parent exit and obtain the same exclusive operation lock; invoke `--closeout` before 15:39 using the same exact plan. It performs zero credential/provider I/O and retains uncertain events as residuals. Do not infer provider success from process death, an available lock, or cleanup alone.
5. If refused before attempt/journal creation or interrupted during their creation, the independent command may not have enough evidence to complete. Verify the exact owned inventory and matching plan hash/source/operation, parent exit and exclusive lock; purge only that exact private plan before 15:40. Preserve every existing sanitized marker, document missing/unconfirmed journal/containment and do not synthesize an outcome or retry. Foreign files/ownership or an active parent blocks cleanup: report the residual. This is a bounded manual local closeout duty, not claimed automatic enforcement by the CLI.
6. Verify plan absence and final inventory before purgeEnd; retain only allowed sanitized evidence. Record actual UTC start/stop, counts, classification, private absence, pending/unknown residuals and consumed/expired authority in governance. Keep runtime/customer/payment scope disabled regardless of the access verdict.

Exact read command, from the backend recovery checkout, **after approval and preparation only**:

```sh
/opt/homebrew/Cellar/python@3.14/3.14.2/Frameworks/Python.framework/Versions/3.14/bin/python3.14 -I -B evidence/APP-013/p08-narrow-access-check-local-20261101/source/access_check.py --read /private/tmp/p08-access-check-dff9307d-e7fb-4e5a-873c-22179faf0958/plan.json
```

Independent closeout command, only when required by step 4:

```sh
/opt/homebrew/Cellar/python@3.14/3.14.2/Frameworks/Python.framework/Versions/3.14/bin/python3.14 -I -B evidence/APP-013/p08-narrow-access-check-local-20261101/source/access_check.py --closeout /private/tmp/p08-access-check-dff9307d-e7fb-4e5a-873c-22179faf0958/plan.json
```

Private inventory is exactly plan.json, attempt.json, journal.json, journal-next.json, closeout.json, independent-closeout.json, entry.lock and result.json. The original cache/configuration is neither copied nor purged. Token remains memory-only; close clears references without claiming secure erasure. No automatic purge timer/scheduled worker is installed; executor availability and the verified closeout receipt are required.

## Observable finish and handoff

Completed: reviewed source/dependencies committed locally, exact draft and pending owner record prepared, binding/expiry/refusal checked without credentials or provider calls, readiness and closeout recorded. Remaining: owner decision; only if approved, exact bounded qualification and independent verified closeout. Next result is NARROW_ACCESS_OBSERVED, SERVICE_DISABLED, NARROW_ACCESS_STOPPED or CONTAINMENT_UNCONFIRMED with sanitized counts; all retain executionReady=false. Missing approval or missed cutoff yields no launch.

No helper subsystem, altered acceptance, new resource, SDK patch, provider change, automatic retry, payment advance or spending. APP-013/3A stays open; accepted 1A/1B/2A/2B **4/8**, newly closed R1 **0/27**; old R10 consumed and unrelated. **No scope deviation.**
