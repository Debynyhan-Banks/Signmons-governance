# System Of Record

## Owner-reviewed intelligence dependency alignment (2026-09-12)

The owner reviewed PRs #28/#22 and requested the coherent six-ticket dependency repair. [INTELLIGENCE_ALIGNMENT_ADOPTION.md](INTELLIGENCE_ALIGNMENT_ADOPTION.md) records this approved documentation decision; integration/merge and release remain unapproved. APP-013 stays sole Now (2B); Next is APP-017 → APP-018 → APP-019 → APP-015 → APP-016 → APP-033. BE-001's residual consent/replay acceptance is consolidated into APP-013, not dropped or declared complete. All older dated Next-empty/proposal-only notes below are historical, superseded for sequencing and pilot definition only. Runtime/evidence and the original 3/8 walkthrough denominator are preserved. No future feature starts until Now meets full acceptance.

## Canonical Precedence

If docs conflict, resolve in this exact order:

1. `SYSTEM_OF_RECORD.md`
2. `WHAT_SIGNMONS_IS_AND_DOD.md`
3. `SAAS_SCOPE_DOD.md`
4. `MARKETING_RELEASE_DOD.md`
5. `EXECUTION_BOARD.md`
6. `GLOBAL_EXECUTION_POINTER.md`
7. `SCREEN_INVENTORY.md`
8. `SCREEN_ROUTE_API_MATRIX.md`
9. `LINK_CTA_MAP.md`
10. `MVP_BACKLOG.md`
11. `DATA_CONTRACTS.md`
12. `PRICING_AND_FEES_POLICY.md`
13. `USAGE_METRICS_SPEC.md`
14. `OFFER_CATALOG.md`
15. `QUALITY_GATES.md`
16. `AI_WORKFLOW_RULES.md`
17. `SESSION_HANDOFF.md`
18. `INTELLIGENCE_ALIGNMENT_ADOPTION.md`
19. `SIGNMONS_INTELLIGENCE_SPEC.md`
20. `INTELLIGENCE_MVP_ROADMAP.md`
21. `MVP_ACCEPTANCE_MATRIX.md`

The owner-reviewed 2026-09-12 alignment is synchronized into higher-precedence product/board documents; it does not override safety, pricing or release rules. Original supplied proposal copies and ARCHIVE documents are historical reference only.

All other docs are reference-only unless explicitly listed above.

## Canonical Artifacts

- Program charter and DoD: `SAAS_SCOPE_DOD.md`
- Product definition + anti-drift DoD: `WHAT_SIGNMONS_IS_AND_DOD.md`
- Marketing release DoD: `MARKETING_RELEASE_DOD.md`
- Active execution queue: `EXECUTION_BOARD.md`
- Global cross-repo state: `GLOBAL_EXECUTION_POINTER.md`
- Screen IDs: `SCREEN_INVENTORY.md`
- Screen/route/API mapping: `SCREEN_ROUTE_API_MATRIX.md`
- CTA/link behavior map: `LINK_CTA_MAP.md`
- Delivery roadmap: `MVP_BACKLOG.md`
- API/event contract policy: `DATA_CONTRACTS.md`
- Commercial pricing/fee policy: `PRICING_AND_FEES_POLICY.md`
- Nonfinancial usage-metric definitions: `USAGE_METRICS_SPEC.md`
- Plan and feature packaging: `OFFER_CATALOG.md`
- Required quality gates: `QUALITY_GATES.md`
- Agent workflow contract: `AI_WORKFLOW_RULES.md`
- Universal chatbot starter: `UNIVERSAL_AGENT_EXECUTION_GUIDE.md`
- Session continuity: `SESSION_HANDOFF.md`

## Non-Contradiction Rules

- Every ticket must reference screen IDs from `SCREEN_INVENTORY.md` only.
- Every public CTA route must exist in `SCREEN_ROUTE_API_MATRIX.md` and `LINK_CTA_MAP.md`.
- `Now` ticket in `EXECUTION_BOARD.md` must be unique (WIP=1).
- Superseded docs/tickets must be moved to `ARCHIVE/` in the same PR.
- Do not run APP ticket implementation while marketing-first phase is active unless explicitly moved in board/pointer.

## Strict Sequencing Rule

- Execute exactly one `Now` ticket at a time.
- Do not start `Next` until `Now` is moved to `Done` with evidence.

## CI Enforcement

PRs must pass docs consistency checks:

- screen IDs exist and are unique,
- `Now` section contains exactly one unchecked ticket,
- ticket screen references resolve,
- CTA map routes/endpoints resolve against route matrix,
- superseded tickets are not referenced in `Now`/`Next`.
