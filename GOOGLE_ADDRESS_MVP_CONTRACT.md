# APP-013 Google-first address contract — review-ready proposal

## County record-type qualification outcome

Read-only review did not qualify a positive county allowlist. All 115,395 current US/OH/Cuyahoga records in the aggregate report validation required; physical Building/Unit plus Site Visit/Photogrammetry labels do not document accuracy. This does not prove bad data, but prevents claiming verified coverage. See CEGIS_RECORD_TYPE_REVIEW.md for 52-group aggregate evidence, candidate counts, exclusions and an unsent source-owner inquiry. County acceptance stays UNKNOWN; no provider configuration or live Google call.

Next decision: approve sending the narrow county GIS inquiry, or separately approve further source research. Google semantic matching can continue as a separate bounded mocked section without bypassing county. Documentation only; runtime unchanged at abde6a9. APP-013 sole Now; Next empty; FE-014 paused. APP-013 50% scope/0 of 12 accepted; onboarding 50% local/0 of 6 accepted; pilot 0 of 12 accepted. No overall estimate, merge, deployment, billing or real data.


## Disabled Google adapter checkpoint

Owner approved a disabled Google adapter with mocked tests and design defaults: permitted correction cache expires at session end or 24 hours; other Google fields stay in memory without explicit caching permission; abandoned drafts delete within seven days or sooner under existing session policy; Signmons automates deletion with the pilot owner accountable. Submitted business-record retention remains separately gated. These are documented defaults, not an implemented deletion job.

Implemented an unregistered fixture adapter only: default DISABLED, no HTTP client, credentials, cache, route, database writes or county resolver. All results keep addressVerified/admissionAuthorized false and county UNKNOWN. Evidence: backend evidence/APP-013/google-adapter/README.md. 19 focused tests and full backend 93 suites/1,772 tests pass, three existing skips; build/lint/architecture/diff pass. No UI change or browser QA applicability. Next proposed: strengthen response policy and qualify county record types, still without live activation. APP-013 sole Now; Next empty; FE-014 paused. APP-013 50% scope/0 of 12 accepted; onboarding 50% local/0 of 6 accepted; pilot 0 of 12 accepted. No overall estimate, merge, deployment, billing, live calls or real data.


Owner selected Google to minimize MVP cost and approved this planning section. This records requirements, not implementation or live-service authorization. U.S.-only Eternity pilot, all of Cuyahoga County, Ohio; no website work. Runtime remains 5fb4f36. This document supersedes earlier statements that no address-provider direction has been selected. The 2026-09-11 review below conditionally qualifies a county-source contract for owner review; it does not accept or activate it.

## 2026-09-11 source qualification outcome

Preferred county source: the official Cuyahoga County CEGIS `NCGIDE/Addressing_Sites_Streets` ArcGIS FeatureServer, service item `facc7d99a6ec40a5b01f5240455b9e6d`, using `SiteAddress` layer 0 plus `RoadCenterline` layer 1. The service identifies versioned point/road records with per-record edit time and GlobalID in WKID 102722/latest 3734. Site data includes structured country/state/county, unit, status, point/capture type and centerline linkage; road data includes left/right country/state/county, ranges and parity. Census Current/ACS26 identifies the canonical Cuyahoga County policy GEOID as `39035` with data as of 2026-01-01; Census address-range geocoding is not used as positive address proof.

Read-only, noncustomer aggregate evidence found 115,395 `Current` US/OH/Cuyahoga site records, but also 388,008 null-status, 3,949 pending, 232 temporary and 20 other records. Those groups reported validation status 2 (validation required, no calculation error), and one `Current` record combined US/OR/Cuyahoga. A separate road query returned explicit Cuyahoga/Lorain, Cuyahoga/Medina and Cuyahoga/Summit side differences. Therefore presence, county text, a point or a status alone cannot authorize coverage.

Conditional resolver rules:

- `IN_AREA` is possible only for one exact `Current` physical site match with US, OH and Cuyahoga, resolved unit requirements, unchanged address/policy revision and a current linked road whose left/right counties are both Cuyahoga.
- `OUT_OF_AREA` is possible only for the same quality of exact current evidence when site and both road sides agree on one non-Cuyahoga Ohio county. Absence never means outside.
- A cross-county road, any site/road disagreement, null/noncurrent status, validation error/unknown, duplicate or missing link, unsupported point/capture type, wrong state/country, unit ambiguity, source outage or stale edit identity is `UNKNOWN` with assistance.
- `VALIDATIONSTATUS` is a gate, not positive proof. The physical `pointtype` and `capturemeth` allowlist remains an owner-reviewed implementation decision; until approved, every record remains `UNKNOWN`.
- A future proof binds service item, minimum record edit identities, query time, address revision and tenant policy version into a keyed digest. Admission rechecks outside its database transaction. No source SLA/global immutable release is claimed; outage is `UNKNOWN`.

