# APP-013 P06 runtime-wiring source card

## Status and authority

Shared-request-budget implementation detail (owner continuation after assets): reuse existing AuditLog as append-only bounded reservation/bind/release events; no schema/migration. Explicit packet-lifetime (maximum 15 minutes) global/tenant/session/start/in-flight limits, not sliding windows. PostgreSQL advisory transaction lock keyed by packet serializes instances; database clock enforces expiry; immutable policy digest prevents cap changes/restart resets. Session identity comes only after credentials verification; global admission precedes body reading. Async release is awaited/caught and never refunds request counts; crashes/unavailable release retain in-flight slot until packet expiry. No forwarded-IP keys, payloads, OTP, token, provider calls or live activation. Expected files: shared-customer-browser-budget.ts/spec, existing budget interface and transport/spec, guarded disposable database verifier. Positive/cap/session/expired/config mismatch/DB failure tests, concurrent independent-client/restart durable proof, full existing gates. Phone monetary admission remains separate and pending; these are HTTP abuse limits only.

Owner decision 2026-09-14: "yes i approve continue" approves recommended same-origin backend asset packaging and PostgreSQL-backed shared admission/budget, including the controlled customer admission adapter, for disabled implementation. No release/paid approval. Reconciled remote planning 2501c6e/29f160f with preserved local phone boundary 5f9a9be/9c9945f; both histories retained. This decision supersedes the implementation-review block below. APP013_P06_RUNTIME_CARD.md records the already-tested phone-boundary substep, not a competing plan.

Bounded delivery substep: package only existing customer-intake-journey.html/.js in Docker, add optional customerIntakePage middleware exposing exact GET /customer-intake and /customer-intake.js, default closed, no tokens/clients or directory serving. Immutable server-loaded bytes, no-store, nosniff, frame denial, self-only scripts/connect and hash-authorized existing inline style; rewrite only existing script URL and controlled marker. Do not add phone UI until actual wired path. Tests real HTTP disabled/GET/method/unknown paths, CSP/script mapping, no cookie/credentials, unrelated routes; existing Playwright harness must load middleware-delivered same page at 390/1440. Build/lint/full Jest/architecture/audits, Docker-copy source assertion, existing disposable database/browser gate and governance checks. Shared-budget/runtime/phone-browser implementation remains under this same approved card, not a new package. No image build or deployment.

Prepared on 2026-09-14 from backend `d07ff3543b86a62112b50972a28fc89c155bf477` and governance `3c37077ba6f7c15ea6a93b90be9b376b2e09cdd7` after the owner-authorized P06 entry reconciliation. This is P06 item 2 preparation inside existing APP-013 section 2B. It is not a new package, implementation approval, release approval, provider-call approval or acceptance.

The card is **source-complete but blocked for implementation review**. It identifies the exact existing seams and a finite recommended patch. The owner must approve the material page-delivery and shared-admission choices before code because the current runtime has neither. No scope deviation is implemented.

## Existing acceptance and observable finish

- Existing acceptance ID: APP-013 / 2B, P06 item 2 connected runtime wiring.
- 2B criterion served: one protected customer journey must obtain current phone access and eligible address evidence, preserve the customer-reviewed draft, and create exactly one job only through the existing controlled admission transaction. Job creation grants no payment, booking, dispatch or send authority.
- This card's finish: name every source, interface, state, retention boundary, test and owner decision required for the default-disabled connection. It does not itself satisfy P06 item 2.
- Subsequent implementation finish: the existing customer journey page, actual pre-parser HTTP mount, actual durable phone service, actual controlled address/admission composition and disposable PostgreSQL create one job in one local same-page flow using synthetic Twilio and Google ports. Refusal, uncertainty, replay and correction remain truthful. No fixture flag, pre-provisioned phone proof or positive admission mock is permitted.

## Verified source inventory and missing behavior

