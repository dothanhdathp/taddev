# MkDocs TadApp

Để sử dụng `TadApp` cần:

- Yêu cầu cài đặt Python
- Yêu cầu cài đặt Pip cho Python

## Chung

Để tải về mkdocs cho hệ thống cần theo các bước:

- Tải về `python`
- Tải về `pip`
- Tải một số gói cài đặt cần thiết:
    ```bash
    pip install mkdocs
    pip install pymdown-extensions
    pip install mkdocs-material
    pip install mkdocs_puml
    pip install mkdocs-network-graph-plugin
    ```

## Các gói tải

Lưu ý với các tệp tài liệu riêng biệt như `taddev`, `taddocs`, .. thì cần phải chạy lệnh cài đặt biến môi trường:

```bash
python3 -m venv linux-venv
source linux-venv/bin/activate
```