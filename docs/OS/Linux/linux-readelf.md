# Linux Readelf

> [Nguồn readelf](https://man7.org/linux/man-pages/man1/readelf.1.html)

## Mô Tả

`readelf` hiển thị thông tin về một hoặc nhiều tệp đối tượng định dạng ELF. Các tùy chọn kiểm soát thông tin cụ thể nào sẽ hiển thị.

`elffile...` là các tập tin đối tượng được kiểm tra. `32-bit` và `64-bit` là các tệp ELF được hỗ trợ, cũng như các kho lưu trữ chứa các tệp ELF.

Chương trình này thực hiện chức năng tương tự như [objdump](linux-objdump.md) nhưng đi sâu vào chi tiết hơn và tồn tại độc lập với thư viện BFD nên nếu có lỗi trong BFD thì readelf sẽ không bị ảnh hưởng.

## OPTIONS

Các dạng quyền chọn dài và ngắn, được hiển thị ở đây dưới dạng các lựa chọn thay thế, đều tương đương nhau. Phải cung cấp ít nhất một tùy chọn ngoài `-v` hoặc `-H`.
Để xem toàn bộ các _options_, sử dụng lệnh `readelf --help` hoặc `readelf -h`.

### Thường Dùng

