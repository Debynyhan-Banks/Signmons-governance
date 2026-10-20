# Signmons Intelligence — owner-reviewed specification

Status: owner-reviewed dependency/pilot documentation, 2026-09-12; see INTELLIGENCE_ALIGNMENT_ADOPTION.md. This is not a runtime prompt or permission to start future tickets, deploy or train.

Signmons is an AI front-office operating system for the trades. Eternity is a tenant-configured pilot, never a source of global prices, branding or customer defaults. A shared orchestrator with typed capabilities is preferred; no speculative agent microservices.

## Authority boundaries

- Knowledge: approved, versioned, tenant-owned sources with review, applicability, effective date and usage rights. Imported websites/documents remain untrusted drafts until approved.
- Business facts: authoritative customer/history, prices, service fees, availability and policy APIs. Unknown stays unknown; corrections retain provenance.
- Policy: server-controlled tenant identity, safety, authorization, consent, payment, booking and dispatch truth.
- Model: intent, relevant discovery, source-supported explanation and proposed next step. It cannot authorize itself or declare successful tool outcomes.
- Tools: typed inputs, tenant/role validation, immutable financial snapshots, timeouts, idempotency, bounded retries and recoverable side effects.
- Evaluation: deterministic safety/financial/permission assertions plus independent rubric/human review. No hidden chain-of-thought storage or self-confidence as calibrated evidence.

## Release A pilot behavior

Voice, ordinary conversational SMS and web share validated context but have independent channel acceptance. Transactional texts are not conversational SMS. Safety interrupts every state, including payment/sales, before identity or booking questions. Ambiguity, transcription mistakes, negation and new hazards require tested safe escalation; no dangerous troubleshooting or autonomous diagnosis.

Relevant comfort discovery uses Situation, Impact, Goals, Needs, Match, Options, Next step, Service flexibly. Respect refusal; do not turn every service request into a sales interview. Never invent prices, discounts, financing, scarcity, savings, warranties, equipment sizing, technical conclusions or availability. Old equipment alone does not imply replacement; uneven temperatures do not imply a larger unit. Approved low-risk guidance and emergency protocols require qualified review before activation.

Private customer/property/equipment history requires appropriate identity and tenant authorization, not merely matching a supplied phone/address. Preserve uncertainty, source/timestamp and corrections; no cross-tenant or unvalidated cross-channel merging. Customer critical-field confirmation, phone verification and consent are separate authorities.

Approved service-fee policy can support advisory booking; full equipment quotes require governed Money/pricebook scope. Missing payment policy fails closed; explicitly not required is distinct from unavailable. A hold is not a confirmed appointment. Verified payment where required plus current conflict check precede promises. No card details enter model transcripts. Technician briefs distinguish observed facts, unconfirmed possibilities and verified findings, with a visible owner and outcome.

## Controlled improvement

Record minimized scenario/intent, confirmed facts, source references, model/prompt/policy/knowledge versions, typed tool outcomes, actual payment/booking/job outcomes, reviewer feedback and corrections with rights/retention controls. Separate synthetic unreviewed examples, development evals and held-out tests; group related conversations/paraphrases to prevent leakage. No tenant pooling/export without rights, no automatic retraining or promotion. Training requires explicit authorization, budget and measured benefit over a baseline.

Safety/privacy/authorization/financial failures block release independently of conversion scores. Measure task completion, latency, cost, grounding, discovery and customer choice separately with sample sizes and uncertainty. No offline simulation is a business-performance claim.

## Extensibility direction — documentation only, 2026-09-20

The owner requested review and inclusion of `Signmons_Codex_Extensibility_Alignment_Prompt.md` in project documentation. This section preserves its engineering direction; the supplied document's agent workflow is not a runtime instruction. This docs-only adoption grants no implementation, refactoring, provider activation, training, publishing or release authority. It adds no acceptance prerequisite, task, ticket or queue change. APP-013/2B remains Now. At this amendment's review checkpoint P06 was 11/14 with R10/R11/R12 open; the September 21 execution pointer now records P06 at 12/14 with R10 complete and R11/full R12 open.

Extend the existing modular application through small, evidenced interfaces and dependency injection. Do not prebuild a universal platform, dynamic plugin loader, broker, microservice architecture or new capability/model registry. Reuse tenant identity, permissions, customer records, audit and financial truth. Keep future marketing assets and audit runs in their own appropriate domain rather than overloading Job or untyped metadata. Additive schema changes may be needed under later approval. Keep trades vocabulary and policies outside generic provider infrastructure where practical; hypothetical industries do not justify a rewrite.

The authority boundary remains: authorized context → model assessment/proposal → server policy checks → domain service action → verified result → audit/UI. Authorize context sharing before model access and recheck authority before side effects. Models cannot establish identity, consent, safety, prices, payment, availability, booking, dispatch or publication truth. Missing policy fails closed; deterministic rules/calculations remain code and safety interrupts remain independent of conversion goals.

### Generation and structured decisions

For later approved integrations, separate text generation from bounded structured decisions using task-specific, runtime-validated contracts. Record task/schema version, authorized context, permitted outputs, outcome status and provider provenance. TypeScript types alone are insufficient. Do not force every provider into a chat-completions interface or describe replacement as a configuration-only swap: adapter work, semantic evaluation and activation approval may be required. Prefer existing dependency injection or a small static mapping when sufficient.

