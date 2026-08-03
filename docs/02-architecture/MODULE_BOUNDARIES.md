# Module Boundaries

- Contract status: `D1 ACCEPTED`

RubikStock khởi đầu là một modular monolith. Các module dùng chung một deployment và một database, nhưng mỗi module tự sở hữu behavior và public application interface của nó.

| Module | Sở hữu | Không được sở hữu |
|---|---|---|
| `identity` | Ánh xạ identity, roles, quyết định authorization | Ngữ nghĩa inventory hoặc approval |
| `catalog` | Products, categories, UOM, conversions, packaging, trạng thái master-data | Số lượng stock |
| `partners` | Customers, suppliers, customer shelf-life policy | Inventory allocation |
| `warehouse` | Warehouses, zones, locations, location capabilities | Định nghĩa thương mại của product |
| `inventory` | Lots, stock movements, balance projection, transfers, reservations | Giá bán hoặc delivery route |
| `inbound` | Purchase receipt, chênh lệch receipt, QC entry, orchestration put-away | Replenishment forecast |
| `outbound` | Sales fulfillment, eligibility, allocation, orchestration pick/stage/ship | Sửa balance trực tiếp ngoài inventory API |
| `quality` | Holds, inspections, recall/block, disposition | Sales confirmation |
| `returns` | Return authorization, receipt quarantine, liên kết workflow inspection | Silent restock |
| `delivery` | Trips, phân công vehicle/driver, stops, POD, reconciliation hàng trả | Sửa balance kho |
| `planning` | Safety stock, event calendar, baseline forecast, purchase recommendation | Tự động duyệt mua hàng |
| `audit` | Audit trail cho hành động/quyết định có đặc quyền và query | Quyền sở hữu business state |
| `files` | Metadata của evidence, private object access | Quyết định approval nghiệp vụ |

## Hướng dependency

```text
catalog/partners/warehouse
        -> inventory
        -> inbound/outbound/quality/returns
        -> delivery
        -> planning
        -> reporting

identity và audit là cross-cutting nhưng không được định nghĩa lại domain rule.
```

## Quyền sở hữu transaction

- Inventory movement và projection của balance/reservation phải commit trong cùng một database transaction.
- Shipment confirmation gọi inventory application service; nó không tự cập nhật balance table.
- Return restock phải gọi inspection/disposition rồi mới gọi inventory movement trong một command được kiểm soát.
- Scheduled planning đọc projection đã qualify và ghi recommendation có version, không ghi trực tiếp inventory.

## Hình dạng layer theo module

```text
api route -> application command/query -> domain rules -> repository/adapter
```

- Route map HTTP input/output và authentication context.
- Application service điều phối transaction và authorization.
- Domain code enforce invariant.
- Repository lưu và query data.
- Pydantic request/response model phải tách khỏi SQLAlchemy persistence model.
