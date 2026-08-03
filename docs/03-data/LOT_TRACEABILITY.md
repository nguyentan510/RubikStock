# Lot Traceability

## Các đường trace bắt buộc

Backward trace:

```text
Customer complaint / returned unit
-> shipment line
-> picked allocation
-> lot and supplier lot
-> receipt line
-> purchase order and supplier
```

Forward trace:

```text
Supplier notice / selected lot
-> tất cả location và status hiện tại
-> reservations và open picks
-> shipments và customers
-> returns, destruction, và quantity còn lại
```

## Rule

- Không bao giờ gộp Lot chỉ vì product và expiry giống nhau.
- Các location tách riêng vẫn giữ cùng một Lot identity.
- Repacking/transformation tạo một link genealogy có kiểm soát khi cần một internal traceability unit mới.
- Block/recall trên Lot ảnh hưởng đến toàn bộ stock segment và mọi allocation mới.
- Trace query phải bao gồm reconciliation quantity: received, shipped, returned, destroyed, adjusted, và remaining.

## Kịch bản nghiệm thu

Với một Supplier lot được chọn, user có thẩm quyền phải có thể tạo ra trong một kết quả trace duy nhất:

1. Tham chiếu supplier và receipt.
2. Quantity hiện tại theo location/status.
3. Reservations/allocations đang mở.
4. Mọi shipment/customer đã nhận Lot đó.
5. Lịch sử return/destruction/adjustment.
6. Mọi chênh lệch quantity chưa giải quyết.
