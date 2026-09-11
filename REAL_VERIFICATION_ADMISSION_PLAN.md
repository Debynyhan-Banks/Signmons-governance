# Real verification to admission — approved direction

## Owner approval

The owner approved the proposed requirements and approval checklist, specified U.S.A.-only operation, and selected Eternity Mechanical Services as the pilot business. This approves the planning direction, not provider activation or production changes. No tenant ID, credentials or production environment is inferred from the business name.

The initial pilot remains English-language, supervised and tenant-isolated. Normal phone/address verification must be automated; staff assistance is for exceptions. Existing operator job review remains distinct from phone/address verification. Selecting Eternity as the Signmons pilot does not authorize changes to its website, marketing, live appointments or customer records.

## Required evidence

- Phone access: server-confirmed code verification bound to tenant, session, normalized phone and phone revision. U.S. destination eligibility must be checked explicitly; a +1 prefix alone is insufficient. This proves access, not identity, ownership, marketing consent or payment.
- Address: approved real validation source, structured address, explicit customer confirmation of corrections and unit handling. Limit to U.S. service addresses and Eternity's separately approved service area. A suggestion, geocode or ZIP match alone is not validated-address or occupancy proof.
- Coverage: deterministic evaluation of the confirmed address against current approved tenant coverage configuration. Missing, malformed, unsupported or uncertain evidence refuses positive coverage; no routing fallback grants it.
- Organization: exact approved business-policy version and reviewed draft. Unapproved edits must not silently replace approval; applicable approved changes require fresh review.
- Every proof retains a minimal source/reference, timestamps, status, relevant revision and explicit freshness policy. Encrypt sensitive retained data. Never persist plaintext codes in ordinary storage/logs or accept caller-supplied VERIFIED flags. Fictional evidence remains ineligible for real admission.

## Admission contract

Admission creates a job record; it does not authorize booking, payment, dispatch or messaging. At the write boundary validate current tenant/session ownership, exact reviewed draft, phone/address/coverage proof and applicable organization policies. Refuse expired, revoked, mismatched, uncertain or unsupported evidence. Atomically create one job with evidence references and audit; exact replay returns the original receipt, changed replay refuses. Do not call external providers while holding the database transaction. Bind the durable admission receipt before session closure; later receipt replay must not create new authority.

Phone/address corrections invalidate affected proof; unrelated edits should not require unnecessary re-verification. Keep payment-before-dispatch, scheduling, availability, consent and sending gates separate. Human exceptions must never relabel unverified data as verified; any exception authority requires an explicit separate policy.

## Recovery and cost requirements

Wrong/expired code, ambiguous address, outage and budget refusal retain customer progress with a clear next action. Unknown provider outcomes preserve the operation reference and potential cost; never automatically resend or assume rollback. Shared organization/session/destination/request-source limits must work across processes. Reconcile reservations against actual usage before releasing liability or replenishing allowance. Alerts and a tested stop switch complement, not replace, a hard cap.

Existing approved phone policy: $50 USD per organization/month, alerts at $25/$40, explicit approval for higher limits. This is not authorization to incur charges. Address-provider costs and the total live-test spending limit require separate approval. No new customer fees, overages or billing changes are authorized.

## Open implementation decisions

Before code connecting real proof to admission, specify and review:

1. Exact pilot tenant/environment and approved owner/operator roles; Eternity service areas, hours, emergency fallback and support owner.
2. Supported U.S. address types and destination classification, including treatment of territories, unsupported numbers, PO boxes and missing/unvalidated units.
3. Provider capabilities and binding, challenge expiry, proof lifetime, resend cooldown, attempt/rate limits and freshness/revocation semantics. Values must be documented and tested, not inherited accidentally from session expiry or invented as universal best practice.
4. Verification notice, terms/privacy links, retained fields, retention/deletion policy and authorized access. No legal-compliance certification is implied by this plan.
5. Real rate inputs, reconciliation/recovery procedures, address budget, alert delivery and kill-switch owner.
6. The exact next bounded implementation section and its acceptance tests. No new provider is selected by this document.

## Approval checklist

- [x] Requirements/approval-checklist direction approved by owner.
- [x] U.S.A.-only scope approved.
- [x] Eternity Mechanical Services selected as the pilot business.
- [ ] Resolve and approve the implementation decisions above.
- [ ] Approve one bounded implementation section; preserve disabled provider/admission defaults until gates pass.
- [ ] Before live testing: explicitly approve provider/account/service configuration, named participants and destinations, duration, total spending cap, alerts, reconciliation and stop switch.
- [ ] Pass negative, concurrency, crash/restart, privacy and provider tests; demonstrate the complete customer-to-admission journey.
- [ ] Separately approve merge/deployment and pilot acceptance. No production migration, IAM/secrets/billing change, real customer/appointment mutation or website change is authorized here.

## Governance and progress

APP-013 remains sole Now; Next empty; FE-014 paused. Backend runtime checkpoint remains 5fb4f36. This planning decision changes no acceptance result: APP-013 50% recorded scope / 0 of 12 accepted; onboarding 50% locally demonstrated / 0 of 6 accepted; pilot 0 of 12 accepted. No defensible overall engineering percentage or ETA. Next bounded work is to resolve the open pilot/verification decisions into an implementation-ready contract, not activate services automatically.