| Source at backend `d07ff354` | Reuse | Exact missing behavior |
| --- | --- | --- |
| `src/main.ts` | Pre-CORS/pre-parser mount; `rawBody: true`; Nest resources | Calls `customerSessionHttp()` without a binding. No loader can produce a reviewed binding. |
| `src/communications/customer-session-http.ts` | Namespace isolation, sanitized no-store refusal, request context, stream ownership | Accepts direct socket TLS only. Cloud Run terminates TLS before the container, so `req.socket.encrypted` is false by design. It has no server-owned managed-TLS mode. |
| `src/communications/customer-consent-browser-transport.ts` | Exact host/origin/fetch-metadata/header/body/session checks; controlled v2 submit | `phone`, `verify`, `address`, `correction` and `end` are fixture-loopback-only. There is no controlled customer phone port or controlled session close path. |
| `src/communications/controlled-intake-composition.ts` | Replay-first intake, authority, phone-current read, address ledger/transport, final admission | Has no deployed resource/configuration loader. Address policy, capability, keys, account and transport are supplied only by tests. |
| `src/communications/durable-verification.service.ts` and `twilio-verify.adapter.ts` | Durable one-START/five-CHECK ledger, uncertain outcome, controlled phone proof, bound Twilio adapter | No customer-journey admission policy or runtime loader. The controlled proof exists only when a real `TwilioVerifyAdapter` and current controlled policy are injected. |
| `src/communications/staging-phone.service.ts` / `staging-phone-admission.ts` | Prior closed staging test and account-serialized held liability pattern | Operator-authenticated, fixed-session/fixed-phone and legacy route only. It cannot be mounted as the customer path or activated by `STAGING_PHONE_TEST_ENABLED`. |
| `src/communications/verification-budget-admission.ts` | Same-transaction reservation shape | Explicitly `FIXTURE_ONLY`; not a production approval/rate source. |
| `src/communications/customer-consent-browser-budget.ts` | Local request/in-flight limits | Explicitly in-memory and single-binding. Restart resets it; Cloud Run can have multiple processes/instances; socket peer is the Cloud Run proxy, not a qualified customer identity. |
| `src/communications/customer-intake-continuation.service.ts` | Server-side approved-organization reply, draft, exact controlled reader/writer | Can reuse `continueOrganization`; no new AI collaborator is needed for this P06 flow. It still needs reviewed construction with Prisma, cipher and customer credentials. |
| `scripts/fixtures/customer-intake-journey.html/.js` | The same P05 customer page and truthful states | Test-only. It has no browser phone-code journey. |
| `scripts/verify-controlled-intake-connected-browser.mjs` | Actual HTTP/transport/composition/browser assertions | Pre-provisions phone proof before browser interaction. It does not prove customer START/CHECK through HTTP. |
| `Dockerfile` | Backend build/runtime | Runtime copies only `dist`, dependencies and Prisma. It does not ship `scripts/fixtures`, `ui/out` or any customer page. |
| `ui/src` | Existing static operator/customer appointment surfaces | Contains no protected intake page. Static hosting is separate from the backend and no same-origin BFF mapping is recorded. |

## Current managed-runtime facts

Read-only service metadata on 2026-09-14 confirms `signmons-calldesk-staging` in `us-east5`, service identity `signmons-calldesk-runtime@signmons.iam.gserviceaccount.com`, container port 8080 and service ingress `all`. Normal traffic remains 100% on `signmons-calldesk-staging-app013bounds`; this card changed nothing.

Official Cloud Run documentation states that the `run.app` URL accepts HTTPS, Cloud Run terminates TLS, and the container receives proxied cleartext HTTP. It also states that ingress `all` permits direct internet access to the `run.app` URL. Therefore:

1. `req.socket.encrypted` cannot be required inside Cloud Run.
2. `Forwarded` or `X-Forwarded-Proto` must never be treated as independent authority from an arbitrary request.
3. A server-owned startup binding may attest `CLOUD_RUN_MANAGED_HTTPS_V1` only when the immutable release packet matches the exact service/configuration/revision/origin and the owner has approved that release.
4. The current public ingress and absent shared admission layer are release blockers, not facts that configuration alone can waive.

