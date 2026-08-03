# Non-goals và Complexity Guardrails

## Non-goals của MVP

- Thay thế hệ thống accounting, tax, invoicing, hoặc receivables.
- Mua hàng trực tiếp không qua approval.
- Quyết định do AI tạo ra nhưng không thể giải thích hoặc audit.
- Tối ưu route giao hàng trước khi độ chính xác trip và POD cơ bản được chứng minh.
- Hỗ trợ mọi packaging model có thể có trước khi catalog ví dụ thật của RUBIK được lập xong.
- Xây microservices, Kafka, distributed caches, hoặc feature store.
- Coi giao diện dashboard đẹp như bằng chứng của correctness vận hành.

## Điều kiện để xem xét đưa vào scope

Một non-goal chỉ có thể vào scope khi:

1. Có bài toán kinh doanh đã đo được.
2. Thiết kế modular hiện tại không thể giải quyết an toàn.
3. Ownership và hành vi khi lỗi đã được định nghĩa.
4. Có kế hoạch data, migration, test, và rollback.
