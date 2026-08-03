# ADR-0004: Proposed Managed-provider Deployment Stack

- Status: `SUPERSEDED`
- Date: 2026-08-03
- Superseded by: [`0005-local-docker-vps-target.md`](0005-local-docker-vps-target.md)

## Context

RUBIK đề xuất Python/FastAPI/SQLAlchemy/Pydantic, Supabase, Vercel, và GitHub Actions public. Hệ thống cũng cần web UI, scheduled jobs, private evidence storage, và tách biệt môi trường.

## Decision proposal

- Next.js/TypeScript PWA trên Vercel.
- FastAPI/SQLAlchemy/Pydantic chạy trong container runtime; Cloud Run là khuyến nghị mặc định hiện tại.
- Supabase PostgreSQL/Auth/private Storage.
- Alembic là authority duy nhất cho database migration.
- GitHub Actions với staging và protected production environments.

## Disposition

RUBIK đã chọn Local Docker-first và VPS Docker Compose làm target đầu tiên tại `TBD-013`. Vercel, Cloud Run và Supabase trở thành alternatives để review sau khi có measured operational need; proposal này không còn là deployment baseline.
