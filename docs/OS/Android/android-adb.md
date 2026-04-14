# Android ADB
> Android Debug Bridge


## Overview

Là công cụ hỗ trợ _debug_ dành cho các thiết bị __Android__. Công cụ này được phát triển bởi __Google__ giúp đọc các tệp nhật ký hệ thống, truy xuất dữ liệu và điều khiển thiết bị Android. Cái quan trọng là tuân thủ quyền bảo mật hệ thống và phát triển.

## Content

- {{ book("Android ADB",        "android-adb") }}
- {{ book("Tải về ADB",         "android-adb", "adb.html#download-adb") }}
- {{ book("Làm sao để mở ADB",  "android-adb", "adb-enable.html") }}
    - {{ book("Developer Mode", "android-adb", "adb-enable.html#developer-mode") }}
    - {{ book("ADB Usb",        "android-adb", "adb-enable.html#adb-usb") }}
    - {{ book("ADB Wifi",       "android-adb", "adb-enable.html#adb-wifi") }}
- Function
    - {{ book("Gửi Key Event",      "android-adb", "adb-control.html#key-event") }}
    - {{ book("Chụp ảnh màn hình",  "android-adb", "adb-screen.html#chụp-ảnh-màn-hình") }}

### Mở ứng dụng

### Default apps

Là những ___native application___ có sẵn trên thiết bị và hầu như sẽ giống nhau ở mọi thiết bị Android. Trường hợp thiết bị tùy biến sẽ không còn những tính năng này nữa.

```bash
adb shell am start -n package_name/app_name
```

| Tên ứng dụng | package_name/app_name                                |
| :----------- | :--------------------------------------------------- |
| __Settings__ | `com.android.settings/com.android.settings.Settings` |
| Camera       |                                                      |
| __Chrome__   |                                                      |





## 3Party Apps

Đầu tiên dùng lệnh này để hiển thị tất cả 3-party application.

```bash
adb shell pm list packages -3
```

Sau đó có thể sao chép tất cả ra ngoài để xoá bằng lệnh:

```bash
adb uninstall <package_name>
```

Hoặc 

```bash
This command with --user 0 <package_name>
```

## Thêm quyền cho ứng dụng trong khi chạy

Ứng dụng bạn chạy cần một số quyền để sử dụng chức năng hệ thống như truy cập vào tệp, sử dụng danh bạ, phone, truy cập mic, camera, ... thì có thể dùng các lệnh sau để cài đặt quyền động thay cho việc khai báo trực tiếp trong ___Android Manifest___.

Công thức:
```bash
adb shell pm grant your.package.name <permission_name>
```

Ví dụ:
```bash
adb shell pm grant your.package.name android.permission.READ_EXTERNAL_STORAGE
adb shell pm grant your.package.name android.permission.WRITE_EXTERNAL_STORAGE
adb shell pm grant your.package.name android.permission.CAMERA
adb shell pm grant your.package.name android.permission.ACCESS_FINE_LOCATION
adb shell pm grant your.package.name android.permission.RECORD_AUDIO
adb shell pm grant your.package.name android.permission.READ_CONTACTS
adb shell pm grant your.package.name android.permission.WRITE_CONTACTS
adb shell pm grant your.package.name android.permission.INTERNET
```

## Chọn thiết bị

Nếu có hơn một thiết bị được kết nối, dùng thêm cờ `-s ID` để chọn thiết bị. ID lấy bằng `adb devices` ở đây:

Ví dụ:

- Tìm DI thiết bị:
    ```txt
    devices
    List of devices attached
    WCR7N18505010318        device
    192.168.10.123:5555     offline
    ```
- Chạy một số command, ví dụ ở đây là vào __*shell*__:
    ```txt
    adb -s WCR7N18505010318 shell
    ```

## Check Information

### Check API & Android Version

## Broadcast Sender

```bash
adb shell am broadcast -a <message> --es "key" "var" --ei "key" <int>
```