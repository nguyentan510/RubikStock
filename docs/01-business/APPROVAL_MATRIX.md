# Approval Matrix

Threshold values are `TBD` and must be configured, not hard-coded.

| Action | Initiator | Approver | Mandatory reason | Evidence |
|---|---|---|---|---|
| FEFO override | Sales/warehouse | Warehouse manager according to policy | Yes | Customer request and original/selected lots |
| Stock adjustment | Warehouse/count team | Warehouse manager; second level above threshold | Yes | Count/recount |
| Return to available | Receiver/QC | Authorized inspector | Yes | Inspection result |
| Damage classification | Warehouse/QC | Authorized inspector/manager | Yes | Condition evidence |
| Destruction | Warehouse/QC | Independent manager | Yes | Quantity, lot, execution evidence |
| Purchase order | Purchasing | Authorized purchasing manager | Yes for plan override | Recommendation and supplier terms |
| Manual forecast override | Sales/purchasing | Planning owner | Yes | Event/customer context |
| Lot recall/block | QC/manager | Authorized manager | Yes | Incident/supplier notice |
| Role/permission change | Administrator | Security/business owner | Yes | Access request |

## Approval invariants

- Approver must hold the required role at approval time.
- Approval records are immutable; revocation creates a new record/action.
- The subject state/version approved must match the state executed.
- Self-approval is prohibited where separation of duty applies.
- Expired approval cannot authorize a later changed request.

