# APP-013 / 3A / P08 — service-state HTTPS correction proposal

Status: OWNER APPROVED FOR ALTERNATIVE 1 LOCAL CORRECTION ONLY. R1-W01 / APP-013 / 3A remains unchanged.

Owner decision: On October 28, 2026, the owner approved Alternative 1 against this proposal's pre-decision SHA256 `d03112fea6f1d0bb91931a967c01b26a60e820ad21e5814bb5001a13a01c7827`. This authorizes only the bounded local HTTPS-path implementation and fake subprocess/HTTP tests below. It does not authorize gcloud, network/provider access, retry or mutation.

## Demonstrated gap

Both consumed role-creation operations stopped on the same fourth call, `gcloud services describe iam.googleapis.com`, before any HTTPS or mutation request. R02 now classifies the failure as `TRANSPORT`. The first three gcloud calls—active owner, exact configured project and memory-only bearer—completed, so the repeated blocker is isolated to the gcloud Service Usage transport path. Repeating the unchanged operation would violate the no-retry boundary and would not address the demonstrated path failure.

Google's Service Usage contract requires a project number for an exact `services.get` resource. The corrected path therefore needs an exact Resource Manager project GET to obtain and validate the number in memory before the Service Usage GET.

## Alternative 1 — recommended bounded local correction

Within the existing evidence helper only:

1. remove the failing gcloud service-state command from the native creation path;
2. after owner/project/bearer checks, make one exact read-only Resource Manager HTTPS GET for project `signmons`, validate project ID, numeric project number and active lifecycle, retain the number only in process memory;
3. make one exact read-only Service Usage HTTPS GET for `projects/{number}/services/iam.googleapis.com`, require `state=ENABLED`, then discard the number and raw bodies;
4. expand the same-attempt permission probe to require `resourcemanager.projects.get` and `serviceusage.services.get` in addition to the existing four permissions;
5. preserve the two policy CLI reads, exact-ID absence reads, fixed create bodies/readbacks, zero-binding gates, one attempt/no retry, signals/deadlines/concurrency, private binding/purge and independent closeout;
6. bind the new ceiling to exactly five CLI and nine HTTPS calls (14 total) on the success path;
7. add fixed HTTPS stage and safe status/transport classifications without retaining raw URL parameters, bearer, project number, stdout/stderr or response/error bodies;
8. test exact methods, URLs, headers, bodies and all positive, denial, malformed-project, disabled-service, HTTP/transport, partial/lost, signal, cutoff, concurrency, closeout and privacy paths using fake subprocess/HTTP only;
9. run all repository gates.

No credential resolution, gcloud subprocess, network/provider read, role create, IAM change, account/database/token/runtime/Stripe/payment action, spending or external retry is included. A later external operation requires a fresh exact proposal and owner approval.

## Alternative 2 — narrow diagnostic only

Prepare a separate read-only Resource Manager and Service Usage diagnostic first. This adds another governed operation without advancing role creation and is not recommended because Alternative 1 preserves the same shift-left gates in the eventual creation attempt.

## Alternative 3 — stop

Leave Stage A blocked on the gcloud transport path.

Owner decision recorded: Alternative 1 approved for bounded local correction and fake tests only. Accepted counts remain unchanged. **Demonstrated transport-path change accepted for correction; no external action is authorized.**
