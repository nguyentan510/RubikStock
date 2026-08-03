# Traceability Matrix

Trạng thái phản ánh evidence hiện có, không phải work tương lai dự định.

| Rule set | Design owner | Planned implementation | Required verification | Status |
|---|---|---|---|---|
| INV-001..008 | Inventory ledger | `inventory` module + migrations | Test ledger/projection, negative, reversal, transfer | Documented |
| LOT-001..006 | Lot/quality | `catalog`, `inventory`, `quality` | Test thiếu date, recall, trace nhiều location | Documented |
| UOM-001..004 | Catalog/UOM | `catalog` + inventory posting | Test conversion/version/fraction chính xác | Documented; TBD-002 open |
| OUT-001..010 | Outbound | `outbound` + inventory reservations | Test concurrency, FEFO, shelf-life, override, nhiều Lot | Documented |
| QLT-001 | Quality | status eligibility policy | Test toàn bộ blocked-status allocation | Documented |
| RET-001..004 | Returns/quality | return và disposition services | Test quarantine/restock/genealogy | Documented |
| DST-001..002 | Quality/inventory | destruction workflow | Test tách biệt, idempotent posting, evidence | Documented; threshold TBD |
| DEL-001..005 | Delivery | trip/loading/POD/reconciliation | Test delivery partial/failed và return reconciliation | Documented |
| PLN-001..006 | Planning | versioned planning runs | Test reproducibility, stockout flag, event window, WAPE/bias | Documented; history TBD |
| AUD-001..003 | Audit | audit service/storage | Test actor/state/reason/occurred-vs-recorded | Documented |
| SEC-001..003 | Identity/security | auth middleware/policy/CI | Test permission, secret scan, browser exposure | Documented |

## Quy tắc promotion

Một dòng chỉ được nâng từ `Documented` khi đường implementation của nó đã tồn tại và verification bắt buộc thực sự pass. Chỉ hoàn thành tài liệu không thể đặt thành `Implemented`.
