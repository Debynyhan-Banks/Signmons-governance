# Google-only MVP service-area policy

## Owner approval — 2026-09-12

The owner explicitly approved replacing independent county-GIS qualification with Google-based business service-area qualification for the U.S.-only Eternity pilot covering all Cuyahoga County, Ohio. This is an approved requirements change, not implemented or live-accepted behavior.

This policy supersedes requirements for CEGIS physical-site/linked-road evidence, source-owner replies and CEGIS digests as mandatory MVP admission prerequisites in GOOGLE_ADDRESS_MVP_CONTRACT.md, REAL_VERIFICATION_ADMISSION_PLAN.md, DATA_CONTRACTS.md and COUNTY_FALLBACK_LIVE_GAP_ASSESSMENT.md. Those source assessments remain historical evidence, not launch gates. No new provider, adjacent-county coverage or parcel certification is authorized.

## Decision boundary

Use the existing Google Address Validation integration direction. The documented USPS county name and fipsCountyCode are candidate evidence, not guaranteed fields. No second geocoding API or county lookup is required by this policy. Official reference: https://developers.google.com/maps/documentation/address-validation/reference/rest/v1/TopLevel/validateAddress#UspsData .

- IN_AREA requires a valid physical service address, resolved required unit, explicit customer confirmation, consistent US/OH/Cuyahoga evidence and current tenant/session/address/policy bindings.
- Prefer structured USPS county code plus independently checked state/country fields from the same validated response; a bare county name, postal city, ZIP, customer claim or approximate map point cannot authorize coverage. Verify actual code format and normalize state/county deliberately; never assume a returned county code is a five-digit GEOID. Canonical target remains 39035.
- County code/name disagreement, absent required structured evidence, unresolved or conflicting address components, expired evidence, unsupported record types, PO boxes/private mailboxes and provider failures yield UNKNOWN. Preserve the draft and request correction or offer assistance; no routine manual approval requirement for clear qualifying results.
- OUT_OF_AREA requires otherwise valid, consistent evidence for a resolved location outside the approved area. An invalid address or missing evidence is UNKNOWN, not outside.
- Customer confirmation does not repair missing provider evidence, prove occupancy or confer payment, booking or messaging authority. Phone verification remains a separate current proof.

Google-derived eligibility is a business coverage decision, not independent physical parcel/boundary certification. Accepting this tradeoff removes mandatory county-GIS qualification; it does not guarantee every legitimate address will auto-pass.

## Privacy and implementation gates

No blanket caching or durable storage permission is inferred for USPS county fields, derived coverage outcomes or response IDs. Do not reuse the former CEGIS durable-digest exception for Google content. Retention matrix and Google case 75382710 remain unresolved where applicable. A local classifier may use fictional in-memory test inputs without retaining live provider content.

Live address dispatch, actual provider field qualification, approved request/cost caps, notices, retention handling, current-proof admission and controlled staging acceptance remain gates. No calls, deployment, credentials/IAM, charges or production actions are approved by this document.

## Next bounded implementation

Implement an authority-neutral, default-disabled Google service-area evaluator with fictional local tests, using existing adapter semantics rather than a new demo. It may return a proposed coverage classification but cannot set realVerificationAccepted, admissionAuthorized, bookingAuthorized or deliveryAuthorized. No raw provider persistence, new API client, schema migration or responseId cache. This independent section need not await the county or retention reply.

Acceptance cases: valid Cuyahoga; valid adjacent county; cross-county ZIP with structured county controlling; missing county code; code/name/state/country conflict; unqualified code format; missing/unconfirmed unit; PO box/private mailbox; correction invalidation; stale policy/session/revision; tenant mismatch; provider failure; all downstream authority false; no provider I/O or durable output. Before live use, confirm supported code formats and signals against approved legitimate-address evidence.

## Fixed progress and review

APP-013/2B remains Now. Real phone subcheck passed; closed phone proof must not be reused as current admission evidence. Walkthrough stays 3/8 (37.5%), not total MVP effort. No extra milestone and no queue change: APP-017 → APP-018 → APP-019 → APP-015 → APP-016 → APP-033.

Review this policy's source substitution, uncertainty behavior and retention limits together. Existing runtime remains unchanged until separately implemented and validated; county fixtures must not be relabeled Google or real evidence. No merge or release included.

Validation: cross-repository docs consistency passed; all eight execution-placement/intelligence-alignment regressions passed; both repositories passed whitespace checks. Documentation-only change: no fresh runtime test/build/lint or browser acceptance claimed. Focused feature branches retained; unrelated saved checkout changes untouched.
