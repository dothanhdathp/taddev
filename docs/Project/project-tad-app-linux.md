# Project Tad-App Linux

## Chuẩn bị

1. Update System
    ```text
    sudo apt update
    ```
1. Cài đặt __git__
    ```text
    sudo apt install git
    ```
    _Ở một số hệ thống, **git** có thể là phần mềm mặc định_
1. Cài đặt __repo__
    ```text
    sudo apt install repo
    ```
1. Cài đặt __npm__ và __electron__
    ```text
    sudo apt install nodejs npm
    ```
1. Chạy lệnh sau để __npm__ cài đặt các gói cần thiết.
    ```text
    npm install electron-context-menu
    npm install electron --save-dev
    npm run dist
    ```

## Cài Đặt

### repo

Sử dụng `repo` để kéo dự án về:

```text
repo init git@github.com:dothanhdathp/tad-doc.git
repo sync
repo start main --all
```

Sau khi kết thúc thì sẽ có bộ cây thư mục như này:

```text
├── app
└── docs
    ├── linux-venv
    ├── tadbooks
    ├── tadcode
    ├── taddev
    ├── taddiary
    ├── tadstudy
    └── tadworks
```

### Script Setup

Trong đó ứng dụng sẽ nằm trong thư mục __*tad-doc/app*__. Để cài đặt thì có thể chạy tệp `setup.sh`, nó là một tệp đóng gói đầy đủ.

Về bản chất cài đặt bình thường chỉ có một dòng này, và icon được cài đặt thêm qua tệp `setup.sh`

```bash
sudo apt install ./dist/tad-app_1.0.0_amd64.deb
```

## Zorin OS

Với __Zorin OS__ có đôi chút vấn đề. Icon không hoạt động. Để có icon sử dụng lệnh dưới này khai báo vào tệp `/usr/share/applications/tad-app.desktop`

```bash
sed -i 's|Icon=tad-app|Icon=/home/dtdat/Pictures/cat-white-icon.png|' /usr/share/applications/tad-app.desktop
```