This is conditional technical qualification, not live-source acceptance. Exact public evidence and review steps are in backend `evidence/APP-013/address-source-retention/README.md`.

## Smallest customer flow

Manual structured address/unit entry -> server-side direct ValidateAddress request on submission -> explicit customer confirmation/correction -> independent physical-county eligibility -> current-proof checks at admission. No autocomplete session, map, bulk validation or validation on keystrokes. Corrections invalidate affected evidence. Missing or unconfirmed units cannot silently become verified. PO boxes and nonphysical service locations cannot pass as visit locations.

Google documents direct validation as Pro and Autocomplete sessions terminating in validation as Enterprise; this is not a field-selection distinction. Published Pro allowance: 5,000 monthly events free, then $17/1,000 in the first paid tier. With the entire allowance available, 6,000 requests cost $17 and 10,000 cost $85 for validation only. Billing-account usage is aggregated across projects; do not promise each tenant its own free allowance. Phone, infrastructure and any other API costs are excluded. Rates and actual account usage must be checked before activation.

## County qualification contract

IN_AREA requires confirmed physical U.S./Ohio/Cuyahoga evidence, current tenant coverage-policy version and an unchanged address revision. Reliable resolved outside evidence gives OUT_OF_AREA; uncertainty gives UNKNOWN, preserves progress and offers assistance. Postal county, ZIP, customer assertion, approximate geocode and routing fallback cannot grant membership.

A candidate resolver must identify source, dataset version/date, geographic identifier, coordinate system, address-match precision, boundary provenance and documented uncertainty behavior. A point-in-polygon result is insufficient when location uncertainty crosses the county boundary. Missing precision, boundary contact, conflicting sources or an unresolved unit/location require UNKNOWN. Do not invent a numerical buffer as a substitute for documented accuracy.

Census address geocoding is only a candidate: it derives positions from address ranges, so a returned county alone does not qualify it for this contract. No dataset has been downloaded or approved. Source qualification must demonstrate known inside/outside locations, a cross-county ZIP, misleading postal county, boundary/low-precision cases and outages. If it fails, report the smallest alternative and its cost rather than silently adding a provider. This is the remaining county implementation blocker, not a claim that county validation is finished.

## Retention and privacy contract

Separate customer-provided/explicitly confirmed address data from Google content. Record the confirmation event and exact address revision; confirmation does not establish occupancy or consent to messaging. Encrypt permitted sensitive data and use tenant/role-scoped access.

Under the cited non-EEA service terms, listed address components may be cached for downstream transactions for up to 30 days, then deleted or replaced with end-user confirmed/corrected data. Listed correction flags have a corresponding correction-purpose allowance. Latitude/longitude must be deleted within 30 days. Use earlier session expiry where practical; 30 days is a maximum, not proof freshness. Do not persist whole responses, unlisted USPS fields, verdicts or derived county outcomes on an assumed blanket permission. An explicit field-to-permission review is required before durable proof implementation. Hashing/encryption does not extend retention rights.

Proposed durable receipt contains only Signmons-generated operation ID, tenant/session references, address revision, confirmation time and policy version; any provider-derived status/reference requires its own reviewed retention basis. No Google raw response in logs, traces, screenshots, analytics, fixtures or backups. Purge design must cover replicas/backups and restore handling, not just the live row. Customer-data retention/deletion duration and accountable owner still require approval; no indefinite customer-data retention is authorized here.

Exact MVP matrix for owner review:

| Data | Persistence rule |
| --- | --- |
| Customer-entered address/unit | Encrypted in the existing session. After explicit confirmation/correction, create a customer-provided value under an approved Signmons customer-data policy; implementation remains blocked until duration/deletion owner are approved. |
| Google `formattedAddress`, `postalAddress`, component names and USPS standardized address | End-user-scoped transient confirmation cache only; expire at the earlier of session expiry or 24 hours, delete on abandonment, or replace with the customer's explicit confirmed/corrected value. Never durable/logged/backed up. |
| Google correction flags | Same transient cache and expiry, for correction display only; delete after confirmation. |
| Google latitude/longitude | In-process only for the current lookup; delete immediately after county resolution/failure. Never persist/log/back up. |
| Google Place ID | Although documented as indefinitely cacheable, retain none for this MVP; transient operation use only. |
| Google verdict/granularity/metadata/nonlisted USPS data/response ID/raw response/headers | In-process or isolated transient operation cache only; never durable; earlier-of-session-or-24-hour purge. |
| Raw CEGIS attributes/geometry/record IDs | Immediate decision only; never copied to durable customer/job data. Store a keyed source-snapshot digest, source name/version, checked time and derived county result. |
| Signmons proof receipt | Signmons operation/tenant/session references, address revision, customer confirmation/check/expiry timestamps, tenant coverage-policy version, source name/version, keyed CEGIS digest, canonical county GEOID and coverage outcome only. No address, coordinate or Google identifier. |

