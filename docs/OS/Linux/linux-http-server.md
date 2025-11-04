# HTTP Server

Khởi động __HTTP Server__ trên Ubuntu đơn giản bằng:

```bash
python3 -m http.server [PORT] [OPTION]
```

- `PORT`: Port number

- `OPTION`:
    - `-d` hoặc `--directory` + `<arg>`: Chọn thư mục để bắt đầu máy chủ
    - `-b` hoặc `--bind` + `<IP Address>`: Liên kết với một địa chỉ IP cụ thể __*(IP Address)*__
    - `--cgi`: Kích hoạt `CGI HTTPRequestHandler`

!!! note "CGI là cái gì?"
    __CGI__ là viết tắt của __*Common Gateway Interface (Giao diện Cổng Chung)*__. Đây là một giao thức chuẩn được sử dụng để cho phép máy chủ web thực thi các chương trình bên ngoài —thường là các tập lệnh—và gửi kết quả đầu ra trở lại trình duyệt của máy khách . Đây là cách các trang web động ban đầu hoạt động trước khi các nền tảng hiện đại xuất hiện.

    Ví dụ, khi người dùng gửi biểu mẫu, máy chủ có thể chạy một tập lệnh CGI (viết bằng Python, Perl, v.v.) để xử lý dữ liệu và trả về phản hồi.

    Thế nên `CGI HTTPRequestHandler` cho phép __HTTP Server__ được quyền phục vụ các tập lệnh CGI qua các giao thức.
