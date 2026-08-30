# Offer Catalog

Purpose: canonical summary of what each plan offers and how upgrade paths are justified.

## Product Promise

Stop sending trucks to unpaid jobs. Signmons answers, qualifies, collects payment, dispatches, updates customers, and proves recovered revenue.

## Product Modules

- **CallDesk:** phone/SMS/web intake, qualification, safety, booking, summaries, and handoff
- **Dispatch:** calendars, availability, booking readiness, routing, assignment, and confirmations
- **Money:** estimates, approvals, deposits, invoices, payment links, receipts, reminders, and refunds
- **Field:** technician jobs, notes, photos, signatures, equipment context, and status updates
- **Customers:** customer/property/equipment/service/communication history
- **Growth:** missed-call recovery, reviews, maintenance-plan renewal, and attribution
- **Intelligence:** conversion, payment, dispatch, revenue, and AI-quality reporting

Modules share one tenant-scoped operating record. They are not sold as disconnected products.

## Founding Partner Program (Limited Early Access)

- `$199/mo` + `$299` one-time guided setup
- limited to the first `10` external businesses approved for the program
- up to `100` AI-handled calls/month
- CallDesk web intake, calendar booking, owner alerts, customer/job history, and basic professional estimates/invoices as each capability is released
- month-to-month; founding price locked for `12` months while the account remains active
- early-access or planned capabilities must be labeled accurately and cannot be billed before activation
- founding accounts convert to a public plan only with advance notice and affirmative acceptance

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
- branded estimates and invoices
- customer approval, payment link, and receipt

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
- deposit and partial-payment workflows
- estimate-to-job-to-invoice conversion
- invoice reminders, credits, refunds, and payment-status reporting
- customer review requests

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
- QuickBooks Online integration; Xero follows through an approved adapter
- advanced estimate options, progress/recurring invoices, and approval workflows
- technician mobile workflow and governed pricebook
- maintenance-plan renewal workflows
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

Performance fees are disabled by default at launch. They may be enabled only after billable-event attribution, tenant contract acceptance, invoice evidence, dispute handling, and credits/voids are production-ready.

## Invoice and Payment Packaging Rules

- Basic professional estimates, invoices, payment links, and receipts are included in every paid public plan after Signmons Money is released.
- Do not charge a Signmons per-invoice fee for the basic feature.
- Processor, ACH, chargeback, financing, and optional third-party invoicing fees are disclosed and passed through according to the tenant contract.
- Signmons does not provide bookkeeping, payroll, tax filing, or general-ledger accounting.
- Advanced deposits, progress/recurring invoicing, automated reminders, pricebook controls, margin reporting, and accounting synchronization may be tiered.

## Upgrade Logic

- Founding Partner -> Starter: generally available CallDesk + Money baseline and standard support
- Starter -> Growth: payment gate + multi-tech routing + advanced invoicing + dashboard
- Growth -> Pro: scheduling/routing intelligence + field workflow + integrations + auditability
- Pro -> Enterprise: multi-location + custom policy/compliance + SLA
