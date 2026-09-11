# CallDesk MVP completion audit — 2026-09-11

## Outcome and scope

The MVP is substantially implemented in pieces, but the complete real customer-to-job-to-completion journey is not demonstrated. Verification is the immediate S1 blocker, not the only remaining MVP work. Stop expanding isolated fixtures: require each next section to remove a named blocker in the fixed steel thread below.

Audit snapshot: backend ffb0dc9, governance ae2366c, both remote feature branches fetched. Read-only source/document review; no live environment, provider account or mailbox inspection. Prior test results are evidence records, not rerun results. APP-013 remains the sole Now; Next empty; FE-014 paused. This audit authorizes no new ticket, feature, source substitution or release.

Authoritative scope: CALLDESK_MVP_PLAN.md required capabilities and its twelve pilot acceptance checks; CALLDESK_STEEL_THREAD_CLOSEOUT.md S1–S4; ORGANIZATION_ONBOARDING_MVP.md S0. Website import, sales-advisor expansion, unrestricted editors, advanced analytics and deferred trades modules remain excluded.

## Current capability ledger

“Built” below means a relevant implementation exists, not all requirements are done. “Local” includes mocks and isolated fixtures. No row gains whole-pilot acceptance from earlier staging work.

| Required capability | Built / demonstrated evidence | Missing integration or acceptance |
| --- | --- | --- |
| Business onboarding and approved answers | Organization profile save/approve, deterministic FAQ, local payment-policy and combined organization/address evidence | Production identity/tenant binding, canonical policy adoption, full six-outcome owner acceptance; live model answer behavior is not proved by deterministic FAQ |
| Web-chat intake and operator handoff | Protected customer/session/review, separate operator admission and browser-review-admission fixtures | Latest address-bearing review cannot create an eligible job; real proofs, correction confirmation, current-policy consumption and application UI/identity connection |
| Automated phone/address verification | Inactive Verify adapter, durable reservations/budget, Google matching fixture | County source qualification, exact correction confirmation, phone freshness/revocation, shared abuse controls, reconciliation, deadlines, approved accounts/rates and live evidence |
| AI phone answering and conversational SMS | Signed tenant-resolved webhooks, greeting, consent keywords | Voice currently returns Say greeting only; SMS routes to consent keywords. Full dialogue, missed-call recovery, interruption and cross-channel handoffs remain |
| Safety and urgency | Existing safety/intake foundations and refusal cases | Full conversational channel safety, dropped-call/provider failure and human-owned exception demonstration |
| Payment controls | APP-012 provider/webhook/policy foundations and local/sandbox evidence | Current pilot end-to-end payment gate, continuous approved integration and failure/out-of-order cases; do not equate old staging summaries with current live acceptance |
| Booking and private customer management | Registered confirm/reschedule/cancel services; APP-011 evidence | Connect newly verified job, current payment/availability and truthful Calendar recovery; recovery journal/review classes are not registered in SchedulingModule |
| Customer communications | Registered SMS intent/delivery/history, fixed templates, email content/event/eligibility foundations | Durable customer email delivery/failure/retry, full event/recipient policy matrix, safe private actions and controlled real delivery evidence |
| Dispatcher and technician workflow | APP-008–010 foundations, technician inbox and job progression | Same pilot job through assignment and completion with current roles, visibility and auditable exceptions |
| Operational oversight/readiness | Reporting/audit/access foundations and local recovery tests | Defined pilot indicators/latency limits, actionable uncertain work, retention/deletion, restore/rollback, incident ownership and complete owner acceptance |

## Evidence anchors inspected

Backend paths relative to its focused worktree:

- src/communications/communications.module.ts: registered SMS/settings components; Google/local verification paths absent.
- src/communications/twilio-webhook.service.ts: receiveVoice greeting and receiveSms consent-keyword routing.
- src/scheduling/scheduling.module.ts: lifecycle services registered; separate recovery services absent.
- src/reporting/reporting.service.ts: existing reporting foundation, not proof of all pilot indicators.
- evidence/APP-013/google-adapter/README.md: 49 mocked tests; no confirmation endpoint or real verification authority.
- evidence/APP-013/organization-address-thread/README.md: combined approved organization/address review, no new job, deterministic FAQ.
- evidence/APP-013/verification-journey/README.md: mocked provider, held reservations, incomplete reconciliation/replenishment/alerts.
- evidence/APP-013/booking-readiness-preview/README.md: readable blockers, not booking authority.
- evidence/APP-013/browser-review-admission/README.md and organization-setup/README.md: local handoff/onboarding evidence.
- evidence/APP-009/readiness-report.md, APP-011/readiness-report.md, APP-012/readiness-report.md and APP-013/readiness-report.md: prior workflow/evidence boundaries. Older report headers and staging statements must not override current scope or be treated as a fresh deployment check.

