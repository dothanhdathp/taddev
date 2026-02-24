# AnyDesk

## Tổng quan

[Trang chủ](https://anydesk.com/en)

## Tải Về / Cài Đặt

### Windown

- Bản tải về trực tiếp tại [https://download.anydesk.com/AnyDesk.exe](https://download.anydesk.com/AnyDesk.exe). Đây là bản phát hành tiêu chuẩn.
- Bản đã _crack_ [_Anydesk full không lisences (google drive)_](https://drive.google.com/file/d/12DIt9FGeRvLS7prDeDmb9ucBqC5L5k5X/view?usp=sharing). Tải về tại [_nguồn_](https://phanmemvui.com/anydesk-full-crack/).
- Cách thứ ba hình như là chỉ cần xóa tệp gì đó trong tệp _config_ đi là được _(tự crack)_.

### Linux

Với Linux tải về bản `anydesk_7.0.2-1_amd64.deb` bẳng lệnh:

```bash
wget https://download.anydesk.com/linux/anydesk_7.0.2-1_amd64.deb
```

Sau đó dùng lệnh sau để cài đặt:

```bash
sudo dpkg -i anydesk_7.0.2-1_amd64.deb
```

## Điều khiển

Các phần mã lệnh là giống nhau, chỉ là nếu mở trên __*Windows*__ vui lòng đưa vào tệp `.exe`

### Restricted Settings

!!! danger "Danger"
    __Anydesk__ sẽ yêu cầu quyền __*Adminstrator*__ để có các cài đặt cấp cao hơn.

- Trên __*Windows*__ bạn sẽ được yêu cầu _mởi lại ứng dụng với quyền admins_ và mở cho bạn quyền truy cập vào các cài đặt nguy hiểm.
- Trên __*Ubuntu/Linux*__ dùng lệnh dưới này để gọi.
    ```bash
    sudo anydesk --admin-settings
    ```

### Command

- `--admin-settings`: sẽ mở bảng cài đặt cấp cao. Yêu cầu có quyền __*Adminstrator*__ hoặc `sudo`.
- `--get-id`: Trả về địa chỉ _address_ của phiên hiện tại.

## Xử lý vấn đề

??? bug "Lỗi __display_server_not_supported__ trên __Ubuntu__"
    <figure markdown="span">
        ![alt text](./img/anydesk.png)
        <figcaption></figcaption>
    </figure>

    Lỗi này do ???, để sửa nó thì chạy lệnh sau:

    ```bash
    sudo nano /etc/gdm3/custom.conf
    ```

    Sau đó thêm dòng này vào mục `[daemon]`, kiểu kiểu này:

    ```txt
    # GDM configuration storage
    #
    # See /usr/share/gdm/gdm.schemas for a list of available options.

    [daemon]
    AutomaticLoginEnable=true
    AutomaticLogin=tad

    # Uncomment the line below to force the login screen to use Xorg
    WaylandEnable=false

    # Enabling automatic login

    # Enabling timed login
    #  TimedLoginEnable = true
    #  TimedLogin = user1
    #  TimedLoginDelay = 10

    [security]

    [xdmcp]

    [chooser]

    [debug]
    # Uncomment the line below to turn on debugging
    # More verbose logs
    # Additionally lets the X server dump core if it crashes
    #Enable=true
    ```