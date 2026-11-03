# APP-013 / 3A / P08 — bounded prospective-key absence qualification proposal

**Decision-ready local amendment; NOT implemented or externally executable.** Owner directed proposal preparation with “proceed”. Backend entry facd84c0950028a385137d6d9ef7272fd8602dff; governance928445183a075e476fddcc7d44e9c9282dda50bf. No new code, private plan, credential read, provider request or live window. Existing AGENTS.md change preserved.

## Approved criterion and demonstrated gap

R1-W01 / APP-013 / 3A / P08 remains same-admitted-job Sandbox Checkout → authentic matching signed settlement → gate/failure/replay proof → owner acceptance. Reuse existing payment/authentication journey; no new acceptance section or denominator. APP013_REMAINING_EXECUTION_CONTRACT.md3A and existing payment-admission DATA_CONTRACTS remain unchanged.

October29 R10 stopped with rolesExact=false, API Keys DISABLED and prospective key absence DENIED. November3 six-read receipts confirmed exact roles and requested owner permissions; subsequent exact service enablement/readback confirmed ENABLED13:50:28, retained and independently closed. Key absence has not been refreshed; neither permission-test success nor service enablement proves it. See APP013_P08_REMAINING_READINESS_RECONCILIATION_20261103.md. Billing flags passed historically in R10; current billing is UNKNOWN, not an established current failure.

Inspected source pinned in backend a7adc1fa846d889432ed9295ead5395d71cac7de:

- p08-narrow-access-check-local-20261101/source/access_check.py SHA256 c608a7ea3d9b8feee7af0131eaa37d7f92c7e2abb6739f513866d27d840e5616, manifest816b1c774f46bb515b20ad9beeeaa3e4d30332884b4750faa8f6a66083974715. Existing V2 is six fixed reads; V3 is conditional service enablement. Neither exposes key GET. Reuse ReadCapability, exact NativeIO type gate, cached-token/configuration guard, bounded HTTP serialization, atomic journal, lock and closeout.
- p08-role-contract-local-20261029/source/qualification_launch.py SHA25676722d3265cda655b6b2433bc83d3bbcee06c12c6d0f66c07cad9fe2ae2e7e18 contains the exact metadata GET and bounded absence classification. Its read_access primes26 CLI reads and nine access HTTPS descriptors including SDK credential resolution. Running it would exceed this narrow purpose and does not establish cached-only/no-retry behavior.
- p08-native-entry-local-20261101/source/authority.py SHA256763dd24f5dac70b3ec87d350ab2efc6d0fe110aae9f261708aba8c54e481e365 requires current nine-check qualification; native --run mutates runtime/IAM/key/authentication. It cannot supply the missing narrow read safely.

