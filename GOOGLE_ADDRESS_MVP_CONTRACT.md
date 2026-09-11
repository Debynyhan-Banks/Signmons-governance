# APP-013 Google-first address contract — review-ready proposal

Owner selected Google to minimize MVP cost and approved this planning section. This records requirements, not implementation or live-service authorization. U.S.-only Eternity pilot, all of Cuyahoga County, Ohio; no website work. Runtime remains 5fb4f36. This document supersedes earlier statements that no address-provider direction has been selected; no county source has yet qualified.

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

Before live UI use, review applicable billing-country terms, public privacy/terms notices, Google attribution and data sharing. This is an engineering interpretation, not legal certification. Do not send invented U.S. addresses to live Google validation: synthetic fixtures remain local mocks. Any live test requires separately approved legitimate addresses and participants.

## Cost and recovery controls

Live switch defaults off. No amount of free allowance authorizes enabling billing or API calls. A separate address budget, account/environment, alert recipient and stop-switch owner must be approved before activation; the $50 phone budget is not an address budget.

Before each call, atomically reserve worst-case paid-tier liability and request allowance at shared account, tenant and session levels. Do not rely on budget notifications as a hard stop. Concurrent identical requests share one operation; tenant/session/address revision and policy changes prevent unsafe reuse. No cross-customer cache. Uncertain timeouts retain liability and do not automatically retry; reconciliation resolves actual usage before release/reset. Track corrections and failed/abandoned journeys, not only admitted jobs. Provider requests stay outside admission transactions.

## Acceptance checklist and next section

- [ ] Qualify physical-county source and boundary uncertainty policy using noncustomer evidence.
- [ ] Approve exact retained-field matrix, expiry/purge behavior and customer notice.
- [ ] Approve address budget/account ownership and legitimate live-test scope separately.
- [ ] Local tests: corrected/missing unit, stale revision/policy, wrong tenant, OUT_OF_AREA/UNKNOWN, expiry, duplicate concurrent submission, timeout/restart liability and disabled-provider refusal.
- [ ] Privacy tests: forbidden response fields never persist; expiry and restore purge cannot resurrect content.
- [ ] Before real admission, demonstrate current phone/address/organization proofs atomically consumed; preserve existing verification blockers until then.

Next proposed bounded section is source qualification plus the exact retention field matrix, not another customer fixture feature or live activation. Implementation remains separately approval-gated. APP-013 sole Now, Next empty, FE-014 paused. APP-013 50% recorded scope / 0 of 12 accepted; onboarding 50% local / 0 of 6 accepted; pilot 0 of 12 accepted. No new acceptance or defensible overall percentage/ETA.

## Evidence and review

Documentation-only: no runtime/schema/dependency change, provider call, production data access, configuration, billing, merge or deployment. Review the unresolved checklist before treating this as implementation-ready. Run `node scripts/docs-consistency-check.mjs` and `git diff --check`; application tests/build/browser QA are not rerun for this planning-only change and prior results are not new evidence.

Official sources reviewed 2026-09-10:

- https://developers.google.com/maps/billing-and-pricing/sku-details
- https://developers.google.com/maps/billing-and-pricing/pricing
- https://cloud.google.com/maps-platform/terms/maps-service-terms (Address Validation section; verify applicable account terms before activation)
- https://developers.google.com/maps/documentation/address-validation/policies
- https://www.census.gov/programs-surveys/geography/technical-documentation/complete-technical-documentation/census-geocoder.html
