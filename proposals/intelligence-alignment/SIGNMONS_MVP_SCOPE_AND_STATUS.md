# Signmons Intelligence: MVP Scope, Sequence and Progress

Prepared 2026-09-12. Proposed alignment pending application, review and adoption. Neither repository was modified by this bundle's preparation.

## Evidence snapshot

- Governance main: af8a34031f669cd120c3c4c674860dd9e33007b9.
- Backend main: 2c7468b9bb80897f996add422faa5ce1a1027989.
- Open backend PR #21 is APP-013 transactional messaging; observed head 64942c0919e344ef248989b40e02b5c8c2c91db1. Active work may advance.
- The main boards record eight accepted application tickets: APP-003 and APP-006 through APP-012. These cover completion, intake/urgency review, dispatch, technician workflow, routing, customer booking management and payment workflow within their recorded acceptance boundaries.
- BE-003, BE-007 and BE-008 are also recorded as accepted webchat, lead-source-reporting and communications foundations.
- APP-013 remains Now. Open PR work is not a completed release. Its initial description leaves lifecycle triggers, dispatcher alerts, UI, monitoring and staging acceptance outstanding; inspect its latest code/evidence before deciding what remains.
- APP-017/018/019 were queued in the backend but lacked ticket files at the reviewed governance baseline. This bundle supplies them.

These are repository/board observations, not a new production retest. Unpushed Codex work is not visible here. No defensible engineering-completion percentage follows from ticket counts: scope, effort and integration risk differ. The backlog contains future work as well as first-release work.

## Release A: bounded Eternity CallDesk intelligence pilot

The first integrated MVP should demonstrate:

1. Safe tenant-correct voice, ordinary conversational SMS and web intake. Each channel needs its own evidence; notifications do not satisfy conversational SMS.
2. Relevant HVAC and comfort discovery, approved explanations, common objection handling and appropriate service/consultation booking without independent diagnosis or fabricated equipment recommendations.
3. Versioned tenant rules, trusted service charges/payment requirements, brand behavior, authorized customer/property/equipment context and a reviewed knowledge collection.
4. Canonical confirmation, conflict-safe scheduling, required-payment integrity, dispatch/technician ownership, customer confirmations and visible recovery.
5. Technician briefs, durable outcomes, human review, baseline evaluations, model/prompt/policy/knowledge versioning, latency/cost telemetry and basic funnel instrumentation.
6. Reviewed safety/handoff protocols, role access, consent/retention configuration, verified tenant/channel/calendar/processor setup, operating ownership, feature flags, rollback and explicitly approved activation.

Accepted components must be tested together. Unverified channels or tools must stay unavailable and cannot be advertised. This is a limited owner-operated pilot, not general availability of every paid plan.

## Release B: general commercial MVP and plan gates

The pilot does not waive SAAS_SCOPE_DOD.md, WHAT_SIGNMONS_IS_AND_DOD.md, OFFER_CATALOG.md or marketing release requirements. Before a general paid release, verify the tenant/admin interface, onboarding, subscription entitlement/billing, operational support, security, monitoring and recovery promised by the offer.

Full professional estimates/approvals/invoices/receipts require the governed Money release (APP-020 and relevant APP-021 scope). An approved service-fee configuration is sufficient for the first advisory booking pilot; it is not a full equipment pricebook or invoice product.

Reconcile remaining APP-001/002/004/005, APP-014, applicable BE security/reliability and OPS-001/002/003 requirements against real implementation. Create missing ticket specs before promotion. Existing code may satisfy some requirements; do not assume either absence or completion from backlog labels.

Starter's basic completion summary does not require the full APP-024 diagnostic-report product. Growth launch still requires the complete approved diagnostic-report workflow; Pro retains its further governed requirements. Do not sell a tier by silently dropping its release gates.

## Release C: after-pilot expansion and model optimization

Richer equipment sales, deeper diagnostic support, retention campaigns, predictive recommendations, financing handoff and broader trade operations are separately scoped increments. APP-024 supplies technician-verified diagnostic evidence; APP-025 through APP-032 retain their future boundaries. Basic recovery and safety are required now, even if advanced automation comes later.

Fine-tuning, preference/reinforcement experiments and additional autonomous agents require reviewed data, usage rights, an evaluation baseline, budget authorization and measured benefit. They are not automatic consequences of collecting conversations and are not first-pilot prerequisites.

## Ordered next queue

Finish the live APP-013 ticket and its required acceptance first. Do not interrupt its branch or treat a partial PR as Done. After adoption, align both boards with this queue:

| Order | Ticket | Why it comes here |
| --- | --- | --- |
| 1 | APP-017 | Versioned rules, approved service fees and missing-policy fail-closed behavior |
| 2 | APP-018 | Consistent tenant persona and ethical comfort/sales behavior |
| 3 | APP-019 | Authorized customer/property/equipment history and provenance |
| 4 | APP-015 | Quality review and independent evaluation baseline before richer AI release |
| 5 | BE-001 | Reconcile consent/telemetry requirements against accepted BE-008; reuse proven controls |
| 6 | APP-016 | Conflict-safe appointment lifecycle and payment-aware integration before voice promises bookings |
| 7 | APP-033 | Shared advisory intake, voice orchestration, knowledge/tools, human handoff and failure recovery |

This refines the earlier conversation: full APP-021 and APP-024 are not forced ahead of basic advisory voice. Trusted service pricing and booking/payment integrity are required. Equipment-specific priced proposals must wait for approved pricebook/estimate workflows.

Seven queued tickets are not seven equal tasks, nor the entire commercial MVP. Each must meet its own complete acceptance. After the queue, assess every pilot criterion and then the separate commercial-release requirements. Do not mark a whole ticket Done because only a pilot-facing subset works.

## Autonomous but governed progression

WIP remains one. Once adopted, finish Now with evidence, synchronize governance board/global pointer and the implementation board, then promote the first approved Next item within existing permissions. Routine phase selection need not return to the owner. Required human acceptance, provider authorization, budgets and production approvals remain gates. Do not skip a blocked Now or pull Later into Now simply to continue coding.

If a necessary dependency is missing, document it and use a governed scoped ticket change. Avoid rebuilding existing services or adding speculative agent infrastructure. Preserve real current progress when applying this dated proposal: never resurrect APP-013 if the live boards have advanced.

## Required completion report

Maintain requirement status as accepted, implemented-not-accepted, in-progress, missing or unverified. Link code, tests, release evidence, reviewer/owner and unresolved blockers. Use MVP_ACCEPTANCE_MATRIX.md as the release checklist, not as an effort estimate. A successful demo is a conversation -> appropriate next step -> authoritative sandbox action/handoff -> technician brief -> outcome -> review -> evaluation result.

## Sources for this snapshot

- https://github.com/Debynyhan-Banks/Signmons-governance/blob/af8a34031f669cd120c3c4c674860dd9e33007b9/EXECUTION_BOARD.md
- https://github.com/Debynyhan-Banks/Signmons-governance/blob/af8a34031f669cd120c3c4c674860dd9e33007b9/SAAS_SCOPE_DOD.md
- https://github.com/Debynyhan-Banks/Signmons-governance/blob/af8a34031f669cd120c3c4c674860dd9e33007b9/MVP_BACKLOG.md
- https://github.com/Debynyhan-Banks/signmons-calldesk-backend/pull/21

