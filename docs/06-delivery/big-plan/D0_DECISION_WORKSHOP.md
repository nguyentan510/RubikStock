# D0 Decision Workshop

- Status: `COMPLETED`
- Started: 2026-08-03
- Facilitator: Codex
- Business decision owner: `Quản lý Kho`
- Source register: [`../../00-product/OPEN_QUESTIONS.md`](../../00-product/OPEN_QUESTIONS.md)

## Mục tiêu workshop

Xử lý `TBD-001..014` bằng một trong ba disposition rõ ràng:

- `ACCEPTED`: RUBIK chấp nhận quyết định và downstream documents phải được cập nhật.
- `DEFERRED_WITH_OWNER`: chưa quyết định ngay nhưng có owner, lý do, điều kiện đóng và phase deadline.
- `REJECTED`: loại phương án, ghi lý do và replacement direction.

Không dùng `implied acceptance`. Im lặng hoặc tiếp tục code không đồng nghĩa một business policy đã được duyệt.

## Đề xuất điều hành

Workshop được chia thành bốn batch để quyết định không bị lẫn giữa vận hành, dữ liệu, kiểm soát và platform:

1. **Batch A - Operating shape:** `TBD-001`, `TBD-004`, `TBD-005`, `TBD-011`.
2. **Batch B - Product/data truth:** `TBD-002`, `TBD-003`, `TBD-006`.
3. **Batch C - Customer/control/evidence:** `TBD-008`, `TBD-009`, `TBD-010`, `TBD-014`.
4. **Batch D - Integration/platform/legal:** `TBD-007`, `TBD-012`, `TBD-013`.

Thứ tự này giúp chốt operating reality trước, sau đó mới khóa schema và deployment decisions.

## Batch A - Operating shape

- Batch status: `ACCEPTED`
- Approved by: `Quản lý Kho`
- Decision date: 2026-08-03

| ID | Đề xuất mặc định | RUBIK cần xác nhận | Tác động downstream | Decision |
|---|---|---|---|---|
| TBD-001 | Hai warehouse, khoảng 300 SKU; dùng bốn zone cơ bản `INB`, `AVL`, `QTN`, `OUT`; pilot `WH-01`, bắt đầu tại `WH-01-AVL` | Đã xác nhận; tên thương mại/địa chỉ warehouse sẽ thu thập private ở M1 | M1 schema, label rollout, test volume | `ACCEPTED` |
| TBD-004 | Đơn chủ yếu đến từ Sales; Sales ghi/xác nhận trên RubikStock và RubikStock trở thành operational system of record của order sau confirmation | Đã xác nhận | M4 order scope, integration, user workflow | `ACCEPTED` |
| TBD-005 | Một order có thể giao nhiều đợt/nhiều chuyến; hỗ trợ `PARTIAL_DELIVERY` và `BACKORDER`, mỗi shipment reconcile riêng | Đã xác nhận | State machine, reservation, M4/M6 | `ACCEPTED` |
| TBD-011 | PC và mobile; Wi-Fi/4G kho/xe ổn định; MVP là online-first responsive web/PWA, offline write không thuộc MVP | Đã xác nhận | D2 UX/runtime, M1 labels, M3-M6 mobile flow | `ACCEPTED` |

### Zone baseline được chấp nhận

| Code | Zone | Mục đích |
|---|---|---|
| `INB` | Inbound/Receiving | Nhận hàng, kiểm đếm ban đầu trước put-away |
| `AVL` | Available Storage | Lưu stock đủ điều kiện bán/xuất |
| `QTN` | Controlled Hold | QC hold, quarantine, return, damaged, expired, destroy-pending; tách bin vật lý theo status |
| `OUT` | Outbound Staging | Tập kết hàng đã pick trước loading/shipment |

Inventory status vẫn là thuộc tính riêng của stock segment; zone không thay thế `QC_HOLD`, `QUARANTINE`, `DAMAGED`, `EXPIRED` hoặc `DESTROY_PENDING`.

Location code đi theo `warehouse-zone-rack-level-bin`; `level` có thể bỏ qua nếu layout không cần. `WH-01` được chọn làm primary pilot warehouse. Physical-label pilot bắt đầu tại `WH-01-AVL` với tập SKU đại diện, sau đó mở rộng `INB/QTN/OUT` để rehearsal end-to-end.

### Accepted decision records - Batch A

