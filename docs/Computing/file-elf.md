# Executable and Linkable Format ELF

ELF là một định dạng tập tin tiêu chuẩn phổ biến cho

- **executable files**: Các loại tệp thực thi, được mở trực tiếp như là các ứng dụng.
- **object code**: Là sản phẩm phụ của trình biên dịch, chứa các mã thực thi và sẽ được dùng để tạo thành các đối tượng khác, thường là các tệp thực thi - **executable files**
- **shared libraries**: Thư viện động
- **device drivers**: drivers
- Và **core dumps**:  Các tệp phản hồi, báo cáo khi có lỗi xảy ra trong thư viện.

Để đọc ELF, có tham khảo [công cụ readelf của Linux](../OS/Linux/linux-readelf.md)