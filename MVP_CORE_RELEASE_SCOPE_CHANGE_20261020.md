# Core commercial MVP downsizing — owner direction and exact adoption proposal

## Decision and status

On October 20, 2026, Debynyhan Banks answered the six release-scope questions: "yes, yes, yes, yes yes, quickbooks and existing FSM is not needed now, yes. i agree with your proposal".

**Approved direction:** narrow the first commercial release to the connected Revenue Integrity Dispatch service-call journey; use the limited Founding Partner/Starter path; keep basic phone answering; require the approved service-call fee/deposit before booking when policy requires it and collect the approved final balance after work; use guided setup, online-only field operation and manual dispatch; require neither QuickBooks nor an existing FSM; move richer intelligence/configuration and other optional capabilities to later releases.

**Not yet adopted:** the exact protected acceptance replacements in [the proposed diff](MVP_CORE_RELEASE_PROPOSED_DIFF_20261020.patch). The owner approved the product direction and preparation of a formal scope proposal, not previously unseen protected wording. This record and diff are that concrete proposal. The active baseline, current pointer, Now/Next order and all accepted evidence remain in force until this exact amendment is reviewed and adopted through the existing safeguard process. No application implementation or external action is authorized by this preparation.

Source snapshots: governance `fe3cfada8803e17c0b8f41003c5d65dae93deb77`; backend `c426c319c240879dfb7c7ebf2f5aabfa5161c9d7`. Both focused worktrees were clean before proposal preparation.

## Demonstrated gap, alternatives and decision

The 13-row integrated intelligence pilot requires broad brand/comfort behavior, contextual history, approved retrieval and independent evaluation before commercial gates are considered. The 60-package plan explicitly excludes commercial subscription launch and full Money/pricebook/diagnostic products. Consequently, calling all of it "MVP" hides a larger launch boundary, while merely removing already-deferred inventory/payroll/financing would not remove the actual intelligence gate.

Alternatives reviewed: (1) complete the entire integrated intelligence pilot and all selected plan promises before first commercial learning; (2) narrow to a web-only/payment demonstration, losing the marketed phone product and full commercial journey; (3) retain the complete core transaction and commercial safety while deferring optional breadth. The owner selected option 3. No time saving, launch date, new effort percentage, or completed capability is inferred from that decision.

## Release 1 — supported buyer and connected finish

Initial cohort: small service/repair businesses, one location and up to two technicians, English, online access, one approved service area, guided setup, one supported calendar path, Stripe and owner/dispatcher supervision. Exact pilot tenant/environment bindings and every external operation retain their existing qualification and approval boundaries. This is a product cohort, not a new tenant or deployment authorization.

Supported journey: lead -> qualify -> confirm -> enforce required payment/policy -> book -> manual dispatch -> complete -> collect approved final balance -> report the outcome. Unknown repair scope does not justify invented upfront prices. Additional paid work requires an approved quote/scope before execution. Deposits must be allocated against the final balance without duplicate collection.

The following are proposed release acceptance boundaries, **not numbered implementation packages or a new progress denominator**:

| Boundary | Required user-observable finish | Existing ownership / reuse |
| --- | --- | --- |
| Setup and access | Guided business setup, correct tenant/roles, approved hours/coverage/fees, safe activation and fixed-subscription administration | APP-001/004/005, BE-006, OPS-003; reuse organization controls |
| Intake and confirmation | Basic AI phone answering, bounded web/SMS intake, missed-call text-back, qualification and critical-field confirmation with approved emergency/human fallback | APP-006/007/013/033, BE-008; preserve accepted verification |
| Policy and initial payment | Finite versioned policy, missing/changed policy refusal, immutable fee/currency snapshot and authentic required-payment evidence | APP-017/012/016; same-job P07/P08 |
| Booking and communications | Conflict-safe booking, private appointment management, changes/cancellation, essential eligible notices and truthful failures | APP-011/013/016, BE-001; P09–P14 |
| Dispatch and completion | Controlled manual assignment, technician status, relevant notes/photos/equipment facts, completion summary and confirmed outcome | APP-008/009 and basic APP-033 brief |
| Basic customer Money | Approved simple quote, final invoice, deposit allocation, payment link, receipt and auditable partial/failed/refund/credit/void state | APP-020 subset and APP-012; reuse DATA_CONTRACTS.md billing contracts |
| Outcome and exceptions | Supported-stage counts, actual collections, stalled/failed work and owner; minimum customer/job linkage and source provenance | APP-014 subset, BE-007, existing audit/jobs/payments |
| Quality and operations | Independent critical safety/privacy/payment/booking tests, relevant version/outcome evidence, latency/cost monitoring, support, incident ownership and tested restore/rollback | APP-015, BE/OPS and minimal APP-031/032 obligations |
| Commercial acceptance | Authorized connected lead-to-completed-and-paid journey plus critical negative/recovery scenarios, correct offer activation and explicit owner sign-off | Release gate; no capability accepted by this proposal |

