# Startup Script

Tạo một tệp thực thi dạng __*script*__ và sẽ được chạy khi bắt đầu khởi động.

Để làm được điều đó đầu tiên cần có __*script*__, Tạo ví dụ về một tệp lệnh như sau dùng để truyền một message chứa địa chỉ IP đến một máy đích thông qua cổng NET.
- Tạo __*script*__
    ```bash title="startup.sh"
    #!/usr/bin/bash

    function share_ip_address {
    while true; do
        echo PC: $(hostname) :: IP: $(hostname -I) | nc -w1 $1 $2;
        sleep 2;
    done;
    }

    ## Share IP address to target IP
    share_ip_address 192.168.100.54 55555 &
    share_ip_address 192.168.100.121 55555 &
    ```
- Lưu tệp ví dụ lưu với tên __*startup.sh*__ vào dường dẫn `/etc/init.d/` _(Nên là đường dẫn này để chứa các tệp thực khi lúc khởi động)_
- Chạy lệnh:
    ```bash
    sudo crontab -e
    ```
- Chọn `1` để chọn tiến trình chỉnh sửa bằng `nano`
- Kéo xuống cuối cùng và thêm đường dẫn này vào dưới dạng:
    ```text
    ...
    # For more information see the manual pages of crontab(5) and cron(8)
    #
    # m h  dom mon dow   command

    @reboot /etc/init.d/startup.sh
    ```

Để đọc được bản tin, ở máy đích dùng lệnh:

```text
nc -l -p 55555
```