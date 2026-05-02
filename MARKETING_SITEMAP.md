# Signmons Marketing Sitemap (High-Ticket)

Purpose: canonical site architecture for public marketing surfaces aligned to governance screen IDs and execution sequencing.

## Positioning

Signmons is the AI front office and dispatch intelligence system for trades businesses.

## Primary Navigation

- Product
- Solutions
- How It Works
- Pricing
- Demo
- Resources
- CTAs: `Book Demo`, `Get Revenue Audit`, `Login`

## Core Routes and Governance Mapping

### Conversion

- `/` -> `SCR-PUB-001` (Home)
- `/pricing` -> `SCR-PUB-006` (Pricing)
- `/demo` -> `SCR-PUB-007` (Demo)
- `/contact` -> `SCR-PUB-009` (Lead capture)
- `/roi-calculator` -> `SCR-PUB-016` (ROI)

### Product Education

- `/how-it-works` -> `SCR-PUB-002`
- `/ai-dispatcher` -> `SCR-PUB-003`
- `/about` -> `SCR-PUB-008`
- `/done-for-you-setup` -> `SCR-PUB-011`
- `/business-rules` -> `SCR-PUB-012`
- `/brand-voice` -> `SCR-PUB-013`
- `/dispatch-scheduling` -> `SCR-PUB-014`
- `/revenue-dashboard` -> `SCR-PUB-015`
- `/customer-technician-experience` -> `SCR-PUB-019`

### Comparison

- `/compare/answering-services` -> `SCR-PUB-017`
- `/compare/field-service-software` -> `SCR-PUB-018`
- Child SEO pages (planned):
  - `/compare/smith-ai`
  - `/compare/workiz`
  - `/compare/jobber`
  - `/compare/housecall-pro`
  - `/compare/servicetitan`

### Industry

- `/industries` -> `SCR-PUB-004` (Trades verticals hub)
- `/industries/hvac` -> child route (inherits `SCR-PUB-004`)
- `/industries/plumbing` -> child route (inherits `SCR-PUB-004`)
- `/industries/electrical` -> child route (inherits `SCR-PUB-004`)
- `/industries/drains` -> child route (inherits `SCR-PUB-004`)
- `/industries/roofing` -> child route (inherits `SCR-PUB-004`)
- `/industries/construction` -> child route (inherits `SCR-PUB-004`)
- `/industries/landscaping` -> child route (inherits `SCR-PUB-004`)
- `/industries/multi-location` -> child route (inherits `SCR-PUB-004`)

### Trust and Legal

- `/trust-safety` -> `SCR-PUB-005`
- `/privacy` -> `SCR-PUB-010`
- `/terms` -> `SCR-PUB-010`
- `/sms-terms` -> `SCR-PUB-010`
- Optional trust pages:
  - `/security`
  - `/responsible-ai`

## Home Page Section Contract (`SCR-PUB-001`)

1. Hero: missed-call revenue recovery + clear CTA
2. Pain: missed calls, no-shows, dispatch chaos, no revenue visibility
3. Product flow: call/text/chat -> qualify -> classify -> collect -> schedule -> dispatch -> notify -> report
4. Six pillars: front office, business rules, payment gate, dispatch, updates, revenue dashboard
5. Proof framing: control + policy enforcement, not generic answering
6. Demo preview
7. Pricing teaser
8. Final CTA

## Commercial Offer Map (High-Ticket)

Signmons public offer is intentionally multi-layered:

1. Base subscription (monthly/annual)
2. Setup fee (one-time)
3. Included call volume + overage blocks
4. Performance fees (qualified booked jobs, emergency captured jobs)
5. Add-ons (advanced recovery/escalation/seats/locations/custom setup)

Target public ladder:

- Starter: `$299/mo` + `$499` setup
- Growth: `$799/mo` + `$1,000` setup
- Pro: `$1,499/mo` + `$2,500` setup
- Enterprise: `from $3,500/mo` + custom setup (`$5,000+` baseline)

## Pricing Page Section Contract (`SCR-PUB-006`)

Pricing page must include all sections below:

1. Tier cards (Starter/Growth/Pro/Enterprise)
2. Setup fee disclosure by tier
3. Included volume + overage policy disclosure
4. Performance fee disclosure:
   - qualified booked job fee (range/policy)
   - emergency captured job fee (range/policy)
5. Add-ons section
6. Annual billing discount disclosure
7. "How pricing works" formula:
   - `Monthly Total = Base + Overage + Performance Fees + Add-ons`
8. Billable event definitions summary with link to full policy
9. Tier-specific CTA map:
   - Starter: `Start Early Access`
   - Growth: `Book Revenue Demo`
   - Pro: `Build My AI Dispatcher`
   - Enterprise: `Talk to Sales`

## Revenue and ROI Pages Contract (`SCR-PUB-015`, `SCR-PUB-016`)

Revenue Dashboard and ROI calculator pages must include:

1. Plain-language assumptions panel
2. Inputs that map to governed contracts (`PricingPlan`, `PerformanceFeePolicy`)
3. Output disclosure distinguishing estimates vs realized values
4. "What counts as billable" summary
5. Contact conversion CTA to `/contact`

## Build Priority

### Sprint 1: Core conversion

- Home, Pricing, Demo, Contact, Trust/Safety

### Sprint 2: High-ticket explanation

- Done-For-You Setup
- Business Rules
- Brand Voice
- Dispatch & Scheduling
- Revenue Dashboard

### Sprint 3: Competitive selling

- ROI Calculator
- Compare pages
- Customer & Technician Experience

### Sprint 4: SEO expansion

- Industry vertical pages

## Quality Rules

- Every route added here must map to a screen ID in `SCREEN_INVENTORY.md`.
- Every CTA target must exist in `LINK_CTA_MAP.md` before merge.
- Claims on these pages must obey `SAAS_SCOPE_DOD.md` high-ticket guardrails and proof-lock rules.

## Child Route Governance

- `/industries` maps to `SCR-PUB-004`.
- Industry child routes inherit `SCR-PUB-004` unless promoted into standalone screen IDs.
- `/compare/answering-services` maps to `SCR-PUB-017`.
- Answering-service competitor child pages (for example `/compare/smith-ai`) inherit `SCR-PUB-017`.
- `/compare/field-service-software` maps to `SCR-PUB-018`.
- FSM competitor child pages (for example `/compare/workiz`, `/compare/jobber`, `/compare/housecall-pro`, `/compare/servicetitan`) inherit `SCR-PUB-018`.
- `/security` and `/responsible-ai` inherit `SCR-PUB-005` unless promoted into standalone screen IDs.
- `/about` maps to `SCR-PUB-008`.
- `/blog` and `/resources` are content surfaces outside MVP screen enforcement unless promoted into governed screens.
