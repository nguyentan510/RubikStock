# Business Rules

## Trạng thái và định danh

Các rule này ở trạng thái `PROPOSED` cho đến khi RUBIK chấp nhận. Rule ID là ổn định và phải được dùng trong test, API, tiêu chí nghiệm thu UI, và traceability matrix.

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
| INV-008 | Chênh lệch physical count phải có lý do và approval policy trước khi post adjustment. |

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

## Sales, reservation, và outbound

| ID | Rule |
|---|---|
| OUT-001 | Cam kết bán hàng phải dùng available/ATP policy, không bao giờ dùng raw on-hand quantity. |
| OUT-002 | Nhu cầu đã xác nhận phải tạo active reservation trước khi picking. |
| OUT-003 | Hàng sắp hết hạn đủ điều kiện phải được allocate theo FEFO; receipt time là tie-breaker cho date liên quan bằng nhau/không rõ theo policy. |
| OUT-004 | Mức shelf-life tối thiểu của khách là một bộ lọc đủ điều kiện được áp dụng trước khi sắp xếp FEFO. |
| OUT-005 | Một order line có thể allocate từ nhiều Lot và nhiều location. |
| OUT-006 | FEFO override cần permission, lý do, gợi ý gốc, lựa chọn thực tế, và approval policy. |
| OUT-007 | Xác nhận picking phải kiểm tra product, Lot, location, và quantity khớp với allocation. |
| OUT-008 | Xác nhận shipment phải ghi nhận stock-out movement và tiêu thụ reservation tương ứng một cách atomic. |
| OUT-009 | Nhu cầu đã xác nhận nhưng không được đáp ứng phải được phân loại rõ: partial, backorder, substitute proposal, rejected, hoặc lost sale. |
| OUT-010 | Trạng thái order, stock, hoặc shipment không rõ sẽ chặn tiếp tục để tránh thao tác không an toàn cho đến khi reconcile xong. |

## Quality, returns, và destruction

| ID | Rule |
|---|---|
| QLT-001 | Stock ở trạng thái `QC_HOLD`, `QUARANTINE`, `DAMAGED`, `EXPIRED`, `RECALLED`, hoặc `DESTROY_PENDING` không được bán hay allocate. |
| RET-001 | Hàng khách trả về luôn phải vào trạng thái/location quarantine trước bất kỳ quyết định restock nào. |
| RET-002 | Return record phải giữ nguyên order gốc, shipment, product, Lot, quantity, reason, và evidence khi có. |
| RET-003 | Restock cần kết quả inspection và disposition đã được duyệt; chỉ nhận hàng không đủ để trả lại availability. |
| RET-004 | Return không tạo manufacturer lot mới, trừ khi một quy trình transformation/repacking đã được ghi nhận yêu cầu một internal traceability unit mới. |
| DST-001 | Destruction cần product, Lot, quantity, reason, requester, independent approver, execution record, và evidence policy. |
| DST-002 | Số lượng `DESTROYED` là kết quả lịch sử của movement và không còn là on hand. |

## Delivery

| ID | Rule |
|---|---|
| DEL-001 | Loading phải xác nhận shipment, vehicle/trip, và package/quantity thực tế trước khi rời kho. |
| DEL-002 | Driver có thể báo kết quả delivery nhưng không được trực tiếp sửa inventory balance hoặc allocation. |
| DEL-003 | Delivery bị partial/failed phải ghi riêng số lượng đã giao và số lượng mang về. |
| DEL-004 | Hàng vật lý mang về phải được reconcile vào một return location được kiểm soát trước khi trip được đóng. |
| DEL-005 | POD và evidence cho delivery exception là private và có kiểm soát truy cập. |

## Replenishment và forecast

| ID | Rule |
|---|---|
| PLN-001 | Purchase recommendation chỉ là advisory và cần human approval trước khi trở thành purchase order. |
| PLN-002 | Input và formula/version của recommendation phải được lưu để có thể reproduce kết quả. |
| PLN-003 | Receipt đã xác nhận, active reservations, lead time, safety stock, MOQ/case pack, demand đã qualify, và seasonal events là input bắt buộc phải khai báo. |
| PLN-004 | Khoảng thời gian stockout/lost-sale phải được đánh dấu để số bán bằng 0 không tự động bị hiểu là demand bằng 0. |
| PLN-005 | Sự kiện âm lịch/mùa vụ phải dùng solar date theo từng năm và demand window trước sự kiện có thể cấu hình. |
| PLN-006 | ML forecasting không được đẩy lên trước khi các gate về baseline quality, WAPE, bias, và backtesting được định nghĩa và pass. |

## Audit và security

| ID | Rule |
|---|---|
| AUD-001 | Mọi quyết định có đặc quyền phải ghi actor, timestamp, target, prior state, new state, reason, và tham chiếu approval/evidence. |
| AUD-002 | Identity đăng nhập phải là cá nhân được nêu tên; cấm dùng shared accountable-user credentials. |
| AUD-003 | Timestamp nghiệp vụ phải phân biệt thời điểm sự kiện xảy ra với thời điểm nó được ghi nhận. |
| SEC-001 | Secret key, database credential, và dữ liệu kinh doanh thật không bao giờ được commit lên public repository. |
| SEC-002 | Browser client không bao giờ nhận database secret/service-role credentials. |
| SEC-003 | Authorization phải được enforce ở server-side và được test xác minh; ẩn UI không phải là authorization. |
