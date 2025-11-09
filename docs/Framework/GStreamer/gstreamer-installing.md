# Installing GStreamer

Trang tải về ở đây:

- [https://gstreamer.freedesktop.org/documentation/installing/index.html](https://gstreamer.freedesktop.org/documentation/installing/index.html)
- Vì thời gian không cho phép nên một số đầu mục mình sẽ để lại, tập trung chủ yếu vào __*Android*__ và __*Linux*__ thôi.

## Tải về cho Windows

Tham khảo đường dẫn này dể có bản cập nhập mới nhất cho Windows: [link](https://gstreamer.freedesktop.org/download/#windows)

- Hoặc có thể tải xuống trực tiếp bản cài đặt ở đây: 
    - [gstreamer-1.0-msvc-x86_64-1.26.5.msi](https://gstreamer.freedesktop.org/data/pkg/windows/1.26.5/msvc/gstreamer-1.0-msvc-x86_64-1.26.5.msi)

## Tải về cho Linux

!!! abstract "Abstract"
    __GStreamer__ được tích hợp sẵn trong tất cả các bản phân phối Linux. Chúng tôi khuyên bạn nên sử dụng phiên bản mới nhất của một bản phân phối có tốc độ phát triển nhanh như __Fedora__, __Ubuntu__ _(không phải LTS)_, __Debian__ sid hoặc __OpenSuse__ để nhận bản phát hành __GStreamer__ mới nhất.

=== "Ubuntu/Debian"
    ```bash
    sudo apt-get install libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libgstreamer-plugins-bad1.0-dev \
    gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly \
    gstreamer1.0-libav gstreamer1.0-tools gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 \
    gstreamer1.0-qt5 gstreamer1.0-pulseaudio -y
    ```

=== "Fedora"
    ```bash
    dnf install gstreamer1-devel gstreamer1-plugins-base-tools gstreamer1-doc gstreamer1-plugins-base-devel \
    gstreamer1-plugins-good gstreamer1-plugins-good-extras gstreamer1-plugins-ugly gstreamer1-plugins-bad-free \
    gstreamer1-plugins-bad-free-devel gstreamer1-plugins-bad-free-extras
    ```

## Mac OS X

## Android

Tải về __*tarball*__ của GStream và giải nén __*(trên các máy Linux)*__.

Xem phiên bản ổn định trên [trang chủ của gstreamer](https://gstreamer.freedesktop.org/download/#android) và tải về phiên bản ổn định nhất.

Sau đó giải nén là đã có thể sử dụng.

Theo dõi [hướng dẫn cho Android](gstreamer-android-tutorial-1.md) để biết rõ các bước.

Các phiên bản khác có thể xem ở [_đường dẫn_](https://gstreamer.freedesktop.org/data/pkg/android/). Vào thư mục và tải về tệp `gstreamer-1.0-android-universal-1.xx.x.tar.xz` tương ứng.

Hai tệp còn lại mình không rõ, có lẽ để `checksum`, sẽ nghiên cứu sau.

## iOS