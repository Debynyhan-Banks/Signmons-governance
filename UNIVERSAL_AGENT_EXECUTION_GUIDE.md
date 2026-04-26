# Universal Agent Execution Guide

Purpose: provide one copy-paste protocol you can use with any chatbot/coding agent.

## Copy-Paste Starter Prompt

```txt
You are my coding agent in <repo-path>.

Before coding, read:
- /Users/debynyhanbanks/Web Projects/signmons-governance/SYSTEM_OF_RECORD.md
- /Users/debynyhanbanks/Web Projects/signmons-governance/SAAS_SCOPE_DOD.md
- /Users/debynyhanbanks/Web Projects/signmons-governance/MARKETING_RELEASE_DOD.md
- /Users/debynyhanbanks/Web Projects/signmons-governance/EXECUTION_BOARD.md
- /Users/debynyhanbanks/Web Projects/signmons-governance/GLOBAL_EXECUTION_POINTER.md
- /Users/debynyhanbanks/Web Projects/signmons-governance/SCREEN_INVENTORY.md
- /Users/debynyhanbanks/Web Projects/signmons-governance/SCREEN_ROUTE_API_MATRIX.md
- /Users/debynyhanbanks/Web Projects/signmons-governance/LINK_CTA_MAP.md
- /Users/debynyhanbanks/Web Projects/signmons-governance/AI_WORKFLOW_RULES.md
- /Users/debynyhanbanks/Web Projects/signmons-governance/SESSION_HANDOFF.md

Rules:
- Execute only the current Now ticket.
- No scope expansion.
- One focused commit.
- Run required gates and show evidence.
- Update SESSION_HANDOFF.md at end.
- Report: files changed, why, tests, risks, exact commit message.
```

## Session Workflow (Strict)

1. Verify global pointer and repo board alignment.
2. Confirm exactly one `Now` ticket.
3. Implement only that ticket.
4. Run required gates.
5. Capture evidence artifacts.
6. Move ticket state only after evidence passes.

## Mandatory Commands By Repo

### Governance

- `node scripts/docs-consistency-check.mjs`

### Frontend

- `npm run -s build`
- `npm run -s lint`
- `npm test -- --runInBand`

### Backend

- `npm run -s build`
- `npm test -- --runInBand`
- `npm run -s arch:check`

## Non-Negotiable Constraints

- No dead CTA links on public pages.
- Contact conversion must persist to backend (email minimum).
- Demo conversion must run live API flow.
- Docs must not contradict `SYSTEM_OF_RECORD.md`.
- Superseded docs/tickets must be archived in the same PR.
