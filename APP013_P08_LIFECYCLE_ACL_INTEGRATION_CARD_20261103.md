# APP-013 / 3A / P08 lifecycle ACL integration card

## November 3 — approved lifecycle ACL integration locally verified

R1-W01/APP-013/3A/P08. Owner “i approve proceed” approved card60082c6 before implementation, source baseline2972104745134d42062afdf259d9c9f34bc7833f. Verified backend commit d306ca3e2e6d05f1c9555849d8d511507be699c1. Checklist1–6 implemented/tested locally: shared strict full-ACL comparison and separate lifecycle expiry query; RuntimeAdapter wired into existing normal and independent-closeout entry; exact NativeIO SQL allowlist; source/test manifests and pinned pure-module dependency. Existing authority/schema, historical restore/closeout/bridge/client modules and consumed receipts unchanged. Retired classifier output remains unchanged. Full ACL equality precedes legacy digest comparison; enabled/retired state predicates remain inherited and unchanged. No cached passing ACL result.

PASS111 narrow unit,21 assembled entry,6 Node transport,8 owned PostgreSQL and8 owned TLS PostgreSQL tests (154 total). Actual TLS SQL serialization and owned process boundary exercised; test-only CA/endpoint remain isolated from real credentials/providers. Full original grant fixture plus CONNECT was applied only to owned disposable databases. Extra column grants refuse before authentication, in enabled state, at retirement and independently reconstructed closeout. Existing concurrency/replay/clock/deadline/child-failure/session-disagreement tests remain passing. Old/injected arbitrary SQL refused. Both newly exercised owned database fixtures report server reaped and scratch absent; runtime sessions independently observed absent. No failures in the final suites. Byte hashes and counts: LIFECYCLE_ACL_RESULT_20261103.json. Final source verification, architecture, frozen baseline, cross-repository/docs consistency,25 governance tests and whitespace checks PASS. No browser/application-build claim for this isolated prerequisite.

Completed this card only; implemented and locally tested, not live-demonstrated or owner-accepted as3A. LiveObserved=false/executionReady=false/providerCalls0. Continuous monitoring and atomic provider-state guarantees are not claimed: checks occur at existing lifecycle readback boundaries. Broader nine-check producer remains incomplete; expected environment provenance, chosen credential/transport and effective diagnostic contract remain implementer-owned design gaps. Current real role/ACL and provider facts UNKNOWN. Next observable result: resolve those existing producer design blockers into a finite card; no live window/password/replay authorized. Product/provider/DB owners retain later exact external decisions. Accepted1A/1B/2A/2B4/8; R1 newly closed0/27;3A open. **No scope deviation beyond the explicitly approved lifecycle integration.**


## November 3 — owner approved lifecycle ACL integration before implementation

Owner “i approve proceed” approves the exact local integration card at governance60082c6, backend source2972104745134d42062afdf259d9c9f34bc7833f. Checklist1–6, file boundary, acceptance trace, readiness, test commands, exclusions and rollback are incorporated. Baseline and cross-repository checks PASS before edits. No live operation, credentials, provider action or full qualification producer authorized.

Status: proposed local implementation; owner decision pending. Owner “proceed” authorized completion of this card, not its implementation. This is a bounded prerequisite correction in the existing native entry, not another acceptance section. The broader nine-check producer is NOT claimed design-complete.

## Criterion, demonstrated gap and customer workflow

Approved acceptance remains APP013_REMAINING_EXECUTION_CONTRACT.md §3A: same admitted job Sandbox Checkout, authentic matching mode/account/amount/currency signed settlement; fail-closed negative cases and idempotent replay; owner acceptance. DATA_CONTRACTS payment policy is unchanged. This correction preserves least-privilege runtime access needed for that journey.

Inspected entry.py run_entry constructs restore.NativeAdapter for both run and independent closeout. Its inherited preflight/readback/retired methods call self.role, giving one reusable dispatch seam. The locked restore.role query omits column grants. native_io.py constructs allowed_sql by capturing that same old query. Therefore changing only a classifier does not fix actual entry. Native authority.py is itself locked by the narrow access manifest; changing its qualification schema would broaden the dependency impact. Existing seven real PostgreSQL tests prove the legacy digest misses an excluded column grant.

## Selected design and alternatives

Recommended: add a RuntimeAdapter subclass inside existing entry.py, override role only, and have both run and independent closeout instantiate it. Preserve inherited phase-specific predicates and mutations. Share the fixed full-ACL SQL and pure ACL comparison from existing access_check.py. Extend NativeIO's fixed SQL allowlist to the exact same full query. Keep authority.py and historical restore.py/closeout/bridge/client modules byte-identical; no monkey patch or fallback to the incomplete query.

Separate ACL comparison from retired-state classification in access_check.py. The pure ACL function requires independent static expected_retired_acl(), exact typed rows, no duplicate/missing/extra/grant-option rows, database normalization only for the current database, and computes both full and legacy digests after comparison. classify_retired_role continues enforcing all current retired-state predicates; its public output remains unchanged. Preserve its existing SQL/output contract. Add a distinct lifecycle_role_query derived from that query with the single additional raw expiry field required by old enabled-state verification; do not weaken the retired query's exact field validator.

