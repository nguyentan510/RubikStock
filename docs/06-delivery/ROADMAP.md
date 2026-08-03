# Product Roadmap

Hoàn thành roadmap không đồng nghĩa với production readiness. Mỗi phase phải pass acceptance gate của nó trước khi work phụ thuộc được đưa lên.

## D0 - Product truth

- Vision, scope, users, glossary, AS-IS, non-goals, open questions.
- Exit: RUBIK review và chấp nhận/chỉnh sửa business context và boundary.

## D1 - Business contracts

- TO-BE flow, rule ID, state machine, matrix exception và approval.
- Conceptual architecture/data contracts.
- Exit: không còn xung đột chưa giải quyết trong semantics của inventory, Lot, reservation, return, destruction, và delivery.

## D2 - Technical foundation

- Quyết định Git repository/license.
- FastAPI/Next.js skeleton, local environment, Supabase project.
- Authentication, authorization skeleton, migrations, CI, logging, OpenAPI.
- Exit: local build có thể tái tạo, staging deploy cô lập, secret scan, migration reset, health smoke.

## M1 - Master data và warehouse map

- Product, category, UOM/conversion, supplier/customer, warehouse/location.
- Phân tích Excel private và zoning kho.
- Exit: import master data đại diện mà không có conversion mơ hồ.

## M2 - Inventory ledger và opening balance

- Lots, movements, balances, transfers, count, adjustment, reconciliation validator.
- Chạy rehearsal cutover cho opening stock có kiểm soát.
- Exit: reconciliation giữa ledger/projection và test no-negative pass.

## M3 - Inbound

- Purchase order reference, receipt, discrepancy, QC entry, put-away.
- Exit: receipt đại diện trace được tới stock theo Lot-location đủ điều kiện.

## M4 - B2B outbound

- Sales order, reservation, eligibility, FEFO, allocation nhiều Lot, pick, stage, shipment.
- Exit: concurrent reservation và các kịch bản fulfillment lớn nhiều Lot pass.

## M5 - Exceptions và quality

- Return quarantine, inspection, disposition, damage, expiry, recall, destruction.
- Exit: không exception nào có thể âm thầm khôi phục/che giấu stock; approval và trace tests pass.

## M6 - Company delivery

- Trip, vehicle/driver, loading, stops, POD, reconciliation cho delivery partial/failed.
- Exit: reconciliation từ shipment tới POD/return pass.

## M7 - Explainable replenishment

- Safety stock, lead time, MOQ/case pack, business event/lunar calendar, baseline forecast, purchase proposal.
- Exit: recommendation reproduce được từ input/version đã lưu và manual override được audit.

## M8 - Production qualification

- Backup/restore exercise, monitoring, incident drill, performance baseline, UAT, training, cutover.
- Exit: checklist production qualification pass và owner có thẩm quyền approve promotion.

## M9 - Optimization after evidence

- Forecast model comparison, route optimization, integration, hoặc scaling chỉ khi có lợi ích đo được.
