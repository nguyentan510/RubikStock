# D2 Roadmap - Technical Foundation

- Status: `IMPLEMENTED_PARTIAL`
- Depends on: D0-D1 cho các quyết định ảnh hưởng contract; foundation không-domain có thể chạy song song
- Unlocks: Implementation M1-M8 có kiểm soát

## Outcome

Có môi trường development/staging tái tạo được, authentication/authorization foundation, migrations, CI, observability và security baseline đủ để triển khai domain an toàn.

## Baseline đã có

- FastAPI, Pydantic, SQLAlchemy và Alembic scaffold.
- Next.js/TypeScript web shell.
- Full-stack Docker Compose: PostgreSQL `5433`, API `8000`, web `3000` và one-off Alembic migration.
- Health/readiness/meta/OpenAPI, structured logging và CORS.
- Local setup/check/smoke scripts và CI scaffold.
- Local full-stack smoke, API tests, lint, typecheck và web build evidence.

## Work packages

| ID | Nội dung | Deliverables | Verification |
|---|---|---|---|
| D2.1 | Repository governance | License, branch policy, contribution/security policy | Repo governance review |
| D2.2 | Reproducible environments | Full-stack Local Docker Compose, local/test/staging matrix, pinned toolchains | Clean-machine setup smoke |
| D2.3 | Migration lifecycle | Baseline, upgrade/reset/rebuild/rollback policy | Clean PostgreSQL rebuild gate |
| D2.4 | Identity foundation | Authentication adapter, named users, session/token validation | Auth smoke |
| D2.5 | Authorization foundation | Server-side RBAC/policy dependency | Permission allow/deny tests |
| D2.6 | API contract baseline | Error envelope, pagination, idempotency, request IDs | OpenAPI/contract tests |
| D2.7 | Private file foundation | Storage metadata, signed access, size/type policy | Unauthorized-access tests |
| D2.8 | CI/security hardening | Ruff, tests, build, migrations, secret/dependency scan | CI run pass; high findings disposed |
| D2.9 | Staging deployment | Isolated VPS/Compose project, database/secrets/domain, deploy/rollback commands | Staging readiness smoke |
| D2.10 | Foundation exit review | Evidence links và operator commands | Gate D2 pass |

## Thứ tự triển khai đề xuất

1. Đóng D2.1 và D2.2 để repo/setup có quy ước rõ.
2. Chứng minh D2.3 trước migration domain đầu tiên.
3. Triển khai D2.4-D2.5 trước privileged CRUD.
4. Chốt D2.6 trước khi API M1 trở thành public contract.
5. D2.7 chỉ cần trước evidence upload của M5-M6.
6. Đóng D2.8-D2.9, sau đó review D2.10.

## Finding đang mở

- Authentication/authorization chưa được triển khai.
- Full-stack Local Docker Compose đã verified; clean-machine reproduction và staging VPS chưa có evidence.
- `npm audit` có ba finding mức `high` trong dependency tree.
- Baseline migration chưa chứa domain schema; clean reset policy cần evidence trước M1.
- Repository public source-visible nhưng chưa có OSS license; license selection deferred có owner và due gate.

## Exit gate

- Một lệnh setup trên clean environment.
- Migration clean rebuild pass.
- CI thực tế pass toàn bộ configured jobs.
- Auth/authz allow-deny smoke pass.
- Staging cô lập và health smoke pass.
- Không còn security finding mức cao chưa có accepted disposition.
