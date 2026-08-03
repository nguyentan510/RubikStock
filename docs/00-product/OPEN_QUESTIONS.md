# Open Questions and Decision Register

Đây là decision register lịch sử cho `TBD-001..014`. Mỗi mục phải có disposition rõ ràng; `Deferred` không đồng nghĩa đã accepted và chỉ được mở lại theo owner/due gate đã ghi.

D0 workshop đang được điều phối tại [`../06-delivery/big-plan/D0_DECISION_WORKSHOP.md`](../06-delivery/big-plan/D0_DECISION_WORKSHOP.md).

| ID | Câu hỏi | Vì sao quan trọng | Status |
|---|---|---|---|
| TBD-001 | Có bao nhiêu SKU, warehouse, và physical storage zone đang hoạt động? | Ảnh hưởng data volume, rollout, và thiết kế location | Accepted 2026-08-03: 2 warehouse, khoảng 300 SKU, four-zone baseline, pilot `WH-01-AVL` |
| TBD-002 | Product nào được bán sau khi break case/bag, và opened bag có được bán theo weight không? | UOM, food safety, repacking, traceability | Accepted 2026-08-03: product-level case break và measured sale gram/kg có genealogy |
| TBD-003 | Các field supplier lot, MFG, và EXP trong Excel/lịch sử hiện tại đầy đủ tới mức nào? | Ảnh hưởng cutover và policy quarantine | Accepted 2026-08-03: không import legacy; clean-start template + physical opening count + category date policy |
| TBD-004 | Sales order hiện được nhận ở đâu: Excel, Zalo, điện thoại, phần mềm accounting, hay công cụ khác? | Ảnh hưởng integration và phạm vi order-entry | Accepted 2026-08-03: Sales; RubikStock là operational order truth sau confirmation |
| TBD-005 | Một sales order có thể tách thành nhiều lần giao không? | Ảnh hưởng shipment và mô hình state của reservation | Accepted 2026-08-03: multi-shipment, partial delivery và backorder |
| TBD-006 | Có bao nhiêu tháng/năm sales history là tin cậy, bao gồm cả stockout period? | Ảnh hưởng forecast qualification | Accepted 2026-08-03: bỏ legacy history, capture forward bằng format chuẩn |
| TBD-007 | Hệ thống accounting/invoice nào phải nhận kết quả fulfillment? | Xác định boundary và integration | Deferred 2026-08-03, owner `Kế toán`: không integration/export trong MVP; xác định MISA product/edition và contract trước integration slice |
| TBD-008 | Khách nào cần minimum remaining shelf life, và yêu cầu đó được biểu đạt như thế nào? | Ảnh hưởng FEFO eligibility | Accepted 2026-08-03: dealer/shop; configurable days, percent hoặc both |
| TBD-009 | Ngưỡng approval nào áp dụng cho adjustment, FEFO override, discount, và destruction? | Ảnh hưởng permission/approval matrix | Accepted 2026-08-03: one-level Warehouse Manager; no second level; discount out of scope |
| TBD-010 | Evidence nào là bắt buộc về pháp lý/vận hành cho destruction và customer returns? | Ảnh hưởng lưu trữ và audit | Accepted 2026-08-03: mandatory private photo + note |
| TBD-011 | Kho và xe hiện có thiết bị, connectivity, và khả năng offline như thế nào? | Ảnh hưởng PWA, barcode, offline behavior | Accepted 2026-08-03: PC/mobile, stable connectivity, online-first MVP |
| TBD-012 | License nào nên áp dụng cho public source code? | Ảnh hưởng quyền reuse và contribution | Deferred 2026-08-03, owner `CEO/Project Owner`: public source-visible, chưa có OSS license; review trước external contribution/distribution |
| TBD-013 | Runtime target ban đầu là managed multi-provider hay Docker/VPS? | Ảnh hưởng runtime và operations design | Accepted 2026-08-03: Local Docker-first, production target Linux VPS bằng Docker Compose |
| TBD-014 | Thời gian lưu trữ bắt buộc cho audit log, delivery evidence, và transaction record là bao lâu? | Ảnh hưởng storage, privacy, compliance | Accepted 2026-08-03: no auto-delete; CEO final approval + Warehouse Manager review for policy change |

## Quy trình quyết định

Mỗi mục được giải quyết phải ghi lại câu trả lời, người duyệt, ngày, các rule bị ảnh hưởng, và việc có cần ADR hoặc migration hay không.
