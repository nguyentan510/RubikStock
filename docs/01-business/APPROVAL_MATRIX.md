# Approval Matrix

RubikStock MVP dùng một cấp duyệt cho FEFO override và stock adjustment; không có second-level theo quantity/value. Discount nằm ngoài RubikStock và do Sales/Accounting quản lý.

| Action | Initiator | Approver | Mandatory reason | Evidence |
|---|---|---|---|---|
| FEFO override | Sales/warehouse | Warehouse manager, luôn bắt buộc một cấp | Yes | Customer request and original/selected lots |
| Stock adjustment | Warehouse/count team | Warehouse manager, luôn bắt buộc một cấp | Yes | Count/recount |
| Unplanned receipt release | Warehouse receiver | Warehouse manager | Yes | Supplier/reference và lý do không có PO |
| Over-receipt release | Warehouse receiver | Warehouse manager | Yes | Expected/actual/excess quantity và supplier evidence |
| Return to available | Receiver/QC | Authorized inspector | Yes | Inspection result |
| Damage classification | Warehouse/QC | Authorized inspector/manager | Yes | Condition evidence |
| Destruction | Warehouse/QC | Independent manager | Yes | Quantity, Lot, private photo và note |
| Purchase order | Purchasing | Authorized purchasing manager | Yes for plan override | Recommendation and supplier terms |
| Manual forecast override | Sales/purchasing | Planning owner | Yes | Event/customer context |
| Lot recall/block | QC/manager | Authorized manager | Yes | Incident/supplier notice |
| Role/permission change | Administrator | Security/business owner | Yes | Access request |

## Approval invariants

- Approver must hold the required role at approval time.
- Approval records are immutable; revocation creates a new record/action.
- The subject state/version approved must match the state executed.
- Self-approval is prohibited where separation of duty applies.
- FEFO override và stock adjustment không có second-level approval theo quantity/value trong MVP.
- Expired approval cannot authorize a later changed request.
