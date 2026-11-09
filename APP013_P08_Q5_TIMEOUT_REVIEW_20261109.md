# APP-013 / 3A / P08 — Q5 local timeout review

Owner “proceed i approve” authorized local diagnosis after83fda7c. Source710e774; Q5 evidence3ef767f. No live operation, credentials/cache/provider logs, SDK command or network probe executed. Only pinned source, sanitized receipt and owned synthetic child-process tests inspected.

## Findings

NativeIO.cli passes min(readDeadline,clock()+30) to _owned_run. The computed local timeout variable is unused but the actual30-second cap is enforced by the passed deadline. _owned_run reserves two seconds for _finish, applies both wall-clock and monotonic deadlines, raises PROCESS_TIMEOUT at deadline minus2, and reaps the owned group. Q5 project began15:16:40.238Z with499.762seconds remaining before15:25Z; it failed after28013ms. This matches the per-command work cap, not exhaustion of the full operation window or the hidden password prompt. _finish success is consistent with the retained PROCESS_TIMEOUT rather than PROCESS_CLEANUP_UNCONFIRMED and final verified cleanup.

Pinned SDK583.0.0 surface/projects/describe.py Run calls projects_api.Get; projects_api.py Get uses the Resource Manager client. This source trace cannot identify whether Q5 waited in authentication refresh, DNS/connect/TLS, provider response or SDK-internal retry. SDK stderr is deliberately discarded and raw responses are not retained. No lost output will be reconstructed or logs fetched. Earlier successful commands do not prove present network/service health.

Two actual local tests PASS in1.416s: SDKDiagnosticTests.test_actual_owned_timeout_identifies_label_and_closes_child and OwnedProcessTests.test_real_child_success_oversize_timeout_and_group_cleanup. They exercise owned child timeout/success/oversize/cleanup with synthetic programs, not the live SDK. Existing144runtime/local+25governance suite remains historical for unchanged source; no full runtime rerun claimed.

## Disposition and next bounded decision

Local diagnosis complete; no implementation defect established and no timeout increase, transport change, role grant or another full recovery/qualification justified by this evidence. Q4 permission cause still UNKNOWN; Q5 never reached it. Retain strict limits and consumed authorities.

Recommended next scope, if the owner chooses further external diagnosis: a separately proposed, source-bound owner/project-only SDK read with no SQL, recovered target UUID, full qualification, token print or explicit cache inspection. Existing SDK refresh/cache/internal retries would require explicit allowance. The current recovery entry requires SQL and the full qualifier requires both private bindings, so neither is an appropriate silent substitute. A safe narrower invocation/authority/receipt path must be concretely reviewed first; this document does NOT implement or authorize a new helper/entry point. Its readiness and exact time window are not yet established. Alternative: defer all external work with verified cleanup intact. Responsible owner decides diagnostic scope; implementer prepares the exact reviewable contract before any implementation or execution.

No new subsystem, user-facing section, acceptance change or provider-read authority. All Q5/R13 private material purged; guard absent; no replay. Completed local source/deadline review and focused tests. Remaining blocker external SDK stall cause, responsible owner/provider-admin; then original full permission qualification and same-job Sandbox payment/negative/replay/owner acceptance.3A OPEN; accepted1A/1B/2A/2B4/8;R1newlyclosed0/27. No scope deviation.
