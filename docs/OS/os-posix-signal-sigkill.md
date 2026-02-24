# POSIX SIGKILL

__SIGKILL__ là tín hiệu đầu tiên cần chú ý. Khác với các lỗi khác như __SIGTERM__ hay __SIGABRT__, tín hiệu này:

- Được gửi từ bên ngoài
- Không thể bị ngăn chặn

## Vấn Đề Của SIGKILL

Các tín hiệu này thường thất nhất khi bạn cố gắng hủy đi một tiến trình từ hệ thống qua lệnh `kill` _(hoặc taskill của __Windows__)_. Lệnh này sẽ ngay lập tức chấm dứt luồng đang hoạt động và nó dễ gây hỏng đến các vùng nhớ.

Theo các lỗi được ghi nhận thì các lỗi cơ bản mà dễ thấy nhất chính là:

- Các tệp đang được thực thi sẽ bị hỏng, ví dụ như tiến trình đang ghi dữ liệu vào một file nào đó, nó sẽ hỏng. Hầu hết các trường hợp là ta nên xóa tệp đang thực thi đi và làm lại.
- Các tệp tạm trong __*tmp*__ và các tệp __*lock*__ vẫn tồn tại sau khi dừng tiến trình. Nếu người quản trị không để ý để thu dọn nó sẽ ở đó vĩnh viễn. Trường hợp xấu nếu tiến trình khởi động lại và truy cập lại vào các tệp này nó sẽ bị hỏng ở lần hoạt động tiếp theo do trạng thái không xác định. Trường hợp tốt thứ hai là nó sẽ khóa chặt khiến chương trình không thể khởi động.

Trường hợp xấu:

- Các vùng nhớ chung như __Shared Memory (Bộ nhớ dùng chung)__ vẫn tồn tại. Các vùng nhớ này có vòng đời độc lập và do tiến trình bị đóng khẩn cấp thế nên nó sẽ trở thành khu vực vô chủ, vẫn chiếm một phần nhỏ trên RAM và không bị thu hồi cho đến khi người dùng xóa thủ công hoặc là khởi động lại hệ thống.
- __*Deadlock*__ xảy ra do tiến trình đang giữ khóa bị kết thúc trước khi trả khóa, tiến trình liên kết với nó sẽ chờ key trong vô vọng. Nó gây treo tài nguyên. Sự đáng sợ nhất của vấn đề này là chương trình vẫn có thể khởi động nhưng sau đó sẽ không làm gì cả. Đây không phải lỗi thế nên không có mã lỗi hay tín hiệu, tiến trình bị treo ở tác vụ đơn nhất.

## Giải Quyết Vấn Đề

### Dọn Dẹp Thủ Công

- Tìm và xóa các file tạm được phát sinh trong `/tmp/`
- Các lệnh `ipcs -m` và `ipcrm -m` để xóa các bộ nhớ dùng chung.

### Lập Trình An Toàn Với Terminate

1. Sử dụng __Robust Mutexes__ (`PTHREAD_MUTEX_ROBUST`) thay cho các dạng Mutex thông thường. Khi tiến trình giữ Mutex chết nó sẽ bắt được mã lỗi và tiến hành chỉnh sửa.
1. Ghi lại nhật ký và tiến hành phục hồi trạng thái, tiến hành sửa đổi sau khi tiến trình bị hủy.
1. Trong mọi trường hợp, nếu có thể, nên sử dụng `SIGTERM`, bắt tín hiệu và xử lý thoát một cách an toàn thay cho lệnh __*kill*__.
1. __\[Win32\]__ Sử dụng __Named Mutex__ thay cho __Robust Mutexes__ của __POSIX__. Lúc này các tiến trình khác sẽ nhận được `WAIT_ABANDONED` và kết thúc an toàn, tránh __*Death Lock*__