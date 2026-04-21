# Data Contracts

## Purpose

Ensure backend, frontend, SMS/voice flows, and integrations stay compatible over time.

## Contract Rules

- Contract-first: define schema before implementation
- Version when breaking changes are introduced
- Backward compatibility is required by default
- Validate all external payloads at ingress boundaries

## Required Contract Categories

- Public API DTOs
- Internal event payloads
- Webhook payload normalization
- Persistence model invariants for critical flows

## Change Policy

- Non-breaking: additive fields, optional fields, safer defaults
- Breaking: renames/removals/type changes require:
  - migration plan
  - compatibility window
  - explicit release note

## Verification

- Contract tests for critical request/response shapes
- Schema validation in CI for changed contracts