Basic reporting must distinguish estimate, invoice, collected, partially paid, failed and refunded values. BE-007 currently reports tenant-scoped job lifecycle counts and website_chat attribution, not all leads, collected revenue or profit. Do not rename job-created counts as all leads or claim causal recovered revenue. Profit remains unavailable until governed APP-026 costs exist.

## Release and feature disposition

| Release | Included direction / constraints |
| --- | --- |
| R1 Core MVP | The complete supported journey and commercial safety above; fixed templates/finite policies; simple approved customer/job facts and completion evidence |
| R2 Operations | Bounded pricebook and quoting improvements, richer service history, review requests and improved communications. QBO/FSM remain optional, unrequired and inactive unless later justified and separately approved |
| R3 Intelligence/Growth | Rich brand/discovery/retrieval, advanced reporting, memberships/maintenance automation and diagnostics if Growth is offered; costing before profit attribution; good/better/best only after governed prices/quote approval |
| R4 Scale | Offline synchronization, inventory/purchasing, time/payroll export, broad integrations, multi-location and migration breadth; financing where independently justified |

Advanced diagnostic reports, full pricebook, good/better/best sales, review automation, memberships, deep equipment history, generic business-rule automation, persona configuration, advanced analytics, costing, inventory, time/payroll export, offline, broad CRM/FSM, financing and APP-034 are not R1 prerequisites. Later releases are separately scoped capabilities, not a bundle that must all ship together.

Merge factual greeting/approved business facts/finite policy configuration into guided setup; preserve authoritative policy separately from free-form brand text. Use one customer/job identity and one outcome/exception view. Do not create a new CRM, unrestricted workflow builder, marketing suite or generic platform merely to prepare for future work.

Deferral costs remain explicit: less sales consultation/personalization, slower manual quoting and accounting entry, manual review/renewal follow-up, no margin claim, and no fit for offline-dependent operations. Target buyers whose workflow fits these constraints rather than masking unsupported behavior.

## Commercial promises and safety retained

Use the existing Founding Partner bridge for accurately labeled activated capabilities. Public Starter cannot be called generally available before its actual promises pass, including basic phone/SMS/web, missed-call recovery, owner alerts and basic Money. Keep existing fixed subscription pricing and capacities. Growth remains gated by full diagnostic reporting; Pro retains its later promises. No new price, add-on, usage charge or performance fee is introduced.

Tenant/role isolation, verified external events, current policy, customer authorization, consent/STOP/HELP, secure private links, retention/redaction, idempotent side effects, truthful uncertain states, visible failure ownership, controlled recovery, support and restore evidence cannot be deferred. Safety evaluation remains independent of sales scores. Recording/training and new vendor/data sharing remain separately governed.

Existing domain boundaries, identifiers, applied policy snapshots, explicit states, audit/provenance and narrow provider interfaces are sufficient architecture direction. Future features consume those records outside the critical booking path. No event bus, plugin framework, microservices, speculative schema or future UI is authorized.

## Existing ticket and package traceability

| Existing scope | Proposed R1 treatment | Deferred requirement preserved |
| --- | --- | --- |
| P01–P06 / 1A–2B | Preserve accepted work/evidence; do not reopen | None removed or reaccepted |
| P07–P14 / 3A–3D | Retain same-job payment, calendar, received text, changes/recovery unchanged | No new walkthrough section or bypass |
| P15–P22 / APP-013 | Essential notices/owner events, consent, privacy, delivery failures/audit; fixed templates and finite setup | Broad independent SMS/email event/recipient/brand customization and full appointment-email/calendar-action breadth to R2 |
| P23–P27 / APP-017 | Authoritative finite policy, versions, fees/snapshots and safe essential actions | General automation/trigger configuration and broad center to later scope |
| P28–P31 / APP-018 | Approved factual greeting/wording and safety/refusal checks in guided setup | Persona builder, broad behavior previews and comfort-sales scenarios to R3 |
| P32–P36 / APP-019 | Minimum authorized customer/property/current-job facts, prior relevant work, provenance/corrections/retention | Rich equipment/history/preferences/recommendations UI and memory to R2/R3 |
| P37–P41 / APP-015 | Essential metrics/failure ownership and independent critical-failure evaluation with version/outcome evidence | Advanced review/dashboard/export tooling and optimization to R3; no automatic training |
| P42–P45 / APP-016 | Retain full booking/payment/private-link/lifecycle integrity | None of these integrity gates deferred |
| P46–P55 / APP-033 | Basic phone/bounded web/SMS, approved curated facts, typed tools, safety, confirmation, interruption/fallback and truthful brief/outcome | Broad corpus/retrieval tooling, rich shared memory and comfort/sales orchestration to R3 |
| P56–P60 | Retain guided setup, operating owner, recovery, restore and narrowed commercial journey proof | Full intelligence rehearsal/matrix acceptance remains a later requirement |
| APP-020, APP-014, BE-006, OPS / commercial tail | Explicit basic Money, collections report, subscriptions/admin and commercial support gates | Existing source gaps must be sized; not silently assumed in the old 60 packages |
| APP-021/022/023/024/025–032/034 and integrations | Retain only the minimum commercial safety/ownership obligations explicitly listed above | Wider products remain Later/release-dependent; QBO/FSM not required now |

