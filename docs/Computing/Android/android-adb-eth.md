# Android ADB Ethernet

> Phần này trình bày các vấn đề liên quan đến mạng, wifi, linh tinh, ...

## ADB Wireless

Ở các phiên bản cũ, __*ADB Wireless*__ không có sẵn lựa chọn trong __Developer Settings__ mà cần mở thông qua `ADB USB`. Dù có hay không thì tính năng này hầu như luôn sẵn có trong các thiết bị __*Android*__. Nếu không thấy lựa chọn mà điện thoại của bạn vẫn có wifi có thể thử  cách dưới đây

### Qua ADB Usb

Sử dụng adb debug qua usb port như bình thường và dùng lệnh sau:

```bash title="Mở Adb wiless cho port 5555"
adb tcpip 5555
```

Sau đó thì kết nối với thiết bị đích thông qua địa chỉ ip của nó _(nhớ kết nối cùng mạng)_.

```bash
adb connect IP:5555
```

Nếu không kết nối được có thể dùng

```bash
adb kill-service
adb start-service
```

### Qua console

Trên các thiết bị nhúng nếu được kết nối thông qua cổng _debug_ riêng và có thể truy cập trực tiếp vào __*shell*__ của thiết bị, có thể dùng lệnh sau:

```bash
su
setprop service.adb.tcp.port 5555
stop adbd
start adbd
```

## Đọc Cấu Hình Wifi    

Nhìn chung thì cấu hình mạng wifi sẽ không giấu. Đọc các tệp này có thể dùng để đọc cấu hình *Wifi* và __UUID/PASS__ của Wifi được lưu trong hệ thống.
Để đọc được giá trị của nó thì đọc giá trị tại tệp dưới đây:

=== "Trước Android 9"
    ```bash
    cat /data/misc/wifi/wpa_supplicant.conf
    ```
=== "Sau Android 9"
    ```bash
    cat /data/misc/apexdata/com.android.wifi/WifiConfigStore.xml
    ```

    Đọc từ trên xuống lấy __*WifiConfiguration*__

    ```text
    <WifiConfiguration>
    <string name="ConfigKey">&quot;tot_home2G_12f&quot;WPA_PSK</string>
    <string name="SSID">&quot;tot_home2G_12f&quot;</string>
    <string name="PreSharedKey">&quot;74200075&quot;</string>
    ```