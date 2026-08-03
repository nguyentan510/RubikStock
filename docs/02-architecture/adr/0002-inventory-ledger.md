# ADR-0002: Inventory Ledger Is the Source of Truth

- Status: `PROPOSED`
- Date: 2026-08-03

## Context

A mutable `remaining_quantity` cannot explain receipts, transfers, reservations, returns, damage, counting, and reversal history reliably.

## Decision

Use append-only inventory movements as stock history. Maintain transactionally consistent balance/reservation projections for operational reads.

## Consequences

- Every quantity can be traced to business operations.
- Corrections require reversal/replacement instead of editing history.
- Projection reconciliation tests and an operational consistency check are required.
- Business commands must be idempotent and transactional.

