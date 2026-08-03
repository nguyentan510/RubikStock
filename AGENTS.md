# RubikStock Agent Rules

## Product boundary

RubikStock is an operational inventory and fulfillment system for RUBIK COMPANY. It is not an accounting ERP in MVP.

## Mandatory domain principles

1. Inventory truth comes from append-only stock movements, not direct balance edits.
2. Every stock quantity is scoped by product, lot, location, and inventory status.
3. `available = eligible_on_hand - active_reservations`.
4. Expiring goods allocate by FEFO after customer shelf-life rules are applied.
5. Returns enter quarantine and never return directly to available stock.
6. Destruction, stock adjustment, and FEFO override require reason and audit evidence.
7. Unknown lot, expiry, order, or delivery state fails closed.
8. Forecasting cannot be promoted before inventory and sales history are qualified.

## Engineering shape

- Prefer a modular monolith.
- Keep Pydantic API models separate from SQLAlchemy persistence models.
- Keep business invariants in domain/application services, not UI or route handlers.
- Use one database-migration source of truth; the proposed default is Alembic.
- Do not add Redis, message brokers, microservices, or ML without a demonstrated need.

## Documentation discipline

- Business documents are canonical in Vietnamese; identifiers and code contracts use English.
- Use rule IDs from `docs/01-business/BUSINESS_RULES.md` in tests and traceability.
- Mark unknown business facts as `TBD`; do not turn assumptions into accepted policy.
- Update implementation status only with actual code/test/runtime evidence.

## Safety

- Never commit secrets or real business data.
- Never mutate production data without explicit authorization, a backup, and a rollback plan.
- Never bypass reservation, QC, approval, or audit controls for convenience.

