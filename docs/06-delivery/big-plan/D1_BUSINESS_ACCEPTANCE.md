# D1 Business Contract Acceptance

- Status: `COMPLETED`
- Started: 2026-08-03
- Depends on: D0 `ACCEPTED`
- Business decision owner: `Quản lý Kho`
- Source rules: [`../../01-business/BUSINESS_RULES.md`](../../01-business/BUSINESS_RULES.md)
- Scenario pack: [`../../07-testing/BUSINESS_SCENARIOS.md`](../../07-testing/BUSINESS_SCENARIOS.md)

## Mục tiêu

Review rule, state, approval và scenario trước khi tạo domain schema/code. D1 acceptance chỉ chấp nhận business semantics; không tuyên bố implementation, migration hoặc runtime đã tồn tại.

## Cách review

| Batch | Work packages | Chủ đề | Status |
|---|---|---|---|
| A | D1.1-D1.2 | Inventory truth, Lot, UOM, package break/measured sale | `ACCEPTED` |
| B | D1.3 | Inbound, discrepancy, QC, put-away | `ACCEPTED` |
| C | D1.4 | Order, reservation, shelf-life, FEFO, picking, shipment | `ACCEPTED` |
| D | D1.5-D1.6 | Return, quality, destruction, delivery reconciliation | `ACCEPTED` |
| E | D1.6-D1.8 | Planning boundary, audit/security, conceptual model | `ACCEPTED` |
| Final | D1.9 | Cross-document review và business sign-off | `ACCEPTED` |

Một batch chỉ chuyển `ACCEPTED` khi business owner xác nhận rõ. Thay đổi policy phải cập nhật rule/scenario tương ứng trước khi batch được chấp nhận.

## Batch A - Inventory, Lot và UOM

### Contract đề nghị chấp nhận

1. Mọi stock change được post dưới một `inventory_operation` chứa một hoặc nhiều immutable `inventory_movement`; balance chỉ là projection có thể rebuild.
2. Confirmed balance không âm. Operation nhiều leg phải atomic; transfer bảo toàn normalized quantity.
3. Stock scope tối thiểu gồm warehouse, location, product, Lot khi product có date/Lot tracking và inventory status.
4. Mỗi product có một base inventory UOM. Movement giữ cả entered quantity/UOM và exact normalized base quantity; không dùng floating point.
5. Conversion theo product có version/effective date; conversion mới không diễn giải lại movement cũ.
6. Product chỉ được break case hoặc measured sale khi policy cho phép. Open/repack giữ genealogy về supplier Lot/package gốc.
7. F&B thiếu Lot/EXP bắt buộc fail closed vào `QUARANTINE`; không tự sinh hoặc suy đoán supplier Lot/MFG/EXP.
8. Posted movement không sửa/xóa. Sai sót dùng reversal + replacement có liên kết audit.
9. Physical-count variance cần recount/reason và một cấp `Quản lý Kho` approve; requester khác approver.

### Scenario nghiệm thu Batch A

| ID | Given/When | Kết quả bắt buộc |
|---|---|---|
| D1-A01 | Nhận 10 case, conversion 12 bottle/case | Lưu entered `10 case`, normalized `120 bottle`, cùng Product/Lot/location/status |
| D1-A02 | Mở bao 25 kg và bán 750 g với product cho phép measured sale | Trừ chính xác `750 g`; phần còn lại và operation trace về supplier Lot/package gốc |
| D1-A03 | Receipt F&B thuộc `LOT_EXP_REQUIRED` nhưng EXP không xác minh được | Stock chỉ vào `QUARANTINE`, không vào `AVAILABLE` |
| D1-A04 | Transfer 20 base units giữa hai location | Source -20 và destination +20 cùng operation/transaction; không có partial post |
| D1-A05 | Hai request đồng thời cùng làm confirmed balance âm | Tối đa request hợp lệ được commit; request còn lại fail mà không tạo partial movement |
| D1-A06 | Phát hiện posted receipt sai quantity | Không edit movement cũ; post reversal và replacement có audit link |
| D1-A07 | Physical count thấp hơn system | Recount + reason + approver khác requester trước `COUNT_ADJUSTMENT_OUT` |
| D1-A08 | Đổi conversion case sau khi đã có movement lịch sử | Movement cũ giữ normalized quantity/version ban đầu; chỉ transaction effective sau dùng conversion mới |

