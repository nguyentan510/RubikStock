# Current-state Process (`AS-IS`)

## Cơ sở evidence

Tài liệu này ghi lại các phát biểu discovery do RUBIK cung cấp. Nó chưa phải là quan sát kho theo thời gian thực hay đánh giá Excel đã audit.

## Bức tranh vận hành hiện tại

```text
Trao đổi supplier/customer
        -> Nhập Excel thủ công
        -> Dựa vào kinh nghiệm nhân sự và thói quen kho
        -> Nhận hàng/lấy hàng/giao hàng vật lý
        -> Sửa và theo dõi thủ công
```

## Đặc điểm đã biết

- Đơn B2B ít nhưng mỗi đơn có thể rất lớn.
- Bố trí kho dựa vào kinh nghiệm/thói quen, chưa có mã khu/tầng/ô chính thức.
- Stock và planning đang được quản lý thủ công bằng Excel.
- RUBIK có hoạt động giao hàng riêng.
- Bộ phận mua hàng lập kế hoạch cho mặt hàng gần hết và cần bối cảnh chu kỳ bán hàng/mùa vụ.
- Lịch âm và mùa Trung thu ảnh hưởng thời điểm demand.
- Hàng lỗi, hết hàng, trả hàng, hết hạn, và hủy là các vấn đề vận hành đau đầu.

## Các vùng rủi ro quan sát được

| Vùng | Rủi ro hiện tại |
|---|---|
| Inventory truth | Số dư trên bảng tính có thể không phân biệt available, reserved, quarantined, hoặc damaged stock |
| Lot/expiry | Việc chọn Lot và xử lý hàng gần hết hạn phụ thuộc vào kiến thức thủ công |
| Location | Tìm và đếm hàng phụ thuộc vào trí nhớ từng cá nhân |
| Phân bổ đơn lớn | Một đơn có thể tiêu thụ phần lớn stock và tạo xung đột với cam kết khác |
| Returns | Hàng trả về có thể khó trace và tách riêng một cách nhất quán |
| Destruction | Quantity, reason, approval, và evidence có thể không tạo thành một audit trail hoàn chỉnh |
| Delivery | Quantity đã giao, bị từ chối, và mang về có thể phải reconcile thủ công |
| Purchasing | Quyết định replenishment có thể pha trộn trực giác, stock chưa đủ, và history chưa qualify |
| Continuity | Kiến thức vận hành quan trọng tập trung vào một vài cá nhân |

## Evidence cần thu thập

Trước khi chốt workflow, cần thu thập:

1. Mẫu Excel hiện tại và định nghĩa field.
2. Mười receipt mẫu và mười order B2B mẫu.
3. Ví dụ về hàng lỗi, return, destruction, và delivery thất bại.
4. Khảo sát kho thực tế và ràng buộc lưu trữ.
5. Yêu cầu shelf-life hiện tại của khách hàng.
6. Ví dụ lead time, MOQ, và case-pack từ supplier.
7. Lịch sử bán hàng hiện tại và các giai đoạn stockout đã biết.

File nghiệp vụ thật phải được lưu riêng tư và tuyệt đối không commit vào public repository.
