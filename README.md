# RubikStock

RubikStock là hệ thống quản lý tồn kho, xử lý đơn B2B, điều phối giao hàng của công ty, và lập kế hoạch replenishment cho RUBIK COMPANY, đơn vị phân phối nguyên liệu làm bánh và pha chế.

Dự án đi theo một nguyên tắc vận hành:

```text
Tồn kho đúng trước -> Vận hành có kiểm soát -> Kế hoạch giải thích được -> Tối ưu sau
```

## Trạng thái hiện tại

- Giai đoạn: D2 technical foundation in progress
- Runtime implementation: API/web skeleton, migrations, local setup, và CI scaffold đã được tạo
- Production readiness: Chưa đánh giá
- Trạng thái chuẩn: [`docs/06-delivery/IMPLEMENTATION_STATUS.md`](docs/06-delivery/IMPLEMENTATION_STATUS.md)

## Điểm vào tài liệu

- [`docs/README.md`](docs/README.md) - bản đồ tài liệu
- [`docs/GOVERNANCE.md`](docs/GOVERNANCE.md) - nguồn sự thật và chính sách thay đổi
- [`docs/00-product/VISION_AND_SCOPE.md`](docs/00-product/VISION_AND_SCOPE.md) - mục tiêu product và ranh giới MVP
- [`docs/01-business/TO_BE_PROCESS.md`](docs/01-business/TO_BE_PROCESS.md) - quy trình vận hành mục tiêu
- [`docs/01-business/BUSINESS_RULES.md`](docs/01-business/BUSINESS_RULES.md) - các quy tắc domain bắt buộc
- [`docs/03-data/DATA_MODEL.md`](docs/03-data/DATA_MODEL.md) - conceptual data model
- [`docs/06-delivery/BUILD_ORDER.md`](docs/06-delivery/BUILD_ORDER.md) - thứ tự triển khai an toàn theo dependency
- [`docs/06-delivery/big-plan/MASTER_PLAN.md`](docs/06-delivery/big-plan/MASTER_PLAN.md) - kế hoạch tổng và roadmap chi tiết theo từng phase

## Local commands

- `npm run setup` - cài API/web dependencies, copy `.env` nếu cần, khởi tạo local PostgreSQL tại `localhost:5433`, và chạy Alembic baseline upgrade.
- `npm run dev` - khởi chạy API và web dev servers sau khi setup local xong.
- `npm run check` - chạy docs validation, API tests, migration upgrade, và web lint/typecheck/build.
- `npm run smoke:api` - chạy HTTP readiness smoke tạm thời qua API và local PostgreSQL.
- `npm run stack:up` - build và chạy PostgreSQL + one-off Alembic migration + FastAPI + Next.js bằng Docker Compose.
- `npm run smoke:stack` - build/start full stack, kiểm tra API readiness và web HTTP; success marker `RUBIKSTOCK_STACK_SMOKE_OK`.
- `npm run stack:down` - dừng full stack nhưng không xóa PostgreSQL volume.

## Chính sách repository

Source repository hiện theo policy public source-visible, nhưng operational data là private. Tuyệt đối không commit dữ liệu khách hàng, nhà cung cấp, giá, credential, production export, proof giao hàng, dữ liệu an ninh kho, hoặc dữ liệu incident.

Repository chưa có open-source license và không được mô tả là open source. Public visibility không tự cấp quyền tái sử dụng; license sẽ được review trước external contribution/distribution, và repository có thể chuyển private sau. Xem [`docs/00-product/OPEN_QUESTIONS.md`](docs/00-product/OPEN_QUESTIONS.md).
