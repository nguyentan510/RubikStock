# Domain Glossary

| Thuật ngữ | Nghĩa chuẩn |
|---|---|
| SKU | Mã sản phẩm ổn định được RUBIK sử dụng. Biến thể bao bì có thể cần SKU bán riêng hoặc UOM conversion rõ ràng. |
| Product | Danh tính hàng hóa thương mại, tách biệt với một Lot hay location cụ thể. |
| UOM | Unit of measure như case, bag, bottle, kg, hoặc gram. |
| Base UOM | Đơn vị được dùng để lưu và tính stock cho một product. |
| Lot | Lô sản xuất/nhà cung cấp có thể trace được của một product. |
| Supplier lot | Mã Lot do nhà sản xuất hoặc nhà cung cấp in/cung cấp. |
| Internal lot code | Mã nội bộ của RUBIK, dùng mà không thay thế Supplier lot. |
| MFG | Manufacture date khi áp dụng. |
| EXP | Expiry/best-before date khi áp dụng. |
| FEFO | First Expired, First Out: lô có expiry sớm hơn và còn đủ điều kiện được ưu tiên trước. |
| FIFO | First In, First Out: receipt cũ hơn được dùng làm tie-breaker hoặc cho hàng không có expiry. |
| On hand | Số lượng vật lý được phản ánh trong inventory ledger, bao gồm cả status bị chặn. |
| Eligible on hand | Số lượng on-hand ở status cho phép cho nghiệp vụ yêu cầu. |
| Reservation | Số lượng đã cam kết cho nhu cầu đã xác nhận nhưng chưa ship. |
| Available | Eligible on-hand trừ đi reservation đang hoạt động. |
| Allocation | Việc chọn một hoặc nhiều quantity từ lot/location đủ điều kiện cho một order line. |
| Quarantine | Hàng được tách khỏi bán hàng để chờ inspection hoặc quyết định. |
| Put-away | Di chuyển hàng từ receiving/QC vào location lưu trữ đã phân bổ. |
| Picking | Lấy hàng thực tế từ kho theo allocation để fulfillment. |
| Staging | Khu vực kiểm soát để giữ hàng đã pick trước khi loading/shipment. |
| POD | Proof of delivery: chữ ký, ảnh, timestamp, hoặc evidence tương đương. |
| Return authorization | Yêu cầu đã duyệt, khi có thể thì link hàng trả về shipment gốc. |
| Disposition | Quyết định restock, rework/repack, return to supplier, destroy, hoặc investigate. |
| Stock adjustment | Movement đã duyệt để sửa sai lệch đã xác minh; không bao giờ overwrite balance trực tiếp. |
| ATP | Available to Promise: stock và các receipt đủ chắc chắn để cam kết cho khách theo policy. |
| Safety stock | Lượng đệm để hấp thụ biến động demand/lead time. |
| Lead time | Thời gian dự kiến từ purchase đã duyệt đến receipt có thể dùng. |
| Lost sale | Nhu cầu khách đã xác nhận nhưng không được đáp ứng vì supply không có và khách không chờ. |
| WAPE | Weighted Absolute Percentage Error dùng để đánh giá sai số forecast tổng hợp. |
| Forecast bias | Xu hướng over-forecast hoặc under-forecast kéo dài. |
