# Acceptance Gates

## Gate D0 - Product acceptance

- Status: `PASSED` ngày 2026-08-03, approved by `Quản lý Kho`.
- Evidence: [`big-plan/D0_PRODUCT_ACCEPTANCE.md`](big-plan/D0_PRODUCT_ACCEPTANCE.md).

- Business context và scope được RUBIK review.
- Accounting boundary được chấp nhận.
- Open questions được gán owner.
- Không có confidential data trong public repository.

## Gate D1 - Business contract acceptance

- Status: `PASSED` ngày 2026-08-03, approved by `Quản lý Kho`.
- Evidence: [`big-plan/D1_FINAL_ACCEPTANCE.md`](big-plan/D1_FINAL_ACCEPTANCE.md).

- Rule cho inventory, UOM, Lot/date, FEFO, return, destruction, delivery được chấp nhận hoặc thay đổi rõ ràng.
- State transition và ownership của approval được chấp nhận.
- Các kịch bản đại diện thực tế được review.
- Conceptual data model hỗ trợ mọi quy trình đã chấp nhận.

## Gate D2 - Technical foundation

- Setup local bằng một lệnh.
- Database migration có thể rebuild local database sạch.
- CI chạy lint, types, unit/contract tests, migration validation, build, và secret scan.
- Staging tách biệt khỏi production.
- Authentication/authorization smoke pass.
- Không còn security finding mức cao chưa xử lý.

## Gate M2 - Inventory truth

- Ledger bằng projection với toàn bộ test/rehearsal data.
- Test no-negative và concurrent reservation pass.
- Transfer bảo toàn quantity.
- Reversal giữ nguyên lịch sử.
- Rehearsal opening-stock reconcile đúng count đã duyệt.

## Gate M4 - Fulfillment

- Shelf-life eligibility của customer được áp dụng trước FEFO.
- Allocation nhiều Lot và nhiều location pass.
- Short pick/reallocation và expired-after-allocation pass.
- Shipment tiêu thụ reservation đúng một lần.

## Gate M5-M6 - Exceptions and delivery

- Return không thể bypass quarantine.
- Destruction không thể tự approve hoặc post hai lần.
- Delivery partial/failed reconcile quantity đã giao và mang về.
- Trace của Lot đi tới receipt, stock, shipments, customers, returns, và destruction.

## Gate M7 - Planning

- Recommendation reproduce được từ input/version đã lưu.
- Xử lý lost-sale/stockout phải rõ ràng.
- Event window theo lịch âm/mùa vụ phải theo từng năm.
- Baseline WAPE và bias phải được báo cáo trước khi so sánh ML.

## Gate M8 - Production qualification

- UAT có chữ ký của business owners.
- Backup restore đã thực sự test.
- Incident, secret rotation, và access revocation được diễn tập.
- Monitoring và reconciliation alerts tới đúng owner có trách nhiệm.
- Điểm quyết định cutover và rollback được chấp nhận.
- Production promotion được ủy quyền rõ ràng.
