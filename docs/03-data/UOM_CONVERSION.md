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

RUBIK đã chấp nhận bán một số product từ bao đã mở theo gram/kg. Behavior này chỉ bật theo product policy và bắt buộc quy trình package-open/repacking có genealogy tới Lot gốc.

## Product packaging policy

- `allows_case_break`: cho phép xé case để bán unit/chai/gói nguyên seal.
- `allows_measured_sale`: cho phép mở package và bán quantity đo theo gram/kg.
- `measurement_uom`: UOM đo; product theo weight mặc định dùng `gram` làm base UOM.
- `measurement_precision`: số chữ số thập phân/step được chấp nhận theo thiết bị cân và policy.

Khi một sealed package được mở/repack, system phải ghi original Lot/package, quantity trước/sau, actor/time/location và internal traceability unit nếu cần. Không được tạo manufacturer Lot mới.

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

## Accepted D0 decision

`TBD-002` đã accepted: từng product được phân loại `sealed-only`, `break-case` hoặc `measured-sale/repacked`. Giá trị cụ thể của khoảng 300 SKU sẽ được khai báo qua master-data template ở M1.
