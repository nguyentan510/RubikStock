# Monitoring và Reconciliation

Monitoring tồn tại để phát hiện state cũ, không an toàn, bị hỏng, hoặc chưa rõ.

## Tín hiệu critical

- Ledger/projection mismatch.
- Negative balance hoặc reservation lớn hơn eligible stock.
- Stock operation thất bại/trùng lặp.
- Shipment/reservation mismatch.
- Delivery trip đóng trong khi return chưa reconcile.
- Return/destruction chờ xử lý vượt ngưỡng.
- Stock expired/recalled nhưng vẫn còn eligible hoặc đã allocate.
- Scheduled planning/alert job bị miss, fail, hoặc chồng lặp.
- Bất thường authentication/authorization và tăng đột biến privileged action.
- Database/storage/backup lỗi.

## Tín hiệu nghiệp vụ

- Inventory accuracy.
- Tần suất stockout và lost sale.
- Quantity/value gần hết hạn và expiry destruction.
- Order fill rate và partial delivery.
- Tỷ lệ return/damage theo product/supplier/reason.
- Tuổi tồn kho và days of cover.
- Forecast WAPE/bias sau khi qualify.

## Yêu cầu cho alert

Mọi critical alert phải có owner, severity, evaluation interval, threshold, response runbook, deduplication key, và tested delivery path. Một dashboard không có alert path gắn với người chịu trách nhiệm thì chưa phải operational readiness.
