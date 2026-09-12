# Signmons-managed communications

Status: owner-approved architecture direction, 2026-09-12. Documentation only; not implemented or production-approved.

## Decision and ownership

Clients use Signmons for voice, SMS and application email. Signmons operates Twilio for voice/SMS/verification and Twilio SendGrid for application email. Clients are not expected to create or operate provider dashboards in the standard managed offering.

Signmons owns the platform provider accounts, operational configuration, usage accounting and provider billing. Each client retains its business identity, approved brand voice, communication permissions and customer relationships. Eternity Mechanical Services is the first pilot tenant, not the owner of Signmons infrastructure.

The existing Eternity Resend account and website remain separate and untouched. Its free plan and usage are not evidence of Signmons email readiness or cost. This decision does not authorize disabling, migrating or replacing existing website delivery.

## Target separation

| Component | Target structure |
| --- | --- |
| Twilio | Signmons parent account with one managed subaccount per client; client-specific numbers, messaging services, registration and usage attribution |
| SendGrid | Signmons parent account with client-specific subusers and authenticated sending domains as the multi-client offering scales; qualifying plan and availability must be verified before purchase |
| Signmons | Server-enforced organization boundaries for recipients, sender identities, policies, message history, credentials and cost attribution |
| Environments | Isolated test/live configuration; nonproduction recipient allowlists; live sending disabled until separately approved |

Twilio subaccounts and SendGrid subusers are different provider resources and must be mapped independently to the same internal organization. They do not replace application tenant authorization. Credentials must never be supplied to a client browser.

For a one-client pilot, a dedicated Signmons SendGrid account may avoid premature purchase of multi-client features. This is a possible phased implementation, not proof of isolation readiness for additional clients. Before a second client is activated, explicitly review and approve the isolation design and required plan.

## Client onboarding and identity

Collect business identity, authorized representative, approved brand voice/templates, reply destination, phone-number authorization and applicable domain authorization in Signmons onboarding. Automate provider submissions where supported and expose truthful pending/approved/rejected states. Provider approval cannot be guaranteed or bypassed.

For U.S. local-number A2P SMS, register the appropriate customer profile, brand and campaign for each client under the ISV architecture. Signmons' own registration does not automatically authorize unrelated businesses' messages. Toll-free or other number types require their applicable approval paths.

Use an authenticated client sending domain where authorized. A Signmons sending subdomain with a clear “Client business via Signmons” identity is a possible pilot alternative requiring sender-policy approval; never spoof an unverified client domain. Route replies only to an approved destination. SendGrid is application email infrastructure, not a replacement for business inbox hosting.

## Reliability and cost controls

Require current recipient eligibility, channel-specific consent/purpose rules, suppression and opt-out handling, approved templates, duplicate-send protection, bounded retries, signed callback validation, delivery/bounce tracking, audit history and per-client kill switches. Account approval or phone access proof alone is not consent or send authority.

Signmons pays provider costs and bills clients through its own approved pricing. Track fixed number/registration/plan fees separately from variable voice, SMS segments, verification and email costs. Allocate shared costs explicitly; do not assume a flat cost per message or double-count a shared allowance.

Twilio subaccounts share the parent balance; account segmentation is not an enforced per-client spending cap. Define application-enforced client limits, shared fraud controls and reconciliation before live scale. Parent account suspension remains a shared operational risk.

SendGrid has separate email plan economics; do not assume the Twilio balance includes email. Exact plan, overage behavior, renewal costs and budget require current account verification and explicit spending approval. Marketing campaigns and advanced sales/advisor features remain outside this decision's MVP scope.

## Approval checklist and next bounded work

- Confirm whether a Signmons SendGrid account already exists and record ownership without exposing secrets.
- Map the existing Eternity pilot resources to the proposed tenant/subaccount structure; review any migration separately.
- Verify the required pilot plan and multi-client upgrade path, including actual charges and spending controls.
- Prepare the exact sender/domain, DNS, credentials, consent, callback, test-recipient and rollback packet for review.
- Obtain separate approval before provisioning, DNS/IAM/secrets changes, paid plans, number purchases/ports, migrations, live sends or deployment.

APP-013 remains sole Now; Next remains empty; FE-014 remains paused. This does not add a ninth steel-thread section, accept an unfinished milestone or authorize implementation. Existing eight-section acceptance remains 3/8 (37.5% of milestones, not engineering completion); 2B live-verification gates remain unresolved. Other MVP acceptance counts and completion estimates are unchanged.

## Official architecture references

Reviewed in the owner discussion on 2026-09-12:

- [Twilio ISV onboarding and preferred subaccount architecture](https://www.twilio.com/docs/messaging/compliance/a2p-10dlc/onboarding-isv)
- [Twilio subaccounts and shared-parent risks](https://www.twilio.com/docs/iam/api/subaccounts)
- [Twilio account and subaccount billing](https://help.twilio.com/articles/360011132374-Getting-Started-with-Twilio-Accounts-and-Subaccounts)
- [SendGrid subusers and eligibility](https://www.twilio.com/docs/sendgrid/ui/account-and-settings/subusers)
- [SendGrid architecture planning](https://www.twilio.com/docs/sendgrid/onboarding/email-api/evaluate-and-plan-your-strategy)
- [SendGrid email plan pricing](https://www.twilio.com/en-us/products/email-api/pricing)
