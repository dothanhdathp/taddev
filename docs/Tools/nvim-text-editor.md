# NeoVim

## Thông Tin

- Trang Chủ: [https://neovim.io/](https://neovim.io/)

## Tải Về và Cài Đặt

Có nhiều cách để tải về NeoVim, có thể dùng:

- [Install](https://neovim.io/doc/install/): Trang chủ chứa các bản phát hành có sẵn, khuyến nghị.
    - Với _**Linux**_ Sau khi tải về ta có bản nén của `nvim-linux-{arch}.tar.gz`. Giải nén và đưa vào thư mục `/opt/`
    - Sau đó tạo một tệp _simbolic-link_ tới `/opt/nvim-linux-arch/bin/nvim` trong `/usr/bin/`
        ```bash
        sudo ln -s nvim /opt/nvim-linux-arch/bin/nvim
        ```
    - Ứng dụng đương nhiên sẽ có icon và nhiều thứ, nhưng mình không định đưa thành _**desktop application**_ thì để vậy là được rồi.
- Nếu không thích có thể tải bản dựng mới nhất từ [github-releases](https://github.com/neovim/neovim/releases)
- Hoặc cũng có thể tham khảo trang này để bắt đầu [Tự xây dựng NeoVim từ nguồn](https://neovim.io/doc/build/)

## Quick Start

### Các Chế Độ

- `Esc` được sử dụng khi chuyển đổi các chế độ về mặc định. Từ khu vực này, các chế độ sẽ được di chuyển từ chế độ mặc định.
- Nhấn phím `i` để vào chế độ [chỉnh sửa văn bản](#chinh-sua-van-ban).
- Nhấn phím `v` vào chế độ [Chỉnh sửa nhanh (Editing)](#chinh-sua-nhanh-editing).
- Nhấn phím `:` vào chế độ [Nhập Lệnh](#che-do-nhap-lenh).

### Chế Độ Nhập Lệnh

Chế độ nhập lệnh là chế độ cơ bản nhất.
Ở chế độ này, người dùng bắt đầu nhập lệnh qua phím `:`. Chỉ cần ấn phím đó, nvim sẽ bắt đầu chuyển vào chế độ nhập lệnh.

| Lệnh  | Thay Thế | Công Dụng               |
| :---- | :------- | :---------------------- |
| `:q`  |          | Thoát khỏi chương trình |
| `:w`  |          | Lưu thay đổi            |
| `:x`  | `:wq`    | Lưu & Thoát             |
| `:q!` |          | Thoát nhưng không lưu   |

### Chỉnh Sửa nhanh (Editing)

Chế độ này được bắt đầu khi nhấn `v` từ chế độ nhập lệnh. Ở chế độ này có các tác dụng sau:

| Lệnh | Thay Thế | Công Dụng                         |
| :--- | :------- | :-------------------------------- |
| `x`  |          | Xóa ký tự ngay tại con trỏ.       |
| `dd` |          | Xóa (cắt) cả dòng.                |
| `yy` |          | Sao chép (copy) cả dòng.          |
| `p`  |          | Dán (paste) nội dung sau con trỏ. |
| `u`  | `Ctrl+r` | Hoàn tác (undo) Redo.             |

Tôi không chắc các phím này sử dụng trong chế độ điều hướng hay không. Hình như được dùng trong chế độ chỉnh sửa nhanh.

- `h`,`l`,`k`,`j` dùng để điều hướng trái, phải, trên, dưới
- `w`: Nhảy đến đầu từ tiếp theo.
- `b`: Quay lại đầu từ trước đó.
- `0`: Về đầu dòng / $: Tới cuối dòng.
- `gg`: Về đầu file / G: Tới cuối file.

### Chỉnh Sửa Văn Bản

Chế độ này được bắt đầu khi nhấn `i` từ chế độ nhập lệnh.

## Cài Đặt LSP

**NeoVim** không có sẵn các plug-in để hoạt động như một trình chỉnh sửa văn bản toàn diện. Sử dụng _deamon_ ngoài giúp việc đó.

```bash
sudo apt update
sudo apt install build-essential clangd
```
