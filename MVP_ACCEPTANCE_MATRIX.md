# Intelligence pilot acceptance matrix

Owner-reviewed integrated pilot requirements, 2026-09-12. No capability is accepted by this documentation decision. Existing fixed walkthrough: 3/8 accepted (37.5%), current 2B; not overall engineering completion. Each row requires code, tests, environment-specific evidence, reviewer and acceptance date before accepted status. This matrix adds no claimed engineering percentage.

| Requirement | Current evidence/status | Owning ticket / missing acceptance |
| --- | --- | --- |
| Transactional communications and verified intake | In progress on backend PR #21; not main runtime adoption | APP-013 current-session proof binding, Google-derived retention, protected bootstrap and connected acceptance remain; county GIS is not a gate |
| Payment/calendar/text walkthrough | In progress; docs/execution-baseline/PAYMENT_BOOKING_TEXT_STEEL_THREAD.md: 1A/1B/2A accepted, 2B current | Remaining 2B, 3A Sandbox payment, 3B test calendar, 3C received text, 3D recovery |
| Voice and ordinary conversational SMS | Unverified for integrated pilot; transactional foundation is not channel acceptance | APP-033 actual authorized channel tests, privacy, interruption/handoff evidence |
| Web conversation, tenant safety and discovery | Implemented portions, not accepted as intelligence pilot; existing protected-intake/organization evidence | APP-033 contextual hazard and discovery scenarios across stages |
| Versioned rules, service fees, payment policy | Implemented portions in organization/verification/payment policies; complete acceptance unverified | APP-017 approved/missing/changed-policy and cross-tenant tests |
| Brand and ethical comfort/sales behavior | Missing accepted integrated behavior; earlier deferral superseded by reviewed pilot clarification | APP-018 versioned previews, refusal and no fabricated claims |
| Customer/property/equipment memory | Existing records; authorized integrated history acceptance unverified | APP-019 provenance/corrections, sensitive access and tenant tests |
| Approved knowledge retrieval | Approved facts/FAQ portions; full reviewed retrieval acceptance unverified | APP-033 review/version/rights/applicability, stale/conflicting/missing sources and injection tests |
| Booking/payment integrity and technician ownership | Prior APP-011/012 accepted components; no new integrated retest | APP-016 live slot races, late payment, duplicate webhook, recovery; reuse existing tests |
| Technician brief and outcome | Existing technician workflow; intelligence-linked brief/outcome acceptance unverified | APP-019/033 facts versus conclusions, durable ownership and actual tool/job outcomes |
| Human review and independent evaluation | Missing accepted intelligence eval/review baseline | APP-015 failure taxonomy, corrections, held-out cases, version/outcome lineage |
| Consent, retention, tenant security | Existing controls and unfinished live activation gates, not waived | BE-001 residuals consolidated into APP-013; APP-033 reuses accepted consent/private access/redaction controls |
| Latency/cost/funnel and operations | Unverified integrated pilot evidence | APP-015/033 telemetry, fallback, rollback, operating owner and critical failure release block |

Mandatory scenario set: emergencies before/after discovery and during payment; old equipment without forced replacement; uneven temperature without invented sizing; respectful objections; missing/conflicting sources; unverified identity/cross-tenant access; prompt injection; unavailable slots/duplicate bookings; forged/replayed payments; provider timeout/disconnect; consent withdrawal and unsupported tool requests.

Review must show concern → safe discovery → approved knowledge/context → appropriate authoritative sandbox action or human handoff → technician brief → persisted outcome → correction/review → independent evaluation. Finite passing tests do not prove zero risk. No live/canonical proof from mocks, no automatic training, no commercial availability from pilot acceptance.
