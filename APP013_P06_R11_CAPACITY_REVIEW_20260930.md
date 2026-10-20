# APP-013 / 2B / P06-R11 read-only capacity review

Status: approved read-only review completed once; result verified and interpreted. No further read or write authorized. This is one bounded diagnostic within existing2B, not a new acceptance section. Build-only approval and its 7:30–8:15 window do not authorize this database review.

## Question and verified local basis

Determine which verification allowances block another connected journey, and whether the retained address operations identify sessions with remaining protected payload. Do not repeat the original submission or pretend a clearer refusal fixes capacity.

The consumed September30 06:53Eastern snapshot (operation9b7217da-290d-4635-a0c3-1518b345daa7) reported phone10holds/USD5 and address account/tenant each6rows/USD0.60, no matching job or exact-request address intent and no session identified by that narrow join. These are historical observations, not current database state; zero correlated sessions does not prove no retained session/payload.

Saved enabled28 runtime packet binds address account6requests/USD0.60, tenant6/USD0.60, session2/USD0.20, per operationUSD0.10; phone accountUSD5 and per-flow reservationUSD0.50. Its phone and address allowances were both exhausted at the recorded snapshot. Scope overlap means address account/tenant totals must not be added. Reservations are not invoices.

Source address-operation-ledger.ts aggregates every retained row for count limits, without state or time filtering. Cancellation only changes eligible RESERVED rows to CANCELLED/zero heldMicros; it does not remove the row. Session closure/payload purge also does not release historical rows or liabilities. A money release alone therefore cannot restore an exhausted row-count allowance. No automatic daily reset is established by this source.

The older scripts/p06-r11-address-capacity-diagnostic.mjs has historical2request/USD0.20 comparison constants. Reuse its SELECT aggregation and validation concepts, not its readiness label. Compare against the exact saved packet6/USD0.60 instead, clearly marked historical approved limits; no current policy approval is inferred.

## Fixed scope, evidence and reuse

Backend baseline3cf8a9dc53d0282a35e6263a36d749c5b32f8e2e plus reviewed local refusal correction. Built candidate digest sha256:533baa19504fb3a6525242c2e877d5921d7713669f7bb2e599bca264d012ee48; image unused. Source archive12bfaafc7aec232e349ad03e484ea8684fe8ce3d1db8625b577043aa07286d13. No application changes proposed.

Use the same fixed PG18 TARGET/database/user and participant/account/tenant bindings as the completed outcome reader, without reusing its operation. Reuse READY-first owner hidden-password input via anonymous pipe, TLS certificate checks, source/dependency hashes, identity/version verification, exclusive one-use attempt, read-only repeatable-read transaction and rollback-before-result. Never request passwords in chat, persist them or print them. Saved packet path: /Volumes/Signmons-P06/r11-supervised-run-20260929-0800/runtime-packet.json. Packet SHA256: be338c4477cf07f20f3b8a729a94311f1f4acbcae4a499f030bfe4f4cf217748.

## Exact proposed read set

1. Current account-scoped phone reservation audit metadata, same allowlisted staging/controlled held actions as the previous reader: version, state, currency, reservedMicros and packet-match boolean only. Output total held counts/micros by staging/controlled and same-old-packet/other-packet; reject malformed rows, invalid currency/state/amount or more than10000 rows. No phone, provider credential, verification code, event body or invoice query.
2. Address account aggregates and fixed-tenant subset: count, sum heldMicros, invalid count. Preserve all states and rows, including CANCELLED. Output separate count-headroom and money-headroom comparisons against the saved limits. No inference that a new session escapes account limits. Reject malformed totals or account inventory exceeding100rows; no pagination or widening.
3. For only that fixed account AND tenant, read at most101 operation metadata rows ordered by createdAt/id: state, heldMicros, createdAt, executionDeadline, attemptId-present boolean, alias count and exact-original-intent-match boolean. Group by existing conversation/session inside SQL or private process; output only per-snapshot ordinal group numbers, operation/session counts and totals, no opaque identifiers or policy/provider bodies. The101st row is a stop, not a partial report.
4. Only sessions identified through those account/tenant operations, matching both Conversation.id and collectedData.sessionId with tenant equality: status, hasLifecycle, closed, purged, hasVerificationOperations, hasLocalPhone, hasLocalAddress, and hasProtectedIntakePayload booleans. Reuse the original strict tenant-bound CommunicationEvent/CommunicationContent EXISTS predicate. Report unmatched/ambiguous correlations explicitly; do not scan unlinked sessions or infer identity from timestamps. Output no collectedData/payload values, addresses or names.
5. Refresh only original request4d5b5043-c975-48ab-b899-f8c2c29b9e8a job count/states and controlled-submitted/admitted audit counts, plus the two enabled-approval booleans, runtime role canLogin/connectionLimit/expired and active session count. Reuse corrected text-to-UUID casts. More than one matching job, contradictory correlation, invalid booleans or an unexpectedly enabled runtime/approval produces a stop classification, not an automatic repair.

