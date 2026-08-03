# M2 Roadmap - Inventory Ledger and Opening Balance

- Status: `PLANNED`
- Depends on: M1 master data/location gate
- Unlocks: M3-M7

## Outcome

Thiết lập inventory truth từ append-only movements, scoped theo warehouse/location/product/Lot/status, có projection và reconciliation đáng tin cậy.

## Work packages

| ID | Nội dung | Deliverables | Verification |
|---|---|---|---|
| M2.1 | Lot model | Internal/supplier Lot, MFG/EXP, status, product uniqueness | `LOT-001..006` tests |
| M2.2 | Movement contract | Movement type, original/base quantity, actor/time/reference/reason | Immutable ledger tests |
| M2.3 | Balance projection | On-hand theo warehouse/location/product/Lot/status | Ledger = projection tests |
| M2.4 | Posting transaction | Atomic movement + projection update, idempotency | Duplicate/concurrency tests |
| M2.5 | Transfer/reversal | Paired transfer và reversal/replacement links | Conservation tests |
| M2.6 | Count/adjustment | Count session, variance, reason, approval | `INV-008`, audit/auth tests |
| M2.7 | Reservation primitive | Active reservation projection và available formula | No-oversell concurrency tests |
| M2.8 | Opening-balance pipeline | Snapshot, validation, approval, posting batch | Rehearsal reconcile |
| M2.9 | Inventory query UI/API | Stock by SKU/Lot/location/status, movement history | Contract/workflow tests |
| M2.10 | M2 gate | Reconciliation validator và evidence pack | Gate M2 pass |

## Invariants bắt buộc

- `INV-001..008` được enforce tại domain/database layer phù hợp.
- Confirmed balance không âm.
- Posted movement không update/delete để thay đổi nghĩa.
- Transfer bảo toàn base quantity trong cùng transaction.
- Blocked status không đóng góp vào available.
- Duplicate command không post movement lần hai.

## Thứ tự triển khai

`M2.1 -> M2.2 -> M2.3 -> M2.4 -> M2.5 -> M2.6 -> M2.7 -> M2.8 -> M2.9 -> M2.10`.

Opening balance chỉ chạy sau khi movement/projection/reconciliation đã pass bằng fixture xác định.

## Exit gate

- Ledger và projection reconcile cho toàn bộ test/rehearsal data.
- No-negative, idempotency và concurrent reservation pass.
- Transfer/reversal bảo toàn quantity và history.
- Opening-stock rehearsal khớp snapshot đã duyệt.

## Không thuộc M2

Không hoàn thiện purchase receipt, picking, delivery hoặc forecast.