### Traceability của Batch A

- Rules: `INV-001..008`, `LOT-001..006`, `UOM-001..004`.
- Existing scenarios: `SCN-001`, `SCN-002`, `SCN-013`, `SCN-016`.
- Data contracts: [`../../03-data/INVENTORY_LEDGER.md`](../../03-data/INVENTORY_LEDGER.md), [`../../03-data/UOM_CONVERSION.md`](../../03-data/UOM_CONVERSION.md), [`../../03-data/LOT_TRACEABILITY.md`](../../03-data/LOT_TRACEABILITY.md).
- Downstream: M1 product/UOM/Lot master và M2 ledger/opening balance.

### Decision record Batch A

| Field | Value |
|---|---|
| Decision | `ACCEPTED` |
| Approver | `Quản lý Kho` |
| Date | 2026-08-03 |
| Accepted scope | 9 contract points và 8 scenarios `D1-A01..D1-A08` |

## Batch B - Inbound, discrepancy, QC và put-away

### Contract đề nghị chấp nhận

1. Receipt nên tham chiếu approved Purchase Order khi có. Hàng đến không có PO vẫn được nhận vật lý vào `RECEIVING/QUARANTINE`, nhưng cần reason và `Quản lý Kho` approve trước khi release thành `AVAILABLE`.
2. Receipt line luôn lưu expected quantity và actual received quantity riêng biệt; inventory chỉ tăng theo actual quantity đã xác nhận.
3. Short receipt được ghi nhận theo actual quantity; phần thiếu phải được chọn rõ `WAIT_REMAINDER`, `BACKORDER_SUPPLIER` hoặc `CLOSE_WITH_SHORTFALL` thay vì tự coi là đã nhận đủ.
4. Over receipt được cách ly phần vượt và cần `Quản lý Kho` approve trước khi release; không sửa PO hoặc expected quantity để che discrepancy.
5. Mỗi receipt line phải validate Product, effective UOM conversion, supplier Lot và MFG/EXP theo tracking policy. Thiếu conversion thì reject line; thiếu Lot/date bắt buộc thì nhận vào `QUARANTINE`.
6. Baseline condition check áp dụng cho mọi receipt. Product có `qc_required=true` hoặc có dấu hiệu hỏng, sai nhãn, sai date, nhiệt độ/bảo quản bất thường phải vào `QC_HOLD/QUARANTINE` chờ inspection.
7. Receipt có thể split quantity theo condition/status: phần đạt giữ luồng release, phần hỏng/không rõ bị cách ly; không block hoặc release toàn dòng bằng suy đoán.
8. Release và put-away là command riêng. Chỉ quantity đủ điều kiện mới chuyển sang `AVAILABLE`; put-away phải xác nhận đúng Product/Lot/quantity/destination location và post movement atomic.
9. Receipt command có idempotency key/reference ổn định. Retry cùng payload trả kết quả cũ; cùng key khác payload trả conflict; không post duplicate stock.

### Scenario nghiệm thu Batch B

