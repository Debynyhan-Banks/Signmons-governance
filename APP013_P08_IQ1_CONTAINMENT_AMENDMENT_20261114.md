# APP-013 / 3A — IQ1 bounded process-containment amendment

Status: proposed local change, not implemented or live-authorized. Backend baseline `ea3ab5b`; governance baseline `764ac83`. IQ1 local approval `fa98c82` remains valid for its original work. This amendment addresses only the demonstrated descendant-closure gap before continuing that work.

## Requirement and evidence

Acceptance remains the existing 3A same-job Sandbox Checkout/event/payment-gate and recovery criterion in APP013_REMAINING_EXECUTION_CONTRACT.md. IQ1 isolates the runtime identity prerequisite that stopped R48; it does not complete 3A or diagnose R48 retrospectively. The approved IQ1 card requires independent process closure and prevents changes to existing transport semantics without prospective review.

Actual `qualification_launch.NativeIO` reports process-group closure, not arbitrary descendant closure. The committed local probe at backend ea3ab5b demonstrates the distinction. Installed SDK `core/metrics.py` can launch a detached reporting subprocess via `Platform.AsyncPopenArgs`; existing `sdk_environment` disables usage reporting. That source finding does not establish that telemetry ran in an earlier attempt or prove all other SDK paths cannot detach.

New finite local design probes establish that `/usr/bin/sandbox-exec` with `(version 1)(allow default)(deny process-fork)` allows a single Python process but refuses `fork`, `posix_spawn`, and detached `Popen` with EPERM on this Mac. The SDK's direct pinned Python entry point successfully parses `iam service-accounts enable --help` with empty disposable configuration and OS-denied network and real credential-directory access. This is parser compatibility only, not credential refresh, provider access or mutation compatibility. The tool's nested sandbox initially refused sandbox installation; the same bounded probe ran outside that tool sandbox with automatic approval. Actual runner availability must be tested locally and must fail closed, never fall back.

Evidence: backend `iq1-local-verification/containment_probe.py`, source hash record and captured results in `containment-review.json`. No actual SDK operational command, real credential read or provider call was made.

## Exact proposed change

Inside the already proposed `iq1_identity_boundary.py`, translate only validated existing IQ1 logical CLI vectors into:

`/usr/bin/sandbox-exec -p '(version 1)(allow default)(deny process-fork)' <pinned Python> -I -B -S <resolved pinned SDK>/lib/gcloud.py <validated arguments>`

Feed that exact vector to the existing owned-process transport. Do not edit the installed SDK, existing transport, other runners or their manifests. Keep actual RuntimeAdapter/NativeIO serialization and RB1 readback semantics. Child creation is forbidden by the OS; same-process execution remains under the inherited restriction. Retain current SDK environment/configuration validation, deadlines, operation/source bindings and independent worker ownership. The independent worker itself is outside this child-only sandbox so it can launch the finite main/cleanup commands. Do not apply the network/credential denials used by the offline probe to future approved provider commands.

Extend the planned IQ1 manifest to pin the sandbox executable, resolved interpreter/SDK entry and reviewed SDK dependencies alongside existing source guards. Verify pins and local sandbox support before execution; missing sandbox, changed source/environment or wrapper mismatch refuses before mutation. No unsandboxed fallback, command substitution, arbitrary command entry, retry, new provider request, token export or additional credential read is permitted. Helpers required by credential configuration must cause a safe refusal, not relaxed containment.

Affected files remain the three originally proposed IQ1 procedure/test/manifest files, their local evidence directory, and governance records. No production module, shared transport or existing operation is changed. One logical CLI command still invokes one SDK command; remote ceiling remains 11 CLI, one enable and one disable, zero explicit cache reads/direct HTTPS/SQL/payment. Local sandbox capability probes are not provider calls and must use disposable inputs. Future live authority must bind the actual wrapped command, not just the logical gcloud arguments.

## Finite work and verification

1. Implement the exact IQ1-only wrapper, authority/source/configuration gates and fail-closed local sandbox support check; reuse original fixed descriptors, serializer, RB1 adapter and process ownership.
2. Finish the original IQ1 worker/journal/reservations/lease/cleanup implementation. The worker owns SDK process objects; main or launcher loss cannot orphan a mutation behind an untracked main child. Abrupt worker loss remains UNKNOWN unless separately proven closed; no automatic replay.
3. Run actual-wrapper tests: valid single-process output; fork, posix_spawn and detached-child denial; missing sandbox/profile/interpreter/source drift; exact command whitelist; timeout, interruption, launcher/main loss, duplicate starts, PID ownership and safe failure output. Never infer cancellation of a remotely dispatched request from local process closure.
4. Complete the original positive/negative/state/UID/configuration/at-most-once and independent-cleanup tests. Lost mutation acknowledgement remains UNKNOWN even after a disabled readback. Ensure helper refusal cannot be hidden by SDK success or produce a false qualification.
5. Run pinned-Python IQ1 and connected/native regression suites, source guards, architecture and required governance/whitespace checks. Publish actual results and committed readiness before any live proposal. Full runtime suites have not yet run for this amendment; five design checks are not replacement acceptance tests.

Original 660-second cleanup and 120-second purge reserves, private-output rules, source/UID binding, 0700/0600 custody, resource lease, independent owner/project/UID cleanup checks and no-retry limits are unchanged. The exact live credential/helper behavior remains UNKNOWN and belongs to the future qualification, never a full payment run by default. No browser/Neon attendance is required for this local work.

## Alternatives, impact and decision

Source review alone is smaller but does not enforce the required no-detached-descendant property. PID polling cannot reliably recover an already orphaned child or justify adopting a reused PID. A general process supervisor or replacement API client would expand scope. The recommended OS restriction reuses the existing transport and prevents the problematic creation at the child boundary.

Impact: one IQ1-only launch translation and focused process tests within the already approved files; no new acceptance section, provider action, spending allowance, dependency-order change or general subsystem. Platform dependency is the installed macOS sandbox facility; unsupported/changed behavior is a refusal. No numerical time estimate is asserted. Rollback is leaving IQ1 disabled/unimplemented; no old operation is replayed.

Requested owner decision: approve this IQ1-only local containment amendment and completion of the existing IQ1 implementation/tests. This does not authorize sign-in, SDK operational commands, credentials, enable/disable, deployment or payment. Implementer owns local completion; owner/cloud/credential custodians retain live authority. Observable finish is the complete original IQ1 checklist passing with enforced containment and truthful unknown outcomes, followed by a separately reviewable live packet.

Accepted 1A/1B/2A/2B remain 4/8; 3A OPEN; R1 newly closed 0/27. R48 consumed, R47 uncertainty unchanged. Explicit prospective deviation proposal: IQ1 launch semantics only; no deviation implemented.
