# APP-013 / 3A / P08 — ND1 local diagnostic correction proposal

OWNER APPROVED local implementation in chat November 11. Implemented and locally verified at backend22a6dc0.  Owner authorized investigation after R30. This is the resulting smallest correction for review; no new live operation.

Source: backend c2e2923e7a7e1b2e626f913a968684aee43b3a69; governance 2d0c406. R30 receipts prove qualification passed, native stopped before PREFLIGHT, no runtime/IAM activation or authentication/payment, independent cleanup and purge passed. Accepted milestones remain 1A/1B/2A/2B, 4/8; 3A OPEN, R1 newly closed 0/27.

## Demonstrated gap and acceptance trace

The existing 3A criterion requires the same admitted job's Sandbox payment, authentic signed event and application/browser state. Native preflight currently loses the safe refusal needed to diagnose a blocked prerequisite. `p08-live-binder-local-20261029/source/coordinator.py:194` recognizes only its own Stop class; native `private_inventory.Stop` and restoration `restore.Stop` are distinct. Thus LOCAL_ADAPTER_OR_SOURCE_STOP does not establish an unexpected implementation exception. R30's original cause and exact preflight boundary remain UNKNOWN.

November 11 local injection through the actual coordinator run/catch boundary, with reserve/save/closeout and provider invocation replaced by inert doubles, produced: native Stop(ROLE_OUTPUT_UNKNOWN) -> generic; restoration Stop(OWNER_MISMATCH) -> generic; coordinator Stop(RUNTIME_PREFLIGHT) -> retained; ValueError containing synthetic private text -> generic. Zero provider calls, credential reads, or filesystem writes. This proves classification loss, not R30's original cause.

## Proposed bounded change and alternatives

Implement an adapter in the current native entry only that records fixed runtime/access preflight stage labels and translates explicitly allowlisted safe codes from the inspected native/restoration/bridge Stop types into the coordinator's Stop. Unexpected exceptions remain generic; never persist raw exception messages, SQL, provider output, identifiers or credentials. Do not alter immutable historical coordinator code, provider commands, permissions, timeouts, retry behavior, cleanup or acceptance gates. Preserve safe refusal semantics; do not convert any failure to success.

Alternatives: repeat unchanged live operation (rejected: same lost diagnostic); persist raw traceback/provider text (rejected: private data); bypass failed preflight (rejected: weakens gate).

## Section card and readiness requirements

Reuse entry.Coordinator, actual inherited run/invoke boundary, EntryTests fixtures and current source manifest mechanism. Expected files: native entry.py, test_entry.py, corresponding current source/test manifests, source-binding references only where existing validators require them, and sanitized local evidence. Before edits inventory every transitive current manifest consumer; no historical frozen-anchor rebaseline. Unexpected immutable-source conflict is a STOP.

Finite checklist: inventory relevant Stop types and constant error codes; implement stage and explicit-code normalization at the current entry boundary; test each source type and both preflight stages; reject arbitrary message/unknown code/unexpected exception; prove no enablement after preflight refusal and cleanup still runs; verify independent closeout and interruption behavior unchanged; run full existing native and connected packet suites and applicable qualification/source-validator checks; required governance/architecture/whitespace checks; record exact source and sanitized proof.

Tests must call the same inherited coordinator boundary, not only a new helper. Include normal path, recognized code, unknown code, synthetic secret text, cross-module Stop identity, interruption and cleanup failure. Concurrency/one-use and cleanup tests reuse existing suite. Browser tests are not relevant to diagnostic serialization; no claim of payment/browser acceptance. Exact commands and resulting source graph must be recorded before any later execution proposal.

No new identity/data store/retention or provider action; safe fixed stage/code fields only in existing journal. Owner approves this bounded local correction; implementer owns implementation and local verification. Unknown original failure remains unknown until independently established. Disabled state remains consumed R30; rollback is reverting only ND1 changes. Observable finish: native preflight retains tested safe codes/stages, arbitrary text stays suppressed, existing gates and cleanup pass. No deadline/authority extension or fresh live session included.

Effort: one focused diagnostic correction and regression verification, no new acceptance section or dependency subsystem. Explicit deviation proposal: broaden local diagnostic work from inspection to the correction above; approved by owner before implementation under AGENTS.md prerequisite-change rule. Correction and verification are recorded below.

Pre-edit consumer inventory: native source-manifest entry.py; native test-manifest test_entry.py and runtimeManifestSha256; current key-correction source-manifest entry.py and native source-manifest. Historical manifests/receipts remain unchanged. Source-gate checks are mandatory after these current bindings refresh.

## Implementation review

Owner approved ND1 in chat before edits. Runtime change is confined to current entry.Coordinator.invoke: only non-cleanup preflight calls record one fixed stage and normalize allowlisted codes from native, restoration, bridge packet, and coordinator Stop classes. Unknown codes, other exceptions, and arbitrary text remain generic. All other calls delegate unchanged. The historical coordinator and its source pin are untouched. Added actual assembled-entry regression covers both preflight stages and ten cases each; verifies no activation/authentication, closure, empty residuals, private purge and secret-text absence. Existing tests cover positive execution, independent closeout, cleanup failure, concurrency and interruption.

Current native/source-binding gates PASS. Native32, connected38, correction52, governance25 tests PASS; qualification230 passed in sandbox and sole process-inspection-blocked case passed unchanged on host rerun; composed qualification17 passed. Initial sandbox native run had two local loopback-fixture failures; approved host run passed unchanged test expectations. No external operation, credential read, payment, deployment or new source authority. R30 remains consumed; exact original refusal remains UNKNOWN. Rollback is reverting ND1 entry/test changes and their three current manifests only.

## Final closeout

ND1 local diagnostic correction COMPLETE at backend22a6dc0 under owner approval. Current native entry records fixed runtime/access preflight stage and preserves explicitly allowlisted safe Stop codes across module boundaries; unknown errors/private text remain generic. Historical coordinator/commands/gates unchanged. Actual assembled regression covers20cases across both stages, no activation/authentication and successful cleanup/private purge. Native32,connected38,correction52,composedQualification17,governance25 pass. Qualification230 passed in sandbox; sole ps-permission-blocked parent-death test passed unchanged on host rerun. Current/committed source checks, baseline, consistency, architecture and whitespace pass. Evidence evidence/APP-013/p08-connected-packet-20261110/nd1-local-verification.json. No live provider or credential action. R30 remains consumed/closed; original preflight cause UNKNOWN. Implementer owns next source-bound qualification-only readiness proposal to isolate the native preflight refusal before another full payment attempt; owner retains external authority. Same-job Sandbox payment/event/application/browser acceptance remains pending. Accepted4/8;3A OPEN;R1newlyclosed0/27. Approved ND1 correction complete; no further scope deviation.
