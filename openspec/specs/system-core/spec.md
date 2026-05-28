# System Core Specification

## Overview

The system SHALL provide a support ticket management API.

The API SHALL allow users to:
- create tickets
- comment on tickets
- update ticket statuses
- retrieve ticket information

---

## Requirement: Ticket Creation

The system SHALL allow users to create support tickets.

### Scenario: Successful ticket creation

- GIVEN a valid title and description
- WHEN the user submits the request
- THEN the system SHALL create the ticket
- AND the ticket status SHALL be OPEN

### Scenario: Empty title

- GIVEN an empty title
- WHEN the user submits the request
- THEN the system SHALL reject the request

---

## Requirement: Ticket Comments

The system SHALL allow comments on active tickets.

### Scenario: Add comment to active ticket

- GIVEN an OPEN ticket
- WHEN a user submits a comment
- THEN the system SHALL store the comment

### Scenario: Comment on closed ticket

- GIVEN a CLOSED ticket
- WHEN a user submits a comment
- THEN the system SHALL reject the operation

---

## Requirement: Ticket Status Transition

The system SHALL enforce valid status transitions.

### Scenario: OPEN to IN_PROGRESS

- GIVEN a ticket with OPEN status
- WHEN the status changes to IN_PROGRESS
- THEN the system SHALL update the ticket

### Scenario: IN_PROGRESS to CLOSED

- GIVEN a ticket with IN_PROGRESS status
- WHEN the status changes to CLOSED
- THEN the system SHALL update the ticket

### Scenario: CLOSED to OPEN

- GIVEN a CLOSED ticket
- WHEN a user attempts to reopen the ticket
- THEN the system SHALL reject the operation