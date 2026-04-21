# Engineering Standards

## Architecture

- Separate transport, application orchestration, domain policy, persistence
- Keep modules cohesive and boundaries explicit
- Prefer pure functions for domain rules when feasible

## SOLID and SoC Requirements

- Single Responsibility: one reason to change per service/module
- Open/Closed: extend via registration/composition, avoid giant switch edits
- Liskov: implementations honor contract behavior
- Interface Segregation: narrow interfaces per consumer
- Dependency Inversion: depend on interfaces/tokens at boundaries

## Code Quality Rules

- No god classes or god functions
- Constructor dependency fan-in must remain controlled and justified
- Do not instantiate repositories/services manually in constructors
- Use typed contracts at boundaries

## Testing

- Add/adjust tests with every behavior change
- Prefer small focused tests + integration tests for boundary flows
- Keep replay/regression suites for conversation-critical behavior

## Documentation

- Ticket must update affected contracts/docs
- Breaking changes require migration notes
