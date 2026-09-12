# Signmons-managed communications

Status: owner-approved architecture direction, 2026-09-12. Documentation only; not implemented or production-approved.

## Decision and ownership

Clients use Signmons for voice, SMS and application email. Signmons operates Twilio for voice/SMS/verification and native Twilio Email for application email. Clients are not expected to create or operate provider dashboards in the standard managed offering.

Correction approved 2026-09-12: native Twilio Email is the selected direction, replacing this document's initial separate SendGrid account/subuser recommendation. Twilio Email and SendGrid use related infrastructure but are distinct products. Do not purchase a SendGrid subscription or create a separate SendGrid account for this plan.

Signmons owns the platform provider accounts, operational configuration, usage accounting and provider billing. Each client retains its business identity, approved brand voice, communication permissions and customer relationships. Eternity Mechanical Services is the first pilot tenant, not the owner of Signmons infrastructure.

The existing Eternity Resend account and website remain separate and untouched. Its free plan and usage are not evidence of Signmons email readiness or cost. This decision does not authorize disabling, migrating or replacing existing website delivery.

## Target separation

| Component | Target structure |
| --- | --- |
| Twilio | Signmons parent account with one managed subaccount per client; client-specific numbers, messaging services, registration and usage attribution |
| Twilio Email | Use the same Twilio parent/client subaccount structure, with client-scoped email traffic and authorized authenticated sending domains; validate actual resource isolation before live onboarding |
| Signmons | Server-enforced organization boundaries for recipients, sender identities, policies, message history, credentials and cost attribution |
| Environments | Isolated test/live configuration; nonproduction recipient allowlists; live sending disabled until separately approved |

Map each internal organization to its approved Twilio subaccount server-side. Native Twilio Email supports subaccount traffic segmentation; this does not replace application tenant authorization or prove every resource's isolation. Credentials must never be supplied to a client browser.

Use Eternity as the first tenant of this structure. Before live use, test that sender domains, logs, suppressions, callbacks and credentials cannot cross tenant boundaries. Before a second client is activated, review isolation evidence and account-specific limits. Dedicated IPs and separate SendGrid plans are not MVP prerequisites established by this decision.

## Client onboarding and identity

Collect business identity, authorized representative, approved brand voice/templates, reply destination, phone-number authorization and applicable domain authorization in Signmons onboarding. Automate provider submissions where supported and expose truthful pending/approved/rejected states. Provider approval cannot be guaranteed or bypassed.

For U.S. local-number A2P SMS, register the appropriate customer profile, brand and campaign for each client under the ISV architecture. Signmons' own registration does not automatically authorize unrelated businesses' messages. Toll-free or other number types require their applicable approval paths.

Use an authenticated client sending domain where authorized. A Signmons sending subdomain with a clear “Client business via Signmons” identity is a possible pilot alternative requiring sender-policy approval; never spoof an unverified client domain. Route replies only to an approved destination. Twilio Email is application email infrastructure, not a replacement for business inbox hosting.

## Reliability and cost controls

Require current recipient eligibility, channel-specific consent/purpose rules, suppression and opt-out handling, approved templates, duplicate-send protection, bounded retries, signed callback validation, delivery/bounce tracking, audit history and per-client kill switches. Account approval or phone access proof alone is not consent or send authority.

Signmons pays provider costs and bills clients through its own approved pricing. Track fixed number/registration/plan fees separately from variable voice, SMS segments, verification and email costs. Allocate shared costs explicitly; do not assume a flat cost per message or double-count a shared allowance.

Twilio subaccounts share the parent balance; account segmentation is not an enforced per-client spending cap. Define application-enforced client limits, shared fraud controls and reconciliation before live scale. Parent account suspension remains a shared operational risk.

Native Twilio Email uses consolidated Twilio billing. Public pricing checked 2026-09-12 is $0.0013 per email sent, with no monthly base fee or feature tiers: 100 emails = $0.13; 1,000 = $1.30; 10,000 = $13.00, before any applicable taxes or account-specific terms. These are reference estimates, not measured Signmons charges or spending approval. Do not apply the separate SendGrid $19.95/month starting subscription to native Twilio Email.

