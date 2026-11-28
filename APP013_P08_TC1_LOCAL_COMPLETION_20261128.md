# APP-013 / 3A / P08 — TC1 local completion

TC1 is implemented and locally verified at backend **ee98bc4891605ad8e96632f15553a7bafc50a4d3**. Owner decision `APP013_P08_TC1_LOCAL_DECISION_20261128.json` binds the review at governance158b246 and baseline backend4470996. This completes the approved timing/cleanup amendment; it grants no live authority.

## Requirement and final behavior

The existing 3A criterion remains one admitted job with authenticated protected access, owner Sandbox payment, an authentic matching event, a cleared payment gate, cleanup and owner acceptance. TC1 repairs the attempt timing and cleanup prerequisite; it does not count as customer acceptance. The review identifies the inspected missing behavior and source hashes; the companion completion JSON binds every changed file and the exact commands/results below.

- AQ1 setup is capped at780seconds, including hidden input of at most120seconds. Its authentication child is capped at240seconds, payment preflight at30, and post-settle admission at600. The unchanged IAM settle reserve is420. Wall and monotonic clocks both constrain the actual execution boundaries; ordinary-payment timing stays unchanged.
- Qualification response close, native stream cancellation, endpoint input and Git approval reads are bounded. Primary safe errors survive disposal failure. Owned CLI/SQL processes preserve their existing output/error categories; each8second call includes its reaping reserve. Node children retain separately counted bounded reaping.
- Main AQ1 cleanup stops before workEnd and reserves time for owned-child closure, a durable acknowledgment and parent exit. A separately supervised independent attempt requires the prior parent to have exited, the complete source/operation-bound inventory to match, all recorded groups to be absent, the attempt to be unconsumed, and the full unchanged660seconds to remain. Both phases handle interruption cooperatively. An unknown/live child blocks overlap; parent-group termination is never treated as descendant proof.
- Cleanup budgets are checked before intent. An expiry after intent but before dispatch records bounded positive no-dispatch provenance. Only that evidence permits one first independent dispatch; issued/ambiguous actions remain consumed. The key's one-use transient grant cannot become permission for a second DELETE. Attempted-action history is preserved. Deferred cleanup still writes the work result.
- AQ1 opening checks consume the actual committed successful sign-in record and its exact opening decision. The existing recovery interface receives a pre-dispatch callback on the actual validated capability. The opening decision must include `connectedSession` with recovery/qualification/native operation IDs and the fixed purge time. The `--recover-first` route checks this before recovery I/O; later checks use recovery's recorded actual start, source and scope. Historical unbound records cannot be reused.
- One shared source calculation enforces latest native admission: `min(native cutoff, forward end) - (780 +420 +600)`. Qualification and native approval waits are clamped to that earlier instant. Actual time is checked after prior stages and before dispatch. Purge remains fixed from opening, custody remains at most3600seconds, and cached credential expiry must remain strictly later than purge.

## Finite checklist and evidence

All TC1 implementation items and the inspected local verification are complete:

| Verification | Result |
| --- | --- |
| Native phase, provenance, owned-process/journal and response cleanup |41 passed |
| Inherited coordinator and closeout |21 passed |
| Packet, launcher, approval waits and two actual PTY/process scenarios |51 passed |
| Native HTTPS/disposal, selected payment boundaries and qualification/recovery callback |76 passed |
| Ordinary-purpose, identity, timing and child/journal regressions |37 passed |
| Required governance test files |25 passed |
| Current/committed source guards, frozen baseline, cross-repository consistency, architecture and whitespace |PASS |

The226 focused test executions use injected provider/database ports, fictional input and harmless owned processes. The two PTY cases verify no-echo input, timeout/interruption, detached-group closure and survival of an unrelated sentinel. Actual Handoff→NativeIO→Node tests preserve authentication diagnostics across successful output, safe refusal, lost output, timeout and independent interruption. Corrupt snapshot/provenance and consumed-attempt cases refuse. Fast synthetic timing admits; slow, expired or inadequately covered timing refuses without rebinding deadlines.

The exact commands, final tested-file hashes, result timestamps, log hashes and independent review summaries are retained in `APP013_P08_TC1_LOCAL_COMPLETION_20261128.json`. No broad test discovery, PostgreSQL server/fixture, browser opening, real credentials, provider call or payment was used. Existing application tests from the earlier repair remain historical and are not counted here.

## Integration findings resolved

Source guards initially refused intermediate hashes during parallel local editing; final current and committed guards pass without a bypass. The review caught and repaired potential overwriting of child authentication fields by process-inventory persistence, as well as the corresponding exact parent-snapshot transition. Opening validation now runs on the actual recovery capability to avoid validating one envelope and dispatching another. Qualification waiting and final parent-exit checks use the same deadline rules.

The ordinary-payment synthetic fixture initially failed because this sandbox refused its owned127.0.0.1 HTTP server with EPERM. The same37 regressions passed with reviewed local-loopback access and all provider/SQL injections unchanged. That environment failure did not justify a production change. The fixture uses an HTTP test client; it launches no browser or Checkout.

A conservative source-bound journal-size fixture is65,051bytes with all20 optional no-dispatch markers, below the65,536byte private reader limit; the two-marker path is58,705bytes. This arithmetic verifies the new bounded inventory shape, not arbitrary future payloads.

The direct launcher fixture was updated for valid current clocks/opening evidence. Four additional current source-pin files and four current manifests were enumerated and independently reviewed before mechanical edits, as the approved card permits. Final scope is18 behavioral/test files,4 hash-only source references and13 current manifests. Manifest structure/non-hash values and executable tokens outside hash literals in those4 pin files are unchanged. Unrelated AGENTS.md and historical receipts/anchors are preserved.

## Readiness disposition and remaining work

**Local TC1 proof is complete. No live session is scheduled or execution-ready.** The following distinctions remain mandatory:

| Prerequisite / boundary | Evidence and current result | Responsible role |
| --- | --- | --- |
| Output contracts, missing fields, safe failures, response disposal |Final source and synthetic actual-boundary tests above; PASS locally |Implementer |
| Opening, exact resource/source pins, dynamic purpose and environment |Actual validators and committed-source guards pass locally; a fresh approved opening/result is still required |Implementer and owner |
| Effective identity/permissions, APIs, database and deployed authentication |Current live facts UNKNOWN; metadata/fixtures are not access proof |Owner authorizes the smallest qualification; implementer observes |
| Timing, concurrency, interruption, owned-process cleanup |Actual local process/PTY and source-bound tests PASS; no automatic retry or overlap |Implementer |
| Restoration within660seconds |Not guaranteed. Completed-main source bounds are about522/554seconds before hidden input/local work; partial-main can require about915. The allowance is a finite attempt horizon |Implementer must report residual-state feasibility before attendance; owner retains policy decisions |
| Retention |Fixed opening purge, at most3600second custody and120second purge reserve are enforced locally; no fresh private inputs retained |Implementer |
| Customer acceptance |Live authentication UNKNOWN, payment unobserved; accepted1A/1B/2A/2B remain4/8,3A OPEN,R1newlyclosed0/27 |Owner |

Next observable result is a fresh source-bound **qualification-only** readiness record with feasible actual windows and explicit restoration limitations, then a useful bounded authentication outcome only under separate external approval. The remaining connected payment/event/gate/acceptance work is unchanged. R67/R68 causes remain UNKNOWN and their consumed attempts are not reusable. No provider, credential, sign-in, billing, deployment, merge, customer contact or support action is authorized by this completion.

Rollback restores these local files and derived pins; there was no provider change to roll back. **No scope deviation within the approved TC1 repair and tests.**
