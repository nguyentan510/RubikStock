# Environment Policy

| Environment | Mục đích | Data | Deploy policy |
|---|---|---|---|
| Local | Phát triển và automated tests bằng full-stack Docker Compose | Chỉ dùng fake deterministic seed | PostgreSQL `5433`, API `8000`, web `3000` |
| Staging | Integration, migration rehearsal, UAT trên isolated Compose/VPS target | Chỉ synthetic/sanitized | Workflow có kiểm soát; tách khỏi production |
| Production | Linux VPS Docker Compose vận hành RUBIK thật | Dữ liệu confidential thật | Protected environment và manual approval |

## Quy tắc tách biệt

- Tách riêng Compose project/host, database, auth namespace và storage cho staging/production.
- Tách riêng origin và secret cho frontend/API.
- Production credentials không có trong pull-request workflow.
- Preview deployment không bao giờ kết nối production data.
- Tên environment có thể thấy được; secret value thì không.

## Các lớp configuration

- Public configuration: API base URL, environment label và auth client config đã được review.
- Private runtime configuration: database URL, admin/storage key, signing/cron credentials.
- Business configuration: time zone, shelf-life policy, reason code, approval threshold; versioned/audited trong application data khi phù hợp.
