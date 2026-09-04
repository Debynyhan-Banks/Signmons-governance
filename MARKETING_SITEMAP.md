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

Signmons public offer is intentionally simple:

1. Fixed subscription (monthly/annual)
2. Tier-specific feature, location, technician, and fair-use capacity
3. Fixed-price plan upgrade or Enterprise subscription when needs consistently exceed the current tier
4. No setup, per-call overage, per-booking, emergency-capture, revenue-share, or required MVP add-on fees

Target public ladder:

- Starter: `$299/mo`
- Growth: `$799/mo`
- Pro: `$1,499/mo`
- Enterprise: fixed custom monthly/annual subscription

Limited bridge offer:

- Founding Partner: `$199/mo`, first `10` approved external businesses, `12`-month price lock while active, no setup fee
- Must be labeled early access; unshipped capabilities cannot be represented as generally available or billed before activation

## Pricing Page Section Contract (`SCR-PUB-006`)

Pricing page must include all sections below:

1. Tier cards (Starter/Growth/Pro/Enterprise)
2. Included feature, location, technician, and fair-use capacity guidance
3. Explicit no-setup/no-overage/no-outcome-fee disclosure
4. Fixed-price upgrade policy when needs consistently exceed the current tier
5. Annual billing discount disclosure
6. "How pricing works" formula:
   - `Signmons subscription total = fixed selected-plan subscription` (plus applicable taxes only)
7. Contractor-to-customer Stripe payment boundary
8. Basic payment-before-booking gate included in every paid public plan after the Signmons Money release gate; Growth and higher differentiate through advanced payment-policy controls
9. Tier-specific CTA map:
   - Starter: `Start Early Access`
   - Growth: `Book Revenue Demo`
   - Pro: `Build My AI Dispatcher`
   - Enterprise: `Talk to Sales`
10. Professional invoicing disclosure:
   - basic estimates/invoices/payment links/receipts included after the Signmons Money release gate
   - no basic Signmons per-invoice fee
   - processor and other pass-through provider fees disclosed separately

## Revenue and ROI Pages Contract (`SCR-PUB-015`, `SCR-PUB-016`)

Revenue Dashboard and ROI calculator pages must include:

1. Plain-language assumptions panel
2. Inputs that map to governed contracts (`PricingPlan`, `SubscriptionEntitlement`, `UsageMetricEvent`)
3. Output disclosure distinguishing estimates vs realized values
4. "What the subscription includes" and nonfinancial capacity assumptions summary
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
