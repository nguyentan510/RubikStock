# Business Rules

## Trạng thái và định danh

Document đang `D1 ACCEPTED`. Rule ID là ổn định và phải được dùng trong test, API, tiêu chí nghiệm thu UI, và traceability matrix.

| Rule group | Status | Evidence |
|---|---|---|
| `INV-001..008` | `ACCEPTED` | D1 Batch A, `Quản lý Kho`, 2026-08-03 |
| `LOT-001..006` | `ACCEPTED` | D1 Batch A, `Quản lý Kho`, 2026-08-03 |
| `UOM-001..004` | `ACCEPTED` | D1 Batch A, `Quản lý Kho`, 2026-08-03 |
| `INB-001..009` | `ACCEPTED` | D1 Batch B, `Quản lý Kho`, 2026-08-03 |
| `OUT-001..011` | `ACCEPTED` | D1 Batch C, `Quản lý Kho`, 2026-08-03 |
| `QLT-001..004`, `RET-001..005`, `DST-001..004`, `DEL-001..007` | `ACCEPTED` | D1 Batch D, `Quản lý Kho`, 2026-08-03 |
| `PLN-001..007`, `AUD-001..006`, `SEC-001..006` | `ACCEPTED` | D1 Batch E, `Quản lý Kho`, 2026-08-03 |

## Inventory truth

| ID | Rule |
|---|---|
| INV-001 | Mọi thay đổi stock phải tạo một inventory movement bất biến với actor, thời điểm xảy ra, thời điểm ghi nhận, lý do/tham chiếu, product, quantity, và quantity đã normalize theo UOM. |
| INV-002 | Balance có thể thay đổi là projection/cache được suy ra; nó không bao giờ là nguồn duy nhất của lịch sử stock. |
| INV-003 | Stock phải được scope tối thiểu theo warehouse, location, product, lot khi cần, và inventory status. |
| INV-004 | Confirmed balance không được âm. Reservation/allocation phải atomic khi có request đồng thời. |
| INV-005 | Available quantity = eligible on-hand quantity trừ active reservations. Stock bị blocked, quarantine, damaged, expired, recalled, hoặc chờ hủy không được tính là available. |
| INV-006 | Movement đã post không được xóa hay sửa để đổi nghĩa; lỗi phải sửa bằng reversal và replacement kèm audit link. |
| INV-007 | Transfer phải dùng cặp movement nguồn/đích trong cùng một transaction. |
| INV-008 | Chênh lệch physical count phải có lý do và một cấp `Warehouse Manager` approval trước khi post adjustment; requester và approver phải khác nhau. |

## Product, Lot, và date

| ID | Rule |
|---|---|
| LOT-001 | Supplier lot và internal lot là hai định danh riêng; định danh nội bộ không được làm mất Supplier lot. |
| LOT-002 | Lot uniqueness được enforce trong phạm vi product/supplier đã xác định; constraint chính xác sẽ chốt ở data design. |
| LOT-003 | Yêu cầu MFG và EXP được cấu hình theo product/category; thiếu dữ liệu bắt buộc thì fail closed. |
| LOT-004 | Trạng thái expired được suy ra từ business date/time và policy đã kiểm soát, không được bỏ qua thủ công. |
| LOT-005 | Recall/block trên một Lot phải ngăn mọi allocation mới trên tất cả location đang giữ Lot đó. |
| LOT-006 | Lot/expiry không rõ hoặc không thể xác minh khi cutover phải vào quarantine cho đến khi được giải quyết. |

## UOM và packaging

| ID | Rule |
|---|---|
| UOM-001 | Mỗi product có một base inventory UOM. Mọi movement phải lưu UOM/quantity đã nhập và base quantity đã normalize. |
| UOM-002 | Conversion là theo từng product, có version/effective date, và không được diễn giải lại movement đã post theo cách hồi tố. |
| UOM-003 | Hàng rời/đơn chiếc dùng base quantity nguyên chính xác; kết quả lẻ bị từ chối trừ khi product cho phép measured quantity một cách rõ ràng. |
| UOM-004 | Chỉ được mở/bẻ seal của package khi product có policy repacking/traceability đã được chấp nhận. |

## Inbound, discrepancy, QC và put-away

