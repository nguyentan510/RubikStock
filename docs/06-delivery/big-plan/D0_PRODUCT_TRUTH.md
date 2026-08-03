# D0 Roadmap - Product Truth

- Status: `PROPOSED`
- Depends on: Không có
- Unlocks: D1 business acceptance và domain schema an toàn

## Outcome

RUBIK và nhóm triển khai có cùng một định nghĩa về product boundary, người dùng, quy trình hiện tại, dữ liệu đầu vào và các quyết định còn mở.

## Work packages

| ID | Nội dung | Output bắt buộc | Verification |
|---|---|---|---|
| D0.1 | Scope và non-goals | Vision, phạm vi MVP, accounting boundary | Business owner review |
| D0.2 | Users và operating ownership | Role list, task ownership, named approvers | Role walkthrough |
| D0.3 | Hiện trạng dữ liệu/quy trình | AS-IS, nguồn Excel/Zalo/accounting, data owner | Source inventory được xác nhận |
| D0.4 | Decision register | Owner/due disposition cho `TBD-001..014` | Đã đủ: 12 accepted, 2 deferred có owner |
| D0.5 | Public/private boundary | Public source-visible/no-OSS-license disposition, data classification, repository policy | License review deferred tới khi có reuse/contribution intent |
| D0.6 | Product acceptance | [`D0_PRODUCT_ACCEPTANCE.md`](D0_PRODUCT_ACCEPTANCE.md) | Gate D0 checklist và business acceptance |

Workshop đang hoạt động tại [`D0_DECISION_WORKSHOP.md`](D0_DECISION_WORKSHOP.md).

## Thứ tự triển khai

`D0.1 -> D0.2 -> D0.3 -> D0.4 -> D0.5 -> D0.6`.

D0.3 có thể chạy song song D0.1-D0.2 nhưng không được đưa dữ liệu thật vào public repository.

## Câu hỏi phải đóng hoặc defer rõ ràng

- Số warehouse, SKU, zone và thiết bị thực tế.
- Quy tắc break case/bag và measured quantity.
- Chất lượng supplier Lot/MFG/EXP trong dữ liệu cũ.
- Nguồn sales order, split shipment và accounting integration.
- Customer shelf-life policy và approval thresholds.
- Production hosting, retention và evidence policy.

## Exit gate

- Scope và non-goals được RUBIK chấp nhận.
- Mọi `TBD` có owner và disposition.
- Public/private data boundary được duyệt.
- Không có dữ liệu confidential/secret trong repository.

## Không thuộc D0

Không thiết kế bảng vật lý, code CRUD, import Excel thật hoặc chọn ML model.
