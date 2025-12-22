# \[POSIX\] Shell

Theo chuẩn POSIX.1-2008, các câu lệnh này được coi là chuẩn mực và bắt buộc phải có trên mọi hệ điều hành tuân thủ POSIX (như các bản phân phối Linux chuẩn, BSD, Unix).

Dưới đây là danh sách các câu lệnh gốc thiết yếu, chia theo mục đích sử dụng:

1. Quản lý Tệp và Thư mục:
    - `ls`: Liệt kê nội dung thư mục.
    - `cd`: Thay đổi thư mục làm việc.
    - `pwd`: In đường dẫn thư mục hiện tại.
    - `cp`: Sao chép tệp.
    - `mv`: Di chuyển hoặc đổi tên tệp.
    - `rm`: Xóa tệp hoặc thư mục.
    - `mkdir`: Tạo thư mục.
    - `rmdir`: Xóa thư mục trống.
    - `touch`: Thay đổi thời gian truy cập/chỉnh sửa tệp (thường dùng để tạo tệp trống).
    - `ln`: Tạo liên kết (link) giữa các tệp.
2. Xử lý Văn bản (Công cụ dòng lệnh mạnh nhất)
    - `cat`: Nối và hiển thị nội dung tệp.
    - `grep`: Tìm kiếm văn bản theo biểu thức chính quy.
    - `sed`: Trình chỉnh sửa dòng (Stream Editor) để biến đổi văn bản.
    - `awk`: Ngôn ngữ quét và xử lý mẫu văn bản.
    - `cut`: Trích xuất các trường/cột từ mỗi dòng của tệp.
    - `paste`: Ghép các dòng của các tệp lại với nhau.
    - `sort`: Sắp xếp các dòng văn bản.
    - `uniq`: Loại bỏ các dòng lặp lại trong văn bản đã sắp xếp.
    - `head`: Hiển thị phần đầu của tệp.
    - `tail`: Hiển thị phần cuối của tệp.
    - `wc`: Đếm số dòng, số từ và số byte.
3. Quản trị Hệ thống và Tiến trình
    - `ps`: Báo cáo trạng thái các tiến trình hiện tại.
    - `top`: Hiển thị các tiến trình đang hoạt động (đây là lệnh gốc POSIX, khác với htop).
    - `kill`: Gửi tín hiệu đến tiến trình (thường để dừng tiến trình).
    - `chmod`: Thay đổi quyền truy cập tệp (mode).
    - `chown`: Thay đổi chủ sở hữu tệp.
    - `umask`: Thiết lập mặt nạ quyền tạo tệp mặc định.
    - `df`: Báo cáo dung lượng đĩa trống của hệ thống tệp.
    - `du`: Ước tính dung lượng sử dụng của tệp/thư mục.
4. Điều khiển Shell và Scripting
    - `sh`: Trình thông dịch lệnh chuẩn POSIX.
    - `echo`: In các đối số ra đầu ra tiêu chuẩn (stdout).
    - `read`: Đọc một dòng từ đầu vào tiêu chuẩn (stdin).
    - `test` (hoặc dấu `[`): Kiểm tra các điều kiện (dùng trong câu lệnh if).
    - `printf`: Định dạng và in dữ liệu (thường được khuyên dùng thay cho echo trong POSIX).
    - `export`: Đặt biến môi trường.
    - `wait`: Chờ tiến trình con kết thúc.
5. Khác
    - `man`: Hiển thị tài liệu hướng dẫn hệ thống.
    - `find`: Tìm kiếm tệp trong hệ thống thư mục.
    - `xargs`: Xây dựng và thực thi các câu lệnh từ đầu vào tiêu chuẩn.
    - `vi`: Trình soạn thảo văn bản chuẩn (mọi hệ thống POSIX bắt buộc phải có vi).