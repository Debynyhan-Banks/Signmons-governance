# APP-013 / P06 R11 supervised browser test

Status: the owner-approved one-command attended coordinator is locally complete at backend `26404ff`. Four existing holds remain preserved; exactly one future packet may bind a 500,000-micro flow to a 2,500,000-micro ceiling, but no packet or live action is authorized or has occurred under that policy. Earlier live attempts remain closed and consumed. R11 remains unaccepted; P06 remains 12/14.

## Requirement traceability

- Approved section: P06-R11, controlled acceptance execution.
- Frozen criterion: in one protected journey, the participant verifies phone access, confirms an eligible Cuyahoga address and explicitly submits the reviewed request. The authoritative result must correlate the actual journey and create exactly one job or return a truthful refusal. No automatic resend or retry beyond the exact packet.
- Missing behavior: R10 reached `READY_FOR_R11`, but the owner ran only Terminal commands and never opened the browser page. Three GET deployment probes and no POST requests do not establish a participant journey.
- Customer workflow advanced: this is the first live proof that the protected browser flow can move verified participant input through current phone, address, coverage and tenant policy checks into one job without granting payment, booking, dispatch or delivery authority.
- Sources inspected: backend `c4f8ab7`; governance `b55dd9f`; `GLOBAL_EXECUTION_POINTER.md`; `SESSION_HANDOFF.md`; `TICKETS/APP-013.md`; `APP013_REMAINING_EXECUTION_CONTRACT.md`; this baseline; `DATA_CONTRACTS.md`; backend `customer-intake-page.ts`, `customer-intake-journey.html/js`, controlled result/submission services, R10 controller and September 21 result/closeout evidence.

## Existing components to reuse

- Existing private participant binding and hidden-input handling. The phone, verification code, address and customer text stay out of chat, repository evidence and ordinary logs.
- Existing controlled page at the exact origin returned by a future `READY_FOR_R11` result, its same-origin customer-session transport and its explicit review/submit controls.
- Existing finite phone/address/provider caps, one-use controller reservations, zero-traffic enabled revision and mandatory R12 closeout.
- Existing browser result projection: `ADMITTED` returns a request reference, job reference and recorded job state; `REFUSED`, `CORRECTION_REQUIRED` and `UNCERTAIN` cannot claim job creation.

No new application code, interface, schema, dependency, secret, IAM role, provider configuration or provisioning is requested.

## Future preparation and approval sequence

1. The owner selects one new future attended 30-minute Eastern window.
2. The owner separately authorizes read-only provider/target/eligibility refresh and fresh packet preparation for that window. This step may not open LOGIN, activate, deploy, call a provider, issue a code or execute the journey.
3. Review the resulting exact packet, revision, digests, current policies, participant eligibility, finite request/cost caps, run window and closeout deadline.
4. The owner separately approves or refuses that exact plan. Only exact approval may authorize its named guarded helper installation, one-command attended coordinator, bounded database LOGIN, activation, zero-traffic deployment, provider requests, browser journey and closeout.
5. After exact approval, the owner runs one reviewed coordinator command. It waits locally, prompts once, performs the exact at-most-once controller sequence, displays the URL, waits for local `DONE`/`STOP` and performs mandatory closeout. A stopped, uncertain, elapsed or consumed operation is never rerun.

Selecting a window alone grants no live authority.

## Supervised R11 browser sequence

After the approved coordinator prints `R10_ACTIVE_READY` with the exact HTTPS `/customer-intake` URL, the owner manually opens it in an already-visible normal browser. The implementer must not create or navigate a task-controlled browser tab and must not click, type or submit in the live page. No intermediate chat marker is required; the owner completes this sequence without placing private values in chat:

