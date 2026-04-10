# MkDocs

## MKDocs là gì?

__MKDocs__ là một công cụ viết tài liệu bằng markdown vô cùng mạnh. Nó là giải pháp thay thế tốt cho cái phong cách viết đầu tiên của mình. Công cụ này có đầy đủ những chức năng thiết yếu để viết tài liệu offline + online. Đồng thời còn hỗ trợ cả việc đưa tài liệu lên __*Internet*__.

### Yêu cầu

- Yêu cầu có cài đặt Python, [xem hướng dẫn ở đây]().

## Cài Đặt Mkdocs

Hướng dẫn cài đặt chi tiết

{{ slide("dev/how-to-install-mkdocs.html") }}

Tóm tắt các câu lệnh sử dụng 

=== "Linux"
    Khởi động python venv
    ```bash
    python3 -m venv linux-venv
    source linux-venv/bin/activate
    ```
    Kết thúc
    ```bash
    pip install click==8.0.4
    pip install mkdocs
    pip install pymdown-extensions
    pip install mkdocs-material
    pip install mkdocs_puml
    pip install mkdocs-network-graph-plugin
    pip install mkdocs-macros-plugin
    ```
    Kết thúc python venv
    ```bash
    deactivate
    ```
=== "Windows"
    ```text
    pip install --upgrade pip
    python get-pip.py
    pip install mkdocs
    ```
    Hoặc
    ```text
    python -m pip install mkdocs
    python -m mkdocs
    ```

## Bắt đầu với Mkdocs

- Đầu tiên bạn cần (nên) có một tài khoản Github để lưu trữ
- Tạo một nhánh bất kỳ để lưu trữ tài liệu
- Sau đó vào trong thư mục của git và bắt đầu với:

```bash
mkdocs new .
```

- Nếu thành công sẽ có kết quả như này

```bash
INFO    -  Writing config file: ./mkdocs.yml
INFO    -  Writing initial docs: ./docs/index.md
```

- Với các ví dụ sẵn có, có thể chạy lệnh sau để khởi động server

```bash
mkdocs serve
```

- Bật một __Web Brower__ bất kỳ với `localhost:8000`

```bash
http://localhost:8000/
```

Vậy là xong, sẽ có một trang web hiện lên và bạn đã có một trang web tài liệu cho riêng mình rồi đó.

## Tham khảo

- [Trang chủ Mkdocs](https://www.mkdocs.org)
- [Hướng dẫn cài đặt Mkdocs trên trang chủ](https://www.mkdocs.org/user-guide/installation/)