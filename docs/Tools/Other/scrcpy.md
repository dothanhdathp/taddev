# Scrcpy

## Overview

Ứng dụng này dùng để _stream_ màn hình từ thiết bị __Android__

- Github: [https://github.com/Genymobile/scrcpy/tree/master](https://github.com/Genymobile/scrcpy/tree/master)

### Tải về cho Windows

!!! note "Ghi chú"
    [Xem hướng dẫn tại đây](https://github.com/Genymobile/scrcpy/blob/master/doc/windows.md)

Tải về theo đường dẫn rồi chạy trực tiếp tệp `scrcpy.exe`

### Tải về cho Linux

!!! note "Ghi chú"
    [Xem hướng dẫn tại đây](https://github.com/Genymobile/scrcpy/blob/master/doc/linux.md)

__Các bước thực hiện:__

1. Lấy về _source-code_ `scrcpy`
    ```bash
    git clone https://github.com/Genymobile/scrcpy
    ```
1. Kéo về thay đổi mới nhất
    ```bash
    git pull
    ```
1. Tải về các gói phụ thuộc
    ```bash
    sudo apt install ffmpeg libsdl2-2.0-0 adb wget \
        gcc git pkg-config meson ninja-build libsdl2-dev \
        libavcodec-dev libavdevice-dev libavformat-dev libavutil-dev \
        libswresample-dev libusb-1.0-0 libusb-1.0-0-dev -Y
    ```
1. Cài đặt
    ```bash
    ./install_release.sh
    ```
1. Chạy thử
    ```bash
    scrcpy
    ```

### Tải về cho macOS

!!! note "Ghi chú"
    [Xem hướng dẫn tại đây](https://github.com/Genymobile/scrcpy/blob/master/doc/macos.md)
