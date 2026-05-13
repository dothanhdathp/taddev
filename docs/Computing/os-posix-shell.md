# POSIX Shell

Theo chuẩn POSIX.1-2008, các câu lệnh này được coi là chuẩn mực và bắt buộc phải có trên mọi hệ điều hành tuân thủ POSIX (như các bản phân phối Linux chuẩn, BSD, Unix).

Dưới đây là danh sách các câu lệnh gốc thiết yếu, chia theo mục đích sử dụng. Có 5 loại chính là:

1. _**Quản lý Tệp và Thư mục**_ = `QLT_TM`
1. _**Xử lý Văn bản**_ = `XLVB`
1. _**Quản trị Hệ thống và Tiến trình**_ = `QTHH_TT`
1. _**Điều khiển Shell và Scripting**_ = `DKS_S`
1. _**Khác**_ = `Another`

| Lệnh                    |     Lớp     | Tác Dụng                                                                       |
| :---------------------- | :---------: | :----------------------------------------------------------------------------- |
| `ls`                    | __QLT_TM__  | Liệt kê nội dung thư mục.                                                      |
| `cd`                    | __QLT_TM__  | Thay đổi thư mục làm việc.                                                     |
| `pwd`                   | __QLT_TM__  | In đường dẫn thư mục hiện tại.                                                 |
| `cp`                    | __QLT_TM__  | Sao chép tệp.                                                                  |
| `mv`                    | __QLT_TM__  | Di chuyển hoặc đổi tên tệp.                                                    |
| `rm`                    | __QLT_TM__  | Xóa tệp hoặc thư mục.                                                          |
| `mkdir`                 | __QLT_TM__  | Tạo thư mục.                                                                   |
| `rmdir`                 | __QLT_TM__  | Xóa thư mục trống.                                                             |
| `touch`                 | __QLT_TM__  | Thay đổi thời gian truy cập/chỉnh sửa tệp (thường dùng để tạo tệp trống).      |
| `ln`                    | __QLT_TM__  | Tạo liên kết (link) giữa các tệp.                                              |
| `cat`                   |  __XLVB__   | Nối và hiển thị nội dung tệp.                                                  |
| `grep`                  |  __XLVB__   | Tìm kiếm văn bản theo biểu thức chính quy.                                     |
| `sed`                   |  __XLVB__   | Trình chỉnh sửa dòng (Stream Editor) để biến đổi văn bản.                      |
| `awk`                   |  __XLVB__   | Ngôn ngữ quét và xử lý mẫu văn bản.                                            |
| `cut`                   |  __XLVB__   | Trích xuất các trường/cột từ mỗi dòng của tệp.                                 |
| `paste`                 |  __XLVB__   | Ghép các dòng của các tệp lại với nhau.                                        |
| `sort`                  |  __XLVB__   | Sắp xếp các dòng văn bản.                                                      |
| `uniq`                  |  __XLVB__   | Loại bỏ các dòng lặp lại trong văn bản đã sắp xếp.                             |
| `head`                  |  __XLVB__   | Hiển thị phần đầu của tệp.                                                     |
| `tail`                  |  __XLVB__   | Hiển thị phần cuối của tệp.                                                    |
| `wc`                    |  __XLVB__   | Đếm số dòng, số từ và số byte.                                                 |
| `ps`                    | __QTHH_TT__ | Báo cáo trạng thái các tiến trình hiện tại.                                    |
| `top`                   | __QTHH_TT__ | Hiển thị các tiến trình đang hoạt động (đây là lệnh gốc POSIX, khác với htop). |
| `kill`                  | __QTHH_TT__ | Gửi tín hiệu đến tiến trình (thường để dừng tiến trình).                       |
| `chmod`                 | __QTHH_TT__ | Thay đổi quyền truy cập tệp (mode).                                            |
| `chown`                 | __QTHH_TT__ | Thay đổi chủ sở hữu tệp.                                                       |
| `umask`                 | __QTHH_TT__ | Thiết lập mặt nạ quyền tạo tệp mặc định.                                       |
| `df`                    | __QTHH_TT__ | Báo cáo dung lượng đĩa trống của hệ thống tệp.                                 |
| `du`                    | __QTHH_TT__ | Ước tính dung lượng sử dụng của tệp/thư mục.                                   |
| `sh`                    |  __DKS_S__  | Trình thông dịch lệnh chuẩn POSIX.                                             |
| `echo`                  |  __DKS_S__  | In các đối số ra đầu ra tiêu chuẩn (stdout).                                   |
| `read`                  |  __DKS_S__  | Đọc một dòng từ đầu vào tiêu chuẩn (stdin).                                    |
| `test` _(hoặc dấu `[`)_ |  __DKS_S__  | Kiểm tra các điều kiện (dùng trong câu lệnh if).                               |
| `printf`                |  __DKS_S__  | Định dạng và in dữ liệu (thường được khuyên dùng thay cho echo trong POSIX).   |
| `export`                |  __DKS_S__  | Đặt biến môi trường.                                                           |
| `wait`                  |  __DKS_S__  | Chờ tiến trình con kết thúc.                                                   |
| `man`                   | __Another__ | Hiển thị tài liệu hướng dẫn hệ thống.                                          |
| `find`                  | __Another__ | Tìm kiếm tệp trong hệ thống thư mục.                                           |
| `xargs`                 | __Another__ | Xây dựng và thực thi các câu lệnh từ đầu vào tiêu chuẩn.                       |
| `vi`                    | __Another__ | Trình soạn thảo văn bản chuẩn (mọi hệ thống POSIX bắt buộc phải có vi).        |