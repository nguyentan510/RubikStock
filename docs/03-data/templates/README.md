# Clean-start Data Templates

## Phạm vi

Bộ template này thay thế kế hoạch import lịch sử Excel cũ. Đây là contract dữ liệu đầu vào cho discovery/rehearsal; chưa phải database import API đã implemented.

Các file:

- [`product_master.csv`](product_master.csv): product và tracking policy.
- [`uom_conversion.csv`](uom_conversion.csv): conversion về base UOM.
- [`customer_shelf_life_policy.csv`](customer_shelf_life_policy.csv): policy date theo customer/group/category/product.
- [`opening_stock.csv`](opening_stock.csv): physical opening count mới.
- [`receipt_capture.csv`](receipt_capture.csv): receipt mới trong giai đoạn chuyển tiếp.
- [`sales_capture.csv`](sales_capture.csv): sales/fulfillment history mới từ clean-start.

## Quy ước chung

- Encoding: UTF-8.
- Delimiter: comma `,`.
- Date: `YYYY-MM-DD`.
- Timestamp: RFC 3339 có timezone, ví dụ `2026-08-03T09:30:00+07:00`.
- Boolean: `true` hoặc `false`.
- Decimal: dấu chấm, không dùng dấu phân cách hàng nghìn.
- Code: uppercase ASCII với `-`/`_`, không dùng tên hiển thị làm identifier.
- Blank chỉ hợp lệ khi data dictionary cho phép.
- File thật là confidential và không được commit vào public repository. Lưu bản điền thật bên ngoài repo hoặc trong `private-data/`/`templates/filled/` đã được Git ignore.

## Product tracking policy

| Code | Mặc định áp dụng | Required fields |
|---|---|---|
| `LOT_MFG_EXP_REQUIRED` | Kem, dairy, chilled, frozen, short-life | `supplier_lot`, `mfg_date`, `exp_date` |
| `LOT_EXP_REQUIRED` | Bột, syrup, sauce, topping, packaged F&B | `supplier_lot`, `exp_date`; MFG nếu có |
| `NO_DATE_TRACKING` | Non-food packaging/tools | Không bắt buộc Lot/date |

Product chưa phân loại dùng `LOT_EXP_REQUIRED`.

## Template rules

### Product master

- `sku`: stable unique code.
- `base_uom`: unit nhỏ nhất dùng cho inventory truth; measured-sale theo weight dùng `GRAM`.
- `allows_case_break`: cho phép bán sealed unit từ case.
- `allows_measured_sale`: cho phép mở package và bán gram/kg.
- `measurement_uom`: bắt buộc khi `allows_measured_sale=true`.
- `measurement_precision`: step/decimal precision được chấp nhận.

### UOM conversion

`base_quantity_per_input_uom` là số base units trong một input UOM. Ví dụ `1 CASE = 12 BOTTLE` ghi factor `12`; `1 BAG = 25000 GRAM` ghi factor `25000`.

### Opening stock

- Nguồn là physical count mới, không phải copy balance từ Excel cũ.
- `count_batch_ref + location_code + sku + supplier_lot` phải định danh row ổn định cho rehearsal/import.
- F&B thiếu Lot/EXP xác minh được phải dùng `inventory_status=QUARANTINE`.
- `AVAILABLE` chỉ dùng khi product/date/location đã pass policy và count đã được duyệt.

### Customer shelf-life policy

- Scope cụ thể nhất thắng: customer/product -> customer/category -> group -> company default.
- Ít nhất một trong `minimum_remaining_days` hoặc `minimum_remaining_percent` phải có.
- Nếu cả hai có giá trị, allocation candidate phải đạt cả hai.
- Numeric thresholds là business configuration có effective date và approval, không hard-code.

### Receipt capture

- Mỗi `receipt_ref + line_no` là duy nhất.
- UOM phải có conversion hợp lệ cho SKU.
- Missing required Lot/date phải vào controlled status hoặc reject; không tự sinh date.

### Sales capture

- `order_ref + line_no` là duy nhất.
- Sau confirmation, thay đổi quantity/state cần được audit; không sửa file cũ để viết lại history.
- `stockout_flag` và `lost_sale_quantity` giúp M7 không diễn giải sai demand bằng 0.
- Một order có thể xuất hiện ở nhiều shipment/trip trong system; template này capture outcome theo line ở mức khởi đầu, contract shipment chi tiết thuộc M4-M6.

## Import safety

Khi import pipeline được xây ở M1-M2, nó phải có dry-run, row-level errors, idempotency, accepted/rejected/quarantined counts và reconciliation totals. Không được dùng CSV để update balance trực tiếp.
