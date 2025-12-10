# \[Project\] Tad-App Linux

Cho hệ thống linux nó nằm trên nhánh `linux-application`

Sau đó sẽ có tệp `tad-app_1.0.0_amd64.deb` trong thư mục `./dist`

Để cài đặt sử dụng:

```bash
sudo apt install ./dist/tad-app_1.0.0_amd64.deb
```

## Zorin OS

Với __Zorin OS__ có đôi chút vấn đề. Icon không hoạt động. Để có icon sử dụng lệnh dưới này khai báo vào tệp `/usr/share/applications/tad-app.desktop`

```bash
sed -i 's|Icon=tad-app|Icon=/home/dtdat/Pictures/cat-white-icon.png|' /usr/share/applications/tad-app.desktop
```