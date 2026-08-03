# Inventory Ledger Contract

## Source-of-truth model

```text
Business command
  -> inventory_operation
  -> one or more immutable inventory_movements
  -> balance/reservation projection updated in the same transaction
```

## Minimum movement fields

- `id`
- `operation_id`
- `movement_type`
- `product_id`
- `lot_id` when lot-controlled
- `warehouse_id`
- `location_id`
- `inventory_status`
- signed `base_quantity`
- entered quantity and UOM where applicable
- business reference type/ID
- reason code and optional note
- `occurred_at`
- `recorded_at`
- actor identity
- reversal link where applicable

## Movement types

Initial types include:

- `RECEIPT`
- `PUTAWAY_TRANSFER`
- `LOCATION_TRANSFER`
- `STATUS_TRANSFER`
- `SHIPMENT`
- `CUSTOMER_RETURN_RECEIPT`
- `RETURN_TO_AVAILABLE`
- `RETURN_TO_SUPPLIER`
- `DAMAGE`
- `EXPIRY_BLOCK`
- `DESTRUCTION`
- `COUNT_ADJUSTMENT_IN`
- `COUNT_ADJUSTMENT_OUT`
- `REVERSAL`
- `OPENING_BALANCE`

The type explains the business reason; source/destination legs express quantity conservation.

## Invariants

1. Movement is append-only after posting.
2. One operation posts all legs atomically or none.
3. Transfer source and destination normalized quantities balance.
4. No eligible balance becomes negative.
5. Idempotency key/operation identity prevents duplicate posting.
6. Projection equals ledger sum under its exact dimensions.
7. Reservation projection is reconciled separately and cannot exceed eligible stock under policy.

## Reconciliation gate

The future validator must compare ledger-derived balances with operational projections and return a non-zero exit code on any unexplained difference. No production-readiness claim is allowed without this gate and a recovery procedure.

