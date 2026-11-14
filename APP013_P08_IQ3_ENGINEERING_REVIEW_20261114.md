# APP-013 / 3A — IQ3 local engineering review

Owner authorized local engineering review after IQ3; current proceed continues that review only. Backend baseline ccc33da, runtime512c584; governance125cb0e. No runtime edits, credential/provider account reads, new operation, sign-in or mutation. Public Google documentation was consulted.

## Findings

1. Actual IQ1 commands derive enable/disable vectors from the existing restore adapter. Mutation matching is exact before JSON acknowledgement handling. Installed SDK enable.yaml dispatches iam.projects.serviceAccounts.enable; generated client uses POST v1/{+name}:enable and Empty response. Describe.Run calls projects_serviceAccounts.Get for the named account. There is no inspected command reversal.
2. SDK EnableIamAccountConfirmation discards the Empty response and emits a status message. Existing Cloud.cloud accepts empty/[] only for the exact identity mutation. This is acknowledgement, not disabled-state proof; the subsequent actual RuntimeAdapter.readback supplies that proof.
3. IQ3 STATE_MISMATCH differs from IQ1 DISABLED_MISSING. Local inert calls through the actual RuntimeAdapter.readback reproduce STATE_MISMATCH for disabled=true or numeric1 when enabled is expected; false/numeric0 pass; null/stringtrue classify INVALID. Thus retained IQ3 classification supports an opposite accepted state, but does not distinguish raw boolean from numeric encoding. No raw response is retained, and none is reconstructed.
4. run_worker invokes coordinate synchronously; coordinator calls driver.step(4) before returning or throwing. Only its finally path closes main processes and then calls driver.cleanup. The independent cleanup cannot explain the main observation by running first in this inspected program. Source inspection does not exclude another external actor; IQ3 owner confirmed no overlapping Signmons operation.
5. Prior installed-SDK formatter probe preserved true/false/null/missing for both projections. No discovered formatting fix is justified. Existing tests and unchanged safe evidence do not prove provider read consistency.
6. Official enable/disable documentation does not establish a delay explaining this event. Creation visibility or IAM-policy propagation guidance is not evidence for this existing account transition. Do not insert an arbitrary wait, retry or success waiver. Generated enable documentation also distinguishes accounts disabled by other means; there is no evidence that this happened here.

Sources: backend iq1_identity_boundary.py (commands, Cloud, Boundary.step, run_worker, coordinator), native entry.py RuntimeAdapter.readback, bound restore.NativeAdapter.change, immutable iq3-live-20261114; installed SDK surface/iam/service_accounts/{enable.yaml,describe.py}, command_lib/iam/hooks.py and generated_clients/apis/iam/v1/iam_v1_client.py. Inert readback probe:6 cases, no transport/provider invocation. SDK source and actual adapter were read, not replaced by a reconstructed fixture implementation.

Public references checked November14:
- https://docs.cloud.google.com/iam/docs/service-accounts-disable-enable
- https://docs.cloud.google.com/iam/docs/audit-logging
Google documents EnableServiceAccount and DisableServiceAccount as Admin Activity methods. These provide a potentially discriminating historical evidence source, not a promise that logs identify this cause.

## Smallest next evidence proposal — not execution authority

Review existing Admin Activity records for only project signmons, exact runtime identity, and IQ3's22:30:00Z–22:32:00Z interval on November14 (5:30–5:32 p.m. Eastern). Include only EnableServiceAccount and DisableServiceAccount methods; inspect method/time, provider status, exact resource match and expected-versus-other principal classification. Do not retrieve request/response bodies, credentials, IP addresses or unrelated project history. Resource names can use email or numeric UID: resolve against existing exact-UID binding rather than guess a filter that silently excludes numeric names.

Question: did the provider record the enable and cleanup disable successfully for the intended identity, and was there an intervening operation? Successful calls alone do not prove the readback was current. No entries, truncated results, unavailable permission, unexpected identity representation or ambiguous ordering must remain UNKNOWN; they do not prove no action occurred. Current receipts lack per-call timestamps, so audit ordering alone may not establish whether an additional write preceded the readback.

Before any external read, the implementer must prepare the exact finite command/filter, safe output projection, pagination/output bound, credential exception, source/configuration pins, deadline, process closure and retention record through the existing owned transport. Current review does not authorize adding a logging runner or broadening an existing allowlist. No new identity mutation or repeat qualification is justified by this review. Account restoration remains last-confirmed disabled; R47 historical flags are unchanged.

Completed: local command/SDK/ordering/classifier review. Blocker: actual provider transition cause UNKNOWN. Responsible owner: implementer prepares the bounded read-only observation; cloud/credential custodian authorizes access. Next observable result: exact audit-read proposal capable of distinguishing provider failure/intervening activity, or an explicit access/interface blocker. No attendance/password needed during preparation.

Unchanged remaining3A: identity prerequisite; current account containment/entry; authenticated same-job Sandbox payment/event/application failure recovery; independent cleanup; owner acceptance. Accepted1A/1B/2A/2B remain4/8;3A OPEN;R1 newly closed0/27. No scope deviation.
