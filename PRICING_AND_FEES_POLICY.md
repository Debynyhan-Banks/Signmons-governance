# Pricing and Fees Policy

Purpose: define the public commercial model and governance constraints for high-ticket pricing.

## Public Plan Ladder (Target)

| Tier | Monthly Price | Best For | Included Volume | Setup Fee |
| --- | --- | --- | --- | --- |
| Starter | `$299/mo` | Solo owner-operator | `100` AI-handled calls/mo | `$499` |
| Growth | `$799/mo` | `2-5` trucks | `500` AI-handled calls/mo | `$1,000` |
| Pro | `$1,499/mo` | `5-15` trucks | `1,500` AI-handled calls/mo | `$2,500` |
| Enterprise | `from $3,500/mo` | Multi-location / franchise | custom | custom (`$5,000+` baseline) |

## Annual Pricing Policy

- Annual plans target `15%-20%` effective discount vs monthly.
- Annual policy values must be versioned in governed pricing contracts.

## Add-On Pricing Policy (Baseline)

| Add-On | Price |
| --- | --- |
| Extra `250` AI-handled calls | `$99/mo` |
| Premium AI voice profile | `$149/mo` |
| Advanced missed-call recovery campaigns | `$199/mo` |
| Advanced after-hours emergency escalation | `$299/mo` |
| Additional `5` technician seats | `$149/mo` |
| Extra service area / location | `$199/mo` |
| Custom brand voice tuning | `$500` one-time |
| Custom call-flow buildout | `$1,000-$3,000` one-time |
| CRM/FSM integration setup | `$1,500-$5,000` one-time |

## Performance Fee Policy (Baseline Ranges)

| Fee Type | Baseline Range |
| --- | --- |
| Qualified booked job fee | `$10-$25` per job |
| Emergency captured job fee | `$50-$100` per emergency job |
| Optional revenue-share model | `3%-8%` of recovered revenue |

Rules:

- Performance fees require enabled `PerformanceFeePolicy` on tenant contract.
- Billable items must be derived from backend billable events only.
- Plan pages may show ranges; invoice values use tenant policy values.

## Pricing Formula Disclosure (Required)

Every pricing implementation must support this formula:

`Monthly Total = Base Subscription + Overage + Performance Fees + Add-ons`

## Enforcement Rules

- Public pricing copy must match governed contracts in `DATA_CONTRACTS.md`.
- Any change to price points, setup fees, overage blocks, or fee ranges requires:
  - docs update (this file + contract references),
  - analyzer/check update where applicable,
  - change log evidence in ticket artifacts.