## Percentages: what can actually be defended

| Measure | Numerator / denominator | Result | Meaning |
| --- | --- | --- | --- |
| APP-013 local scope index | 1 demonstrated + 10 partial at 0.5 + 1 missing, divided by 12 criteria | 50% | Existing equal-weight scope rubric; not effort or whole-MVP completion |
| APP-013 signed acceptance | 0 / 12 | 0% | No formal criterion sign-off recorded |
| Onboarding local demonstration | Recorded 3 / 6 outcomes | 50% | Existing local baseline, not production onboarding |
| Onboarding acceptance | 0 / 6 | 0% | No formal outcome sign-off |
| Whole-pilot acceptance | 0 / 12 frozen pilot checks | 0% | No complete accepted pilot; not 0% built |

No defensible effort-weighted overall build percentage can be calculated from current evidence. The numerator is mixed registered code, unregistered fixtures and prior staging work; the denominator contains unsized voice/channel and operational integrations. Inventing weights would create false precision. Do not average the two 50% values, count tests as completion, or treat 0% pilot acceptance as absence of implementation.

Keep the twelve-criterion APP-013 ledger unchanged: only ask-once email retention is locally demonstrated; email failure/retry is missing end-to-end; the other ten remain partial. Recent address work removes prerequisites but does not finish a notification criterion. Retire rolling 20–35-section forecasts as already directed by the steel-thread closeout; this audit supplies order and exit conditions, not a calendar ETA.

## Fixed delivery order and stop conditions

S0 is the existing setup prerequisite, not a new feature. Reuse its implementation. Start with the web-chat proving channel; phone/SMS stay in full MVP.

1. **S1 correction confirmation:** bind customer confirmation to exact candidate/address revision, session and tenant; edits/expiry invalidate it. Stop at mocked end-to-end corrected-address confirmation/refusal evidence, with no job authority.
2. **S1 verification operations:** close timeout, duplicate/unknown outcome, proof freshness/revocation and shared cost/recovery controls for existing providers. Stop when mocked crash/retry/budget cases preserve progress and liability. Size this package before coding; do not promise it fits one turn.
3. **S1 real-proof-to-job connection:** consume approved current phone/address/coverage/business-policy proofs atomically. Stop when the same customer/operator journey creates exactly one eligible job and all stale/foreign/uncertain cases refuse. Real source/account/retention approvals are entry gates, not waived by local mocks.
4. **S2 payment, booking and notifications:** reuse existing modules; demonstrate one governed payment-required booking plus change/cancel and eligible communication, including owned uncertain failures. Email delivery and Calendar recovery remain explicit work, not done by address completion.
5. **S3 assignment to field completion:** same job, correct dispatcher/technician roles, lifecycle alerts, visible payment/booking state and recovery ownership.
6. **S4 full channels and pilot readiness:** voice/SMS/missed-call handoffs, safety/fallback, indicators, retention/restore/rollback and twelve-check owner acceptance. Map later-ticket work in pointer/handoff before starting it.

These are ordered outcome packages, not six equal coding sections. Only package 1 is currently bounded as the next implementation section; later packages need entry-point sizing against existing modules. No generic framework cleanup unless a reachable failure blocks the next demonstration.

## External decisions and parallel work

County inquiry was sent with explicit approval on September 11; no reply check during this audit. A qualified county source is still missing. Do not let waiting halt independent correction-confirmation work, but do not substitute ZIP or label-based acceptance.

Before live proof/admission: named tenant/environment, provider accounts and rates, separate address spend cap, notices, submitted-record retention/deletion schedule, alert/recovery owner and legitimate test participants. Before release: explicit merge/deploy/migration/configuration authority and acceptance. Existing $50 phone cap is not spend permission.

## Review, validation and governance cleanup

Review capability gaps, scoring and the six ordered packages against the frozen pilot checklist. Next recommended approval: package 1 only, with an exact candidate/revision confirmation demonstration. Audit changes no runtime and grants no release permission.

DELIVERY_COMPLETION_MATRIX.md contains a dated April marketing-first snapshot; mark it historical and direct readers to current pointer and this audit. Historical plan percentages remain evidence history, not active forecasts.

Applicable audit gates: governance consistency, four execution-placement tests and git diff --check. No application build/test/browser run is needed for documentation-only changes; no old results are claimed as fresh.