Connection settings: current fixed target and PostgreSQL18 identity check; default_transaction_read_only=on, connection timeout5s, statement timeout10s, lock timeout5s, query timeout12s. One connection/transaction/attempt, rollback and connection close even on failure. Save sanitized result only after successful rollback. No retry after an uncertain attempt. Raw query errors/rows are not copied to chat or durable output.

## Output and decisions

Output distinguishes phone-money headroom, address-count headroom, address-money headroom, operation states, session-retention flags, original-request disposition and closure controls. Use fixed classifications for LIMITS_EXHAUSTED, SNAPSHOT_HEADROOM_ONLY, INCONSISTENT_STOP and UNCONFIRMED_DO_NOT_RETRY. Any headroom is snapshot-only, not reservation or permission to run.

If counts remain6, cancellation or payload cleanup cannot by itself restore the existing address count allowance. If phone holds remainUSD5, anotherUSD0.50 flow exceeds the old phone allowance. Preserve every hold and row. Later choices must be separately presented: retain the closed state; reconcile specific liabilities where evidence permits; or request an explicit prospective policy/budget change that retains historical liabilities and the one-journey scope. This proposal authorizes none of those changes and does not recommend an amount without evidence. Do not solve limits by deleting rows, changing account identity or silently raising ceilings.

No cloud refresh in this capacity-first read. The just-built image digest/cleanup evidence remains saved evidence; runtime target/provider qualification would be separately scoped after the capacity decision, before deployment. This avoids refreshing unrelated cloud metadata while a known prerequisite is unresolved.

## Finite implementation/execution card

Acceptance link: existing2B truthful refusal, retained progress and controlled exactly-one-job admission. Demonstrated gap is the old request-only join's inability to identify retained operation sessions and the need to distinguish count versus monetary gates. Existing reader components above are reused; no subsystem/schema/runtime API.

Expected files after approval: one fresh private reader/query/wrapper/plan/binding/authorization directory, local synthetic/SQL test evidence and governance/backend handoff only. No edits to consumed helpers. Data identity/retention boundaries are the fixed scopes and metadata-only projections above; result contains no participant input.

Checklist: (1) exact scope/source/read set/proposal prepared; (2) after approval bind fresh operation and future25-minute Eastern window, prepare helper; (3) validate positive exhausted/headroom cases, legacy-threshold trap, CANCELLED rows still count, grouped/unmatched sessions, foreign bindings, privacy, malformed/duplicate/overflow, timeout/rollback and consumed/expired guards; actual disposablePG18 PREPARE/execution tests for joins/casts, then remove fixture; (4) exclusive0700/0600 install/readback, no-action check; (5) owner hidden input and one read, rollback/close; (6) sanitized interpretation and explicit next decision. Stages2–6 remain unperformed, not claimed complete.

Commands/gates: helper syntax/AST and synthetic tests; real localPG18 SQL checks; backend architecture/governance baseline, governance frozen/consistency and21safeguard tests; whitespace both repos. Earlier2413 runtime tests and10browser cases are historical implementation evidence, not new reader validation. No browser/provider tests in this read.

Owner decision requested: approve preparation, installation and ONE read-only database snapshot of the exact expanded operation/session metadata scope above; choose a future25-minute Eastern window and enter the existing password privately when prompted. This involves authenticated access to live private metadata using an existing privileged database login, constrained by read-only mode; it is not a database/runtime-role configuration change. Start before the final5minutes of the chosen window. Implementer owns preparation/validation/result review; owner owns scope/window and hidden input. No cloud/provider/database mutation, deployment, new request, job creation, hold release, cleanup mutation, broad tenant scan or paid verification. No inherited build permission or expired-window reuse.

