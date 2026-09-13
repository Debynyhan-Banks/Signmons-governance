# Owner-requested drift safeguards

Installed under the owner's explicit request to put the previously proposed safeguards in place. This is governance tooling, not another APP-013 implementation section. No acceptance criterion or section baseline changes.

## Enforcement

- Root AGENTS.md in governance and backend requires requirement/section traceability, a complete pre-code card, finite scope, connected-workflow evidence, explicit deviation reporting and owner-approved material changes before implementation.
- scripts/frozen-baseline-check.mjs compares protected text against immutable source revision 57ca1cf0f12ed79075b6afd4781bf28be5e36abc. It protects execution-contract structure/cards/rules, original eight walkthrough acceptance cards, and APP-013's twelve acceptance criteria. Checkbox state and evidence outside protected blocks can change without rewriting requirements. Existing intelligence alignment checks enforce the approved queue and cross-repository consistency.
- docs-consistency-check.mjs includes the frozen check, and the existing CI workflow fetches full history and runs all 17 regression cases. Missing baseline history fails closed. No auto-update or bypass option exists.
- Backend scripts/check-governance-baseline.mjs requires an explicitly resolved governance checkout and invokes the combined cross-repository check. AGENTS.md mandates it before and after governed changes. It is not a newly imposed production pipeline.

## Commands and review

In governance: `node scripts/frozen-baseline-check.mjs`; `SIGNMONS_BACKEND_REPO=<backend> node scripts/docs-consistency-check.mjs`; `node --test scripts/frozen-baseline-check.test.mjs scripts/execution-placement.test.mjs scripts/intelligence-alignment-check.test.mjs`.

In backend: `SIGNMONS_GOVERNANCE_REPO=<governance> node scripts/check-governance-baseline.mjs`. Read both root AGENTS.md files. Review the mutation tests: changed requirement/dependency, added/renamed section, duplicate/missing section and missing history fail; checkbox/evidence changes pass. Tests use in-memory copies, not edits to real requirements.

## Limits and authorized change process

These checks detect protected-document drift, not whether arbitrary code is necessary or whether an acceptance claim is true. They cannot authenticate owner approval. An actor able to change the checker/workflow can weaken it; repository-admin required checks/reviewer protections are not configured or claimed by this work. Review changes to AGENTS.md, checker/anchor/tests and workflow with the same scrutiny as baseline changes. Branch protection is a separate authorized administration decision.

If the baseline genuinely needs changing: stop implementation; present the exact old/new criterion, reason/evidence, alternatives, impact and owner decision request. After explicit approval, record that real decision in a dedicated change record and prepare a reviewable baseline amendment. Only then may a dedicated reviewed commit update the anchor to the approved baseline revision. Never use a generated approval entry or move the anchor merely to make a failing check pass.

Status updates must say No scope deviation or disclose a deviation proposal. Current product section remains 2B and accepted walkthrough remains 3/8 (37.5%). No overall MVP percentage is inferred. After this safeguard task, the next product work remains completing the exact 2B implementation contract before coding.
