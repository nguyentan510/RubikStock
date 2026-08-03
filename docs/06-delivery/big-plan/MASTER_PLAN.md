# RubikStock Master Implementation Plan

## Mục tiêu

Chuyển RubikStock từ documentation foundation thành hệ thống quản lý kho có inventory truth, traceability theo Lot, fulfillment B2B, xử lý exception, delivery reconciliation và replenishment có thể giải thích.

Master Plan dùng ba nguyên tắc:

1. **Dependency-safe:** không xây consumer trước khi upstream truth đáng tin cậy.
2. **Vertical slice:** mỗi slice phải đi xuyên từ contract tới runtime evidence nhỏ nhất có ích.
3. **Evidence-first:** trạng thái chỉ tăng khi test/gate thực sự pass.

## Phân tích và quyết định triển khai

### Vì sao không triển khai theo danh sách màn hình

UI Product, Nhập kho hoặc Xuất kho có thể nhìn hoàn chỉnh nhưng vẫn sai nếu UOM, Lot, balance, reservation và approval chưa có invariant. Vì vậy, mỗi phase phải đóng đồng thời data contract, domain behavior, API, UI, tests và operations tối thiểu.

### Vì sao D0-D1 vẫn phải đóng dù D2 đã bắt đầu

D2 hiện đã có local technical foundation. Tuy nhiên 14 mục `TBD` vẫn ảnh hưởng trực tiếp tới schema và workflow. Foundation có thể tiếp tục harden, nhưng không được đưa domain schema M1-M2 lên trạng thái accepted trước khi các quyết định liên quan được chốt hoặc defer có chủ ý.

### Vì sao M2 là trục chính

Inbound, outbound, return, delivery và planning đều tiêu thụ inventory truth. Append-only movement, balance projection, Lot/location/status scope và no-negative transaction phải được chứng minh ở M2 trước khi mở rộng nghiệp vụ.

### Vì sao M7-M9 bị trì hoãn

Forecast cần sales history, stockout flags, lead time, event data và inventory đủ chất lượng. Optimization không được dùng để che lỗi correctness hoặc quy trình chưa ổn định.

## Dependency map

```text
D0 Product truth
  -> D1 Business contracts
      -> D2 Technical foundation
          -> M1 Master data + warehouse map
              -> M2 Inventory ledger + opening balance
                  -> M3 Inbound
                  -> M4 Reservation + FEFO + outbound
                      -> M5 Returns + quality + destruction
                          -> M6 Company delivery
                              -> M7 Replenishment + seasonality
                                  -> M8 Production qualification
                                      -> M9 Evidence-driven optimization
```

M3 và một phần M4 có thể phát triển song song sau khi M2 contracts ổn định, nhưng không được merge behavior làm thay đổi inventory nếu M2 gate chưa pass.

## Trạng thái baseline ngày 2026-08-03

| Phase | Documentation | Implementation | Runtime evidence | Quyết định |
|---|---|---|---|---|
| D0 | Draft đầy đủ | N/A | Chưa có acceptance | Active decision track |
| D1 | Draft rules/contracts | Chưa có domain code | Chưa có acceptance | Active decision track |
| D2 | Draft + scaffold | Partial | Local PostgreSQL/API/web verified | Active engineering track |
| M1-M8 | Planned | Chưa bắt đầu | Chưa có | Locked theo dependency |
| M9 | Định hướng | Chưa bắt đầu | Chưa có benefit evidence | Deferred |

## Execution unit chuẩn

Mỗi work package được triển khai bằng một bounded slice theo thứ tự:

```text
Decision/TBD
-> Business rule hoặc ADR
-> Data/API contract
-> Migration
-> Domain/application service
-> API/UI nhỏ nhất có ích
-> Unit/contract/integration tests
-> Runtime smoke hoặc rehearsal
-> Traceability + implementation status
```

Một slice không được coi là hoàn thành nếu chỉ có UI, chỉ có migration hoặc chỉ có documentation.

## Definition of Ready

Trước khi bắt đầu một work package:

- Upstream gate cần thiết đã pass hoặc có bounded exception được ghi lại.
- Business rule liên quan không còn xung đột.
- Input/output/owner/state/failure mode đã rõ.
- Dữ liệu test không chứa dữ liệu kinh doanh thật.
- Compatibility, migration và rollback/reversal đã được xác định khi có persisted state.
- Acceptance test có thể mô tả trước khi code.

## Definition of Done

Một work package chỉ `DONE` khi:

- Code nằm đúng module boundary.
- Migration có upgrade path và clean-rebuild evidence.
- Server-side authorization được enforce khi có privileged action.
- Business invariants có automated tests.
- API/OpenAPI và error behavior thống nhất.
- Audit evidence tồn tại cho hành động cần kiểm soát.
- Documentation, traceability và implementation status phản ánh evidence thật.
- Không để lại finding security mức cao chưa có disposition được duyệt.

## Đồng bộ artifacts trong mỗi slice

| Artifact | Khi nào phải cập nhật |
|---|---|
| `BUSINESS_RULES.md` / `STATE_MACHINES.md` | Khi semantics hoặc transition thay đổi |
| ADR / architecture | Khi đổi boundary, provider hoặc transaction ownership |
| Alembic migrations | Khi persisted schema thay đổi |
| OpenAPI/Pydantic schemas | Khi public API thay đổi |
| Domain/database tests | Khi thêm invariant hoặc constraint |
| `TRACEABILITY_MATRIX.md` | Khi rule có implementation/verification mới |
| `IMPLEMENTATION_STATUS.md` | Sau khi có evidence thực tế |
| Operations runbooks | Khi deploy, recovery hoặc operator command thay đổi |

## Nhịp triển khai đề xuất

Không khóa kế hoạch theo số tuần khi chưa biết team capacity. Dùng nhịp theo gate:

1. Chọn một phase active và tối đa một vertical slice `in_progress`.
2. Review business decision trước khi tạo persisted contract.
3. Merge slice nhỏ sau khi targeted gate pass.
4. Chạy phase regression trước khi chuyển phase.
5. Demo bằng sanitized fixtures cho business owner.
6. Ghi sign-off hoặc open issue; không dùng im lặng làm acceptance.

## Release strategy

- Pilot một warehouse và một tập SKU đại diện trước.
- Dual-run Excel và RubikStock trong bounded reconciliation window.
- Không cho phép hai hệ thống cùng là inventory writer không có ownership rõ ràng.
- Chỉ cutover khi opening balance, movements và physical count reconcile.
- Rollback phải bảo toàn transaction history đã phát sinh.

## Current execution queue

Work-package status hiện hành được theo dõi tại [`CURRENT_PHASE_TRACKER.md`](CURRENT_PHASE_TRACKER.md).

1. Đóng D0.1-D0.5: gán owner và xử lý các `TBD` ảnh hưởng schema/workflow.
2. Đóng D1.1-D1.7: business acceptance cho inventory, Lot, UOM, outbound, return và delivery.
3. Song song harden D2.1-D2.9: auth/RBAC, clean migration reset, staging và security findings.
4. Chỉ sau đó mở M1.1 cho master-data schema.

## Scope control

Không mở microservices, Redis, message broker, ML forecast, route optimization hoặc accounting replacement khi chưa có evidence rằng modular monolith và flow hiện tại không đáp ứng được nhu cầu.
