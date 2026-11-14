# APP-013 / 3A — IQ1 identity-only qualification procedure

Status: local implementation proposal, not yet approved or implemented. No sign-in, password, provider call or attendance is requested. Source baseline: backend `6ea74f09195dce87a86fea0fad7f5f48da1a29b3`; RB1 runtime `157d65dd512ce4b7414c4373cb889985649489cf`. The owner requested the completion plan and then preparation of this procedure. That preparation is not approval to implement or execute it.

## Traceability and bounded change

Existing 3A criterion: “map admitted job/current policy to existing request → expose existing Checkout link → consume authentic matching Sandbox event → demonstrate payment gate and failure recovery. Patch only gaps found in this sequence; no replacement payment stack.” IQ1 qualifies the runtime identity prerequisite that stopped R48 before authentication/payment. R48's `RUNTIME_READBACK` response was discarded; its precise cause remains UNKNOWN. RB1 now classifies the same readback safely, with 638 local regression/governance tests. It has not demonstrated this live boundary.

The current `packet.py`/`entry.py` offers full execution or read-only preflight. Preflight cannot activate the identity and full execution continues through IAM/key/authentication/payment. Repeating the full path imposes unrelated SQL/password setup and can conceal a prerequisite failure. A read of the current disabled state cannot reconstruct the prior post-enable mismatch. Proposed change: one identity-only procedure with local tests, using existing primitives; no new general runner, payment stack, acceptance section or full-entry behavior change.

## Reuse and exact expected files

Reuse the current `RuntimeAdapter.change/readback` and RB1 codes; `NativeIO.cloud` acknowledgement/JSON handling; `restore.command`; qualification owner/project descriptors and project classifier; `sdk_environment`, configuration/source checks and owned-process transport `qualification_launch.NativeIO._owned_run/close`; existing private-inventory/custody/atomic-reservation patterns. KQ1's fixed-phase supervisor is a reference for independent execution, not a key driver to repurpose. Do not modify KQ1 or construct a counterfeit full-native capability.

Expected backend files, all under `evidence/APP-013/p08-connected-packet-20261110/`:

- `iq1_identity_boundary.py`: one fixed-purpose local-proof/native CLI module with strict source/decision/resource binding, finite phase state and cleanup.
- `test_iq1_identity_boundary.py`: synthetic actual-boundary and local process tests.
- `iq1-source-manifest.json`: exact hashes for this procedure/test and its existing dependency graph; no changes to existing native, qualification or KQ manifests.
- A local IQ1 verification directory; governance approval/readiness/completion records.

The adapter exposes only the exact allowlisted owner/project/identity CLI vectors. SQL, HTTP clients, token export, key/secret access, authentication, payment, browser and arbitrary-command interfaces must refuse. Do not call `NativeIO.ensure_owner/credentials`: those would add token acquisition/password behavior. Instead use the existing explicit owner/project and configuration checks before each phase, then route only the existing cloud serializer through the owned-process transport. The new exact IQ1 authority gate must run before constructing native hooks. Importing the module or running local proofs grants no external authority.

## Fixed sequence and proposed live ceiling

Target is the existing `signmons-calldesk-p07-runtime@signmons.iam.gserviceaccount.com` in project `signmons`, owner `debynyhan@signmons.com`. Full command descriptors are in `APP013_P08_IQ1_PROPOSAL_READINESS_20261114.json`, derived from the existing contracts and actual adapter methods with an in-memory synthetic CLI; no provider commands were executed.

| Phase | Maximum commands and required behavior |
| --- | --- |
| Main, 5 CLI | Owner/project checks (2); exact email/uniqueId/disabled metadata (1), requiring initially disabled; persist operation/source/UID-hash and enable intent; enable once (1); run the unchanged RB1 enabled-state readback once (1). No polling or retry. |
| Independent cleanup, 6 CLI | Fresh owner/project checks (2); fresh same-email/UID metadata (1); at most one disable (1), conditional on proven baseline ownership, recorded enable intent and matching UID; unchanged disabled-state readback (1); final metadata/UID confirmation (1). |

Total ceiling: 11 CLI invocations, at most one enable and one disable, zero explicit credential-cache reads, direct HTTPS requests, SQL, key/secret access, browser operations or payment. SDK-internal credential/cache use and authentication retries are not zero and cannot be inferred from CLI count; the existing narrowly stated SDK exception needs separate explicit live approval. No SDK sign-in, token export or credential renewal is inside IQ1. Any required renewal/coverage evidence is reviewed separately after local preparation.

An initially enabled, missing, malformed or foreign identity refuses activation. Cleanup never disables a different UID. If no enable was dispatched, record that no owned mutation needs reversal; do not claim the identity is disabled without evidence. If enable acknowledgement is lost, retain that outcome uncertainty even if cleanup later observes disabled state. Each mutation intent is durable before dispatch; a reservation is consumed even after timeout/interruption. A reserved disable cannot be repeated by main, supervisor or cleanup.

## Independent cleanup, concurrency and retention

Start the bounded cleanup worker and verify its exact ready/binding receipt before enabling. It runs in a separate owned process and remains responsible after main failure or parent loss. Use an IQ1 resource-specific exclusive lease held by that worker through final closure so two IQ1 attempts cannot overlap; duplicate operation/phase execution refuses. This does not claim to lock unrelated external actors or other tools: the live packet must establish that no other approved Signmons operation overlaps.

