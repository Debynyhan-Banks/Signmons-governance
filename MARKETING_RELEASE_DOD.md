# Marketing Release DoD (High-Ticket)

Purpose: define when the public marketing funnel is complete enough to support premium positioning and reliable lead capture before deeper app execution resumes.

## Phase Objective

Finish marketing first so Signmons can reliably convert traffic into qualified leads and demo requests while preserving truthful high-ticket positioning.

## Required Outcome Statement

The site must prove this operational claim without ambiguity:

"Signmons captures jobs, classifies urgency, enforces payment policy, routes work with controls, notifies teams, updates customers, and reports revenue outcomes."

## Scope Included In This DoD

- `SCR-PUB-001` Home
- `SCR-PUB-006` Pricing
- `SCR-PUB-007` Demo Experience
- `SCR-PUB-009` Contact / Waitlist / Demo Request
- `SCR-PUB-010` Privacy + Terms + SMS Terms
- `SCR-PUB-011` Done-for-you Setup
- `SCR-PUB-012` Business Rules and Custom Logic
- `SCR-PUB-013` Brand Voice and AI Personality
- `SCR-PUB-014` Dispatch and Scheduling
- `SCR-PUB-015` Revenue Dashboard
- `SCR-PUB-016` ROI Calculator
- `SCR-PUB-017` Compare: Answering Services
- `SCR-PUB-018` Compare: Field Service Software
- `SCR-PUB-019` Customer and Technician Experience

## High-Ticket Readiness Gates

### 1) Conversion Integrity

- Every primary CTA has a real route and real outcome.
- No `#` placeholder links for conversion actions.
- CTA labels and destinations match `LINK_CTA_MAP.md`.

### 2) Lead Capture Integrity (Email-Minimum)

- Contact flow requires a valid email at minimum.
- Submission persists to backend storage (no frontend-only success states).
- Frontend surfaces success/failure states from backend response.
- Lead event is auditable (request ID or persisted lead ID available).

### 3) Live Demo Integrity

- `/demo` route uses live backend demo APIs, not static-only simulation.
- Start-demo action returns status handle (`leadId` or equivalent).
- UI supports pending, success, and fail-closed fallback states.

### 4) Pricing Integrity

- Pricing copy is contract-driven and validated by `pricing:check`.
- Tier boundaries are non-conflicting (included vs add-on language).
- Setup fee + volume policy + overage policy are explicit.
- Performance fee policy disclosure is explicit (qualified booked jobs, emergency captured jobs).
- "How pricing works" formula is visible:
  - `Monthly Total = Base + Overage + Performance Fees + Add-ons`.
- Billable-event definitions are linked and consistent with governed specs.

### 5) Legal/Trust Integrity

- Privacy, Terms, SMS terms are reachable and current.
- Public claims do not exceed shipped behavior.
- Consent language for contact/demo is visible where required.

### 6) Experience Quality

- Responsive on mobile and desktop for all conversion routes.
- Accessibility basics: heading order, keyboard support, visible focus.
- Performance baseline: no critical regressions in build output.

## Frontend/Backend Alignment Checklist

- Route/CTA mapping updated in:
  - `SCREEN_ROUTE_API_MATRIX.md`
  - `LINK_CTA_MAP.md`
- Backend endpoints for marketing conversion are defined and available:
  - `POST /api/marketing/try-demo`
  - `GET /api/marketing/try-demo/:leadId`
  - `POST /api/marketing/lead-capture` (or explicit approved replacement)
- Payload contracts are documented in `DATA_CONTRACTS.md` before release.
- Failure modes are explicit:
  - endpoint unavailable
  - validation failure
  - timeout/retry exhausted

## Evidence Required Before Marking Marketing Complete

- Build/lint/test logs for touched FE tickets.
- Demo-flow proof (request + persisted status proof).
- Contact-capture proof (request + persisted record proof).
- Mobile + desktop screenshots for home, pricing, demo, contact.

## Exit Criteria To Unlock APP Sequence

Marketing phase is complete only when FE-006, FE-007, and FE-008 are in `Done` with evidence.
Once complete:
- move global `Now` from FE phase to `APP-006`
- switch frontend board from active execution to maintenance mode
- continue strict sequence on APP tickets
