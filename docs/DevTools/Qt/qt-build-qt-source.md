# Buikd Qt Source

## Tải Về

Tải về nguồn tại [kho lưu trữ **official_releases**, thư mục **qt**](https://download.qt.io/official_releases/qt/). Sau đó tại phiên bản mong muốn tìm đến thư mục **single**, tìm tệp binary tải về  có dạng _**qt-everywhere-src-{version}.zip**_ hoặc _**qt-everywhere-src-{version}.tar.xz**_.

## Build

### Yêu Cầu
> [Tham khảo tại](https://doc.qt.io/qt-6/linux-requirements.html)

- Theo trang chủ, các tệp dưới này là yêu cầu cần thiết.
- Thêm cờ `-y` để các gói tải về luôn _(thay cho câu trả lời **yes**)_

```text
apt install \
    libfontconfig1-dev \
    libfreetype-dev \
    libgtk-3-dev \
    libx11-dev \
    libx11-xcb-dev \
    libxcb-cursor-dev \
    libxcb-glx0-dev \
    libxcb-icccm4-dev \
    libxcb-image0-dev \
    libxcb-keysyms1-dev \
    libxcb-randr0-dev \
    libxcb-render-util0-dev \
    libxcb-shape0-dev \
    libxcb-shm0-dev \
    libxcb-sync-dev \
    libxcb-util-dev \
    libxcb-xfixes0-dev \
    libxcb-xkb-dev \
    libxcb1-dev \
    libxext-dev \
    libxfixes-dev \
    libxi-dev \
    libxkbcommon-dev \
    libxkbcommon-x11-dev \
    libxrender-dev -y
```

### Build

- Trước tiên giải nén tệp vừa tải về - tệp tar.xz. Ở đây ví dụ nó là tệp `qt-everywhere-src-6.10.2` và tôi giải nên ở `/tmp/` để sau khi kết thúc, máy tính sẽ dọn dẹp các tệp đó.
    ```bash
    tar -xvf ./qt-everywhere-src-6.10.2.tar.xz -C /tmp/
    ```
- Tạo một thư mục khác để cấu hình và các biên dịch sẽ được tải vào đó. Ở đây với mong muốn hiểu hệ thống nên mình sẽ sử dụng thư mục riêng được đặt ở `~/.local/`, nơi chứa các biến và thành phần cục bộ. Có nghĩa là, ở cấp độ hệ thống sẽ không có Qt tránh gây rác, xung đột.
    - Tạo thư mục mới như sau
        ```bash
        mkdir ~/.local/lib
        mkdir ~/.local/lib/qt
        mkdir ~/.local/lib/qt/qt6.10.2
        cd ~/.local/lib/qt/qt6.10.2
        
        ```
- Theo mặc định, Qt được cấu hình để cài đặt trong đường dẫn `/usr/local/Qt-6.10.2`. Khi đó chạy lệnh cấu hình ở chế độ mặc định với lệnh `/tmp/qt-everywhere-src-6.10.2/configure`. Điều này có thể được thay đổi bằng cách sử dụng tùy chọn `-prefix`. Xem danh sách các tùy chọn cấu hình để điều chỉnh thêm. Vì mình muốn cài đặt Qt cho user nên mình dùng lệnh dưới này:
    ```bash
    /tmp/qt-everywhere-src-6.10.2/configure -top-level -prefix /home/tad/.local/lib/qt/qt6.10.2
    ```
- Một cách khác, khi mà cờ `-prefix` không hoạt động hoặc lỗi, có thể đưa trực tiếp cờ vào hệ thống như này:
    ```text
    /tmp/qt-everywhere-src-6.10.2/qtbase/configure -top-level -- -DCMAKE_INSTALL_PREFIX=/home/tad/.local/lib/qt/qt6.10.2
    ```
- Sau khi _configure_ hoàn thành. Tiến hành xây dựng thư viện và công cụ:
    ```bash
    cmake --build . --parallel
    ```
- Cài đặt cho Qt
    ```bash
    cmake --install .
    ```

## Tham Khảo

### Phiên Bản Qt

etc.
