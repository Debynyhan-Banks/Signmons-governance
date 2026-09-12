# 2B county fallback and live-verification gap assessment

Reviewed 2026-09-12 against backend f9181eb and governance 5bd8875. Owner approved this bounded readiness assessment. Documentation only; no source accepted or activated.

## Decision

Keep county UNKNOWN. No reviewed fallback meets the existing physical-site/current-source contract yet. This is a bounded negative qualification result, not proof that no suitable source exists. Do not await a county email before doing independent engineering, but do not mark 2B accepted or advance the queue on synthetic evidence.

The county inquiry is owner-reported sent; response pending per owner. No mailbox was searched this turn. Older unsent-inquiry/ask-permission-to-send instructions are superseded. Existing f9181eb tests prove an inactive composition, not live verification.

## Source comparison

| Candidate | Public evidence checked now | Decision under current contract |
| --- | --- | --- |
| Cuyahoga CEGIS | Published county GIS disclaimer describes free public data supplied as-is without accuracy, completeness or timeliness guarantees. Prior record-type aggregate remains historical; live metadata refresh returned a retrieval error in this assessment. | Still pending physical-record quality, freshness, operational and reuse qualification. A disclaimer alone neither proves bad data nor disqualifies practical use; source-specific suitability evidence is missing. |
| Ohio LBRS download | Official table lists Cuyahoga centerlines dated 2023-11-27 and address points dated 2023-12-01. No archive downloaded or individual address inspected. | Candidate only. This page does not establish a current 2026 release, per-record precision or independent provenance; not a fresh substitute for CEGIS. It does not prove newer data is unavailable elsewhere. |
| Census Geocoder | Official documentation says coordinates are interpolated/approximated from address ranges, which can include nonexistent structure numbers. | Cannot supply positive physical-building proof under current contract. No customer lookup sent. |
| Census TIGER boundary plus Google point | A boundary can classify a coordinate, but cannot remove uncertainty in the coordinate. Existing contract requires uncertainty crossing a boundary to remain UNKNOWN. | No qualified combined error model or boundary-case evidence established. Do not invent a buffer or treat a Google point/ZIP as county proof. |

Sources:
- [County GIS terms](https://gis.cuyahogacounty.us/portal/sharing/rest/content/items/b41c3350839741098c9a3bc4d495e04a/data).
- [Ohio LBRS download table](https://gis1.oit.ohio.gov/geodatadownloadtable/lbrs.aspx).
- [Census Geocoder documentation](https://www.census.gov/programs-surveys/geography/technical-documentation/complete-technical-documentation/census-geocoder.html).
- [Google ValidateAddress reference](https://developers.google.com/maps/documentation/address-validation/reference/rest/v1/TopLevel/validateAddress).

No paid vendor selected, dataset licensed, commercial permission inferred or new fixed cost incurred. Public availability is not a reviewed operational SLA. Provider-directory CLI lookup was unavailable; official-source browsing used instead without installing software.

## Fixed remaining work within existing 2B

These are acceptance work packages inside 2B, not extra walkthrough milestones or a promise of four coding turns.

| Work package | Verified implementation gap | Finish line |
| --- | --- | --- |
| Controlled live request lifecycle | address-operation-ledger.ts only accepts FIXTURE_ONLY policy; google-address-operation.ts requires injected ports and discards the response. | Explicit approved account/tenant/session policy binds server identity, rates, limits and deadline; no fixture promotion. Reserve before dispatch, preserve uncertain liability, demonstrate stop/recovery behavior. |
| Address semantics and confirmation | google-address.adapter.ts parses fixture responses; composed transport observation is not a correction candidate. Request shape lacks previousResponseId. | Reuse parser rules through an authority-neutral semantic boundary; bind correction and confirmation to exact revision and current session. Carry the first Google response ID for revalidation as documented, transiently and within approved retention; never confuse response IDs with proof or logs. Tests cover corrected/unit/stale/duplicate/deadline cases. |
| Qualified county and current proof | current-proof-admission.ts only accepts FIXTURE_ONLY and returns realVerificationAccepted=false; continuation writes NOT_VERIFIED. | Qualified source and approved coverage policy feed genuine current evidence. Recheck revisions, deadlines, tenant and one-time admission atomically; source I/O outside locks. UNKNOWN refuses automated admission without destroying the draft. |
| Controlled end-to-end acceptance | durable-verification.service.ts is an inactive local proving connection; no live bootstrap acceptance. Checklist still requires actual source-to-job evidence. | Verify exact staging identity/resources, effective IAM, notices/retention, account rates and approved capped test packet. Observe code receipt, confirmed address, qualified county and exactly one job, plus negative/recovery cases. No payment, booking or confirmation send implied. |

A county reply is an external evidence gate, not the only missing implementation. Conversely, a successful HTTP response is not 2B completion.

## Next bounded implementation recommendation

Address revalidation lifecycle is the next concrete independent gap: add a server-held, transient first-response reference bound to the same session/intent/revision and validation sequence; permit only that trusted reference in follow-up requests. Preserve disabled live dispatch, no browser-supplied reference, existing expiry and no raw response persistence. Reuse the existing transport/parser rather than building another demo. Finish with contract and negative tests; do not enable calls.

This recommendation does not pre-approve a retention exception: confirm the transient response-reference handling against applicable provider terms and the existing field matrix before implementing. If that cannot be resolved, stop and report that specific issue.

County source qualification can resume when a reply or current quality-documented release is available. Changing from verified physical county to a lower-confidence business service-area policy would be a material owner decision, not a routine implementation shortcut; no such change is adopted here. No routine manual approval flow is substituted for the owner's automation goal.

## Review and validation

Review source dates and limitations, compare the four package rows with the cited backend files, and ensure no fixture result is relabeled real. Original focused worktrees clean before documentation edits; unrelated saved checkout changes preserved.

Cross-repository docs-consistency-check passed. Initial governance regression run: six passed, two failed because execution-placement tests searched for a removed historical sentence beginning “2. After review”; that sentence is also absent at pre-change HEAD. Test extraction now selects step 2 within the canonical Next Actions section, preserving the existing swapped-row, missing-step and ordering assertions. Final eight governance regressions and git diff --check passed. Runtime, dependency, schema and UI files unchanged: no fresh build/lint/runtime-test/browser-QA claim. Prior 2,001 passing tests remain historical evidence from f9181eb.

APP-013 sole Now; 2B current. Next APP-017 → APP-018 → APP-019 → APP-015 → APP-016 → APP-033 unchanged. Walkthrough accepted 3/8 (37.5%); five remaining acceptances, not whole-MVP completion or ETA. No merge, release, IAM/secrets, provider configuration, charges, messages, production migration or real data action.
