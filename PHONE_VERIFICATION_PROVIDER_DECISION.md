# Phone verification provider decision — 2026-09-10

## Recommendation and scope

Recommend Twilio Verify v2 with provider-generated SMS codes for the first real integration, subject to owner review. This is an engineering recommendation, not account activation, a purchase or approval to send. Existing CallDesk Twilio transport and installed SDK reduce integration divergence; do not reuse the fixture's public code or interpret FIXTURE_VERIFIED as evidence.

This bounded research checkpoint starts from backend fd8d08a and governance eec9c28 after fetching both origins. Existing source includes twilio 5.13.1, Verify verificationChecks.create({verificationSid, code}), verification creation, and explicit autoRetry options. No package upgrade is required merely to expose those calls. Account readiness, credentials, Verify Service SID, balances and production configuration were not inspected.

Provider-directory skill was attempted first. Installed Stripe CLI 1.34.0 lacks directory; it advertises a newer CLI. No install/upgrade was performed. Official provider documentation was used as a scoped fallback; no Directory listing or ranking is claimed.

## Alternatives and rationale

- Twilio Verify: purpose-built verification with SMS and other channels; recommended because the app already uses the Twilio SDK while guest phone access can remain separate from staff authentication. This is architectural judgment, not a guarantee of delivery or lowest cost. [Verify API](https://www.twilio.com/docs/verify/api)
- Firebase phone authentication: viable, but its documented web flow uses reCAPTCHA and signs the customer into a Firebase account. Invisible reCAPTCHA can avoid interaction, so this is not inherently a poor UX. Adopting it would require an explicit guest/customer identity design separate from existing operator Firebase roles. [Firebase phone authentication](https://firebase.google.com/docs/auth/web/phone-auth)
- Custom codes over general SMS: not recommended for this MVP. It would move code generation, lifecycle and recovery responsibility into CallDesk without addressing the remaining end-to-end proof. Existing general SMS templates are not a verification engine.

## Current published cost, not an approved budget

Twilio lists USD 0.05 per successful verification plus USD 0.0083 per US SMS. At those published rates, 1,000 successes with exactly one SMS each calculate to USD 58.30. Resends and failed/abandoned attempts can add channel charges. This is an illustrative US calculation, not a quote, spend cap or worldwide estimate; confirm destination/account pricing, applicable fees and taxes before activation. [Verify pricing](https://www.twilio.com/en-us/verify/pricing), [Verify billing explanation](https://www.twilio.com/en-us/user-authentication-identity/verify)

No pilot volume, spend ceiling or destination region is approved here.

## Provider semantics that change the local model

Default code validity is 10 minutes; another send inside the validity window returns the same code. Therefore do not label every resend as a new code or reset expiry from an assumed local timer. Local fixture's 5-minute challenge is not the provider default. [Validity and limits](https://www.twilio.com/docs/verify/api/rate-limits-and-timeouts)

Use VerificationCheck with the stored verification SID and customer code, and inspect status rather than legacy valid. An approved, expired or exhausted verification can later return 404. Thus 404 cannot establish success or distinguish those outcomes. Never use the manual approval endpoint as a substitute for checking the customer's code. [Verification Check](https://www.twilio.com/docs/verify/api/verification-check), [Verification lifecycle](https://www.twilio.com/docs/verify/api/verification)

Verify is not among the resources supported by Twilio test credentials. Local/mock evidence must remain separate from controlled real-recipient delivery testing. A trial does not mean no external action or no resource consumption. [Test credentials](https://www.twilio.com/docs/iam/test-credentials)

## Proposed application contract, not implemented here

1. Server-owned tenant/service/account binding; canonical phone, customer session and phone revision. The client supplies neither provider SID nor approval status. Keep a durable logical request ID and minimal provider correlation.
2. Reserve a request/check durably before a provider call; do not hold the database transaction across the network. Finalize its result with version checks and an audit. Explicitly disable SDK automatic retries for side-effecting operations.
3. Separate PENDING, APPROVED, REFUSED, EXPIRED and UNKNOWN. Provider acknowledgment is not SMS delivery. Only correlated provider check approval plus a committed application proof can establish phone access.
4. A response lost after local commit can replay its saved receipt without another provider check. If the provider may have approved but the application did not persist proof, retain UNKNOWN: never derive approval from a later 404. Design authenticated reconciliation or an explicit fresh challenge after the prior window ends; preserve intake details instead of forcing the customer to retype them. Prove this failure boundary before live acceptance.
5. Bind proof expiry and exact phone/version; a changed number invalidates old proof and delayed responses cannot resurrect it. Phone proof remains independent of messaging/email consent, address, payment and booking. Admission transfer remains a later explicit connection.

Do not turn the deterministic local class into a provider implementation by changing a constant. Keep fixture and real adapters unmistakably separate.

## Customer experience, safety and channel decisions

Use a clear “Text my code” action, numeric/autofill-friendly entry, visible destination, accessible errors, countdown-based resend and inline phone correction. Propose an initial 30-second resend delay with increasing backoff; production thresholds require explicit policy review and cannot be inherited wholesale from the fixture. [Twilio retry guidance](https://www.twilio.com/docs/verify/developer-best-practices)

Before sending, show the OTP purpose, “Standard message and data rates may apply”, and Terms/Privacy links. Record the request opt-in timestamp and notice version. Do not treat this as appointment-notification or marketing permission. Final business-specific terms and notice acceptance remain a launch prerequisite. [Verify opt-in policy](https://www.twilio.com/docs/verify/consent-opt-in)

Retain server-side session/destination/peer limits, destination-region restrictions and a spend circuit breaker. Require review of actual Fraud Guard configuration; never bypass it automatically after a refusal. Its SMS protections do not cover voice. [Fraud Guard](https://www.twilio.com/docs/verify/preventing-toll-fraud/sms-fraud-guard)

SMS is the first proving path, not removal of phone/SMS channels from MVP. Landlines, unsupported destinations, voice-call code entry and customer-selected fallback need explicit channel handling; do not claim all-customer automation from one mobile-SMS proof. No voice fallback is activated or priced in this decision.

## Smallest next implementation and stop point

After owner review of the recommendation, implement an inactive Verify adapter with an injected/mock SDK client: exact create/check mapping, strict response binding, sanitized error classification, no automatic side-effect retries, missing-config refusal and no production registration. Its tests must cover approved/pending/malformed/foreign SID responses, timeout/429/404 and zero logging of codes or full provider payloads. This is the next bounded coding section, not another broad provider survey.

Do not claim a complete durable network workflow from adapter tests alone. Connect durable reservation/finalization and browser recovery before any controlled delivery test. Activation additionally requires explicit account/service/credential approval, named consenting test recipients, allowed countries/channels, a spend ceiling, privacy/terms approval, and separate live-send authorization. No IAM, secrets, billing, real data or deployment changes are authorized now.

## Validation and progress

Documentation/source review only. Governance placement tests, docs consistency and git diff checks apply; no new runtime, browser or dependency-audit results are claimed. Prior local evidence is unchanged.

APP-013 sole Now, Next empty, FE-014 paused. Recorded scope coverage stays 50% / formal acceptance 0 of 12; onboarding 50% local / 0 of 6 accepted; pilot 0 of 12 accepted. No overall engineering ETA. Address/coverage, actual admission transfer and final self-service booking remain open.
