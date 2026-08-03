# Big Plan Map

`big-plan` là lớp điều phối chi tiết cho toàn bộ quá trình triển khai RubikStock. Nó không thay thế business rules, architecture, migration, tests hoặc runtime evidence.

## Cách dùng

1. Đọc [`MASTER_PLAN.md`](MASTER_PLAN.md) để biết dependency, gate và trạng thái tổng thể.
2. Đọc [`CURRENT_PHASE_TRACKER.md`](CURRENT_PHASE_TRACKER.md) để biết work package đang active và evidence còn thiếu.
3. Chỉ mở roadmap của phase đang active.
4. Triển khai từng work package theo đúng thứ tự dependency.
5. Cập nhật code, tests, contracts, traceability và implementation status trong cùng một slice.
6. Không nâng maturity nếu chưa có evidence được yêu cầu.

## Roadmap theo phase

| Phase | Roadmap | Trạng thái hiện tại |
|---|---|---|
| D0 | [`D0_PRODUCT_TRUTH.md`](D0_PRODUCT_TRUTH.md) | `PROPOSED`, chờ business acceptance |
| D1 | [`D1_BUSINESS_CONTRACTS.md`](D1_BUSINESS_CONTRACTS.md) | `PROPOSED`, chờ business acceptance |
| D2 | [`D2_TECHNICAL_FOUNDATION.md`](D2_TECHNICAL_FOUNDATION.md) | `IMPLEMENTED_PARTIAL`, local runtime đã verify |
| M1 | [`M1_MASTER_DATA_WAREHOUSE_MAP.md`](M1_MASTER_DATA_WAREHOUSE_MAP.md) | `PLANNED`, bị khóa bởi D0-D2 |
| M2 | [`M2_INVENTORY_LEDGER.md`](M2_INVENTORY_LEDGER.md) | `PLANNED`, bị khóa bởi M1 |
| M3 | [`M3_INBOUND.md`](M3_INBOUND.md) | `PLANNED`, bị khóa bởi M2 |
| M4 | [`M4_B2B_OUTBOUND.md`](M4_B2B_OUTBOUND.md) | `PLANNED`, bị khóa bởi M2-M3 |
| M5 | [`M5_QUALITY_EXCEPTIONS.md`](M5_QUALITY_EXCEPTIONS.md) | `PLANNED`, bị khóa bởi M2-M4 |
| M6 | [`M6_COMPANY_DELIVERY.md`](M6_COMPANY_DELIVERY.md) | `PLANNED`, bị khóa bởi M4-M5 |
| M7 | [`M7_REPLENISHMENT.md`](M7_REPLENISHMENT.md) | `PLANNED`, bị khóa bởi qualified history |
| M8 | [`M8_PRODUCTION_QUALIFICATION.md`](M8_PRODUCTION_QUALIFICATION.md) | `PLANNED`, bị khóa bởi scope release đã chọn |
| M9 | [`M9_OPTIMIZATION.md`](M9_OPTIMIZATION.md) | `DEFERRED`, chỉ mở sau production evidence |

## Quy tắc trạng thái

- `PROPOSED`: đã mô tả nhưng chưa được chấp nhận.
- `ACCEPTED`: business/architecture owner đã duyệt.
- `IMPLEMENTED_PARTIAL`: đã có một phần code nhưng chưa pass exit gate.
- `IMPLEMENTED`: implementation và automated verification của phase đã hoàn tất.
- `RUNTIME_VERIFIED`: đã chạy thành công trong môi trường mục tiêu.
- `DEFERRED`: cố ý chưa làm vì dependency hoặc evidence chưa đủ.
- `BLOCKED`: không thể tiến tiếp vì thiếu quyết định hoặc external state bắt buộc.

`PLANNED` trong bảng trên chỉ biểu thị thứ tự dự kiến, không phải maturity chính thức của product.
