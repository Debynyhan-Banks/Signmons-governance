# APP-013 / 3A / CR-K1 — QK5 exact read-only qualification proposal

Status: PENDING OWNER APPROVAL; qualification-only. No external calls or private input requested by preparation. CR-K1 scope/local implementation approved ed64d49; source a7ae8b3e82b302343d4c17c97721accdb806a3ae; source-manifest SHA256 f18cbb8bdb686d2a1848e3100d3a50b2787bb1bd3264edccbb06104cf24b44b4. Exact spec: APP013_P08_KEY_QUALIFICATION_QK5_SPEC_20261110.json. Operation ed308ba4-ce5a-4b72-a927-ea2538b2f4b4; scope SHA256 60500c692b3153500afe9592e225d53c6a427d11a86288a146054808e4bdaaf1. decisionCommit remains null until actual owner approval is separately committed. The proposed decision below is not authority.

## Exact action and timing

Start now through strictly before7:10p.m. Eastern November10; all qualification work ends7:20p.m.; absolute process/private-memory closeout7:30p.m. The owner's active Terminal time is expected5–10minutes, not a requirement to wait through the whole window. One attempt, no retry or automatic retiming. A deadline or failure ends the attempt with a safe stage/code receipt. No waiting for a payment or handoff marker.

Owner privately enters existing correct Sandbox secret key and existing endpoint ID at hidden prompts. The same single Node child now validates endpoint/key and performs its three read-only Stripe requests BEFORE Google/SQL preflight. Only after that succeeds does the current CHILD SQL administrator password prompt occur. Provider counts and boundaries are unchanged; this ordering is source-bound in a7ae8b3. Never chat/argv/files. Project number is discovered by the approved process and verified against the existing hash; no old test-account UUID/recovery handoff. No raw secret or endpoint input persists. Spec contains only public pins/hashes and may be copied to a private600 input file; receipts contain no credentials/project number.

Maximum27 SDK commands: owner/config/token5, project1, project billing/account2, project/identity IAM policies2, existing candidate1, retired identity/version/policy/tag state15, candidate-name inventory1. Maximum12 Google HTTPS requests:3 service states and9 effective-permission checks (Run1, identity1, secrets7). Two existing full-role-ACL read-only SQL queries. One bounded Node child issues exactly at most3 Stripe GETs: connected accounts list limit100/no pagination, test-mode balance, exact disabled webhook endpoint. These are logical dispatch ceilings, not all underlying SDK network calls. No secret payload read from existing version1.

Qualified output must bind current environment/role ACL/payment return URL, usable key/account/mode/endpoint, retired runtime, existing source/image/normal traffic, service/billing state and permission checks. Actual output can refuse safely; unknowns are not promoted. Existing shared validators, actual provider boundaries, source/SDK locks and new read-only mutation refusal gates are tested. Global allowance0 and all mutation/payment holds remain unchanged. No API-key creation, secret version creation/enablement, IAM/role change, deploy, endpoint enablement, checkout/payment, customer contact or normal-traffic change is included.

Proposed decision for review only:

```json
{
  "owner": "Debynyhan Banks",
  "decision": "APPROVE_EXACT_CR_K1_QUALIFY",
  "scopeSha256": "60500c692b3153500afe9592e225d53c6a427d11a86288a146054808e4bdaaf1",
  "externalReadAuthorized": true,
  "externalMutationAuthorized": false,
  "costHoldReleased": false
}
```

After actual owner approval, record that decision under APP013_P08_KEY_CORRECTION_DECISION_20261110.json and bind its commit in the private spec. Actual command: `/opt/homebrew/bin/python3.14 -B evidence/APP-013/p08-key-correction-20261110/launch.py /private/tmp/p08-qk5-ed308ba4-ce5a-4b72-a927-ea2538b2f4b4.json`, from the backend checkout. Before launch compare exact source, manifest, SDK, spec, time and fresh root `/private/tmp/p08-key-correction-ed308ba4-ce5a-4b72-a927-ea2538b2f4b4`. No directory/attempt is created by preparation. Inspect only sanitized result/failure and process exit; credentials remain process memory only and are cleared on exit. No replay if already consumed.

## Readiness record and handoff

November10 23:41UTC: same source a7ae8b3 and manifest; actual launch.verify checks committed source, SDK, proposed exact scope and time successfully; new operation root absent. Existing source tests25Python+18Node and synthetic PTY proof reused, not rerun. Current baseline/documentation/architecture/whitespace checks required before review. Same finite qualification interfaces, resource pins, limits, deadlines, no-retry and private-memory clearing as QK4. No implementation change.

QK4 consumed at SANDBOX_KEY/PAYMENT_TEST_KEY_REQUIRED, endpoint matched, zero provider calls by inspected source order. Owner reports entering we_ at the secret-key prompt and now confirms sk_test_ key available. This explains the reported input-type mismatch; key validity remains UNKNOWN until qualified. FIRST prompt: full sk_test_ Sandbox secret API key. SECOND prompt: same we_ Destination ID. THIRD SQL-password prompt appears only after key validation. No raw value in chat/files/argv. No new key creation or key rotation.

Exact QK5 external-read approval PENDING. Key validity/account/mode/endpoint-state/current access remain UNKNOWN. Implementer owns launch/receipt/closure; owner approves exact read and supplies hidden inputs. Successful qualification grants no mutation or cost/hold release. Correction and independent-cleanup packet/cost decision, reviewed candidate adoption, connected payment/event/application/browser proof and owner acceptance remain. Accepted1A/1B/2A/2B4/8;3A OPEN;R1newlyclosed0/27. Approved CR-K1 scope deviation only; no further deviation.
