# Traceability Matrix

Trạng thái phản ánh evidence hiện có, không phải work tương lai dự định.

| Rule set | Design owner | Planned implementation | Required verification | Status |
|---|---|---|---|---|
| INV-001..008 | Inventory ledger | `inventory` module + migrations | Test ledger/projection, negative, reversal, transfer | Business contract accepted D1 Batch A; not implemented |
| LOT-001..006 | Lot/quality | `catalog`, `inventory`, `quality` | Test thiếu date, recall, trace nhiều location | Business contract accepted D1 Batch A; not implemented |
| UOM-001..004 | Catalog/UOM | `catalog` + inventory posting | Test conversion/version/fraction/repack genealogy | Business contract accepted D1 Batch A; not implemented |
| INB-001..009 | Inbound | `inbound`, `inventory`, `quality` | Test discrepancy, QC split, idempotency, put-away mismatch | Business contract accepted D1 Batch B; not implemented |
| OUT-001..011 | Outbound | `outbound` + inventory reservations | Test concurrency, lifecycle, FEFO, shelf-life, override, nhiều Lot | Business contract accepted D1 Batch C; not implemented |
| QLT-001..004 | Quality | status eligibility/inspection policy | Test hold scope, partial release, Lot recall | Business contract accepted D1 Batch D; not implemented |
| RET-001..005 | Returns/quality | return và disposition services | Test quarantine/restock/genealogy/idempotency | Business contract accepted D1 Batch D; not implemented |
| DST-001..004 | Quality/inventory | destruction workflow | Test separation, version/quantity, idempotent posting, evidence | Business contract accepted D1 Batch D; not implemented |
| DEL-001..007 | Delivery | trip/loading/POD/reconciliation | Test delivery partial/failed, authorization và return reconciliation | Business contract accepted D1 Batch D; not implemented |
| PLN-001..007 | Planning | versioned planning runs | Test reproducibility, stockout flag, event window, fallback, WAPE/bias | Business contract accepted D1 Batch E; not implemented |
| AUD-001..006 | Audit | audit service/storage | Test actor/state/reason/time/correlation/retention authorization | Business contract accepted D1 Batch E; not implemented |
| SEC-001..006 | Identity/security | auth middleware/policy/CI/private files | Test permission, assigned scope, secret scan, evidence và environment isolation | Business contract accepted D1 Batch E; not implemented |

## Quy tắc promotion

Một dòng chỉ được nâng từ `Documented` khi đường implementation của nó đã tồn tại và verification bắt buộc thực sự pass. Chỉ hoàn thành tài liệu không thể đặt thành `Implemented`.
