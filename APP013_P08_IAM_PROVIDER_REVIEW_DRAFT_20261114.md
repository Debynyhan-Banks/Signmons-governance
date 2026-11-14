# APP-013 / 3A — IAM state-transition review handoff

DRAFT ONLY — not sent, no support case created, no paid support or new provider operation authorized. Prepared from retained IQ3/AL1 evidence under the owner-requested engineering review. Backend80edf70; governancea184277. No runtime correction is established.

## Suggested case text

Subject: Service account enable acknowledged, immediate Get reports disabled; request consistency guidance

Project: signmons. Service account: signmons-calldesk-p07-runtime@signmons.iam.gserviceaccount.com. Please investigate IAM state visibility for this existing identity. We verified the same identity by its numeric UID hash before/after the operation; the raw UID was not retained in this report.

On November14,2026, our bounded operation started with the account disabled, issued one gcloud iam service-accounts enable, received a successful CLI acknowledgement, then performed a single gcloud iam service-accounts describe with --format=json(email,disabled). The readback classified the state as opposite to the required enabled state. The classifier rejects missing/null/string fields separately; this was RUNTIME_IDENTITY_STATE_MISMATCH. It accepts boolean/numeric equality, so retained classification alone cannot distinguish disabled:true from numeric1. Raw response was discarded under the approved retention policy.

Independent cleanup then issued one disable, verified disabled state and matching identity, and closed successfully. No token issuance, application authentication or payment occurred. No mutation retry or polling was performed.

A separately authorized historical Admin Activity query returned exactly these matching events, both attributed to the expected owner:
- 2026-11-14T22:30:48.718738427Z: google.iam.admin.v1.EnableServiceAccount
- 2026-11-14T22:30:51.265846694Z: google.iam.admin.v1.DisableServiceAccount

No explicit status.code was projected for either event. No additional matching enable/disable event appeared in the exact two-minute interval. This does not establish that all possible external activity was absent. Individual readback request timestamps/IDs were not retained. The approximately2.547-second difference is between audit event timestamps, not a measured enable-to-Get latency.

Our installed SDK dispatches enable to POST v1/{name}:enable and describe to projects.serviceAccounts.Get. Enable's response type is Empty; the CLI confirmation hook discards that response, so we independently check state. The local procedure runs the readback before cleanup; we found no reversed command or concurrent cleanup within that procedure. A local formatter probe preserves boolean/null/missing fields. These checks do not establish the provider response was current.

Questions:
1. What consistency guarantee applies to ServiceAccounts.Get immediately after EnableServiceAccount returns for an existing account? Can disabled remain true temporarily, and is there a documented bound or recommended observation procedure?
2. Can the two audit events be correlated with a server-side outcome or intervening/system state change? What additional minimal identifiers are necessary? Please do not request passwords, tokens or service-account private keys.
3. If reproduction is necessary, what minimal safe fields and request timings would distinguish provider visibility from client serialization or another actor, without repeated mutations or broad HTTP/credential logging?

We have intentionally left the account disabled and will not weaken the state check or schedule another reproduction until we have a specific evidence plan. Any new reproduction is subject to separate owner approval.

## Evidence and decision boundary

Retained local references (not externally attached automatically): APP013_P08_IQ3_RESULT_20261114.md; APP013_P08_AL1_RESULT_20261114.md; backend iq3-live-20261114 and al1-live-20261114 safe results. IQ3 source512c584, approval7795fa9; AL1 approval101f6d3. This draft includes project/account identifiers and event timestamps; owner must review those disclosures before sending. No support entitlement or cost assumption is made.

Public documentation inspected November14:
- https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/enable — API scope/Empty response; no timing conclusion inferred.
- https://docs.cloud.google.com/iam/docs/service-accounts-create — eventual-consistency wording is about creation; not proof of this existing-account enable cause.
- https://docs.cloud.google.com/logging/docs/reference/audit/auditlog/rest/Shared.Types/AuditLog — status describes overall operation; retained projection has no explicit numeric code, so original STATUS_ABSENT evidence remains unchanged.

## Review outcome and alternatives

Completed: command/ordering/classifier review, bounded historical log read and this concrete provider-review handoff. Current evidence cannot reconstruct the discarded readback. Another identical mutation, another current-state read or re-querying the same projected audit events does not resolve that limitation. No local patch, guessed wait, polling allowance or success waiver is justified yet.

Recommended next decision: owner/cloud custodian reviews this draft for submission through the organization's existing Google Cloud support channel. Do not send it or purchase support without explicit instruction. If provider support is unavailable, the alternative is a separately scoped local proposal for minimal timestamped, safe-type/UID readback evidence followed by one separately approved discriminating reproduction; no such implementation or live action is authorized here. Any proposed observation schedule must be evidence-based and bounded before coding.

Responsible roles: implementer maintains existing disabled/closed state and evidence; owner/cloud custodian chooses provider review or a concrete instrumentation proposal. Next observable result: provider guidance or an approved finite evidence design, not another identical attempt. No new sign-in, attendance or password request.

Remaining3A: identity prerequisite; current account containment/entry including preserved R47 UNKNOWNs; authenticated same-job Sandbox event/application outcome and recovery; independent cleanup; owner acceptance. Accepted1A/1B/2A/2B remain4/8;3A OPEN;R1 newly closed0/27. No scope deviation.
