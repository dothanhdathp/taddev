# \[Zorin\] Menu Application

## Local Application

Giả sử mình có một ứng dụng tự dựng _(tự định nghĩa)_ và muốn cho nó vào trong __Menu__ để mở nhanh thì cần phải _khai báo một tệp desktop_.

Đầu tiên là các tệp được phân bổ trong đây: `/usr/share/applications`

Tạo một tệp mới tự định nghĩa, ví dụ như mình tạo ra `tad-app` là ứng dụng của mình thì.

- Tạo tệp mới trong đường dẫn `/usr/share/applications`
tên là `tad-app.desktop`
- Sử dụng vim hoặc nano để chỉnh sửa nội dung. Nội dung khá giống dạng tệp `TUML`

```text
[Desktop Entry]
Type=Application
Name=Tad App
Comment=This is my local executed application. Build in another folder
Exec=/home/dtdat/Git/electrone-docs-app/dist/tad-1.0.0.AppImage
Icon=/home/dtdat/Git/electrone-docs-app/node_modules/app-builder-lib/templates/icons/electron-linux/16x16.png
Terminal=false
Categories=Utility;
```
```text
[Desktop Entry]
Name=Tad
Exec=/opt/tad/tad-app %U
Terminal=false
Type=Application
Icon=/home/dtdat/Pictures/cat-white-icon.png
StartupWMClass=tad
Categories=Utility;
```

!!! failure "Failure"
    Vẫn chưa thêm phần icon cho cho ứng dụng Tad vào resource. Nói chung là cái này vẫn lỗi tùm lum.

- `Type`: Loại ứng dụng
- `Name`: Tên ứng dụng
- `Comment`: Mô tả về ứng dụng
- `Exec`: Nơi thực thi
- `Icon`: _icon_

## Wine Application

Đôi khi có một số ứng dụng được cài đặc qua wine để lại một tệp ứng dụng trên màn hình trong khi tệp thực thi đã bị xóa hoặc loại bỏ. Cấu hình ảnh của nó ở trong:

```text
~/.local/share/applications/
```

Mà cụ thể là:

```text
~/.local/share/applications/wine/Programs/
```