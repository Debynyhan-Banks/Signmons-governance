# Address-format decision — APP-013 / 2B / P06-R11

Status: owner-approved alternative 3 implemented and locally verified October 1. Finite implementation checklist 1–4 complete; no deployment or live acceptance. This is a bounded matching-policy change within existing 2B, not a new section or live-test approval.

## Requirement, source and demonstrated gap

Existing acceptance: APP013_REMAINING_EXECUTION_CONTRACT.md, section 2B, requires one customer-reviewed job after current phone, eligible Cuyahoga address and tenant-policy checks. Invalid, uncertain or stale input retains progress without creating a job. GOOGLE_ONLY_SERVICE_AREA_POLICY.md requires consistent provider evidence; customer confirmation cannot supply missing evidence.

Inspected backend HEAD: 3cf8a9dc53d0282a35e6263a36d749c5b32f8e2e plus existing focused-worktree changes. Prior immutable run source: 5a49a3b04b1b0145d3d7ae811221e3f651c0aebc. Preserve both previous work and consumed run snapshots. The completed local correction-limit patch and its evidence remain separate: backend evidence/APP-013/p06-r11-correction-limit-repair-20261001.md.

In src/communications/google-address.adapter.ts, the parser currently compares input ZIP against both postal.postalCode and the unassembled postal_code component. It accepts a confirmed postal_code_suffix component but does not use it. A ZIP+4 postal address and separate ZIP5/suffix4 components therefore cannot agree under that comparison. The same parser requires street strings to agree after case/whitespace normalization only. Existing adapter tests reproduce repeat correction for structured/postal street and ZIP disagreement; they do not identify the actual live response or prove the cause of the October 1 failure.

