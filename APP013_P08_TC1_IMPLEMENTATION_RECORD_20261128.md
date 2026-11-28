# APP-013 / 3A / P08 — TC1 implementation record

Owner approved TC1 local timing/cleanup repair and tests in this conversation. `APP013_P08_TC1_LOCAL_DECISION_20261128.json` binds the exact reviewed card at governance158b246 and backend4470996. Baseline and complete consistency passed before coding. No external authority, attendance or new operation.

Work is divided across existing native phase/cleanup code, connected packet/attended supervision, and HTTP/disposal boundaries. The implementer integrates and independently reviews the actual cross-boundary behavior. File ownership prevents concurrent edits; root owns derived source pins. The final inventory below enumerates thirteen current manifests and four hash-only source references. Their update is hash substitution only, with unchanged keys, structure and non-hash values checked. Backend AGENTS.md and historical files remain untouched.

## Inspected focused test dispatches

- Native: `test_child_cleanup.ChildCleanupTests`, `ResponseCleanupTests` and new TC1 ownership cases; selected `test_entry` TC1/CT4/CT5/AQ1 cases. Actual class names are verified before dispatch. No `test_native_postgres`.
- Inherited coordinator: inspected `test_coordinator`/`test_closeout` classes with injected transports only; new pre-intent, between-intent-and-dispatch and post-dispatch deadline cases.
- Native JavaScript: `node --test test_transports.mjs`; `node --test --test-name-pattern='TC1|actual payment preflight preserves|AQ1 direct payment and route' test_connected_payment.mjs`. Browser-bridge/present fixtures are excluded.
- Qualification: `python3 -B -m unittest -v test_qualification_launch.QualificationHttpDeadlineTests test_qualification_launch.ServiceProjectionTests`, synthetic opener/response and real SIGALRM only; no PostgreSQL fixture or broad discovery.
- Connected: inspected `test_packet` classes, explicitly excluding browser fixtures; new actual subprocess/PTY cases use fictional hidden input and owned temporary processes only.

Record final exact commands/results and any fixture adjustments in completion evidence. Existing passing runtime evidence is historical until rerun. No full schedule or live cleanup guarantee follows from synthetic tests. Current provider access/authentication remain UNKNOWN; payment unobserved; accepted4/8,3A OPEN,R1newlyclosed0/27. No scope deviation within approved TC1.

## Routine direct-fixture adaptation, identified before editing

The existing `evidence/APP-013/p08-connected-packet-20261110/test_launcher.py` supplies expired1970 timestamps and partial mocked inputs. TC1's approved deadline/opening checks correctly reject those fixtures. Update only its fixture clock/opening evidence and related expected wiring to exercise the approved interface, preserving assertions and refusal checks. New TC1 behavioral cases remain in test_packet.py. This necessary direct-test adaptation is covered by the owner's approval of the local repair and tests; it adds no runtime behavior, provider scope, acceptance criterion or prerequisite. The implementer resolved this routine test-file choice without another owner decision. Inspect the final diff; do not weaken a guard to retain stale fixtures.

AQ1 CLI/SQL owned-group reaping is reserved inside the existing8second whole-operation budget (up to2seconds reserved for group closure), rather than adding2seconds to every call. Native Node child reaping remains separately counted as reviewed. No timeout/reservation creates a mutation retry.

## Current source-pin dependencies enumerated before editing

Current `authority.verify_sources()` refused the changed coordinator through the active `bound_handoff.verify_sources()` chain. TC1 explicitly permits mechanical current source-pin updates after enumeration and independent review. The additional current dependencies are:

- `p08-native-closeout-local-20261031/source/adapter.py`: COORDINATOR_SHA; its source-manifest.json coordinator/file hashes.
- `p08-serialized-handoff-local-20261031/source/handoff.py`: coordinator/adapter LOCKS; its source-manifest.json sourceLocks/file hashes.
- `p08-real-client-binding-local-20261031/source/bound_handoff.py`: coordinator/adapter/serialized-handoff LOCKS; its source-manifest.json sourceLocks/file hashes.
- `p08-coordinator-auth-local-20261031/source/source-manifest.json`: current coordinatorSha256 metadata.

All paths are under backend evidence/APP-013. Update only these exact hash values and the nine already-listed current manifests, with recursive dependency recomputation. Preserve all executable tokens other than64-character hash literals, manifest structure/non-hash values, guard algorithms, frozen anchors and historical receipt/audit files. Independent review is requested before these substitutions; source guard failures are retained as expected integration evidence, not bypassed.

Independent dependency review confirmed those seven current pins and identified one additional active file before editing: `p08-coordinator-auth-local-20261031/source/authority.mjs` LOCKS pin coordinator.py and adapter.py; verifySources checks them. Include only those derived hash literals and propagate its new hash through the already-enumerated active manifests/LOCKS. No JavaScript extraction or guard logic changes. This completes the inspected four-source-pin/thirteen-manifest set.

## Additional inspected ordinary-purpose regression dispatch

The two existing ordinary-payment journal methods and the existing connected-identity regression class use `fixture_connected.mjs` with injected provider/SQL ports. Its `present` function uses Node HTTP fetch against the owned `127.0.0.1` bridge; it never starts a browser, a real Checkout, a SQL server or a provider request. The restricted sandbox refused that local listen with EPERM, which the existing adapter safely reports as PAYMENT_ADAPTER_UNKNOWN. A separately inspected harmless loopback bind reproduced EPERM while module import succeeded. Rerun only those named synthetic regressions with local-loopback permission; preserve their assertions and all provider injections. This is local process/HTTP verification within the approved ordinary-purpose regression requirement, not a live browser fixture or new provider scope. No production change is justified by that environment failure.

Final review also requires preserving the existing CLI/SQL output-limit classifications when those calls move into the owned-process supervisor. The approved refactor must not turn an overlong SQL error into a child-only category. Focused synthetic assertions cover that boundary; no SQL server is involved.

## Completion

Implementation and inspected verification finished at backendee98bc4891605ad8e96632f15553a7bafc50a4d3. `APP013_P08_TC1_LOCAL_COMPLETION_20261128.md/json` retain the final source-bound result, exact commands, independent reviews, preserved exclusions and remaining live UNKNOWNs.226 focused tests and25 governance tests passed; the localhost-only environment rerun passed without a production change. No further routine implementation decision is pending.
