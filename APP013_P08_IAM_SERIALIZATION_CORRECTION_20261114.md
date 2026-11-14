# APP-013 / 3A / P08 — IAM serialization local correction

Owner approved “IAM serialization local correction” in chat before implementation. Local only. Source 04160a1e33b532869c57bfbe5bd6d43bd4152278. R43 consumed; LR1 observed lookup absent. Historical failure cause UNKNOWN.

Acceptance served: existing 3A connected same-job Sandbox payment requires temporary access creation and independent removal to process their acknowledgements. This correction does not accept payment or advance the 4/8 milestones.

Inspected gap: entry.Ports supplies NativeIO.cli directly to bridge.Ports; bind/unbind generate dynamic restore_plan IAM vectors without a format flag, then decoded expects JSON. Eight synthetic cases through actual Ports/NativeIO showed both lookup/signing add/remove reject YAML and accept JSON. NativeIO.cloud formatting is bypassed by this path.

Reuse entry.Ports.cloud, restore.command and EntryTests.native_fixture. Exact change: append --format=json only for exact four IAM vectors derived from self.restore_plan. Preserve policy read projection, foreign commands, role/member/condition pins, budgets and readbacks. Files: entry.py, test_entry.py, affected current manifests, this card and sanitized local evidence. No new interface or subsystem.

Identity/state/retention: dynamic operation conditions and scoped roles remain exact; acknowledgement is not state proof. Independent policy readback and cleanup remain required. No credentials, private values, provider or SQL calls in verification. No retention change.

Checklist: record approval/card; implement exact match; verify four mutations through real CLI boundary; reject malformed output; foreign vector unchanged; preserve policy reads; refresh current manifests; run native and connected suites plus governance/architecture/whitespace. Existing suites cover concurrency, expiry, interruption, recovery. No browser behavior changed; browser acceptance remains pending live evidence.

Readiness: source inspected November14; actual dispatch boundary locally reproduced, JSON positive/YAML negative. Dynamic pins reused from actual Ports restore_plan, not reconstructed constants. Deadline/no-retry/cleanup code unchanged and regression suites required. Live credentials, effective access and payment UNKNOWN. This card grants no external readiness or authority.

Dependencies/owners: implementer local correction and checks; owner separate external approval and acceptance. Exclusions: deployment, provider changes, SDK settings, payment execution, new spending, history edits. Rollback: revert this local change and refresh current manifests; external execution remains gated. Observable finish: exact four commands request JSON, negative cases and existing checks pass. No scope deviation beyond this expressly approved correction. 3A OPEN; R1 newly closed 0/27.

Verification completed: native47 + connected50 + correction52 + governance25 =174 passed. Restricted native run had two loopback fixture failures; same suite passed with local socket access. Baseline, consistency, architecture and whitespace passed. Checklist complete locally; live prerequisites remain UNKNOWN. Source diff is four runtime lines plus regression tests and current manifest hashes.
