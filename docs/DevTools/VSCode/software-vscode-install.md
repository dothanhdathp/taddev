# Cài đặt VSCode

## Chính thống

- Trang chủ giới thiệu phần mềm:
- Các bản cài đặt tải về ở đây: [https://code.visualstudio.com/download](https://code.visualstudio.com/download)

## Windows

- Tải bản cài đặt tại trang chủ [https://code.visualstudio.com/download](https://code.visualstudio.com/download)
- Windows sử dụng phiên bản đầu tiên, nên sử dụng phiên bản __User Installer__
- Sau khi tải về, mở tệp cài đặt và cứ __Đồng Ý__ thôi. Công cụ này không có gì nguy hiểm cả

## Linux Distro

### Cài đặt bản mới nhất

1. Dùng lệnh `dpkg --print-architecture` để biết hệ điều hành đang chạy ở core nào.
1. Sau đó như trên trang chủ có chia làm nhiều loại cho các hệ điều hành khác nhau:
    - Gói __*.dpkg*__ dùng cho các hệ điều hành như __Linux__, __Ubuntu__, ..
    - Gói __*.rpm*__ sử dụng cho __Red Hat__, __Fedora__, __SUSE__, ...
1. Chọn đúng hệ điều hành và chọn đúng cả kiến trúc của `cpu-core`.
1. Cài đặt với lệnh:
    ```text
    sudo dpkg -i file_name.deb
    ```


!!! info "Rasberry-Pi"
    Dùng `wget` bản cài đặt về theo link, ví dụ sử dụng.
    
    [code_1.88.1-1712770538_arm64.deb](https://vscode.download.prss.microsoft.com/dbazure/download/stable/e170252f762678dec6ca2cc69aba1570769a5d39/code_1.88.1-1712770538_arm64.deb)
    
    Bản trên là cho __Rasberry-Pi__.

### Bản Classic cho VsCode

```
sudo snap install --classic code
```

## Các phiên bản cũ

Xem lại các phiên bản cũ hơn của __Visual Studio Code__ tại [đường dẫn](https://code.visualstudio.com/updates/)