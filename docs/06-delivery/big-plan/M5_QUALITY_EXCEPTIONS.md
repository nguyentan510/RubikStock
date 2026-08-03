# M5 Roadmap - Quality, Returns and Exceptions

- Status: `PLANNED`
- Depends on: M2 inventory truth, M3 receipt trace, M4 shipment genealogy
- Unlocks: M6 delivery reconciliation đầy đủ và production exception handling

## Outcome

Mọi hàng lỗi, hết hạn, trả về, recall và hủy đều đi qua state/approval/audit rõ ràng; không exception nào âm thầm trở lại available hoặc biến mất khỏi history.

## Work packages

| ID | Nội dung | Deliverables | Verification |
|---|---|---|---|
| M5.1 | Hold/block/recall | Lot/status blocking across locations | Allocation denial tests |
| M5.2 | Return authorization | Link order/shipment/product/Lot/quantity/reason | Genealogy tests |
| M5.3 | Return receipt | Controlled quarantine location/status | `RET-001` bypass tests |
| M5.4 | Inspection | Findings, evidence metadata, inspector/time | Permission/audit tests |
| M5.5 | Disposition | Restock, reject, supplier return, destroy decision | Transition tests |
| M5.6 | Damage/expiry | Detection, status transition, aging alerts | Date/status tests |
| M5.7 | Destruction | Request, independent approval, execute/verify, movement | Separation/idempotency tests |
| M5.8 | Trace/recall query | Lot genealogy from receipt to customers/returns/destruction | End-to-end trace test |
| M5.9 | Exception UI | Quarantine queue, inspection, disposition, approvals | Role workflow tests |
| M5.10 | M5 gate | Exception evidence and reconciliation report | Gate M5 pass |

## Thứ tự triển khai

`M5.1 -> M5.2 -> M5.3 -> M5.4 -> M5.5 -> M5.6 -> M5.7 -> M5.8 -> M5.9 -> M5.10`.

## Invariants bắt buộc

- Return luôn vào quarantine trước.
- Receipt return không đồng nghĩa restock.
- Manufacturer Lot genealogy không bị mất hoặc tự tạo lại tùy tiện.
- Destruction requester và approver phải độc lập theo accepted threshold.
- `DESTROYED` không còn on-hand nhưng vẫn còn historical trace.

## Exit gate

- Return không thể bypass quarantine/inspection/disposition.
- Block/recall ngăn allocation ở mọi location.
- Destruction không self-approve hoặc post hai lần.
- Lot trace đi xuyên receipt, stock, shipment, customer, return và destruction.
