# Signmons customer experience: bounded design

Owner requested “proceed” after the proposal and existing-code comparison. Authorized deliverable: this design, not code, a live test, vendor integration or a changed execution queue. Source baseline: backend3cf8a9d, governance8d7c644 with the preceding proposal/handoff edits preserved. Companion: SIGNMONS_CUSTOMER_EXPERIENCE_PROPOSAL_20260929.md.

## Customer flow

The opening screen asks “How can we help?” and presents three labeled cards with an illustration, a one-sentence explanation and one action. Use progressive questions with Back, an unsure option and preserved in-tab answers. Keyboard operation, readable labels and a compact mobile layout are required. Illustration captions identify equipment type; product/model imagery appears only when supplied or licensed for the contractor's actual offering.

| Choice | First useful result | Intentional handoff |
| --- | --- | --- |
| Book a repair | Applicable service-call fee, what it covers, when it is collected, and any supported surcharge disclosed before commitment | Continue to protected intake; confirm an appointment only after the existing authorized booking path actually succeeds |
| Get a free replacement estimate | An approved planning range before asking for name, phone, email or exact street address | “Request a site assessment”; explain that this requests follow-up unless a separately supported appointment can actually be confirmed |
| Get a free second opinion | Explain what the contractor will compare and that submitting a quote is free | Submit the quote to the contractor's designated reviewer; display a truthful receipt, not an immediate promise of a better price |

Estimate question order: property type → equipment to replace → existing system/fuel → replacement versus conversion → size band only if the approved pricing table requires it. Equipment choices are contractor-enabled furnace, central AC, heat pump, ductless, boiler and unsure. System age is optional unless a pricing rule actually uses it. Do not ask unnecessary questions merely because a competitor does.

Residential supported replacements can receive a range. Commercial, managed-property or unfamiliar configurations receive a custom-review option when there is no matching approved rule. Do not disguise a missing price as a zero-dollar estimate or reuse residential rules for commercial equipment. Approximate area is a pricing input, never a final equipment-sizing decision.

Result layout: selected equipment image; “Estimated project range”; approved low/high amount; included scope; exclusions/assumptions; “Final price confirmed after assessment”; edit-answers and request-assessment actions. No invented monthly payment, rebate, efficiency saving, availability or product recommendation. Missing/incomplete rules produce “We need to review this project to give you a useful estimate.”

## Contractor pricing and images

Recommended first design uses an approved, versioned table maintained by the tenant's authorized administrator. Reuse the inspected organization draft/approval pattern as a design precedent; do not append fields to its strict validator without a separate reviewed change. No new general pricebook or admin application is proposed in this slice.

Proposed catalog entry fields: tenantId, catalogVersion, offeringId, customerLabel, equipmentType, supportedPropertyTypes, imageAssetId, altText, imageRightsSource, includedScope, exclusions and active status. Store image references to approved assets; do not accept arbitrary customer-supplied asset URLs. Never copy competitor equipment images. Generic illustrations must be labeled as illustrations; an image cannot imply an unoffered brand/model.

Proposed pricing-rule fields: ruleId, catalogVersion, effectiveFrom/effectiveUntil, matching answer values, currency, lowCents, highCents, approved adjustments with conditions, scope/assumptions, approvedBy and approvedAt. All amounts use integer cents with validated low<=high and nonnegative approved bounds. Publish only customer-facing amounts, not supplier costs or margins. Tenant identity comes from a trusted public storefront binding, not a client-selected tenant claim.

Deterministic evaluation: validate supported answers → load current approved catalog → find exactly one applicable base rule → apply only listed matching adjustments once → validate bounds → return range and assumptions. Zero rules, overlapping base rules, unsupported/unsure required inputs, expired approval or invalid amounts return NEEDS_REVIEW. AI may explain the returned facts but cannot invent or modify the numbers, scope, equipment sizing or approvals. Editing any pricing input recalculates; stale results cannot authorize a later job price.

