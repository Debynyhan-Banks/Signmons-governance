# Proposed tenant SMS policy configuration contract

2026-09-12. Design only; no implemented API/schema or production approval. Companion: PILOT_PRIVACY_AND_TERMS_DRAFT.md. Public support/privacy email approved: ben@eternityhvacr.com for Eternity only.

## Trusted source

Owner/admin-approved server-side policy must bind the internal organization, legal sender, declared transactional purpose, support contact, immutable disclosure text/version, Privacy Notice and Messaging Terms versions/URLs, effective time and approval audit reference. Resolve organization from the authenticated customer-session binding, never a browser-selected tenant ID.

Policy lifecycle: DRAFT -> REVIEWED -> PUBLISHED_VERIFIED -> CAPTURE_ELIGIBLE, each an explicit audited transition. Suspension or replacement invalidates outstanding capture prompts. None of these states enables delivery. PUBLISHED_VERIFIED requires actual stable public pages and content matching the reviewed versions, not merely syntactically valid URLs.

No application enum, storage field or route is created by this design document. Select existing policy/approval seams and document the additive contract before implementation.

## Public and private boundaries

The browser receives only display identity, disclosure, public support contact, public policy links and an opaque expiring prompt binding. Provider credentials/account IDs, private representative contacts, EIN and other tenants' configuration never appear in that response. Use an approved HTTPS host/path allowlist; reject credentials, fragments, tracking/private tokens, placeholders and unsafe schemes. Do not let user URLs become arbitrary server-side fetch destinations.

An administrator must verify publication through a controlled review process; recurring public checks, if later implemented, need SSRF defenses and explicit scope.

## Capture and revocation

Revalidate current policy version, organization/session, recipient phone and revision, purpose and prompt expiry in the server transaction. Bind the stored evidence to the exact displayed disclosure and policy versions. Exact retry must not duplicate evidence or extend permission. Refuse changed inputs and stale/foreign prompts.

Missing policy, unpublished URLs or an unapproved contact keeps enrollment unavailable while permitting the underlying request. Unchecked/skip creates no new grant and must not clear a prior opt-out. Separate revocation owns withdrawal. Preserve existing suppression precedence; no historical replay automatically grants consent.

No reusable consent grant is created by an OTP, an email choice, a job event, a checkbox alone or another organization's policy. A saved consent receipt is not a sent message, booking, admission or payment authorization.

## Testable implementation boundary

Use injected fictional policy sources and local policy pages to test eligibility before live publication; label all resulting evidence fixture-only and unusable by production delivery. Production capture remains disabled until a real approved policy source is configured. This avoids treating live publication as a prerequisite for testing the implementation.

Acceptance tests: missing configuration; unsafe/foreign URL; stale version; changed phone; wrong tenant/session; expiry; skip; existing opt-out; duplicate retry; rollback/unknown commit; restart; access control; keyboard/mobile; unchanged request continuation; zero provider calls and no delivery-authorized state.

## Next bounded implementation proposal

Implement the trusted policy reader and fixture-only prompt/capture integration in the existing intake, with local pages and evidence isolated from live consent. Do not activate provider sending, create real accounts, publish policies or change existing real consent. Final schema/transport mapping and tests must be reviewed against current DATA_CONTRACTS.md before edits. Existing APP-013 owner approval for local intake implementation remains; missing public URLs alone must not trigger another indefinite series of documentation-only sections.
