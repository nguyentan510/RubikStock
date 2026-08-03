# Vision and Scope

## Trạng thái

`PROPOSED` - dựa trên buổi discovery; các mục được đánh dấu `TBD` cần business xác nhận.

## Vision

RubikStock cung cấp một operational truth có thể audit cho hoạt động phân phối nguyên liệu làm bánh và pha chế của RUBIK COMPANY:

```text
Nhập từ nhà cung cấp -> Tồn kho theo Lot/location -> Phân bổ B2B -> Picking trong kho
-> Giao hàng của công ty -> Return/disposition -> Replenishment planning
```

## Bối cảnh kinh doanh

- RUBIK COMPANY phân phối nguyên liệu làm bánh và pha chế.
- Khách hàng là đại lý B2B, shop, và xưởng sản xuất.
- Số lượng đơn ít, nhưng mỗi đơn có thể rất lớn.
- RUBIK tự vận hành đội xe và tài xế giao hàng.
- Vận hành hiện tại phụ thuộc nhiều vào Excel và phối hợp thủ công.
- Kho hiện chưa có hệ thống mã khu/vị trí chính thức.
- Các vấn đề lặp lại gồm hàng lỗi, hết hàng, trả hàng, hết hạn, và hủy.
- Bộ phận mua hàng cần replenishment planning, seasonality, và lịch âm.

## Kết quả mong muốn của product

1. Biết được số lượng dùng được của từng SKU theo Lot, location, và status.
2. Ngăn overselling và giao hàng không an toàn.
3. Phân bổ hàng có hạn sử dụng bằng FEFO và chính sách shelf-life của khách hàng.
4. Trace một Lot ngược về lần nhập và xuôi tới khách đã giao.
5. Kiểm soát hàng lỗi, trả hàng, điều chỉnh, và hủy bằng approval và evidence.
6. Điều phối picking, staging, loading, delivery, và proof of delivery.
7. Tạo purchase recommendation có thể giải thích bằng lịch sử đã được qualify.

## Phạm vi MVP

### Bao gồm

- Master data cho product, category, supplier, customer, UOM, và packaging.
- Warehouse zones và locations.
- Lot, manufacture date, expiry date, và inventory status.
- Inventory movement bất biến và balance suy ra từ đó.
- Purchase receipt, QC, và put-away.
- Sales order, reservation, FEFO allocation, picking, staging, và shipping.
- Giao hàng bằng vehicle/driver của công ty và proof of delivery.
- Return, quarantine, inspection, disposition, damage, và destruction.
- Cycle count và stock adjustment đã được duyệt.
- Cảnh báo expiry, low-stock, và exception.
- Replenishment recommendation quyết định tất định và calendar sự kiện mùa vụ.
- Authorization theo role và audit trail.

### Ngoài MVP một cách rõ ràng

- General ledger, invoicing, tax, accounts receivable/payable, hoặc payroll.
- Tự động mua hàng không có human approval.
- Machine-learning forecast trước khi data được qualify.
- Multi-company ERP.
- Marketplace/e-commerce storefront.
- Tối ưu route xe nâng cao.
- Microservices hoặc distributed event infrastructure.

## Chỉ số thành công

Mọi mục tiêu số cần baseline trước khi chốt ngưỡng.

| Chỉ số | Định nghĩa | Mục tiêu |
|---|---|---|
| Inventory accuracy | Số lượng trên system so với physical count đã duyệt | `TBD` |
| Lot traceability | Có thể trace từ receipt đến customer cho một Lot đã chọn | 100% sau cutover |
| Negative inventory | Số dư stock xác nhận nhỏ hơn 0 | 0 |
| Unauthorized override | FEFO/adjustment/destruction không có approval bắt buộc | 0 |
| Order fill rate | Nhu cầu đã xác nhận được đáp ứng đúng hạn | `TBD` |
| Expiry write-off | Giá trị/số lượng phải hủy do hết hạn | Lấy baseline rồi giảm |
| Forecast WAPE and bias | Sai số theo SKU/tuần và planning group | Lấy baseline sau khi có history đạt chuẩn |

## Ranh giới product

RubikStock là operational source of truth cho stock và fulfillment. Hệ thống accounting vẫn là financial source of truth cho đến khi một project integration riêng được chấp nhận.