| ID | Given/When | Kết quả bắt buộc |
|---|---|---|
| D1-B01 | PO 100 case, nhận đủ 100 case hợp lệ | Receipt lưu expected/actual 100; normalized quantity đúng; eligible quantity được release rồi put-away |
| D1-B02 | PO 100 case, thực nhận 80 case | Chỉ 80 tăng stock; 20 còn lại có disposition `WAIT_REMAINDER`, `BACKORDER_SUPPLIER` hoặc `CLOSE_WITH_SHORTFALL` |
| D1-B03 | PO 100 case, supplier giao 105 case | 100 và phần vượt 5 được trace riêng; phần vượt chưa `AVAILABLE` trước manager approval |
| D1-B04 | Hàng tới không có PO | Có thể ghi nhận custody vào `RECEIVING/QUARANTINE`; bắt buộc reason và approval trước release |
| D1-B05 | UOM hợp lệ nhưng thiếu EXP bắt buộc | Line được normalize nhưng quantity chỉ ở `QUARANTINE`; không available |
| D1-B06 | 50 package gồm 47 tốt và 3 hỏng | Split 47 eligible và 3 `DAMAGED/QUARANTINE`; tổng actual vẫn reconcile 50 |
| D1-B07 | Client retry receipt sau timeout với cùng idempotency key | Trả receipt gốc và không tạo movement/balance lần hai |
| D1-B08 | Put-away scan đúng Product nhưng sai Lot hoặc destination | Reject confirmation; stock giữ ở receiving location cho tới khi reconcile |

### Traceability của Batch B

- Proposed rules: `INB-001..009`.
- Existing exceptions: `EX-001`, `EX-002`, `EX-003`.
- Existing state: Purchase Order/Receipt và inventory status trong [`../../01-business/STATE_MACHINES.md`](../../01-business/STATE_MACHINES.md).
- Downstream: M3 receipt command, discrepancy, QC, put-away và inbound pilot.

### Decision record Batch B

| Field | Value |
|---|---|
| Decision | `ACCEPTED` |
| Approver | `Quản lý Kho` |
| Date | 2026-08-03 |
| Accepted scope | 9 contract points và 8 scenarios `D1-B01..D1-B08` |

## Batch C - Order, reservation, shelf-life, FEFO, picking và shipment

### Contract đề nghị chấp nhận

1. Sales có thể tạo/sửa order ở `DRAFT`. Sau `CONFIRMED`, RubikStock là operational order truth; thay đổi quantity/customer/date phải dùng controlled command và audit.
2. Confirmed demand chỉ cam kết từ `available`, không dùng raw on-hand. Quantity đủ điều kiện phải được reserve atomic trước picking; backorder quantity không giả lập reservation trên stock chưa có.
3. Active reservation không tự hết hạn âm thầm trong MVP. Nó chỉ được giảm/giải phóng khi shipment tiêu thụ, order/line bị hủy hoặc giảm có authorization, hoặc reconciliation command được audit.
4. Customer shelf-life eligibility được áp dụng tại planned delivery date trước FEFO. Policy hỗ trợ days, percent hoặc cả hai; khi có cả hai thì dùng `AND`, thiếu MFG cần cho percent thì Lot không đủ điều kiện.
5. Trong candidate đủ điều kiện, allocation theo EXP sớm nhất; receipt time là tie-breaker, sau đó mới đến pick/location preference. Một order line có thể split nhiều Lot/location.
6. FEFO override luôn cần reason và một cấp `Quản lý Kho` approve; lưu suggested allocation và selected allocation. Override không hợp thức hóa blocked, expired, recalled hoặc shelf-life-ineligible stock.
7. Picking phải xác nhận Product, Lot, source location và quantity theo allocation. Mismatch bị reject; short pick đi qua recount/reallocate/adjustment workflow, không tự sửa balance.
8. Lot bị block/recall/expired sau allocation nhưng trước shipment phải vô hiệu candidate, chặn pick/shipment và yêu cầu reallocation/reconciliation.
9. Một order có thể có nhiều shipment/trip. Mỗi shipment tiêu thụ đúng reserved quantity của chính nó; remaining confirmed quantity được giữ reservation hoặc backorder theo decision rõ ràng.
10. Shipment confirmation post stock-out movement và consume reservation trong cùng transaction, có idempotency key; retry không tạo duplicate shipment/movement.
11. Khi outcome của reserve/pick/shipment là unknown do timeout hoặc state mismatch, hệ thống fail closed và tra cứu bằng idempotency key/reconcile trước khi cho command mới.

### Scenario nghiệm thu Batch C

