# \[Linux\] Wifi

## Common Linux

Xem danh sách các kết nối wifi _(nếu có)_

```bash
nmcli device wifi list
```

Kết nối đến một mạng Wifi đã biết. Ví dụ mạng "NamWifi" với mật khẩu "12345678" thì:

- `SSID_NAME` = `NamWifi`
- `YOUR_PASSWORD` = `12345678`

```bash
nmcli device wifi connect "SSID_NAME" password "YOUR_PASSWORD"
```

Tắt Wifi

```bash
nmcli device disconnect wlan0
```