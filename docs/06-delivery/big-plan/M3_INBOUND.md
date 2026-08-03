# M3 Roadmap - Inbound

- Status: `PLANNED`
- Depends on: M1 và M2 inventory posting contracts
- Unlocks: Qualified stock cho M4 và lịch sử receipt cho M7

## Outcome

Nhận hàng B2B số lượng lớn từ supplier, ghi Lot/MFG/EXP, discrepancy, QC và put-away với trace đầy đủ tới stock available hoặc blocked.

## Work packages

| ID | Nội dung | Deliverables | Verification |
|---|---|---|---|
| M3.1 | Purchase reference | Purchase order/reference và expected lines tối thiểu | State/contract tests |
| M3.2 | Receipt command | Supplier, product, UOM, quantity, Lot/date validation | Validation/idempotency tests |
| M3.3 | Discrepancy handling | Over/short/damaged/unknown Lot reason codes | Exception scenarios |
| M3.4 | QC entry | `RECEIVING/QC_HOLD/AVAILABLE` eligibility | Blocked-stock tests |
| M3.5 | Put-away | Suggested/confirmed location và transfer/posting | Product-Lot-location match tests |
| M3.6 | Inbound UI | Receive, scan/manual entry, discrepancy, put-away task | Operator workflow tests |
| M3.7 | Receipt documents | Printable receipt/put-away list, private evidence metadata | Access/audit tests |
| M3.8 | Inbound pilot | Representative full/partial/damaged receipts | Runtime rehearsal |
| M3.9 | M3 gate | Receipt-to-stock trace report | Gate M3 pass |

## Thứ tự triển khai

`M3.1 -> M3.2 -> M3.3 -> M3.4 -> M3.5 -> M3.6 -> M3.7 -> M3.8 -> M3.9`.

## Failure policy

- Thiếu field bắt buộc hoặc Lot/date không xác minh được: fail closed hoặc `QC_HOLD/QUARANTINE` theo accepted policy.
- UOM conversion không tồn tại: reject line, không tự quy đổi.
- Retry receipt command: trả cùng result hoặc conflict rõ, không post trùng.
- Put-away mismatch: giữ stock ở receiving location cho tới khi reconcile.

## Exit gate

- Receipt đại diện trace tới Lot/location/status/movement.
- Partial, excess, damaged và unknown-date scenarios pass.
- QC-held stock không xuất hiện trong available.
- Put-away và receipt retry không tạo duplicate stock.
