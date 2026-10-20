# APP-013 / 3A / P07 startup-credential correction proposal

Status: **Alternative 1 owner-approved for package preparation and local testing; no external action is authorized**. On October 20, 2026, Debynyhan Banks replied **“yes i approve”** to the exact four-secret correction presented after source inspection demonstrated production-startup requirements not enumerated in `APP013_P07_REPAIRED_DIGEST_RUNTIME_READINESS_PROPOSAL_20261020.md`. The supplied 6:45–8:15 p.m. Eastern availability block remains unattempted and unconsumed; no executable command was issued and its proposed allowance was not used.

## Requirement traceability and demonstrated gap

- Approved section: R1-W01 / APP-013 / 3A / P07.
- Acceptance criterion served: start the exact repaired image at zero normal traffic so the later separately approved same-job Stripe Sandbox Checkout and authentic signed-event proof can use the repaired payment path.
- Connected customer workflow: enforce payment policy -> request/recover payment -> accept only the exact signed settlement -> clear the booking gate.
- Exact repaired source/image remain commit `465e12cf7ecf4874ddbd13a34bee60d85fbb02bd` and digest `sha256:36f887749947c0b01db683482c081ca663534e7ffe597560b24597f3d46be9da`.
- Inspected source evidence: `src/config/env.validation.ts` requires `OPENAI_API_KEY`, `ADMIN_API_TOKEN`, a 64-hex-character `CONVERSATION_DATA_ENCRYPTION_KEY`, and `TECHNICIAN_LINK_SECRET` in production. `AiModule` constructs its OpenAI client during application composition, and the conversation cipher validates its key during provider construction. These are startup dependencies even though AI, admin, conversation and technician flows are outside the bounded payment proof.
- Missing approved behavior: the dedicated identity was approved for access to only the P07 database secret, existing Stripe test key and P07 webhook secret. A revision retaining the current service's secret references would require unapproved access to shared credentials; a revision with only the three approved secret references cannot satisfy production startup validation.

This is a material readiness prerequisite inside existing P07. It does not add a feature, acceptance section, ledger row or denominator. No application change, rebuild, role, secret, IAM binding, deployment, provider action or payment follows without the owner's decision and a later exact live-operation approval.

## Alternatives

| Alternative | Effect | Recommendation |
| --- | --- | --- |
| 1. Create four dedicated, short-lived P07 startup secrets | Generate independent random values for the OpenAI placeholder, candidate-only admin token, conversation key and technician-link key; give the dedicated identity resource-level access; pin numeric versions; disable them at the same fixed retirement deadline. The OpenAI value is deliberately invalid and cannot authorize model use. No accepted/shared runtime credential is exposed. | **Recommended** |
| 2. Give the dedicated identity access to the four existing shared runtime secrets | Fewer new resources, but the payment candidate gains reusable OpenAI, admin, encryption and technician credentials belonging to the serving runtime. Compromise or misconfiguration crosses the proposed isolation boundary. | Reject |
| 3. Change application composition/validation so a payment-only revision can start without these dependencies, then rebuild | Produces the narrowest eventual runtime but adds application design, tests and another image build before the Sandbox proof. It risks turning readiness into a separate payment micro-runtime. | Defer to a later architecture improvement |
| 4. Run the candidate with `NODE_ENV=test` or known literal placeholder credentials | Avoids secrets by weakening production validation or exposing predictable candidate credentials on a public tagged revision. It would not prove production-equivalent readiness. | Reject |

## Exact Alternative 1 correction

Add these four resources to the already approved readiness design:

- `signmons-staging-p07-disabled-openai-key`
- `signmons-staging-p07-admin-token`
- `signmons-staging-p07-conversation-key`
- `signmons-staging-p07-technician-link-key`

Each resource receives exactly one generated value through hidden standard input and one returned numeric version. Values never enter command arguments, files, chat, receipts or logs. The OpenAI placeholder must be a random non-provider token and the operation must refuse an `sk-` or `rk-` prefix. The conversation key must be 32 random bytes encoded as 64 hexadecimal characters. The admin and technician values must be separate random values of at least 32 bytes. No value is copied from an existing secret.

The dedicated service identity receives resource-level `roles/secretmanager.secretAccessor` on these four resources in addition to the three previously approved resources. No project-level role, service-account key, P06 secret, Twilio/Resend credential, Firebase privilege, provider-capable OpenAI key or shared admin/crypto/signing credential is included.

Deployment must replace, rather than inherit, the revision's application environment and secret maps. The allowlisted plain environment disables controlled intake, webchat tools, notifications, SMS, scheduling, staging phone and background work; sets production/test-mode payment configuration; and retains only non-secret values required for liveness/readiness. The allowlisted secret map contains exactly the seven numeric references: P07 database, existing Stripe test key, P07 webhook secret and the four dedicated startup secrets. Local controller tests must prove inherited secret references and functional Twilio/Resend/OpenAI/customer-intake configuration cannot survive.

The candidate remains at zero normal traffic, minimum instances zero, and the Stripe destination remains disabled. The later P08 proof may call only the exact payment endpoints authorized by its separate package. No AI, admin, conversation, technician, customer-intake, messaging, scheduling or model-use action is authorized.

## Cost, cleanup and impact

Alternative 1 adds four temporary active secret versions. Together with the already proposed P07 database and webhook versions, the readiness state can add six active versions. At the proposal's cited USD 0.06 per active version-month above the account free tier, the conservative full-month equivalent rises from USD 0.12 to USD 0.36; the operation must retire all six new versions within 24 hours, so actual metered cost should be prorated but remains unverified. The existing USD 1 operational allowance is unchanged and is not a provider-enforced cap.

Mandatory success retirement and any failure containment must disable all four startup versions, remove all four added access bindings, and read back their absence alongside the already specified P07 cleanup. Creation or cleanup uncertainty is a contained failure. Destruction of secret versions remains excluded.

The correction does not change the fixed P07 result: `P07_REPAIRED_RUNTIME_READY_DISABLED` remains readiness evidence only. P08, Checkout, card entry, event delivery, payment, booking and 3A acceptance remain separately gated. Accepted progress remains **0/27 newly closed R1 packages; 6/60 legacy packages; 4/8 walkthrough milestones; 0/13 full-intelligence rows**.

## Decision required

**Owner decision recorded:** Alternative 1 is approved. This authorizes only preparation and local testing of a fresh exact package with the four added dedicated startup secrets, seven total resource-level secret bindings and corrected cleanup/cost bindings. It does not authorize any database, IAM, secret, Stripe, deployment, cost-bearing or cleanup action. The implementer now prepares and tests the fresh no-action package; because the 6:45 start block was not safely bindable, the owner then supplies a new attended block of at least 90 minutes. The finished operation is presented separately for exact live approval.

**Approved scope deviation before implementation:** add four short-lived candidate-only startup secrets and their resource-level bindings because the already built application cannot start in production without them. No external implementation has occurred.
