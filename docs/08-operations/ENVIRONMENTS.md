# Environment Policy

| Environment | Mục đích | Data | Deploy policy |
|---|---|---|---|
| Local | Phát triển và automated tests | Chỉ dùng fake deterministic seed | Do developer kiểm soát |
| Staging | Integration, rehearsal migration, UAT | Chỉ synthetic/sanitized | Tự động sau main hoặc workflow có kiểm soát |
| Production | Vận hành RUBIK thật | Dữ liệu confidential thật | Environment được bảo vệ và cần manual approval |

## Quy tắc tách biệt

- Tách riêng Supabase project/database, auth, và storage cho staging/production.
- Tách riêng origin và secret cho frontend/API.
- Production credentials không có trong pull-request workflow.
- Preview deployment không bao giờ kết nối production data.
- Tên environment có thể thấy được; secret value thì không.

## Các lớp configuration

- Public configuration: API base URL, environment label, publishable key khi thiết kế RLS đã được chấp nhận.
- Private runtime configuration: database URL, secret key, signing/cron credentials.
- Business configuration: time zone, shelf-life policy, reason code, approval threshold; versioned/audited trong application data khi phù hợp.
