# APP-013 / 2B / P06-R11 — Phase B normal-baseline predicate correction

## Demonstrated mismatch

Plan `75f6d775-6604-4356-a543-198bd83521d8`, operation `6f6ebdfa-849d-45ce-9499-d67ceaf4d2d6`, completed `CLOUD_ARTIFACT_DRIFT` at `2026-10-09T09:45:25.944Z`. All staged receipts exist and no stop exists. Never rerun.

- Service qualified: latest Created/Ready/100-percent traffic is `signmons-calldesk-staging-app013dbrot2`; `p06-intake-enabled` tag absent.
- Accepted artifact qualified: digest `sha256:6a7cb0cdb955632250b6d27a349ab1e59097adc44e5fc29d4e6d87848041e0c6` exists.
- Accepted build qualified: `dce97411-6f76-4d85-b86e-3f8aadc23c86` is `SUCCESS` and matches that digest.
- Active normal revision classification: image digest `sha256:37286933d882466b8592120f48eb69c34e14cdb5a23c1f37480e39a1e6ff933a`; development auth, Stripe live webhooks and SMS delivery are literal false; scheduling is present but not false; background-worker and old staging-phone flags are absent.

The helper incorrectly applied the six-literal-false controlled-candidate predicate to the normal service baseline. Existing evidence `p06-target-consumers-recovery.md` records the normal `app013bounds` baseline at the same image digest with scheduling true and SMS delivery false. Credential-recovery revision `app013dbrot2` is the current normal target, not a zero-traffic P06 candidate.

Local source confirms the distinct semantics:

- omitted `BACKGROUND_WORKERS_ENABLED` preserves existing worker behavior and evaluates enabled;
- omitted `STAGING_PHONE_TEST_ENABLED` does not equal `true`, so the old phone-test path is disabled;
- controlled-intake configuration requires all six named flags to be literal `false`, so it fails closed on this normal baseline;
- the verified child database runtime remains closed: both approvals false, runtime role NOLOGIN/limit zero/expired and zero sessions.

The drift result is therefore valid against the helper's stated predicate, but that predicate tested the wrong revision role. It does not prove artifact/build drift or active controlled intake.

## Proposed predicate correction

Alternative 1 accepts the completed staged Cloud receipts according to revision role:

1. Normal service safety: 100-percent `app013dbrot2`, no `p06-intake-enabled` tag, dev auth false, Stripe live false and SMS delivery false; normal scheduling/background behavior is recorded, not mislabeled as a disabled candidate.
2. Controlled-intake safety: rely on the already verified closed child approvals/role/sessions plus the source rule that this normal flag shape cannot load an enabled controlled runtime.
3. Candidate provenance: accepted image and matching successful build remain independently qualified but undeployed by this receipt.
4. Perform one signed-in Twilio metadata readback in a future 15-minute Eastern window: account active, one Verify service, SMS enabled, Fraud Guard enabled, United States SMS monitored, United States voice disabled and unchanged single verified-recipient classification. Never reveal/persist the recipient or open Save.
5. Save one combined sanitized Phase B result and stop.

Alternative 2 pauses. No Cloud rerun is proposed. Excluded: ceiling increase, provider transaction/message/code, database/secret payload, build, IAM, deployment, traffic/tag, activation, customer/job/payment/appointment action.

## Change control and validation

This is an explicit qualification-predicate correction, proposed before use. It changes no application behavior, acceptance criterion, section count or dependency. Owner approval of Alternative 1 plus a future 15-minute Eastern window and current Twilio sign-in is required before the Twilio read.

Owner approved the predicate correction and one Twilio metadata readback for October 9, 6:00–6:15 a.m. Eastern and confirmed signed-in Safari. Fresh plan `05cf17b8-ef41-4249-ab88-4c3e696683b3`, operation `46f1bf06-6d9c-48d0-9e72-93bad3d61ef5`, is privately bound at `/private/tmp/r11-phase-b-twilio-20261009-0600` to completed Cloud operation `6f6ebdfa-849d-45ce-9499-d67ceaf4d2d6`, seven Twilio classifications, no recipient persistence, no Save and no retry. No Safari/provider read or marker exists at preparation close.

The operation was reserved and completed in-window. Sanitized `twilio-result.json` is `TWILIO_METADATA_QUALIFIED`: account active; exactly one Verify service; SMS and Fraud Guard enabled; United States SMS monitored; United States voice disabled; exactly one verified recipient with unchanged classification. Sanitized `phase-b-result.json` is `PHASE_B_METADATA_QUALIFIED` and binds the result to completed Cloud operation `6f6ebdfa-849d-45ce-9499-d67ceaf4d2d6` with role-aware Cloud classification. No recipient, provider identifier or balance was persisted. No Save control was opened; no message, code, provider transaction or mutation occurred. Operation `46f1bf06-6d9c-48d0-9e72-93bad3d61ef5` is consumed and must never be rerun.

Local focused validation after source inspection: 43 tests passed; one managed-HTTP test could not bind `127.0.0.1` in the sandbox and timed out. Staging-phone and background-worker suites passed. No source code changed.

The approved metadata-only Phase B qualification is complete. P06 remains 12/14; R11/full R12 remain open; accepted milestones remain 3/8 because no connected customer outcome was demonstrated. Phone liability remains at its approved ceiling and runtime remains closed. No further external action is authorized. No scope deviation.
