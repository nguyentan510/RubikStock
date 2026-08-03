# Clean-start Data and Cutover Plan

## Nguyên tắc

RUBIK đã quyết định không import legacy Excel history cho Lot/date hoặc sales. Cutover dùng master data mới, physical opening count mới và forward capture theo bộ template chuẩn.

Legacy files có thể được giữ riêng tư để tra cứu thủ công khi cần nhưng không phải migration source, không được dùng làm inventory truth và không được commit vào public repository.

Bộ template chuẩn nằm tại [`templates/README.md`](templates/README.md).

## Các giai đoạn

### 1. Tạo master data mới

- Gán stable SKU cho khoảng 300 product.
- Phân loại category, storage condition và Lot/date tracking policy.
- Khai báo base UOM, case break và measured-sale policy.
- Tạo supplier/customer code mới; không phụ thuộc alias lịch sử chưa qualify.

### 2. Khai báo UOM và warehouse map

- Khai báo conversion về base UOM theo từng product.
- Khai báo 2 warehouse và four-zone baseline `INB/AVL/QTN/OUT`.
- Mã hóa rack/level/bin cho pilot `WH-01-AVL`.
- Validate duplicate SKU, ambiguous conversion và location code.

### 3. Physical opening count

- Gắn location code trước khi đếm.
- Đếm theo warehouse, location, SKU, supplier Lot, date, status và UOM.
- F&B thiếu Lot/EXP xác minh được vào `QUARANTINE`.
- Không copy quantity từ legacy Excel để thay thế physical count.
- Recount và approval cho variance theo policy.

### 4. Validate và dry-run

Mỗi dòng template là `ACCEPTED`, `REJECTED`, hoặc `QUARANTINED` kèm reason code. Import phải idempotent theo template type, batch/reference và row business key.

### 5. Bắt đầu forward capture

- Receipt mới dùng `receipt_capture.csv` cho tới khi M3 UI là system of record.
- Sales mới dùng `sales_capture.csv` cho tới khi M4 order flow là system of record.
- Stockout/lost-sale phải được ghi rõ từ ngày bắt đầu capture.
- Không backfill lịch sử bằng suy đoán.

### 6. Cutover

1. Chốt master-data/template version và physical-count window.
2. Freeze quantity movement trong bounded count/cutover window.
3. Validate/import master data và opening-count batch đã duyệt.
4. Post các `OPENING_BALANCE` operation.
5. Reconcile tổng và trace mẫu các Lot; unknown Lot/date vẫn ở quarantine.
6. Bắt đầu forward capture trên RubikStock/template mới; legacy Excel chỉ read-only/archive.

## Báo cáo import bắt buộc

- Identity/hash của clean-start template batch.
- Số dòng accepted/rejected/quarantined.
- Tổng quantity theo product/UOM.
- Số field thiếu/không hợp lệ.
- Phiên bản template/UOM/location master.
- Import run ID và actor.
- ID của opening-balance operation.
- Chữ ký sign-off reconciliation.

## Rollback

Trước khi live business transaction bắt đầu, cutover thất bại có thể reset môi trường mới và chạy lại từ accepted clean-start templates. Sau khi live transaction bắt đầu, rollback cần business freeze và controlled recovery; database không được reset tùy tiện và forward history không được quay lại legacy Excel như một writer thứ hai.
