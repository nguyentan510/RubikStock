# Dependency-safe Build Order

## Quy tắc

Chỉ xây slice kế tiếp khi upstream truth của nó đã được chứng minh.

```text
D0 Product truth
-> D1 Business contracts
-> D2 Technical foundation
-> M1 Master data/location
-> M2 Inventory ledger/opening balance
-> M3 Inbound
-> M4 Reservation/FEFO/outbound
-> M5 Returns/quality/destruction
-> M6 Delivery
-> M7 Replenishment/seasonality
-> M8 Production qualification
-> M9 Optimization
```

## Vì sao theo thứ tự này

- Forecast phụ thuộc vào sales đã qualify, stockout, inventory, lead-time, và event data.
- Outbound phụ thuộc vào balance theo Lot/location đáng tin cậy và reservation atomic.
- Returns phụ thuộc vào khả năng trace shipment gốc và Lot gốc.
- Delivery reconciliation phụ thuộc vào shipment và xử lý return có kiểm soát.
- Production cutover phụ thuộc vào restore, audit, UAT, và evidence migration.

## Slice có thể triển khai tiếp theo

Slice tiếp theo hiện tại là `D0-D1 Business Acceptance`, chưa phải application code. RUBIK phải giải quyết hoặc cố ý defer các mục `TBD` có tác động lớn:

- UOM/package breaking (`TBD-002`).
- Độ đầy đủ của Lot/expiry (`TBD-003`).
- Nguồn sales-order và split delivery (`TBD-004`, `TBD-005`).
- Shelf-life của khách và ngưỡng approval (`TBD-008`, `TBD-009`).
- Thiết bị/kết nối và backend runtime (`TBD-011`, `TBD-013`).

Sau khi chấp nhận, triển khai `D2 Technical Foundation` như một slice có ranh giới rõ ràng.

## Scope guard

Không bắt đầu ML forecast, route optimization, thay thế accounting, hoặc microservices khi M2 inventory truth chưa được chứng minh.
