# Linux Vim

Vim là công cụ chỉnh sửa văn bản mặc định. Hầu hết tất cả các hệ điều hành chuẩn UNIX đều cho phép vi vì nó nhẹ, đơn giản và cho phép sửa đổi các tệp văn bản ở mức độ nhất định. Đồng thời vi có thể chạy qua `terminal` và không kén chọn loại tệp được chỉ định.

## Chế Độ

Vim có ba chế độ:

1. [Chế độ nhập lệnh](#che-do-nhap-lenh), _(chế độ mặc định)_.
1. Chế độ Sửa Nhanh. Chế độ này thường tương tác dưới dạng bôi đen văn bản và sử dụng các thao tác như thêm, xóa, thay đổi cục bộ, ...
1. Chế độ Sửa Thủ Công. Chế độ này cho phép nhập, xóa, sửa trực tiếp ... từng ký tự đơn lẻ.

### Chế Độ Nhập Lệnh

- Chế độ này sẽ được khởi động lúc khởi động vi với một tệp văn bản nào đó.
- Ở chế độ này, thường sẽ được dùng để di chuyển sang các chế độ khác. Nếu đang ở chế độ khác, ấn **ESC** sẽ quay về chế độ này.
- Các thao tác chung sẽ được tương tác dưới dạng nhập lệnh. Ấn `:` sẽ chuyển vào khu vực nhập lệnh ở góc dưới cùng. Sau đây là trình bày các lệnh.

#### Thao Tác

Các thao tác này được thực hiện trực tiếp không cần lệnh, gọi là chỉnh sửa nhanh.

| Phím Tắt        | Giải thích                                                                         |
| :-------------- | :--------------------------------------------------------------------------------- |
| `x`             | Xóa một chữ, tương đương phím **Backspace**. Lệnh này không thoát chế độ nhập lệnh |
| `dd`            | Xóa nhanh một dòng.                                                                |
| `u`             | Under last change. Trở lại một bước trước đó.                                      |
| `U` _(shift+u)_ | Under All change.                                                                  |
| `*`             | Tại vị trí con trỏ, tìm từ tương tự _**tiếp theo**_ giống từ con trỏ đang trỏ đến.       |
| `#`             | Tại vị trí con trỏ, tìm từ tương tự _**trước đó**_ giống từ con trỏ đang trỏ đến.       |
|                 |                                                                                    |

#### Di Chuyển

| Lệnh      | Giải thích                  |
| :-------- | :-------------------------- |
| `<ctrl>d` | Scroll down (half a screen) |
| `<ctrl>u` | Scroll up (half a screen)   |
| `<ctrl>f` | Page forward                |
| `<ctrl>b` | Page backward               |

#### Với Tệp

| Lệnh    | Giải thích                                             |
| :------ | :----------------------------------------------------- |
| `:q`    | Thoát. Nếu có chỉnh sửa mà thoát, lệnh này sẽ thất bại |
| `:q!`   | Thoát và _**không lưu**_                               |
| `:wq`   | Thoát và _**lưu**_                                     |

#### Lệnh thao tác chỉnh sửa

##### Tìm Kiếm

- Tìm kiếm đoạn bằng lệnh `\text`
- Tìm kiếm từ `\/<word/>`

#### 

## Reversed (Hoàn thiện sau)

- `/usr/share/vim` nơi chia sẻ các tệp cấu hình.
- `/etc/vim/vimrc` hoặc `/etc/vimrc` là nơi lưu trữ các cấu hình mặc định.