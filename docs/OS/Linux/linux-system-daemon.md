# \[Linux\] Daemon

## Định nghĩa

__*daemon*__ là một chương trình chạy nền cho hệ điều hành.

## Đặc điểm

- __Tiến trình nền:__ Không có giao diện đồ họa (GUI).
- __Không tương tác:__ Nó không cần đầu vào từ bàn phím, chuột hoặc thiết bị đầu cuối.
- __Sống lâu:__ Thường tự động khởi động khi máy tính khởi động và tiếp tục chạy cho đến khi máy tính tắt.
- __Nhiệm vụ/Dịch vụ hệ thống:__ Nhiệm vụ của nó là thực hiện một nhiệm vụ cụ thể, thiết yếu, như quản lý kết nối mạng, xử lý công việc in hoặc chạy các tác vụ theo lịch trình.

Các tiến trình chạy ngầm sẽ thường được thêm chữ `d` vào sau tên, ví dụ:

- `sshd` __*(Secure Shell Daemon)*__: Chờ các yêu cầu đăng nhập từ xa an toàn đến.
- `httpd` __*(HTTP Daemon, ví dụ: Apache)*__: Chờ yêu cầu từ trình duyệt web và phục vụ các trang web.
- `crond` __*(Cron Daemon)*__: Chạy các tác vụ theo lịch trình vào thời gian được thiết lập trước (như sao lưu hoặc dọn dẹp hệ thống).
- `syslogd` __*(System Log Daemon)*__: Thu thập và quản lý nhật ký hệ thống.

!!! info "Info"
    __*Daemon*__ chỉ đơn giản là tên gọi của các tác vụ hệ thống chạy ngầm của các hệ điều hành dạng __*Unix-like*__. Đối với _Windows_ nó chính là là [Windows Service (WS)](../Windows/os-windows-services.md).

## Tham Khảo

- [Deamon Wiki](https://en.wikipedia.org/wiki/Daemon_(computing))