# Deployment Runbook

## Trạng thái

`PRE-RUNTIME DRAFT`. Các command chưa thể coi là canonical cho tới khi D2 tạo xong executable project và CI workflow.

## Luồng release dự kiến

1. Pull request phải pass format, lint, types, tests, migration reset, build, và secret scan.
2. Merge tạo ra immutable web/API image, pin bằng release tag hoặc digest.
3. Deploy Compose release tương thích database lên isolated staging VPS/project.
4. Áp dụng migration staging qua migration job được kiểm soát.
5. Chạy health, auth, và critical inventory smoke test.
6. Review migration/compatibility rồi approve production environment.
7. Tạo/xác minh production recovery point cần thiết.
8. Áp dụng production migration với policy lock/timeout.
9. Pull đúng image digest và deploy API/jobs/frontend/reverse proxy bằng production Compose project.
10. Chạy health read-only và bounded transaction smoke.
11. Theo dõi error/reconciliation metrics.
12. Ghi lại release ID, migration ID, evidence, và rollback decision.

## Nguyên tắc rollback

- Application rollback phải còn tương thích với schema đã migrate.
- Ưu tiên expand/migrate/contract cho schema evolution gây breaking change.
- Không tự động đảo ngược migration nếu nó có thể phá dữ liệu nghiệp vụ vừa ghi.
- Tạm dừng stock command và reconcile nếu kết quả deployment không rõ.

## Output bắt buộc của D2

- Full-stack Local Docker canonical command hiện có: `npm run stack:up`; PostgreSQL tiếp tục publish host port `5433`.
- Local verification command: `npm run smoke:stack`, success marker `RUBIKSTOCK_STACK_SMOKE_OK`.
- CI jobs chính xác và success markers.
- Lệnh deploy staging/production chính xác.
- Health endpoint và smoke scenario.
- Version identifier được expose bởi API/web.
- Ma trận quyết định cho migration và rollback.

## VPS preflight bắt buộc

- Linux host version, Docker Engine/Compose version và resource capacity được ghi lại.
- Firewall chỉ mở SSH có kiểm soát và reverse-proxy TLS ports; PostgreSQL không public.
- DNS/TLS, time synchronization và log rotation hoạt động.
- Secret file/environment nằm ngoài repository, permission tối thiểu.
- Database/evidence backup có encrypted off-site target và restore evidence.
- Deploy command dùng immutable image, không build production từ working tree trên VPS.
