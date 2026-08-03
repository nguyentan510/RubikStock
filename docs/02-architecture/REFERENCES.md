# Architecture References

Các nguồn này dùng để định hướng stack đề xuất. Chúng không thay thế business rules hoặc ADR đã được chấp nhận của RubikStock.

## Application runtime

- [FastAPI in Containers](https://fastapi.tiangolo.com/deployment/docker/)
- [Docker Compose production considerations](https://docs.docker.com/compose/how-tos/production/)
- [Docker Engine security](https://docs.docker.com/engine/security/)

## Managed-provider alternatives

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

## MISA integration discovery

- [MISA AMIS Kế toán external application connection](https://helpact.misa.vn/kb/ket-noi-du-lieu-tren-he-thong-amis-voi-cac-ung-dung-khac/)
- [MISA AMIS Open API](https://actdocs.misa.vn/g2/graph/ACTOpenAPIHelp/index.html)
- [MISA meInvoice Integration](https://doc.meinvoice.vn/itg/)

## Repository licensing

- [GitHub: Licensing a repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)
- [Apache Software Foundation License FAQ](https://www.apache.org/foundation/license-faq.html)

## Quy tắc review

Phải kiểm tra lại tài liệu của provider trong D2 trước khi chốt runtime version, tính năng phụ thuộc giá, quota, connection mode, hoặc hành vi production deployment.
