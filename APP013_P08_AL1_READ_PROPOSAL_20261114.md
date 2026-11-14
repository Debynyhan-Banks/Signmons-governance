# APP-013 / 3A — AL1 historical IQ3 audit read

Prepared, not authorized. Operation5bbe2947-783c-4f04-adf3-380151414d11. Owner authorized preparation after IQ3 engineering review. Exact commands, filter template, resource UID hash, source/configuration pins and output projection are in APP013_P08_AL1_READINESS_20261114.json. No runtime changes or new executable. This is a read-only diagnostic, not another identity qualification or payment attempt.

Question: what enable/disable Admin Activity does Google retain for IQ3's exact runtime identity during November14,22:30:00Z inclusive to22:32:00Z exclusive (5:30–5:32 p.m. Eastern)? Look for provider error and additional/intervening operations. Logs cannot by themselves prove read consistency, present identity state or the timing of IQ3's un-timestamped individual readback.

## Exact operation

Maximum4 SDK CLI invocations: existing owner check, project check, exact identity metadata, one logging read. Use pinned IQ1 source512c584 and existing qualification NativeIO owned transport directly under this decision; do not pass a logging command through or broaden IQ1's command allowlist. No new runner is installed. Initial3 vectors are the existing inspected IQ1 descriptors. Match owner debynyhan@signmons.com/projectsignmons through existing validators. Match identity email signmons-calldesk-p07-runtime@signmons.iam.gserviceaccount.com and numeric UID hash3d299bbf03a6c3e2315034fb3a809aedbb6f978c6e6741ff0201fe4464798f72; require explicit disabled:true before proceeding. Any mismatch stops, with no mutation. Keep raw UID/project number transient.

Replace only <MATCHED_NUMERIC_UID> in the bound filter after that match. The filter selects project signmons Admin Activity, iam.googleapis.com, the exact historical two-minute interval, EnableServiceAccount/DisableServiceAccount and exact email-or-UID resource suffix. No principal filter: another actor's exact-resource event is relevant. Never broaden time/resource/method scope to compensate for no results. Execute logging read with --project=signmons --order=asc --limit=20 and the readiness JSON's exact projection.

Wrap each command with the same pinned sandbox-exec deny-process-fork profile, Python and SDK entrypoint. Directly supervise NativeIO._owned_run with sdk_environment and an8-second deadline per invocation; stdout cap65536 bytes, stderr discarded, no fallback. Stop after first failure; no command retry. Always close all owned processes and verify process absence, configuration/source integrity and safe inventory. Use a fresh exclusive receipt directory /private/tmp/p08-al1-5bbe2947-783c-4f04-adf3-380151414d11; do not replay IQ3 or create any identity mutation intent.

## Output and uncertainty

SDK receives matching provider records transiently; its JSON projection emits only timestamp, methodName, resourceName, status.code and principalEmail. It does not emit request/response bodies, status message, IP or unrelated payload. Local installed-SDK projection probe verified omission of synthetic private fields. This projection is not a server-side field mask.

Parse a list of at most20 records. Validate every timestamp, method, exact resource suffix and field type; unexpected shapes stop as UNKNOWN. Retain only timestamps, method label, resourceMatch boolean, principal class EXPECTED/OTHER/ABSENT, explicit numeric status code or STATUS_ABSENT, and safe counts/classification. Do not persist raw entries, resource numeric UID or other principal names. Missing status is not silently promoted to proof of success. Zero entries means NO_MATCHING_RECORDS_OBSERVED, not no operation. Exactly20 means POSSIBLY_TRUNCATED; no follow-up page/query. Other resource encodings, missing fields, transport/access failure or ambiguous order remain UNKNOWN. No live run is released on audit success alone.

## Limits and authority

Launch before5:55 p.m. Eastern November14; reads end5:58; independent local cleanup/private-data removal ends6:00, within already confirmed reachability through6:05. No Terminal/password/sign-in required. Current credential usability/logging permission/audit availability remain UNKNOWN. Permit existing-owner SDK refresh/internal authentication retries/cache maintenance plus SDK read pagination within the process deadline. --limit=20 caps returned entries and page size; it does not guarantee one underlying HTTPS request. SDK internal requests are not capped at4. No explicit cache/token export, credential renewal, new scopes, direct HTTPS, SQL, provider mutation, payment, refund, booking or customer message. Additional allowance$0 is not a hard cloud-billing cap.

Before launch compare actual command/source/configuration/time/root absence to this record and committed exact owner decision. Authorize only this read scope; do not weaken existing validators. Process or configuration uncertainty stops. Preserve safe result/closeout evidence, drop all raw output/UID/principal values by6:00; no private input file is needed, do not delete SDK cache. No automatic follow-up or mutation is authorized.

## Readiness and responsibilities

Committed existing source guard/config snapshot PASS; installed logging read/FetchLogs source confirms explicit timestamp filter, parent scope, ascending order and bounded returned count; installed SDK synthetic projection PASS. Reuse existing transport/process closure and prior unchanged-source sandbox proof, not a newly claimed runtime suite. Prepare safe classifiers through inspected expected field shapes; do not introduce new application code. Governance/architecture/whitespace checks required before review and after evidence changes. This is qualification-only: live permissions and evidence completeness are UNKNOWN.

Implementer owns one bounded read and independent closure; cloud/credential custodian owns external access approval. Requested decision: approve AL1's4 read-only CLI calls, stated SDK refresh/retry/cache/pagination exception and local cleanup before the exact cutoff. Repository AGENTS.md and existing diagnostic authority boundaries require this separate exact external approval; prior approval covered local review/preparation.

Completed: concrete read preparation. Remaining: historical observation, supported diagnosis or explicit UNKNOWN; then current identity/account entry prerequisites, authenticated same-job Sandbox payment/event/application recovery, cleanup and owner acceptance. No extra acceptance section. Accepted4/8;3A OPEN;R1 newly closed0/27;IQ3 consumed and restored, R47 history unchanged. No scope deviation.