| ID | Disposition | Decision | Reason | Approved by/date | Affected artifacts và due gate |
|---|---|---|---|---|---|
| TBD-001 | `ACCEPTED` | 2 warehouse, khoảng 300 SKU, four-zone baseline; `WH-01-AVL` pilot | Giữ zoning đơn giản nhưng đủ cách ly và trace flow | Quản lý Kho / 2026-08-03 | Scope, M1 roadmap/data contract; M1 |
| TBD-004 | `ACCEPTED` | Sales là nguồn order chính; RubikStock là operational order truth sau confirmation | Loại bỏ order truth phân tán sau khi xác nhận | Quản lý Kho / 2026-08-03 | TO-BE, system context, M4; D1/M4 |
| TBD-005 | `ACCEPTED` | Cho phép multi-shipment, partial delivery và backorder | Phù hợp đơn B2B lớn và giao nhiều đợt/chuyến | Quản lý Kho / 2026-08-03 | State/outbound/delivery contracts; D1/M4/M6 |
| TBD-011 | `ACCEPTED` | PC/mobile, connectivity ổn định, online-first MVP | Không có evidence cần offline complexity ở MVP | Quản lý Kho / 2026-08-03 | UX/runtime/operations; D2 |

## Batch B - Product and data truth

- Batch status: `ACCEPTED`
- Approved by: `Quản lý Kho`
- Decision date: 2026-08-03

| ID | Đề xuất mặc định | RUBIK cần xác nhận | Tác động downstream | Decision |
|---|---|---|---|---|
| TBD-002 | Case/bag chỉ được break khi product có policy rõ; hỗ trợ bán/repack theo gram/kg và giữ genealogy về Lot/package gốc | Đã xác nhận; hiểu “product được phép” là cấu hình theo từng product | UOM model, packaging, labels, Lot trace | `ACCEPTED` |
| TBD-003 | Không import Lot/MFG/EXP từ Excel cũ; tạo clean-start templates và physical opening count. F&B mặc định bắt buộc Lot+EXP; short-life cold bắt buộc Lot+MFG+EXP; non-food không bắt buộc date | Đã chấp nhận hướng clean-start và policy khuyến nghị | M1 intake, M2 opening balance, M3 receipt | `ACCEPTED` |
| TBD-006 | Không import legacy sales history; bắt đầu capture chuẩn từ thời điểm vận hành mới. M7 chỉ dùng forward-qualified history và deterministic/manual planning cho tới khi đủ gate | Đã xác nhận | M7 qualification/backtest | `ACCEPTED` |

### Lot/date policy được chấp nhận

| Policy code | Áp dụng mặc định | Bắt buộc |
|---|---|---|
| `LOT_MFG_EXP_REQUIRED` | Kem, dairy, chilled, frozen và nhóm short shelf-life | Supplier Lot, MFG, EXP |
| `LOT_EXP_REQUIRED` | Bột, syrup, sauce, topping và F&B shelf-stable đóng gói | Supplier Lot, EXP; MFG phải nhập nếu có trên bao bì |
| `NO_DATE_TRACKING` | Bao bì, dụng cụ và non-food | Không bắt buộc Lot/MFG/EXP |

Product/category chưa phân loại dùng fail-safe default `LOT_EXP_REQUIRED`. Existing F&B stock không có Lot/EXP xác minh được tại opening count phải vào `QUARANTINE`, không được nhập `AVAILABLE`.

### Measured-sale policy được chấp nhận

- Chỉ product có `allows_case_break=true` mới được xé thùng/bán chai-gói lẻ.
- Chỉ product có `allows_measured_sale=true` mới được mở bao và bán theo gram/kg.
- Product đo theo weight dùng base UOM chính xác, mặc định `gram`.
- Khi mở bao/repack phải ghi operation, quantity tiêu thụ/tạo ra và genealogy về manufacturer/supplier Lot gốc.
- Không tạo manufacturer Lot mới; internal traceability unit có thể được tạo cho package đã mở/repack.

### Accepted decision records - Batch B

| ID | Disposition | Decision | Reason | Approved by/date | Affected artifacts và due gate |
|---|---|---|---|---|---|
| TBD-002 | `ACCEPTED` | Product-level case break và measured sale gram/kg có traceability | Phù hợp mô hình bán lẻ từ package lớn nhưng phải giữ Lot truth | Quản lý Kho / 2026-08-03 | UOM/rules/M1-M2; D1/M1 |
| TBD-003 | `ACCEPTED` | Không import legacy Lot/date; clean-start templates + physical opening count; category policy fail closed | Tiết kiệm migration effort mà không hy sinh safety của stock hiện hữu | Quản lý Kho / 2026-08-03 | Lot/cutover/templates; M1-M2 |
| TBD-006 | `ACCEPTED` | Không import legacy sales history; capture forward theo format chuẩn | Giảm data-cleaning scope và tránh forecast từ history không qualify | Quản lý Kho / 2026-08-03 | Sales template/planning; M4-M7 |

