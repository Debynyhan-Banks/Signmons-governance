# APP-013 / 3A — authentication readiness after SV1 and AD2

Local source/evidence review only. Companion JSON records current source SHA/time and committed source/SDK verification. No provider/credential read, implementation, attendance request or new live authority.

## Findings through the actual path

native_child.mjs -> transports.createPorts -> boundClients -> coordinator adapters -> recovery sequence is inspected. Owner credential handoff, exact target/job/runtime/key binding, TLS, finite child budget and time checks remain. The signing payload uses the pinned runtime identity and reviewed custom-token audience; key retrieval verifies the owned key string digest; exchange requires exact localId/idToken; application authentication verifies claims and the registered authenticated job-reader response. Signing/key/exchange responses remain bounded and no issuance retry is permitted.

The existing qualification covers enabled APIs including IAM Credentials/Identity Toolkit/API Keys, exact role definitions, configuration/resource/secret pins and effective-permission evidence. Those checks do not call signBlob or exchange a token. Neither metadata nor policy results prove successful authentication. KQ3 remains historical live key-lifecycle evidence, IQ8 historical identity qualification; R49 passed runtime activation/readbacks17/17 but failed TOKEN_INTENT before application authentication. R49 discarded the specific substage; no later fixture can reconstruct it. No further local functional defect was identified by this review; absence of a discovered defect is not live readiness.

AD2 now preserves SIGN/KEY_READ/EXCHANGE, allowlisted failure category and nullable HTTP status through the actual child/journal boundary.38focused and65assembled native tests from the completed correction are historical local evidence; not rerun or treated as provider proof here. Source/SDK verification is freshly run. SV1 observed exact webhook version1 DISABLED and independently closed, resolving that current restoration question. R49's historical AUTH_OUTCOME_UNKNOWN remains immutable. SV1 did not query accounts or prove authentication.

## One named question for the next operation

If later authorized, the next existing connected attempt asks: can the actual source-bound signing -> owned key retrieval -> token exchange -> application authentication path complete, and if not, which exact safe substage/category/status refuses? This is new observable evidence from the corrected actual boundary, not a claimed fix to an established provider cause. Success may continue only within separately approved same-job Sandbox payment scope; failure ends the session after independent cleanup. No automatic retry or second full run.

No standalone auth-only live mode or safe mid-run resume is exposed by the existing connected workflow. Do not invent a partial live invocation or new diagnostic subsystem. Preparing the existing connected packet preserves its original sequence and runtime/IAM/key/account cleanup. A narrower new live mode would require a separately scoped change before implementation; none is proposed or approved by this review.

## Concrete next preparation, owners and UNKNOWNs

Implementer next prepares one fresh connected session card/spec/recovery draft and inert readiness using source d3d6e6b (full SHA in JSON), current source-derived limits and fresh IDs. Include dynamic qualification/native review templates and the named question above. Only after this preparation request attendance and any necessary credential renewal. No new timed session or launch is scheduled by this record. Current credential horizon, fresh bindings/current account/job state, usable API access and live authentication remain UNKNOWN. Fresh qualification must cover current entry conditions; do not promote earlier observations to current authorization. Existing runner has no single-password promise and retains one immediate identity readback; preserve both limitations.

Required sequence remains fresh credential prerequisite if needed -> recovery -> exact current qualification -> exact native decision -> one instrumented connected attempt -> independent cleanup/private purge -> actual result review. Existing maxima and retention/no-retry limits remain unchanged. Owner/cloud/DB custodians retain external/credential decisions; implementer owns readiness, exact command comparison, cleanup and evidence. Do not request user to attend an unprepared prompt.

Completed this section: actual-path review, known/unknown reconciliation and current source/SDK verification. Remaining customer outcome: authenticated same-job Sandbox payment, matching signed event/application gate, recovery/cleanup evidence and owner acceptance. Accepted1A/1B/2A/2B4/8;3A OPEN;R1newlyclosed0/27. No scope deviation. Next observable deliverable is a prepared existing-workflow session packet, not another diagnostic-code proposal.