| ID | Rule |
|---|---|
| INB-001 | Receipt nên tham chiếu approved Purchase Order khi có; unplanned receipt chỉ được nhận vào controlled receiving/quarantine và cần reason cùng `Warehouse Manager` approval trước khi release. |
| INB-002 | Receipt line phải lưu expected quantity và actual received quantity riêng; inventory chỉ tăng theo actual quantity đã xác nhận. |
| INB-003 | Short receipt phải giữ disposition rõ cho phần thiếu: `WAIT_REMAINDER`, `BACKORDER_SUPPLIER` hoặc `CLOSE_WITH_SHORTFALL`. |
| INB-004 | Phần over receipt phải được trace/cách ly và cần `Warehouse Manager` approval trước khi release; không sửa expected quantity để che discrepancy. |
| INB-005 | Product, effective UOM conversion, supplier Lot và MFG/EXP phải được validate theo tracking policy; thiếu conversion thì reject line, thiếu Lot/date bắt buộc thì quarantine. |
| INB-006 | Mọi receipt có baseline condition check; `qc_required` hoặc condition/label/date/storage exception phải vào `QC_HOLD/QUARANTINE` chờ inspection. |
| INB-007 | Receipt quantity có condition khác nhau phải được split theo status/disposition nhưng tổng split phải reconcile actual received quantity. |
| INB-008 | Release và put-away là command riêng; put-away phải xác nhận Product/Lot/quantity/destination và post transfer atomic. |
| INB-009 | Receipt command phải idempotent: cùng key/cùng payload trả kết quả gốc; cùng key/khác payload conflict; không post stock trùng. |

## Sales, reservation, và outbound

| ID | Rule |
|---|---|
| OUT-001 | Cam kết bán hàng phải dùng available/ATP policy, không bao giờ dùng raw on-hand quantity. |
| OUT-002 | Nhu cầu đã xác nhận phải tạo active reservation trước khi picking. |
| OUT-003 | Hàng sắp hết hạn đủ điều kiện phải được allocate theo FEFO; receipt time là tie-breaker cho date liên quan bằng nhau/không rõ theo policy. |
| OUT-004 | Mức shelf-life tối thiểu của khách là bộ lọc áp dụng trước FEFO, hỗ trợ minimum remaining days, percent hoặc cả hai; khi dùng cả hai, candidate phải đạt cả hai và percent không được suy đoán khi thiếu MFG/EXP. |
| OUT-005 | Một order line có thể allocate từ nhiều Lot và nhiều location. |
| OUT-006 | FEFO override luôn cần một cấp `Warehouse Manager` approval, lý do, gợi ý gốc và lựa chọn thực tế; override không được làm blocked/expired/ineligible stock trở thành hợp lệ. |
| OUT-007 | Xác nhận picking phải kiểm tra product, Lot, location, và quantity khớp với allocation. |
| OUT-008 | Xác nhận shipment phải ghi nhận stock-out movement và tiêu thụ reservation tương ứng một cách atomic. |
| OUT-009 | Nhu cầu đã xác nhận nhưng không được đáp ứng phải được phân loại rõ: partial, backorder, substitute proposal, rejected, hoặc lost sale. |
| OUT-010 | Trạng thái order, stock, hoặc shipment không rõ sẽ chặn tiếp tục để tránh thao tác không an toàn cho đến khi reconcile xong. |
| OUT-011 | Active reservation không được tự hết hạn âm thầm trong MVP; chỉ shipment, authorized order change/cancellation hoặc audited reconciliation command được tiêu thụ/giảm/giải phóng reservation. |

## Quality, returns, và destruction

| ID | Rule |
|---|---|
| QLT-001 | Stock ở trạng thái `QC_HOLD`, `QUARANTINE`, `DAMAGED`, `EXPIRED`, `RECALLED`, hoặc `DESTROY_PENDING` không được bán hay allocate. |
| QLT-002 | Quality hold có thể scope theo stock segment; Lot-level recall/block phải áp dụng trên mọi location đang giữ Lot. |
| QLT-003 | Quality inspection phải giữ subject quantity/Lot/location/status version, inspector, time, findings, evidence và disposition. |
| QLT-004 | Release/reclassification chỉ áp dụng đúng approved quantity/version bằng inventory operation; inspection một segment không tự release toàn Lot. |
| RET-001 | Hàng khách trả về luôn phải vào trạng thái/location quarantine trước bất kỳ quyết định restock nào. |
| RET-002 | Return record phải giữ nguyên order gốc, shipment, product, Lot, quantity, reason, note và ít nhất một private photo evidence. |
| RET-003 | Restock cần kết quả inspection và disposition đã được duyệt; chỉ nhận hàng không đủ để trả lại availability. |
| RET-004 | Return không tạo manufacturer lot mới, trừ khi một quy trình transformation/repacking đã được ghi nhận yêu cầu một internal traceability unit mới. |
| RET-005 | Return receipt và disposition command phải idempotent; retry không được tạo duplicate on-hand, restock hoặc destruction. |
| DST-001 | Destruction cần product, Lot, quantity, reason/note, requester, independent approver, execution record, và ít nhất một private photo evidence. |
| DST-002 | Số lượng `DESTROYED` là kết quả lịch sử của movement và không còn là on hand. |
| DST-003 | Requester và approver destruction phải khác nhau; approval gắn với đúng request version và quantity. |
| DST-004 | Destruction execution phải idempotent và post đúng một movement effect; quantity khác approved quantity phải được duyệt lại. |

