# Signmons Execution Board

Purpose: single active queue for execution.

## Operating Rules

1. WIP limit is 1 (`Now` only).
2. No coding without a ticket in `Now`.
3. Do not pull from `Later` directly to `Now`.
4. Every completed ticket includes objective evidence.
5. Update this board before changing scope.
6. Ticket completion must satisfy `QUALITY_GATES.md`.

## Required Completion Gates

- Backend tickets: `npm run -s build` + `npm test -- --runInBand` + `npm run -s arch:check`
- Frontend tickets: `npm run -s build` + `npm run -s lint` + test command for touched surface

---

## Now

- [ ] FE-002 Public trust/compliance pages (`SCR-PUB-005`, `SCR-PUB-010`)
  - Source: `MVP_BACKLOG.md`
  - Ticket spec: `TICKETS/FE-002.md` (create if missing before implementation)
  - Evidence required: acceptance checklist complete + frontend gate output + screenshot proof

## Next

- [ ] BE-001 Enforce keyword opt-in/out persistence and telemetry
- [ ] FE-003 AI CSR page (`SCR-PUB-003`)

## Later

- Remaining MVP epics in `MVP_BACKLOG.md`

## Blockers

- None recorded

## Done

- [x] GOV-001 Bootstrap governance docs
- [x] GOV-002 Cross-repo docs pointers (`DOCS_INDEX.md`)
- [x] FE-001 Marketing Home (`SCR-PUB-001`)
  - Code commit: `a0063be` (`feat(marketing): implement FE-001 home screen`)
  - Gate evidence:
    - `npm run -s build` pass (`/Users/debynyhanbanks/Web Projects/signmons-marketing-web-feat-marketing-site/evidence/FE-001/build.txt`)
    - `npm run -s lint` pass (`/Users/debynyhanbanks/Web Projects/signmons-marketing-web-feat-marketing-site/evidence/FE-001/lint.txt`)
    - `npm test -- --runInBand` unavailable (`Missing script: "test"`) (`/Users/debynyhanbanks/Web Projects/signmons-marketing-web-feat-marketing-site/evidence/FE-001/test.txt`)
  - Screenshot evidence:
    - Mobile full page: `/Users/debynyhanbanks/Web Projects/signmons-marketing-web-feat-marketing-site/evidence/FE-001/home-mobile-full.png`
    - Desktop full page: `/Users/debynyhanbanks/Web Projects/signmons-marketing-web-feat-marketing-site/evidence/FE-001/home-desktop-full.png`
    - CTA close-up: `/Users/debynyhanbanks/Web Projects/signmons-marketing-web-feat-marketing-site/evidence/FE-001/home-cta-closeup.png`
