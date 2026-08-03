# Architecture References

Các nguồn này dùng để định hướng stack đề xuất. Chúng không thay thế business rules hoặc ADR đã được chấp nhận của RubikStock.

## Application runtime

- [FastAPI in Containers](https://fastapi.tiangolo.com/deployment/docker/)
- [Vercel: FastAPI](https://vercel.com/docs/frameworks/backend/fastapi)
- [Vercel: Python Runtime](https://vercel.com/docs/functions/runtimes/python)
- [Vercel: Managing Cron Jobs](https://vercel.com/docs/cron-jobs/manage-cron-jobs)
- [Google Cloud Run overview](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)

## Supabase data và security

- [Supabase: Understanding API keys](https://supabase.com/docs/guides/getting-started/api-keys)
- [Supabase: Securing your data](https://supabase.com/docs/guides/database/secure-data)
- [Supabase: Connect to Postgres](https://supabase.com/docs/guides/database/connecting-to-postgres)
- [Supabase: Database backups](https://supabase.com/docs/guides/platform/backups)

## Delivery pipeline

- [GitHub: Deployment environments](https://docs.github.com/en/actions/concepts/workflows-and-actions/deployment-environments)
- [GitHub: OpenID Connect](https://docs.github.com/en/actions/concepts/security/openid-connect)

## Quy tắc review

Phải kiểm tra lại tài liệu của provider trong D2 trước khi chốt runtime version, tính năng phụ thuộc giá, quota, connection mode, hoặc hành vi production deployment.