Before restoration, establish owned main/SDK process closure using the existing process primitives and bound identities; if termination or delayed mutation outcome is uncertain, preserve UNKNOWN and refuse successful qualification. The worker must never adopt foreign/reused PIDs or mutate a replaced identity. Its provider restoration authority is explicitly part of the same future packet, with a fixed deadline and no replay. If independent cleanup cannot be made reliable using these existing primitives within this scope, stop before live execution and report the specific local blocker rather than expanding the runner.

Use exact scope/source/approval/operation hashes, exclusive 0700 roots, owned 0600 single-link receipts and existing atomic reservation/journal patterns. Persist only operation/stage, fixed failure codes, match flags, UID hash, counts, timestamps, process/root binding and residuals. Raw SDK output, project number, UID and any SDK credential remain transient and are never logged. Retain safe evidence; verify private input inventory absent and clear transient references. SDK cache effects remain subject to the separately approved exception, not a promise to erase the user's existing SDK cache.

Future windows must be absolute and finite, with at least the existing 660-second independent-cleanup and 120-second purge reserves; no window is scheduled now. Provider command timeout is bounded at 8 seconds through the owned transport. Clock rollback, source/configuration drift, timeout or interruption stops main work. Cleanup is bounded independently; a clean exit is never equated with a passed identity test.

Final public result keeps distinct fields for boundary outcome, fixed failure code, enable outcome uncertainty, restoration readback, process/configuration/private-data closure and residuals. `QUALIFIED_AND_CLOSED` requires confirmed enabled-state readback, matching disabled/UID final evidence and complete cleanup with no unresolved outcome. It proves observed control-plane state only, not intended-client permission, application authentication, payment or section acceptance. Failure with verified cleanup is reported separately from containment unconfirmed.

## Finite local checklist and finish

1. Bind the new authority/source/resource/command scope and reject foreign or unapproved native entry before any transport. Reuse actual descriptor generation; keep all unrelated interfaces unreachable.
2. Implement the single main attempt and prestarted independent cleanup worker, fixed budgets, intents, exclusive operation/resource ownership and safe receipts.
3. Test true/false/omitted/null/numeric0/1/malformed SDK output through actual serializer and RB1 adapter, plus exact command vectors/counts. Preserve existing predicates. Verify every failure retains a useful safe stage/code with no raw canary text.
4. Test wrong owner/project/UID/source/configuration; initially enabled/missing resource; lost acknowledgement; no main intent; failure before/after intent; interruption, main/supervisor death, descendant processes, PID reuse, duplicate/concurrent starts, cleanup disagreement, expired windows and clock rollback. Tests must establish one enable/disable maximum and independent worker completion or truthful UNKNOWN, without remote calls or real credential reads.
5. Run the new focused suite, existing connected suite, native adapter regressions, actual source/manifest guards, architecture, required governance/baseline/consistency tests and whitespace checks. Use disposable local subprocess fixtures only; no Neon database or live browser gate is required by this procedure. Report existing suite local fixtures accurately. Do not count old RB1 tests as newly run.
6. Publish committed-source/readiness and exact test/cleanup evidence. Then prepare the one live packet with current credential/owner readiness, timestamps, commands, SDK exception, unchanged limits and cleanup authority for a separate owner decision. Do not schedule attendance before this local checklist is complete.

Commands: pinned Python from the current connected packet, `-B -m unittest discover -s evidence/APP-013/p08-connected-packet-20261110 -p 'test_iq1_identity_boundary.py'`, then that directory's `test_*.py` suite and native `p08-native-entry-local-20261101/source` regressions. Run `npm run arch:check`, backend `SIGNMONS_GOVERNANCE_REPO=<governance> node scripts/check-governance-baseline.mjs`, governance frozen-baseline/consistency and the three required governance test files, and both `git diff --check`. Rebuild before any dist-dependent regression if required by the existing harness. All live/source-readiness checks are distinct from synthetic tests.

## Decision, ownership, unknowns and rollback

Requested decision: IQ1 local implementation and tests only. Implementer owns this finite checklist and future exact proposal; owner/cloud/credential custodians own external authority. No password or Terminal attendance is needed for local work. This approval would not authorize enabling/disabling a service account, credential access, sign-in, deployment or payment.

Local source/interface feasibility and descriptors have been inspected. The cleanup worker, its tests and new executable authority gate are not yet implemented; no automated enforcement is claimed. Current live identity UID/state, effective permissions/API behavior and credential coverage remain UNKNOWN and must be addressed by the future qualification-only packet. Historical R47 uncertainty is unchanged; this procedure cannot resolve account/session/revocation flags. R48 remains consumed.

Rollback/disabled state: the new procedure has no native action without its separately committed live decision. Leave existing full/native-preflight flows unchanged; reverting only the eventual IQ1 files/evidence is a separate governed local action and never replays an old operation. No full payment run follows automatically.

This adds one bounded prerequisite procedure, not a new acceptance section or changed 3A criterion. Alternatives considered were another full run or another disabled-state-only read; neither isolates the observed post-enable failure. Scope beyond the three named files/tests/evidence, changes to existing transport semantics, new resource actions or higher limits require a prospective change decision. Accepted 1A/1B/2A/2B remain 4/8; 3A OPEN; R1 newly closed 0/27. No scope deviation implemented; the bounded change is proposed before coding.
