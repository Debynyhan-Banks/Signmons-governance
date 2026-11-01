# APP-013 / 3A / P08 — no-retry transport change request

**Local result:** approved amendment implemented; 49 focused cases PASS. See backend `evidence/APP-013/p08-narrow-access-check-local-20261101/NO_RETRY_AMENDMENT_RESULT_20261101.md`. No external execution authorized.

**Owner decision, November 1, 2026:** “i approve” authorizes option 1 local implementation and synthetic testing. The original proposal below is retained; pending-decision statements are superseded for this bounded local amendment only. No live credential/provider operation is authorized. Implementation card: backend evidence/APP-013/p08-narrow-access-check-local-20261101/SECTION_CARD.md.

**PROPOSED; owner decision pending. Local implementation/testing only is requested.** The owner's latest “proceed” authorized investigation of the recorded SDK blocker; it did not change the exact eight-CLI/three-HTTPS contract. No runtime change, SDK modification, real credential read or provider operation has been made under this proposal.

## Demonstrated gap and connected workflow

Section R1-W01 / APP-013 / 3A / P08 retains same-admitted-job Sandbox Checkout, authentic matching signed settlement, failure/replay and owner acceptance. This internal prerequisite establishes only scoped access facts needed before that workflow; it closes no acceptance milestone. Accepted 1A/1B/2A/2B remain 4/8; R1 newly closed 0/27; R10 consumed/no retry.

Backend source entry d5f1f876e8f17f8236d2262d1856a6fa323a86a4; governance 996cc7fb5be906ddf64d1d337c7fa6dc24a3a001 plus preserved uncommitted work. Existing access_check.py hash 40b4e2921e752236a2b77c6e3a7bc8d9eb739cc8262d3e7ad461471432957729; manifest 2bc1858ec57385d2b9c6f9867cf77783995b77ea1722a786fa311fa299d2697b. Backend `evidence/APP-013/p08-narrow-access-check-local-20261101/SDK_RETRY_REVIEW_20261101.md` records current installed SDK source hashes and four new diagnostic tests, all passing. Full module: 33 PASS.

Actual generated project/role clients made five synthetic transport invocations on repeated 503. Actual OAuth Credentials.refresh made three. Lower library parameters reduce each to one, but no supported global CLI control was established. auth list can involve static providers; broad credential loading has fallback paths; direct SDK store constructors can create/migrate local tables. Counting subprocesses or using a timeout does not meet the approved no-retry condition.

## Alternatives and proposed decision

1. **Recommended bounded local amendment:** adapt the existing module to six fixed direct HTTPS reads and cached-token-only loading, with no gcloud subprocess or OAuth refresh. Prove the changed boundary with synthetic files and transports before preparing any external operation.
2. Use the existing owner/provider-administrator evidence alternative. No new runtime implementation; administrator supplies current scoped project/role/permission/service evidence. This does not by itself prove native execution or full P08 qualification.
3. Keep the current hard stop and defer this prerequisite. Patching the installed SDK, weakening no-retry, or replaying broad R10 are excluded.

Requested owner decision is option 1 local-only or option 2/defer. **No owner decision on this amendment is recorded yet.** Prior approvals are retained for their original scopes.

## Exact proposed behavior and files

Reuse `access_check.py`, `test_access_check.py`, their separate manifests, SECTION_CARD and RESULT in the existing narrow directory. Reuse its authority/source/decision checks, role and project parsers, twelve permission names, environment refusal, HTTPS deadline/output/redirect handling, one-use journal and independent local cleanup. No new package, coordinator, production code, schema migration or acceptance section.

Change request inventory from eight CLI plus three HTTPS to **zero CLI plus six HTTPS**, ordered:

1. GET Resource Manager V1 projects/signmons, with exactly the existing projectId/projectNumber/lifecycleState fields.
2. GET IAM V1 first existing pinned project role, with the existing full role fields.
3. GET IAM V1 second existing pinned project role, same fields.
4. Existing Resource Manager project testIamPermissions POST, unchanged ten names.
5. Existing IAM service-account testIamPermissions POST, unchanged two names.
6. Existing Service Usage apikeys.googleapis.com GET, unchanged project-number binding.

Resource pins remain those in `APP013_P08_NARROW_ACCESS_CHECK_PROPOSAL_20261101.md` and the existing runtime contract: owner debynyhan@signmons.com, project signmons, existing numeric-project fingerprint, service account signmons-calldesk-p07-runtime@signmons.iam.gserviceaccount.com, two exact role IDs/definitions and existing three HTTPS hosts. No extra probe or token introspection endpoint. Project and role REST method contracts: [Resource Manager projects.get](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/get), [IAM projects.roles.get](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.roles/get). Serialization must be verified against these method contracts and the existing parsers before coding the changed boundary.

