# Excel Discovery and Cutover Plan

## Nguyên tắc

Excel data là input để qualify, không phải source of truth được tin ngay lập tức. Không có import nào được phép tự bịa ra nghĩa còn thiếu của Lot, expiry, UOM, customer, hoặc quantity.

## Các giai đoạn

### 1. Kiểm kê và phân loại file

- Xác định owner, mục đích, tần suất cập nhật, và khoảng thời gian của từng workbook.
- Hash và lưu trữ riêng tư source file như input migration bất biến.
- Map sheet/column sang khái niệm chuẩn.

### 2. Profile và normalize

- SKU trùng/thiếu.
- Tên và UOM xung đột.
- Date không hợp lệ hoặc mơ hồ.
- Thiếu supplier lot/MFG/EXP.
- Quantity âm hoặc không giải thích được.
- Order/receipt trùng.
- Alias của customer/supplier.

### 3. Xây mapping table

- Legacy SKU -> product chuẩn.
- Legacy unit -> product UOM/conversion.
- Legacy warehouse text -> location đã mã hóa.
- Legacy customer/supplier -> partner chuẩn.
- Legacy status/reason -> enum/reason code có kiểm soát.

### 4. Dry-run import

Mỗi dòng sẽ là `ACCEPTED`, `REJECTED`, hoặc `QUARANTINED` kèm lý do. Import phải idempotent theo hash file nguồn, sheet, và row/source key.

### 5. Opening count vật lý

- Gắn nhãn zone/location ban đầu.
- Đếm theo product, Lot, expiry, location, và status.
- Lot/date không xác minh được thì vào quarantine.
- So sánh physical count với Excel đã qualify và duyệt chênh lệch.

### 6. Cutover

1. Đóng băng cập nhật vận hành trên hệ thống cũ vào thời điểm đã thống nhất.
2. Lấy export cuối cùng và hash nó.
3. Chạy import đã được validate.
4. Post các `OPENING_BALANCE` operation đã được duyệt.
5. Reconcile tổng và trace mẫu các Lot.
6. Đưa Excel về read-only/archive; tránh dual-entry kéo dài vô hạn.

## Báo cáo import bắt buộc

- Identity/hash của source.
- Số dòng accepted/rejected/quarantined.
- Tổng quantity theo product/UOM.
- Số field thiếu/không hợp lệ.
- Phiên bản mapping.
- Import run ID và actor.
- ID của opening-balance operation.
- Chữ ký sign-off reconciliation.

## Rollback

Trước khi live business transaction bắt đầu, cutover thất bại có thể reset môi trường mới và chạy lại từ input bất biến. Sau khi live transaction bắt đầu, rollback cần một business freeze rõ ràng và controlled recovery; database không được reset một cách tùy tiện.
