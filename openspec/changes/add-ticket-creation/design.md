# Design: Ticket Creation

## Architecture

The implementation SHALL follow the layered architecture:

- API layer
- Service layer
- Repository layer
- Database layer

---

## Ticket Lifecycle

New tickets SHALL:
- start with OPEN status
- require title
- require description

---

## Validation Rules

- title cannot be empty
- description cannot be empty

---

## Persistence

Tickets SHALL be stored in PostgreSQL using SQLAlchemy ORM.