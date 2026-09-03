# Billable Events Spec — Retired

This specification is retired by the owner-approved subscription-only commercial model dated 2026-09-01.

Signmons does not charge setup, per-call overage, booked-job, emergency-capture, revenue-share, or basic per-invoice fees. The former `qualified_booked_job`, `emergency_captured_job`, and `overage_block_consumed` billing events must not create invoice line items or tenant charges.

Operational usage, booking, and emergency metrics remain valuable for product analytics, forecasting, capacity guidance, and ROI reporting. Their nonfinancial contract is now governed by `USAGE_METRICS_SPEC.md` and `UsageMetricEvent` in `DATA_CONTRACTS.md`.

This file remains only as a compatibility marker so older references fail toward the current policy instead of silently restoring the retired fee model.