Sources: <https://docs.cloud.google.com/run/docs/container-contract#transport-layer-encryption-tls>, <https://docs.cloud.google.com/run/docs/triggering/https-request#http-to-https>, and <https://docs.cloud.google.com/run/docs/securing/ingress#available-network-ingress-settings>.

## Recommended finite patch, pending owner approval

### 1. Immutable, default-disabled runtime configuration

Add `src/communications/controlled-intake-runtime-config.ts` with one strict parser for a server-owned versioned envelope. Absence, `enabled:false`, unknown fields, malformed values or any binding mismatch returns DISABLED and constructs no credentials/provider clients. The envelope must bind:

- exact project, service, configuration, revision, HTTPS origin/host, tenant, integration and packet IDs;
- activation validity window, allowed service categories, approved organization/payment digests and priority policy already required by `ControlledIntakeAuthority`;
- Twilio account/service, participant phone HMAC, notice/rate versions, per-flow/account limits and the one-run approval digest;
- Google project/address account, rate version, two-request/session limits, liability ceilings and execution deadline policy;
- active customer-session key ID and numeric secret-version labels only. Key/token values remain separate injected secrets and never enter the envelope or evidence.

No default tenant, origin, rate, budget, participant, key ID or provider identifier is allowed. `STAGING_PHONE_TEST_ENABLED`, fixture modes and prior packet values are not aliases.

### 2. Server-owned composition loader

Add `src/communications/controlled-intake-runtime.ts` returning either `undefined` or one frozen `ServerBinding`. It may reuse Nest `PrismaService` and `ConversationMemoryCipher`, and must construct exactly one shared instance set per process:

- `CustomerConsentCredentials` from an exact active key ID and at most two 32-byte session keys;
- `CustomerConsentResponseService`, `CustomerConsentCaptureService`, `CustomerIntakeContinuationService` using `continueOrganization`, and a controlled session lifecycle close port;
- `ControlledIntakeAuthority` whose current-state reader is `CustomerIntakeContinuationService.readControlledCurrentState`;
- `TwilioVerifyAdapter`, `DurableVerificationService`, a new controlled phone admission reader and the existing controlled policy proof;
- `GoogleAddressOAuthTransport`, controlled address policy reader and `ControlledIntakeComposition`;
- `CustomerConsentBrowserTransport` with distinct controlled ports. Fixture ports remain unavailable in production.

Construction must fail closed before listening if an envelope is enabled but incomplete. Disabled mode may start the rest of the API and keeps `/customer-session/*` at sanitized 503.

### 3. Managed-HTTPS request security

Change `customerSessionHttp` to accept a frozen server security binding with only `DIRECT_TLS_TEST` or `CLOUD_RUN_MANAGED_HTTPS_V1`.

- Direct mode retains the current socket-TLS and explicit 127.0.0.1 fixture tests.
- Cloud Run mode is valid only for `NODE_ENV=production`, exact `K_SERVICE`, exact `K_CONFIGURATION`, an allowlisted `K_REVISION`, container port 8080 and the exact HTTPS origin/host in the reviewed packet. It supplies `encrypted:true` to the transport because Cloud Run is the reviewed TLS terminator; request headers do not supply that fact.
- `Forwarded`, `X-Forwarded-Proto`, `X-Forwarded-Host` and socket peer values never grant tenant, session, TLS or activation authority.
- Origin/Host/Fetch Metadata/custom-header/session checks remain mandatory. Failure occurs before body read/provider construction.

This mapping qualifies transport only. It does not solve public abuse or page delivery.

### 4. Shared admission and phone boundary

