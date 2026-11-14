# APP-013 / 3A — IQ1 local prerequisite stop

IQ1 implementation/test approval is recorded in `APP013_P08_IQ1_LOCAL_APPROVAL_20261114.json` (commit fa98c82). Local prerequisite testing found a transport limitation before any executable IQ1 procedure or live packet was created. This is not IQ1 completion or a failed provider operation.

## Demonstrated gap

On backend source `6ea74f09195dce87a86fea0fad7f5f48da1a29b3`, the existing `qualification_launch.NativeIO._owned_run/_finish/close` tracks its direct Popen and process group. A finite synthetic subprocess created a descendant in a separate session and exited. The actual existing transport returned success and reported closed while the descendant had not finished. The descendant subsequently completed its fixed two-second task. No provider, credential, database, account or browser access occurred.

Reproduction and captured result: backend `evidence/APP-013/p08-connected-packet-20261110/iq1-local-verification/process_boundary_probe.py` and `process-boundary-result.json`. Run the pinned Python with `-I -B` and that script path. This demonstrates a missing general descendant-closure guarantee. It does not show that Google SDK actually escapes its group, explain R48, or retrospectively invalidate authoritative resource readbacks.

The approved IQ1 checklist requires descendant/process closure or truthful UNKNOWN. Its independent-cleanup section explicitly says: “If independent cleanup cannot be made reliable using these existing primitives within this scope, stop before live execution and report the specific local blocker rather than expanding the runner.” A worker owning all SDK Popen objects addresses main-parent loss but does not, by itself, close this detached-descendant gap. Treating group absence as complete closure would overstate evidence.

## Status and next decision

Completed: approval recorded; actual transport boundary inspected; finite local counterexample reproduced and evidence retained. Checklist item 4 has a demonstrated prerequisite failure. Items 1–3 and 5–6 remain incomplete; no IQ1 executable, source manifest, authority gate, full test suite or live-readiness claim exists. Existing runtime and historical receipts are unchanged. No live packet or attendance request is appropriate.

Implementer owns the next bounded design review: establish whether the exact pinned SDK invocation can be proven not to detach descendants, or prepare an explicit transport-correction change card if reliable closure needs transport changes. Compare both approaches before implementation; no new general supervisor subsystem is authorized. The observable unblock is a local test that rejects or contains this counterexample without adopting foreign/reused PIDs, while preserving finite deadlines and no retries. Tests must also cover launcher/main loss and source/configuration drift. Do not launch IQ1 or another full payment run to discover this behavior externally.

The existing proposal excludes changes to transport semantics, so no such correction has been implemented. No additional owner approval is requested for the already approved IQ1 work; any actual scope expansion must be concrete and reviewed prospectively under AGENTS.md.

3A remains OPEN; accepted 1A/1B/2A/2B remain 4/8; R1 newly closed 0/27. R48 remains consumed; exact prior mismatch UNKNOWN; R47 historical account/session/revocation flags unchanged. Current provider state and credential coverage UNKNOWN. No scope deviation.
