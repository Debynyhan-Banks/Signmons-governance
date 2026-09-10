# Automated verification connection map — 2026-09-10

## Scope and evidence

Read-only source audit at backend 511cd1a and governance 1218eb6, after fetching both origins. This completes the approved contract-mapping step, not implementation or provider acceptance. No external provider was researched, selected, contacted or configured.

## Existing contracts versus missing connections

| Area | Verified repository evidence | Reuse and boundary |
| --- | --- | --- |
| Phone transport | src/communications/twilio-webhook.service.ts: voice greeting, inbound consent keywords and SMS delivery status; package.json includes twilio | Existing transport is not a phone challenge/check service. No customer OTP flow found in application source. Do not route verification through appointment templates or assume existing credentials authorize new sends. |
| Customer session | src/communications/customer-consent-credentials.ts: purpose-bound signed tenant/conversation/session claims; explicit comment that possession is not identity/mailbox proof | Reuse session isolation patterns. A customer bearer is not proof of phone access; operator Firebase authentication is not customer phone verification. |
| Intake persistence | src/communications/customer-intake-continuation.service.ts creates address with random googlePlaceId, empty components and zero coordinates; admission flags NOT_VERIFIED | These are placeholders, not provider validation. Never use the field name, coordinates or customer-typed text as verified evidence. Preserve existing records; no migration authorized here. |
| Address/coverage schema | prisma/schema.prisma has PropertyAddress, ServiceArea and CustomerCoverageCheck | Useful storage foundations, not implemented autocomplete/validation proof. No application customerCoverageCheck usage was found. Schema alone does not close the workflow. |
| Routing | src/jobs/routing.service.ts matches active ZIP areas; no matching routing rules permits fallback | Reuse explicit configured-area semantics, not the fallback as positive coverage proof. Formatted-text ZIP extraction is not address validation. src/config/coverage.config.ts concerns test coverage, not geography. |
| Booking readiness | src/jobs/booking-readiness-preview.service.ts requires admission contact/address VERIFIED flags | Replace bare-flag reliance only after authoritative evidence binding is implemented. Phone, address, coverage, payment and availability are distinct decisions. No blocker is cleared by this audit. |

## First implementation slice: customer phone challenge in local intake

Proposed observable outcome: in the existing fictional customer browser journey, request a code, enter it, see phone access verified, correct the number and see the old proof invalidated. No staff verification step. Use an explicitly labeled deterministic local adapter for proof; it cannot establish live delivery or pilot acceptance. No production registration.

Keep the scope to request/check/resend/status plus durable session-bound challenge/proof and the browser controls needed to demonstrate them. Do not build a general verification framework, address adapter or booking transition in this slice.

Required contract boundaries before implementation:

- Server derives tenant and session from the existing customer credential; client cannot supply verification authority. Bind challenge and proof to exact canonical phone and current intake phone version, not merely a job ID.
- Separate provider-owned challenge verification from durable application state. Persist opaque identifiers and minimal timestamps/status; no plaintext codes in database, audit, URLs or ordinary logs. A local adapter must be unmistakably fixture-only.
- Request/retry uses one logical operation. An unknown send outcome remains pending/uncertain until reconciled, not automatically resent. Resend is explicit and bounded; concurrent checks cannot mint duplicate proof.
- Specify challenge expiry, proof validity, resend cooldown and shared per-session/per-destination abuse budgets as explicit reviewed policy. Do not inherit consent-token durations accidentally. Choose numeric values alongside the selected provider contract; none are approved by this audit.
- Wrong, expired, exhausted, unavailable and uncertain responses must have safe customer recovery. Exact phone edits invalidate prior challenges/proofs; unrelated edits should not force unnecessary re-verification.
- Server-authoritative proof is phone access only. No email verification, consent, identity, address, payment or booking authority. Do not set a customer-supplied VERIFIED flag.
- Existing admission closes the customer session and remains human-reviewed. Start proof collection before submission; a later separately tested admission connection must validate and transfer current proof. Do not promise post-close customer access or a fully automated booking journey yet.
- Web is the first proving surface; voice/SMS code entry and interruption behavior need explicit channel design before full-MVP acceptance.

Required proof: real local persistence plus browser request/check/resend/correction; wrong/expired/replayed code, concurrent operations, lost response, restart, cross-session/tenant refusal, shared attempt exhaustion, audit rollback and privacy checks. Browser demonstrates honest fixture status, no real SMS. Stop after one connected local phone outcome; do not automatically start address or provider activation.

## Following connections, not authorized implementation in this checkpoint

Address autocomplete/validation needs a provider contract, selected-address confirmation and structured result/provenance. Coverage must consume that result plus current configured service-area evidence and refuse unknown configuration. Bind address/unit changes and coverage-policy changes to invalidation; a matching ZIP alone cannot manufacture a validated address.

Real phone/address providers, delivery and costs require separate selection/configuration approval. Provider research should precede SDK/API decisions. No account secrets were inspected. Existing operator admission is a separate experience gap to reconcile explicitly, not a justification to require staff phone/address verification.

## Validation and progress

Source-only/documentation checkpoint. Governance execution-placement tests, docs consistency and git diff checks are the applicable gates; no runtime, browser, build or security rerun is claimed. Prior runtime results remain historical evidence only.

APP-013 sole Now, Next empty, FE-014 paused. APP-013 recorded coverage 50%, acceptance 0/12; onboarding local 3/6 (50%), acceptance 0/6; pilot acceptance 0/12. No new completion credit or engineering ETA. No merge/deploy, schema/migration, live code, provider configuration, real data, billing, IAM/secrets or charges.
