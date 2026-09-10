# Verification unit economics — 2026-09-10

## Owner direction and boundary

Owner approved proceeding with the inactive Verify adapter and asked to remain competitive and profitable across differing provider prices. This document records measurement/control requirements, not a price change, billing implementation or approved target margin. No subscriptions, plan entitlements, live spend caps, provider configuration or charges changed.

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

No margin target, launch pricing, usage allowance or production spend ceiling is chosen here. The next coding slice remains the durable verification operation connection; do not expand it into a billing platform.