Actual rule rows and approved asset files remain contractor inputs. Blank cells mean unavailable, never defaults. Required worksheet columns: equipment/project type; property type; fuel/system; required size band; included work; low/high installed range; approved adjustments; exclusions; image source; approval/version dates. No price amounts are fabricated in this design.

## Proposed data and state boundaries

These are conceptual contracts, not existing endpoints or final schema names.

- EstimateAnswers: bounded enumerated answers; no contact information, exact address, photos or free-text personal details. Proposed first implementation keeps them in browser memory only. Refresh/close clears them; do not promise cross-device or reload recovery.
- EstimateResult: RANGE or NEEDS_REVIEW, catalog/rule versions, currency/bounds when valid, scope and assumptions. Evaluation creates no customer, job, appointment, payment, provider request or durable anonymous lead. Redact request bodies from logs; any usage counters must exclude answers and identity.
- AssessmentRequest: created only after an intentional contact handoff. Carry the selected offering and untrusted estimate reference for server revalidation. Exact identity fields, retention and durable receipt must be specified at the existing intake integration boundary before coding. A planning range remains separate from a binding job price or payment policy.
- QuoteReviewRequest: a distinct lead/review purpose, not a disguised repair job. Proposed fields are tenant-bound request ID, verified submitter/session reference, contact preference, private attachment references, submitted time, review state and retention deadline. Creation, retry and receipt lookup use one idempotent request identity; uncertain acknowledgments retain that identity. No duplicate submission as a recovery shortcut.

Reuse current protected intake and current-proof admission only at the real job handoff. Existing customer-intake-draft.ts requires identity/address data; do not make its fields optional to accommodate anonymous browsing. Existing Job pricingSnapshot:{} is not an estimate catalog. Do not place an unvalidated client range into it. The precise estimate-to-job reference and retention mapping remain a design-to-implementation gate.

Free estimate follow-up must not silently bypass the existing paid-job calendar path. Recommended initial behavior is an assessment request with a clear pending-follow-up receipt. An actual free-visit calendar policy needs its own approved change; do not label a request “Booked.” Repair prices/collection timing remain the contractor's approved policy, not global Eternity defaults.

## Second-opinion handling

Recommended bounded first version: a human review of an uploaded quote, without automatic OCR, AI pricing judgment or an automated offer to undercut competitors. Compare model/capacity, efficiency, included equipment/labor, duct/electrical/permit scope, warranty and exclusions. Verify contractor credentials through an appropriate process before making a “verifiable licensed contractor” claim. Missing information produces a clarification request, not a favorable/unfavorable verdict.

Proposed limits for owner review: PDF/JPEG/PNG only, up to3 files and10MB per file; reject archives, executable content, encrypted/unreadable PDFs and format/signature mismatches. Uploads remain quarantined until validation/scanning succeeds. Reuse an existing approved storage/scan seam if established; none was found in this focused inspection. Do not provision a new storage service by inference.

Proposed access: submitter and explicitly authorized tenant owner/reviewer only; no cross-tenant access, public URLs, quote attachments in notification email or model training. Download access must be short-lived and authorized. Proposed retention is30days from submission, with deletion covering originals, derivatives and temporary uploads; minimal receipt metadata retention must be explicitly agreed. These limits are recommendations, not inherited Eternity policy or approved Signmons retention. A designated reviewer owns the response; do not display a guaranteed turnaround without their approved service commitment.

Proposed states: VALIDATING → QUEUED → IN_REVIEW → RESPONDED, with REJECTED/EXPIRED as explicit outcomes. A receipt says “Quote received for review” only after durable acceptance. It grants no booking/payment/send authority. Existing email/SMS delivery controls remain separate.

## Inspected reuse and implementation boundary

