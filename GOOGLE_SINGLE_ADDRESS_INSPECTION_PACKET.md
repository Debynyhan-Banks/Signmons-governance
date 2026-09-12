# Single-address inspection packet — review only

## Read-only preflight — 2026-09-12

Verified API enabled in signmons. Service Usage returned effective validate_address_requests limits of 5/min/project and 10/day/project; these do not enforce this packet's one-request limit and remaining daily usage was not established. Active CLI principal is debynyhan@signmons.com, not the backend runtime identity.

Runtime service account signmons-calldesk-runtime@signmons.iam.gserviceaccount.com has only roles/firebaseauth.viewer in the inspected direct project bindings. Inherited/group/conditional effective authorization was not resolved; do not assert all access is absent. Listed Firebase browser key API restrictions omit addressvalidation.googleapis.com; no key value retrieved or restriction changed. Backend source uses OAuth, so this key is not a substitute.

Official public [pricing](https://developers.google.com/maps/billing-and-pricing/pricing) lists Address Validation Pro at USD 17/1,000 first-paid-tier events and 5,000 free monthly events. USD 0.017/request is public list pricing, not verified account-specific terms, tax or remaining free allowance. Proposed USD 0.10 remains unapproved.

Google case addendum was sent with owner approval in the existing email thread; Gmail SENT message 1a097f693007a7e8, thread 1a096bbab636f717. Case portal explicitly directs replies by email. No substantive answer asserted. Earlier unsent references are historical.

Next concrete gap: qualify the existing OAuth execution identity and a one-shot runner without widening permissions or bypassing existing reservation gates. This is not blocked solely on the support reply. No address sent, provider request, configuration/IAM change or charge in this preflight.

Prepared 2026-09-12 under APP-013/2B. Preparation approved; execution, spending and support sending NOT approved by this packet. No county GIS dependency.

## Proposed bounded test

- One legitimate owner-confirmed U.S./Ohio service address, including the real unit if required. Collect privately just before execution; do not reuse a historical address without confirmation or commit it.
- One direct POST to https://addressvalidation.googleapis.com/v1:validateAddress; regionCode US, administrativeArea OH, enableUspsCass true. No autocomplete, geocoding, follow-up correction or SMS. No invented live fixture address.
- Project/quota project: signmons. Existing backend GoogleAddressOAuthTransport uses OAuth cloud-platform scope and X-Goog-User-Project signmons. This is inspected source behavior, not verified current credential readiness.
- Proposed run ceiling: ONE provider request and USD 0.10 reserved application liability. This amount is a proposed allowance, NOT an asserted Google rate, account-wide billing cap or existing approval. Recheck current applicable rate/taxes and refuse if the conservative bound exceeds it. Free allowance is not assumed.
- Single invocation, no automatic retries. Existing transport's eight-second deadline and 64 KiB response ceiling apply. Abort does not recall an in-flight request; uncertain outcome consumes the attempt and keeps liability pending.
- Examine field presence/type/code width and physical-address signals in process. No raw response/error headers, responseId, address, coordinates or credentials in terminal logs, screenshots, chat, repository, cache or backup. Do not automatically persist derived findings pending retention review.
- Stop immediately after response/timeout; no job, payment, booking, current-proof admission or app deployment. This is wire-shape inspection, not end-to-end acceptance.

## Unresolved preflight gates — do not label executable

1. Confirm participant/address privately and acknowledge Google/USPS processing; approve the one-request/USD 0.10 proposed ceiling and exact short UTC window.
2. Identify exact existing staging credential principal and effective API permission/quota-project access read-only. No IAM grant, secret retrieval/change, API enablement or key restriction change inferred. An API-restricted browser key is not automatically a server OAuth credential.
3. Verify applicable account rate and existing request restrictions/usage. Never rely on budget alerts to enforce the run limit.
4. Qualify an executable one-shot runner that wraps the existing transport with pre-dispatch approval/liability reservation and no-log private input. Existing FIXTURE_ONLY operation policy is not live authorization. Do not silently bypass it with curl or direct Console trial.
5. Resolve what sanitized findings may be retained. If this is unsettled, do not capture the response for later review or claim live acceptance from undocumented observations.

No production/IAM workaround is proposed. If a gate fails, stop before dispatch and identify that gate rather than repeatedly creating new generic test sections.

## Owner review

Review the one-request limit, private address handling, USD 0.10 proposed allowance and explicit missing gates. Approval of the packet alone must not be reported as a successful request. After qualification, present the exact remaining execution authorization, not another broad roadmap.

APP-013/2B Now; 3/8 (37.5%) walkthrough acceptance unchanged. Runtime unchanged.
