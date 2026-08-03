# Deployment Runbook

## Trạng thái

`PRE-RUNTIME DRAFT`. Các command chưa thể coi là canonical cho tới khi D2 tạo xong executable project và CI workflow.

## Luồng release dự kiến

1. Pull request phải pass format, lint, types, tests, migration reset, build, và secret scan.
2. Merge tạo ra build artifact/image bất biến.
3. Deploy ứng dụng tương thích database lên staging.
4. Áp dụng migration staging qua migration job được kiểm soát.
5. Chạy health, auth, và critical inventory smoke test.
6. Review migration/compatibility rồi approve production environment.
7. Tạo/xác minh production recovery point cần thiết.
8. Áp dụng production migration với policy lock/timeout.
9. Deploy API/jobs và frontend.
10. Chạy health read-only và bounded transaction smoke.
11. Theo dõi error/reconciliation metrics.
12. Ghi lại release ID, migration ID, evidence, và rollback decision.

## Nguyên tắc rollback

- Application rollback phải còn tương thích với schema đã migrate.
- Ưu tiên expand/migrate/contract cho schema evolution gây breaking change.
- Không tự động đảo ngược migration nếu nó có thể phá dữ liệu nghiệp vụ vừa ghi.
- Tạm dừng stock command và reconcile nếu kết quả deployment không rõ.

## Output bắt buộc của D2

- Cách setup local bằng đúng một lệnh.
- CI jobs chính xác và success markers.
- Lệnh deploy staging/production chính xác.
- Health endpoint và smoke scenario.
- Version identifier được expose bởi API/web.
- Ma trận quyết định cho migration và rollback.
