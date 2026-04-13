# mkbook

Công cụ này giúp tạo các tệp sách giống như rust từng làm. Mình dự định kết hợp nó với tadprebuild để xây dựng các cuốn sách cho các nội dung dài hướng dẫn ứng dụng hoặc gì đó.

Để tải về sử dụng công cụ:

- [github of mdbook](https://github.com/rust-lang/mdbook/)
- [github mdbook release](https://github.com/rust-lang/mdbook/releases)

> Công cụ này là độc lập nên có thể sao chép trực tiếp binary vào trong `/usr/bin/` để sử dụng.

Tải về binary và lưu vào local. Sau đó chạy lệnh

```text
mdbook init my-book-name
```

Nó sẽ tự tạo cấu trúc khởi tạo cho các tệp sách.

- Sau đó các đề mục có thể khai báo vào trong `SUMMARY.md`
- Các tệp md sẽ chứa các nội dung của từng chương.
- `book.toml` lưu trữ thông tin cục bộ, nó có dạng này:
    ```text
    [book]
    title = "High Performance Browser Networking"
    authors = ["Ilya Grigorik"]
    language = "en"
    ```
## Kết hợp với puml

Để dùng với planuml cần tải plugin

```text
cargo install mdbook-plantuml
```

Sau đó khai báo trong `toml`

```text
[preprocessor.plantuml]
command = "mdbook-plantuml"
plantuml-cmd = "java -jar /path/to/plantuml.jar" # Đường dẫn tới file jar PlantUML của bạn
```

`mdbook-plantuml` cũng là công cụ **CLI** nên cũng sẽ cho dần vào trong các tệp gốc nhé.