Replace auth/config/token CLI calls with bounded local configuration validation and **one account-specific read of the already-cached access token**, using the pinned installed SDK schema as evidence. This explicitly introduces local read-only SQLite cache access; provider/application SQL remains zero. It is not permission to read actual user credentials during local implementation. Requirements:

- Only the expected default SDK root and active named configuration; exact owner/default universe, no impersonation, credential file, token file, endpoint, proxy or alternate-root override. Reject unsupported configuration rather than silently emulate all SDK resolution behavior.
- Only existing access_tokens.db, exact owner row, token/expiry and restriction fields needed to refuse unsupported state. Do not load credentials.db, refresh tokens, RAPT/ID tokens, other account rows, ADC, static providers or metadata. No SDK credential constructor, refresh, login, fallback or cache write/migration.
- Read-only database access must be demonstrated to create/change no database or sidecar files. Refuse unsafe ownership, links, schema, journal/concurrency state or an unsupported read-only access mode. SQLite write/DDL/extension/attach and non-allowlisted queries must be blocked. Resolve the exact no-write opening method with synthetic stores before runtime implementation; if it cannot be proved within this module, stop and report, without inventing another cache subsystem.
- Require a well-formed nonempty cached token, supported restriction state and verified expiry beyond purgeEnd. Missing, expired, ambiguous or changing cache/config state stops before HTTPS. No automatic renewal. Cache account binding is local evidence, not independent proof of current provider authorization.
- Token stays in process memory, never plan/journal/log/argv/error output. Close database/response handles and clear references; no secure memory-erasure claim. No token/cache copy or new private input file. Existing owner cache is not deleted or altered by cleanup.

Existing absolute 0/120/240/540/600-second offsets, output 65536-byte ceiling, eight-second total per-call bound, start/read/cleanup cutoffs, source/decision commitments, operation root inventory, exclusive reservation and zero retry/redirect requirements stay. Scope/request hashes and all call-limit assertions must change explicitly with this approved contract; old authority cannot authorize it. Readiness stays blocked until all local obligations pass; external capability still needs a separate committed owner decision and exact window.

## Finite acceptance and readiness record required before implementation

1. Complete the existing section card with owner decision, inspected method/cache/config contracts, final file/interface list, source hashes and dynamic configuration refusal. Resolve read-only cache opening using synthetic stores only; no real credential access.
2. Implement only the existing module's changed descriptors and cache/config boundary. Preserve strict parsers, private inventory, authority, independent cleanup and classified UNKNOWN behavior. Remove CLI dispatch from the amended contract.
3. Exercise the actual entry/native boundary with synthetic files and injected transports: exact six-call ceiling/order; project/role serialization including missing/null/deleted fields; permissions/service denial; expired/missing/wrong-owner/cache/schema/config/override/restriction refusal; token privacy; proof of no refresh/fallback/network during cache loading; no cache/sidecar mutation; source/authority drift; HTTP 401/429/503/redirect/timeout each one attempt; concurrent/interrupted/cache-changing cases; duplicate execution, cutoff and independent cleanup without provider/credential I/O. Retain applicable existing 29 cases and four SDK regression diagnostics. No fake result is current live evidence.
4. Update separate manifests; run actual source validator, the full focused Python module, backend architecture/cross-repository baseline, governance frozen baseline/docs consistency/25 safeguard tests and whitespace. Browser and application/PostgreSQL tests are inapplicable; local SQLite fixture tests are required under this amendment.
5. Record exact final source, evidence timestamp/results, responsible owners, finite completed/remaining checklist and UNKNOWNs. Only after local proof may the implementer prepare a separately reviewable exact external qualification operation. No operation scheduled by this proposal.

## Impact, responsibility, rollback and observable finish

Impact: moderate bounded change in one existing module/test; replaces subprocess/refresh uncertainty with a version-pinned read-only cache compatibility dependency. Valid cached token availability remains UNKNOWN and may block live use. No additional provider permission/resource, customer capability, acceptance denominator, queue ordering or spending. Owner approves the material prerequisite change and any later external operation; implementer owns local proof; owner/provider administrator owns current access/remediation. Billing/runtime/CHILD/Firebase/job/key/payment qualification remains outside this amendment.

Rollback retains the current source/manifest and its hard SDK refusal; no prior runtime changes are overwritten. Finish is either a source-pinned locally verified six-read entry, or a precise unresolved blocker if read-only cache/transport requirements cannot be met. Provider use remains disabled without separate exact authority. **Explicit change proposal; no deviation implemented.**
