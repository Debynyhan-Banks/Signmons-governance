# Rules and Policy Model (DB Source Of Truth)

Purpose: define the policy entities and execution flow for business rules, pricing policy, dispatch behavior, and tenant voice.

## Source of Truth

- Canonical source: database configuration.
- JSON templates may seed defaults at onboarding.
- UI builder edits DB-backed policy records.

## Core Policy Entities

1. `tenant_rule_set`
- `id`, `tenantId`, `version`, `isActive`, `createdAt`

2. `dispatch_rule`
- `tenantRuleSetId`
- `tradeCategory`
- `serviceArea`
- `urgencyLevel`
- `availabilityWindow`
- `assignmentMode` (`manual` | `recommended` | `auto`)
- `assignTo` / `onCallGroup`
- `priority`

3. `payment_policy`
- `tenantRuleSetId`
- `requiresPaymentBeforeDispatch` (bool)
- `diagnosticFeeCents`
- `depositPolicy`
- `emergencyFeePolicyRef`

4. `emergency_fee_policy`
- `tenantRuleSetId`
- `tradeCategory`
- `timeWindowStart` / `timeWindowEnd`
- `feeCents`
- `reasonCode`

5. `tenant_voice_profile`
- one active profile per tenant
- `brandTone`, `greetingStyle`, `forbiddenPhrases`, `escalationLanguage`

6. `calendar_integration`
- `tenantId`
- `provider` (`google` required for MVP)
- `status`
- `lastSyncAt`

## Execution Flow

1. Intake event created (call/text/chat/contact)
2. Load active `tenant_rule_set`
3. Evaluate urgency + payment + emergency fee policy
4. Evaluate dispatch mode and assignment recommendation
5. Apply scheduling constraints and calendar availability
6. Emit decision payload (`decision + reasonCodes`)
7. Persist audit event for each gate decision

## Required Decision Output

- `tenantId`
- `ruleSetVersion`
- `isEmergency`
- `emergencyFeeApplied`
- `requiresPaymentBeforeDispatch`
- `dispatchMode`
- `recommendedAssigneeId` (nullable)
- `reasonCodes` (string[])
- `timestamp`

## Plan Policy Lock

- Starter: `manual`
- Growth: `recommended`
- Pro/Enterprise: `auto` allowed
