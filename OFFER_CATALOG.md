# Offer Catalog

Purpose: canonical summary of what each plan offers and how upgrade paths are justified.

## Product Promise

Stop sending trucks to unpaid jobs. Signmons answers, qualifies, collects payment, dispatches, updates customers, and proves recovered revenue.

## Tier Catalog

### Starter (`$299/mo`)

Best for:
- solo owner-operators

Includes:
- `100` AI-handled calls/month
- `24/7` call answering
- SMS + web chat intake
- booking-ready summaries
- payment link handoff
- basic appointment request collection
- basic lead history
- owner alerts (email/SMS)

Excludes:
- advanced dispatch and routing
- no-payment-no-dispatch enforcement
- advanced analytics and integrations

Setup fee:
- `$499` one-time

### Growth (`$799/mo`)

Best for:
- `2-5` truck teams

Includes Starter plus:
- `500` AI-handled calls/month
- missed-call recovery (basic)
- urgency classification (emergency/high-priority/standard)
- after-hours capture
- deposit collection + service-fee preauthorization
- no-payment-no-dispatch gate
- multi-tech routing (`up to 5` vehicles)
- basic dispatch board
- customer confirmations
- technician SMS notifications
- revenue recovery dashboard
- human handoff for urgent/unclear calls

Setup fee:
- `$1,000` one-time

### Pro (`$1,499/mo`)

Best for:
- `5-15` truck operations

Includes Growth plus:
- `1,500` AI-handled calls/month
- advanced dispatch rules
- calendar and scheduling board
- technician availability and skill routing
- service area routing
- brand voice + AI personality controls
- business rules and automation center
- customer profiles and service history
- transcripts and audit trail
- CRM/FSM integrations
- advanced revenue reporting
- monthly optimization review

Setup fee:
- `$2,500` one-time

### Enterprise (`from $3,500/mo`)

Best for:
- multi-location/franchise operations

Includes Pro plus:
- custom volume
- multi-location reporting
- SLA-backed operations
- white-label AI experience
- dedicated implementation
- executive business reviews
- custom integrations/data pipelines
- advanced compliance controls

Setup fee:
- custom (`$5,000+` baseline)

## Performance Fee Options

Per-tenant policy-controlled options:
- qualified booked job fee
- emergency captured job fee
- optional revenue-share model

Billable definitions and constraints:
- governed in `BILLABLE_EVENTS_SPEC.md`
- enforced by contracts in `DATA_CONTRACTS.md`

## Upgrade Logic

- Starter -> Growth: payment gate + multi-tech routing + dashboard
- Growth -> Pro: scheduling/routing intelligence + integrations + auditability
- Pro -> Enterprise: multi-location + custom policy/compliance + SLA
