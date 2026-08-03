# Exception Matrix

| ID | Tình huống | Hành vi ngay lập tức của hệ thống | Cách xử lý | Evidence bắt buộc |
|---|---|---|---|---|
| EX-001 | Quantity receipt khác PO | Ghi quantity thực tế; không bịa quantity dự kiến | Chấp nhận variance, chờ phần còn lại, hoặc claim với supplier | Receipt discrepancy và actor |
| EX-002 | Thiếu Lot/EXP bắt buộc | Đưa vào quarantine; không available | Xác minh nhãn/chứng từ hoặc reject | Ảnh/chứng từ và inspector |
| EX-003 | Gửi receipt trùng | Từ chối duplicate theo idempotency | Trả lại kết quả gốc | Request key và reference gốc |
| EX-004 | Nhiều order đồng thời vượt available | Chỉ request thắng atomic mới reserve; request sau bị thiếu | Partial/backorder/reject | Quyết định reservation |
| EX-005 | Lot đã allocate bị block/expired | Chặn pick/shipment và vô hiệu allocation đủ điều kiện | Reallocate hoặc escalate | Allocation cũ/mới và lý do |
| EX-006 | Short pick tại location | Không tự đổi balance bằng suy đoán | Recount, relocate, reallocate, hoặc workflow adjustment | Scan/count evidence |
| EX-007 | Scan nhầm Lot | Từ chối xác nhận | Pick đúng Lot hoặc realloc đã được duyệt | Sự kiện scan |
| EX-008 | Khách đòi date mới hơn | Áp dụng shelf-life filter; FEFO trong tập đủ điều kiện | Controlled override nếu vẫn cần | Yêu cầu khách và approval |
| EX-009 | Xe rời kho khi loading còn variance | Chặn xác nhận departure | Sửa record loading/shipment | Xác nhận của loader/coordinator |
| EX-010 | Giao một phần | Tách quantity đã giao và quantity trả về | Return quarantine và reconcile | POD/lý do của driver |
| EX-011 | Giao thất bại | Hàng vẫn nằm trong custody của shipment, chưa available | Return và reconcile vào location được kiểm soát | Lý do thất bại và return receipt |
| EX-012 | Customer return không trace được Lot | Quarantine và fail closed | Điều tra; destroy/hoặc disposition khác đã duyệt | Evidence customer/order |
| EX-013 | Phát hiện hàng hư/hết hạn | Move/block quantity bị ảnh hưởng | Inspect và duyệt disposition | Lot, location, ảnh/lý do |
| EX-014 | Physical count lệch | Ghi variance mà không ghi đè lịch sử | Recount rồi post adjustment đã duyệt | Count sheet và approval |
| EX-015 | Scheduled job chạy hai lần | Duplicate có idempotency sẽ không tạo hiệu ứng kinh doanh trùng | Dùng lại run identity/result | Job run ID |
| EX-016 | Forecast input chưa đủ | Đánh dấu recommendation là low-confidence/blocked | Qualify data hoặc dùng manual plan đã duyệt | Báo cáo input thiếu |
| EX-017 | API timeout sau stock command | Xem outcome là unknown; không retry mù bằng key mới | Tra theo idempotency key/reconcile | Trace request và response |