Public documentation advertises a new-user 30-day trial with 100 emails/day; Signmons' existing paid account eligibility is unverified, so do not assume free sends. Verify account-specific rates, billing units, failed/retried-send charging and limits before a live test. Marketing campaigns and advanced sales/advisor features remain outside this decision's MVP scope.

## Approval checklist and next bounded work

### Pilot packet update — 2026-09-12

Owner-approved directions: retain the existing number for staging without reconfiguration; use a separate 216-area-code pilot number subject to price/availability/purchase approval; use the approved client email identity with owner-managed GoDaddy DNS; add optional unchecked service-related SMS consent in Signmons intake, with no marketing bundling and no service-request exclusion for declining.

The consolidated private packet contains owner-provided legal/representative details and the exact approved sender identity. No EIN value is stored. Do not publish private contact/address information in repository evidence. Consent wording remains a draft pending current requirements and Privacy/Terms link verification; no implementation or compliance acceptance is claimed.

Inventory review found no subaccounts and no authenticated native Email domains. Identity and consent-direction decisions are complete, but creation, number selection/purchase, registration, DNS/secrets, implementation and live-test approval are not. Next is read-only DNS and Signmons intake/policy readiness review before presenting exact setup actions and costs. The checklist below remains an execution gate, not permission to act.

Observed in the existing Safari Signmons LLC Twilio console on 2026-09-12: native Email is available in navigation, and Domain Authentication shows no authenticated domains. This is console visibility, not proof of delivery readiness, pricing entitlement or completed tenant setup.

The following items remain pending; none are approved by documenting this checklist:

- [ ] Inventory existing parent/subaccounts and Eternity pilot numbers, registrations and email resources read-only. Record tenant mapping without secrets; do not assume parent registrations cover Eternity.
- [ ] Identify the exact nonproduction/pilot account and any required resource migration. Obtain separate migration approval; do not move existing numbers or disrupt service.
- [ ] Verify native Email account eligibility, rates, quota, billing units, shared balance and application-enforced client/global caps. State exact maximum test spend.
- [ ] Approve sender identity, exact sending subdomain, Reply-To, domain owner and DNS administrator. Review DNS records and rollback without altering existing website or mailbox records.
- [ ] Define least-privilege account-scoped credentials and server-only secret storage, signed callback verification, suppression behavior and tenant routing. Test isolation without live recipients.
- [ ] Approve the named willing test participant, exact recipient allowlist, purpose/consent, message template, send count, retry ceiling, time window and stop conditions.
- [ ] Approve the implementation and controlled provider actions separately. Verify delivery evidence, duplicate prevention, bounce/complaint handling, billing reconciliation and rollback before acceptance.
- [ ] Obtain explicit approval before provisioning, DNS/IAM/secrets changes, purchases, number ports, migrations, live sends or deployment.

Next bounded action: read-only pilot resource inventory and an exact account/domain/cost approval packet. Do not start a separate SendGrid signup. Continue in the user's existing Safari Twilio tab; do not open another browser tab without request.

APP-013 remains sole Now; Next remains empty; FE-014 remains paused. This does not add a ninth steel-thread section, accept an unfinished milestone or authorize implementation. Existing eight-section acceptance remains 3/8 (37.5% of milestones, not engineering completion); 2B live-verification gates remain unresolved. Other MVP acceptance counts and completion estimates are unchanged.

## Official architecture references

Reviewed in the owner discussion on 2026-09-12:

- [Twilio ISV onboarding and preferred subaccount architecture](https://www.twilio.com/docs/messaging/compliance/a2p-10dlc/onboarding-isv)
- [Twilio subaccounts and shared-parent risks](https://www.twilio.com/docs/iam/api/subaccounts)
- [Twilio account and subaccount billing](https://help.twilio.com/articles/360011132374-Getting-Started-with-Twilio-Accounts-and-Subaccounts)
- [Native Twilio Email GA: existing accounts, billing and subaccount segmentation](https://www.twilio.com/en-us/changelog/twilio-email-ga)
- [Native Twilio Email documentation](https://www.twilio.com/docs/email)
- [Native Twilio Email usage pricing and product distinction](https://www.twilio.com/en-us/products/email-api/twilio-pricing)
