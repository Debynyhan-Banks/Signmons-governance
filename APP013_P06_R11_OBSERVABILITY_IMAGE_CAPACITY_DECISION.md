# APP-013 / P06 R11 observability-image and final-capacity decision

Status: alternative 1 owner-approved; the one image build succeeded and mandatory cleanup is verified. The one-future-packet policy is approved, but packet preparation and live execution remain separately gated.

## Demonstrated state

The owner accepted the controlled-refusal observability repair at backend `574f25a` and governance `ccbe4c8`. Current 6:45 AM read-only qualification found the Cloud Run baseline safe, the new candidate image tag absent, the existing build identity enabled with all three temporary grants absent, and the signed-in Twilio account still limited to the same one-service, Fraud-Guard-protected, United States SMS/voice-disabled and single verified-recipient boundary.

Consumed read-only operation `759d896c-767b-467b-b223-771afb6267de` found tenant/category present, phone approval inactive, runtime role closed with zero sessions, seven valid retained phone holds / 3,500,000 micros, four valid retained address operations / 400,000 micros at both aggregate scopes, and zero malformed rows. Its `PHONE_STATE_INVALID` label came only from comparing the consumed historical scope packet with its own expected retained hold; it is not evidence of corrupt liability or a future packet collision. The operation is consumed and will not be rerun.

Backend `574f25a` adds the fixed allowlisted refusal marker needed to identify any future controlled submit 409. It does not fix or identify the historical enabled21 refusal retroactively. At decision time, no registry image contained this repair. A reviewed local tracked-source archive was unuploaded and bound exact source `574f25a` to candidate tag `p06-r11-574f25a66952`.

## Alternatives

### Alternative 1 — one image build plus one future-capacity policy decision (recommended)

During the currently selected 6:45–7:30 AM Eastern preparation window:

1. Submit exactly one Cloud Build from clean backend `574f25a66952bd839a2b9b8eeb8943c643e68a8d` using existing `cloudbuild.deploy.yaml`, `Dockerfile`, `signmons-build@signmons.iam.gserviceaccount.com`, `E2_HIGHCPU_8`, a 1,200-second timeout, the existing `signmons_cloudbuild` source bucket and a USD1 operational allowance. The allowance is not an invoice or provider hard cap.
2. Push only `us-east5-docker.pkg.dev/signmons/signmons/signmons-calldesk-backend:p06-r11-574f25a66952`. Do not deploy it. One submission only; no automatic retry.
3. Temporarily grant only `roles/storage.objectViewer` on `signmons_cloudbuild`, `roles/artifactregistry.writer` on repository `us-east5/signmons`, and `roles/logging.logWriter` on project `signmons`. Remove and read back all three immediately after terminal success or failure. Any build ambiguity or cleanup failure stops.
4. Preserve all seven phone and four address holds. Approve exactly one later R11 packet to bind `flowUpperBoundMicros: 500000` under `accountCeilingMicros: 4000000`, plus address account/tenant six operations / 600,000 micros and session two / 200,000 micros. This is policy approval only; the later packet needs a fresh owner-selected execution window and separate preparation. Its guarded execution preflight must revalidate current database policy, liability and inactive authority before activation.

The build result may record only source/build/image provenance, terminal status, privacy-safe cost evidence and mandatory grant cleanup. Successful build and policy approval do not create a packet or authorize LOGIN, activation, deployment, provider request, verification code, browser/customer action or live execution.

### Alternative 2 — build the observability image only

Perform steps 1–3 above but do not approve the 4,000,000-micro future phone ceiling. The image can be retained, but a separate capacity decision remains required before any future packet.

### Alternative 3 — stop

Keep the local repair and current read-only evidence. Do not build an image or approve another future packet. R11 and full R12 remain open; P06 stays 12/14.

## Impact and boundaries

Alternative 1 raises only one future packet's explicit phone retained-liability ceiling from the consumed 3,500,000-micro bound to 4,000,000 micros. It preserves every hold and the existing 500,000-micro per-flow bound. Address aggregate/session bounds and per-operation cost remain unchanged from the last approved packet. It grants no payment, booking, dispatch, messaging, customer-contact, secret access/change, deployment or production authority.

At decision time, exact owner approval or refusal was required. P06 remained 12/14 with R11 and full R12 open, and no scope deviation had been implemented.

## Owner decision and result

The owner approved alternative 1 exactly for 6:45–7:30 AM Eastern. Cloud Build `d1b08776-bd6a-48bd-85aa-ed8628d026dc` was submitted once and returned `SUCCESS`. Registry readback binds tag `p06-r11-574f25a66952` to immutable digest `sha256:53f82468d86c49d1ddd1024e9550de27bc0ac49f6841b958f5bc393e10f9f4b9`. All three temporary grants were removed and independently read back absent.

The approved future policy preserves all seven phone and four address holds and allows exactly one later packet at phone 500,000/4,000,000 micros and address account/tenant six/600,000, session two/200,000. No packet exists. A new owner-selected window and separate read-only packet-preparation authorization are required, followed by separate exact execution approval. P06 remains 12/14. Approved one-image and one-future-packet capacity deviations only; no other scope deviation.

## Packet preparation result — 2026-09-23

The owner selected 7:15–8:00 AM Eastern and separately authorized current read-only target/provider/participant refresh plus one packet. Plan `c8e05c7b-f2a3-4b8c-9447-92e6c471d5df` now binds the exact approved image and limits to enabled22, one 7:40–7:55 AM connected runtime and closeout by 8:00 AM. All preparation gates pass and exactly three private review files exist. No helper, execution authorization or live action exists. Exact execution approval remains required. P06 remains 12/14. Approved deviations unchanged.
