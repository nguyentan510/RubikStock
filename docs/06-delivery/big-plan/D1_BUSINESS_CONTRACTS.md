# D1 Roadmap - Business Contracts

- Status: `PROPOSED`
- Depends on: D0 product context đủ rõ
- Unlocks: D2 domain contracts, M1 và M2

## Outcome

Chuyển quy trình mong muốn thành rule, state, approval và acceptance scenario không mâu thuẫn, đủ rõ để code không tự phát minh policy.

## Work packages

| ID | Nội dung | Rule/contract trọng tâm | Verification |
|---|---|---|---|
| D1.1 | Inventory semantics | `INV-001..008` | Ledger/no-negative/reversal scenarios được review |
| D1.2 | Product, Lot và UOM | `LOT-001..006`, `UOM-001..004` | Case/bottle, bag/weight, unknown expiry scenarios |
| D1.3 | Inbound contract | Receipt, discrepancy, QC, put-away states | Receipt walkthrough |
| D1.4 | Outbound contract | `OUT-001..010`, shelf-life, FEFO override | Multi-Lot/concurrent/short-pick scenarios |
| D1.5 | Quality và exception | `QLT`, `RET`, `DST`, approval matrix | Return/destruction/recall walkthrough |
| D1.6 | Delivery và planning boundary | `DEL-001..005`, `PLN-001..006` | Partial/failed delivery và advisory forecast review |
| D1.7 | Audit/security contract | `AUD-001..003`, `SEC-001..003` | Privileged-action and permission scenarios |
| D1.8 | Conceptual model review | Aggregate ownership, state machines, transaction boundaries | Cross-document consistency review |
| D1.9 | Business acceptance | Scenario pack và sign-off | Gate D1 pass |

## Thứ tự triển khai

`D1.1 -> D1.2 -> D1.3 -> D1.4 -> D1.5 -> D1.6 -> D1.7 -> D1.8 -> D1.9`.

Security/audit phải được review cùng từng privileged workflow, không để tới cuối mới bổ sung.

## Exit gate

- Không còn xung đột về inventory, Lot, UOM, reservation, return, destruction và delivery.
- State ownership và approval ownership được chấp nhận.
- Conceptual data model hỗ trợ mọi scenario đã duyệt.
- Các điểm cố ý defer được ghi rõ, không ngầm coi là accepted.

## Không thuộc D1

Không tạo production schema, auth provider, CRUD API hoặc warehouse UI.
