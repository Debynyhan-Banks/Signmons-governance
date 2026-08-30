# Pricing and Fees Policy

Purpose: define the public commercial model and governance constraints for high-ticket pricing.

## Public Plan Ladder (Target)

| Tier | Monthly Price | Best For | Included Volume | Setup Fee |
| --- | --- | --- | --- | --- |
| Starter | `$299/mo` | Solo owner-operator | `100` AI-handled calls/mo | `$499` |
| Growth | `$799/mo` | `2-5` trucks | `500` AI-handled calls/mo | `$1,000` |
| Pro | `$1,499/mo` | `5-15` trucks | `1,500` AI-handled calls/mo | `$2,500` |
| Enterprise | `from $3,500/mo` | Multi-location / franchise | custom | custom (`$5,000+` baseline) |

## Founding Partner Program (Non-Public-Ladder Bridge)

| Program | Monthly Price | Included Volume | Setup Fee | Limit |
| --- | --- | --- | --- | --- |
| Founding Partner | `$199/mo` | `100` AI-handled calls/mo | `$299` | first `10` approved external businesses |

Rules:

- This is a time- and capacity-limited early-access program, not a replacement public tier.
- It is implemented as a versioned Starter contract override, not a new public `PricingPlan.planId`.
- Founding price is locked for `12` months while the account remains active.
- Accounts remain month-to-month unless a separate signed agreement says otherwise.
- Planned features are not billable until enabled for the tenant.
- Conversion to a public plan requires advance notice and affirmative customer acceptance.

## Annual Pricing Policy

- Annual plans target `15%-20%` effective discount vs monthly.
- Annual policy values must be versioned in governed pricing contracts.

## Add-On Pricing Policy (Baseline)

| Add-On | Price |
| --- | --- |
| Starter AI-call overage | `$1.50` per qualifying call |
| Growth AI-call overage | `$1.00` per qualifying call |
| Pro AI-call overage | `$0.75` per qualifying call |
| Premium AI voice profile | `$149/mo` |
| Advanced missed-call recovery campaigns | `$199/mo` |
| Advanced after-hours emergency escalation | `$299/mo` |
| Additional `5` technician seats | `$149/mo` |
| Extra service area / location | `$199/mo` |
| Custom brand voice tuning | `$500` one-time |
| Custom call-flow buildout | `$1,000-$3,000` one-time |
| CRM/FSM integration setup | `$1,500-$5,000` one-time |

The earlier `$99` per `250` calls overage is retired as a target because it was not supported by measured voice/AI unit economics.

## Usage and Unit-Economics Guardrails

- An AI-handled call is billable only when it meets the governed qualifying-call definition; spam, silent calls, blocked calls, and failed test calls are excluded.
- SMS carrier/registration charges and optional telephony numbers must be disclosed separately or included through an explicit allowance.
- Before general availability, measured telephony, transcription, model, messaging, support, and payment-provider cost must be recorded by plan.
- Target direct provider cost is no more than `25%-30%` of usage revenue at normal volume.
- Any lower promotional overage requires a time-limited, versioned contract.

## Professional Invoice and Payment Fee Policy

- Basic professional estimates, invoices, payment links, and receipts are included in every paid public plan after the Signmons Money release gate.
- Signmons does not charge a basic per-invoice platform fee.
- Payment processor, ACH, dispute, financing, instant-payout, and optional third-party invoicing fees are disclosed and passed through under the tenant contract.
- Signmons must not add a payment-volume platform fee at initial launch.
- A future payment-volume fee requires Stripe Connect or an equivalent approved platform model, demonstrated reconciliation/support value, updated contracts, and explicit tenant acceptance.
- Contractor-to-customer invoices and Signmons SaaS invoices use separate numbering, policies, permissions, and ledgers.

## Performance Fee Policy (Baseline Ranges)

| Fee Type | Baseline Range |
| --- | --- |
| Qualified booked job fee | `$10-$25` per job |
| Emergency captured job fee | `$50-$100` per emergency job |
| Optional revenue-share model | `3%-8%` of recovered revenue |

Rules:

- Performance fees require enabled `PerformanceFeePolicy` on tenant contract.
- Performance fees are disabled by default at launch.
- Billable items must be derived from backend billable events only.
- Production enablement requires auditable attribution, tenant acceptance, dispute workflow, and credit/void handling.
- Plan pages may show ranges; invoice values use tenant policy values.

## Pricing Formula Disclosure (Required)

Every pricing implementation must support this formula:

`Monthly Total = Base Subscription + Overage + Enabled Performance Fees + Add-ons + Disclosed Pass-Through Provider Fees`

## Enforcement Rules

- Public pricing copy must match governed contracts in `DATA_CONTRACTS.md`.
- Any change to price points, setup fees, overage rates/blocks, or fee ranges requires:
  - docs update (this file + contract references),
  - analyzer/check update where applicable,
  - change log evidence in ticket artifacts.