The proposed diff narrows the relevant current ticket clauses in place and preserves original text as archived scope at adoption. Closing a future amended R1 ticket would mean its explicitly amended R1 criteria passed, not that the original full module shipped. Deferred criteria require later scoped work; no original item is silently marked accepted.

Keep the current Now and Next ticket order: APP-013, then APP-017 -> APP-018 -> APP-019 -> APP-015 -> APP-016 -> APP-033. Their proposed R1 scope is smaller; full acceptance of each *adopted* criterion remains necessary before promotion. Do not skip, partly close, or promote from this proposal. Basic Money/reporting/admin remain unsequenced commercial-tail gates until their source/evidence cards and dependencies are reviewed; no invented executable tail queue.

## Count, effort and current-operation impact

- Existing accepted ledgers remain **6/60 packages, 4/8 walkthrough milestones, 0/13 full intelligence-pilot rows**. They are separate measures; no acceptance or percentage improves because optional scope is deferred.
- The proposed APP-013 replacements preserve its twelve criterion positions; the content changes are visible in the diff. Its original full-scope evidence remains traceable and unaccepted items stay unaccepted.
- The eight walkthrough milestones, accepted 1A/1B/2A/2B and all 3A–3D acceptance text remain unchanged. APP-016 financial/calendar integrity is unchanged.
- A new commercial R1 progress denominator is not established here. First inventory retained code, environment-specific acceptance evidence, basic Money/reporting and commercial administration gaps; then size a finite ledger for review. The old 60 packages cannot simply be shortened and relabeled commercial MVP.
- No launch date or effort-saving estimate is established. Current P07 readiness blockers remain; this scope decision does not qualify providers, renew operation windows or authorize replay/deployment/payment.

## Exact amendment and bounded adoption procedure

Review `MVP_CORE_RELEASE_PROPOSED_DIFF_20261020.patch` against the source snapshots above. It contains exact old/new protected APP-013 replacements, future ticket scope changes and synchronized proposed canonical/release boundary text. It is a review artifact only, not applied changes.

After exact approval: archive the prior scope texts without moving active tickets out of place; adopt only the reviewed replacements; keep the original frozen anchor and apply a narrowly pinned immutable amendment rather than resetting it; retain tests rejecting unauthorized mutation. Run frozen-baseline, cross-repository consistency, placement/alignment regressions, backend baseline/architecture and whitespace checks. No bypass flag or self-approval. The global execution pointer and runtime stay unchanged during this adoption; any later ticket promotion is separately evidenced.

Rollback before implementation: leave the current governed source untouched and mark this proposal declined/superseded. After an adoption, reversing it requires its own explicit reviewed change; never rewrite accepted evidence or history.

**Next observable result:** owner review of this exact diff; then adoption and a source-sized R1 acceptance map. The implementer owns proposal/traceability/checks; Debynyhan Banks owns the exact amendment decision and later release acceptance. Approved direction only; exact scope adoption pending. No scope deviation implemented.

## Preparation validation

Current frozen-baseline and cross-repository documentation consistency checks pass, as do all 21 existing governance safeguard regressions, the backend governance-baseline wrapper, architecture check and whitespace checks in both repositories. The proposed documentation diff passes `git apply --check` against the stated governance source. A read-only virtual-snapshot audit confirms exactly the two declared protected sections would change (APP-013 acceptance and the contract's remaining-MVP paragraph), all twelve APP-013 criterion positions remain, 2B/3A/3B/3C/3D section text is unchanged, and APP-016/pointer/queue have no proposed edits. These checks validate proposal preparation, not adoption, application behavior or customer acceptance.
