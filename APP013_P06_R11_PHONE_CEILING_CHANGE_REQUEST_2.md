# APP-013 / P06 R11 second phone account-ceiling change request

Status: alternative 1 approved; packet preparation authorized separately for the current window; live execution remains unapproved.

The owner approved alternative 1 exactly: preserve all three holds and permit one newly prepared R11 packet with `flowUpperBoundMicros: 500000` and `accountCeilingMicros: 2000000`. The existing 12:45–1:30 PM Eastern read-only preparation authorization applies to that packet. This does not authorize LOGIN, database mutation, activation, deployment, traffic change, provider request, verification code, browser/customer action, hold release, secret/IAM change, billing change or live execution.

## Demonstrated gap

Owner-authorized read-only operation `27091628-3b8c-493a-ade5-1c1ede40277a` completed at `2026-09-21T16:50:53.180Z`. Its repeatable-read transaction found one valid staging-phone hold and two valid controlled-phone holds totaling 1,500,000 USD micros. Invalid-row count was zero. The current controlled approval is disabled with its exact digest after verified closeout.

The proposed fresh R11 flow requires a 500,000-micro upper bound. Retained liability plus that flow would total 2,000,000 micros, exceeding the owner-approved 1,500,000-micro packet ceiling. The preparation therefore stopped before creating a packet. No LOGIN, database write, activation, deployment, provider request, verification code, browser/customer action, hold release, secret/IAM change or billing change occurred.

## Alternatives

### Alternative 1 — allow one future packet at a 2,000,000-micro account ceiling (recommended)

Preserve all three existing holds. Permit exactly one newly prepared R11 packet to bind `flowUpperBoundMicros: 500000` and `accountCeilingMicros: 2000000`. Existing admission code already supports this policy input. The packet retains one START, bounded CHECKs, no resend and no automatic retry. A stopped or consumed packet does not automatically authorize another ceiling increase.

Impact: application-recorded maximum retained phone liability rises from USD 1.50 to USD 2.00. This is not an invoice reconciliation or provider/account spending hard cap. All holds remain visible for full R12 reconciliation. Read-only provider/target/policy qualification, a fresh packet, and exact execution approval remain separate gates.

### Alternative 2 — reconcile retained holds before another run

Do not raise the ceiling. Design and approve an append-only settlement path based on authoritative provider/billing evidence, then change admission to count only safely reconciled liability. This requires a separate implementation/test card and separately approved database write or migration. No hold may be deleted, reset or silently excluded.

### Alternative 3 — stop R11 live acceptance

Keep the 1,500,000-micro ceiling and all holds unchanged. Do not prepare another live R11 packet. P06 remains 12/14 with R11 and full R12 open.

## Decision boundary

Alternative 1 is the smallest path to the frozen R11 criterion while preserving all recorded liability. Approval of this change request authorizes only the stated policy direction. Packet preparation, LOGIN, database mutation, activation, deployment, traffic change, provider request, verification code, browser/customer action, hold release, secret/IAM change, billing change and live execution remain separately gated.

P06 remains 12/14 with R11 and full R12 open. Approved policy deviation is limited to one future packet's explicit retained-liability ceiling; no live deviation has occurred.