| ID | Given/When | Kết quả bắt buộc |
|---|---|---|
| D1-C01 | Order 100 units được confirm khi available đúng 100 | Reserve atomic 100; available-to-promise còn 0, on-hand chưa giảm trước shipment |
| D1-C02 | Hai order đồng thời cùng reserve 100 units cuối | Tổng reservation thành công tối đa 100; request còn lại partial/backorder/reject theo decision |
| D1-C03 | Customer yêu cầu còn tối thiểu 90 ngày, Lot gần nhất chỉ còn 60 ngày | Loại Lot 60 ngày trước FEFO; không cần override để dùng Lot đủ điều kiện kế tiếp |
| D1-C04 | Policy yêu cầu cả 90 ngày và 60%, Lot đạt ngày nhưng thiếu MFG | Candidate không đủ điều kiện vì không tính được percent |
| D1-C05 | Lot FEFO đủ điều kiện còn 4, Lot kế còn 6, demand 10 | Allocation tạo hai dòng 4+6 và giữ thứ tự gợi ý |
| D1-C06 | Sales yêu cầu Lot mới hơn dù Lot cũ vẫn đủ điều kiện | Chờ manager approval, lưu reason/suggested/selected; shipment chưa được dùng override chưa duyệt |
| D1-C07 | Operator scan đúng Product nhưng sai Lot/location | Reject pick confirmation; không đổi allocation hay balance âm thầm |
| D1-C08 | Lot đã allocate bị recall trước shipment | Chặn pick/shipment, release/invalidate allocation có audit rồi reallocate từ candidate hợp lệ |
| D1-C09 | Order 100 giao hai shipment 60 và 40 | Mỗi shipment consume reservation/stock đúng một lần; order chỉ close khi toàn bộ quantity có disposition |
| D1-C10 | Shipment 60 bị retry sau timeout cùng idempotency key | Trả kết quả gốc; chỉ có một shipment confirmation và một stock-out effect |
| D1-C11 | Request timeout, client không biết reserve đã commit hay chưa | Không retry bằng key mới; lookup/reconcile outcome trước command tiếp theo |

### Traceability của Batch C

- Proposed rules: `OUT-001..011`.
- Existing exceptions: `EX-004..008`, `EX-017`.
- Existing scenarios: `SCN-003..007`, `SCN-012`.
- Data contract: [`../../03-data/SHELF_LIFE_POLICY.md`](../../03-data/SHELF_LIFE_POLICY.md), reservation/allocation aggregates trong [`../../03-data/DATA_MODEL.md`](../../03-data/DATA_MODEL.md).
- Downstream: M4 reservation/FEFO/outbound và M6 multi-shipment delivery.

### Decision record Batch C

| Field | Value |
|---|---|
| Decision | `ACCEPTED` |
| Approver | `Quản lý Kho` |
| Date | 2026-08-03 |
| Accepted scope | 11 contract points và 11 scenarios `D1-C01..D1-C11` |

## Batch D - Quality, return, destruction và delivery reconciliation

### Contract đề nghị chấp nhận

