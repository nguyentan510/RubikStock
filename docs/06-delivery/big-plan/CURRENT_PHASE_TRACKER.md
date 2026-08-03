# Current Phase Tracker

- Snapshot date: 2026-08-03
- Active decision track: D0-D1
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
- `COMPLETED`: work package đã đủ deliverable/disposition; không đồng nghĩa phase gate đã pass.
- `NOT_STARTED`: chưa có implementation/evidence.
- `LOCKED`: upstream dependency chưa pass.

## D0 tracker

| ID | Status | Evidence hiện có | Việc còn lại |
|---|---|---|---|
| D0.1 | `DRAFTED` | Vision/scope/non-goals | RUBIK review và acceptance |
| D0.2 | `DRAFTED` | Users/roles draft | Xác nhận named owners/approvers |
| D0.3 | `PARTIAL` | AS-IS và clean-start/cutover direction | Khảo sát physical layout và lập opening-count plan |
| D0.4 | `COMPLETED` | 12/14 `ACCEPTED`, 2/14 `DEFERRED_WITH_OWNER`, 0 Open không owner | Theo dõi due gate của TBD-007/TBD-012 |
| D0.5 | `PARTIAL` | Public source-visible/no-OSS-license policy và private-data boundary đã có disposition | CEO/Project Owner chỉ chốt license khi có reuse/contribution intent |
| D0.6 | `READY_FOR_REVIEW` | [`D0_PRODUCT_ACCEPTANCE.md`](D0_PRODUCT_ACCEPTANCE.md) | `Quản lý Kho` review và xác nhận acceptance |

## D1 tracker

| ID | Status | Evidence hiện có | Việc còn lại |
|---|---|---|---|
| D1.1 | `DRAFTED` | `INV-001..008`, ledger scenarios | Business acceptance |
| D1.2 | `DRAFTED` | D0 Lot/UOM/measured-sale policy đã accepted | D1 scenario review và contract acceptance |
| D1.3 | `DRAFTED` | Inbound TO-BE/state | Business walkthrough |
| D1.4 | `DRAFTED` | D0 shelf-life days/percent và one-level override accepted | D1 allocation/override scenario review |
| D1.5 | `DRAFTED` | D0 photo+note và approval shape accepted | D1 return/destruction scenario review |
| D1.6 | `DRAFTED` | Delivery/planning boundaries | Delivery/planning owner review |
| D1.7 | `DRAFTED` | D0 no-delete/retention governance accepted | Permission/retention contract acceptance |
| D1.8 | `DRAFTED` | Conceptual data/module docs | Cross-document review |
| D1.9 | `NOT_STARTED` | Chưa có sign-off | Gate D1 review |

## D2 tracker

| ID | Status | Evidence hiện có | Việc còn lại |
|---|---|---|---|
| D2.1 | `PARTIAL` | Git/GitHub; public source-visible/no-OSS-license disposition | Branch/security policy; license deferred theo owner/due gate |
| D2.2 | `LOCAL_VERIFIED` | Setup script, pinned lockfiles, Docker PostgreSQL | Full-stack Compose và clean-machine verification |
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

1. `Quản lý Kho` review [`D0_PRODUCT_ACCEPTANCE.md`](D0_PRODUCT_ACCEPTANCE.md).
2. Review D1 theo scenario inventory/UOM/Lot/outbound/return/delivery.
3. Song song đóng D2.1, D2.3 và full-stack Local Docker slice trước D2.4-D2.5.
4. Không mở Accounting integration hoặc gắn OSS license nếu chưa đạt due gate của TBD-007/TBD-012.
