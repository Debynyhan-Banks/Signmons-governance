# IR2 — R38 remaining runtime identity read

Prepared only; no external authority exercised. Section 3A remains OPEN; accepted milestones 1A/1B/2A/2B remain 4/8. No scope deviation.

## Purpose and inspected evidence
The 3A exit criterion remains same-job Sandbox payment, authentic signed event, application gate and recovery proof (APP013_REMAINING_EXECUTION_CONTRACT.md, section 3A). R38 did not reach authentication or payment. Its immutable r38-result.json records ENTRY_CONTAINMENT_UNCONFIRMED with one runtime identity residual. Resolve that cleanup uncertainty before further payment work; this diagnostic cannot accept 3A.

Source 5e029f9b36f7872f9e809499de6435b1cd367993. Exact commands, operation UUID, manifests and windows are in APP013_P08_IR2_IDENTITY_READ_SCOPE_20261112.json; local verification at 2026-11-12T15:29:42.918757+00:00 is in APP013_P08_IR2_IDENTITY_READ_READINESS_20261112.json. Current source, committed source, SDK/config and exact descriptor validation passed without credential or provider reads. Reuse qualification_launch.py cli_contract, validate_cli_descriptor, NativeIO.cli/_owned_run/close, strict_json and existing project/owner validation. Use committed ir_identity_dispatch.py, which resolves JSON commands to source objects before reservation. Its five actual NativeIO.cli boundary tests passed; process execution was mocked locally. Shared validator unchanged. IR1 remains consumed; no replay.

## Finite execution and finish
1. Before launch recheck approved scope digest, source/SDK/config, clock, and exclusive operation reservation. No existing operation may be replayed. Refuse any mismatch.
2. Invoke only the three ordered descriptors owner, project, identity; reserve each once before invocation. Require exact active owner and ACTIVE pinned project/project-number digest before identity read. Each existing owned-process call is bounded to 30 seconds, with output bounds and no caller retry. Explicit SDK environment validation precedes invocation.
3. Parse identity through strict JSON. Require matching email and nonempty uniqueId. Only explicit boolean disabled=true verifies disabled state; explicit false means enabled; absent/null/wrong type yields UNKNOWN. Do not coerce null or missing fields. Nonzero/timeout/malformed output yields safe failure, never a guessed cause.
4. In finally close owned subprocesses using existing NativeIO.close; independently verify only recorded owned processes absent. Keep sanitized reservation/result/cleanup receipts, no raw provider output, project number, uniqueId, token or credential. Remove owned temporary executor/request files. Never delete SDK credential state authorized below.
5. Report disabled/enabled/UNKNOWN and cleanup evidence. An enabled or UNKNOWN state remains unresolved and requires separately scoped containment authority. No automatic disable or payment retry.

## Authority, boundaries and owners
Owner decision requested: IR2 read-only operation, existing-owner SDK refresh/cache maintenance/internal retries exception, and independent local process cleanup. Exactly three top-level CLI calls maximum; zero SQL, explicit HTTPS, direct cache reads, token exports, sign-ins, cloud mutations, payments or deployments. SDK internal authentication request count is UNKNOWN. Existing credential state may be refreshed by SDK; it is retained under the exception. No new scopes requested. User password input not needed.

Launch before 10:32 a.m. Eastern November 12; reads end 10:33, independent cleanup ends 10:34. TR8 evidence covers beyond 10:35 and owner attendance through 10:45; historical validity does not prove live access. Implementer owns source/pin/deadline/reservation/closure checks; cloud custodian owns provider state; owner controls external authority.

Five fresh local boundary tests passed; no live test claimed. Existing boundaries reused; inspect exact descriptors before dispatch. Runtime enable/disable serialization cause remains UNKNOWN; installed command output:none and adapter object expectation are a hypothesis only. No rollback mutation applies to these reads. Observable finish is a sanitized current identity state plus verified owned-process closure, or an explicit unresolved failure. Approval does not authorize correction implementation or broader execution.
