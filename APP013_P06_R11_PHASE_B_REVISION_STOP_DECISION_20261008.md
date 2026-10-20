# APP-013 / 2B / P06-R11 — Phase B Cloud Run revision stop decision

## Verified stop

Owner-terminal replacement plan `bf1e1367-2c23-49d6-9230-b4ff4aaa4bb5`, operation `62cd3b76-4a8b-4aac-a642-c1a984e22221`, reserved at `2026-10-09T00:46:12.342Z` and stopped at `CLOUD_RUN_REVISION` at `2026-10-09T00:46:14.639Z`. Attempt/stop exist; no Cloud result exists. Never rerun.

The helper completed enough of the Cloud Run service stage to select a 100-percent traffic revision, then entered the revision stage. The receipt cannot distinguish revision-describe failure, response-shape drift or a disabled-flag mismatch. Artifact Registry and build provenance were not reached. Twilio was not inspected. No mutation occurred.

## Proposed observability correction

Alternative 1 is one fresh 20-minute owner-terminal metadata capture:

1. Bind new plan/operation identities to the same project, region, service, accepted image/build, future window and no retry.
2. Read the service once and immediately save only latest Created/Ready names, 100-percent traffic revision/percent and enabled-tag presence.
3. Read that revision once and save only image digest plus presence/value classifications for the six safety flags. A missing/non-false flag becomes `REVISION_DRIFT`, not an unclassified exception.
4. Independently read the accepted Artifact Registry digest and matching build provenance, saving only digest/status/match booleans. Command failure becomes a named sanitized stage category.
5. Return `CLOUD_ARTIFACT_QUALIFIED`, `CLOUD_ARTIFACT_DRIFT` or a precise sanitized stage failure and stop. Only a qualified receipt permits signed-in Twilio readback in the same approved window.
6. No database, secret payload, provider transaction, message/code, build, IAM, deployment, traffic/tag, activation, customer/job/payment/appointment action.

This changes observability only; it does not weaken any predicate or authorize continuation on drift. Any invocation, stop or uncertainty consumes it. Alternative 2 is pause.

Owner approval of Alternative 1 plus a future 20-minute Eastern window and signed-in Twilio confirmation is required before preparation/access. Phone ceiling remains 16 / USD 8.00 and runtime remains closed. P06 remains 12/14; R11/full R12 remain open; accepted milestones remain 3/8. No scope deviation.

Owner approved Alternative 1 for October 9, 5:45–6:25 a.m. Eastern and confirmed signed-in Twilio Safari. Fresh plan `75f6d775-6604-4356-a543-198bd83521d8`, operation `6f6ebdfa-849d-45ce-9499-d67ceaf4d2d6`, is privately prepared at `/private/tmp/r11-phase-b-staged-20261009-0545`. Exact bindings, private modes, three failure-category checks, formatting and no-action preflight pass; no marker or external read exists. Owner invokes once from normal Terminal; Twilio remains conditional on a qualified Cloud receipt.
