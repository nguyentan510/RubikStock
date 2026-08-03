# Backup và Restore

## Mục tiêu

Khôi phục cả business data lẫn liên kết evidence về một điểm nhất quán nội bộ. Backup đã cấu hình nhưng chưa từng test restore thì không được xem là evidence của recovery.

## Phạm vi

- PostgreSQL schema và data.
- Đối tượng evidence của private object storage và liên kết metadata.
- Phiên bản deployment/migration.
- Danh mục cấu hình môi trường nhưng không lộ secret value.

## Quyết định policy còn cần

- Recovery Point Objective (`RPO`).
- Recovery Time Objective (`RTO`).
- Thời gian retention.
- Yêu cầu export off-site/logical.
- Chiến lược backup cho storage object.

## Bài test restore

1. Chọn một backup/recovery point đã biết.
2. Restore vào môi trường cô lập.
3. Áp dụng/xác minh đúng application và migration version.
4. Chạy reconciliation ledger/projection.
5. Trace một số Lot mẫu từ receipt đến stock/customer.
6. Xác minh liên kết và quyền truy cập của evidence object.
7. Ghi lại thời gian thực hiện, data gap, lỗi, và cách khắc phục.

Production readiness đòi hỏi một bài test thành công, không chỉ là trạng thái backup của nhà cung cấp.

Với VPS target, database volume hoặc object-storage volume trên cùng VPS không được tính là off-site backup. D2/M8 phải chứng minh encrypted copy sang failure domain khác và restore vào environment cô lập.
