# APP-013 / 3A — IQ1 exact identity-only qualification

Status: QUALIFICATION ONLY; prepared, not approved or launched. Operation `1993c5da-d093-4a4c-a950-bf50cb5bae48`. Runtime source `bdec9fa789b7a749434bf81fd23b843b885e4ebf`; manifest `5fbdcc7394ba8f8757bd6b593764f5c19129bb9c93d5e317748edba11dbdc8f5`; scope `cf73007780b912b6b2245706baccb5f6319cc2e9d183451f180d95713554b9eb`. Exact scope, logical and actual wrapped command arrays, configuration binding and readiness are in APP013_P08_IQ1_LIVE_READINESS_20261114.json.

## Purpose and bounded action

Qualify the existing Google runtime identity prerequisite that stopped R48 before authentication/payment. Reuse the completed IQ1 procedure and actual RB1 serializer/readback; do not repeat a full payment run. Target: `signmons-calldesk-p07-runtime@signmons.iam.gserviceaccount.com`, project `signmons`, existing owner `debynyhan@signmons.com`.

One main sequence: current owner and project reads; exact email/UID/initially-disabled metadata; persist one enable intent; enable once; observe enabled state once. Independent cleanup: fresh owner/project and matching UID metadata; reserve at most one disable of that same proven identity; disabled-state readback and final matching-UID metadata. Initially enabled/foreign/missing/malformed identity refuses before enable. Lost acknowledgement retains UNKNOWN even if later disabled. No retry, polling, different identity, permission expansion or replacement operation is authorized.

Maximum 11 SDK CLI invocations: main 5, independent cleanup 6; at most one enable and one disable. Zero explicit credential-cache reads, direct HTTPS calls, SQL, key/secret access, token export, browser, payment, refund, booking or customer message. SDK-internal authentication/API retries and cache maintenance are covered only by the exception below; their internal request count is not asserted to be zero or bounded by 11. This changes a Google service-account state temporarily; it does not itself make a Stripe payment.

## Exact window — November 14, 2026, Eastern

| Boundary | Time |
| --- | --- |
| Earliest start | 4:55 p.m. |
| Launch cutoff | Before 5:10 p.m. |
| Main work ends | 5:15 p.m. |
| Independent cleanup ends | 5:26 p.m. |
| Input-file removal/private inventory check ends | 5:28 p.m. |
| Requested reachability | Through 5:30 p.m. |

The 660-second cleanup and 120-second purge reserves are unchanged. This is a maximum window, not a required wait. Each SDK invocation is limited by the existing 8-second owned-process boundary. Expired approval does not renew itself. No operation starts without the exact owner decision and confirmation of reachability/no overlapping Signmons operation. No password prompt or Terminal attendance is needed.

## Credential and spending exception

Permit the existing owner SDK's normal refresh, narrowly internal authentication retries and cache maintenance under `SDK_EXISTING_OWNER_REFRESH_CACHE_INTERNAL_RETRIES_NO_TOKEN_EXPORT`. This is not approval for browser sign-in, new scopes, external credential helpers, credential renewal commands or explicit token/cache export. Existing environment/configuration guards must pass. Current credential usability and enable/disable permissions are UNKNOWN; initial current owner/project reads qualify entry before mutation. Failure stops this attempt, followed by applicable cleanup; it does not trigger automatic renewal or another attempt. Future cleanup credential success cannot be guaranteed by a local test or historical horizon.

Additional spending allowance is $0; this is not a hard cloud billing cap and does not erase existing liabilities. No deployment, billing configuration, paid test, real charge or payment action is included.

## Launch, custody and closure

After approval only, persist the exact public scope plus the committed decision reference in a 0600 envelope in the exclusive 0700 directory `/private/tmp/p08-iq1-input-1993c5da-d093-4a4c-a950-bf50cb5bae48`. The exact launcher argv is recorded in the readiness JSON. It invokes the existing module's `--run` interface using the pinned Python and fixed module directory. No executable temporary helper is needed.

Each allowlisted logical CLI vector is translated by the approved IQ1 implementation to `/usr/bin/sandbox-exec -p '(version 1)(allow default)(deny process-fork)' <pinned Python> -I -B -S <pinned SDK>/lib/gcloud.py <exact arguments>`. Full vectors are in the bound scope. Missing/changed sandbox or any pin mismatch refuses, with no unsandboxed fallback.

The prestarted independent worker holds the IQ1 resource lease, owns all SDK process objects, and verifies its ready receipt before enable. The main coordinator cannot make provider calls. Verify the final result via the existing read_result/custody checks, worker/process closure, immutable call/intent receipts and private inventory. A killed worker or missing result is UNKNOWN, never success or permission to replay. No arbitrary discovered PID is adopted. The IQ1 lease protects IQ1 instances only; owner must confirm no other Signmons operation overlaps.

Remove the input envelope/directory after the copied worker envelope is available and no later than purge end. Preserve only public scope and safe operation/stage/count/UID-hash/result receipts in `/private/tmp/p08-iq1-1993c5da-d093-4a4c-a950-bf50cb5bae48`. Raw SDK output/UID/project-number values are transient; no private input file is required. The safe resource-lock inode remains to prevent lock replacement races. Do not delete the user's SDK cache. Any unresolved identity/process/configuration/retention outcome is reported to the owner/cloud custodian; no new mutation is inferred from cleanup failure.

## Readiness record and finish

Current source/manifest/configuration shape and exact descriptors passed the actual IQ1 validators; committed source checks and an inert approval-shape test passed (the inert reader was not real authority). Fresh local sandbox fork-denial/process-close check passed. Source unchanged from the completed 187 connected tests (51 IQ1), 135 native tests and 25 governance tests; those runtime tests are historical same-source evidence, not newly rerun. Preparation invoked no provider, SDK operational command or credential-cache read, and created no attempt root/reservation. Current provider state, UID, effective permissions and credential usability remain UNKNOWN—the purpose of this smallest bounded qualification.

Before launch, recompare actual source, configuration hash, logical/wrapped commands, exact committed decision, current time, root absence and non-overlap against this record. Inconsistency blocks launch, without rebaselining. Implementer owns these checks, one launch and closeout; owner/cloud/credential custodians own the explicit action/SDK exception and unresolved external facts.

Finish is either `QUALIFIED_AND_CLOSED` with observed enabled state, matching disabled final UID and complete closure, or one classified failure with explicit UNKNOWN/residuals. Neither outcome demonstrates intended-client access, authentication or payment. No full connected payment run follows automatically.

Requested decision: approve this exact IQ1 identity qualification, the stated SDK refresh/retry/cache exception, $0 additional allowance and independent cleanup/input removal; confirm reachability through 5:30 p.m. and no overlapping Signmons operation. The existing local implementation approval does not authorize these provider state changes under AGENTS.md.

Completed: local IQ1 and exact qualification preparation. Remaining 3A: this live prerequisite, current connected readiness/authentication, same-job Sandbox payment/event/application recovery, closure and owner acceptance. Accepted 1A/1B/2A/2B remain 4/8; 3A OPEN; R1 newly closed 0/27. R48 consumed; R47 historical uncertainty unchanged. No scope deviation.
