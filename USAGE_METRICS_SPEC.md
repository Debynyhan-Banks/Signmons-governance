# Usage Metrics Spec

Purpose: define nonfinancial operational usage metrics for subscription capacity guidance, forecasting, product analytics, and ROI reporting.

## Non-Billing Rule

No usage event carries a billable amount or creates a Signmons invoice line item. Signmons-to-tenant billing is a fixed monthly or annual subscription.

## Metric Types

- `ai_call_handled`
- `sms_sent`
- `sms_received`
- `booking_confirmed`
- `emergency_escalated`
- `active_technician_observed`
- `location_observed`

## Qualifying AI-Handled Call

A call counts toward plan-suitability visibility only when it:

- reaches the tenant AI experience,
- contains customer speech or a valid accessibility-equivalent input,
- passes configured minimum-duration or engagement rules,
- has a stable source communication ID for deduplication,
- is not spam, blocked traffic, a silent hang-up, or an approved test.

## Capacity Response

- Approaching plan capacity produces an operator-visible notice.
- Sustained excess usage produces a fixed-price upgrade recommendation or Enterprise review.
- Capacity cannot create a metered charge, booking fee, emergency fee, revenue share, or automatic invoice adjustment.
- Life-safety and emergency handling must never be interrupted solely because a tenant reached a capacity guide.

## Audit Requirements

Every usage metric includes tenant ID, source event ID, event type, quantity, timestamp, exclusion state, and reason code. Metrics are tenant-scoped, deduplicated, privacy-conscious, and auditable.

## Reporting Boundary

Revenue and ROI reporting may use operational metrics to estimate value. It must label assumptions clearly and must not represent bookings, emergencies, calls, or recovered revenue as Signmons charges.
