# P08 producer implementation readiness — blocking contract audit

Owner design decisionfc9262a approved in current conversation. No further approval is needed to investigate the local contracts. This record must not be presented as an implementation-ready card. Source inspection found additional concrete coverage/cleanup gaps in the existing producer; the mandatory shift-left gate blocks requesting implementation or scheduling a live window until those are resolved in the card.

## Reuse resolved

Use existing p08-https-output-category-local-20261029/source qualification_launch.py and composed_qualification.py as the producer correction seam. No manifest references to that directory were found in the current evidence manifest search; historical receipts remain immutable. Reuse current retained-role/full ACL functions and native-entry scope/hash checks, not old roleCount==0. Reuse approved19-field runtime rules rather than historical observed environment digest. SDK/psql remains the selected transport family; external retry/cache exception is still unapproved. Owner phase distinction is now approved; four post-binding diagnostics and actual authentication remain mandatory.

## Exact gaps that must be covered before implementation approval

| Inspected source | Existing behavior | Required card resolution |
| --- | --- | --- |
| composed_qualification.PERMISSIONS | Nine permissions: project get/setIamPolicy; service-account get/setIamPolicy; API Keys create/get/getKeyString/delete; serviceusage.operations.get | Map every actual activation/readback/retirement/independent-closeout command to resource and effective owner permission proof. Existing nine are insufficient for all native operations. |
| restore.command79–88 | Enables/disables identity and secret versions, changes secret policies, updates Cloud Run traffic and IAM | Permission coverage must include these operations and cleanup counterparts. Do not set effectiveAccess true from the old nine-permission response. Exact additional API/diagnostic descriptors and output contracts are still unresolved; no inferred permission names are implemented. |
| qualification_launch.NativeIO.https | Uses urllib.request.urlopen, without the narrow adapter's no-redirect opener or explicit response-close handling on all failures | Fixed host/request allowlist, redirects refused, bounded output and verified response closure must be in the selected transport implementation/tests. |
| qualification_launch.NativeIO children/close | children starts empty, no registration in shown subprocess.run paths, close reports only not children | This is not independent process-tree proof. Reuse owned-process tracking/termination/readback from existing proven boundaries; define interruption and partial-failure closeout before counting privateInventory true. |
| qualification_launch.NativeIO.sql | Two descriptors only, old qualification SQL includes absent-role premise | Add exact retained-role read through approved fixed query, preserve exact business/tenant/operator/session SQL, and define allowance for independent cleanup readback separately from work reads. |
| native authority qualification shape | Checks nine true fields and scope/hash/expiry but does not itself produce observed facts | Producer must derive every field, never accept caller assertions; observation interval/expiry/provenance and native-entry consumption binding need explicit interfaces. |

## Existing request baseline and dependency order

Inspected cli_contract defines26 descriptors: owner,config,project,billing_project,billing_account,service,revision,identity; six secret states; seven secret policies; project/identity policy; two roles;token. Billing-account descriptor is derived only from validated project billing linkage/fingerprint. access_https_contract defines nine descriptors: six service states, project and identity testIamPermissions, exact prospective key metadata; Firebase lookup is tenth and must wait for exact database-derived owned UID. sql_contract has qualification and closeout only. Those counts describe old code, not a sufficient new request allowance or provider-call ceiling. SDK internal requests are not counted by invocation totals. No new live limit can be frozen until the missing permission probes and cleanup descriptors are enumerated.

## Finite card work remaining, implementer-owned

1. Build the complete action/resource/permission/diagnostic matrix from existing native runtime, key, identity/Firebase and independent-closeout interfaces; verify the actual provider contracts before freezing descriptors. Keep post-binding runtime access separate from owner entry capability.
2. Select the exact existing owned-process/response/SQL cleanup interfaces and account for required cleanup reads. Source-pin those interfaces and identify precise changed files plus manifests; no historical bundle rebaseline.
3. Specify strict per-domain producer outputs and nine-field reduction, exact observed environment/legacy ACL digest after independent validation, source/decision/operation/target/scope/expiry binding, and failed/UNKNOWN results. Output remains unqualified on any missing coverage or cleanup evidence.
4. Complete finite implementation/test checklist, exact commands and rollback. Tests must exercise actual SDK serialization, no redirect/oversize/error response closure, process interruption/tree reaping, disposable SQL/TLS/session cleanup, current versus stale/cross-scope evidence and all existing positive/negative entry guards. Local fixtures cannot constitute current live evidence.

No new subsystem, provider change or acceptance criterion is proposed. The next observable result remains a complete producer card with this matrix and cleanup boundary resolved, not another permission request based on a partial card. Responsible owner of current blocker: implementer. Product/credential/provider/DB owner decisions apply only when a concrete external scope or material change is prepared. No user credential/input is needed for the remaining source/contract investigation.

## Handoff

Completed: recorded approved design; selected existing producer seam; enumerated actual old request set/dependencies; identified permission coverage, redirect/response ownership and process-closeout gaps. Remaining: complete exact additional descriptors and cleanup interfaces before implementation. Current real runtime/DB/job/Firebase/billing/access facts UNKNOWN. No runtime edits, credentials, live read/write, payment, deployment or consumed-operation replay. Existing backendd306ca3 lifecycle proof remains complete; accepted1A/1B/2A/2B4/8;R1 newly closed0/27;3A open. **No scope deviation.**

Inspection UTC 2026-11-03T15:53:52.551850+00:00; backend d306ca3e2e6d05f1c9555849d8d511507be699c1.

- `p08-https-output-category-local-20261029/source/qualification_launch.py` SHA256 `94b73ea8be71410f0f51e1d3a5d20f14eba126b1aa7370da7af537c9586a15f0`.
- `p08-https-output-category-local-20261029/source/composed_qualification.py` SHA256 `19181d987eddec481a105ecc1dbe89413a42fe2b07436c073934aef6aafde685`.
- `p08-restoration-local-20261028/source/restore.py` SHA256 `a0bf4bc90cca0bd52935915d710ccb44e065dd3deed841a12ab49cb3ac4a1cb9`.