RuntimeAdapter.role must parse strict bounded JSON from one SQL read, verify exact database/operator/role identity from cap, validate full ACL against the static baseline, reject unsafe flags, membership in either direction, owned objects, PUBLIC CREATE/TEMP, malformed counts/booleans and missing/null fields. Return the legacy-shaped projection only after those checks: count/login/limit/expires/expired/unsafe/memberships/owned/sessions/acl. Inherited readback still enforces enabled LOGIN/limit6/exact workEnd expiry, and retired NOLOGIN/limit0/expired/zero sessions. Never coerce active state into retired state to reuse its classifier. Full-ACL checking occurs every time self.role is invoked, including independent closeout; no cached passing verdict. Existing temporal gaps between readbacks remain; this does not promise continuous monitoring or atomic external state.

No qualification schema change is needed for this correction: roleAclSha256 remains the exact legacy digest, checked only after independent full ACL equality. Full baseline is bound by pinned source/fixture; full digest is local evidence, not a caller-supplied approval. Add access_check.py to native source-manifest lockedSources and verify the imported pure functions against that hash before dispatch. Do not import or invoke its live/cache functions. If this creates a source-loader cycle or requires changes beyond the file list, stop before broadening it.

Alternatives rejected: editing historical restore.py would require its nested bundle manifests to be reviewed/re-pinned; adding only a new query to the allowlist leaves dispatch unchanged; a new standalone demo does not exercise the actual entry path. Deferral leaves native readiness blocked.

## Exact file boundary

Under evidence/APP-013/:

- p08-narrow-access-check-local-20261101/source/access_check.py: factor pure ACL comparison; add lifecycle query; preserve existing public retired proof behavior.
- Same directory test_access_check.py, test_retired_role_postgres.py, source-manifest.json and test-manifest.json: regression/real SQL proof and exact provenance.
- p08-native-entry-local-20261101/source/entry.py: subclass, strict bridge, shared run/closeout construction.
- Same directory native_io.py: exact full-query allowlist; no arbitrary SQL, credential or retry change.
- Same directory test_entry.py and test_native_postgres.py: assembled normal/independent-closeout and owned PostgreSQL coverage.
- Same directory source-manifest.json and test-manifest.json: actual changed bytes and added pure-module dependency.
- Current section/result documents and governance handoff only.

No new runtime file, authority.py/schema change, application module, migration, provider configuration, old locked implementation or SDK modification. This is an explicit proposed change from local-only ACL proof into existing lifecycle dispatch; approval of the prior proof does not authorize it.

## Data, identity, retention and disabled state

Tests use synthetic envelopes and owned disposable PostgreSQL only. Apply original pinned grant fixture plus CONNECT exclusively there. Real database/password/token/account/customer data must not be read. Fixture TLS and session ownership reuse existing test_native_postgres/test_bound_postgres seams; test the new fixed query through the actual NativeIO.sql allowlist using a fixture-only process/credential port, never create a real external Capability. Unit mocks alone do not establish this boundary.

Queries remain fixed catalog-only read-only transactions; no business-row/password payload. Exact output cap65536 bytes, strict UTF-8/JSON and field types, SQL statement/lock deadlines and operation cutoff remain enforced. Temporary secrets synthetic/memory-only; owned children reaped, sessions independently observed absent and fixture roots removed. Cleanup failure cannot become a success. No live run/qualification mode is added. Existing external authority checks remain unchanged and no operation is authorized.

## Finite checklist and observable finish

1. Verify source pins, approval and both repository checks; preserve AGENTS.md and consumed receipts.
2. Factor pure ACL comparison with unchanged retired behavior; add lifecycle output contract and positive/negative tests.
3. Wire actual RuntimeAdapter for run and independent closeout and exact NativeIO SQL allowlist. Prove unknown/old/arbitrary SQL refusal.
4. Prove real full grant fixture and both enabled/retired states; inject column drift at preflight, enabled readback, retirement and independently reconstructed closeout. Each must refuse or retain a residual; no authentication/closure success.
5. Exercise null/missing/bool-as-int/duplicate/wrong identity, extra/missing/GRANT OPTION grants, PUBLIC exposure, wrong expiry/limit, role absence, active sessions at retirement, concurrent entry, duplicate attempts, rollback/deadline, interrupted parent, lost child response and cleanup disagreement through existing assembled tests. Preserve all existing tests and assertions.
6. Update manifests, run all listed gates, record failures and sanitized source hashes/cleanup evidence, verify unchanged historical files and consumed receipts, and close this card only.

Required commands from backend (use pinned Python3.14.2 executable already recorded in the prior card; -B for tests):

```sh
python3.14 -B evidence/APP-013/p08-narrow-access-check-local-20261101/source/test_access_check.py -q
python3.14 -B evidence/APP-013/p08-narrow-access-check-local-20261101/source/test_retired_role_postgres.py -v
python3.14 -B evidence/APP-013/p08-native-entry-local-20261101/source/test_entry.py -v
python3.14 -B evidence/APP-013/p08-native-entry-local-20261101/source/test_native_postgres.py -v
node --test evidence/APP-013/p08-native-entry-local-20261101/source/test_transports.mjs
python3.14 -I -B evidence/APP-013/p08-narrow-access-check-local-20261101/source/access_check.py --check-source
node scripts/architecture-check.mjs
```

