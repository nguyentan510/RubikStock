# Incident Runbook

## Quy tắc trạng thái không an toàn

Nếu outcome của inventory, reservation, shipment, hoặc database chưa rõ, hãy tạm dừng các stock command mới bị ảnh hưởng cho tới khi reconciliation xác nhận state.

## Hướng dẫn severity

| Severity | Ví dụ | Hành động ngay |
|---|---|---|
| SEV-1 | Stock movement sai/trùng, truy cập trái phép diện rộng, production data không thể reconcile | Dừng hoạt động bị ảnh hưởng, giữ evidence, gọi incident lead |
| SEV-2 | Module không khả dụng, workflow giao hàng bị trễ, lỗi permission cô lập | Khoanh vùng, chuyển sang fallback đã duyệt, điều tra |
| SEV-3 | Lỗi report/alert không quan trọng nhưng core stock đúng | Theo dõi và sửa mà không dùng workaround nguy hiểm |

## Phản ứng đầu tiên

1. Công bố incident ID, owner, thời điểm bắt đầu, và phạm vi bị ảnh hưởng.
2. Dừng các command gây hại, không nhất thiết dừng mọi read operation.
3. Giữ log, request ID, movement/operation ID, deployment version, và evidence database.
4. Xác định trạng thái nhất quán cuối cùng đã biết.
5. Reconcile trước khi replay hoặc sửa.
6. Dùng reversal/compensating movement, không chỉnh balance ẩn.
7. Truyền đạt workaround vận hành và giới hạn rõ ràng.

## Kết thúc

- Root cause và mức ảnh hưởng.
- Timeline và record bị ảnh hưởng.
- Evidence khôi phục/reconciliation.
- Hành động khắc phục/phòng ngừa.
- Chữ ký xác nhận của business owner nếu inventory/customer delivery bị ảnh hưởng.