1. Stock ở `QC_HOLD`, `QUARANTINE`, `DAMAGED`, `EXPIRED`, `RECALLED` hoặc `DESTROY_PENDING` không được reserve, allocate, pick hoặc ship. Hold có thể áp dụng theo stock segment; recall/block cấp Lot áp dụng trên mọi location.
2. Quality inspection phải lưu subject quantity/Lot/location/status version, inspector, occurred/recorded time, findings, note/evidence và disposition. Chỉ accepted disposition mới được release/reclassify stock.
3. Release khỏi hold phải chuyển đúng approved quantity/status bằng inventory operation; không đổi toàn bộ Lot khi inspection chỉ bao phủ một segment.
4. Customer return luôn được nhận vào controlled return location với `QUARANTINE`, kể cả bao bì còn nguyên. Return phải link order/shipment/Product/Lot gốc khi xác định được, lưu reason, note và ít nhất một private photo.
5. Return không trace được shipment/Lot vẫn được ghi nhận custody nhưng fail closed trong `INVESTIGATION_HOLD`; không tự tạo supplier/manufacturer Lot hoặc restock.
6. Restock cần inspection và disposition approval cho đúng quantity/version. `RETURN_TO_AVAILABLE` post đúng một lần; chỉ nhận hàng hoặc chụp ảnh không làm available tăng.
7. Return receipt/disposition command phải idempotent; retry không tạo duplicate on-hand, restock hoặc destruction.
8. Destruction cần requester khác approver, reason/note, Product/Lot/quantity, ít nhất một private photo, execution record và verification. Approval gắn với đúng request version/quantity.
9. Destruction execution post `DESTRUCTION` movement đúng một lần; quantity chuyển khỏi on-hand và history không được xóa. Quantity khác approved quantity phải quay lại approval.
10. Loading phải xác nhận shipment, Product/package/quantity, vehicle và trip trước departure. Loading variance chặn xe rời kho cho tới khi reconcile.
11. Driver chỉ ghi delivery result/POD/reason theo stop được giao; không được trực tiếp sửa balance, reservation hoặc allocation.
12. Partial/failed delivery phải tách delivered quantity và returned quantity. Hàng mang về vẫn thuộc controlled custody cho tới khi nhận vào return location/quarantine và reconcile.
13. Trip chỉ được `CLOSED` sau khi mọi stop có disposition, returned quantity/variance đã reconcile và private POD/exception evidence được link đúng shipment.

### Scenario nghiệm thu Batch D

| ID | Given/When | Kết quả bắt buộc |
|---|---|---|
| D1-D01 | Một segment của Lot đang `QC_HOLD` | Segment đó không xuất hiện trong available/allocation; segment available khác không bị block nếu không có Lot-level hold |
| D1-D02 | Supplier recall toàn Lot đang nằm ở ba location và có allocation | Block allocation/pick/shipment trên cả ba location; quantity không tự biến mất khỏi on-hand history |
| D1-D03 | Inspection chỉ approve 40/50 units trong quarantine | Chỉ 40 được `RETURN_TO_AVAILABLE`; 10 còn lại giữ hold/disposition riêng |
| D1-D04 | Khách trả 10 units còn nguyên bao bì | Nhận đủ 10 vào return quarantine, link shipment/Lot, photo+note; available chưa tăng |
| D1-D05 | Return không xác định được Lot | Nhận custody vào `INVESTIGATION_HOLD`; không tạo Lot giả hoặc restock |
| D1-D06 | Restock command retry sau timeout | Cùng idempotency key trả result gốc; available chỉ tăng một lần |
| D1-D07 | Requester destruction cố tự approve | Authorization từ chối; request vẫn chưa đủ điều kiện execute |
| D1-D08 | Approved destruction 20 units nhưng execution nhập 22 | Không post movement; yêu cầu sửa request/re-approval cho quantity mới |
| D1-D09 | Destruction 20 units được retry | Chỉ một `DESTRUCTION` movement; on-hand giảm đúng 20 và evidence/history còn nguyên |
| D1-D10 | Loading quantity lệch shipment | Chặn `DEPARTED`; loader/coordinator phải sửa/reconcile trước khi xe rời kho |
| D1-D11 | Shipment 100 chỉ giao 80, mang về 20 | Ghi delivered 80/returned 20; 20 vào return quarantine trước khi trip close |
| D1-D12 | Driver báo failed delivery nhưng hàng chưa về kho | Shipment/returned custody chưa available; trip không close cho tới receipt/reconciliation |
| D1-D13 | Driver thử cập nhật trực tiếp inventory | Server-side authorization từ chối; chỉ delivery result command được phép |

### Traceability của Batch D

- Proposed rules: `QLT-001..004`, `RET-001..005`, `DST-001..004`, `DEL-001..007`.
- Existing exceptions: `EX-009..013`.
- Existing scenarios: `SCN-007..011`, `SCN-016`.
- State contracts: inventory status, customer return, destruction, trip/stop trong [`../../01-business/STATE_MACHINES.md`](../../01-business/STATE_MACHINES.md).
- Downstream: M5 quality/exceptions và M6 delivery reconciliation.

