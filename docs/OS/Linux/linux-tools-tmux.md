# Tmux

## Tmux là gì

- __tmux__ nghĩa là `terminal multiplexer` (chia thành nhiều kênh).
- Tác dụng của __tmux__ là ứng dụng sẽ chia terminal thành nhiều phiên làm việc (session). Khi bạn chạy ứng dụng này tức là bạn mở một session mới. Trong mỗi session, có nhiều terminal

## Tải về tmux

```bash
sudo apt-get install tmux -y
```
## Sử dụng

### Câu lệnh

#### Xem danh sách phiên

```bash
tmux ls
```

#### Tạo phiên

=== "New"
    Tạo một phiên mới _(bất kỳ, tên sẽ được đánh tự do theo luật)_. Thường sẽ là 0, 1, 2, ...

    ```bash
    tmux
    ```
=== "New + Open"
    Tạo một phiên mới _(bất kỳ, tên sẽ được đánh theo luật)_. Đồng thời mở luôn phiên đó trong trong cửa sổ làm việc:

    ```bash
    tmux a
    ```
=== "New + Name"
    Cách này thường dùng nhất. Tạo một phiên làm việc với với tên xác định và cũng mở luôn phiên làm việc đó.

    ```bash
    tmux new -s NAME
    ```

    Với `NAME` là tên riêng tự đặt cho phiên làm việc đó

#### Mở lại phiên làm việc

Kiểm tra trước với lệnh `tmux ls`, nếu phiên đã tồn tại, gọi lệnh sau để mở lại phiên với tên:

```bash
tmux a -t NAME
```

#### Xóa phiên

Lệnh dưới này sẽ đóng phiên từ __*terminal*__

```bash
tmux kill-session -t NAME
```

### Phím tắt

| Phím tắt                   | Tác dụng                                  |
| :------------------------- | :---------------------------------------- |
| `Ctrl + B` + `D`           | Thoát cửa sổ hiện tại                     |
| `Ctrl + B` + `C`           | Tạo một cửa sổ mới                        |
| `Ctrl + B` + `W`           | Xem danh sách cửa sổ hiện tại             |
| `Ctrl + B` + `N` or `P`    | Chuyển đến cửa sổ tiếp theo hoặc trước đó |
| `Ctrl + B` + `F`           | Tìm kiếm cửa sổ                           |
| `Ctrl + B` + `,`           | Đặt/Đổi tên cho cửa sổ                    |
| `Ctrl + B` + `&`           | Đóng cửa sổ                               |
| `Ctrl + B` + `pgup`/`pgdn` | Cuộn con trỏ để đọc log trong cửa sổ      |