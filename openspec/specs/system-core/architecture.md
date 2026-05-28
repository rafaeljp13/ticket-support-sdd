# Architecture Constraints

## Controllers

Controllers MUST:
- remain thin
- contain no business logic
- never access the database directly

---

## Services

Services MUST:
- contain business rules
- orchestrate workflows
- validate status transitions

---

## Repositories

Repositories MUST:
- handle persistence only
- contain no business rules

---

## Schemas

Schemas MUST:
- use Request/Response naming conventions
- validate external input

---

## Testing

The system MUST include:
- unit tests for services
- integration tests for endpoints