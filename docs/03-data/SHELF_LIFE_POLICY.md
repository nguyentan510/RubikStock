# Customer Shelf-life Policy

## Trạng thái

`D0 ACCEPTED` cho policy shape. Numeric thresholds là versioned business configuration được nhập ở M1, không hard-code trong source code.

## Phạm vi

Đại lý và cửa hàng thường yêu cầu date xa vì họ tiếp tục lưu/bán hàng. Eligibility phải được đánh giá trước FEFO để một Lot gần EXP không được gợi ý cho khách không chấp nhận.

## Policy resolution

Ưu tiên policy cụ thể nhất đang có hiệu lực:

```text
customer + product
-> customer + category
-> customer group + product/category
-> company default
```

Policy có các field:

- `minimum_remaining_days`.
- `minimum_remaining_percent`.
- `effective_from` và `effective_to`.
- customer/customer-group và optional category/product scope.
- approval/audit metadata.

Khi policy active, ít nhất một threshold phải có. Nếu cả days và percent cùng có, Lot phải đạt cả hai.

## Calculation contract

Tại `planned_delivery_date`:

```text
remaining_days = exp_date - planned_delivery_date
total_life_days = exp_date - mfg_date
remaining_percent = remaining_days / total_life_days * 100
```

- Date dùng calendar day theo business timezone.
- Percent chỉ tính khi có MFG và EXP hợp lệ và `total_life_days > 0`.
- Thiếu field cần cho active policy thì candidate fail closed.
- Candidate expired, blocked hoặc quality-ineligible luôn bị loại trước FEFO.
- Sau eligibility filter, FEFO sắp xếp EXP gần nhất trước.

## Override boundary

Warehouse Manager có thể approve chọn Lot mới hơn trong tập eligible vì yêu cầu khách/chính sách công ty. Override không thể biến blocked, expired hoặc shelf-life-ineligible stock thành eligible. Original suggestion, selected Lot, reason và approver phải được audit.

## Required tests

- Days-only, percent-only và both/AND.
- Boundary đúng bằng threshold.
- Missing MFG với percent policy.
- Customer override so với group/company default.
- Planned delivery date khác current date.
- FEFO override vẫn không bypass eligibility.
