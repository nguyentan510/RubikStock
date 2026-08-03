# M9 Roadmap - Optimization After Evidence

- Status: `DEFERRED`
- Depends on: Production-like/production evidence và measured bottleneck
- Unlocks: Chỉ capability đã chứng minh lợi ích

## Outcome

Cải thiện cost, speed, forecast quality, routing hoặc integration dựa trên baseline và benefit đo được, không làm suy giảm correctness/auditability.

## Work packages

Các work package dưới đây chỉ là candidate; từng mục vẫn cần measured bottleneck trước khi mở.

| ID | Candidate | Điều kiện mở | Required evidence |
|---|---|---|---|
| M9.1 | Query/index optimization | Slow query/SLO bottleneck đã đo | Before/after benchmark |
| M9.2 | Cache/async jobs | Database/latency load chứng minh nhu cầu | Correctness/failure tests |
| M9.3 | Advanced forecast | Baseline M7 ổn định và model có uplift | Out-of-sample WAPE/bias |
| M9.4 | Route optimization | Delivery history đủ chất lượng và cost baseline | Distance/time/cost comparison |
| M9.5 | Accounting integration | Stable contract và owner rõ | Reconciliation/idempotency tests |
| M9.6 | Barcode/mobile/offline hardening | Device/connectivity evidence | Offline/conflict recovery tests |
| M9.7 | Service extraction | Modular monolith có bottleneck ownership/deploy rõ | ADR + failure/ops proof |

## Quy trình mở một optimization slice

1. Ghi baseline và bottleneck.
2. Xác định metric thành công và guardrail correctness.
3. Tạo ADR/experiment plan.
4. Chạy bounded comparison.
5. Chỉ promote khi benefit vượt threshold được chấp nhận.
6. Có rollback về baseline behavior.

## Không được dùng làm lý do

- “Có thể cần scale sau này”.
- “Microservices hiện đại hơn”.
- “ML nghe thông minh hơn baseline”.
- “Dashboard đẹp hơn” nhưng không cải thiện quyết định/vận hành.

## Exit condition

M9 không có một exit gate chung. Mỗi optimization candidate có gate riêng và phải chứng minh tăng lợi ích, giảm risk hoặc tăng reliability.
