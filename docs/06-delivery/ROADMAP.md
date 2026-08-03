# Product Roadmap

Hoàn thành roadmap không đồng nghĩa với production readiness. Mỗi phase phải pass acceptance gate của nó trước khi work phụ thuộc được đưa lên.

Work packages, dependency và evidence chi tiết của từng phase nằm trong [`big-plan/README.md`](big-plan/README.md).

## D0 - Product truth

Roadmap chi tiết: [`big-plan/D0_PRODUCT_TRUTH.md`](big-plan/D0_PRODUCT_TRUTH.md).

- Vision, scope, users, glossary, AS-IS, non-goals, open questions.
- Exit: RUBIK review và chấp nhận/chỉnh sửa business context và boundary.

## D1 - Business contracts

Roadmap chi tiết: [`big-plan/D1_BUSINESS_CONTRACTS.md`](big-plan/D1_BUSINESS_CONTRACTS.md).

- TO-BE flow, rule ID, state machine, matrix exception và approval.
- Conceptual architecture/data contracts.
- Exit: không còn xung đột chưa giải quyết trong semantics của inventory, Lot, reservation, return, destruction, và delivery.

## D2 - Technical foundation

Roadmap chi tiết: [`big-plan/D2_TECHNICAL_FOUNDATION.md`](big-plan/D2_TECHNICAL_FOUNDATION.md).

- Public source-visible/no-OSS-license repository governance và due gate cho license review.
- FastAPI/Next.js skeleton, full-stack Local Docker Compose và Linux VPS target.
- Authentication, authorization skeleton, migrations, CI, logging, OpenAPI.
- Exit: local build có thể tái tạo, staging deploy cô lập, secret scan, migration reset, health smoke.

## M1 - Master data và warehouse map

Roadmap chi tiết: [`big-plan/M1_MASTER_DATA_WAREHOUSE_MAP.md`](big-plan/M1_MASTER_DATA_WAREHOUSE_MAP.md).

- Product, category, UOM/conversion, supplier/customer, warehouse/location.
- Phân tích Excel private và zoning kho.
- Exit: import master data đại diện mà không có conversion mơ hồ.

## M2 - Inventory ledger và opening balance

Roadmap chi tiết: [`big-plan/M2_INVENTORY_LEDGER.md`](big-plan/M2_INVENTORY_LEDGER.md).

- Lots, movements, balances, transfers, count, adjustment, reconciliation validator.
- Chạy rehearsal cutover cho opening stock có kiểm soát.
- Exit: reconciliation giữa ledger/projection và test no-negative pass.

## M3 - Inbound

Roadmap chi tiết: [`big-plan/M3_INBOUND.md`](big-plan/M3_INBOUND.md).

- Purchase order reference, receipt, discrepancy, QC entry, put-away.
- Exit: receipt đại diện trace được tới stock theo Lot-location đủ điều kiện.

## M4 - B2B outbound

Roadmap chi tiết: [`big-plan/M4_B2B_OUTBOUND.md`](big-plan/M4_B2B_OUTBOUND.md).

- Sales order, reservation, eligibility, FEFO, allocation nhiều Lot, pick, stage, shipment.
- Exit: concurrent reservation và các kịch bản fulfillment lớn nhiều Lot pass.

## M5 - Exceptions và quality

Roadmap chi tiết: [`big-plan/M5_QUALITY_EXCEPTIONS.md`](big-plan/M5_QUALITY_EXCEPTIONS.md).

- Return quarantine, inspection, disposition, damage, expiry, recall, destruction.
- Exit: không exception nào có thể âm thầm khôi phục/che giấu stock; approval và trace tests pass.

## M6 - Company delivery

Roadmap chi tiết: [`big-plan/M6_COMPANY_DELIVERY.md`](big-plan/M6_COMPANY_DELIVERY.md).

- Trip, vehicle/driver, loading, stops, POD, reconciliation cho delivery partial/failed.
- Exit: reconciliation từ shipment tới POD/return pass.

## M7 - Explainable replenishment

Roadmap chi tiết: [`big-plan/M7_REPLENISHMENT.md`](big-plan/M7_REPLENISHMENT.md).

- Safety stock, lead time, MOQ/case pack, business event/lunar calendar, baseline forecast, purchase proposal.
- Exit: recommendation reproduce được từ input/version đã lưu và manual override được audit.

## M8 - Production qualification

Roadmap chi tiết: [`big-plan/M8_PRODUCTION_QUALIFICATION.md`](big-plan/M8_PRODUCTION_QUALIFICATION.md).

- Backup/restore exercise, monitoring, incident drill, performance baseline, UAT, training, cutover.
- Exit: checklist production qualification pass và owner có thẩm quyền approve promotion.

## M9 - Optimization after evidence

Roadmap chi tiết: [`big-plan/M9_OPTIMIZATION.md`](big-plan/M9_OPTIMIZATION.md).

- Forecast model comparison, route optimization, integration, hoặc scaling chỉ khi có lợi ích đo được.
