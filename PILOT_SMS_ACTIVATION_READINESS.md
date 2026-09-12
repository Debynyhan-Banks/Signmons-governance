# Pilot SMS: production policy and activation readiness

## P2 bounded suppression checkpoint — 2026-09-12

Backend 64942c0 completes shared recipient serialization, atomic START and suppression precedence over verbal grants, with a database-incremented consent revision. This is one section within P2, not P2 completion. Evidence: evidence/APP-013/sms-consent-serialization/README.md. Next within P2 is production-shaped policy-bound capture evidence/registry integration under this lock and revision. Existing fixture records remain non-authoritative; capture and sending stay unactivated. Provider event replay/order, retention/key lifecycle, publication and release remain gated. Acceptance unchanged: 3/8 milestones (37.5%), not overall MVP completion.

## P1 implementation checkpoint — 2026-09-12

Owner approved P1; backend 5e771c3 implements the inactive tenant registry/reader and local six-group database proof. See evidence/APP-013/tenant-sms-policy-registry/README.md. P1 is review-ready, not live publication/capture acceptance. Next proposed implementation is P2 after review, with consent/suppression integration and capture/sending still disabled. Older “next P1” wording below describes the original plan, superseded by this checkpoint; no additional planning-only loop or storage rewrite is required.

2026-09-12. APP-013 bounded reconciliation requested by the owner. Planning/checklist only; no implementation, publication, provider, spending or release approval is implied. Baseline inspected: backend c081fb0, governance 4119c4a, fetched focused branches. Account/public-site state was not refreshed this run.

## Decision summary

The fixture storage/retry proof is complete for its stated scope. Do not repeat it or promote its records into live consent. Two bounded engineering packages remain for the consent path: a trusted tenant policy registry, then production consent/suppression integration with delivery still disabled. Controlled activation belongs to existing milestone 3C after the prerequisite 2B/3A/3B acceptances; it is not a new milestone. These are work packages, not a promise of two remaining turns or completion of all APP-013 work.

Public policy approval/publication and provider readiness can be resolved alongside engineering. Do not block local tests on live public pages, and do not let fictional pages satisfy live gates. No new generic dashboard, policy crawler, messaging editor, email subsystem or marketing work is needed for this bounded path.

## Verified code versus remaining proof

| Area | Verified repository evidence | Remaining prerequisite / acceptance evidence |
| --- | --- | --- |
| Durable capture | durable-fixture-sms-consent.ts; separate encrypted FixtureSmsConsentState/Prompt; original-receipt retry, audit rollback, current recipient and policy revision checks | Production policy and suppression source; no fixture row or fixture receipt may become a real grant |
| Tenant policy | customer-messaging-settings.service.ts saves four event preferences with owner/admin and version checks | Preferences are not consent disclosure/publication approval. Add separately versioned reviewed policy content and an active policy reference |
| Live consent | sms-consent.service.ts reads/writes tenant/phone-hashed SmsConsentRecord and updates Customer.consentToText; STOP/START/HELP paths exist | Purpose-bound affirmative capture and provenance, shared revocation serialization, no stale replay after STOP, documented migration/legacy behavior and key compatibility |
| Delivery | sms-delivery.service.ts checks consent at queue creation and before provider send; processQueue checks smsDeliveryEnabled; registered provider/worker exist | Audit every send entry point, tenant allowlist/kill controls, current event and consent checks, capped attempts/spend, callback attribution and ambiguous-outcome ownership in the exact pilot environment |
| Public policies | PILOT_PRIVACY_AND_TERMS_DRAFT.md has approved public contact but unresolved editorial/publication blockers | Actual data-practice/retention inventory, appropriate legal review, owner-approved text/host/effective date, accessible version-matched public pages |
| Provider resources | MANAGED_COMMUNICATIONS_ARCHITECTURE.md records intended Signmons parent/client subaccount architecture and prior inventory | Fresh read-only account/resource/registration/rate evidence before approving exact setup or test actions; prior inventory is not current certification |

Important coupling: writing SmsConsentRecord can alter existing outbound eligibility even if a new capture response says deliveryAuthorized=false. Neither that response flag nor the queue-worker switch alone proves all sending is disabled. Production integration must prove isolation from every delivery entry point before any real capture is enabled.

## Package P1 — tenant policy registry (next proposed implementation)

Scope: a narrow communications-owned, server-side registry and reader using the existing owner/admin access/version/audit patterns. Reuse the current intake and shared SMS validation. Do not add fields to the four-event preference object or treat tenant display name as legal sender approval.

Reviewed version must bind organization, legal sender, transactional purpose, support contact, exact disclosure, disclosure version, Privacy Notice and Messaging Terms versions/approved URLs, effective time, review actor/time and evidence reference. Store immutable reviewed versions plus a versioned current pointer; do not overwrite the text an old receipt references. Organization comes from authenticated context, never a browser-selected ID. Opaque public slugs, if used later, are not internal tenant IDs or credentials.

States follow the existing proposed DRAFT → REVIEWED → PUBLISHED_VERIFIED → CAPTURE_ELIGIBLE contract, with suspension/replacement invalidation. Each transition needs audited evidence and appropriate actor authority. No state enables delivery. Local tests can inject fictional publication evidence explicitly marked non-live; that marker must never satisfy production eligibility. Real publication verification is a controlled review, not arbitrary URL fetching.