## Batch C - Customer, control and evidence

- Batch status: `ACCEPTED`
- Approved by: `Quản lý Kho`
- Decision date: 2026-08-03

| ID | Đề xuất mặc định | RUBIK cần xác nhận | Tác động downstream | Decision |
|---|---|---|---|---|
| TBD-008 | Đại lý/cửa hàng cần date xa; policy cấu hình theo customer/group/category/product bằng minimum days, minimum percent hoặc cả hai | Đã xác nhận; numeric thresholds sẽ là business configuration ở M1 | FEFO eligibility, M1 partner policy, M4 allocation | `ACCEPTED` |
| TBD-009 | FEFO override và stock adjustment luôn cần một cấp `Quản lý Kho` duyệt; không có second-level threshold; discount ngoài RubikStock | Đã xác nhận | D1 approval matrix, D2 RBAC, M2/M4/M5 | `ACCEPTED` |
| TBD-010 | Return và destruction bắt buộc ảnh + note; không bắt buộc video/chữ ký trong MVP | Đã xác nhận | Private Storage, retention, audit, M5/M6 | `ACCEPTED` |
| TBD-014 | Tạm thời giữ transaction/audit/POD/return/destruction evidence không thời hạn và không auto-delete; CEO final approval, Quản lý Kho operational review cho thay đổi retention | Đã xác nhận | Storage cost, privacy, M8 production gate | `ACCEPTED` |

### Shelf-life policy được chấp nhận

- Policy resolution: product/customer override -> customer group -> company default.
- Đại lý và cửa hàng là các group cần policy date xa có thể cấu hình.
- `minimum_remaining_days` và `minimum_remaining_percent` đều optional nhưng ít nhất một giá trị phải có khi policy active.
- Nếu cả hai được cấu hình, Lot phải đạt cả hai điều kiện (`AND`).
- Remaining days được tính tại planned delivery date.
- Remaining percent cần cả MFG và EXP; thiếu field cần thiết thì candidate không đủ điều kiện, không được suy đoán.
- Numeric thresholds không hard-code trong D0; chúng là versioned business configuration ở M1.

### Approval/evidence/retention policy được chấp nhận

- FEFO override: requester Sales/Warehouse, một cấp `Quản lý Kho` approve, reason bắt buộc; selected Lot vẫn phải saleable và đạt customer eligibility.
- Stock adjustment: requester và approver khác nhau; một cấp `Quản lý Kho` approve; không có second-level theo quantity/value.
- Discount không thuộc RubikStock; Sales/Accounting là source of truth.
- Return/destruction phải có ít nhất một private photo và note mô tả reason/condition/action.
- Tạm thời không auto-delete transaction, audit, POD, return và destruction evidence.
- Thay đổi retention hoặc deletion policy cần CEO final approval và Quản lý Kho operational review; mọi deletion sau này phải audit được.

### Accepted decision records - Batch C

| ID | Disposition | Decision | Reason | Approved by/date | Affected artifacts và due gate |
|---|---|---|---|---|---|
| TBD-008 | `ACCEPTED` | Dealer/shop shelf-life policy hỗ trợ days/percent/both | Khách nhập lại cần date xa và policy phải linh hoạt | Quản lý Kho / 2026-08-03 | Shelf-life contract/M1/M4; D1/M1 |
| TBD-009 | `ACCEPTED` | One-level Warehouse Manager approval cho FEFO override/adjustment; discount out of scope | Giữ workflow đơn giản nhưng vẫn có control | Quản lý Kho / 2026-08-03 | Approval/RBAC/M2/M4; D1-D2 |
| TBD-010 | `ACCEPTED` | Mandatory photo + note cho return/destruction | Đủ evidence vận hành tối thiểu | Quản lý Kho / 2026-08-03 | Files/quality/retention; D2/M5 |
| TBD-014 | `ACCEPTED` | Indefinite/no-auto-delete tạm thời; CEO final + Warehouse Manager review | Tránh mất audit evidence trước khi có policy chính thức | Quản lý Kho / 2026-08-03 | Retention/security/M8; D2/M8 |

## Batch D - Integration, platform and repository

- Batch status: `CLOSED_WITH_DEFERRED_ITEMS`
- Decision date: 2026-08-03
- Business owner for accepted runtime decision: `Quản lý Kho`

