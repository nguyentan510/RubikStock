# Users and Roles

## Mô hình role

| Role | Trách nhiệm chính | Không được tự làm một mình |
|---|---|---|
| Sales | Tạo/xác nhận nhu cầu khách và yêu cầu shelf-life | Điều chỉnh stock hoặc duyệt destruction |
| Purchasing | Theo dõi supplier lead time và duyệt kế hoạch mua | Ghi nhận hàng chưa nhận thành available |
| Receiving | Ghi receipt, Lot, date, và discrepancy | Tự duyệt ngoại lệ supplier khi cần tách vai trò |
| Warehouse operator | Put-away, transfer, pick, stage, load, count | Sửa balance trực tiếp hoặc duyệt adjustment của chính mình |
| QC/authorized inspector | Release, quarantine, reject, và disposition stock | Xóa lịch sử inspection |
| Delivery coordinator | Lập trip, phân xe/tài xế, xác nhận loading | Sửa Lot đã pick mà không qua warehouse reversal |
| Driver | Xem trip được giao, ghi kết quả delivery và hàng trả | Sửa inventory hoặc quantity order trực tiếp |
| Warehouse manager | Duyệt exception, adjustment, FEFO override, destruction | Bỏ qua yêu cầu audit |
| System administrator | Quản lý identity, role assignment, configuration | Tự động thực hiện approval nghiệp vụ thường nhật |
| Auditor/read-only | Xem movement, approval, và traceability | Sửa dữ liệu nghiệp vụ |

## Mức tối thiểu của separation-of-duty

- Stock adjustment: người tạo và người duyệt nên khác nhau nếu vượt ngưỡng cấu hình.
- Destruction: requester và approver phải khác nhau.
- FEFO override: operator phải nêu lý do; cần manager approval theo policy.
- Return to available: bắt buộc inspection; người nhận không được tự release stock âm thầm.
- Thay đổi role: phải ghi trong security audit log.

## Giả định về authentication

- Chỉ dùng account cá nhân có tên; không dùng shared warehouse login cho hành động có trách nhiệm.
- Driver chỉ được truy cập trip đã phân công và dữ liệu delivery liên quan.
- Role đặc quyền cần policy authentication mạnh hơn, sẽ được định nghĩa trong D2 security design.

## D0 decision authority

`Quản lý Kho` là role chấp nhận các quyết định D0 operating-shape trong workshop hiện tại. Việc này không tự cấp quyền self-approve adjustment/destruction hoặc bỏ qua separation-of-duty trong runtime.
