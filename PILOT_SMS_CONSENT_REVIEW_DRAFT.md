# Eternity pilot SMS consent and messaging policy draft

2026-09-12 — review only. Not implemented, published, submitted or legally approved. Messaging supplements below are not a complete Privacy Policy or Terms of Service. Review against actual data practices and applicable law before publication; no compliance guarantee.

## Customer screen — proposed copy

**Eternity Mechanical Services LLC**  
Service request powered by Signmons

### Optional appointment texts

Mobile number: [customer-entered number; never prefilled with the owner's contact]

[ ] I agree to receive automated service-related text messages from Eternity Mechanical Services LLC about my request and appointments. Message frequency varies. Message and data rates may apply. Reply STOP to opt out or HELP for help. Consent is not a condition of purchase.

Privacy Policy [approved public URL required] · Messaging Terms [approved public URL required]

You can continue without agreeing to texts. This choice does not book an appointment or authorize payment.

Button: **Continue to review**

Design requirements: checkbox starts unchecked; full label clickable; keyboard and screen-reader accessible; links separately focusable; no forced consent or marketing bundling. Keep this step inside the existing protected Signmons request flow. Missing approved disclosure or policy links disables new SMS enrollment, not the underlying service request. A phone-access verification code is a distinct purpose and does not grant appointment-text consent.

## Intended state and evidence requirements — not implemented

- Checking the box only selects a draft preference. Persist consent through a separately authorized server operation, not a browser flag.
- Before persistence, revalidate current tenant/session, phone revision, sender, purpose and disclosure/policy versions. Refuse mismatches.
- Capture the displayed text/version, server timestamp, organization, recipient reference and request context under existing security/retention rules. Do not invent a retention period or collect extra IP/device data without a justified policy.
- Unchecked means no new grant; it must not erase a prior opt-out or silently revoke unrelated existing consent. A dedicated unsubscribe path owns revocation.
- A generic form submission, email consent, successful OTP or another client's consent cannot authorize this campaign.
- After successful persistence, show a saved-preference acknowledgment only. On failure, show “Your text preference was not saved. You can still continue with your service request.” Avoid claiming a send, booking, payment or completed request.
- Sending remains globally disabled for this section. Later delivery requires current eligibility and approved live controls, not historical consent alone.

## Messaging privacy supplement — proposed public wording

Eternity Mechanical Services LLC uses Signmons to manage service requests and related communications. For appointment texting, we use your mobile number, request context and consent record to provide requested updates and honor messaging preferences. Signmons and communication providers such as Twilio process necessary information to operate this service on our behalf.

We do not sell mobile numbers or SMS opt-in information, or share them with third parties or affiliates for their marketing or promotional purposes. Your SMS consent is specific to Eternity's service-related messaging and is not transferred to another business's campaigns.

Message frequency varies with your request and appointments. Message and data rates may apply. Reply STOP to opt out of service-related texts or HELP for assistance. You may request service without opting in to SMS.

**Publication blockers:** confirm service-provider roles/contracts, actual data categories and retention, security practices, privacy-request contact/process, applicable rights and the governing full Privacy Policy. Do not present this supplement as the complete policy or promise deletion that conflicts with necessary opt-out/audit retention.

## Messaging terms supplement — proposed public wording

Eternity Mechanical Services LLC offers optional service-related texts concerning requests, appointment confirmations, reminders, changes and cancellations. This program does not enroll you in promotional messaging. Enrollment is voluntary and is not required to purchase or request service.

Message frequency varies. Message and data rates may apply. Reply STOP to discontinue this program or HELP for help. You may also contact us using the published support contact below. A permitted opt-out acknowledgment may confirm your request; further program messages must stop. Carriers are not responsible for delayed or undelivered messages.

Texts do not by themselves establish a confirmed appointment, payment authorization or emergency response. Refer to the explicit booking and payment confirmation for those actions. Do not use this messaging program for emergencies; call 911 for immediate danger.

**Publication blockers:** approve the customer-facing support contact (do not automatically reuse a private registration contact), verified Privacy Policy URL, effective date and applicable full service terms. Confirm STOP/HELP responses actually match implementation before publishing.

## Draft campaign description — not submission evidence

Use case: customer care / service-related appointment updates, subject to provider classification review. Customers requesting service from Eternity through Signmons may choose a separate unchecked SMS checkbox. They may continue without opting in. Privacy and messaging terms links appear beside the disclosure. Consent is recorded for the specific business and recipient. No marketing or transferred consent.

This describes the intended flow, not an existing deployed flow. Do not submit it as operational evidence until implementation and accessible review evidence exist. List additional opt-in methods only if implemented, reviewed and actually used.

## Review and implementation acceptance checklist

- [ ] Owner reviews tenant-branded screen and both messaging supplements.
- [ ] Appropriate policy/legal review verifies wording against real practices.
- [ ] Public policy URLs, support contact and effective date approved; placeholders removed before release.
- [ ] Separately approve bounded implementation in the current APP-013 scope.
- [ ] Test unchecked/default, decline continuation, failed-save handling, version/tenant/phone mismatch, prior opt-out, replay/duplicate capture and keyboard/mobile behavior.
- [ ] Demonstrate no job, booking, payment, provider send or cross-tenant grant caused by the preference step.
- [ ] Independently authorize policy publication, registration submission, provider setup and controlled sending/spend.

Next proposed section after draft review: size and approve the existing intake's optional SMS preference/evidence integration, with mock-only tests and sending disabled. Publishing legal pages, changing Eternity's website, DNS and provider actions are separate approvals. APP-013 sole Now; Next empty; eight-section baseline and 3/8 accepted count unchanged.

## Sources checked 2026-09-12

- [Twilio: separate unchecked opt-in and accessible policy evidence](https://www.twilio.com/docs/api/errors/30925)
- [Twilio: consent and mobile-data sharing restrictions](https://www.twilio.com/docs/api/errors/30932)
- [Twilio: declining consent must not block the primary action](https://www.twilio.com/docs/api/errors/30931)

These support provider-readiness requirements, not a legal opinion or proof the proposed flow is implemented.