1. Open the exact returned URL and select **Start a new request**.
2. Enter the service issue and continue. Skip optional email and appointment-text enrollment unless the reviewed packet expressly includes them; neither is required for P06.
3. Enter the reviewed customer details and the privately bound phone number.
4. Select **Review code request**, confirm the displayed number, request one verification code and enter that code once. Do not resend or restart to bypass a limit.
5. Enter the privately retained, customer-confirmed standardized Cuyahoga service address, including its ZIP+4, from the beginning. Review any displayed correction field by field. A second address request or corrected submit is allowed only when the exact packet permits it.
6. Complete the issue category, property type, service intent and issue summary. Check **I reviewed these details**, then select **Preview validated draft**.
7. Read the complete preview. If correct, select **Confirm details and submit request** exactly once.
8. Report only the final non-private status and displayed request/job references. Do not report the phone, code, address, name or issue narrative.
9. Return to Terminal and type `DONE` after a terminal browser result or `STOP` after any error. The same coordinator performs mandatory closeout. Report the final non-private browser status/references and final coordinator line once. Do not run a separate closeout, clear, reset or retry an uncertain operation before reconciliation.

## Result classification

- R11 success: the page displays **Job created — this receipt does not confirm a booking**, plus one request reference, one job reference and a recorded job state; correlated server evidence confirms exactly one job for the request.
- Truthful refusal: the page displays **No job created** and retains fields for review. Record the sanitized reason/status; R11 is not accepted and no rerun is implied.
- Correction required: review and correct only within the exact packet's remaining caps. If no permitted correction remains, stop and close out.
- Uncertain: the page displays **Outcome unconfirmed** with the same request reference. Do not start another request or use the UI retry unless the exact approved packet explicitly permits that same-request recovery. Preserve the hold for reconciliation.
- Any expired, unavailable, malformed or unexpected response: stop, close out and record the safe stage. It is not acceptance.

## Data, identity, state and retention boundaries

- Identity and consent are limited to the currently verified, owner-controlled participant and exact private binding qualified in the future packet.
- Raw phone, code, address, name, narrative, credentials and bearer/session values remain only in the attended private interfaces. Evidence stores opaque IDs, digests, stages, counts and permitted references.
- Browser state is private and short-lived. Closing the session purges permitted verification material while retaining authoritative job/audit records and any unknown cost hold required for reconciliation.
- A created job grants no payment, booking, dispatch or message-delivery authority. The enabled revision remains at zero normal traffic throughout.
- Full R12 requires approval revocation, tag removal, runtime NOLOGIN/limit zero/sessions zero, baseline traffic readback, browser/session cleanup, retention review, provider/database billing reconciliation and owner acceptance.

## Finite checklist and evidence

- Before action: current governance and source SHAs; clean/expected worktree state; exact owner-approved plan; current provider/target/policy/participant readbacks; packet and runtime digests; request/cost caps; closeout deadline; disabled baseline; no stale authorization.
- Positive evidence: `READY_FOR_R11`; exact opened origin; sanitized browser terminal status; request/job references; correlated one-job readback; approval/revision/provider audit references; closeout and independent baseline readbacks.
- Negative evidence: no payment, booking, dispatch or delivery authority; no normal traffic; no duplicate job; no extra verification/address request; no secret or private input in evidence.
- Concurrency: the existing one-use reservations, approval/revision comparison and job uniqueness must reject duplicate or stale execution; do not manufacture a concurrent live attempt.
- Recovery: stop on refusal, uncertainty, expiry or unexpected stage; execute mandatory closeout; retain unknown holds and assign reconciliation; no automatic retry.
- Browser checks: exact controlled page loads over HTTPS; controls follow the sequence above; final status matches its receipt; private storage clears on close; no claim beyond the displayed and correlated evidence.

Post-run checks must include the governance frozen-baseline and consistency gates, backend governance/architecture gates, both whitespace checks and the exact packet's database/browser/closeout validations. Historical synthetic browser suites may support implementation confidence but cannot satisfy R11.

## Observable finish

R11 closes only with one successfully correlated live protected journey and exactly one job. Full R12 and P06 close only after mandatory shutdown, retention/billing reconciliation and explicit owner acceptance. Until then P06 remains 12/14, R11 and full R12 remain open, and the service stays inactive with normal traffic on the baseline revision.

No scope deviation.
