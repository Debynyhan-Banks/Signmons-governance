# Section 2B controlled-verification entry checklist

Owner accepted 2A with “i reviewed continue”. Three of eight sections accepted; 2B is section four, blocked at entry, not demonstrated. This is the existing section's gate inventory, not a new implementation section. Runtime f8e35e8 is unchanged. Latest origins fetched; both focused branches were clean and aligned before documentation work.

## Recorded versus missing

### Participant confirmation and read-only account preflight

Owner explicitly volunteered as the participant and confirmed a U.S. mobile phone capable of receiving verification texts plus an authorized Cuyahoga County address. These participant prerequisites are recorded; do not ask them again. Exact phone/address remain uncollected and must be supplied privately only for an approved test. This is a user attestation, not provider verification or permission to send.

Read-only preflight: the Google Cloud console opened with Signmons selected. Enabled Address Validation API, account-specific billing/rates, quotas, key restrictions and approved nonproduction tenant binding were not verified. Twilio console reached its loading screen, not verified account readiness. Chrome then blocked automation because another extension UI was open; stop browser actions until the user dismisses it. No settings, secrets, billing, terms, permissions or provider operations changed.

Directory skill was consulted first. Installed Stripe CLI has no directory command; the public Directory page could not be retrieved. No plugin installation or CLI upgrade was performed during this read-only task. Official provider pricing pages supplied provisional reference rates instead, not account verification.

Official public reference rates checked September 11: [Twilio Verify](https://www.twilio.com/en-us/verify/pricing) lists $0.05 per successful verification plus $0.0083 per U.S. SMS. [Google Maps pricing](https://developers.google.com/maps/billing-and-pricing/pricing) lists Address Validation Pro's 5,000-event monthly free cap and $17 per 1,000 events in the first paid tier. Free capacity is billing-account aggregate, not a promised tenant entitlement. These do not establish actual account charges, remaining allowance, taxes or additional fees.

Draft lean test packet, NOT APPROVED: one named nonproduction tenant, owner as participant, one 30-minute supervised window; at most three SMS starts and ten direct address-validation calls; proposed separate $0.50 phone/$0.50 address authorization ceilings, $1 combined. Reference arithmetic assuming three successful one-message verifications and ten fully paid address events is $0.3449 before any additional fees. No number becomes runtime policy or a billing guarantee. If actual account rates/fees cannot fit enforceable conservative bounds, refuse calls and revise the packet before approval. No automatic resend, new account, subscription, paid lookup add-on, calendar write, payment or confirmation SMS. County/source qualification, exact resources/notices, control implementation, recovery owner and explicit approval are still required. This packet is incomplete and is not ready for live execution.

The two focused Outlook searches were repeated and again returned no matching messages for the GIS sender or CEGIS. No new county qualification evidence was located; no mail was sent or changed.

| Gate | Current evidence | Needed before live testing |
| --- | --- | --- |
| Prior sections | 1A, 1B, 2A accepted | No repeat acceptance required |
| Geography | U.S.-only; all Cuyahoga County, Ohio, GEOID 39035 | Actual eligible test address supplied privately; no ZIP substitution |
| County source | CEGIS source/field rules documented; positive physical-record allowlist not qualified | Source-owner clarification or separately approved authoritative qualification evidence, supported types, uncertainty/precision rules and terms |
| Participant | Owner confirmed participation, U.S. SMS-capable mobile and authorized Cuyahoga address | Exact test phone/address supplied privately after action approval; server checks still required |
| Environment and identity | Local fixture identity only; no production auth acceptance | Exact nonproduction tenant, operator identity and isolated provider resources; no inferred Eternity production tenant |
| Provider accounts | Adapter direction documented, no current account-readiness certification | Read-only confirmation of existing approved account/service/project identity and capabilities; separate permission for any changes; no secrets in chat or repository |
| Rates and spend | Existing monthly phone policy is not test spending permission | Current account-specific phone/address rates, separate and shared hard caps, maximum attempts and test window, stop/alert owner; explicit approval of final packet |
| Notices and retention | Mock notices and 1A/1B lifecycle evidence exist | Approved actual notices/terms/privacy destinations, test-data handling and provider terms; no claim of legal certification |
| Recovery | Mock expiry/retry/held-liability tests pass | Controlled-source reconciliation, uncertain-outcome ownership, functioning stop switch, no blind resend or unsupported refund |
| Acceptance | 2A fictional source-to-job evidence | Received code, confirmed valid address/qualified county and exactly one job through the same application boundary; negative/concurrency/recovery results |

## Read-only inquiry check

The historical session handoff records a county inquiry sent via Outlook September 11. Current connected Outlook searches for `from:gis@cuyahogacounty.us` and `CEGIS` each returned zero results, without pagination. No message was sent, modified or marked read. These bounded searches did not locate a response or the original inquiry; they do not establish absence across other accounts/folders/indexes. A supplied reply or the correct inquiry mailbox is needed to assess any county clarification. Do not describe the stale “draft only” source document as the latest send status.

## Strict next steps

1. Participant prerequisites are confirmed. Dismiss the blocking Chrome extension UI, then resume read-only account/environment checks. Do not publish phone, address, credentials or account-sensitive evidence.
2. Locate/review county clarification and qualify the exact supported source rules. No positive county outcome while this is unresolved.
3. Read-only inspect the named existing accounts and verify current prices/capabilities. Prepare a single explicit live-test approval packet containing exact resources, actions, destinations, duration, attempt limits, separate/shared monetary caps and stop/recovery owner. No guessed numerical budget becomes policy.
4. Only after the packet is approved, implement/compose the bounded controlled path and collect actual source-to-job evidence. No booking/payment/confirmation SMS is authorized by OTP test approval.

Current “continue” authorizes this readiness review, not a live test with unspecified resources or spending. Do not provision services, configure providers, handle new secrets, change billing, deploy, migrate production, modify real appointments or touch the Eternity website. If prerequisites remain unavailable, keep 2B blocked; do not count mocks as real completion or silently advance to 3A.

## Validation and progress

Documentation consistency, four execution-placement tests and diff checks apply. No runtime files changed, so backend/UI tests, builds, lint and browser QA are not rerun claims. Prior 2A runtime evidence remains historical: 99 suites/1,887 backend tests and 170 UI tests passed; intermittent Node exit 139 and existing toolchain warnings remain open. APP-013 local scope index 50%, accepted 0/12; onboarding local 50%, accepted 0/6; pilot accepted 0/12. No overall engineering percentage or calendar ETA.
