# APP-013 / 3A / P08 — bounded role provenance extension

Status: proposal only. Owner requested proceeding after DBR1; no exact extension or external operation was previously described. This record requests local implementation approval; no live authority or window is created.

## Demonstrated gap and customer connection

Backend fe9581b (runtime50144cb), governance2d6613f. DBR1 sanitized result confirms noMemberships/noDatabaseTemp FAIL and ten other checks PASS; independent cleanup verified. qualification_launch.py role_diagnostic_observation retains fixed conditions only. access_check.py retired_role_query counts incoming and outgoing edges but returns no membership identities; effective TEMP is a boolean. RoleDiagnosticCapability and RoleDiagnosticIO pin the unchanged query, so substituting a query under DBR1 authority is prohibited. DBR1 is consumed.

3A acceptance remains authentic matching Sandbox payment on the admitted job with negative/duplicate/replay checks. This diagnostic addresses the demonstrated database prerequisite blocking that connected journey; it does not satisfy payment acceptance. DATA_CONTRACTS payment policy/job binding and APP013_REMAINING_EXECUTION_CONTRACT section3A remain unchanged.

## Alternatives and proposed change

Repeating DBR1 cannot answer provenance. Blind membership or PUBLIC revocation could affect other roles. Proposed: one bounded provenance mode in the existing diagnostic module, with separate exact authority/query pins and the same three SQL reservations (one catalog observation plus normal and independent cleanup). No new subsystem. No modification of locked access_check.py or weakening of its classifier.

Expected files: qualification_launch.py, its existing unit/PostgreSQL tests, source-manifest.json, one evidence card and governance status. Reuse NativeIO, role cleanup, strict JSON, committed source verification, runtime/resource/environment validation, exclusive reservations and public closeout. Existing DBR1 mode and full qualification semantics remain unchanged.

## Exact data boundary and observable result

Fixed CHILD endpoint/database/admin/role from DBR1; READ ONLY catalog transaction only. Inventory direct membership edges in both directions, endpoint role names, grantor, admin option and version-supported inheritance/set options. Inventory current database owner and TEMP ACL entries including defaults when datacl is null; distinguish PUBLIC, direct and effective inherited access using server permission predicates. Include server version and bounded membership reachability necessary to explain effective privileges. Do not equate an incoming member with inherited access. Cycles, unsupported version, missing/null fields, inaccessible metadata, unexplained effective privilege, or output overflow produce UNKNOWN/incomplete rather than a correction recommendation.

Bound response at existing transport cap; proposed maximum64 membership edges and64 TEMP ACL entries, detect truncation explicitly without refetch or increasing caps. Relevant role names/options are administrative metadata: retain only a validated bounded provenance receipt, never passwords, connection strings, unrelated role catalog, raw SQL output or customer rows. Role-name disclosure/retention is an explicit change from fixed flags and must be included in approval. Names alone cannot establish provider-managed status or safe revocation. Shared PUBLIC impact remains DB-owner review; no claim of enumerating every affected application.

## Finite implementation checklist and readiness

1. Implement a separately authorized provenance mode and fixed query with exact query/resource/source pins; preserve original diagnostic authority separation.
2. Strictly validate bounded output and identity/version semantics; emit complete or UNKNOWN provenance, always candidate null/executionReady false.
3. Reuse three-slot lifecycle, deadlines, one attempt, interruption cleanup and independent public closeout; no CLI/HTTPS/cache/private identifier recovery.
4. Test at real NativeIO serialization boundary and disposable PostgreSQL: incoming/outgoing membership, PUBLIC/default/direct/inherited TEMP, no grant, null/missing/type/duplicate fields, foreign identity, malformed names, cycle/overflow/version limits; unchanged direct ACL distinction.
5. Test denied old authority/query substitution, concurrent launch, cutoff, timeout/oversize, interruption/hard crash, unused independent cleanup and consumed-slot refusal; record actual cleanup and source hashes. Run existing diagnostic/full-module regressions, architecture, frozen baseline, cross-repository consistency and whitespace gates. Browser not applicable: no UI/runtime payment change.

Local prerequisite status: source/interface gap VERIFIED by inspection November9; DBR1 fixed flags and cleanup VERIFIED by immutable receipt. New query/server-version compatibility, parsing, bounds, lifecycle regression and retention checks NOT IMPLEMENTED/UNKNOWN until checklist passes. Live grant provenance, usable access at next operation and provider-managed membership implications UNKNOWN. Implementer owns local readiness; DB owner owns interpretation/correction impact; credential custodian owns hidden password; owner approves scope. No attendance scheduling or execution approval request until local readiness complete.

Rollback/disabled state: absent distinct approved packet refuses new mode; no persistent database changes. Existing mode remains usable only with its own fresh authority. One later qualification-only external packet would authorize3SQL and0Google/HTTPS/cache, fresh timing/source and mandatory cleanup; it is not authorized by this proposal.

Impact: adds five bounded local tasks and one possible later read-only operation within3A; no acceptance denominator, section order or dependency changes. Effort not yet verified. No permission correction, PUBLIC revoke, role grant/revoke, role login, deployment, migration, payment, billing, full qualification retry or other project work.

Finish: validated provenance capability and evidence, then separately reviewed live packet; eventually exact membership/grant-source facts with explicit UNKNOWNs to support a DB-owner correction decision. Accepted1A/1B/2A/2B4/8;3A OPEN;R1newlyclosed0/27.

Deviation proposal before implementation: expand existing diagnostic query and retained administrative metadata only. Owner decision PENDING. No scope deviation implemented.