The 24-hour ceiling is deliberately shorter than Google's documented 30-day maximum and is not a proof-freshness promise. The cache must be isolated from backups and support restore-time purge. Public Terms/Privacy, Google Maps attribution and Google/USPS data-sharing notice remain live-use gates. `regionCode: US` and `enableUspsCass: true` are the proposed request settings; validation must be complete at premise/subpremise level, resolve required units, use acceptable USPS DPV signals and obtain explicit customer confirmation after corrections. Validation is not occupancy, county, identity, payment, booking or messaging consent.

Before live UI use, review applicable billing-country terms, public privacy/terms notices, Google attribution and data sharing. This is an engineering interpretation, not legal certification. Do not send invented U.S. addresses to live Google validation: synthetic fixtures remain local mocks. Any live test requires separately approved legitimate addresses and participants.

## Cost and recovery controls

Live switch defaults off. No amount of free allowance authorizes enabling billing or API calls. A separate address budget, account/environment, alert recipient and stop-switch owner must be approved before activation; the $50 phone budget is not an address budget.

Before each call, atomically reserve worst-case paid-tier liability and request allowance at shared account, tenant and session levels. Do not rely on budget notifications as a hard stop. Concurrent identical requests share one operation; tenant/session/address revision and policy changes prevent unsafe reuse. No cross-customer cache. Uncertain timeouts retain liability and do not automatically retry; reconciliation resolves actual usage before release/reset. Track corrections and failed/abandoned journeys, not only admitted jobs. Provider requests stay outside admission transactions.

## Acceptance checklist and next section

- [x] Technically qualify a conditional physical-county source and boundary uncertainty policy using noncustomer evidence; owner/live acceptance remains open.
- [x] Define the exact retained-field matrix and earlier-of-session-or-24-hour transient-cache ceiling; customer-data duration/deletion owner and notice acceptance remain open.
- [ ] Approve address budget/account ownership and legitimate live-test scope separately.
- [ ] Local tests: corrected/missing unit, stale revision/policy, wrong tenant, OUT_OF_AREA/UNKNOWN, expiry, duplicate concurrent submission, timeout/restart liability and disabled-provider refusal.
- [ ] Privacy tests: forbidden response fields never persist; expiry and restore purge cannot resurrect content.
- [ ] Before real admission, demonstrate current phone/address/organization proofs atomically consumed; preserve existing verification blockers until then.

Next proposed bounded section is owner decision on the conditional CEGIS rules, physical point/capture allowlist, 24-hour cache and customer-retention owner/duration before any adapter implementation. Address budget/account and legitimate live-test approval remain separate. APP-013 sole Now, Next empty, FE-014 paused. APP-013 50% recorded scope / 0 of 12 accepted; onboarding 50% local / 0 of 6 accepted; pilot 0 of 12 accepted. No new acceptance or defensible overall percentage/ETA.

## Evidence and review

Documentation-only: no runtime/schema/dependency change, Google call, production data access, configuration, billing, merge or deployment. Review the unresolved checklist before treating this as implementation-ready. Backend build/lint, 92 suites/1,753 tests with three existing skips, architecture, Prisma, two zero-finding audits and diff passed; UI lint, 170 tests, 16-page build and two zero-finding audits passed; governance consistency and four placement tests passed. The first sandboxed backend test run could not open loopback sockets; the permitted unchanged rerun passed. Responsive browser QA is not applicable to unchanged rendered code.

Official sources reviewed through 2026-09-11:

- https://developers.google.com/maps/billing-and-pricing/sku-details
- https://developers.google.com/maps/billing-and-pricing/pricing
- https://cloud.google.com/maps-platform/terms/maps-service-terms (Address Validation section; verify applicable account terms before activation)
- https://developers.google.com/maps/documentation/address-validation/policies
- https://developers.google.com/maps/documentation/address-validation/requests-validate-address
- https://developers.google.com/maps/documentation/address-validation/build-validation-logic
- https://www.census.gov/programs-surveys/geography/technical-documentation/complete-technical-documentation/census-geocoder.html
- https://gis.cuyahogacounty.gov/server/rest/services/NCGIDE/Addressing_Sites_Streets/FeatureServer
- https://gis.cuyahogacounty.gov/server/rest/services/NCGIDE/Addressing_Sites_Streets/FeatureServer/0
- https://gis.cuyahogacounty.gov/server/rest/services/NCGIDE/Addressing_Sites_Streets/FeatureServer/1
- https://tigerweb.geo.census.gov/tigerwebmain/Files/acs26/tigerweb_acs26_county_oh.html
