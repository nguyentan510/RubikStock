# Current Phase Tracker

- Snapshot date: 2026-08-03
- Active decision track: D0-D1
- Active engineering track: D2
- Next domain phase: M1, hiện đang locked

Tracker này phản ánh evidence hiện có. Khi một work package được triển khai, status phải được cập nhật cùng `IMPLEMENTATION_STATUS.md` và `TRACEABILITY_MATRIX.md` nếu có rule implementation liên quan.

## Status vocabulary

- `DRAFTED`: tài liệu đã có, chờ review/acceptance.
- `OPEN`: câu hỏi hoặc quyết định chưa có disposition.
- `PARTIAL`: có một phần deliverable/evidence nhưng chưa đủ work-package gate.
- `LOCAL_VERIFIED`: đã chạy thành công trong local target.
- `NOT_STARTED`: chưa có implementation/evidence.
- `LOCKED`: upstream dependency chưa pass.

## D0 tracker

| ID | Status | Evidence hiện có | Việc còn lại |
|---|---|---|---|
| D0.1 | `DRAFTED` | Vision/scope/non-goals | RUBIK review và acceptance |
| D0.2 | `DRAFTED` | Users/roles draft | Xác nhận named owners/approvers |
| D0.3 | `PARTIAL` | AS-IS và Excel migration assumptions | Kiểm kê source thật trong private environment |
| D0.4 | `OPEN` | `TBD-001..014` đã đăng ký | Gán owner và disposition |
| D0.5 | `PARTIAL` | Data classification/repository policy | Chọn license và duyệt public/private boundary |
| D0.6 | `NOT_STARTED` | Chưa có sign-off | Tổ chức product acceptance review |

## D1 tracker

| ID | Status | Evidence hiện có | Việc còn lại |
|---|---|---|---|
| D1.1 | `DRAFTED` | `INV-001..008`, ledger scenarios | Business acceptance |
| D1.2 | `DRAFTED` | Lot/UOM rules và contracts | Đóng `TBD-002..003` |
| D1.3 | `DRAFTED` | Inbound TO-BE/state | Business walkthrough |
| D1.4 | `DRAFTED` | `OUT-001..010`, FEFO contract | Đóng shelf-life/override decisions |
| D1.5 | `DRAFTED` | Return/quality/destruction rules | Evidence và approval thresholds |
| D1.6 | `DRAFTED` | Delivery/planning boundaries | Delivery/planning owner review |
| D1.7 | `DRAFTED` | Audit/security rules | Permission matrix acceptance |
| D1.8 | `DRAFTED` | Conceptual data/module docs | Cross-document review |
| D1.9 | `NOT_STARTED` | Chưa có sign-off | Gate D1 review |

## D2 tracker

| ID | Status | Evidence hiện có | Việc còn lại |
|---|---|---|---|
| D2.1 | `PARTIAL` | Git/GitHub repository | License và branch/security policy |
| D2.2 | `LOCAL_VERIFIED` | Setup script, pinned lockfiles, Docker PostgreSQL | Clean-machine verification |
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

1. Chạy D0 decision workshop để gán owner/disposition cho `TBD-001..014`.
2. Review D1 theo scenario inventory/UOM/Lot/outbound/return/delivery.
3. Song song đóng D2.1, D2.3 và lập implementation slice D2.4-D2.5.
4. Không tạo M1 persisted schema trước khi các quyết định UOM/Lot/location liên quan được chốt.
