# Signmons customer experience proposal

Status: owner agreed to the direction and documenting a comparison with existing work. This is a product proposal, not implementation, release or replacement diagnostic approval. Prepared September 29, 2026. Backend inspected at3cf8a9d; governance at8d7c644. Existing APP-013 section order and acceptance criteria remain unchanged.

## Agreed direction

Give customers useful answers quickly through simple questions, equipment pictures and clear pricing. Present three starting choices:

| Entry point | Customer receives | Next action |
| --- | --- | --- |
| Book a repair | Clear service-call charge and what it covers, using that contractor's approved policy | Continue into the existing protected intake and the applicable booking/payment journey |
| Get a free replacement estimate | Preliminary planning range based on a few answers and contractor-approved prices, before requiring name, phone or email | Choose whether to request a visit to confirm the scope and final price |
| Get a free second opinion | A way to submit an existing contractor quote for comparison of equivalent work | Receive a reviewed response; no automatic promise to beat a price |

Free refers to the estimate or second-opinion service, not repair labor or equipment. Fees must be contractor-specific. Do not copy Eternity's business rates into Signmons-wide defaults or overwrite the restricted pilot policy.

## Proposed replacement journey for review

1. Ask whether the property is residential, commercial or managed; explain any unsupported scope honestly. Commercial or unusual systems can request a custom estimate when no approved range exists.
2. Show labeled equipment illustrations or licensed product photos: furnace, central air conditioner, heat pump, ductless system, boiler and an unsure option. Final supported categories depend on the contractor's catalog. Pictures aid recognition; they are not a sizing method.
3. Ask only questions needed by the approved pricing rules. Candidate inputs are equipment being replaced, existing fuel/system type, approximate home size and whether the project is a replacement or a conversion. Provide unsure options; the exact question set is not yet an implementation contract.
4. Display a planning range with the assumed scope, major exclusions and explanation of what the site assessment confirms. If answers are insufficient, explain why a custom assessment is needed instead of fabricating a price.
5. Offer a visit or human follow-up. Collect contact details at this intentional handoff and reuse required verification before a real job is admitted. A displayed range is not a job, booking, charge or promise of availability.

Suggested result copy, without invented amounts: “Based on your answers, your estimated project range is [approved low]–[approved high]. This assumes [scope]. A site assessment confirms equipment sizing, installation conditions and your final price.”

Proposed identity/retention boundary: browsing and preliminary calculation do not create a customer/job or require contact fields. Whether anonymous answers are transient or saved must be decided in the implementation card. Quote upload is a separate intentional submission; specify allowed files, size/type validation, private access, retention/deletion and human-review responsibility before implementation. No automatic publication or reuse of uploaded quotes.

## Existing implementation comparison

This is a focused source inspection, not a full repository absence audit or a live capability claim.

| Proposed behavior | Inspected existing seam | Gap or required decision |
| --- | --- | --- |
| Classify the request | src/communications/customer-intake-draft.ts already validates RESIDENTIAL/COMMERCIAL/MANAGED and DIAGNOSTIC/REPAIR/INSTALLATION/MAINTENANCE/OTHER | Three customer-facing choices require explicit routing semantics; second opinion is not a dedicated intent in that validator |
| Disclose a service-call fee | src/tenants/organization-payment-policy.ts supports approved fixed USD service-fee/deposit policy | Inspect the actual presentation and ensure one coherent policy; do not infer a complete property-type/after-hours fee matrix or pay-at-visit support from these fields |
| Protect a submitted job | customer-intake-continuation.service.ts and APP013_REMAINING_EXECUTION_CONTRACT.md section2B provide reviewed intake/current-proof admission | Preserve tenant/session/phone/address/policy verification, exact-request recovery and no downstream authority from job creation; R11 remains unresolved |
| Show a range before contact details | Current CustomerIntakeDraft requires customerName, phone and address; admitted job is written with pricingSnapshot:{} in the inspected service | Cannot achieve this by merely relabeling the protected intake. Need a bounded preliminary-estimate contract and contractor-approved price rules/catalog/versioning |
| Show system images/options | Current protected journey fixture inspected; no equipment-catalog flow identified there | Need approved assets, accessible labels and a defined supported catalog; no copying competitor assets |
| Review uploaded competitor quotes | No estimate/quote/upload/catalog-named source file located in the focused src filename search | No reusable end-to-end upload/review path established by this inspection. Determine existing storage/review seams, confidentiality and retention before selecting an implementation |
| Schedule after the customer chooses to continue | Remaining contract3A covers payment and3B covers the paid-job calendar path | Free-estimate appointments may need a distinct approved policy. Do not silently remove the existing payment prerequisite or treat an estimate lead as an accepted paid job |

## Reference evidence and limits

In the previous browser exploration, Martinov's shop identified Contractor Commerce and required an address before its questionnaire. It described a later home visit to confirm job details and adjustments. No address permission was received in that exploration, so equipment images and the final price range were user-reported, not independently reproduced. Its separate ServiceTitan Scheduling Pro path exposed ZIP, service type, equipment age, equipment type and scheduling; a sample replacement path showed no timeslots and a call option. No contact submission or appointment was made. An agreement to this product direction is not permission to transmit the business address.

References: https://www.martinov-homesolutions.com/shop/#/journey/h_v_a_c_system_quote ; https://book.servicetitan.com/m/mk5okzcb5rl4fn11da0zjc7r ; https://www.contractorcommerce.com/pricing/ . Vendor pricing and marketing claims are not requirements or proof of Signmons capability. No vendor subscription is proposed here.

## Change proposal and next decision

Demonstrated gap: the inspected protected intake requires identity/address data and does not establish the requested anonymous visual estimate or quote-review flow. A front-end relabel alone would not deliver the agreed experience.

Alternatives: (A) retain the proposal while completing the existing accepted-scope journey; (B) approve a bounded design/change card for the estimate/catalog and quote-review additions; (C) separately evaluate a vendor integration against costs, data ownership and current architecture. No alternative authorizes a subscription or external action.

Recommendation: retain the three-entry experience as the product direction and complete a bounded design card before any code expansion. It must name catalog/pricing owner, price-rule inputs and limits, approved image sources, lead-to-job handoff, free-visit policy, quote-review owner, file/privacy/retention boundary, existing interfaces, finite tests, dependencies and exact changes. Size and delivery effort are not yet established; do not promise a small UI-only change.

Planning checklist completed: capture agreed direction; inspect existing relevant seams; identify reuse/gaps; state data/authority boundaries; propose next decision. Remaining: owner selects placement of the bounded design work, then implementer completes the design card; implementation remains unapproved. No new acceptance section, queue promotion or deadline. Existing2B/P06 remains12/14;R11/fullR12open;accepted1A/1B/2A remain3/8. Current unresolved request and consumed diagnostic are preserved; this agreement does not authorize a replacement read. Proposed scope additions are disclosed above; no implementation deviation occurred.

## Bounded design delivered

Owner requested “proceed” with the design. See SIGNMONS_CUSTOMER_EXPERIENCE_DESIGN_20260929.md for concrete flows, proposed contracts, retention/access recommendations, inspected integration limitations and finite validation plan. Design is complete; implementation depends on the explicitly listed business/data/integration decisions and a complete approved change card. No application or live changes.
