# M6 Roadmap - Company Delivery

- Status: `PLANNED`
- Depends on: M4 shipment và M5 controlled returns
- Unlocks: Closed-loop order fulfillment và qualified delivery history

## Outcome

Quản lý chuyến xe nội bộ từ loading tới POD và reconcile hàng giao thiếu/thất bại/mang về mà driver không thể sửa trực tiếp inventory.

## Accepted D0 inputs

- Một order có thể giao nhiều đợt và nhiều chuyến.
- Mỗi shipment/trip phải có reconciliation riêng.
- Partial delivery và backorder là behavior bắt buộc.
- Driver/coordinator dùng mobile/PC theo online-first MVP.

## Work packages

| ID | Nội dung | Deliverables | Verification |
|---|---|---|---|
| M6.1 | Fleet master | Vehicle, driver assignment và active status | Authorization tests |
| M6.2 | Trip planning | Trip, stops, shipment assignment, sequence | State/uniqueness tests |
| M6.3 | Loading control | Scan/confirm shipment-package-quantity-trip | Mismatch tests |
| M6.4 | Dispatch | Ready/departed controls và handoff evidence | Transition tests |
| M6.5 | Stop outcome/POD | Delivered, partial, failed, reason, private evidence | Access/audit tests |
| M6.6 | Return-to-warehouse | Returned quantity vào controlled return location | Inventory boundary tests |
| M6.7 | Trip reconciliation | Loaded = delivered + returned + approved variance | Conservation tests |
| M6.8 | Driver/dispatcher UI | Mobile stop flow và reconciliation console | Role workflow tests |
| M6.9 | Route-day rehearsal | Multiple stops, partial/failed delivery | Runtime rehearsal |
| M6.10 | M6 gate | Shipment-to-POD/return evidence pack | Gate M6 pass |

## Invariants bắt buộc

- Áp dụng `DEL-001..005`.
- Driver ghi outcome nhưng không update balance/allocation trực tiếp.
- Hàng mang về chưa reconcile không trở thành available.
- Trip không đóng nếu conservation equation chưa khớp hoặc chưa có approved variance.
- POD và evidence là private objects có access control.

## Exit gate

- Loading mismatch bị chặn.
- Partial/failed deliveries reconcile quantity chính xác.
- Hàng mang về đi vào return/quarantine workflow phù hợp.
- Trace từ shipment tới trip, stop, POD và return hoàn chỉnh.
