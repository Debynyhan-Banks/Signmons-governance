# APP-013 / P06 R11 correction-selection final-run request

Status: alternative 1 owner-approved for one no-retry build plus read-only qualification and conditional packet preparation from 8:00–8:45 PM Eastern on September 21. No execution authority exists.

## Demonstrated gap and completed local repair

Consumed plan `4be1b8c1-6c55-4190-aff9-272d2bb9179f` reached enabled20, real phone verification and a truthful `CORRECTION_REQUIRED` result with `jobCreated:false`. The page displayed the standardized suggestion but offered no selection control. The owner entered `DONE` before a corrected second preview/submit. The coordinator returned `R11_ATTENDED_COORDINATOR_CLOSED_BROWSER_DONE`; revocation readback is `REVOKED` and closeout is `CLOSED` with no failures. The plan must not be rerun.

Backend `f1ee1f3` completes the existing APP-013/2B correction-selection requirement. A valid suggestion now exposes one explicit **Use suggested address** button that copies the structured street/unit/city/ZIP into visible fields without a provider call or submit. The customer must still review, preview and explicitly submit. Overlong candidates remain unselectable. Focused/full tests, lint, build, architecture, a 14-case synthetic browser matrix and the guarded PostgreSQL 18 connected browser harness pass. The connected correction cases use exactly two synthetic address calls and create one fictional job only after the second explicit submit. No live action occurred.

## Why one more preparation decision is required

The prior immutable image does not contain `f1ee1f3`. The consumed live run may also have added one phone hold and one address operation. Current phone/address retained liability must be read rather than inferred. The next packet therefore needs a new immutable repair image plus one current provider/target/policy/participant/liability qualification. Those steps can be combined under one preparation approval to avoid separate build, refresh and packet loops. Execution remains separately approval-gated because it opens database LOGIN, activates approval, deploys a tagged zero-traffic revision and permits real provider/customer actions.

## Alternatives

### Alternative 1 — one consolidated preparation, then one execution approval (recommended)

For one owner-selected preparation window:

1. Build exactly backend `f1ee1f3` once with the existing `signmons-build` identity, `E2_HIGHCPU_8`, a 1,200-second timeout and USD1 operational allowance. Temporary scoped `storage.objectViewer`, `artifactregistry.writer` and `logging.logWriter` grants must be removed and read back absent. Tag the candidate `p06-r11-f1ee1f3`. No automatic retry.
2. Perform read-only Cloud Run, Twilio policy/recipient, participant-eligibility, tenant-policy and database retained-liability refresh. Do not send a verification code or provider request. Preserve every existing hold.
3. Prepare one fresh private packet only if phone liability is at most 3000000 micros and address liability is at most three valid operations / 300000 micros at account and tenant. Bind one future phone flow at 500000 micros under an account ceiling of 3500000 micros; bind address account and tenant to five operations / 500000 micros and keep the session at two operations / 200000 micros. Any invalid row, higher liability, active approval, target drift, participant mismatch, build failure or cleanup failure stops without a packet.
4. Return one exact plan for separate owner execution approval. No helper/action authorization, LOGIN, activation, deployment, provider request, verification code or browser/customer action occurs during preparation.

If separately approved later, the one-command attended coordinator will handle the exact LOGIN/activation/zero-traffic deployment/browser pause/mandatory closeout sequence. The owner will use **Use suggested address** if correction is returned, then separately preview and submit before typing `DONE`. No automatic retry.

### Alternative 2 — stop after the local repair

Retain backend `f1ee1f3` and the consumed enabled20 evidence. Do not build, refresh, prepare a packet or run another connected journey. R11/full R12 remain open and P06 stays 12/14.

## Impact and boundaries

Alternative 1 changes only the one-future-packet cumulative phone/address ceilings needed to preserve all observed holds and allow one initial address validation plus one explicit correction. It does not release holds, change per-operation costs, authorize payment/booking/dispatch/message delivery, merge, expose secrets, change IAM permanently or alter the acceptance denominator. Build and read-only preparation authority does not imply execution authority.

No scope deviation beyond this proposed bounded operational capacity decision. Owner selection of an alternative and a preparation window is next.
