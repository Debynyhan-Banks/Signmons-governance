# VM2 — proposed local preparation for one metadata diagnosis

PENDING OWNER DECISION; no implementation or new external action is authorized. APP-013 / 3A / P08. Backend runtime source 6df778d9858ff728d10e02f2b69084886a7cb102; R57 safe closeout evidence commit 9a75393. This is a bounded diagnostic preparation, not an additional acceptance section or a new connected workflow.

## Demonstrated gap, traceability and alternatives

Section 3A requires the same admitted job's Sandbox payment, authentic signed event and application settlement before owner acceptance (APP013_REMAINING_EXECUTION_CONTRACT.md, section3A). R57 could not qualify its current entry conditions: the ninth CLI command, metadata for signmons-staging-p07-payment-database-url version1, returned PROCESS_REFUSED. The exact command and immutable receipts are in APP013_P08_R57_STOP_RESULT_20261124.md. Existing qualification_launch.NativeIO._owned_run discards stderr for this command. R57 is consumed and closed; authentication and payment were not attempted. The demonstrated gap is safe observability of this exact prerequisite, not a demonstrated permission or provider defect.

Inspected alternatives: the existing VM1 NativePorts.http accepts this metadata endpoint but discards all non-200 detail; the SQ1 transport retains safe errors but excludes Secret Manager from its host allowlist; qualification HTTPS descriptors do not admit this metadata GET. The billing/SQL diagnostic flags explicitly reject this command and must not be bypassed. Another full R57-like session would not recover the discarded detail. A direct CLI stderr diagnostic could classify a leading typed status but cannot reliably distinguish service-disabled from permission-denied explanations. No existing unchanged command provides the required safe distinction.

Proposed bounded change: one isolated operator procedure using existing owner/project, cache, strict JSON, error classification, deadline and process-cleanup seams. Its only prospective provider resource request is metadata for the exact version; it can never read the secret payload. The local approval requested here authorizes implementing and testing that procedure only. A live packet will be presented after the complete local readiness gate passes.

## Exact local files, interfaces and exclusions

Only three new files under backend evidence/APP-013/p08-connected-packet-20261110/:

- vm2_metadata_read.py: exact operator orchestration; default disabled without a separately committed exact live decision.
- test_vm2_metadata_read.py: focused synthetic tests through the actual orchestration boundary.
- vm2-source-manifest.json: exact source/dependency hashes for this isolated procedure.

Governance completion/readiness evidence and canonical pointer/board/handoff may record the result. Existing runtime sources and their manifests are not changed; no new application route, payment flow, authentication mode, SDK allowlist expansion or broad transport is added. If implementation needs additional runtime files or permissions, stop and present the concrete gap before changing them.

Reuse q.cli_contract descriptors selected by IDs owner and project (indices0 and2), validate_cli_descriptor, strict SDK child environment, NativeIO owned-process lifecycle and validate_recovery_project. Reuse access_check.config_snapshot/read_cached_token/http_deadline. Reuse sq1.strict_json, NoRedirect and classify_sign_response only for non-2xx. The Secret Manager request is an explicitly isolated exact-URI composition; the existing SQ1 host allowlist stays unchanged. No role/identity/key/secret change, retry, SQL, token-export command, sign-in, browser, payment, deployment, support contact or spending is included in local preparation.

## End-to-end boundaries and finite checklist

