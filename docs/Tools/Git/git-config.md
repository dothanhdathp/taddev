# \[Git\] Git Config

Nhận và thiết lập các tùy chọn kho lưu trữ hoặc chung.

## Xem cấu hình

Để xem các cấu hình sẵn có của _git_ thì ta sử dụng lệnh `git config --list`

## Kho lưu trữ

__Kho lưu trữ__ nghĩa là để xác định _phân vùng_, hoặc _khu vực làm việc_ riêng biệt. Có 2 phân vùng chính là:

1. `--local`
1. `--system`
1. `--global`
1. `--worktree`
1. `--file`

Trong đó mình ít dùng `--local`, hầu hết là `--global`.

Nhưng có thể hiểu đơn giản, là `--local` mang ảnh hưởng cục bộ ở trên __*project*__ thôi còn `--global` sẽ mang ảnh hưởng trên toàn bộ các tiến trình __*git*__

## User

Phía `user` có hai __trường mặc định__ là _name_ và _email_. Thường thì nếu không có hai trường này git sẽ chặn các hành độnh như _clone_, _push_, ...

Cấu hình như sau:

=== "dtdat"
    ```bash
    git config --global user.name "dtdat"
    git config --global user.email=rakauhouha10@gmail.com
    ```
=== "tad"
    ```bash
    git config --global user.name "tad"
    git config --global user.email=rakauhouha10@gmail.com
    ```

## Core

Trong phần này có nhiều lựa chọn hơn, các cấu hình sẽ ảnh hưởng phần lớn đến hoạt động của _git_.

### code.filemode

Có một vấn đề rất buồn cười đó là một số tệp bị tô màu đỏ lòm trong khi không có chỉnh sửa gì trong nội dung cả. Thông thường, lỗi này xảy ra nhiều với các tệp trên __Linux__ hơn là __Windows__.

`code.filemode` dùng để bỏ qua sự thay đổi về quyền của tệp ví dụ như quyền `root` hoặc `user`. Chống các chương trình chỉnh sửa tệp như là __VSCode__ sửa đổi quyền thay đổi tệp.

```bash
git config --global code.filemode "false"    
```

Sau lệnh trên, một số tệp của dự án sẽ không bị tô màu đỏ lòm trong khi không có chỉnh sừa

### core.editor

`core.editor` dùng để thay đổi phần mềm sửa các nội dung văn bản ví dụ như khi dùng `git commit`. Nếu không thì sẽ là dùng phần mềm chỉnh sửa văn bản mặc định từ hệ điều hành, dạng như `vim` hoặc `WordPad` ...

Để thay đổi thì dùng công thức sau:

```bash
git config --global core.editor "<tool>"
```

#### Notepad++

Theo lý thuyết chỉ cần để cấu hình như này là được:

```bash
git config --global core.editor "C:/Program\ Files/Notepad++/notepad++.exe"
```

Nhưng nếu để như vậy rất bất tiện. Các dự án sẽ vào chung trên một tiến trình `notepad++`. Trong khi đó, sửa đổi chỉ được xác nhận khi mà đóng cửa sổ _notepad++_ đó đi, rất bất tiện. Thế nên mới có cấu hình dưới

```bash
git config --global core.editor "'C:\Program Files\Notepad++\notepad++.exe' -multiInst -notabbar -nosession -noPlugin"
```

Với cài đặt ở dưới, mỗi lần sử dụng _git_ để sửa đổi gì đó ví dụ như `git commit` thì sẽ mở lại __*notepad++*__ trên một tiến trình (cửa sổ) mới. Sau khi chỉnh sửa xong chỉ cần đóng cửa sổ là được.

#### Sublime

__Sublime__ cũng là một `text-editor` tiềm năng, cơ mà hiện tại với git thì mình thích dùng __notepad++__ để đọc hơn.

### autocrlf

> Lỗi __LF/CRLF__

Khi thêm tệp vào đôi khi có thể sẽ gặp lỗi:

```txt
warning: in the working copy of 'site/assets/javascripts/lunr/min/lunr.da.min.js', LF will be replaced by CRLF the next time Git touches it
```

Lỗi này đánh dấu một số tệp bị trục trặc do khác _kiến trúc tệp_ của __Windows__ và __Unix__, nơi đặt các giá trị đầu cuối dòng như `/r/n` ... khác nhau:

Để loại bỏ vấn đề này thì cần đặt lại cấu hình như sau:

=== "Windows"

    ```bash
    git config --global core.autocrlf true 
    ```
=== "Unix/macOS"

    ```bash
    git config --global core.autocrlf input
    ```