Add an async `ControlledCustomerAdmission` interface backed by the existing PostgreSQL transaction and account/tenant/session locks. It must reserve liabilities before provider I/O, bind the first allowed fresh session to the reviewed one-run packet and participant HMAC, enforce one START/five CHECKs, retain ambiguous holds, refuse replay changes/restarts/revocation and expose no phone/OTP. It must not reuse the fixture budget or fixed-session staging runner.

Change `CustomerBrowserBudget.acquire` to permit an async shared implementation and add a database-backed global/tenant/session request budget for an enabled runtime. Because the current Cloud Run socket peer is not a qualified customer identity, forwarded client IP is not a key. Before a session exists, use the immutable packet/tenant/global window; afterward add session identity. This is a bounded correctness/security dependency, not an analytics or generic rate-limit platform.

Add a separate controlled phone port to the existing `verify` browser contract. Browser input maps only to durable `START` or `CHECK` with server-held notice/approval; receipt remains operation/state/outcome/usage plus all downstream authority false. `APPROVED` is displayed as phone access for this session, never SMS consent. The code value is transient request content and is not logged or returned. Editing phone invokes the existing proof revocation before a replacement attempt.

### 5. Same-origin page delivery

The current transport requires request `Host` to equal the configured page origin and the runtime image ships no page. One of these owner-approved choices is required before implementation:

- **Recommended minimal choice:** package the existing reviewed customer journey assets as immutable backend static assets and serve them from a narrow no-store `/customer-intake` GET on the same reviewed HTTPS origin. The page remains the existing P05 flow; add phone request/code states, not an alternate form. Asset responses contain no session token and use a strict self-only policy. Docker copies only those reviewed assets.
- **External BFF choice:** name an existing same-origin frontend/BFF and its exact Cloud Run/load-balancer mapping. This requires a separate resource/configuration diff and cannot be inferred from the current static operator UI.

Do not loosen Host/origin checks or add broad CORS to bridge separate origins.

### 6. Bootstrap, correction and close sequence

1. GET the reviewed same-origin page; no credential or provider action.
2. POST empty canonical JSON to `start`; shared admission reserves an anonymous start slot before a new protected session is committed.
3. Customer explicitly requests phone code; controlled phone admission and durable START reserve liability before Twilio.
4. Customer explicitly checks one six-digit code; durable CHECK may create current controlled phone proof.
5. Approved organization conversation, optional email choice and review-only draft continue using current protected endpoints.
6. Customer enters/confirms address and explicitly submits v2. Controlled composition rechecks current phone, address budget/policy, tenant/category/organization/payment/activation and exact draft/revision.
7. Provider I/O remains outside database transactions. Only transient Google review is consumed by the final existing admission transaction; no Google body/response ID/county/verdict survives.
8. ADMITTED exact replay returns the original receipt and never repeats phone/address/job work. CORRECTION_REQUIRED preserves draft and volatile sequence for one explicit correction. REFUSED preserves editable input. UNCERTAIN preserves exact retry identity and disables edits.
9. Explicit end closes the session and cleanup remains bounded; failed cleanup cannot restore authority.

No step authorizes payment, appointment, dispatch, delivery or confirmation messaging.

## Expected implementation files and exit tests

Expected new files: `controlled-intake-runtime-config.ts/.spec.ts`, `controlled-intake-runtime.ts/.spec.ts`, `controlled-customer-admission.ts/.spec.ts`, and a narrowly named shared browser-budget adapter/spec. Expected edits: `main.ts`, `customer-session-http.ts/.spec.ts`, `customer-consent-browser-budget.ts/.spec.ts`, `customer-consent-browser-transport.ts/.spec.ts`, `scripts/fixtures/customer-intake-journey.html/.js`, `scripts/verify-controlled-intake-connected-browser.mjs`, `scripts/verify-operator-intake-admission.mjs`, `Dockerfile`, `.env.example`, `config/env.validation.ts` and relevant evidence. If source inspection during implementation requires a schema migration, new cloud resource or a broader UI application, stop and propose the deviation before editing.

Finite exit matrix:

