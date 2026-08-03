# ADR-0001: Start with a Modular Monolith

- Status: `PROPOSED`
- Date: 2026-08-03

## Context

RubikStock có các transaction inventory, fulfillment, return, delivery, và planning gắn chặt với nhau. Đội ngũ cần correctness và traceability trước khi nghĩ đến scale độc lập.

## Decision

Xây một FastAPI deployment và một PostgreSQL database, với domain modules và application interfaces được định nghĩa rõ.

## Consequences

- Các thao tác stock xuyên module có thể dùng một database transaction.
- Deployment và local development đơn giản hơn.
- Ownership của module phải được enforce bằng code review và tests.
- Chỉ được tách một module ra khi có nhu cầu vận hành/scale đã đo được và contract ổn định.

## Bác bỏ cho MVP

- Microservices và distributed transactions.
- Event broker làm source of truth.
- Database riêng cho từng module.
