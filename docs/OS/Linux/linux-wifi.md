# Linux Wifi

## Xem Danh Sách

Xem danh sách các kết nối wifi _(nếu có)_

```bash
sudo nmcli device wifi list
```

## Kết Nối

### Cách 1

Kết nối đến một mạng Wifi đã biết. Ví dụ mạng "NamWifi" với mật khẩu "12345678" thì:

- `SSID_NAME` = `NamWifi`
- `YOUR_PASSWORD` = `12345678`

```bash
sudo nmcli device wifi connect "SSID_NAME" password "YOUR_PASSWORD"
```

### Cách 2

Nếu mật khẩu chứa các ký tự đặc biệt có thể dùng cách sau _(hoặc có thể là để giấu mật khẩu)_.

```bash
sudo nmcli device wifi connect "SSID_NAME" --ask
```

Lúc này câu lệnh sẽ yêu cầu nhập mật khẩu wifi thủ công.

## Tắt Wifi

```bash
sudo nmcli device disconnect wlan0
```
