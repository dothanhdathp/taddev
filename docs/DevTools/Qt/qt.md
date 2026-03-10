# Qt

## Mô tả

__Qt__ là `cross-platform` 

- Qt Framework
- Qt Development Tools
- Qt Design Studio
- Qt Accelerate

## Download

### Official Releases

- Tải về __Qt__ bản mới nhất chắc chắn là trên trang chủ: [**https://www.qt.io/**](https://www.qt.io/)
- Nếu phiên bản bạn cần sử dụng không phải là bản mới nhất, có thể tra cứu lại __các phiên bản đã được xuất bản (vẫn còn hỗ trợ)__ [**Official Releases**](https://download.qt.io/official_releases/).
- Hoặc có thể tải bản _cài đặt không mạng_ [**offline-installers**](https://www.qt.io/offline-installers)

### Archive of Historical Versions

Và nếu bạn là một đứa nghèo rách _(giống mình)_ thì có thể tìm và cài đặt một số phiên bản cũ hơn ở đây: [https://download.qt.io/archive/](https://download.qt.io/archive/)

Các phiên bản khuyến nghị:

- `Qt5.12.10`: Bản này _crack_ được! Là bản cao cấp nhất có thể _crack_

## Tự Xây Dựng

Vào đường dẫn [qt-archive](https://download.qt.io/archive/qt/) và tải về bản _**qt-everywhere**_ của phiên bản mong muốn. Ví dụ:

| Version | Download                                           |
| :------ | :------------------------------------------------- |
| 6.10    | [Download](https://download.qt.io/archive/qt/6.10) |
| 6.9     | [Download](https://download.qt.io/archive/qt/6.9)  |

Sau đó tải về các tệp _**qt-everywhere-src**_, ví dụ với bản mới nhất hiện được biết đến là:

- [qt-everywhere-src-6.10.2.zip](https://download.qt.io/archive/qt/6.10/6.10.2/single/qt-everywhere-src-6.10.2.zip)
- [qt-everywhere-src-6.10.2.tar.xz](https://download.qt.io/archive/qt/6.10/6.10.2/single/qt-everywhere-src-6.10.2.tar.xz)

Sau khi tải về qt thì bắt đầu thực hành xây dựng

### Các thư viện phụ thuộc (Dependencies)

Trước khi tải mã nguồn, bạn cần các công cụ biên dịch và thư viện phát triển hệ thống:

```bash
sudo apt update
sudo apt install build-essential perl python3 ruby libxcb-xinerama0 \
libx11-dev libxext-dev libxfixes-dev libxi-dev libxrender-dev \
libxcb1-dev libx11-xcb-dev libxcb-glx0-dev libxcb-keysyms1-dev \
libxcb-image0-dev libxcb-shm0-dev libxcb-icccm4-dev libxcb-sync-dev \
libxcb-xfixes0-dev libxcb-shape0-dev libxcb-randr0-dev \
libxcb-render-util0-dev libxcb-util-dev libxcb-xkb-dev \
libxkbcommon-dev libxkbcommon-x11-dev
```

### Cấu Hình - Configure

Đây là bước quan trọng nhất. Bạn sẽ quyết định Qt sẽ bao gồm những gì. Nên tạo một thư mục riêng để build (shadow build) để giữ sạch mã nguồn:

```bash
mkdir build && cd build
../configure -prefix /opt/qt-custom \
-release \
-opensource \
-confirm-license \
-nomake examples \
-nomake tests \
-xcb
```

Giải thích:

- `-prefix`: Đường dẫn nơi Qt sẽ được cài đặt sau khi biên dịch xong.
- `-release`: Biên dịch bản phát hành ưu hiệu năng _(thay vì `-debug` để gỡ lỗi)_.
- `-nomake examples/tests`: Bỏ qua ví dụ và bài test để tiết kiệm thời gian (có thể giảm vài tiếng đồng hồ build).

### Biên dịch và Cài đặt

!!! danger "Danger"
    - qt5 trở xuống dùng **qmake**
    - qt6 dùng **cmake**

```bash
cmake --build . --parallel $(nproc)
sudo cmake --install .
```

`$(nproc)` là số luồng máy tính hỗ trợ tốt nhất để xây dựng. Thường là số luồng của **CPU**. Nếu máy tính cần sử dụng thêm các tác vụ khác có thể xem xét giảm con số này xuống.

### Thiết lập biến môi trường

Để hệ thống và các công cụ như `qmake` hoặc `cmake` nhận diện được bản **Qt** vừa xây dựng, bạn cần thêm đường dẫn vào `.bashrc` hoặc `.zshrc`:

```bash
export PATH=/opt/qt-custom/bin:$PATH
export LD_LIBRARY_PATH=/opt/qt-custom/lib:$LD_LIBRARY_PATH
```