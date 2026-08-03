# Secret Management và Rotation

## Rule

- Commit `.env.example` chỉ với tên biến, không bao giờ commit value.
- Lưu runtime secret trong cơ chế secret/environment của platform.
- Bảo vệ production deployment thông qua GitHub Environment approval.
- Ưu tiên OIDC deployment identity ngắn hạn khi được hỗ trợ.
- Giữ database, auth administrative và storage credentials ở phía server.
- Che/redact authorization header, connection string, token, và signed URL khỏi log.

## Mẫu quy trình rotation

1. Xác định phạm vi secret và các consumer.
2. Tạo secret thay thế mà không xóa secret đang hoạt động nếu platform hỗ trợ.
3. Deploy consumer dùng secret mới.
4. Xác minh authentication và audit log.
5. Revoke/xóa secret cũ.
6. Xác minh secret cũ không còn dùng được.
7. Ghi lại thời điểm rotation, owner, hệ thống, và evidence mà không ghi value.

## Nghi ngờ bị lộ

1. Coi việc lộ ra public repository là đã bị compromise, kể cả khi xóa nhanh.
2. Revoke/rotate trước theo quy trình của provider.
3. Rà soát log và data/operation bị ảnh hưởng.
4. Loại secret khỏi lịch sử hiện tại và đi theo policy incident; rewrite Git history cần được ủy quyền rõ ràng.
5. Thêm scanning/control phòng ngừa.
