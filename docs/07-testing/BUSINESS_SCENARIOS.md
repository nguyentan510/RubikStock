# Business Acceptance Scenarios

- Status: Core scenario index; detailed D1 Batch A-E scenarios đã accepted và được quản lý tại [`../06-delivery/big-plan/D1_BUSINESS_ACCEPTANCE.md`](../06-delivery/big-plan/D1_BUSINESS_ACCEPTANCE.md).

| ID | Kịch bản | Kết quả mong đợi |
|---|---|---|
| SCN-001 | Nhận 10 case, 12 bottle/case | Hệ thống lưu đúng 10 case đã nhập và chính xác 120 base bottle với Lot/location/status |
| SCN-002 | Thiếu EXP bắt buộc | Quantity của receipt vẫn ở quarantine/unavailable |
| SCN-003 | Hai user cùng reserve 100 unit cuối cùng | Tổng reservation thành công tối đa là 100; không có available âm |
| SCN-004 | Lot đủ điều kiện cũ nhất còn 4, Lot kế còn 6 cho demand 10 | Allocation tạo hai dòng Lot 4+6 |
| SCN-005 | Lot có expiry sớm nhất vi phạm shelf-life của khách | Loại bỏ Lot đó, rồi FEFO trong các Lot còn đủ điều kiện |
| SCN-006 | Operator chọn thủ công Lot mới hơn | Yêu cầu permission/reason/approval và giữ lại suggested versus actual allocation |
| SCN-007 | Lot đã allocate bị recall trước khi pick | Pick/shipment bị chặn và phải realloc có kiểm soát |
| SCN-008 | Khách trả hàng đã giao | Nhập vào return quarantine; available không tăng |
| SCN-009 | Return qua inspection | Chuyển status/restock movement đã duyệt làm available tăng đúng một lần |
| SCN-010 | Lot bị hỏng và hết hạn được destroy | Cần approval độc lập và một destruction movement/evidence record |
| SCN-011 | Delivery chỉ giao một phần | Quantity đã giao đóng đúng cách; quantity mang về được reconcile qua return location |
| SCN-012 | Cùng một shipment request được retry sau timeout | Cùng idempotency key trả lại kết quả gốc; không phát sinh duplicate stock-out |
| SCN-013 | Count thấp hơn system | Recount/approval rồi post adjustment movement; ledger trước đó vẫn nguyên vẹn |
| SCN-014 | Sự kiện Trung thu đổi sang ngày dương lịch năm sau | Event window theo từng năm làm thay đổi input forecast một cách tái tạo được |
| SCN-015 | Doanh số bằng 0 trong giai đoạn stockout đã biết | Planning phải gắn cờ censored demand thay vì coi đó là demand bằng 0 |
| SCN-016 | Trace một Supplier lot | Kết quả phải liệt kê receipt, current stock, reservations, shipments/customers, returns, destruction, và reconciliation |

Các scenario sanitized cụ thể hơn sẽ trở thành automated tests/rehearsal ở phase implementation; business acceptance không được báo cáo là test runtime pass.
