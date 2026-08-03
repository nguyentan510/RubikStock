# Security Model

## Mục tiêu security

1. Ngăn thay đổi inventory và approval trái phép.
2. Bảo vệ khách hàng, supplier, giá, sales history, dữ liệu kho, và file evidence.
3. Giữ audit trail có thể quy trách nhiệm.
4. Giảm blast radius khi credential bị lộ.
5. Khôi phục sau lỗi operator hoặc data corruption.

## Authentication và authorization

- Supabase Auth có thể cung cấp user identity/JWT.
- FastAPI xác thực identity và enforce RBAC/policy ở phía server.
- Việc UI hiển thị hay không không phải authorization.
- Mọi hành động có trách nhiệm phải dùng account có tên rõ ràng.
- Role có đặc quyền và production administration cần kiểm soát authentication mạnh hơn ở D2.
- Quyền của driver chỉ giới hạn trong trips/stops được giao.

## Phân loại secret

| Secret | Nơi được phép | Nơi cấm |
|---|---|---|
| Database runtime URL | API runtime secret manager | Browser, Git, docs, logs |
| Database migration URL | CI environment/secret manager đã bảo vệ | Ví dụ cho developer, browser |
| Supabase publishable key | Frontend environment khi RLS/policy đúng | Dùng như bằng chứng authorization |
| Supabase secret key | Chỉ backend | Browser, mobile bundle, public repository |
| Cloud deploy identity | Ưu tiên OIDC ngắn hạn | Token public/repo dài hạn |
| Cron/job authentication | Secret manager | URL query string hoặc source code |

## Truy cập dữ liệu

- Các bảng ảnh hưởng trực tiếp đến inventory chỉ được mutate thông qua FastAPI application service.
- Quản trị database trực tiếp bị giới hạn, phải log, và không thuộc thao tác thường nhật.
- Bucket chứa evidence là private; database chỉ lưu metadata và liên kết nghiệp vụ.
- Signed/object access phải ngắn hạn và chỉ cấp cho role/record yêu cầu.
- Production data không được sao chép sang fixture test local hoặc public.

## Application controls

- Idempotency cho các command ảnh hưởng stock.
- Optimistic version hoặc database locking cho các transition đồng thời.
- Database constraint cho các bất biến không được phép vi phạm.
- Input validation và file upload có giới hạn.
- Audit logging có che/masking field nhạy cảm.
- Rate limit và abuse control ở biên authentication và public boundary.
- Không chứa secret trong exception message, tracing attribute, hoặc analytics.

## Threat cần xử lý trong D2

| Threat | Control bắt buộc |
|---|---|
| Tài khoản kho bị chiếm đoạt | Session policy, MFA cho role đặc quyền, thu hồi nhanh, audit |
| Browser bị can thiệp | Authorization phía server và domain validation |
| Gửi lặp/double-submit | Idempotency key và unique operation constraint |
| Oversell đồng thời | Reservation transactional và locking/constraint |
| Secret bị lộ trên public Git | Secret scanning, push protection, rotation runbook |
| Upload evidence độc hại | Kiểm tra MIME/size, private storage, chiến lược malware `TBD` |
| Xóa audit | Append path bị giới hạn, retention/backup, integrity review |
| Lạm dụng database đặc quyền | Phân role riêng, access hạn chế, database audit strategy |

## Security gate trước production

- Authorization tests cho mọi command đặc quyền.
- Secret scan không còn credential chưa xử lý.
- Review RLS/data API exposure nếu có browser-to-Supabase access.
- Restore test và access revocation test.
- Review public repository để chắc chắn không có business data thật.
- Diễn tập incident và credential-rotation.
