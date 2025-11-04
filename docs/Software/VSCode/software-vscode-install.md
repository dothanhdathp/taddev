# Cài đặt VSCode

## Cài đặt cho Windows

- Tải bản cài đặt tại trang chủ [link](https://code.visualstudio.com/download)
- Sau khi tải về, mở tệp cài đặt và cứ ___Next___ thôi.


## Cài đặt cho Linux

1. Dùng lệnh `dpkg --print-architecture` để biết hệ điều hành đang chạy ở core nào.
1. Lên trang chủ của Microsoft, tải về bản cài đặt. Nhớ tải đúng kiến trúc của `cpu-core`.
1. Dùng `wget` bản cài đặt về theo link, ví dụ sử dụng [link](https://vscode.download.prss.microsoft.com/dbazure/download/stable/e170252f762678dec6ca2cc69aba1570769a5d39/code_1.88.1-1712770538_arm64.deb) là cho Rasberry-Pi.
1. Cài đặt với `dpkg -i file_name.deb`

```
sudo snap install --classic code
```

## Các phiên bản cũ hơn

Xem lại các phiên bản cũ hơn của __Visual Studio Code__ tại [đường dẫn](https://code.visualstudio.com/updates/)

### Linux

_Chưa làm_