# Temporary phone-test signing permission — review only

2026-09-12. Owner authorized preparing this plan, not applying it. Project custom-role list returned empty. No IAM, identity, token or provider mutation occurred.

## Exact proposed change

- Project: signmons.
- Create custom role projects/signmons/roles/stagingPhoneTokenSigner with only iam.serviceAccounts.signBlob. Check permission support before creation; stop if unsupported. No automatic broader-role substitution.
- Bind that role on service account signmons-calldesk-runtime@signmons.iam.gserviceaccount.com only, to user:debynyhan@signmons.com. No project-wide binding and no runtime self-signing grant.
- Binding title: staging-phone-one-session. Condition: request.time >= timestamp(START_UTC) && request.time < timestamp(END_UTC). Choose and show concrete UTC values immediately before separately approved execution; duration at most 15 minutes. Do not extend or remove condition on failure. Condition expiration stops new signing, not already-issued credentials.
- Re-read policy with etag/version 3 and preserve every unrelated binding. Verify principal, resource, only permission and effective expiration. Check IAM Credentials API availability read-only first; enabling an API is not included by implication.

## Material risk and limits

signBlob is powerful even without signJwt/getAccessToken explicitly listed. Arbitrary signed payloads can mint Firebase tokens for other UIDs and can support service-account impersonation using signed assertions. It cannot be constrained to the test UID or one call through this role. The service account already has access to application resources. A time-bound custom role narrows the listed permissions and exposure period, but does not eliminate this risk. Do not represent it as harmless or single-user-enforced.

Actual token issuance is a separate approved operation: only staging-phone-owner-20260912, expected isolated tenant claims, private in-memory custom-token exchange for a Firebase ID token, no token/password/key in chat/files/logs. Qualify an existing Identity Platform API key and its restrictions without creating or relaxing one. No private-key download. No emulator token, dev-auth bypass, production user or UID substitution. If private exchange is not qualified, do not grant signing access yet.

## Removal and verification

After the single authorized signing operation or any failure, remove only the exact new principal/role/condition binding immediately, without waiting for expiry. Re-read policy and testIamPermissions; effective signBlob should match baseline (absent), with IAM propagation caveat. If other grants appear, do not delete them; report the changed baseline. Disable the newly created custom role after binding removal and verify no remaining intended use; retain it disabled for audit rather than deleting unrelated roles.

Removal/expiry does not revoke minted Firebase ID/refresh tokens or other signed credentials. Approved identity closeout must independently disable the isolated user, revoke refresh tokens, revoke database phone approval/suspend tenant and turn candidate phone flag off. Existing tokens can remain valid until expiry unless verifier checks revocation; do not rely on IAM removal alone. Do not revoke existing production identities or rotate shared secrets.

## Approval boundary

Next authorization would cover creation of this exact role, this resource-scoped conditional grant, immediate removal and role disabling. It would not by itself authorize identity activation, token issuance, candidate activation or a paid SMS. Prefer bundling the full reviewed supervised-access/closeout operation only once remaining private exchange prerequisites are known, so the signing window is not consumed by setup. No additional application feature is proposed. APP-013/2B remains Now, walkthrough 3/8 (37.5%) unchanged.

Sources checked: https://docs.cloud.google.com/iam/docs/managing-conditional-role-bindings ; https://docs.cloud.google.com/iam/docs/conditions-attribute-reference ; https://firebase.google.com/docs/auth/admin/create-custom-tokens ; https://cloud.google.com/iam/docs/create-short-lived-credentials-delegated .
