# APP-013 phone-only staging test packet

Date: 2026-09-12. Status: REVIEW ONLY; NOT EXECUTABLE OR SEND AUTHORIZATION.

## Scope and finish line

One supervised owner-participant phone-verification test within existing 2B. A confirmed phone result must not authorize address validation, county eligibility, job admission, payment, booking or confirmation messages. Google calls and job admission remain disabled. No new MVP milestone.

## Resources and observed deployment

- Google project signmons, Cloud Run signmons-calldesk-staging, us-east5.
- Runtime identity: signmons-calldesk-runtime@signmons.iam.gserviceaccount.com.
- Read-only service description today: 100% normal traffic targets signmons-calldesk-staging-app013bounds. Latest ready revision signmons-calldesk-staging-app013smstest is separately tagged app013-sms-test. Latest-ready does not prove normal traffic or phone-test capability. Deployed image-to-reviewed-commit mapping remains unverified.
- Prior console observations in this conversation: Signmons LLC account ending c417 (full identifier intentionally omitted under repository push protection), Verify service VA9aee2b6f81cdf797d4af79e939ab04f0 named Signmons. Resolve and recheck the full account identifier privately against the console before execution, together with exact service, SMS-only, US-only and Fraud Guard.
- Signmons Dispatch MG40bd30c5806901f74aafdfc2179e26e7 and its staging number are separate Programmable Messaging resources, not the Verify service.
- Exact staging tenant UUID, authenticated operator binding and private destination allowlist are not yet recorded. Owner participation is already agreed; do not ask the owner to volunteer again.

## Proposed controls, not installed configuration

A single 30-minute UTC window, default-disabled server switch, one participant, one tenant, no automatic resend or alternate channel. Initial run: one START and at most five CHECK operations in one session, matching the existing durable component. Three total STARTs is only an outer proposed ceiling across separately approved attempts, not permission to resend in the same session. Stop after success or uncertainty. No automatic rerun after failure.

Proposed phone liability ceiling: USD 0.50, reserved atomically before dispatch with concurrent attempts included. Public reference pricing is USD 0.05 per successful verification plus USD 0.0083 per US SMS; this is not account-specific fee/tax confirmation or a provider hard cap. Missing authoritative rate bound, approvals, identities, expiry or budget must refuse. Retain uncertain liability; do not refund or retry based solely on a timeout.

Never commit credentials, OTPs, raw participant phone or session tokens. Record redacted operation identifiers, timestamps, result, reserved liability and stop evidence only. Revalidate current opt-in; do not override a prior opt-out or infer consent from phone ownership.

## Concrete execution gap and bounded next work

At backend e791fd3, DurableVerificationService explicitly remains inactive, without controller/DI/live bootstrap; CommunicationsModule does not register it or TwilioVerifyAdapter. The existing address budget review is not a live phone budget. The proposed packet therefore cannot truthfully be called executable.

Next implementation deliverable within 2B: a default-disabled phone-only staging entry point composing existing verification logic with authenticated tenant/operator/participant binding, approval expiry, atomic phone attempt/liability limits and an effective stop switch. Prove refusal, concurrent caps, replay and ambiguous-provider behavior locally before proposing a release. Do not add another generic fixture service or activate it during implementation.

Then identify the reviewed image/revision, validate the final private resource bindings and rate bounds, and request explicit bounded deployment/test approval with exact UTC window. No configuration change, release or SMS is authorized by this document.

## Acceptance evidence and separate blockers

Finish this subtest only with actual participant receipt, successful code check, redacted provider/application correlation, enforced limits/stop evidence, and proof that address/job/payment/calendar/confirmation paths remain off. Local tests alone are not live acceptance.

Google responseId retention and county source qualification still block full 2B admission, not preparation of this phone-only path. Earlier console observation recorded Google case 75382710 (temporary responseId retention), New/P4; no response or resolution is asserted.

Walkthrough remains 3/8 accepted (37.5% of milestones, not whole-MVP engineering completion). Remaining fixed milestones: 2B, 3A, 3B, 3C, 3D.