1. Before coding, run governance frozen-baseline/complete consistency and backend governance wrapper; preserve owner AGENTS.md and prior renewal evidence.
2. Bind exact owner debynyhan@signmons.com, project signmons, existing canonical project-number digest37d4aa0f46ca5b8f0b81b1148bda235a0f4a9a424b6b4638ec993d889563be54, source/config/SDK pins and one operation ID. Use the existing canonical-JSON project hashing rule, not a reconstructed raw-string digest.
3. Implement exclusive one-attempt custody and committed scope/decision checks. Proposed future ceilings are2CLI,1readonly credential-cache read,1HTTPSGET,0SQL and0mutations. Reserve before dispatch. Existing SDK internal refresh/retry/cache behavior remains a separately reviewed live exception; direct logical counts are not network totals.
4. Owner/project responses must match existing validators. Cache read uses clean parent environment and requires expiry strictly beyond independent closeout. Tokens and numeric project identity stay in memory. No credential read occurs during local preparation.
5. Exact prospective request is GET https://secretmanager.googleapis.com/v1/projects/<verified-number>/secrets/signmons-staging-p07-payment-database-url/versions/1?fields=name,state. No :access, redirects, retries, proxy override, alternative resource or second read. Bound to8seconds and65536responsebytes using existing deadline and strict parsing rules.
6. HTTP200 requires exactly name/state and exact numeric resource equality; retain only a finite ENABLED/DISABLED/DESTROYED/UNKNOWN classification and match flags. For non2xx, reuse SQ1's safe numeric HTTP/status/allowlisted ErrorInfo reason/domain/equality flags; never retain error messages, raw details, resource number, token or body. Unknown fields/reasons stay UNKNOWN. NOT_FOUND is provider-reported, not independent proof of absence. An observation would be current evidence, never reconstruction of R57's discarded stderr.
7. Independently close/reap only owned processes, close responses on every path, compare nonsecret configuration, discard private memory and remove only owned temporary inputs. Safe immutable attempt/result/classification/cleanup receipts remain. Interruption, malformed output, timeout, source/config drift, conflicting operation or incomplete closure must refuse successful completion without replay.
8. Run the focused tests, existing relevant cache/error-projection regressions, source-manifest checks, architecture/governance checks and whitespace checks. Publish exact commands/results and unresolved facts. No live launch or schedule follows automatically.

## Tests and observable finish

Positive tests: matching owner/project; exact version metadata for each finite state; safe401/403/404/429/5xx error projection including allowed permission/service reasons. Negative tests: foreign identity/resource, missing/null/wrong-type fields, duplicate keys, invalidUTF8/nonfinite/deepJSON, oversized/partial output, redirect, unsafe token/environment, expired/equal-horizon cache, changed source/config, absent/mismatched approval and scope. Concurrency/recovery: exclusive attempt replay refusal, bounded one dispatch, owned-process closure, socket timeout, interruption before/after reservation, response-close failure, independent closeout after main failure and private-value exclusion. Use synthetic input and injected CLI/cache/opener boundaries only; test the same procedure later used for live qualification. Browser tests are not applicable: this procedure has no browser interface.

Commands after local approval: pinned Python -I -B unittest discovery for test_vm2_metadata_read.py; applicable existing test_access_check.py and test_sq1_signing_boundary.py; backend architecture/governance wrapper; governance frozen-baseline/complete consistency and25 governance tests; git diff --check in both repos. Record actual counts rather than preclaiming results.

Rollback/disabled state: new isolated files are unused by the connected runner; no live scope/decision is created by local approval. Remove only these unadopted files if abandoned; preserve immutable failed-attempt evidence and unrelated user changes. The implementer owns local implementation/tests/readiness. Owner approves this bounded scope; cloud/credential custodian retains any later exact external read decision.

Observable local finish is a source-pinned tested diagnostic procedure, current complete readiness record, and one precise live qualification proposal—or a concrete local blocker. Current provider cause/state/access remains UNKNOWN. TR30's existing coverage and attendance are recorded facts, not authorization for this new read; do not request another sign-in merely to implement local code.

## Readiness at proposal time and owner decision

At the timestamp recorded in the source-review JSON on November24, inspected source pins are recorded in APP013_P08_VM2_LOCAL_SOURCE_REVIEW_20261124.json. Existing metadata API contract confirms metadata-only GET and secretmanager.versions.get permission: https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets.versions/get. Actual transport seams and safe-error restrictions were reviewed independently; existing synthetic coverage was inspected, not newly run. R57 cleanup and private purge are verified;25governance tests, architecture, baseline/consistency and whitespace passed for closeout. The new exact composition has not been implemented or tested, so this card is **local-preparation approval only**, never execution-ready. Final local readiness is a blocking prerequisite to any live approval request.

Owner decision requested: approve VM2 local operator preparation and focused tests within these exact files and exclusions. No external actions, credential reads or deadline are included. Scope-deviation proposal: add this finite isolated diagnostic preparation for the demonstrated R57 observability gap. No protected acceptance criterion, dependency order, section count or denominator changes; accepted1A/1B/2A/2B remain4/8,3A OPEN,R1newlyclosed0/27. No deviation has been implemented.
