# Dependency-safe Build Order

## Quy tắc

Chỉ xây slice kế tiếp khi upstream truth của nó đã được chứng minh.

Chi tiết work package và exit evidence nằm trong [`big-plan/MASTER_PLAN.md`](big-plan/MASTER_PLAN.md).

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

Gate D0 đã pass. Slice tiếp theo của decision track là `D1 Business Contract Acceptance`, bắt đầu với inventory/Lot/UOM Batch A, song song với D2 foundation. Ba mục Batch D vẫn giữ disposition:

- Accounting integration (`TBD-007`) deferred có owner `Kế toán`; không thuộc MVP.
- Repository license (`TBD-012`) deferred có owner `CEO/Project Owner`; public source-visible nhưng chưa open source.
- Runtime (`TBD-013`) accepted: Local Docker-first và Linux VPS Docker Compose target.

Tổng register có 12 accepted, 2 deferred có owner và không còn mục Open vô chủ.

D1 business contracts phải được review riêng theo [`big-plan/D1_BUSINESS_ACCEPTANCE.md`](big-plan/D1_BUSINESS_ACCEPTANCE.md). D2 tiếp tục theo slice full-stack Compose, migration lifecycle, auth/RBAC và staging VPS; không coi D0 acceptance là evidence D1/D2 pass.

## Scope guard

Không bắt đầu ML forecast, route optimization, thay thế accounting, hoặc microservices khi M2 inventory truth chưa được chứng minh.
