# M4 Roadmap - B2B Outbound

- Status: `PLANNED`
- Depends on: M2 inventory truth; M3 cho stock receipt flow hoàn chỉnh
- Unlocks: M5 return genealogy, M6 delivery và sales history M7

## Outcome

Fulfill đơn B2B khối lượng lớn bằng reservation atomic, customer shelf-life eligibility, FEFO allocation nhiều Lot/location và shipment posting đúng một lần.

## Work packages

| ID | Nội dung | Deliverables | Verification |
|---|---|---|---|
| M4.1 | Sales order contract | Customer/order/line/UOM/requested date/state | API/state tests |
| M4.2 | ATP/reservation | Available policy và atomic reservation | Concurrent no-oversell tests |
| M4.3 | Eligibility | Status, expiry, customer minimum shelf life | Boundary-date tests |
| M4.4 | FEFO allocator | Stable sorting, multi-Lot/location allocation | Deterministic allocation tests |
| M4.5 | Override workflow | Original suggestion, selection, reason, permission/approval | Audit/auth tests |
| M4.6 | Pick/short-pick | Pick tasks, mismatch validation, reallocation/backorder | Workflow tests |
| M4.7 | Stage/ship | Staging control, atomic stock-out + reservation consumption | Idempotent shipment tests |
| M4.8 | Documents/UI | Pick list, packing list, order/pick/stage screens | Operator workflow tests |
| M4.9 | Large-order rehearsal | Mixed Lot, partial stock, concurrent orders | Runtime/performance baseline |
| M4.10 | M4 gate | Fulfillment evidence pack | Gate M4 pass |

## Allocation sequence

```text
Confirmed demand
-> ATP check
-> Active reservation
-> Customer shelf-life/status eligibility
-> FEFO sort
-> Multi-Lot/location allocation
-> Pick verification
-> Stage
-> Atomic shipment posting
```

## Invariants bắt buộc

- Áp dụng `OUT-001..010` và `QLT-001`.
- Shelf-life filter chạy trước FEFO sort.
- Override không thể bypass blocked status hoặc expired policy.
- Shipment không consume reservation/post movement hai lần.
- Unknown order/stock/shipment state phải chặn thao tác tiếp theo.

## Exit gate

- Concurrent reservation, multi-Lot, multi-location và short-pick pass.
- FEFO deterministic và override audit đầy đủ.
- Shipment posting atomic/idempotent.
- Large B2B order rehearsal đạt baseline được chấp nhận.
