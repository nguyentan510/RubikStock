# M7 Roadmap - Explainable Replenishment and Seasonality

- Status: `PLANNED`
- Depends on: Qualified inventory, receipt, sales, stockout và lead-time history từ M2-M6
- Unlocks: Purchase recommendation có thể kiểm chứng

## Outcome

Đề xuất nhập hàng có thể giải thích và reproduce từ demand đã qualify, stock position, lead time, safety stock, MOQ/case pack và seasonal/lunar events; quyết định mua vẫn do con người duyệt.

## Accepted D0 input

- Không import legacy sales history.
- RubikStock bắt đầu capture sales/fulfillment/stockout/lost-sale theo format chuẩn từ clean-start date.
- M7 chỉ dùng forward-qualified history; trước khi đủ data gate, replenishment dùng min/max, safety stock và human review thay vì forecast claim.

## Work packages

| ID | Nội dung | Deliverables | Verification |
|---|---|---|---|
| M7.1 | History qualification | Sales/stockout/lost-sale/receipt quality report | Data-quality gate |
| M7.2 | Planning inputs | Lead time, safety stock, MOQ, case pack, service policy | Validation tests |
| M7.3 | Event calendar | Solar dates, lunar-event mapping per year, demand windows | Calendar boundary tests |
| M7.4 | Baseline demand | Moving/seasonal baseline with explicit version | Backtest reproducibility |
| M7.5 | Recommendation formula | On-hand, reservation, inbound, demand, safety stock | Formula unit tests |
| M7.6 | Versioned planning run | Input snapshot, formula version, output, timestamp | Re-run equality tests |
| M7.7 | Review/override | Human approve/reject/adjust with reason and audit | Permission/audit tests |
| M7.8 | Planning UI/report | Explanation, risk flags, WAPE/bias, event context | User review scenarios |
| M7.9 | Shadow run | So sánh recommendation với quyết định thực tế | Bounded evaluation report |
| M7.10 | M7 gate | Reproducibility/quality evidence pack | Gate M7 pass |

## Thứ tự triển khai

`M7.1 -> M7.2 -> M7.3 -> M7.4 -> M7.5 -> M7.6 -> M7.7 -> M7.8 -> M7.9 -> M7.10`.

## Guardrails

- Áp dụng `PLN-001..007`.
- Sales bằng 0 trong stockout window không tự động bằng demand bằng 0.
- Lunar event phải map sang solar date riêng cho từng năm.
- Recommendation không tự tạo/approve purchase order.
- ML chỉ được mở như experiment sau khi baseline/WAPE/bias/backtest đã có.

## Exit gate

- Kết quả reproduce được từ input/version đã lưu.
- Data-quality và stockout treatment rõ ràng.
- Baseline metrics được báo cáo theo SKU/segment phù hợp.
- Override có actor/reason/audit.
