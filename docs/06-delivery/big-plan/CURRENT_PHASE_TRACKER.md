# Current Phase Tracker

- Snapshot date: 2026-08-03
- Active decision track: D0-D1 closed
- Active engineering track: D2
- Next domain phase: M1, hiện đang locked

Tracker này phản ánh evidence hiện có. Khi một work package được triển khai, status phải được cập nhật cùng `IMPLEMENTATION_STATUS.md` và `TRACEABILITY_MATRIX.md` nếu có rule implementation liên quan.

## Status vocabulary

- `DRAFTED`: tài liệu đã có, chờ review/acceptance.
- `IN_PROGRESS`: work package đã bắt đầu và đang chờ deliverable/decision tiếp theo.
- `OPEN`: câu hỏi hoặc quyết định chưa có disposition.
- `PARTIAL`: có một phần deliverable/evidence nhưng chưa đủ work-package gate.
- `LOCAL_VERIFIED`: đã chạy thành công trong local target.
- `READY_FOR_REVIEW`: deliverable đã đủ để owner thực hiện acceptance review.
- `ACCEPTED`: business/architecture owner đã xác nhận rõ ràng.
- `COMPLETED`: work package đã đủ deliverable/disposition; không đồng nghĩa phase gate đã pass.
- `NOT_STARTED`: chưa có implementation/evidence.
- `LOCKED`: upstream dependency chưa pass.

## D0 tracker

| ID | Status | Evidence hiện có | Việc còn lại |
|---|---|---|---|
| D0.1 | `ACCEPTED` | Vision/scope/non-goals trong D0 Product Acceptance | Không còn; thay đổi scope cần decision mới |
| D0.2 | `ACCEPTED` | Users/roles và `Quản lý Kho` business owner | Named user account được tạo ở D2/M1, không giữ D0 mở |
| D0.3 | `ACCEPTED` | AS-IS và clean-start/cutover direction | Physical mapping/opening-count rehearsal chuyển M1-M2 |
| D0.4 | `COMPLETED` | 12/14 `ACCEPTED`, 2/14 `DEFERRED_WITH_OWNER`, 0 Open không owner | Theo dõi due gate của TBD-007/TBD-012 |
| D0.5 | `ACCEPTED` | Public/private boundary accepted; OSS license deferred có owner/due gate | CEO/Project Owner chỉ mở lại khi có reuse/contribution intent |
| D0.6 | `ACCEPTED` | [`D0_PRODUCT_ACCEPTANCE.md`](D0_PRODUCT_ACCEPTANCE.md) | Accepted bởi `Quản lý Kho` ngày 2026-08-03 |

## D1 tracker

| ID | Status | Evidence hiện có | Việc còn lại |
|---|---|---|---|
| D1.1 | `ACCEPTED` | `INV-001..008` và `D1-A01..A08` accepted bởi Quản lý Kho | Dùng làm contract đầu vào cho M2 sau D1/D2 gate |
| D1.2 | `ACCEPTED` | `LOT-001..006`, `UOM-001..004` và D1 Batch A accepted | Dùng làm contract đầu vào cho M1-M2 sau D1/D2 gate |
| D1.3 | `ACCEPTED` | `INB-001..009` và `D1-B01..B08` accepted bởi Quản lý Kho | Dùng làm contract đầu vào cho M3 sau upstream gates |
| D1.4 | `ACCEPTED` | `OUT-001..011` và `D1-C01..C11` accepted bởi Quản lý Kho | Dùng làm contract đầu vào cho M4 sau upstream gates |
| D1.5 | `ACCEPTED` | `QLT/RET/DST` và `D1-D01..D13` accepted bởi Quản lý Kho | Dùng làm contract đầu vào cho M5 sau upstream gates |
| D1.6 | `ACCEPTED` | Delivery accepted Batch D; planning accepted Batch E | Dùng làm contract đầu vào cho M6-M7 sau upstream gates |
| D1.7 | `ACCEPTED` | `AUD-001..006`, `SEC-001..006` và Batch E scenarios accepted | Dùng làm contract đầu vào cho D2 auth/audit/private files |
| D1.8 | `COMPLETED` | Conceptual ownership và cross-document consistency review | Evidence tại [`D1_FINAL_ACCEPTANCE.md`](D1_FINAL_ACCEPTANCE.md) |
| D1.9 | `ACCEPTED` | 58 contract points, 56 scenarios và cross-document review | Accepted bởi `Quản lý Kho` ngày 2026-08-03 |

## D2 tracker

| ID | Status | Evidence hiện có | Việc còn lại |
|---|---|---|---|
| D2.1 | `PARTIAL` | Git/GitHub; public source-visible/no-OSS-license disposition | Branch/security policy; license deferred theo owner/due gate |
| D2.2 | `LOCAL_VERIFIED` | Full-stack Compose build/start; migrate exit 0; API/web/PostgreSQL healthy; `RUBIKSTOCK_STACK_SMOKE_OK` | Reproduce trên clean machine để complete work-package gate |
| D2.3 | `PARTIAL` | Alembic baseline và PostgreSQL upgrade pass | Clean reset/rollback lifecycle evidence |
| D2.4 | `NOT_STARTED` | Chưa có authentication adapter | Implement và auth smoke |
| D2.5 | `NOT_STARTED` | Chưa có RBAC enforcement | Permission allow/deny tests |
| D2.6 | `PARTIAL` | OpenAPI và health schemas | Error/idempotency/request contract baseline |
| D2.7 | `NOT_STARTED` | Chưa có private file integration | Storage/access policy và tests |
| D2.8 | `PARTIAL` | CI scaffold, local checks, secret scan config | CI evidence và high findings disposition |
| D2.9 | `NOT_STARTED` | Chưa có staging deploy | Isolated staging + rollback smoke |
| D2.10 | `NOT_STARTED` | Gate chưa review | Tổng hợp evidence sau D2.1-D2.9 |

## Locked phases

M1-M8 đều `LOCKED` theo dependency trong `MASTER_PLAN.md`. M9 là `DEFERRED` cho tới khi có production evidence và measured bottleneck.

## Next bounded actions

1. Đóng D2.3 migration lifecycle: clean rebuild và rollback/forward policy evidence.
2. Reproduce D2.2 trên clean machine khi có target; không giữ D2.3/auth chờ việc này nếu local contract đủ.
3. Sau D2.3, mở D2.4-D2.5 auth/RBAC.
3. Song song đóng D2.1, D2.3 và full-stack Local Docker slice trước D2.4-D2.5.
4. Không mở M1 persisted domain schema cho tới khi D1/D2 dependency tương ứng pass.
