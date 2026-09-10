# Address and service-area connection map — 2026-09-10

## Approved bounded scope

Source audit at backend 77c2744 and governance b37ae9b after fetching both origins. The latest handoff explicitly proposed inspecting/mapping address-validation and service-area evidence into the same customer journey. This checkpoint completes that mapping only, not address implementation or provider selection. No production or customer-data action.

## Existing code and reuse boundaries

| Existing source | Verified behavior | Safe reuse / gap |
| --- | --- | --- |
| src/communications/customer-intake-draft.ts | Address is a bounded customer-stated string, not structured validation. | Preserve draft; add selected structured address evidence separately. Text formatting cannot prove a location exists. |
| src/communications/customer-intake-continuation.service.ts:635–638,675–676 | Admission creates random googlePlaceId, empty components, zero coordinates and NOT_VERIFIED contact/address flags. | These are placeholders. Do not treat the column name, ID or coordinates as provider proof; no backfill or migration in this section. |
| prisma/schema.prisma:174–253 | PropertyAddress stores structured components/coordinates; ServiceArea holds versionable updatedAt and JSON definition; CustomerCoverageCheck links address and optional area with status/reason/time. | Schema is available, but no customerCoverageCheck runtime usage was found under src. It requires a PropertyAddress, whereas the protected draft exists before job admission. Do not silently create master address/customer records merely to store pre-admission evidence. |
| src/jobs/dto/save-service-area.dto.ts; src/jobs/routing.service.ts:164–214 | Existing audited, tenant-scoped service-area writes support ZIP definitions with US postal-code validation. | Reuse configured active ZIP areas; preserve owner/dispatcher permissions of existing endpoints. Do not invent a new geographic scope or overwrite configuration. |
| src/jobs/routing.service.ts:345–445 | Routing matches category/urgency/time and optional service area. No base matches yields covered:true and NO_ROUTING_RULE_CONFIGURED; a rule without an area can also match. | This is routing fallback, not affirmative customer service coverage. Keep routing behavior unchanged; a customer coverage decision must refuse missing geographic authority. |
| src/jobs/routing.service.ts:492–545 | ZIP comes from components or a five-digit regex in formatted text; matching compares first five characters of configured ZIPs. | Reuse only explicitly validated canonical ZIP semantics for the new path. Never infer a validated address from arbitrary formatted text. Non-ZIP definitions cannot be guessed into coverage. |
| src/jobs/booking-readiness-preview.service.ts:90–92 | Missing VERIFIED admission metadata keeps contact/address blockers. | New local mock results must not set these flags or clear blockers. Later authoritative proof transfer needs explicit validation. |
| src/config/coverage.config.ts | Test-coverage thresholds, not geographic service coverage. | Do not reuse for geography. |

Repository search under src found no geocoding/autocomplete/address-validation implementation and no customerCoverageCheck application consumer. This is a scoped source finding, not a claim about every historical branch or external system.

## Proposed next implementation: one connected local address outcome

In the existing customer journey, use an explicitly fictional injected address fixture: request suggestions, select one, confirm structured address/unit, and see a separate current service-area result. Reuse the protected customer-session boundary and configured ServiceArea rows. No provider SDK, account, API key or external call. No customer-entered validated:true/covered:true authority.

Separate two decisions:

- Address: NOT_CHECKED, NEEDS_SELECTION, NEEDS_CORRECTION, FIXTURE_VALIDATED, UNAVAILABLE. A fixture-selected candidate never proves a real location or occupancy.
- Coverage: NOT_CHECKED, FIXTURE_IN_AREA, OUT_OF_AREA, UNKNOWN. UNKNOWN includes missing/disabled/malformed/unsupported configuration or missing validated ZIP. Only an explicit matching active ZIP definition can yield the fixture in-area result.

These names describe the proposed local contract, not existing enums or an implemented API. Do not expand live geographic support beyond the existing US ZIP contract without approval. A ZIP match is geography only, not availability, trade capability, technician assignment, price, payment or booking.

Persist minimal encrypted session-scoped candidate/selection evidence rather than manufacturing PropertyAddress records. Bind to tenant, exact session, normalized input plus unit, candidate identity/source version, customer confirmation, address revision and selected service-area IDs/updatedAt plus definition digest. Use a stable snapshot of all relevant area configuration so newly added/disabled areas also invalidate a previous assessment. Recheck scope and policy before consumption; timestamps alone are not proof of currency.

Address or unit edits invalidate selection and coverage together. Phone edits do not rewrite address proof. Changed service-area configuration invalidates/requires fresh coverage assessment, not silently adopting historical positive evidence. Unknown provider/configuration outcomes retain the draft and offer correction/retry without a false positive.

Keep no job creation, admission metadata changes, routing behavior changes, booking, charge or delivery authority in this local slice. Human assistance remains an exception, not the normal address-verification requirement. Existing human-reviewed job admission remains a separate authority decision.

## Acceptance checklist for that implementation

1. Browser selects/confirms a fictional structured candidate and receives separately labeled address and coverage results.
2. Active configured ZIP match is the only positive local geographic result; wrong ZIP, no areas, inactive area, malformed/non-ZIP definitions and missing canonical ZIP refuse or remain UNKNOWN.
3. Address/unit change, stale candidate, stale area configuration and cross-session/tenant requests cannot reuse a positive result.
4. Exact replay does not duplicate persistence; concurrent edits and audit failure leave a consistent transaction.
5. Timeout/refusal preserves the draft; no phone/address verification, booking or sending authority is granted.
6. Mobile/desktop QA, clear/expiry/privacy checks, and retained existing customer journey regression.

## Decisions remaining before live address validation

Provider selection, actual supported geography, address-unit/deliverability semantics, licensing/retention, rate limits, costs and approved spending require a separate provider contract review. The $50 approved phone-verification ceiling does not authorize address-provider spending. A geocode or suggested address alone must not be labeled validation or customer identity.

No provider decision is required to implement the fictional local contract above. Do not stop that local work solely to ask for credentials or a live budget.

## Progress and review

Mapping only; no runtime or acceptance increment. APP-013 remains sole Now, Next empty, FE-014 paused. APP-013 50% recorded scope / 0 of 12 accepted; onboarding 50% local / 0 of 6 accepted; pilot 0 of 12 accepted. No overall engineering percentage or ETA.

Review the reuse table, strict separation of address and coverage, and six acceptance cases. After owner review, implement exactly the connected local outcome above; do not jump to provider activation or change routing fallback.
