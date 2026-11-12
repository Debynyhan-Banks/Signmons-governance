# APP-013 / 3A / P08 — TR6 fresh owner browser sign-in

PREPARED, NOT APPROVED. Source backendcd9c46352fc6644e9c76ed20f986a701b13b3182. CV2 is consumed/closed: its one cached-token check did not cover the requested 8:15 a.m. November12 horizon. Today is November12; no prior time window or sign-in authority carries forward. Owner approved preparation. This repeats the existing reviewed TR4 procedure under a new reservation and exact decision, not a consumed operation.

## Exact operation for review

One invocation of `/opt/homebrew/bin/gcloud auth login debynyhan@signmons.com --force --no-activate --brief --quiet --verbosity=none` using installed SDK583.0.0. Owner selects **debynyhan@signmons.com**, not personal Gmail, and completes Google sign-in/MFA/consent directly in the browser. Assistant never enters passwords or copies authorization codes. No manual-code fallback or second invocation.

Approve standard SDK scopes: openid; userinfo.email; cloud-platform; appengine.admin; sqlservice.login; compute; accounts.reauth. Full scope URLs and installed source hashes are in APP013_P08_TR6_SOURCE_READINESS_20261112.json. Existing granted scopes were not inspected. No Drive scope, custom scopes, ADC update, impersonation, alternate configuration or credential-file import. --force avoids cached-login selection; --no-activate preserves active account/project configuration, independently checked before/after. Wrong-account/cancellation/failure stops.

Explicit exception: SDK OAuth browser/callback/authentication traffic, SDK-managed internal retries and persistent credential/token/cache metadata maintenance for this exact owner. One invocation does not bound internal authentication request count. Stdin/stdout/stderr are DEVNULL; child controls disable file/HTTP logs, prompts and usage reporting. Browser session and authorized SDK credential writes are retained; no signout/revocation rollback. No provider-resource probe, SQL, IAM, API enablement, Firebase, payment/Stripe, billing, deployment, customer action or new spending. USD0 incremental spending authority.

## Time, reservation and cleanup

November12 Eastern: earliest7:20a.m.; launch strictly before7:30a.m.; one300second sign-in; independent closure by7:37a.m. One conditional cache postcheck requires expiry strictly beyond8:15a.m. (2026-11-12T13:15:00Z). That horizon is not attendance consent or downstream execution authority.

Reservation owner-signin-20261112-tr6; receipt directory backend evidence/APP-013/p08-narrow-access-check-local-20261101/renewals/20261112-tr6/. Exclusive0700 directory,0600 entry.lock/attempt.json/result.json/receipt-verification.json and nonblocking lock; existing reservation refuses. Use pinned Python3.14.2 and existing packet.renewal_preflight with actual committed decision, source/SDK/runtime/config/current-clock gates. Existing wire action APPROVE_TR1_CREDENTIAL_RENEWAL_SDK_RETRY_CACHE_AND_CLEANUP is retained only for compatibility; exact TR6 reference/proposal hash/source/reservation/window and argv must all match. Do not use the stale historical native_readiness source graph or change historical pins.

Verify all9additional sign-in SDK files against committed readiness before launch. Reject ambient credential/proxy/config overrides. One directly owned process group with monotonic300second bound, closed stdin/output and SDK's existing ephemeral OAuth callback. On timeout/interruption terminate/reap only the still-owned group, bounded TERM then KILL; verify leader reaped/group absent. No guessed/reused PID signals or unrelated tab closure. Unknown closure is not success. Do not create another auth listener.

Only clean exit0, owned-group absence and unchanged exact configuration permit ONE cache read, reserved first, through existing access_check.read_cached_token inside its8second deadline. Discard the token immediately; retain no token, expiry, raw SDK output, authorization URL or code. Output only VALID_THROUGH_CUTOFF or safe refusal. Failure stops without retry, credential repair or recovery. Independently verify receipt inventory/modes/single links, source/decision/counts and process absence; remove only owned temporary executor artifacts. Authorized browser/SDK state remains. Exit0 alone is not credential validity.

## Readiness and section card

Reuse unchanged TR4 command/procedure, PA1 actual preflight and existing cache helper. NQ1 remains locally verified, not live-authorized. Demonstrated gap: no currently verified token horizon for fresh native preflight qualification. This operation resolves only that prerequisite to the existing3A same-job payment criterion; it does not demonstrate payment or award acceptance.

Local checks: actual current/committed source graph and non-secret configuration; installed SDK hashes; pinned runtime; original receipt directory absence; actual renewal preflight with proposed authority only. Prior five AST-level sign-in cases are historical proof against the same reverified SDK hashes, not newly run browser tests. Browser availability, user OAuth consent, returned credentials and usable horizon remain UNKNOWN. Those are the bounded qualification purpose; no credentials/provider reads during preparation.

Finite checklist after exact approval: preflight/reserve; one sign-in; one conditional cache validity check; independent process/receipt closure; sanitized outcome. Implementer owns command/source/time/privacy/closeout; owner handles sign-in and approves seven scopes plus SDK retry/cache exception. Required frozen-baseline, consistency, governance25, architecture and whitespace checks apply. No new implementation or subsystem. Accepted1A/1B/2A/2B4/8;3A OPEN;R1newlyclosed0/27. No scope deviation; fresh external exception proposed only.

Terminal visibility check passed with dummy input; no password retained. Owner availability through8:15a.m. is confirmed. Browser sign-in is handled directly by owner; future SQL prompts must be in the visible standalone Terminal. TR5 and R31 remain consumed. No repeat under historical authority.
