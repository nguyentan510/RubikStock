# ADR-0005: Local Docker-first và VPS Deployment Target

- Status: `ACCEPTED`
- Date: 2026-08-03
- Decision ID: `TBD-013`
- Approved by: `Quản lý Kho`
- Supersedes: deployment provider proposal trong [`0004-deployment-stack.md`](0004-deployment-stack.md)

## Context

RUBIK cần stack chạy ổn định trên local trước, có cấu hình Docker chuẩn và có thể đưa lên VPS Server sau. Việc phân tán frontend, API và data trên Vercel, Cloud Run và Supabase chưa tạo giá trị cần thiết cho MVP, đồng thời làm tăng provider và operations surface.

## Decision

- Giữ modular monolith: Next.js web/PWA, FastAPI API, PostgreSQL và private object storage adapter.
- Local development và integration dùng Docker Compose làm reproducible runtime boundary.
- Production target đầu tiên là một Linux VPS chạy versioned container images qua Docker Compose.
- Alembic là authority duy nhất cho database migration.
- GitHub Actions build/test/scan image; production deployment phải có manual approval và immutable release identifier.
- Vercel, Cloud Run và Supabase vẫn là alternative provider, không phải target mặc định hiện tại.

Full-stack Compose chưa được coi là implemented: hiện runtime evidence mới có PostgreSQL container tại host port `5433`. Web/API container, reverse proxy, TLS, auth adapter, private object storage, backup và deployment automation thuộc D2.

## Target topology

```mermaid
flowchart TB
    User["PC/Mobile browser"] --> TLS["Reverse proxy + TLS"]
    TLS --> Web["Next.js web container"]
    TLS --> API["FastAPI container"]
    Web --> API
    API --> PG["PostgreSQL container/service"]
    API --> Files["Private object storage adapter"]
    Jobs["Scheduled jobs using API image"] --> API
    Backup["Encrypted off-site backup"] <-- PG
    Backup <-- Files
```

## Consequences

### Positive

- Local và VPS gần nhau hơn về runtime shape.
- Một release có thể pin bằng image tag/digest và Docker Compose version.
- Giảm phụ thuộc đa provider trong giai đoạn đầu.

### Risks

- Một VPS tạo single failure domain nếu không có backup/restore và recovery plan.
- RUBIK phải sở hữu OS patching, TLS, firewall, resource monitoring và secret handling.
- Local volume không phải production backup; database và evidence cần encrypted off-site copy.
- Self-hosted auth/storage có thể tăng scope; D2 phải chọn adapter đơn giản và được kiểm thử trước khi domain implementation phụ thuộc vào nó.

## Review condition

Review lại ADR khi production load/evidence chứng minh một VPS không đáp ứng reliability, security hoặc scale; hoặc khi chi phí vận hành self-hosted cao hơn managed provider có thể đo được. Không chuyển provider chỉ vì preference.