Finish: one validated sanitized snapshot or preserved safe stop, then a concrete decision about blockers. Runtime stays closed; rollback concerns only the read transaction. P06 remains12/14,R11/fullR12open;accepted1A/1B/2A remain3/8. No scope deviation in preparation. Expanded diagnostic join requires the explicit decision above before implementation/execution.

## Owner-approved execution card — September 30, 7:55–8:20 a.m. Eastern

Owner approved the exact read-only metadata scope, selected7:55a.m., accepted the stated8:20a.m.end and said proceed. Fresh operationad6a22c0-7cf7-425b-a2cd-f22dfa23161b; window11:55–12:20UTC, start before12:15UTC. Preparation/install/one owner-hidden-input read authorized; no writes/provider/cloud actions. Reuse fixed clean reader dependency source0df9b9d and unchanged existing transport; add only approved metadata query module and local tests. Prior consumed readers remain untouched. Proposal checklist2–4 now in progress;5–6 require owner hidden input/result. No scope deviation.

## Installed and validated — owner hidden input next

Operationad6a22c0-7cf7-425b-a2cd-f22dfa23161b; seven files installed exclusively0700/0600 at /Volumes/Signmons-P06/r11-capacity-review-20260930-0755, byte readback and installed no-action check passed.11query tests,6reader guards,12private-input tests,11actualPG18PREPARE statements/nineSQLscenarios pass; disposable cluster removed. Evidence: backend evidence/APP-013/p06-r11-capacity-reader-20260930.md. Checklist1–4complete;5–6pending owner hidden input and result. No live read or acceptance advance. No scope deviation.

## Completed read-only snapshot — September 30, 8:07 a.m. Eastern

Owner reported R11_CAPACITY_REVIEW_LIMITS_EXHAUSTED. Saved operationad6a22c0-7cf7-425b-a2cd-f22dfa23161b attempt12:07:01.778UTC/result12:07:15.274UTC verified within approved window. Reader saves result only after READ ONLY rollback. Result SHA256d23ac7d36fe641b6c93aeef8989916c4fc57596c753a3a95fe2af065305fc594. Consumed; do not rerun. No new query during review.

Phone:10holds/USD5, one staging/other packet, eight controlled/other packet and one controlled/saved enabled28 packet. Address: account and tenant each6rows/USD0.60 (overlapping scopes, not additive), invalidCount0. All six rows OBSERVED, attempt present, one alias each; two operations per each of three linked session groups. Four operations dated September21, two dated September29. None has the original final request intent. OBSERVED is the ledger state, not proof of provider invoice amount or eligibility for releasing liability. Neither cancellations nor money releases are justified by this result.

All three operation-linked sessions match strictly and remain statusONGOING, hasLifecycletrue, closedfalse, purgedfalse, hasVerificationOperationstrue, hasProtectedIntakePayloadtrue. hasLocalPhone/hasLocalAddressfalse only means those keys absent; it does not mean the protected payload lacks private input. No payload values read/output. These are three historical operation-linked sessions, not proof that the narrow original-request join identifies its session. Unmatched count0 within this scope is not a global session inventory.

Original request still has job0, submitted/admitted audit0 and exact-intent operation0 at this snapshot; its original failed guard is still unproved. Both approvalsfalse; runtime roleNOLOGIN, connectionLimit0, expiredtrue and sessions0. This is database closure evidence, not a fresh Cloud Run target/traffic read. Built image remains unused.

Both saved phone monetary and address count/monetary limits are exhausted. Session cleanup alone cannot free the retained address row-count allowance. Recommended order: prepare a narrowly scoped close-before-purge proposal for these three sessions using existing safeguards, preserving jobs/audits/operation rows/holds; obtain explicit cleanup-write approval before executing. Then prepare a prospective bounded allowance decision for one connected journey, accounting for all retained liabilities. Neither cleanup nor policy change is authorized by the read-only approval. No new session/request to bypass limits, arbitrary deletion, provider reconciliation claim or automatic rerun.

Capacity review checklist1–6complete: prepared, validated, installed, owner-executed, result verified and interpreted. R11/fullR12 remain open because live job journey and cleanup/acceptance are not complete. Implementer owns a concrete cleanup proposal on owner direction; owner controls any writes and later capacity policy. P06 remains12/14;accepted1A/1B/2A remain3/8. No scope deviation.