Acceptance: wrong tenant/role and impersonation denied; optimistic write conflicts refused; immutable version history; missing/unapproved/expired/suspended state refused; exact text/link/version projection; safe HTTPS host/path allowlist; no secrets/private representative information; replacement invalidates old prompts; no live consent/customer grant/provider writes. Define the additive schema/DTO mapping in DATA_CONTRACTS.md before coding. Stop with mocked/local evidence, not public publication.

Exit: a reviewed registry/reader that supplies policy identity to the existing capture contract while live capture and sending remain disabled. This package does not require buying a number or publishing on Eternity's website. Implementation approval is the next decision, not granted by this checklist.

## Package P2 — real-consent and suppression integration (after P1 review)

Reuse the demonstrated encryption, scope, deadline, audit and replay invariants; do not copy fixture evidence or merely remove fixtureOnly. Define the production evidence record and its relationship to the existing SmsConsentRecord before changes. Retain exact reviewed policy provenance and minimal protected recipient evidence, with a separately approved retention/key lifecycle. Fixture tables remain non-authoritative.

One documented transaction/locking protocol must cover initial opt-in, explicit revocation and provider keyword updates for the same organization/recipient. STOP wins against stale capture/retry; skip never revokes or restores an earlier choice; any restoration uses a separately permitted new affirmative flow. Stable tenant-bound phone hashing/key-version handling must match existing consumers and suppression lookup. An OTP, email choice, appointment event or customer boolean alone is not consent evidence.

Acceptance: simultaneous STOP/capture, stale capture after revoke, exact receipt retry, changed phone/policy/session, rollback/unknown commit/restart, legacy record rejection or explicit approved compatibility, tenant isolation and privacy-safe audit. Test the existing delivery consumers with a rejecting provider double and assert zero calls/queues where authority is missing. No real consent collection or sender activation during this package.

Exit: production-shaped integration proof with separate capture-release and send-release controls still disabled. Any required production migration/deployment is a distinct reviewed action, with backup/rollback and retention qualifications; disposable-database tests do not authorize it.

## Owner and operational gate checklist

Already recorded decisions (do not ask again absent conflict): Eternity Mechanical Services LLC as pilot; U.S./Cuyahoga County scope; public support/privacy contact ben@eternityhvacr.com; optional unchecked transactional SMS with a no-text service path; existing number retained for staging; separate 216 pilot number preference; Signmons-managed Twilio client separation. These are directions, not proof resources or registration exist. Private representative details remain outside this repository.

- [ ] Policy owner + appropriate reviewer: approve accurate data collection/subprocessors, session storage/cookies/analytics/recording state, data-class retention/deletion and the completed notice/terms. No universal retention period is selected here.
- [ ] Owner: choose the public policy hosting surface and effective date. Proposed approach: Signmons-managed, clearly Eternity-branded tenant policy pages, keeping clients out of provider dashboards. Exact domain/routes remain undecided; neither Signmons nor Eternity publication is authorized here.
- [ ] Implementer + owner: verify approved public pages without authentication and record exact versions/content, host/path and review evidence. No placeholder URL or fictional page qualifies.
- [ ] Operator: refresh the existing Safari Twilio session read-only; reconcile exact parent/subaccount/tenant, chosen number, required registration, callback ownership, credential isolation and approved sender. Keep the staging number unchanged; no new tab required.
- [ ] Owner: separately approve each exact resource creation/purchase, registration submission, DNS/secret/IAM change or deployment, with current account-specific prices and rollback. Do not infer approval from the area-code preference or public price lists.
- [ ] Operator + owner: name the allowed recipient, account/sender, purpose/template, time window, maximum sends/attempts and absolute spend limit; verify STOP/HELP support ownership and stop/incident controls. Previously confirmed participation need not be re-requested, but exact allowlist evidence remains private.
- [ ] Operator: demonstrate current finalized appointment + eligible recipient + current consent, authenticated callbacks, delivery/history and no duplicate logical send; stop on ambiguous provider outcome, attribution error, cap breach or revocation. Owner confirms actual receipt for 3C acceptance.

These are release prerequisites, not statements of current legal compliance or provider rules. Re-verify applicable official provider requirements and account status when preparing the actual setup/submission packet. This source audit makes no fresh pricing or compliance claim.

## Existing steel-thread placement and finish line

P1/P2 support 3C consent readiness; they do not advance the current 2B milestone. The remaining accepted workflow sequence is still: 2B controlled verification → 3A Sandbox payment → 3B test-calendar booking → 3C received confirmation → 3D change/cancel/recovery. County source qualification, verification account approval and bounded spend remain separate 2B gates; this SMS checklist does not solve them. Native Twilio Email remains a separate MVP channel, not a dependency added to this SMS walkthrough.

Acceptance remains 3/8 (37.5% of milestones), five milestone acceptances outstanding. This is not an overall MVP engineering estimate or calendar ETA. No new denominator, ticket transition or feature scope. Stop after this plan is review-ready; next proposed implementation is P1 only, after owner approval. No further planning-only loop is needed unless a concrete new blocker changes this contract.

## Evidence and review

Inspect backend c081fb0 and evidence/APP-013/durable-fixture-sms-consent/README.md for completed proof. Source checks this run examined the durable adapter, communications module, event-preference service, live consent service and delivery consumer. No runtime changed, external account was inspected, legal text approved or migration executed in this reconciliation.

Review the gap table, P1/P2 exit criteria and owner gate checklist. Governance docs-consistency/execution-placement and both repository whitespace checks apply. Prior 1,917 tests and 14 database groups remain historical runtime evidence, not fresh test results from this planning-only run.