[Official API Keys get contract](https://docs.cloud.google.com/api-keys/docs/reference/rest/v2/projects.locations.keys/get), inspected November3, specifies GET of one global key's metadata, no request body, apikeys.keys.get permission; the key string is excluded. Use only that endpoint, never getKeyString, list, lookup, create, delete, undelete or update.

## Exact proposed target and later external scope

Target record APP013_P08_KEY_ABSENCE_TARGET_20261103.json selects identifiers only; it authorizes no creation/authentication:

- Fresh qualification operation651d475e-9344-47f1-b08c-abba317e17d9.
- Fresh prospective authentication operationb3bd682f-1a85-48ab-a242-879169e93571.
- Derived prospective key IDsignmons-p08-b3bd682f1a8548aba242879169e93571.
- Exact owner debynyhan@signmons.com; project signmons; location global. Preserve the established project-number fingerprint37d4aa0f46ca5b8f0b81b1148bda235a0f4a9a424b6b4638ec993d889563be54 and runtime identity pin without exercising that identity.

A later separately approved operation would reserve one cached-token read and at most three HTTPS GETs, zero CLI/refresh/retry/SQL/mutations:

1. Existing Resource Manager GET projects/signmons?fields=projectId,projectNumber,lifecycleState; require exact active project and fingerprint before deriving any numeric resource.
2. Existing Service Usage GET projects/{verified-number}/services/apikeys.googleapis.com; exact resource/state ENABLED required. Disabled/unknown stops without enabling.
3. API Keys GET projects/{verified-number}/locations/global/keys/{exact-derived-key-id}, empty body. Fixed host apikeys.googleapis.com; no caller-supplied URL, query, alternate key or resource name.

No operation time is selected while the new boundary is unimplemented. Validity beyond any future purge deadline is UNKNOWN; past token checks and consumed decisions cannot authorize it. Later exact packet must bind source/contract/target/decision/window and verify prerequisite readiness. Absence is only a point-in-time observation for that target, not a reservation against another creator, future availability guarantee, evidence of create/getKeyString permission, or key-creation authority.

## Recommended bounded local amendment and alternatives

**Option1 recommended: approve local implementation and isolated tests in the existing adapter only.** Add a distinct version4 read-only key-absence capability/entry with three fixed requests and no mutations. Preserve V2/V3 behavior and consumed artifacts. Only four existing source/test/manifest files plus current section/result/governance evidence change; no new module, provider client, daemon, production code or broader qualification subsystem. This is a material request/authority extension requiring approval before implementation. Effort is limited to this boundary and its tests; no new acceptance count/dependency.

Option2: owner/provider administrator supplies authoritative metadata/NOT_FOUND evidence for this exact project/global/key target using their established procedure; future automated qualification still requires its own authority. Do not send a contact message or run an ad-hoc CLI/HTTP request under this proposal. Option3: defer. Do not reopen the consumed R10/full workflow as a substitute.

## Finite preimplementation card for Option1

Source base and acceptance trace above; reuse current source/test module and separate manifests. Expected interfaces in source/access_check.py: distinct KeyAbsenceCapability/KeyAbsenceNativeIO/KeyAbsenceReader, --key-absence and --closeout-key-absence, version4 decision schema binding qualification UUID, prospective authentication UUID and deterministically derived key ID. Different version/path/decision from V2/V3; exact capability type required for native dispatch. Local proof never authorizes native I/O. No live-ready flag or fallback.

1. Bind distinct version4 authority, exact source/contract hashes, target derivation, scope and limits cache1/HTTPS3/CLI0/SQL0/mutations0/retry0. Require valid canonical different qualification/prospective UUIDs; key ID must equal deterministic derivation, with no caller override/path injection. Existing external committed-reader/source binding reused; old read or service-enable approval must refuse.
2. Execute only the ordered three GETs above after the unchanged cache/configuration guard. Reuse fixed-host serializer, memory-only bearer, x-goog-user-project=signmons, no proxies/redirects, eight-second total per call and65536-byte maximum, deadline clipping and no refresh/retry. Do not call the broad _prime_cli/read_access or native mutation lifecycle.
3. Classify final metadata response through the same actual HTTP/parser boundary. Only HTTP404 with object error and exact string status NOT_FOUND establishes KEY_ABSENCE_OBSERVED; if numeric error.code is present it must be integer404. HTTP200 with object exact matching name is KEY_PRESENT_STOP even if deleteTime exists; missing/foreign/malformed200 is KEY_RESPONSE_UNKNOWN. HTTP401/403 is KEY_ACCESS_DENIED, never absence. Other status, wrong/missing/null error shape/status, malformed encoding/JSON, oversize or redirect is UNKNOWN/stop. Never retain raw messages/details/payload/metadata/key material; no retry or alternate-ID search after any result. Official get excludes key string, and no key-string method is in the contract.
4. Reuse one exclusive operation root, attempt/ordered journal, exact inventory and unchanged0/120/240/540/600-second offsets. Retain only sanitized classification/counts/target hashes; no token, expiry, numeric project or returned key metadata. Independent closeout performs zero credential/provider reads, preserves pending/unknown outcomes and purges private plan/scratch. Persistent filesystem failure reports unconfirmed containment and requires the exact-owned attended manual fallback in the later live packet. No automatic purge timer or secure-memory-erasure claim. Clear references even if closeout raises.
5. Extend the existing test module: preserve all76 current cases; add actual new entry/native serialization with synthetic cache/HTTP, metadata404/200/401/403/error/default/null/foreign-name/deleted-key cases, source/decision/version/target/UUID/limit drift, denied native local authority, duplicate/concurrency/each-reservation interruption, cutoff/read/closeout/purge deadlines, clock rollback, successful and interrupted independent cleanup, foreign inventory, secret-safe output and persistent journal/purge failure. Disposable Git checks actual committed reader. Network denied in local tests. Run full focused pinned-Python test module, actual source check, architecture, backend/governance baseline/docs consistency,25 governance safeguards and both whitespace checks. No browser/real database/application build gate applies to this isolated Python change. Source/test manifests hash every changed byte. Stop for review if more files/interfaces are needed.

Rollback: restore only four source/test/manifest files from a7adc1f; all historical/consumed provider evidence untouched. Observable local finish: tested source-pinned three-read entry and exact result/readiness report, followed by a separate live packet proposal only if locally discoverable prerequisites pass. No operation/window/provider read/key creation is authorized by local approval.

## Shift-left readiness and responsible owners

| Prerequisite | Current evidence/status | Owner / next observable result |
| --- | --- | --- |
| Existing source/dependencies/cache/serializer/cleanup | Actual source gate passes, pinned76 local tests from prior turn; no new runtime tests claimed | Implementer reuses and preserves existing paths |
| New three-read authority/target/output boundary | NOT IMPLEMENTED/NOT TESTED; proposed above | Owner local amendment decision, then implementer tests actual boundary |
| Project/API/service/key response contract | Existing exact project/service parsers and old metadata descriptor plus official contract inspected; future provider response UNKNOWN | Implementer validates source-pinned parser; provider administrator if denied |
| Current owner/config/cache validity | Past November3 guards passed, future window UNKNOWN | Credential custodian; no renewal/read implied |
| Actual target absence | UNKNOWN; older R10 target DENIED is not this target | Future exact read-only qualification or administrator evidence |
| Runtime/DB/Firebase/job/billing/full native qualification | UNKNOWN/currently unqualified; successful key absence cannot satisfy all nine gates | Existing owners and later approved scopes |
| External source/decision/window/closeout | ABSENT, no launch requested | Owner only after local proof and concrete packet |

Completed this turn: source/contract review, fresh exact target selection, alternatives, finite local card and readiness record. Remaining: owner selects local amendment/administrator path/deferral; implementer performs only selected authorized work. Accepted1A/1B/2A/2B **4/8**, R1 newly closed **0/27**, 3A open. **Explicit narrow read-interface amendment proposed before implementation; no deviation implemented.**

Preparation checks PASS: actual unchanged source validator, baseline/cross-repository/docs consistency, architecture,25 governance safeguards and both whitespace checks. Documentation-only preparation; no runtime tests rerun or new behavior claimed.