### Decision record Batch D

| Field | Value |
|---|---|
| Decision | `ACCEPTED` |
| Approver | `Quản lý Kho` |
| Date | 2026-08-03 |
| Accepted scope | 13 contract points và 13 scenarios `D1-D01..D1-D13` |

## Batch E - Planning, audit/security và conceptual ownership

### Contract đề nghị chấp nhận

1. Replenishment/forecast output chỉ là advisory recommendation. Nó không tự tạo Purchase Order, không thay đổi stock và cần authorized human approval trước khi trở thành purchasing action.
2. Mỗi planning run phải lưu input snapshot/version, formula/model version, parameters, business date, run ID và result để reproduce được.
3. Input planning tối thiểu gồm eligible on-hand, active reservations/backorders, confirmed inbound, lead time, safety stock, MOQ/case pack, qualified demand và seasonal events. Thiếu input phải flag confidence/block thay vì bịa giá trị.
4. Sales bằng 0 trong known stockout/lost-sale window được xem là censored demand, không tự động hiểu là demand bằng 0.
5. Sự kiện âm lịch/mùa vụ được materialize thành solar date/window theo từng năm, có source/version; không cộng/trừ ngày thủ công không trace được.
6. Khi chưa đủ forward-qualified history, hệ thống dùng deterministic min/max, safety stock, reorder point và human review. ML chỉ được mở sau accepted backtest/WAPE/bias gate.
7. Manual planning override cần owner, reason, prior/recommended value, selected value và audit; override không viết lại planning run gốc.
8. Mọi accountable action dùng named identity. Shared accountable-user credential bị cấm; service/job identity phải riêng và scope rõ.
9. Privileged command/decision phải audit actor, target, prior/new state, occurred/recorded time, reason, approval/evidence, correlation và idempotency/operation reference.
10. Audit event và posted transaction không sửa/xóa để đổi nghĩa. Correction tạo event/operation mới có link; retention hiện tại không auto-delete, thay đổi cần CEO final approval và `Quản lý Kho` review.
11. Authorization được enforce server-side theo least privilege. UI visibility không phải permission; driver chỉ truy cập trip/stop/evidence được giao, requester/approver separation được kiểm tra tại execution time.
12. Secret, database/admin credential và business data thật không vào public repository/browser/log. Local/test chỉ dùng fake deterministic data; staging dùng synthetic/sanitized data.
13. Private evidence file chỉ truy cập qua server-authorized, record-scoped, short-lived mechanism; metadata phải link business record và audit access quan trọng.
14. Module ownership phải đơn nghĩa: Inventory sở hữu movement/balance/reservation invariants; Inbound/Outbound/Quality/Delivery gửi business command qua application service, không update balance trực tiếp.
15. Cross-aggregate command ảnh hưởng stock phải có một transaction boundary rõ. External integration failure, planning result hoặc delivery UI không được tạo partial inventory effect.
16. RubikStock là operational source cho order/fulfillment/inventory; MISA là financial/invoice source. Integration deferred không được làm domain model phụ thuộc MISA ID hoặc cho MISA ghi đè stock truth.

### Conceptual ownership đề nghị

| Owner module | State sở hữu | Consumer không được làm gì |
|---|---|---|
| Catalog | Product, UOM conversion, Lot policy, partner policy | Không post movement |
| Inventory | Operation, movement, balance projection, reservation invariant | Không tự quyết FEFO/customer policy |
| Inbound | PO reference, receipt, discrepancy, QC entry, put-away command | Không update balance trực tiếp |
| Outbound | Order, allocation, pick, shipment orchestration | Không bypass Inventory posting/eligibility |
| Quality | Hold, inspection, return, disposition, destruction approval/execution | Không sửa movement lịch sử |
| Delivery | Trip, stop, loading, delivery result, POD | Driver/UI không mutate inventory |
| Planning | Versioned run và advisory recommendation | Không tạo PO/stock command tự động |
| Identity/Audit | Identity, permission decision và append-only audit event | Không thay domain state ngoài authorized command |

