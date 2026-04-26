# APP-003A - Intake to Dispatch Inbox (Manual-First)

## Ticket Summary

- Ticket ID: `APP-003A`
- Repo: `signmons-calldesk-backend` (+ frontend surface repo for app UI)
- Screen IDs: `SCR-APP-005`, `SCR-APP-013`
- Objective: ship dispatch-assist MVP foundation where AI creates booking-ready jobs and routes to owner/dispatcher review, without autonomous technician assignment.

## Product Positioning Constraint

Signmons is not only an answering layer. This ticket must establish the first operational plane:

- capture job
- classify urgency
- enforce payment/policy gating input state
- create booking-ready record
- notify owner/dispatcher

No full auto-dispatch in this ticket.

## In Scope

- Intake output contract for booking-ready job request with required fields:
  - customer name
  - phone
  - address
  - service category
  - urgency
  - issue summary
  - photos (if provided)
  - preferred window
  - deposit/service fee status
- Job lifecycle minimum for manual-assist mode:
  - `New Request`
  - `Needs Review`
  - `Ready to Assign`
- Dispatch inbox list/card view for owner/dispatcher with core triage actions.
- Owner/dispatcher notifications on new request and emergency classification.
- Audit event write on status transitions.

## Out of Scope

- Automatic technician assignment.
- Technician accept/decline job flow (`APP-003B`).
- Customer appointment confirmation workflow (`APP-003C`).
- Advanced routing rules engine (`APP-003D`).
- Native mobile app packaging and app store release.

## Dispatch-Assist Rules (Non-Negotiable)

- AI may recommend, but this ticket does not assign technicians.
- Dispatcher/owner retains explicit control for approve/edit/assign.
- Critical missing fields force `Needs Review` (fail-closed).
- Tenant and role boundaries must be enforced server-side.

## Acceptance Criteria (must all pass)

- [ ] Intake produces a booking-ready job object with required fields present or flagged.
- [ ] New jobs appear in dispatch inbox with urgency, category, window, payment/deposit state.
- [ ] Owner/dispatcher receives notification for new request and emergency request.
- [ ] No automatic technician assignment path exists in this ticket.
- [ ] Status transition audit events are recorded for every state update.
- [ ] Tenant isolation and RBAC checks validated for inbox/job read-write paths.

## Test and Evidence Plan

- Backend gates:
  - `npm run -s build`
  - `npm test -- --runInBand`
  - `npm run -s arch:check`
- Frontend gates (if UI touched in this ticket):
  - `npm run -s build`
  - `npm run -s lint`
  - `npm test -- --runInBand`
- Evidence artifacts:
  - API contract proof for intake -> job creation
  - dispatch inbox screenshots (desktop + mobile)
  - notification proof (owner/dispatcher)
  - audit log proof for status transitions

## Risks

- Scope drift into technician workflow and routing logic.
- Ambiguity between `Needs Review` vs `Ready to Assign` criteria.
- Missing fail-closed behavior for incomplete intake fields.
- Notification fatigue without emergency prioritization.

## Commit Convention

- Commit message: `feat(app): implement APP-003A intake to dispatch inbox`
- One focused commit only.