Official [Google Address Validation example](https://developers.google.com/maps/documentation/address-validation/confirm-address-example) documents a separately returned postal_code_suffix. The [REST reference](https://developers.google.com/maps/documentation/address-validation/reference/rest/v1/TopLevel/validateAddress) distinguishes postalAddress from validated addressComponents. This supports parsing those representations deliberately; it does not authorize ignoring conflicting components. [USPS Publication 28, Appendix C1](https://pe.usps.com/text/pub28/28apc_002.htm) supplies standard suffix spellings for the finite proposal below. These are documentation reads, not provider validation calls.

## Alternatives and recommendation

1. Retain all current comparisons: least code change, but the reproduced formatting conflicts continue to stop otherwise qualifying synthetic journeys.
2. Repair only ZIP component assembly: fixes that structural comparison; street abbreviations still require identical provider forms.
3. **Recommended: exact ZIP assembly plus the twelve explicit suffix pairs below.** Preserve exact customer review of Google's postal candidate and all other evidence checks. This permits only named representations of the same suffix, not fuzzy address matching.

Do not choose Google's postal text over genuinely disagreeing house number, street name, unit, city, state, ZIP or county evidence. Do not introduce another lookup, an address library or AI adjudication.

## Proposed exact behavior

### ZIP assembly

- Require postal_code to be five digits or an already complete ZIP+4. If postal_code_suffix is present, require exactly four digits and the existing CONFIRMED-component checks.
- For ZIP5 plus suffix4, compare ZIP5-suffix4 to the returned postal ZIP and the customer's reviewed ZIP. For an already complete ZIP+4 plus suffix4, require the suffix to agree with its final four digits. A ZIP5 without a suffix remains ZIP5.
- Never discard, truncate, invent or guess an extension. Missing, malformed, duplicate or contradictory evidence must not produce REVIEW/eligibility. Input ZIP5 versus a provider ZIP+4 still requires the existing correction/review step.

### Street suffix equivalence

Only these pairs may compare as equivalent: STREET/ST, AVENUE/AVE, ROAD/RD, BOULEVARD/BLVD, DRIVE/DR, LANE/LN, COURT/CT, CIRCLE/CIR, PARKWAY/PKWY, PLACE/PL, TERRACE/TER, TRAIL/TRL.

- Apply equivalence only to the final token of the separate street field and the structured street_number + route comparison. Require the same preceding tokens, including the complete house number and at least one street-name token. Keep case/whitespace normalization as currently defined.
- Keep the existing comparison between the customer-reviewed street/unit and Google's joined postal address lines. The customer must still submit the actual postal candidate when its spelling differs. Do not rewrite customer data silently or treat a client-supplied confirmation flag as proof.
- Do not expand abbreviations inside street names, directions, units or city names; do not remove punctuation, alter numbers, infer a suffix, accept an unlisted alias, or drop any provider component. For example, ST JOHN is not SAINT JOHN; EAST is not WEST; STREET is not ROAD.
- Keep inferred/replaced/spellCorrected flags, unconfirmed/missing components, granularity, required-unit and DPV checks unchanged. Persistent flags can still require correction and then the existing terminal stop; this proposal does not guarantee every legitimate address passes.

### Connected workflow, identity and retention

Reuse reviewGoogleAddressResponse and the existing Google service-area evaluator, controlled verification service, durable operation executor, job-admission transaction, correction screen and current proof checks. The parser's REVIEW remains authority-neutral. Only the existing full admission path may create a job.

Keep the tenant/session/conversation/request/address-revision/policy/organization bindings, current phone proof, explicit customer review, physical-address/US/OH/Cuyahoga evidence and freshness limits. Keep the volatile first-response-ID sequence, its five-minute/session-expiry bounds and one-use behavior. No new persistent fields, raw provider retention, interface, schema, provider or endpoint. The existing two-address-operation limit and terminal second-correction behavior remain. General account/tenant capacity cannot be inferred from the session count.

## Files, finite checklist and validation

Expected runtime edit: src/communications/google-address.adapter.ts only, using a small private literal pair table/helper in that file. Tests: its existing spec, google-service-area.spec.ts, controlled-intake-verification.service.spec.ts as needed to prove propagation, and scripts/verify-loaded-intake-browser.mjs. No production UI or service-area policy-gate rewrite is expected. Update only focused evidence and governance status; preserve unrelated dirty files.

1. Save pre-edit copies/delta and reproduce supported split-ZIP and suffix cases through the existing parser tests. Add positive cases for matching split ZIP, already complete ZIP, confirmed corrected postal candidate and paired suffixes; retain exact-match behavior.
2. Implement only the comparisons above. Negative cases: malformed/conflicting/missing ZIP suffix, changed first-five digits, unlisted street alias, suffix in a street-name position, changed house number/name/direction/unit/city/state/country, unconfirmed or missing components, persistent inferred/replaced flags, missing/contradictory county and physical-address failures. No negative may acquire job authority.
3. Exercise the connected existing synthetic database/browser journey at 390/1440: first correction to the postal candidate, second consistent split-ZIP/allowed-suffix response creates exactly one job after current proofs; repeated true conflict still stops after two operations, retains draft and creates no job. Reuse duplicate/concurrent admission, stale/foreign identity, lost sequence/restart, late provider/failed observation and uncertain commit regression coverage; do not weaken it or add a standalone demo.
4. Run focused tests, required full gates and complete existing disposable database/browser harness; record isolated delta and outcomes. Local success is not live demonstration or owner acceptance. Stop and report a material gap instead of adding another policy exception.

Commands from the backend: npm test -- --runInBand src/communications/google-address.adapter.spec.ts src/communications/google-service-area.spec.ts src/communications/controlled-intake-verification.service.spec.ts; npm test -- --runInBand; npm run lint; npm run build; node scripts/architecture-check.mjs; node --check scripts/verify-loaded-intake-browser.mjs. Reuse scripts/verify-organization-profile.mjs with the owned disposable socket-only PostgreSQL cluster, fixture providers and installed Playwright; unset live DATABASE_URL/DIRECT_URL and regenerate only local compiled outputs. Verify fixture databases removed and the owned cluster stopped.

Before/after changes run the backend check-governance-baseline with resolved SIGNMONS_GOVERNANCE_REPO, governance frozen-baseline/docs-consistency checks, the three required governance test files and git diff --check in both repositories. Do not change frozen acceptance text/anchors. For this proposal-only review, documentation/architecture/whitespace checks suffice; prior runtime tests are not fresh evidence.

## Authority, impact, rollback and finish

At proposal time authority was review/preparation only. The preceding approved repair expressly said: "matcher changes are excluded from this approval." The owner decision below approved this concrete exception before application implementation: alternative 3 and its finite local implementation/tests. No need to select individual functions or reapprove routine checks within that decision.

Impact: one parser edit with affected existing tests; no new subsystem, dependency, acceptance section/count or queue change. The twelve-pair rule is a deliberate, limited broadening of matching policy; ZIP assembly corrects the representation comparison. Later live use requires the resulting semantics to be bound into the existing source/policy/release qualification, with no reuse of stale proof. This card does not authorize a release or select a live window.

Owner controls the policy decision; implementer owns implementation and evidence after approval. Local dependencies are installed PostgreSQL/Playwright and existing harness; unavailable prerequisites stop that gate. No deployment, image upload, live database/provider query, message/code request, payment, increased cap, released hold, retry of a consumed run or session cleanup. Current paid allowances remain exhausted according to the saved verified snapshot.

Rollback: revert only this future isolated patch and retain the prior local correction-limit repair and closed live runtime. Observable finish: connected synthetic corrected-format success and true-conflict/uncertainty refusal, reviewed patch and passing checks, with no extra call or duplicate job. Actual provider behavior and live acceptance remain unproven.

Review checklist complete: source/policy gap, official documentation, alternatives, finite behavior/file/test scope and independent read-only audit. Implementation checklist 1–4 is complete under the recorded owner decision. P06 remains 12/14; R11/full R12 open; accepted 1A/1B/2A remain 3/8. The bounded suffix-equivalence policy change was approved before implementation; no additional scope deviation.

## Owner decision

October 1: owner replied "yes i approve" to the explicit proposal to implement and test exact ZIP assembly and twelve suffix pairs locally. Alternative 3 and finite checklist 1–4 are approved, including existing disposable database/browser tests and local compilation. No live calls, deployment, cap increase or new window are authorized. Earlier proposal-stage authority statements above remain the decision history; this decision grants the specific local authority before application edits. Pre-change baseline/frozen/consistency checks passed; five expected source/test files were copied to /private/tmp/r11-address-format-before-20261001 before edits. Preserve unrelated changes and the prior correction-limit repair.

## Review validation

October 1: independent read-only review found no material blocker in the finite proposal. Backend governance baseline, governance frozen baseline and cross-repository consistency, all 21 required governance safeguard tests, backend architecture and both whitespace checks passed. Documentation-only work: no new runtime test, compile, database/browser run or live acceptance is claimed.

## Local implementation completion — October 1

Approved checklist 1–4 complete. One runtime parser file changed; three existing test/harness files changed. Pre-existing correction-limit repair and unrelated changes preserved. Adapter 102/102, service-area 51/51, full 2,480 tests passed with three existing skips; lint/local compile/architecture/syntax passed. The complete disposable database/browser harness passed with 14 loaded cases at 390/1440. Corrected suffix/ZIP+4 cases each create exactly one job from two OBSERVED synthetic calls after explicit review; true conflicts, stale/foreign proofs, uncertainty and duplicate/replay cases preserve their gates. Temporary databases/cluster removed; no live provider call or deployment. Independent runtime diff review found no material issue.

Backend evidence: evidence/APP-013/p06-r11-address-format-repair-20261001.md, with isolated patch/hash and exact logs. The actual prior live mismatch is still unconfirmed. Next is a separately scoped source-bound release/live proposal incorporating both local repairs; implementer owns preparation and owner owns external actions/allowance/window. None prepared or authorized by this local completion. Counts unchanged. No scope deviation from the expressly approved change.
