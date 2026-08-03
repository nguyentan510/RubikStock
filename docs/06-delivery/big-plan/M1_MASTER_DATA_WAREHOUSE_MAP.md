# M1 Roadmap - Master Data and Warehouse Map

- Status: `PLANNED`
- Depends on: D0-D2 gates phù hợp
- Unlocks: M2 inventory truth

## Outcome

Product, UOM, partner và physical warehouse map đủ chính xác để mọi quantity sau này có product/location/UOM hợp lệ.

## Work packages

| ID | Nội dung | Deliverables | Verification |
|---|---|---|---|
| M1.1 | Private data profiling | SKU/UOM/location quality report, duplicate/missing mapping | Sanitized profiling summary |
| M1.2 | Catalog core | Category, product, SKU, storage condition, active status | CRUD + uniqueness tests |
| M1.3 | UOM/conversion | Base UOM, product conversion version, effective date, break policy | `UOM-001..004` tests |
| M1.4 | Warehouse map | Warehouse, zone, rack, level, bin, capability/status | Location hierarchy tests |
| M1.5 | Partners/policies | Supplier, customer, customer shelf-life policy | Policy validation tests |
| M1.6 | Import pipeline | Validate/preview/import/reject report, idempotency | Representative fixture import |
| M1.7 | Operator UI | Search/filter/edit with authorization and audit | Workflow tests |
| M1.8 | Physical labeling pilot | Location code convention và pilot labels | Walkthrough tại một zone |
| M1.9 | M1 gate | Reconciliation report và sign-off | Gate M1 evidence |

## Thứ tự triển khai

`M1.1 -> M1.2 -> M1.3 -> M1.4 -> M1.5 -> M1.6 -> M1.7 -> M1.8 -> M1.9`.

Catalog/UOM và warehouse map có thể phát triển song song sau khi naming/identifier policy được chốt.

## Data migration rule

- Dữ liệu thật chỉ xử lý trong private environment.
- Mọi row lỗi phải có reason code; không silent correction.
- Import phải có dry-run/preview và idempotency key.
- Conversion mơ hồ phải reject hoặc quarantine, không tự suy đoán.

## Exit gate

- SKU/UOM/location representative import không còn ambiguity.
- Mọi product có base UOM và storage policy cần thiết.
- Location hierarchy dùng được tại pilot zone.
- Authorization/audit cho master-data changes pass.

## Không thuộc M1

Không ghi opening stock, không tạo inventory balance và không nhập receipt nghiệp vụ.
