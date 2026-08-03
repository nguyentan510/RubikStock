# ADR-0004: Proposed Web, API, and Data Deployment Stack

- Status: `PROPOSED`
- Date: 2026-08-03

## Context

RUBIK đề xuất Python/FastAPI/SQLAlchemy/Pydantic, Supabase, Vercel, và GitHub Actions public. Hệ thống cũng cần web UI, scheduled jobs, private evidence storage, và tách biệt môi trường.

## Decision proposal

- Next.js/TypeScript PWA trên Vercel.
- FastAPI/SQLAlchemy/Pydantic chạy trong container runtime; Cloud Run là khuyến nghị mặc định hiện tại.
- Supabase PostgreSQL/Auth/private Storage.
- Alembic là authority duy nhất cho database migration.
- GitHub Actions với staging và protected production environments.

## Quyết định còn cần

RUBIK phải chấp nhận production backend runtime và repository license (`TBD-012`, `TBD-013`). Một pilot chỉ dùng Vercel được phép khi có review/exit condition rõ ràng.