TypeSafe AI Jev is an optional future candidate for classification, routing suggestions, scoring or review prioritization, not a current dependency or a claimed supported integration. No Jev API, access, pricing, latency or feature capability was verified in this review. Before designing an adapter, verify current official documentation and record dates and unknowns. Keep generation with a suitable generative provider; do not require dual-model calls. Preserve the actual meaning of supplied probabilities/confidence without fabricating equivalents. Schema correctness is not factual correctness, safety or calibration. Require task-specific evaluation, asymmetric error analysis, abstention and explicit activation approval; do not invent a universal threshold. Neither Jev nor another model may be the sole safety authority or authorize consequential actions. Fallback must preserve permissions, data-sharing/retention constraints, budgets and task semantics; private context must not silently move to another vendor. Offline evaluation precedes separately approved shadow/canary use, feature controls and rollback. Unavailable access does not block current work.

### Future Growth and asynchronous work

Website audits, SEO, GEO, reputation and attribution are future domain capabilities. Preserve tenant-owned property authorization, audit-run identity, evidence, findings, recommendations, approvals and measured outcomes. Distinguish deterministic/tool observations from model interpretation; retain source, timestamp, scope and uncertainty. Do not promise rankings/citations, invent a universal GEO score or equate attribution with causal revenue proof.

Treat crawled/imported content as untrusted data. Future crawling must address SSRF, private/loopback/link-local destinations, redirects, DNS rebinding, credential leakage and resource limits, with authorization, robots policies and provider terms respected. Read access does not authorize publication. Website changes require an authorized asset, preview/diff, scoped owner approval or separately approved automation policy, least-privilege access, concurrency/version checks, verified execution and rollback/recovery.

Long-running audits/imports/reports must be isolated from intake, booking, payment and dispatch reliability. Reuse existing infrastructure where appropriate, assessing tenant-scoped state, quotas, cancellation, bounded retries, idempotency, restart recovery and explicit failures. Distinguish operational events, security audits, analytics and billing records. Reliable delivery requires evidence of transaction consistency and duplicate handling; neither exactly-once delivery nor event sourcing is assumed. Usage measurement must not silently change governed subscription billing.

### Evaluation, telemetry and UX

Apply shift-left security, tenant-isolation and secure-coding review when touching relevant authorized code. Extend existing telemetry only as needed: tenant/task/run correlation, model/prompt/policy/schema versions, latency, errors, abstentions, tool outcomes and actual provider/model/token/cost units. Missing measurements stay unknown, not zero. Exclude credentials, card data, unnecessary personal data and hidden chain-of-thought. No new observability vendor, Langfuse/OpenTelemetry project or automatic training pipeline is authorized here.

Interfaces should reflect backend truth through proposed, awaiting approval, running, succeeded, failed and uncertain states, with human takeover, recovery, accessibility and progressive disclosure. Evaluate verified business outcomes separately from model quality and marketing claims.

### Bounded implementation review and deferred ownership

Review source: backend `ba12d10eba1f0e532ec9f2d447db1237b833abd9`; governance before this amendment `b55dd9fee69bf733aac63a2caed8e6dfe761197f`. Both focused recovery checkouts were clean before this docs-only amendment. These findings are targeted source inspection, not connected acceptance, a security audit or proof of full extensibility.

| Boundary | Existing evidence in backend unless noted | Status and smallest future consideration | Existing scope / approval |
| --- | --- | --- | --- |
| Modular composition | `src/app.module.ts`; domain module files; `AiProviderService` injection of `AI_COMPLETION_PROVIDER` | Implemented composition seams; broad interchangeability unproven. Reuse before adding abstractions. | APP-033 where relevant; scoped implementation approval |
| Model contracts | `src/ai/interfaces/ai-provider.interface.ts` (`IAiProvider`); `src/ai/providers/ai-provider.interface.ts` (`IAiProviderClient`) | Partial: both expose OpenAI types. A vendor-neutral structured-decision contract is not established by these interfaces. | APP-033 candidate alignment; Jev adapter remains an unassigned proposal |
| Tool authority | `src/ai/tools/tool.provider.ts` (`ToolRegistryService`); this specification's Authority boundaries | Registry stores OpenAI tool descriptions; registration alone proves neither runtime validation nor authorization. Preserve domain checks in any later integration. | APP-017 policy / APP-033 tools; no acceptance expansion |
| Recovery infrastructure | `src/communications/sms-delivery.worker.ts` (`SmsDeliveryWorker.processDue`); `prisma/schema.prisma` (`SmsEnqueueIntent`, `CommunicationEvent`, `AuditLog`) | Implemented SMS-specific worker/recovery structures; general crawl scheduling, cancellation and recovery not established in this scope. | Growth APP-024 alignment candidate; general worker changes unassigned pending demonstrated need |
| Telemetry | `src/ai/providers/ai-provider.service.ts` (`logAiEvent`, retry/timeout handling) | Partial: model, tenant/request correlation and failure events exist. Complete token/cost/outcome lineage is not proven by this inspection. | APP-015 evaluation / APP-033 integration; no separate telemetry project |
| Growth and publishing | Governance `INTELLIGENCE_MVP_ROADMAP.md` identifies APP-024 diagnostic-report scope | Specified future direction; tenant website/audit/publishing implementation not established by this bounded inspection. | APP-024 only where existing scope fits; SEO/GEO/publishing expansion requires separate proposal |

Verified structural sketch: domain modules → existing injected `AiProviderService` → OpenAI-shaped completion client; `ToolRegistryService` supplies tool descriptions. Proposed future seams: distinct validated generation/decision contracts → server-authorized domain actions → authoritative results. Existing SMS recovery is domain-specific, not a verified general event bus.

Resume at the current R11 boundary: obtain a future attended window and authorization for read-only provider/target refresh and fresh packet preparation; review the exact resulting packet before separate execution approval. Do not reuse consumed operations or restart R08. This amendment does not execute that next action. Extensible by evidence and small boundaries, not premature rewriting.
