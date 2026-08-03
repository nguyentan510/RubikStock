# Test Strategy

## Các tầng test

| Tầng | Trọng tâm |
|---|---|
| Domain unit | FEFO, eligibility, conversion, state transition, planning formula |
| Database invariant | Constraints, ledger/projection, transactions, concurrency, idempotency |
| API contract | Authentication, authorization, validation, hành vi error/idempotency |
| Integration | Ranh giới Supabase Postgres/Auth/Storage và scheduled jobs |
| Workflow | Receipt-to-putaway, order-to-shipment, return-to-disposition, trip reconciliation |
| Migration | Clean rebuild, upgrade, rollback/forward recovery, Excel import idempotency |
| Security | Role matrix, cross-tenant/object access, secret/log exposure, file upload |
| UAT | Tình huống thật của RUBIK dùng định danh sanitized/fake |
| Operational | Backup restore, alert delivery, reconciliation, incident response |

## Các tính chất bắt buộc

- Không có negative inventory đã được xác nhận.
- Không có duplicate movement từ việc command/job được gửi lặp lại.
- Transfer và reversal phải bảo toàn quantity.
- Blocked stock không được allocate.
- Reservation phải ngăn oversell đồng thời.
- Return không được trở thành available nếu chưa inspection/disposition.
- Command có đặc quyền không được vượt qua authorization hoặc audit.
- Forecast result phải reproduce được từ input/version đã lưu.

## Test data

- Dùng seed fixture mang tính quyết định với partner và product giả.
- Tách riêng conversion case/bottle và bag/weight.
- Bao gồm nhiều Lot, expiry bằng nhau, nhiều location, partial stock, blocked status, và concurrent orders.
- Cấm dùng dữ liệu customer/supplier thật trong fixture của repository.

## Evidence

CI output, migration history, test report, UAT sign-off, và bản ghi thực hành vận hành phải được liên kết từ implementation status trước khi nâng maturity.
