# \[Git\] SSH

Trong bài này sẽ mô tả đầy đủ các bước để bắt đầu một dự án với Git

## SSH Key

__SSH Key__ _(Secure Shell)_ là <u>phương thức xác thực thông tin truy cập</u> được sử dụng để xác thực an toàn người dùng với máy chủ hoặc dịch vụ từ xa. Thay vì sử dụng tên người dùng và mật khẩu truyền thống, khóa SSH sử dụng một cặp tệp được liên kết bằng mật mã: __Public Key__ và __Private Key__.

### Tạo SSH Key

Để có quyền truy cập vào các kho lưu trử git yêu cầu sử dụng `ssh-key`. Tạo `ssh-key` bằng lệnh sau:

=== "Defaule"
    ```bash
    ssh-keygen
    ```
=== "ED25519"
    ```bash
    ssh-keygen -t ed25519 -C "rakauhouha10@gmail.com"
    ```
=== "RSA"
    ```bash
    ssh-keygen -t rsa -b 4096 -C "rakauhouha10@gmail.com"
    ```

- __*rsa*__ là kiểu mặc định nếu bạn không có nhu cầu bảo mật cao
- __*ed25519*__ có khả năng bảo mật tốt hơn
- Trong trường hoặc sử dụng mặc định lệnh `ssh-keygen`, hệ thống sẽ tự chọn _email_ và tên được đăng ký trên hệ điều hành hoặc git để sử dụng làm _key_
- __*rakauhouha10@gmail.com*__ _là email của mình, hãy thay thế bằng mail của bạn

## File

### SSH Key File

Thông thường các tệp key sẽ được đặt tại thư mục:

=== "Windows"
    ```bash
    %USERPROFILE%\.ssh
    ```
=== "Linux"
    ```bash
    ~/.ssh
    ```

- Trong đó sẽ thường có hai kiểu tệp là __*tệp không có đuôi*__ và __*tệp có đuôi là .pub*__
- __*tệp không có đuôi*__ là _private key_, thường thì sẽ không được chia sẻ ra ngoài
- __*tệp có đuôi .pub*__ là _public key_, nếu muốn thêm vào đâu thì sử dụng tệp này.

### SSH Config File

Cũng trong đường dẫn như mục [SSH Key File](#ssh-key-file), còn có một tệp khác xuất hiện là tệp tên __config__. Tệp này cài đặt một số cấu hình riêng biệt dành cho __SSH__ như quy định về cổng, quy định về địa chỉ IP, quy định về _key_ sử dụng, ...

Một số công năng như sau:

#### Sử dụng nhiều SSH Key

Trường hợp mẫu này mình có hai tài khoản __*Github*__ riêng biệt. Thông thường thì có thể sử dụng nếu đơn giản là __*Add SSH Key*__ vào cho cả hai tài khoản. Nhưng đôi khi, vì muốn giấu, hoặc do vấn đề bảo mật nên cùng một tài khoản, mình đã lỡ đăng ký với hai _key_ khác nhau. Và đây là cách mình cấu hình tệp ssh:

```text
Host github.com
Host github.com
User dtdat
Port 22
IdentityFile ~/.ssh/id_rsa_dat

Host tad-github.com
HostName github.com
User tad
Port 22
IdentityFile ~/.ssh/id_rsa_tad
```

Như cáu hình trên, có thể thấy với cùng một _host: github.com_ sử dụng hai loại key khác nhau. Với `github.com` vẫn sẽ là `github.com` và sử dụng _key_ id_rsa_dat.

Đường khác là `tad-github.com`, tuy vẫn trỏ đến `github.com` nhưng key được đăng ký là dùng tệp `id_rsa_tad`

## Sử dụng SSH Key

Về mục đích chính xác key này sử dụng để cho phép truy cập vào các kho lưu trữ như giao thức xác nhận. Lấy ví dụ với [Github](https://github.com/), nếu bạn muốn kéo bất cứ dự án gì về thì không cần __*Key*__, nhưng nếu muốn sửa đổi nội dung rồi đẩy ngược lên từ dự án thì cần key.

- _Hướng dẫn thêm ssh-key vào github_