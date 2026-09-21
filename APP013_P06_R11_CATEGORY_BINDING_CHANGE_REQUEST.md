# APP-013 / P06 R11 category-binding change request

Status: owner decision required before implementation.

## Demonstrated gap

Read-only operation `afd29a7b-b2aa-4c12-b894-76e85265dbec` proved the exact HTTP 409 request failed before address reservation. The accepted tenant category ID `c8fdb27a-abc6-4c70-86f2-4296a3262dcb` has internal name `Regular initial visit / diagnosis`. The browser and `validateCustomerIntakeDraft` allow only customer-facing issue classifications `HEATING`, `COOLING`, `PLUMBING`, `ELECTRICAL`, `DRAINS`, `GENERAL`, `BOILER`, `REFRIGERATION`, `COMMERCIAL_HVAC` and `COMMERCIAL_REFRIGERATION`.

`CustomerIntakeContinuationService.controlledSubmissionReader` currently queries `ServiceCategory.name = draft.issueCategory` and requires exactly one match before address reservation. None of the valid browser classifications equals the configured internal category name. The live path therefore deterministically returns HTTP 409 even when phone, session and policy state are valid. This is the demonstrated blocker to R11; another live attempt without repair would repeat it.

## Alternatives

### Alternative 1 — recommended: bind the server-owned allowed category ID

Extend the internal controlled composition/reader binding with the exact service-category ID already selected by the reviewed activation (`allowedServiceCategoryIds[0]`). The reader uses this server-owned ID for current category/authority/admission checks and no longer treats the customer-facing `draft.issueCategory` enum as a database category name. The draft enum remains validated and preserved as the customer's issue classification. Existing current tenant/category active checks, allowed-ID authority check, policy digests, atomic admission, replay and false downstream authority remain.

Impact: small internal interface change and focused tests; no schema, provider, packet format, public route, acceptance denominator or business setup change.

### Alternative 2 — rejected unless separately chosen: rename or add live categories

Rename the accepted category or create categories matching browser enums and update activation bindings. This mutates live business configuration, changes established bootstrap evidence and expands release work. It also continues conflating customer classification with an internal catalog category.

### Alternative 3 — rejected unless separately chosen: add a dynamic category API/UI

Expose internal category labels to the browser and make the form dynamically load them. This adds a public data contract and larger UI/runtime scope that R11 does not require.

## Proposed local implementation card for alternative 1

- Approved section if selected: P06-R11 repair only.
- Source baseline: backend `72588ba`; governance current commit containing this request.
- Reuse: `ControlledIntakeComposition`, `controlledSubmissionReader`, `ControlledIntakeAuthority`, runtime activation allowed IDs, current-state reader, draft validator, existing controlled browser/disposable PostgreSQL harnesses.
- Expected files: controlled composition/runtime/continuation source and focused specifications or harness assertions only; exact final list follows the existing seams.
- Data/state boundary: internal category ID remains server-owned and must equal the activation-allowed ID; customer issue classification remains a validated enum; no new persistence or private fields.
- Positive tests: a human-named active internal category plus valid customer enum reaches address verification/admission; exactly one job and receipt on the existing synthetic connected path.
- Negative tests: missing/malformed/unallowed/inactive/changed category ID, foreign tenant, stale activation or altered customer enum fails before provider/write; replay/concurrency and false payment/booking/dispatch/delivery authority remain unchanged.
- Recovery/browser: refusal retains the draft; no automatic retry; existing visible-owner handoff and closeout rules remain. Browser test proves the enum and internal category can differ without exposing internal IDs.
- Required checks: focused unit and controlled-runtime/browser/PostgreSQL harnesses, build/lint/architecture, governance frozen-baseline/consistency suites and both whitespace checks.
- Exclusions: no database or schema mutation, category rename/create, packet, LOGIN, activation, deployment, provider request, verification code, browser/customer action, job creation outside synthetic disposable tests, secret/IAM or billing change.
- Rollback/disabled state: revert the local source commit; live service remains closed on baseline traffic with no enabled tag.
- Observable finish: reviewed local commit and evidence showing the exact mismatch is repaired in disposable/synthetic execution, then stop for a fresh packet/window and separate live approval.

## Owner decision

Approve alternative 1 for local repair and testing only, choose another alternative, or decline. Approval does not authorize packet preparation or any live/external action. P06 remains 12/14 with R11/full R12 open. No scope deviation implemented.
