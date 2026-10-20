# APP-013 / 2B / P06-R11 — enabled33 refusal diagnostic decision

## Decision status

Decision-ready local/source review completed October 2, 2026 after the owner authorized bounded diagnosis at 10:23 a.m. Eastern. The owner then explicitly approved the four-category local diagnostic repair and listed tests. Local implementation and validation are complete; no live database query, cloud-log query, provider call, deployment, allowance change, new packet or browser replay occurred. The consumed enabled33 package remains closed and must not be rerun.

## Section and acceptance criterion

This remains internal 2B work under APP-013/P06-R11. It serves the existing criterion that invalid, uncertain or stale intake input must preserve customer progress without creating a job, while recoverable input requests a correction and the connected journey produces an observable truthful result. It does not add a section or change the 2B finish line.

## Inspected evidence and exact source

- Exact deployed source: `0a857edcc88a6da36dc6669382a74546173e480b` at the clean isolated checkout `/private/tmp/signmons-submit-host-candidate-20261001`.
- Browser evidence: the owner screenshot recorded in backend `evidence/APP-013/p06-r11-enabled33-refusal-closeout-20261002.md`; private address and phone are not copied here.
- UI projection: `scripts/fixtures/customer-intake-journey.js` clears and then populates `#controlledSuggestion` only for `CORRECTION_REQUIRED`. The screenshot shows neither the “Suggested address” paragraph nor its action, so the displayed response is the generic `REFUSED` branch with `jobCreated:false`, not the correction branch.
- Verification service: `src/communications/controlled-intake-verification.service.ts` intentionally collapses several conditions into the same generic refusal, including unusable provider semantics, non-`IN_AREA` coverage, unavailable correction sequence state and an unretainable correction response identifier.
- Service-area review: `src/communications/google-service-area.ts` returns `UNKNOWN` unless every narrow address, USPS, property-type and Cuyahoga county condition is present and exact. `UNKNOWN` and `OUT_OF_AREA` both become the same generic refusal.
- Diagnostics: `src/communications/controlled-intake-refusal.ts` logs only fixed exception stages. A normal returned `REFUSED` result does not carry or log the internal branch.
- Durable evidence: `AddressVerificationOperation` and its transition audits retain operation identity/state and privacy-safe transition metadata. They do not retain the provider response, parsed status, coverage classification or generic-refusal branch.

## Finding

The connected submission reached the controlled response path and returned a truthful no-job result. Existing saved evidence is sufficient to classify it as generic `REFUSED`; it is not sufficient to distinguish address-response parsing from coverage classification or correction-sequence retention. A narrow database lookup could at most show whether an operation was observed. It cannot recover the missing reason. A cloud-log lookup likewise cannot recover a normal returned-refusal branch. Spending another credential window on either lookup would not meet the stated diagnostic objective.

No exact root cause is claimed. In particular, the source review does not prove that the customer address was outside Cuyahoga County, that Google returned malformed data, that a particular optional field was omitted, or that the correction cache failed.

## Smallest effective next change

Before any new paid journey, add a privacy-safe, finite internal refusal classification at the point where the generic branches are known, then project only actionable customer categories:

1. `ADDRESS_REVIEW_UNAVAILABLE` for unusable or incomplete provider semantics.
2. `SERVICE_AREA_NOT_CONFIRMED` for `UNKNOWN` coverage.
3. `OUTSIDE_SERVICE_AREA` for confirmed out-of-area coverage.
4. `ADDRESS_CORRECTION_STATE_UNAVAILABLE` for lost/unretainable correction sequence state.

The browser should retain the draft and show a category-specific next action without exposing provider payloads, county data, response identifiers, tokens or internal policy values. Existing explicit `VERIFICATION_LIMIT_REACHED`, `UNCERTAIN`, `CORRECTION_REQUIRED` and `ADMITTED` behavior remains unchanged.

## Proposed files and finite checklist

- `src/communications/controlled-intake-verification.service.ts`: return the finite internal category from each currently generic branch.
- `src/communications/controlled-intake-browser-result.ts`: allow only the approved safe public category and continue denying downstream authority.
- `scripts/fixtures/customer-intake-journey.js`: map each safe category to retained-draft guidance.
- Existing corresponding specs and controlled browser harness: add positive projection, invalid/untrusted-category rejection, provider-unknown, coverage-unknown, outside-area, cache-loss, correction and admitted regressions.
- Run focused tests, lint, build, architecture, disposable database/browser gates, governance baseline/consistency and `git diff --check` in both repositories.

Exit is a locally tested response that distinguishes these safe categories without storing provider data or changing admission, coverage, retry, budget or retention policy. A later deployment and any live acceptance remain separate owner-approved actions.

## Boundaries and decision needed

This is a diagnostic observability repair inside 2B. The owner explicitly approved its public controlled-response and browser-wording change before implementation. That approval does not authorize a database login, provider request, paid journey, allowance increase, deployment or production change. Rollback/disabled state remains the prior generic-refusal projection at source `0a857ed...`; no runtime configuration change is required.

Implementation evidence: backend `evidence/APP-013/p06-r11-refusal-category-repair-20261002.md`. A source-bound release decision and any connected acceptance journey remain separate.

Completed: exact deployed-source trace, screenshot classification, persistence/logging review, owner decision, local implementation and complete local validation. Remaining: source-bound release proposal/decision, separate live authority and actual R11 owner acceptance. P06 remains 12/14; R11/full R12 remain open; accepted 1A/1B/2A remain 3/8. No scope deviation from the expressly approved repair.