| Source inspected | Reuse / caution |
| --- | --- |
| src/communications/customer-intake-draft.ts | Existing property types and repair/installation intents; second opinion has no dedicated intent. Preserve strict identity validation. |
| src/communications/customer-intake-continuation.service.ts | submitControlled, previewDraft, protected review/admission and exact-request recovery; not an anonymous estimator or confirmed scheduler. |
| src/communications/customer-intake-page.ts and scripts/fixtures/customer-intake-journey.js | Existing served journey and browser fixture for integration tests; new customer UI must use the actual served application boundary, not a fixture promoted without review. |
| src/tenants/organization-profile.ts; organization-payment-policy.ts | Strict draft/approval patterns and fixed payment policy; not a versioned installation-price catalog or arbitrary after-hours matrix. |
| prisma/schema.prisma ServiceCategory | basePriceCents/emergencySurchargeCents exist; neither establishes replacement range rules, cost inclusions or permitted fee combinations. |
| src/communications/customer-intake-review.controller.ts | Explicitly local-composition-only and absent from production modules. Do not claim an existing production quote-review console or expose its approve route as an upload shortcut. |
| Focused src upload/storage search | Only multipart dependency security test identified; no established customer-quote upload/storage/reviewer flow. Full seam qualification required before code. |
| APP013_REMAINING_EXECUTION_CONTRACT.md | Preserve2B verified admission and3A→3B payment/calendar dependency. New lead/free-visit semantics require change control. |

Expected code areas, if separately authorized: existing served intake UI/composition, one isolated estimate validator/evaluator beside existing communications logic, a reviewed tenant catalog contract/approval seam, existing intake handoff, and a qualified private attachment/review path. No schema migration, public route, storage vendor, queue worker or admin UI is approved by this document. Exact changed filenames/routes/schema for unestablished seams cannot honestly be fixed yet; this card is a completed design deliverable, not implementation-ready authority.

## Finite delivery and validation plan

Design checklist completed: source/route inspection; three entry flows; deterministic pricing contract; image policy; identity/state/retention boundaries; reuse/gaps; proposed tests, exclusions and dependencies. Remaining implementation decisions are actual catalog/pricing assets, upload storage/scanning seam and retention acceptance, designated reviewer, free-assessment handoff, and placement in the owner-approved queue. Contractor administrator owns business inputs; implementer owns integration qualification; product owner owns material scope/order decisions.

After those decisions, one implementation card must name the exact patch and finite tests. Required cases: valid/unknown/unsupported answers; zero/one/overlapping rules; expired/changed catalog; amount boundaries and duplicate adjustments; edited answers; tenant spoofing; contact-free range display; no implicit job/charge/booking; trusted intake handoff; duplicate/concurrent/uncertain request receipts; foreign file access; malformed/oversize/infected files; failed upload cleanup and30-day deletion; keyboard/mobile/back behavior. Use existing current-proof, continuation and controlled browser suites for their existing responsibilities; do not weaken them or substitute mocks for database/query validation.

Current documentation checks: backend governance baseline and architecture, governance frozen baseline/consistency and21 safeguards, both whitespace checks. Future exact tests for new files belong in the implementation card; established commands include npm run lint, npm run build, npm test -- --runInBand, npm run arch:check and the existing governed disposable database/browser gate. No runtime test result is claimed for this design.

Proposed rollback: new entry/estimate/upload capabilities default disabled until release approval; disabling them preserves the accepted existing journey and durable request receipts, does not delete user files or holds, and continues approved retention handling. No provider integration, paid trial, cloud resource, live customer data, marketing publication, payment change or browser resubmission in this design.

Observable finish of this task: reviewable design and identified remaining decisions. Complexity is material, especially private quote review; no justified delivery estimate yet. Existing section2B/P06 remains12/14,R11/fullR12open;accepted1A/1B/2A remain3/8. No new acceptance denominator or queue promotion. No scope deviation in the authorized design work; proposed implementation expansion is disclosed above.