| ID | Đề xuất mặc định | RUBIK cần xác nhận | Tác động downstream | Decision |
|---|---|---|---|---|
| TBD-007 | Accounting/MISA tiếp tục là financial/invoice source of truth; MVP chưa export hoặc tích hợp | Chưa biết chính xác MISA product/edition và dữ liệu cần trao đổi; `Kế toán` sở hữu discovery | System boundary, future integration candidate | `DEFERRED_WITH_OWNER` |
| TBD-012 | Giữ repository public source-visible nhưng chưa gắn open-source license; có thể đổi private sau | CEO/Project Owner chốt reuse/contribution intent trước external contribution/distribution | Repository governance, D2.1 | `DEFERRED_WITH_OWNER` |
| TBD-013 | Local Docker-first; production target đầu tiên là Linux VPS với Docker Compose; managed providers là alternatives | Đã xác nhận ưu tiên chạy ổn local và chuẩn Docker trước khi đưa lên VPS | Deployment topology, CI/CD, backup/operations | `ACCEPTED` |

### Decision records - Batch D

| ID | Disposition | Decision/reason | Owner hoặc approved by/date | Affected artifacts và due gate |
|---|---|---|---|---|
| TBD-007 | `DEFERRED_WITH_OWNER` | Chưa tích hợp/export MISA trong MVP vì chưa rõ product/edition và accounting payload | Kế toán | MISA discovery; trước accepted integration slice, mặc định M9 |
| TBD-012 | `DEFERRED_WITH_OWNER` | Public source-visible nhưng chưa cấp OSS reuse rights; đây là lựa chọn đảo ngược tốt hơn khi RUBIK có thể chuyển private | CEO/Project Owner | Repository policy; trước external contribution hoặc reusable distribution |
| TBD-013 | `ACCEPTED` | Local Docker-first và VPS Docker Compose giảm multi-provider operations khi MVP chưa cần scale | Quản lý Kho / 2026-08-03 | ADR-0005, deployment/operations; D2 |

`TBD-007` được kiểm soát tại [`../../02-architecture/MISA_INTEGRATION_DISCOVERY.md`](../../02-architecture/MISA_INTEGRATION_DISCOVERY.md). `TBD-013` được khóa bởi [`../../02-architecture/adr/0005-local-docker-vps-target.md`](../../02-architecture/adr/0005-local-docker-vps-target.md). `TBD-012` không tạo file `LICENSE`; public visibility không được mô tả là open source.

## Decision record bắt buộc

Mỗi câu trả lời được chấp nhận phải ghi:

| Field | Nội dung |
|---|---|
| Decision ID | `TBD-xxx` |
| Disposition | `ACCEPTED`, `DEFERRED_WITH_OWNER`, hoặc `REJECTED` |
| Decision | Câu policy ngắn, không mơ hồ |
| Approved by | Cá nhân/role chịu trách nhiệm |
| Decision date | Ngày chấp nhận |
| Reason | Business reason/trade-off |
| Affected artifacts | Rules, state, ADR, schema, test, roadmap |
| Follow-up owner | Người chịu trách nhiệm thực hiện |
| Due gate | D0, D1, D2, M1... |

## Routing sau workshop

| Nhóm quyết định | Artifact phải cập nhật |
|---|---|
| Scope/roles/process | `VISION_AND_SCOPE`, `USERS_AND_ROLES`, `AS_IS/TO_BE` |
| UOM/Lot/date | `BUSINESS_RULES`, `UOM_CONVERSION`, `LOT_TRACEABILITY`, D1/M1/M2 roadmap |
| Order/split/shelf-life | `STATE_MACHINES`, `APPROVAL_MATRIX`, outbound contracts |
| Evidence/retention | Security/Storage/operations documents |
| License/runtime provider | Repository files và deployment ADR |
| Accepted/deferred status | `OPEN_QUESTIONS`, tracker, implementation status |

## Workshop exit criteria

- `TBD-001..014` không còn mục nào chỉ có status `Open` mà không có owner/disposition.
- Các decision tác động business rules được review trong D1.
- Các decision tác động architecture có ADR hoặc explicit accepted proposal.
- D0.5 public/private boundary và license có disposition.
- D0.6 product acceptance có named approver và evidence.

## Bước tiếp theo

Batch A-D đã có disposition cho đủ 14 TBD. [`D0_PRODUCT_ACCEPTANCE.md`](D0_PRODUCT_ACCEPTANCE.md) đã được `Quản lý Kho` chấp nhận ngày 2026-08-03.
