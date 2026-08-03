# RubikStock Documentation Map

## Thứ tự đọc

1. [`GOVERNANCE.md`](GOVERNANCE.md)
2. [`00-product/VISION_AND_SCOPE.md`](00-product/VISION_AND_SCOPE.md)
3. [`00-product/GLOSSARY.md`](00-product/GLOSSARY.md)
4. [`01-business/AS_IS_PROCESS.md`](01-business/AS_IS_PROCESS.md)
5. [`01-business/TO_BE_PROCESS.md`](01-business/TO_BE_PROCESS.md)
6. [`01-business/BUSINESS_RULES.md`](01-business/BUSINESS_RULES.md)
7. [`01-business/STATE_MACHINES.md`](01-business/STATE_MACHINES.md)
8. [`03-data/DATA_MODEL.md`](03-data/DATA_MODEL.md)
9. [`02-architecture/DEPLOYMENT_ARCHITECTURE.md`](02-architecture/DEPLOYMENT_ARCHITECTURE.md)
10. [`02-architecture/MISA_INTEGRATION_DISCOVERY.md`](02-architecture/MISA_INTEGRATION_DISCOVERY.md)
11. [`03-data/SHELF_LIFE_POLICY.md`](03-data/SHELF_LIFE_POLICY.md)
12. [`03-data/templates/README.md`](03-data/templates/README.md)
13. [`06-delivery/BUILD_ORDER.md`](06-delivery/BUILD_ORDER.md)
14. [`06-delivery/big-plan/MASTER_PLAN.md`](06-delivery/big-plan/MASTER_PLAN.md)

## Nhóm tài liệu

| Family | Mục đích | Maturity |
|---|---|---|
| `00-product` | Phạm vi product, user, ngôn ngữ, các quyết định chưa chốt | Nền tảng |
| `01-business` | Quy trình hiện tại và mục tiêu, rule, exception, approval | Bản nháp contract |
| `02-architecture` | Ranh giới hệ thống, module, deployment, security, ADR | Thiết kế đề xuất |
| `03-data` | Data model, inventory ledger, UOM, Excel cutover | Contract khái niệm |
| `04-contracts` | API, errors, idempotency, permissions | Dự kiến ở D2 |
| `05-ux` | Sitemap, luồng màn hình, trải nghiệm kho/mobile | Dự kiến ở D2 |
| `06-delivery` | Roadmap, Big Plan theo phase, build order, status, traceability, gates | Điều phối hiện hành |
| `07-testing` | Test strategy và kịch bản nghiệm thu nghiệp vụ | Contract ban đầu |
| `08-operations` | Environments, deployment, backup, secrets, incidents | Bản nháp trước runtime |

## Từ vựng trạng thái

- `PROPOSED`: đã tài liệu hóa, chưa được chấp nhận như product policy.
- `ACCEPTED`: quyết định product/architecture đã được duyệt.
- `IMPLEMENTED`: đã có code và các test mục tiêu pass.
- `RUNTIME_VERIFIED`: đã chạy thành công trong môi trường mục tiêu.
- `PRODUCTION_READY`: đã pass các gate vận hành, recovery, security, và business.
- `TBD`: vẫn cần xác nhận từ user/business.

Việc hoàn tất tài liệu không đồng nghĩa với runtime hoặc production readiness.

Các provider reference của stack đề xuất được tập hợp trong [`02-architecture/REFERENCES.md`](02-architecture/REFERENCES.md).
