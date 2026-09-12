# Intelligence alignment — owner-reviewed dependency correction

## Decision and authority
Owner reviewed the paired documentation proposal and on 2026-09-12 explicitly requested a coherent dependency repair, complete ticket specs, populated synchronized Next, and integrated intelligence pilot definition. This records that documentation approval, not a merge, deployment, feature acceptance, provider/budget authorization or training approval. PRs: governance #28 and backend #22, still isolated/stacked on the focused APP-013 branches.

Now remains APP-013 (2B); Next: APP-017 → APP-018 → APP-019 → APP-015 → APP-016 → APP-033. BE-001 is substantially implemented; residual consent/telemetry proof belongs to APP-013 before full acceptance, not a separate duplicate queue item. See BE001_DEPENDENCY_REVIEW.md. No future implementation begins in this correction.

## Verified inconsistencies and repair
- Original saved backend board is stale APP-011; current focused backend and governance are APP-013. Do not write over the dirty originals.
- Initial alignment PRs intentionally left Next empty/pending. Owner now approves the dependency correction; both boards and Current Pointer explicitly carry the same six-ticket queue.
- Draft APP-017/018/019 specs existed only in the documentation PR, not original governance main. They are completed here using the repository ticket format with dependencies, contracts, security, checkable acceptance and evidence.
- The initial detailed bundle inserted BE-001 after APP-015 while its shorthand omitted it. Actual code establishes substantial duplication plus residual safety gaps; consolidate those gaps into current APP-013, preserving their acceptance obligation.
- Product identity's September 10 advisory deferral contradicted the reviewed integrated pilot. Archive that historical scope paragraph and replace it with the narrow reviewed pilot clarification. Preserve current APP-013 scope, historical tests and the original 3/8 walkthrough denominator.
- Backend DOCS_INDEX used an incomplete precedence order and hard-coded stale saved paths. It now directs agents to current governance SYSTEM_OF_RECORD and the focused pointer.
- APP-015/016/033 retain original acceptance and gain explicit intelligence dependency/integration criteria. No accepted work is reset or claimed redone.

## Coherent scopes
A: integrated Eternity pilot demonstrates supported voice/conversational SMS/web, safe intake/qualification, relevant comfort discovery, approved knowledge/history, authoritative booking/required-payment handoff, customer confirmation, technician brief, owned structured outcome, human review and evaluation.
B: commercial release separately satisfies entitlements/onboarding/subscriptions, support/security/recovery/monitoring, promised Money/pricebook and Growth diagnostic reporting. Pilot success is not every plan's availability.
C: optimization follows reviewed outcomes. Fine-tuning, preference/reinforcement experiments, predictive recommendations and richer copilot behavior require measured justification, rights, independent evals and explicit budget/training/release authority. No automatic reuse of raw conversations.

## Progress and continuation
Runtime baseline remains backend 330e402, governance parent 387adec. APP-013 PR #21 untouched. Its full acceptance, county/source qualification, controlled verification/budget integration, IAM/test/release authorization and remaining payment/calendar/text/recovery evidence remain open. Historical BE-008 acceptance is preserved, not proof of current advanced replay behavior. Current walkthrough acceptance 3/8 (37.5%) is not overall MVP engineering completion.

After full Now acceptance and required human/provider gates, synchronize boards/pointer and promote the first approved Next without asking for routine phase selection. WIP=1; never skip blocked Now, pull Later, merge, deploy or launch training automatically. Save a truthful resumable handoff.

## Validation and provenance

Correction gates (2026-09-12): `SIGNMONS_BACKEND_REPO=/private/tmp/signmons-alignment-backend.vaLLbj node scripts/docs-consistency-check.mjs` passed, including cross-repo queue equality. `node --test scripts/intelligence-alignment-check.test.mjs`: four passed. Backend `npm run -s build`, `npm run -s lint`, `npm run -s arch:check` passed; `npm test -- --runInBand`: 1,989 passed, three skipped, 105 passing suites/one skipped, first correction run passed. `git diff --check` passed in both repositories. Backend runtime/schema/scripts/package diff against 330e402 is empty. No rendered UI changed; browser QA not applicable, no new live acceptance claimed. Original implementation branch heads remain 330e402 and 387adec. A patch attempt against the oversized historical handoff was rejected without modifying it; corrected with targeted hunks, preserving all history.
Original bootstrap preflight passed but selected stale saved checkouts and lacks cross-repo/version checks. A temporary worktree-compatible copy passed on the isolated current baselines; ZIP unchanged. Supplied proposal SHA snapshot 64942c0 was reconciled to runtime 330e402. Original source documents are historical in proposals/intelligence-alignment, subordinate to this decision.

Original alignment validation: complete governance check passed; backend build/lint/architecture passed; full unchanged rerun 1,989 passed, three skipped, 105 passing suites. Initial shared-dependency-symlink check and Calendar 401/429 failure were documented; isolated dependency copy and unchanged rerun passed. Current correction validation is recorded in the PR update, including dependency-order regression checks. No runtime/schema/package/provider changes.
