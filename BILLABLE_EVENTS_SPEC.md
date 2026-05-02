# Billable Events Spec

Purpose: define billing-grade event semantics for subscription overage and performance fees.

## Event Types

1. `qualified_booked_job`
2. `emergency_captured_job`
3. `overage_block_consumed`

## Qualified Booked Job (Definition)

A job may emit `qualified_booked_job` only when all are true:

- required customer fields are complete under tenant policy,
- service category and urgency are resolved,
- booking window is confirmed,
- payment gate requirements are satisfied for that policy path (or explicit allowed override path exists),
- job status transitions into booked/scheduled state.

Exclusions:

- duplicate bookings for same customer issue without new accepted booking event,
- cancelled or invalidated jobs before booked/scheduled status,
- manual records missing required policy fields.

## Emergency Captured Job (Definition)

A job may emit `emergency_captured_job` only when all are true:

- urgency is classified as `emergency`,
- emergency reason code is present,
- dispatch or escalation event is triggered,
- tenant emergency fee policy marks the event as billable.

Exclusions:

- urgency downgraded prior to dispatch/escalation,
- duplicate emergency events for one lifecycle without explicit re-open policy.

## Overage Block Consumed (Definition)

An `overage_block_consumed` event is emitted when included monthly call volume is exceeded by one configured block unit.

Required:

- explicit block size and price from active pricing plan,
- deterministic counter state at month boundary.

## Amount Calculation Rules

- `qualified_booked_job` amount: tenant performance fee policy value at event time.
- `emergency_captured_job` amount: tenant emergency captured fee policy value at event time.
- `overage_block_consumed` amount: active plan overage block price.

## Immutability and Reversals

- Billable events are immutable once `finalized`.
- Reversal requires explicit credit/void event referencing original event ID.
- UI edits must not mutate finalized billable event amounts.

## Audit Requirements

Every billable event must include:

- source event ID,
- policy version used,
- actor/source channel,
- timestamp,
- reason code.

## Revenue Reporting Boundaries

- Public ROI pages may show estimates.
- Invoice and finance exports must use finalized billable events only.
- Any mismatch between estimate and finalized value must be explainable through policy, status, or timing differences.
