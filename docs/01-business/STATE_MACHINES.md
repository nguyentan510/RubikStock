# State Machines

## Quy tắc chung

- Transition là các command rõ ràng có authorization và audit record.
- Transition không hợp lệ phải fail mà không làm stock biến đổi một phần.
- Cancellation sau khi stock đã movement phải dùng quy trình compensating/reversal.
- `occurred_at` và `recorded_at` phải được giữ nguyên.

## Sales order

```text
DRAFT -> CONFIRMED -> RESERVED -> ALLOCATED -> PICKING -> STAGED
      -> LOADED -> SHIPPED -> DELIVERED -> CLOSED
```

Nhánh cho phép:

- `CONFIRMED/RESERVED/ALLOCATED -> PARTIALLY_ALLOCATED`
- `SHIPPED -> PARTIALLY_DELIVERED`
- Trạng thái trước shipment đủ điều kiện có thể sang `CANCELLED` sau khi giải phóng reservations/allocations.
- Hoàn tất delivery có thể tạo `PARTIALLY_RETURNED` trước khi close.
- Một order có thể sở hữu nhiều shipment/trip; partial delivery không close order khi quantity còn lại vẫn là active backorder.
- Mỗi shipment có lifecycle/reconciliation riêng và không được dùng trạng thái tổng của order để suy đoán shipment đã giao.
- Active reservation không tự expire âm thầm trong MVP; shipment, authorized order change/cancellation hoặc audited reconciliation mới được consume/release.
- Backorder quantity chưa có eligible stock không được biểu diễn như một reservation giả.

Implementation có thể tách state của order, fulfillment, và shipment thay vì dồn mọi giá trị vào một cột. Các transition quan sát được phải tương đương.

## Purchase order và receipt

```text
DRAFT -> APPROVED -> SENT -> PARTIALLY_RECEIVED -> RECEIVED -> CLOSED
```

Nhánh: `CANCELLED`, `REJECTED`, và `CLOSED_WITH_SHORTFALL` theo policy.

Receipt:

```text
DRAFT -> RECEIVING -> RECEIVED -> QC_PENDING -> RELEASED -> PUT_AWAY -> CLOSED
                                  \-> REJECTED / PARTIALLY_RELEASED
```

## Inventory status

Inventory status áp dụng cho một stock segment, không nhất thiết cho toàn bộ Lot:

```text
RECEIVING -> QC_HOLD -> AVAILABLE
                  \-> QUARANTINE -> AVAILABLE
                                  \-> DAMAGED
                                  \-> RETURN_TO_SUPPLIER
                                  \-> DESTROY_PENDING -> DESTROYED
AVAILABLE -> QUARANTINE / RECALLED / EXPIRED / DAMAGED
```

`RESERVED` được duy trì như một reservation, không phải inventory quality status.

## Pick task

```text
CREATED -> ASSIGNED -> IN_PROGRESS -> COMPLETED -> STAGED
                          \-> SHORT_PICK -> REALLOCATED -> COMPLETED
```

Cancellation chỉ giải phóng các quantity chưa bị shipment đã xác nhận tiêu thụ.

## Delivery trip và stop

Trip:

```text
PLANNED -> LOADING -> READY -> DEPARTED -> RETURNED -> RECONCILED -> CLOSED
```

Stop:

```text
PENDING -> ARRIVED -> DELIVERED
                   \-> PARTIAL
                   \-> FAILED
```

Trip không thể close khi hàng trả về hoặc variance giao hàng chưa được reconcile.

## Customer return

```text
REQUESTED -> AUTHORIZED -> RECEIVED_QUARANTINE -> INSPECTING
          -> RESTOCK_APPROVED -> RESTOCKED -> CLOSED
          -> REJECTED -> CLOSED
          -> DESTROY_APPROVED -> DESTROYED -> CLOSED
          -> SUPPLIER_RETURN -> CLOSED
          -> INVESTIGATION_HOLD
```

## Destruction

```text
DRAFT -> SUBMITTED -> APPROVED -> EXECUTED -> VERIFIED -> CLOSED
                   \-> REJECTED
```

Requester và approver phải khác nhau. Execution chỉ tạo stock-out movement đúng một lần.
