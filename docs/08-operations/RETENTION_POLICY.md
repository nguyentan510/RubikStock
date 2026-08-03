# Retention Policy

## Trạng thái

`D0 ACCEPTED - PROVISIONAL`: tạm thời không tự động xóa transaction, audit, POD, return hoặc destruction evidence.

## Record classes

| Record class | Current retention | Access |
|---|---|---|
| Inventory/order/shipment transactions | Không thời hạn, không auto-delete | Authorized operations/audit |
| Audit/approval records | Không thời hạn, không auto-delete | Privileged audit/security |
| POD/delivery evidence | Không thời hạn, không auto-delete | Delivery/customer-case scope |
| Return/destruction photo và note | Không thời hạn, không auto-delete | Quality/manager/audit |

## Governance

- CEO là final approver cho thay đổi retention/deletion policy.
- Warehouse Manager review tác động vận hành và traceability.
- Không user hoặc scheduled job nào được purge record khi chưa có policy change đã duyệt.
- Mọi deletion mechanism trong tương lai phải có scope, reason, actor, approval, dry-run và immutable audit record.
- Database record và private Storage object phải được xử lý đồng bộ; không để orphan hoặc mất genealogy.

## Production review condition

No-delete là policy tạm thời, không phải kết luận pháp lý về thời hạn lưu trữ. Trước Gate M8, RUBIK phải review storage cost, privacy, backup lifecycle và yêu cầu pháp lý/commercial; bất kỳ thay đổi nào vẫn cần approval theo governance trên.