## Delivery

| ID | Rule |
|---|---|
| DEL-001 | Loading phải xác nhận shipment, vehicle/trip, và package/quantity thực tế trước khi rời kho. |
| DEL-002 | Driver có thể báo kết quả delivery nhưng không được trực tiếp sửa inventory balance hoặc allocation. |
| DEL-003 | Delivery bị partial/failed phải ghi riêng số lượng đã giao và số lượng mang về. |
| DEL-004 | Hàng vật lý mang về phải được reconcile vào một return location được kiểm soát trước khi trip được đóng. |
| DEL-005 | POD và evidence cho delivery exception là private và có kiểm soát truy cập. |
| DEL-006 | Loading variance phải chặn departure; trip không được close khi returned quantity hoặc delivery variance chưa reconcile. |
| DEL-007 | Delivery-result command phải idempotent và chỉ được thay đổi delivery state; driver không được trực tiếp mutate inventory/reservation/allocation. |

## Replenishment và forecast

| ID | Rule |
|---|---|
| PLN-001 | Purchase recommendation chỉ là advisory và cần human approval trước khi trở thành purchase order. |
| PLN-002 | Input và formula/version của recommendation phải được lưu để có thể reproduce kết quả. |
| PLN-003 | Receipt đã xác nhận, active reservations, lead time, safety stock, MOQ/case pack, demand đã qualify, và seasonal events là input bắt buộc phải khai báo. |
| PLN-004 | Khoảng thời gian stockout/lost-sale phải được đánh dấu để số bán bằng 0 không tự động bị hiểu là demand bằng 0. |
| PLN-005 | Sự kiện âm lịch/mùa vụ phải dùng solar date theo từng năm và demand window trước sự kiện có thể cấu hình. |
| PLN-006 | ML forecasting không được đẩy lên trước khi các gate về baseline quality, WAPE, bias, và backtesting được định nghĩa và pass. |
| PLN-007 | Khi chưa đủ forward-qualified history, planning phải dùng deterministic min/max, safety stock/reorder policy và human review; manual override giữ recommended/selected value cùng reason. |

## Audit và security

| ID | Rule |
|---|---|
| AUD-001 | Mọi quyết định có đặc quyền phải ghi actor, timestamp, target, prior state, new state, reason, và tham chiếu approval/evidence. |
| AUD-002 | Identity đăng nhập phải là cá nhân được nêu tên; cấm dùng shared accountable-user credentials. |
| AUD-003 | Timestamp nghiệp vụ phải phân biệt thời điểm sự kiện xảy ra với thời điểm nó được ghi nhận. |
| AUD-004 | Transaction, audit, POD, return và destruction evidence không được auto-delete trong policy hiện tại; thay đổi retention/deletion cần CEO final approval, Warehouse Manager review và audit record. |
| AUD-005 | Audit event và posted transaction không được sửa/xóa để đổi nghĩa; correction tạo record mới có link về record gốc. |
| AUD-006 | Privileged command/audit phải giữ correlation, idempotency hoặc operation reference đủ để trace request -> decision -> state effect. |
| SEC-001 | Secret key, database credential, và dữ liệu kinh doanh thật không bao giờ được commit lên public repository. |
| SEC-002 | Browser client không bao giờ nhận database secret/service-role credentials. |
| SEC-003 | Authorization phải được enforce ở server-side và được test xác minh; ẩn UI không phải là authorization. |
| SEC-004 | Private evidence chỉ được truy cập qua server-authorized, record-scoped, short-lived mechanism; metadata link business record và access quan trọng phải audit được. |
| SEC-005 | Least-privilege policy phải giới hạn user/service/job theo role và assigned scope; separation of duty được kiểm tra tại execution time. |
| SEC-006 | Local/test/staging/production tách data và secret; non-production không được dùng production database/evidence data ngoài quy trình sanitized được duyệt. |
