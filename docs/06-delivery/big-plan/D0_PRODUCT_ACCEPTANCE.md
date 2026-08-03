# D0 Product Acceptance Review

- Status: `READY_FOR_REVIEW`
- Prepared: 2026-08-03
- Proposed approver: `Quản lý Kho`
- Scope: D0 product truth và disposition cho `TBD-001..014`

## Outcome đề nghị

Chấp nhận D0 với hai quyết định deferred có owner. D0 không tuyên bố business contracts D1 đã accepted, technical foundation D2 đã hoàn tất, hoặc RubikStock production-ready.

## Decision disposition

| Disposition | Số lượng | IDs |
|---|---:|---|
| `ACCEPTED` | 12 | `TBD-001..006`, `TBD-008..011`, `TBD-013`, `TBD-014` |
| `DEFERRED_WITH_OWNER` | 2 | `TBD-007`, `TBD-012` |
| `OPEN` không owner | 0 | Không có |

## Deferred decision control

| ID | Owner | Quyết định tạm thời | Điều kiện mở lại | Due gate |
|---|---|---|---|---|
| TBD-007 | Kế toán | Không tích hợp/export MISA trong MVP; giữ boundary operational/financial | Xác định product/edition, mapping, test API và reconciliation contract | Trước integration slice, mặc định M9 |
| TBD-012 | CEO/Project Owner | Repository public source-visible, chưa cấp open-source license; có thể đổi private sau | Chốt contribution/reuse/distribution intent và legal review | Trước khi nhận external contribution hoặc phát hành reusable distribution |

Hai mục deferred không chặn D1/M1 vì chúng không được phép tạo integration hoặc quyền reuse ngầm. Chúng sẽ trở thành blocker nếu một slice cần Accounting integration hoặc external open-source distribution.

## Acceptance checklist

- [x] Scope MVP/non-goal đã được tài liệu hóa.
- [x] Hai warehouse, khoảng 300 SKU, zone baseline và pilot đã có disposition.
- [x] UOM, case break, measured sale, Lot/date và clean-start policy đã có disposition.
- [x] Order source, multi-shipment, partial delivery/backorder đã có disposition.
- [x] Shelf-life, FEFO override, adjustment, return/destruction evidence và retention đã có disposition.
- [x] Online-first runtime và Local Docker-first/VPS target đã có disposition.
- [x] Không còn TBD chỉ mang status Open mà không có owner.
- [ ] `Quản lý Kho` review và ghi acceptance D0.

## Acceptance record

Chỉ đổi status thành `ACCEPTED` sau khi người dùng/business xác nhận rõ ràng.

| Field | Value |
|---|---|
| Decision | `PENDING_BUSINESS_ACCEPTANCE` |
| Approver | `Quản lý Kho` |
| Date | Chưa ghi |
| Notes | Chờ review checklist và deferred controls |

## Sau khi D0 được accepted

1. Review D1 bằng business scenarios, không mở lại discovery tổng quát.
2. Tiếp tục harden D2 theo Local Docker-first/VPS target.
3. Chỉ mở M1 khi các dependency gate tương ứng pass; D0 acceptance một mình không mở khóa M1.
