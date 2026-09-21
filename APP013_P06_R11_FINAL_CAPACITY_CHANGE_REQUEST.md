# APP-013 / P06 R11 final controlled-acceptance capacity change request

Status: alternative 1 owner-approved on 2026-09-21; one capacity-qualified packet may be prepared for the owner-selected 6:45–7:15 PM Eastern window. Live execution remains separately approval-gated.

The consumed combined read-only operation `be1d1e7a-6ba5-4634-abee-95267fdb1398` returned `READY_FOR_PACKET`: five valid retained phone holds total 2500000 micros with inactive approval and zero invalid rows, while address account and tenant each retain two valid operations / 200000 micros with zero invalid rows. Current signed-in Safari readback shows one Verify service protected by Fraud Guard, United States as the only monitored SMS destination, Voice disabled and one unchanged verified recipient. Backend `b01673b` binds the attended coordinator to the exact approved phone and address limits and fails closed on mismatch; 13 focused tests and governance checks pass. One packet may be created only inside the approved window after current Cloud safety readback. No packet, helper, action authorization, LOGIN, activation, deployment, provider request, customer action or live execution exists at this checkpoint.

## Demonstrated gap

Read-only operation `98a32610-b621-4f1c-b92c-15e08b26b9ee` returned `ACCOUNT_AND_TENANT_LIMIT_EXCEEDED` at `2026-09-21T21:30:20.489Z`: the fixed address account and tenant each contain two valid retained operations totaling 200000 micros, exactly matching enabled19's two-operation/200000-micro limits. Invalid rows are zero. The fixed enabled19 request consequently has no address alias and did not call Google or reach the job-write transaction.

Each address operation reserves 100000 micros. The protected journey can require an initial validation and one customer-reviewed correction. Preserving both existing holds requires account and tenant capacity of four operations/400000 micros for one future packet; the session remains bounded to two operations/200000 micros. The phone policy is independent. Enabled19 completed phone verification after the last four-hold/2000000-micro refresh, so a future preparation must refresh phone liability and must not assume the consumed 2500000-micro ceiling still has room.

## Alternatives

### Alternative 1 — one final capacity-qualified R11 packet (recommended)

Preserve every phone and address hold. Authorize exactly one future R11 packet to use:

- phone flow upper bound 500000 micros and phone account ceiling 3000000 micros, only if a fresh read-only combined qualification finds valid retained phone liability no greater than 2500000 micros;
- address cost 100000 micros, account and tenant ceilings four operations/400000 micros, and session ceiling unchanged at two operations/200000 micros, only if fresh qualification matches the demonstrated two valid operations/200000 micros;
- one owner-selected support window, one connected browser journey and no automatic retry, subject to fresh packet review and separate exact execution approval.

Impact: application-recorded maximum phone liability can rise from USD 2.50 to USD 3.00 and controlled address liability from USD 0.20 to USD 0.40. Prior separate local Google holds remain visible and are not treated as database rows. These are retained-liability admission ceilings, not provider billing hard caps or settlement. The change permits capacity; it does not release holds, call a provider, create a job or authorize live execution.

This alternative also authorizes a future owner-selected window's read-only preparation to refresh provider/target/policy/participant eligibility and both phone/address liabilities in one pass, then prepare one packet only if all exact bounds match. The owner still reviews that packet and separately approves execution. This removes another capacity-only approval loop while preserving live-action separation.

### Alternative 2 — reconcile holds before another run

Keep all current ceilings. Design and approve append-only settlement based on authoritative provider/billing evidence, then count only safely reconciled liabilities. This requires a separate implementation/test card and separately approved database/provider reads and writes. No hold may be deleted, reset or silently excluded.

### Alternative 3 — stop R11 live acceptance

Keep current limits and holds unchanged. Do not prepare another R11 packet. P06 remains 12/14 with R11 and full R12 open.

## Decision boundary

Alternative 1 is the smallest route that preserves all liability and gives one future journey enough address capacity for the already-demonstrated correction path. Approval authorizes only the stated one-packet policy and future combined read-only preparation after the owner selects a window. It does not authorize database LOGIN/mutation, activation, deployment, traffic change, provider request, verification code, browser/customer action, hold release, secret/IAM change, billing change or execution.

No acceptance criterion, section count or dependency changes. P06 remains 12/14 with R11/full R12 open. No scope deviation is implemented until the owner decides.
