# M8 Roadmap - Production Qualification

- Status: `PLANNED`
- Depends on: Release scope M1-M7 được chọn đã pass domain gates
- Unlocks: Controlled production promotion

## Outcome

Chứng minh hệ thống, dữ liệu, con người và runbooks đủ khả năng vận hành an toàn; production promotion là quyết định được ủy quyền, không phải kết quả tự động của việc build pass.

## Work packages

| ID | Nội dung | Deliverables | Verification |
|---|---|---|---|
| M8.1 | Release scope freeze | Included modules/users/warehouse/SKU và non-goals | Owner sign-off |
| M8.2 | Security qualification | RBAC review, secret rotation, dependency disposition | Security gate |
| M8.3 | Migration rehearsal | Sanitized/full-scale import, reject resolution, timing | Reconciliation report |
| M8.4 | Backup/restore | Automated backup và restore vào isolated environment | Restore evidence |
| M8.5 | Observability | Health, errors, reconciliation, expiry/stock alerts | Alert-delivery test |
| M8.6 | Performance baseline | Large-order, stock query, allocation, import baseline | Accepted SLO report |
| M8.7 | Incident/recovery drill | DB unavailable, unknown shipment, auth revocation | Runbook exercise |
| M8.8 | UAT/training | Role-based scenarios, training, issue disposition | Signed UAT evidence |
| M8.9 | Cutover/rollback | Writer ownership, dual-run window, freeze, rollback criteria | Tabletop + rehearsal |
| M8.10 | Promotion decision | Go/no-go record và named approver | Gate M8 pass |

## Qualification levels

```text
Implementation-aligned
-> Local runtime verified
-> Staging runtime verified
-> Production-like qualified
-> Production-ready
-> Promotion authorized
```

Không dùng một mức để thay thế mức tiếp theo.

## Exit gate

- UAT được business owners ký.
- Restore, incident, secret rotation và access revocation được thực hành.
- Migration/cutover/rollback reconcile.
- Alerts tới đúng accountable owner.
- Không còn critical/high finding chưa có accepted disposition.
- Go-live được người có thẩm quyền phê duyệt rõ ràng.
