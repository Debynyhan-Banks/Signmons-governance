# Google field and retention qualification — 2026-09-12

Read-only official-document review after disabled evaluator implementation. No API request, account change or customer data. County GIS remains unnecessary under the approved Google-only policy.

## Confirmed and unresolved

Google's [REST reference](https://developers.google.com/maps/documentation/address-validation/reference/rest/v1/TopLevel/validateAddress#UspsData) defines county and fipsCountyCode as strings but does not specify code width. USPS fields may be incomplete. DPV Y covers primary/secondary confirmation; H denotes building/apartment. Missing metadata.poBox means unknown. The evaluator's three-digit format and strict explicit flags remain test assumptions, not a live acceptance claim. H-only intentionally excludes other potentially valid record types.

The [revalidation reference](https://developers.google.com/maps/documentation/address-validation/reference/rest/v1/TopLevel/validateAddress) requires follow-up requests to carry the first response ID. This establishes protocol use, not permission for arbitrary retention.

The published [service-specific terms, B.1.3](https://cloud.google.com/maps-platform/terms/maps-service-terms) enumerate limited caching permissions for address display components, correction flags and coordinates. They do not explicitly list USPS county fields, responseId or derived coverage outcomes. This is not a finding that immediate processing is forbidden. It means our proposed session cache/durable proof needs its own reviewed basis; no blanket 24-hour exemption is established. Applicable account terms still require confirmation. No legal certification.

## Smallest next action

Prepare a single legitimate-address, capped staging inspection packet for owner review: exact project/credential restrictions, address privately supplied/confirmed, no invented live address, no automatic retries, explicit cost/request ceiling, immediate response processing only, no response-body logs/cache/screenshots, sanitized field-presence/type/code-width findings, and stop after inspection. This packet is not execution approval. Review whether even sanitized retained findings contain provider-derived content before recording them. No new SMS, admission, payment or deployment.

The inspection can qualify wire shape but cannot settle retention rights. Draft an addendum for existing Google case 75382710 asking about (1) first-response ID held only for active correction flow, (2) immediate USPS county evaluation and (3) whether a minimal coverage outcome may be retained with Signmons-generated timestamps/revisions. Do not send without approval. No county inquiry or new provider selection needed.

No more generic fixture coding is proposed while these live-composition inputs are unresolved. APP-013/2B remains Now; walkthrough 3/8 (37.5%) unchanged. Real phone subcheck remains passed and closed.
