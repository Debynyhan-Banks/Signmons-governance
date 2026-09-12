# Single-SMS activation packet — 2026-09-12

PREPARED FOR REVIEW, NOT SEND AUTHORIZATION. Supersedes the obsolete missing-deployment/identity/secret rows in PHONE_ONLY_RELEASE_AUTHORIZATION_PACKET.md. Runtime remains disabled. No new feature section is proposed.

## Fixed resources

- Source d33ecd067cdb87054fbce8b3df63f757a28c0277; existing PR #21.
- Project signmons, region us-east5, service signmons-calldesk-staging; candidate tag phone-preflight, revision signmons-calldesk-staging-phone-d33ecd0.
- Image sha256:25e194acfd96299bb670de84e63b932d9dc69528e6f421ae42699f80fc9b3d75, reverified Ready in this preparation run. Activation configuration requires a new revision of this same image, not a rebuild or normal-traffic promotion.
- Isolated tenant a1adcfd4-15be-404b-9ac3-5edb1fda20f0; operator staging-phone-owner-20260912. Prior evidence records SUSPENDED/disabled; not activated or freshly queried this run.
- Dedicated session/digest secret versions 1 already mapped. Existing signmons-staging-twilio-auth-token must be mapped to STAGING_PHONE_TWILIO_AUTH_TOKEN using a verified, pinned enabled version after approval; do not rotate it.
- Expected Twilio Signmons LLC account ending c417 and Verify service ending 04f0. Resolve full identifiers privately against existing configuration before execution. Account identity confirmed in existing Safari console; service settings/geography/Fraud Guard not reverified this run. No new service/number/subscription.

## Exact proposed test

Owner only, previously confirmed destination ending 3183, full number reconfirmed privately at execution. One START/SMS; up to five manual CHECKs; stop on success, uncertainty or expiry. No resend, fallback channel or automatic retry. Proposed flowUpperBoundMicros=500000 reserves the full USD 0.50 application allowance, so a second held flow cannot fit. This conservative hold is not an account invoice cap or a new rate quote. Retain unknown liability; do not reset historical holds to permit another test.

Historical public PAYG reference: USD 0.0583 for one successful one-SMS verification (USD 0.05 + 0.0083). Taxes/adjustments and account-specific total remain unverified. Use a dated rateVersion only after refreshing the applicable source at execution; no assumption of free messages from dashboard marketing counters.

Proposed noticeVersion=owner-otp-test-v1: “I request one Signmons verification-code text to my confirmed test phone. This checks access to that phone only. It does not book service, take payment, or enroll me in appointment or marketing messages. Carrier message/data rates may apply. Do not resend automatically.” Owner must approve this notice/request before recording requested=true.

Policy fields must all be populated privately: version=1, tenantId/operatorId above, new sessionId/conversationId UUIDs for actual isolated staging records, exact accountSid/serviceSid, HMAC phoneDigest using dedicated digest key, startsAt/expiresAt epoch milliseconds, rateVersion, flowUpperBoundMicros=500000, noticeVersion. Database approval digest must match the exact canonical policy. Never reuse fixture IDs/evidence or commit phone/token/digest values.

Use a 15-minute policy window chosen when the participant and sign-in path are ready; mint the separate HMAC session only after the activation revision is ready. Effective lifetime is the earlier policy/session expiry. Do not silently extend the window or resend after deployment delay.

## Remaining readiness checks — complete before activation

1. Open the existing Verify service in Safari and verify service SID, SMS-only, US-only geography and Fraud Guard. Present account-specific warnings rather than bypassing them.
2. Qualify private Firebase sign-in for the exact isolated operator. The API requires a genuine Firebase ID token plus the separate HMAC session; the disabled passwordless identity alone cannot authenticate. No qualified bootstrap was found in the inspected execution scripts. Do not use emulator tokens, dev headers, production-owner impersonation or invent signing permissions. Select an existing supported sign-in method and enumerate any identity/IAM change for approval before making it. No password or bearer token through chat or repository.
3. Verify isolated tenant/operator state, exact session/conversation/customer relations required by the existing durable session loader, existing retained liability, pinned credential version and current rates. Creating these scoped staging records is part of the explicit activation preparation approval, not this read-only packet.

## Activation and closeout scope requiring approval

After readiness is qualified: enable only the isolated operator and tenant, create the minimum isolated session records, map the existing token secret, set matching policy/approval, and deploy the same image to the candidate tag with STAGING_PHONE_TEST_ENABLED=true. Keep BACKGROUND_WORKERS_ENABLED, SMS_DELIVERY_ENABLED, SCHEDULING_ENABLED and DEV_AUTH_ENABLED false, Stripe live mode false, zero normal traffic and existing webhook URLs unchanged. No build/IAM expansion inferred.

Supply credentials through a qualified private channel, show the notice, request one START, and let the owner enter the OTP privately. Record redacted outcome, not the OTP/token/raw destination. A provider APPROVED result grants no address/job/payment/calendar/notification authority.

Stop through the authenticated stop endpoint before expiry when possible. Verify database approval disabled, suspend tenant/disable operator and revoke sessions through approved exact-target cleanup; return candidate phone flag to false. If stop auth is unavailable, use the explicitly approved exact-tenant approval revocation fallback. No new send follows acknowledged stop, but in-flight requests may finish. Preserve audit/retained liability, do not erase records or rotate shared secrets to hide outcomes. Closeout permission must be included with activation, not left implicit.

No start, check, token issuance, identity/database mutation, provider configuration, IAM change or deployment occurred in this packet run. APP-013/2B remains Now; accepted walkthrough 3/8 (37.5%), not overall MVP percentage. Google/county admission gates remain separate. This is supervised backend OTP testing, not a completed customer-facing end-to-end UI.
