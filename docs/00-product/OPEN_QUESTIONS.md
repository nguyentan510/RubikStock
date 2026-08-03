# Open Questions and Decision Register

Các mục này vẫn là `TBD` cho tới khi RUBIK xác nhận. Không được ngầm giả định rồi coi như đã xong.

| ID | Câu hỏi | Vì sao quan trọng | Status |
|---|---|---|---|
| TBD-001 | Có bao nhiêu SKU, warehouse, và physical storage zone đang hoạt động? | Ảnh hưởng data volume, rollout, và thiết kế location | Open |
| TBD-002 | Product nào được bán sau khi break case/bag, và opened bag có được bán theo weight không? | UOM, food safety, repacking, traceability | Open |
| TBD-003 | Các field supplier lot, MFG, và EXP trong Excel/lịch sử hiện tại đầy đủ tới mức nào? | Ảnh hưởng cutover và policy quarantine | Open |
| TBD-004 | Sales order hiện được nhận ở đâu: Excel, Zalo, điện thoại, phần mềm accounting, hay công cụ khác? | Ảnh hưởng integration và phạm vi order-entry | Open |
| TBD-005 | Một sales order có thể tách thành nhiều lần giao không? | Ảnh hưởng shipment và mô hình state của reservation | Open |
| TBD-006 | Có bao nhiêu tháng/năm sales history là tin cậy, bao gồm cả stockout period? | Ảnh hưởng forecast qualification | Open |
| TBD-007 | Hệ thống accounting/invoice nào phải nhận kết quả fulfillment? | Xác định boundary và integration | Open |
| TBD-008 | Khách nào cần minimum remaining shelf life, và yêu cầu đó được biểu đạt như thế nào? | Ảnh hưởng FEFO eligibility | Open |
| TBD-009 | Ngưỡng approval nào áp dụng cho adjustment, FEFO override, discount, và destruction? | Ảnh hưởng permission/approval matrix | Open |
| TBD-010 | Evidence nào là bắt buộc về pháp lý/vận hành cho destruction và customer returns? | Ảnh hưởng lưu trữ và audit | Open |
| TBD-011 | Kho và xe hiện có thiết bị, connectivity, và khả năng offline như thế nào? | Ảnh hưởng PWA, barcode, offline behavior | Open |
| TBD-012 | License nào nên áp dụng cho public source code? | Ảnh hưởng quyền reuse và contribution | Open |
| TBD-013 | Cloud Run có được chấp nhận cho production FastAPI backend không, hay bắt buộc Vercel-only? | Ảnh hưởng runtime và operations design | Open |
| TBD-014 | Thời gian lưu trữ bắt buộc cho audit log, delivery evidence, và transaction record là bao lâu? | Ảnh hưởng storage, privacy, compliance | Open |

## Quy trình quyết định

Mỗi mục được giải quyết phải ghi lại câu trả lời, người duyệt, ngày, các rule bị ảnh hưởng, và việc có cần ADR hoặc migration hay không.
