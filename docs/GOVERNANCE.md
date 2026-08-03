# Documentation Governance

## Ngôn ngữ chuẩn

- Business policy và operating procedures: tiếng Việt.
- Table, field, state, event, và API identifiers: tiếng Anh.
- UI labels có thể là tiếng Việt nhưng vẫn phải giữ stable English identifiers ở bên trong.

## Nguồn sự thật

| Chủ đề | Nguồn chuẩn |
|---|---|
| Product boundary | `00-product/VISION_AND_SCOPE.md` |
| Domain terminology | `00-product/GLOSSARY.md` |
| Business invariants | `01-business/BUSINESS_RULES.md` cộng với automated tests |
| Workflow states | `01-business/STATE_MACHINES.md` cộng với domain code |
| Database schema | Các migration file khi implementation bắt đầu |
| Conceptual data design | `03-data/DATA_MODEL.md` |
| API contract | FastAPI OpenAPI được sinh ra khi implementation bắt đầu |
| Permission policy | Tài liệu approval/permission cộng với authorization tests |
| Delivery order | `06-delivery/BUILD_ORDER.md` |
| Detailed phase execution | `06-delivery/big-plan/MASTER_PLAN.md` và roadmap của phase tương ứng |
| Actual maturity | `06-delivery/IMPLEMENTATION_STATUS.md` |
| Deployment behavior | CI/CD workflow cộng với operations runbook |
| Secrets | Hosting secret manager; không bao giờ là documentation hay Git |

## Cách xử lý xung đột

Khi các nguồn mâu thuẫn nhau, ưu tiên theo thứ tự sau:

1. Business rule hoặc ADR đã được chấp nhận.
2. Database/API contract và automated tests.
3. Verified runtime behavior.
4. Tài liệu chung.

Không được để hành vi code phát sinh ngẫu nhiên tự định nghĩa lại policy về inventory, approval, hay traceability.

## Quy trình thay đổi

Mọi thay đổi ảnh hưởng đến nghĩa của inventory, traceability của Lot, reservation, approval, security, persisted data, hoặc public API đều phải có:

1. Business rule hoặc ADR đã cập nhật.
2. Đánh giá tác động compatibility và migration.
3. Targeted tests.
4. Cập nhật traceability.
5. Kế hoạch rollback hoặc reversal.
6. Evidence trước khi nâng status.

## Phân loại dữ liệu

| Loại | Ví dụ | Public repository |
|---|---|---|
| Public | Kiến trúc chung, ví dụ giả, API shapes | Được phép |
| Internal | Quy trình kho, ánh xạ role nội bộ | Nên để ở private operations repository |
| Confidential | Khách hàng, supplier, giá, sales history, warehouse maps | Cấm |
| Secret | Password, database URL, secret key, signing material | Cấm; chỉ dùng secret manager |