Also source verification through existing authority.verify_sources/test_entry provenance test; backend check-governance-baseline with resolved governance; governance frozen-baseline/docs-consistency with resolved backend and25 safeguard tests; git diff --check both. Exact interpreter: /opt/homebrew/Cellar/python@3.14/3.14.2/Frameworks/Python.framework/Versions/3.14/bin/python3.14. No new test counts asserted. Existing TLS tests do not prove the new path until rerun with that path exercised. Browser/payment tests are not applicable to this local catalog correction; they remain mandatory for final3A.

Observable finish: passing assembled normal and independently reconstructed closeout with full ACL refusal, actual disposable SQL/TLS/session evidence and exact source/test manifests. It is a locally tested prerequisite, not a qualified live operation or accepted customer capability.

## Readiness record and remaining producer blocker

| Prerequisite | Inspected result | Owner / next evidence |
| --- | --- | --- |
| Actual lifecycle dispatch | entry.py constructs one adapter for run/closeout; inherited methods dynamically call role | Implementer: subclass wired into both |
| Actual SQL boundary | NativeIO captures old role query into allowlist; TLS verify-full and pinned DB/PGAPPNAME/timeout settings inspected | Implementer: exact new query accepted, arbitrary query refused; owned TLS proof |
| ACL baseline | Original fixture35785d3857f6fc9b01042d6dee3137eebb18950601fb1b8e7644e340be8fb83c plus CONNECT; seven real-PG tests already passed historically | Implementer: new lifecycle-phase tests; current real ACL UNKNOWN |
| Phase expiry/cleanup | restore.readback has enabled exact workEnd and retired zero-session predicates; entry independent closeout reconstructs same runtime | Implementer: preserve predicates, prove interruption/concurrency/cleanup |
| Full evidence producer | authority requires nine checks and exact scope/time/hashes, but old qualification reader primes SDK CLI and uses absent-role predicate | Separate incomplete integration design; no producer implementation authorized here |
| Expected environment | Historical corrected-cloud receiptc324c781 at2026-10-28T14:56:42Z records matching digestb3b3e19722bbd8f5ceadb94323e86612e4b26b8bc896b1d0223e74e683f67cc8 | Historical observed value only; implementer must recover approved expected-set provenance, not promote observed hash |
| Credentials/effective access | NativeIO.ensure_owner invokes SDK auth/config/token; CLI uses SDK; qualification permission tests alone are not usable access proof | Implementer: exact transport and diagnostic contract still unresolved for producer; fresh external owner decision later |

The complete current-state integration card cannot honestly be marked ready yet. Cached-only narrow HTTPS cannot simply replace arbitrary native SDK output/credentials without new implementation and tests. Recommendation is preserve current native transport for this local ACL correction; resolve the producer's SDK-exception-versus-cached transport decision in its own explicit change record, with actual request/output contracts and approved environment provenance. Do not request a live window or password while these remain unresolved.

Rollback: restore exactly listed existing files to source SHA below; retain immutable approval/result evidence. No provider rollback needed because none is touched. No frozen baseline reanchor. Owner approves this finite lifecycle correction or defers; implementer owns proof and remaining producer design. Accepted1A/1B/2A/2B4/8; R1 newly closed0/27;3A open. **No scope deviation implemented; lifecycle integration proposed before coding.**

## Source inspection pins

Inspected 2026-11-03T15:34:15.295885+00:00; backend 2972104745134d42062afdf259d9c9f34bc7833f; governance 726098b1ff789e85d2372b58791caf844aa487bb.

- `p08-native-entry-local-20261101/source/entry.py`: `92bf5b8d0a2b656c76c6eb5600f7cad22f903219d41439ffd359c509b28e5111`.
- `p08-native-entry-local-20261101/source/native_io.py`: `4eca2d6a66b3616db59380d635be8937291b4dd50fd290e727caf578c2c8f498`.
- `p08-native-entry-local-20261101/source/authority.py`: `763dd24f5dac70b3ec87d350ab2efc6d0fe110aae9f261708aba8c54e481e365`.
- `p08-native-entry-local-20261101/source/source-manifest.json`: `8b3ba5afcba4c80a73df8e8e4d0a61e5edc93025efda4775aef02e5711206201`.
- `p08-restoration-local-20261028/source/restore.py`: `a0bf4bc90cca0bd52935915d710ccb44e065dd3deed841a12ab49cb3ac4a1cb9`.
- `p08-narrow-access-check-local-20261101/source/access_check.py`: `50994959a47400f651ee37ad4591cde486fbcf417d31b4eccecddf1564f7bf70`.
- `p08-corrected-cloud-result-20261028/result.json`: `f38b32d4894079b4f97bbfb1df8e06317b1d05f37a15f9e6fd934fc63f6f1c9b`.
