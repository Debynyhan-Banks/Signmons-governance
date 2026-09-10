# Verification unit economics — 2026-09-10

## Owner direction and boundary

Owner approved a $50 USD monthly phone-verification ceiling per organization, internal alerts at $25 and $40, and explicitly approved increases for higher volume. Reserve sufficient potential cost for the whole flow before starting; refuse new cost-bearing work beyond available budget, never bypass verification. This is an internal MVP safeguard, not a customer charge, subscription allowance or profitability guarantee. Review actual usage, conversion and subscription revenue after the first pilot month. No live activation, provider configuration, billing change or charge is authorized.

The inactive implementation is documented in backend evidence/APP-013/verification-budget/README.md. USD integer micro-units avoid floating-point money arithmetic; UTC calendar-month labeling is the current local convention. Fixture quotes deliberately use $25/$30 whole-flow estimates to prove boundaries, not actual provider pricing. All reservations remain HELD across month boundaries until a later approved reconciliation mechanism; this conservative proof cannot yet replenish a recurring monthly allowance. No scheduled alert delivery or approved-override administration is implemented.

## Separate observation, estimate and actual cost

The inactive adapter returns a logical operation ID, START/CHECK classification, attempted SDK invocation count and billing NOT_ATTEMPTED/UNRECONCILED. It cannot know SMS segments, provider retry charges, invoice adjustments or final billable successes from that alone. APPROVED is an observed outcome, not a reconciled invoice item. Unknown outcomes remain potential liabilities rather than zero-cost successes/failures.

Next durable collector must associate tenant, logical request, physical attempt, verification SID when known and observed time; deduplicate receipt replay without collapsing separately incurred attempts. Keep raw phone and code out of metrics. Store provider/account, destination market, currency, channel, rate-card version/effective date and reconciliation status with each estimate. Missing pricing inputs produce UNKNOWN, not zero. Actual provider usage/invoice reconciliation must preserve corrections and attribution; do not overwrite history with today's rate.

The previous published US example in PHONE_VERIFICATION_PROVIDER_DECISION.md remains a dated illustration, not a negotiated quote or an application default. Country/channel rates, extra attempts, taxes and applicable charges require review before spend authorization.

## Useful business measures

- Verification cost per successful customer = attributable verification cost / unique successfully verified customers in the same defined cohort. Include abandoned/failed attempts; do not double count retries of a saved receipt. A zero denominator is not a zero cost.
- Variable cost per booked job = attributable AI, telephony, SMS/email, verification and relevant payment-processing costs / confirmed bookings, with documented allocation for leads that never book.
- Contribution = Signmons revenue less consistently defined variable cost. Margin = contribution / revenue for nonzero revenue; this is not net profit after all overhead.
- For a chosen contribution-margin target m and estimated variable cost C, revenue floor C/(1-m) is a planning relationship, not a proposed public price. Add allowances for support, infrastructure, refunds, taxes and fixed costs as appropriate to the business model.

Separate fees paid by Signmons from fees paid directly by each service business. Customer deposits collected for a contractor are not automatically Signmons revenue. No new Stripe routing, fee policy or tax assumption is made here.

## Controls required before scale

Use per-organization usage attribution, retry/destination/peer limits, bounded pending-cost reservations, configurable alerts and an enforceable spend circuit breaker. Alerts alone are not a hard cap. A provider timeout does not release a cost reservation as if nothing happened. Set limits from approved traffic forecasts and tested recovery; retain a customer-friendly error path.

Compare candidate plan economics at normal and high usage, lower booking conversion, repeated codes, longer calls, different destination markets and provider price changes. Included allowances/overages must follow measured unit costs and owner-approved positioning, not an unverified competitor price or an unlimited-use promise. Competitor research and actual plan changes are separate approved work, not this adapter task.

No margin target, launch pricing, subscription usage allowance or provider rate card is chosen here. The $50 ceiling is approved policy for implementation, not permission to incur it. Actual rate inputs must cover the supported destination/channel and entire bounded flow, including applicable fees and uncertainty; missing inputs refuse rather than default to zero. Higher ceilings still require explicit approval. No automatic overage fee or billing-platform expansion.
