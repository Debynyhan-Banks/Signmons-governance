# APP-013 / P06 R11 phone account-ceiling change request

Status: alternative 1 approved; future packet preparation remains separately gated.

The owner approved alternative 1 exactly: retain both existing holds and allow exactly one future R11 packet with `flowUpperBoundMicros: 500000` and `accountCeilingMicros: 1500000`. The decision is policy approval only. It does not authorize packet preparation, LOGIN, activation, deployment, provider request, verification code, browser/customer action, database write, hold release, secret/IAM change, billing change or live execution. The owner selected 11:15–11:45 AM Eastern on 2026-09-21 as the proposed future window; selection alone grants no preparation or execution authority.

## Demonstrated gap

Read-only operation `bd6a6f3e-6681-4c24-803b-e6ed44248511` found one valid historical staging-phone hold and one valid controlled-phone hold totaling 1,000,000 USD micros. Enabled13 bound one future phone flow at 500,000 micros under a 1,000,000-micro account ceiling. `ControlledCustomerAdmission.reserve` correctly refused because retained liability plus the new bound would be 1,500,000 micros. Packet reuse was false and invalid-row count was zero. The code request never reached durable reservation or Twilio.

R11 cannot complete under the current ceiling unless prior liabilities are reconciled through a separately designed settlement path or the owner explicitly approves a higher retained-liability ceiling. Holds must not be deleted, reset or silently excluded.

## Alternatives

### Alternative 1 — allow one future packet at a 1,500,000-micro account ceiling (recommended)

Retain both existing holds unchanged. Permit one newly prepared R11 packet to bind `flowUpperBoundMicros: 500000` and `accountCeilingMicros: 1500000`. This is a policy-input change only; existing admission code already supports it. The packet still permits one START, bounded CHECKs, no resend and no automatic retry. A stopped or consumed packet does not automatically earn another ceiling increase.

Impact: application-recorded maximum retained phone liability rises from USD 1.00 to USD 1.50. This is neither an invoice reconciliation nor a provider/account spending hard cap. All prior holds remain visible for full R12 reconciliation. A fresh packet/window, read-only provider/target/policy qualification and separate exact execution approval remain required. No code, database mutation, provider call or release occurs when this alternative is approved.

### Alternative 2 — design and implement hold settlement before another run

Do not raise the ceiling. First perform separately approved provider/billing reconciliation for both holds, specify authoritative settlement evidence, add an append-only settlement state and change admission to count only safely reconciled liability. This requires a new implementation/test card and separately approved database migration or write path. It is broader and slower, but closes the reconciliation gap before another live request.

### Alternative 3 — stop R11 live acceptance

Keep the USD 1.00 ceiling and both holds unchanged. Do not prepare another live R11 packet. P06 remains 12/14 with R11 and full R12 open.

## Recommended decision and boundaries

Alternative 1 is the smallest path to the frozen R11 criterion because it preserves every prior liability and changes only the explicit future packet ceiling. It does not weaken one-use, participant, policy, traffic, provider, job or closeout guards. The owner must approve the alternative before any packet uses the higher ceiling.

Approval of this change request alone authorizes only the stated policy direction. Packet preparation, database LOGIN or mutation, activation, deployment, traffic change, provider request, verification code, browser/customer action, secret/IAM change, billing change and live execution remain separately gated.

R11 and full R12 remain open; P06 remains 12/14. Approved policy deviation is limited to one future packet's explicit retained-liability ceiling; no implementation or live deviation occurred.
