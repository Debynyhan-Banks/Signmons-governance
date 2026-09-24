# APP-013/P06 R11 phone capacity and provider-readiness decision

Status: alternative 1 owner-approved on 2026-09-23. Capacity policy is approved; the provider gate remains closed. No packet or live execution is authorized.

## Owner decision

The owner approved alternative 1: preserve all eight phone and four address holds and authorize exactly one future R11 packet at phone `flowUpperBoundMicros: 500000` / `accountCeilingMicros: 4500000`, address account/tenant six operations/600,000 micros, and session two operations/200,000 micros. No packet may be created until the Twilio provider gate passes. This decision does not authorize provider-account changes or any live action.

## Demonstrated current state

### Provider follow-up readback — 2026-09-23

Within the authorized read-only window, Twilio showed Signmons LLC's Primary Compliance Profile as Business / Approved and the account as Active. The Verified Caller IDs page showed exactly one retained verified entry, consistent with the existing private rebind to the sole verified recipient; no number was copied or persisted. After a fresh reload, the Verify Services page still displayed the account-level warning requiring an account upgrade and approved Primary Compliance Profile before sending to any recipient. The approved profile therefore resolves only one stated prerequisite; the contradictory sending warning keeps the provider gate closed. No setting changed, no provider request was sent, and no packet was created.

Consumed read-only operation `65007417-c4d1-41f9-baea-6d797a41c785` completed at `2026-09-24T00:29:07.981Z` with `CAPACITY_DECISION_REQUIRED`. The fixed tenant/category and organization/payment policy match, runtime and phone approvals are inactive, `p06_intake_runtime` is closed with zero sessions, and the participant binding matches the historical controlled scope. All rows are valid.

Phone liability is eight retained holds—one staging and seven controlled—totaling 4,000,000 micros. One future capped 500,000-micro flow therefore needs `accountCeilingMicros: 4500000`. Address liability remains four operations/400,000 micros at both account and tenant scopes; one session of at most two operations/200,000 micros fits account/tenant six operations/600,000 micros and session two/200,000 micros. All holds remain preserved.

Read-only Cloud Run evidence shows normal traffic remains 100% on `app013bounds`, the enabled-intake tag is absent, and the new image digest exists without deployment. The desired/latest template is still historical enabled22, but expired authority plus database revocation/closed-role evidence keeps it unusable.

Twilio is signed in. Console readback shows one Signmons Verify service, SMS channel only, United States SMS monitored by Fraud Guard, Voice disabled, and the existing controlled-test note. The console also presents an account-level warning that sending to any recipient requires an account upgrade and approved Primary Compliance Profile. Exact verified-recipient status was not re-established in this refresh. Provider eligibility is therefore `UNCONFIRMED`, not ready for packet creation. No setting was changed and no request was sent.

## Alternative 1 — approve one future capacity envelope, retain provider gate (recommended)

Preserve all eight phone and four address holds. Approve exactly one future R11 packet to use phone `flowUpperBoundMicros: 500000` and `accountCeilingMicros: 4500000`, plus address account/tenant six operations/600,000 micros and session two operations/200,000 micros. This is policy approval only.

No packet may be prepared until a separately authorized current provider/participant check resolves the Twilio upgrade/compliance warning and confirms the exact recipient remains eligible. If that gate passes, packet preparation still needs a fresh owner-selected window and read-only target/policy/liability refresh; execution requires separate exact approval and mandatory closeout. No automatic retry.

## Alternative 2 — pause without a new ceiling

Keep the repaired image and all evidence. Resolve Twilio account/recipient eligibility first, then revisit capacity. No packet or live run.

## Boundaries

Neither alternative authorizes LOGIN, activation, deployment, traffic change, database mutation, hold release, provider request, verification code, browser/customer action, secret/IAM/billing change, payment, booking, dispatch or message. Alternative 1 does not authorize an account upgrade or compliance-profile creation.

P06 remains 12/14; R11 and full R12 remain open; accepted 1A/1B/2A are unchanged. Implementer owns later read-only qualification after authorization; owner owns the policy decision and any provider-account action. No scope deviation implemented.
