# Pricing and Fees Policy

Purpose: define the public commercial model and governance constraints for high-ticket pricing.

## Public Plan Ladder (Target)

| Tier | Monthly Price | Best For | Locations / Technicians | Fair-Use Call Capacity |
| --- | --- | --- | --- | --- |
| Starter | `$299/mo` | Solo owner-operator | `1` location / up to `2` technicians | approximately `100` AI-handled calls/mo |
| Growth | `$799/mo` | `2-5` trucks | `1` location / up to `5` technicians | approximately `500` AI-handled calls/mo |
| Pro | `$1,499/mo` | `5-15` trucks | up to `3` locations / `15` technicians | approximately `1,500` AI-handled calls/mo |
| Enterprise | fixed custom subscription | Multi-location / franchise | contracted | contracted |

## Founding Partner Program (Non-Public-Ladder Bridge)

| Program | Monthly Price | Fair-Use Call Capacity | Limit |
| --- | --- | --- | --- |
| Founding Partner | `$199/mo` | approximately `100` AI-handled calls/mo | first `10` approved external businesses |

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

## Subscription-Only Policy

- The MVP has no setup fee, metered per-call overage, booked-job fee, emergency-capture fee, revenue share, or required separately priced add-on.
- Normal Twilio phone/SMS, AI, and messaging usage is included within the selected plan's fair-use capacity.
- Capacity is a plan-suitability and cost-monitoring guide, not a unit-price multiplier.
- Approaching capacity produces an operator-visible warning and plan review. Sustained excess usage leads to an agreed fixed-price tier upgrade or Enterprise subscription, never an automatic surprise charge.
- Spam, silent calls, blocked traffic, duplicates, and approved tests are excluded from operational usage measurements.
- Before general availability, telephony, transcription, model, messaging, and support costs must be measured by plan so subscription margins remain viable.
- Feature differences belong in the governed tier package. The MVP does not use separately priced add-ons to recreate a complex fee model.

## Professional Invoice and Payment Fee Policy

- A basic Stripe payment-before-booking gate is included in every paid public plan after the Signmons Money release gate. When a contractor policy requires a booking fee or deposit, booking/dispatch readiness remains fail-closed until verified payment succeeds.
- Growth and higher tiers may add configurable deposit rules, service-fee preauthorization, partial-payment policy, exception approvals, and advanced payment recovery controls; the basic enforcement gate is not withheld from Starter.
- Basic professional estimates, invoices, payment links, and receipts are included in every paid public plan after the Signmons Money release gate.
- Signmons does not charge a basic per-invoice platform fee.
- Payment processor, ACH, dispute, financing, and instant-payout costs belong to the contractor-to-customer payment relationship and are not Signmons subscription or performance fees.
- Signmons must not add a payment-volume platform fee at initial launch.
- A payment-volume platform fee is outside the approved subscription-only commercial model and requires a new owner-approved commercial decision before it may be scoped.
- Contractor-to-customer invoices and Signmons SaaS invoices use separate numbering, policies, permissions, and ledgers.

## Prohibited Signmons MVP Charges

Signmons does not charge a tenant for:

- a qualified or confirmed booking,
- capturing or escalating an emergency,
- a percentage of recovered or contractor revenue,
- an individual AI-handled call,
- basic estimate, invoice, payment-link, or receipt creation,
- normal setup or activation,
- a core MVP capability represented as a required add-on.

## Pricing Formula Disclosure (Required)

Every pricing implementation must support this formula:

`Signmons subscription total = fixed selected-plan subscription` (plus applicable taxes only).

## Enforcement Rules

- Public pricing copy must match governed contracts in `DATA_CONTRACTS.md`.
- Any change to price points, plan capacities, or tier boundaries requires:
  - docs update (this file + contract references),
  - analyzer/check update where applicable,
  - change log evidence in ticket artifacts.
