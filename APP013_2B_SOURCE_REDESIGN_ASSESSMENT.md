# 2B address/coverage source redesign assessment — 2026-09-13

Owner authorized a bounded assessment, not provider replacement, policy weakening or implementation. Baseline governance 6a7699d, backend 01e0bdf. No scope deviation in work performed; alternatives below are unapproved changes. Existing Google-only policy, frozen acceptance and 3/8 walkthrough status remain unchanged.

## Finding

Separating Google address correction from independent county qualification is architecturally possible, but is not yet a verified resolution of the complete retained-proof requirement. The current consumer requires valid physical address/unit plus current county evidence, not simply a customer-confirmed string. Removing durable Google county output alone does not establish permission for the retained address-validity/admission evidence. Do not promise that a redesign bypasses all provider terms questions.

## Bounded alternatives and disposition

1. Google correction + Census county lookup: Census documents coordinates calculated along address ranges and geography lookup over those coordinates. This is not evidence of exact physical-premise/unit validation or boundary precision. Current GOOGLE_ONLY_SERVICE_AREA_POLICY.md explicitly rejects an approximate map point as coverage authority. Therefore reject as a drop-in replacement. Using customer input independently would keep source provenance separate, but still requires an approved accuracy/UNKNOWN policy and retention qualification; do not feed Google coordinates/results to another provider assuming unrestricted reuse. No quote, uptime guarantee or live match accuracy established. No address was submitted.
2. Google-only short-lived/corrected data: Google's published table permits specified address/component data for 30 days with specified deletion/customer-confirmation replacement treatment. It does not expressly enumerate USPS county, responseId or our durable verification/admission proof. A shorter cache is not automatically permission for unlisted fields. This remains a partial design avenue, not verified end-to-end resolution.
3. Single independent address validator, assessed candidate Smarty US Street API: documentation includes DPV/address analysis and county_name/county_fips fields. Subscription agreement section 2.5 expressly permits storage and generally continued retention, subject to order/product restrictions; sections 1/2 restrict internal use and redistribution. Signmons' multi-tenant customer-facing use, reduced evidence records and any post-termination rights must match the actual license/order. The pricing page did not expose a verifiable applicable amount in the retrieved content. Price/minimum spend and product terms are unqualified, not zero. This is a credible candidate, not an approved or ready-to-buy solution.

## Implementation impact if a qualified replacement is approved

Reuse session/draft/customer confirmation, phone proof, durable reservation, current-proof consumer and one-job transaction. Replace only the address provider adapter and county provenance mapping, with explicit source/version/revision/time fields and validated PO-box/CMRA/unit/physical-address semantics. Update GOOGLE_ONLY_SERVICE_AREA_POLICY.md and the affected card/contracts through an owner-reviewed change record; frozen baselines must not be silently altered. Do not run both providers by default and incur duplicate latency/cost.

Expected affected seams: google-address.adapter.ts/google-service-area.ts provider-specific replacement; address-operation provider dispatch and rate binding; controlled proof source proposed in the existing card; admission provenance tests; existing correction UI only for changed provider fields. No replacement UI, CRM, payment, scheduling or database platform. Effort is not sized until exact licensed fields and failure semantics are qualified.

Recovery still requires durable session/revision-bound proof, retained unknown cost holds, no network inside admission transaction, expiry/edit/stop invalidation, duplicate/changed replay tests, and truthful UNKNOWN with draft preserved. Provider product claims do not establish physical occupancy or perfect county accuracy. No mock is live acceptance.

## Decision

Do not implement the hybrid as an assumed fix. The lowest rework path that avoids waiting for Google is a narrowly qualified single-provider replacement with explicit Signmons usage/storage rights and a price acceptable to the owner. Smarty is a candidate because its published agreement has an express storage clause, but licensing/price remain required evidence. No contact, signup, purchase or address request was made. An owner-approved provider inquiry or review of a concrete order is needed before recommending purchase; avoid replacing one unanswered permission assumption with another.

## Primary sources checked

- Census API: https://geocoding.geo.census.gov/geocoder/Geocoding_Services_API.html
- Google caching terms: https://cloud.google.com/maps-platform/terms/maps-service-terms
- Smarty field reference: https://www.smarty.com/docs/apis/us-street-api/reference
- Smarty agreement: https://www.smarty.com/legal/subscription-agreement
- Smarty pricing: https://www.smarty.com/pricing

Provider-directory skill was attempted first; installed Stripe CLI has no directory command. Used official documentation fallback; no CLI/plugin installation. Census copyright URL and assumed Smarty product-terms URL did not return usable content, so no rights conclusion is based on them. This is an engineering/license-gap assessment, not legal certification. No source policy or acceptance criteria changed.
