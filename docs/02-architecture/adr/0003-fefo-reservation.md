# ADR-0003: Reserve Before Picking and Allocate by Eligible FEFO

- Status: `PROPOSED`
- Date: 2026-08-03

## Context

RUBIK processes fewer but larger B2B orders. A confirmed order can consume a material portion of available inventory, and customers may require minimum remaining shelf life.

## Decision

1. Confirmed demand reserves available quantity atomically.
2. Customer shelf-life and stock-status rules determine eligible stock.
3. Eligible stock is sorted by FEFO, then receipt time, then operational pick preference.
4. Override records original and selected allocations, reason, actor, and approval.

## Consequences

- Overselling is controlled under concurrency.
- Newest-date requests do not automatically strand every older lot.
- Reservation expiry/release and reallocation are first-class workflows.

