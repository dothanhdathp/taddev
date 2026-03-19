# Linux ls

## Ứng Dụng

Liệt kê thông tin về các FILE (thư mục hiện tại theo mặc định).

## Cách Dùng

1. `ls` cơ bản cho xem các tệp hiện có. Giữa các tệp được phân cách bởi ký tự **TAB**
1. `ls -la` là cách phổ biến thứ 2 cho phép xem toàn bộ các FILE có trong đường dẫn _(kể cả các tệp ẩn)_
    - `-a`: Hiển thị tất cả
    - `-l`: Hiển thị tất cả dưới dạng danh sách
1. Ví dụ với mỗi lệnh sẽ có hiển thị như này
    ```bash title="ls"
    Android.mk  dummy  lights.c  NOTICE
    ```
    ```bash title="ls -la"
    drwxrwxr-x  3 dtdat dtdat  4096 Thg 3  19 11:43 .
    drwxrwxr-x 15 dtdat dtdat  4096 Thg 3   2 15:40 ..
    -rw-rw-r--  1 dtdat dtdat  1150 Thg 3   2 15:33 Android.mk
    drwxrwxr-x  2 dtdat dtdat  4096 Thg 3  19 11:43 dummy
    -rw-rw-r--  1 dtdat dtdat  4992 Thg 3  19 11:12 lights.c
    -rw-rw-r--  1 dtdat dtdat 10690 Thg 3   2 15:33 NOTICE
    ```

## Diễn Giải

Từ lệnh `ls -la`, có thể thấy các thông số như này với một tệp:

1. Cột đầu tiên có thể thấy ký tự đầu tiên là `d` là thư mục, `-` là tệp.
1. Hai thư mục mới xuất hiện là `.` và `..`. Tệp `.` là đại diện cho thư mục hiện tại, `..` là đại diện cho thư mục trước đó _(thư mục cha chứa thư mục hiện tại)_. Do đó câu lệnh quay lại thư mục trước đó mới là `cd ..`
1. `dtdat dtdat` đại diện cho `{user} {group}`, đại diện cho quyền sở hữu của cá nhân hay nhóm. Nếu khác, tức là bạn không có quyền sử dụng tệp đó.
1. Con số tiếp theo đại diện cho kích thước, tính bằng **Byte**.
1. `Thg 3   2 15:33` đại diện cho thời gian cuối tệp được chỉnh sửa.