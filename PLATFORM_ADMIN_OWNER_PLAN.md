# Platform administration — owner-only first version

## Decision and scope — 2026-09-13

Owner requested discussion and documentation, agreed the first version is for Debynyhan alone, and asked whether this extends the MVP. This records product direction only: no implementation, release, new acceptance criterion, additional package or queue change is authorized. Source governance 40d8add and backend f0201ac.

Documenting this does not extend the Release A pilot's 60-package scope or its estimate. Building additional admin functionality before that pilot could add work and delay; that requires a separately reviewed impact/change proposal, not an implicit addition. Release B already requires commercial administration: this plan refines that direction without claiming its effort is estimated or implemented. Current APP-013/P04 checkpoint and planned P05/P06 order are unchanged. No scope deviation.

## First audience and boundaries

- First version: Signmons owner only. No support-staff or salesperson portal in this version.
- Platform administration remains distinct from each contractor's tenant administration.
- Owner-only does not bypass authentication, least privilege, tenant isolation, sensitive-access auditing or separate authorization for consequential actions.
- Start with operational visibility; retries, refunds, suspensions and configuration changes require explicit action contracts and safeguards before implementation.

## Information architecture

Reuse SCREEN_INVENTORY.md SCR-ADM-001 through SCR-ADM-007: tenant health, subscriptions/billing, security/compliance, usage/cost, AI failure review, payment/webhook failures and onboarding. Overview summarizes these screens rather than introducing another reporting subsystem.

Homepage priorities: critical actionable exceptions first, then tenant/onboarding health, workflow outcomes, and financial summaries with freshness and evidence status. Each issue should identify affected business/workflow, severity, owner, next safe action and resolution evidence.

Proposed business-detail navigation: Summary, Onboarding, Configuration, Activity, Usage/cost, Billing, Issues, Audit. These are proposed views, not new accepted route/API contracts. Default to operational summaries; sensitive customer content requires specifically authorized and audited access.

## Reporting rules to preserve

- Separate Signmons subscription revenue from contractors' customer payments.
- Label costs estimated, provider-reported or reconciled; disclose shared-cost allocation assumptions.
- Missing telemetry is unavailable/not instrumented, never an invented zero.
- Define source events, numerator/denominator, exclusions and reporting periods for every metric.
- Separate contribution from net profit; this is not a general-ledger replacement.
- Sales commissions and compensation percentages in the discussion attachment are proposals, not approved agreements. No payout automation or salesperson access is authorized.
- AI review distinguishes appropriate handoff from failed or missed handoff; customer conversations are not automatically training data.

## Delivery placement and finite next planning step

1. Release A: reuse already-required onboarding, AI review and operational monitoring (including existing P37–P41 and P56–P57); this document adds no dashboard acceptance to them.
2. Release B: map owner administration and commercial billing/entitlement/cost views to existing tickets after inspecting actual code, routes and evidence. Do not assume seven screen names equal seven implementation packages.
3. Later proposals: sales attribution, commission tracking and forecasting require explicit rules and scope approval before scheduling.

Before any admin implementation, prepare one finite screen-to-ticket map with actual existing components, missing route/API/data contracts, owner permissions, acceptance tests, dependencies, exclusions and effort impact. Resolve gaps through existing change control. Do not interrupt P05 to build this panel or alter milestone/package percentages on the strength of this planning note.

## Documentation checkpoint

Completed: owner-only audience, proposed layout, access/reporting rules and release boundary recorded. Remaining: future implementation mapping and sizing when commercial-admin work is authorized. No runtime changes, provider actions, merge, deployment, customer contact, charges or training.
