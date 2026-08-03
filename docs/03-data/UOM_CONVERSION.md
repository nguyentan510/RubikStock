# UOM và Packaging Conversion

## Model

Mỗi product xác định:

- một base inventory UOM;
- các UOM được phép dùng cho purchase/sales/count;
- conversion factor chính xác về base UOM;
- có cho phép base quantity dạng lẻ hay không;
- có cho phép mở seal của package hay không;
- effective period/version.

Ví dụ:

```text
Syrup A base UOM = bottle
1 case = 12 bottles

Flour B base UOM = gram
1 sealed bag = 25,000 grams
```

Ví dụ bột mì không tự động cho phép bán một bao đã mở theo gram. Việc đó cần một quy trình repacking, labeling, traceability, và food-safety đã được chấp nhận.

## Quy tắc posting

Một movement phải lưu đồng thời:

```text
entered_quantity + entered_uom
normalized_base_quantity + conversion_version
```

Thay đổi conversion trong tương lai không bao giờ làm đổi nghĩa của movement trong quá khứ.

## Validation

- Factor phải dương và chính xác.
- Đường conversion phải rõ ràng, không mơ hồ.
- Sản phẩm rời/đơn chiếc phải từ chối base quantity dạng lẻ.
- UOM dùng cho sales/purchase phải được bật cho product tại business date.
- Conversion version dùng cho movement đã post là bất biến.

## Quyết định mở

`TBD-002` phải phân loại product thực tế vào nhóm sealed-only, break-case, measured quantity, hoặc repacked SKU trước khi implementation.