### Scenario nghiệm thu Batch E

| ID | Given/When | Kết quả bắt buộc |
|---|---|---|
| D1-E01 | Safety stock bị vi phạm và system sinh recommendation 100 cases | Recommendation ở trạng thái advisory; không có PO hoặc stock movement tự sinh |
| D1-E02 | Chạy lại cùng input snapshot/formula/parameters | Kết quả reproduce được hoặc có deterministic explanation cho controlled randomness/version |
| D1-E03 | Sales bằng 0 trong 10 ngày nhưng stockout flag active | Demand được flag censored; planning không học trực tiếp 0 như nhu cầu thật |
| D1-E04 | Trung thu của hai năm có solar date khác nhau | Mỗi năm dùng event window/version riêng và run lưu đúng event input |
| D1-E05 | Chỉ có hai tháng forward-qualified history | ML bị khóa; deterministic reorder policy + human review vẫn hoạt động |
| D1-E06 | Planner override recommendation từ 100 xuống 70 | Lưu recommended 100, selected 70, actor/reason; run gốc không bị sửa |
| D1-E07 | Hai nhân viên dùng chung một accountable login | Policy từ chối onboarding/operation; mỗi người cần named identity |
| D1-E08 | User không có manager role approve FEFO/adjustment/destruction | Server từ chối dù UI/API payload được sửa thủ công |
| D1-E09 | Stock command thành công | Audit link được actor, approval, operation, movement, prior/new state và request correlation |
| D1-E10 | Admin cố xóa audit/evidence theo thao tác thường | Bị từ chối; không có auto-delete path ngoài policy change đã duyệt/audit |
| D1-E11 | Driver truy cập POD của trip không được giao | Server từ chối; không trả signed/private file access |
| D1-E12 | Test/preview environment cố dùng production database URL | Environment/security gate fail closed |
| D1-E13 | Delivery result partial được ghi nhận | Delivery module lưu result; inventory chỉ thay đổi qua controlled return/reconciliation command |
| D1-E14 | Planning job hoặc MISA connector lỗi giữa chừng | Không tạo partial inventory effect; retry/reconcile theo run/idempotency identity |
| D1-E15 | Balance projection bị mất/corrupt trong test | Rebuild từ immutable ledger cho cùng scoped result hoặc reconciliation gate fail |
| D1-E16 | Private evidence URL hết hạn hoặc user mất quyền | Access bị từ chối mà file metadata/business record vẫn toàn vẹn |

### Traceability của Batch E

- Proposed rules: `PLN-001..007`, `AUD-001..006`, `SEC-001..006`.
- Existing exceptions/scenarios: `EX-015..017`, `SCN-014..016`.
- Architecture/data contracts: module boundaries, security model, conceptual data model, retention policy.
- Downstream: D2 auth/RBAC/private files/audit, M7 planning và D1.9 final cross-document sign-off.

### Decision record Batch E

| Field | Value |
|---|---|
| Decision | `ACCEPTED` |
| Approver | `Quản lý Kho` |
| Date | 2026-08-03 |
| Accepted scope | 16 contract points, ownership table và 16 scenarios `D1-E01..D1-E16` |

## Final D1.9 review

Batch A-E đã accepted. Cross-document consistency và final sign-off được tổng hợp tại [`D1_FINAL_ACCEPTANCE.md`](D1_FINAL_ACCEPTANCE.md).

## D1 exit gate

- [x] Batch A-E đều có accepted decision record.
- [x] Rule/state/approval không còn conflict chưa có disposition trong D1 review scope.
- [x] Conceptual model hỗ trợ các scenario đã accepted.
- [x] Final D1.9 sign-off được `Quản lý Kho` xác nhận ngày 2026-08-03.
