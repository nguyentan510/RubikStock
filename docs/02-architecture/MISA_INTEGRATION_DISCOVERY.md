# MISA Integration Discovery

- Status: `DEFERRED_WITH_OWNER`
- Decision ID: `TBD-007`
- Owner: `Kế toán`
- Review gate: trước khi mở một integration slice, mặc định không sớm hơn M9
- Last reviewed: 2026-08-03

## Quyết định hiện tại

MVP không tích hợp MISA và chưa export accounting data. RubikStock là operational source of truth cho order đã xác nhận, fulfillment, shipment và inventory; MISA tiếp tục là financial/invoice source of truth.

Không triển khai connector cho tới khi RUBIK xác định chính xác MISA product/edition đang dùng và Accounting chấp nhận data contract. Tên gọi chung "MISA" không đủ để chọn API.

## Kết quả tham khảo official documentation

- [MISA AMIS Kế toán - kết nối ứng dụng khác qua API](https://helpact.misa.vn/kb/ket-noi-du-lieu-tren-he-thong-amis-voi-cac-ung-dung-khac/) mô tả khả năng kết nối external application.
- [MISA AMIS Kế toán - lập chứng từ từ dữ liệu kết nối qua API](https://helpact.misa.vn/kb/lap-chung-tu-hach-toan-tu-du-lieu-ket-noi-voi-cac-ung-dung-khac-qua-api/) cho thấy dữ liệu external có thể đi qua proposal/review trước khi tạo accounting voucher.
- [MISA AMIS Open API](https://actdocs.misa.vn/g2/graph/ACTOpenAPIHelp/index.html) có các nhóm API cho master data và nhiều loại sales/purchase/inventory document.
- [MISA meInvoice Integration](https://doc.meinvoice.vn/itg/) là integration surface riêng cho electronic invoice, có test và production environment.

Các tài liệu trên chứng minh có integration option, nhưng không chứng minh option nào đúng với license, edition hoặc workflow hiện tại của RUBIK.

## Discovery checklist bắt buộc

Accounting phải xác nhận:

1. Product và edition: ví dụ `MISA AMIS Kế toán`, `MISA SME.NET`, `meInvoice`, hoặc tổ hợp đang dùng.
2. Deployment mode, account/license và khả năng cấp API credential/test environment.
3. MISA giữ master nào: customer, supplier, item, UOM, warehouse, tax và invoice number.
4. Event nào cần trao đổi: fulfilled shipment, sales return, warehouse receipt/issue, invoice request hoặc journal proposal.
5. Hướng dữ liệu: ưu tiên one-way RubikStock -> MISA; mọi two-way sync cần owner và conflict rule riêng.
6. Accounting review/approval nào phải xảy ra trước khi voucher hoặc invoice trở thành official.

## Contract guardrails cho integration tương lai

- Mapping dùng external ID rõ ràng; không match theo tên tự do.
- Export/API command phải có idempotency key và lưu external document ID.
- Có trạng thái `PENDING`, `SENT`, `ACCEPTED`, `REJECTED`, `RECONCILIATION_REQUIRED` thay vì coi HTTP success là accounting success.
- Retry không được tạo duplicate voucher/invoice.
- RubikStock không ghi đè inventory truth từ MISA nếu chưa có accepted reconciliation design.
- Discount, tax calculation, posting và official invoice vẫn do Sales/Accounting/MISA sở hữu.
- Credential là private server-side secret; không đưa vào browser, log hoặc repository public.

## Exit condition của trạng thái deferred

TBD-007 chỉ được mở lại khi có đủ: product/edition cụ thể, Accounting owner, accepted field mapping, sample sanitized payload, test environment, error/retry/reconciliation policy và acceptance scenarios.