- configuration: absent/false/unknown/malformed/mismatched project/service/revision/origin/tenant/key/provider/rate/expiry refuses before clients and listener binding;
- ingress: local direct TLS passes; plain direct HTTP and forged/duplicated forwarded headers fail; reviewed Cloud Run startup binding passes without trusting request forwarding headers; wrong service/config/revision/host fails before body read;
- bootstrap/abuse: concurrent starts across two runtime instances admit only the packet limit; restart does not reset counts; budget/database failure refuses; no client-IP claim;
- phone: START/CHECK exact replay, wrong phone/session/tenant/notice/code/operation/start ID, expired/revoked approval, concurrency, provider timeout/unknown result, post-call persistence failure and restart; no automatic resend and no OTP/token logs;
- address/admission: accepted/outside/unknown/correction, second correction cap, phone/address/policy/session expiry, tenant/category/organization/payment change, duplicate/concurrent submit, job/audit rollback and post-commit lost acknowledgment;
- page: same page at 390/1440 performs phone request/code then draft/address/submit; zero browser storage, no overflow/page errors, exact retry, reload/close warning and truthful not-booked receipt;
- isolation: unrelated webhook raw bytes unchanged; legacy fixture and staging phone routes remain disabled; no SMS delivery, scheduling, background worker, Stripe live mode or dev auth enablement.

Required commands after approved implementation: focused Jest files; `npm run build`; `npm run lint`; `npm test -- --runInBand`; `node scripts/architecture-check.mjs`; `npx prisma validate`; both npm audits; disposable PostgreSQL two-process/restart harness; connected 390/1440 Playwright harness; backend governance check; governance frozen/full consistency, 21 regressions and both `git diff --check` gates.

## Retention, identity and recovery boundaries

- Browser session token and OTP stay in page memory/request bodies only; never URLs, logs, storage or evidence.
- Durable phone ledger keeps only existing encrypted operation state, HMAC-bound phone identity, provider-safe IDs/outcomes and unresolved liability metadata; no code or plaintext phone in audits.
- Google response content and correction response ID stay process-local for the existing bounded lifetime and are never durable. Job/audit records retain only current Signmons admission metadata already approved by the terms-first contract.
- Customer session possession authenticates that session, not legal identity, address ownership, SMS consent, payment or booking authority.
- Cloud Run can terminate/restart instances; in-memory correction state may be lost and must return truthful refusal, never repeat a provider call automatically.
- Provider timeout or crash retains liability and uncertainty. Operator review cannot manufacture proof or bypass current policy.

## Decisions, exclusions and rollback

Smallest owner decision before implementation: approve the recommended same-origin backend asset packaging plus PostgreSQL-backed shared admission/budget patch, or name the existing external BFF/load-balancer path that must replace it. Approval must also confirm that this finite P06 item 2 patch may introduce the controlled customer admission adapter described above; it does not approve item 3 release/configuration or item 4 paid run.

Implementer owns the code, synthetic local proof and evidence. Product owner owns the page/ingress/admission design choice and later exact release/provider actions. Item 3 must still bind image digest, numeric secret versions, tenant/participant/rates/caps, IAM/config/ingress diff and costs; item 4 still requires a fresh UTC window and explicit paid execution approval.

Excluded: deployment, traffic change, IAM/secrets, new load balancer or domain, live provider request, actual phone/address, production migration, payment, booking, SMS delivery, merge, new customer form, fixture promotion or legacy runner activation. Rollback/disabled state is absent or `enabled:false` runtime envelope, which leaves the current sanitized 503 mount and all six staging safety flags false.

Relative size: medium-high, low confidence until the owner selects page/shared-admission delivery and implementation confirms whether the database-backed budget can remain schema-free. Accepted packages remain 5/60 (8.3%); walkthrough remains 3/8 (37.5%). The provisional 4–8 weeks at 25–30 collaborative hours/week plus external waits is unchanged and low confidence.
