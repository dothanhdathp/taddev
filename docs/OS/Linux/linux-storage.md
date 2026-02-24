# Linux Storage

> Toàn bộ về quản lý ổ đĩa trong hệ điều hành Linux và các Linux distro.

## Thông tin

### Danh sách ổ cứng

Xem danh sách các thiết bị ổ cứng khả dụng _(đã kết nối với thiết bị)_ bằng `lsblk`, ví dụ:

```bash
lsblk
```

Kết quả:

```text
NAME        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
loop0         7:0    0     4K  1 loop /snap/bare/5
...
...
...
sda           8:0    0 931.5G  0 disk
nvme0n1     259:0    0 476.9G  0 disk
├─nvme0n1p1 259:1    0   512M  0 part /boot/efi
└─nvme0n1p2 259:2    0 476.4G  0 part /
```

- Các thiết bị vật lý sẽ được đánh dấu là `disk` với hai loại tiền tố:
    - `sd*`: Định dạng ổ đĩa __hdd__
    - `nvme*`: Định dạng ổ đĩa __ssd__
- Theo như hình trên, có 2 ổ cứng vật lý là `sda` và `nvme0n1`
- Nhưng các thiết bị chỉ có thông tin là `disk` thì chưa thể sử dụng, cần được ảo hoá thành các thiết bị ảo `path` và đưa vào __MOUNTPOINTS__ thành các _điểm truy cập_ ảo.
    - Theo như hình trên, có ổ cứng __sda__ có tổng dung lượng là `931.5G` là loại __SSD__ chưa được sử dụng nên vẫn còn có định dạng là `disk`
    - Mặt khác, ổ cứng _SSD_ tên __*nvme0n1*__ có tổng dung lượng là `476.9G` đã được sử dụng, được chia thành hai `path` con là __*nvme0n1p1*__ và __*nvme0n1p2*__ với dung lượng lần lượt là `512M` và `476.4G`
        - __*nvme0n1p1:*__ được _mount_ vào phân vùng `/boot/efi` đây là phân vùng khởi động nên đây là phân vùng của hệ điều hành.
        - __*nvme0n1p2:*__ được _mount_ vào phân vùng `/` là phân vùng quản lý dữ liệu cơ bản.

### Xem dung lượng sử dụng

Để xem dung lượng khả dụng của ổ dùng `df -h`

```bash
df -h
```
```text
Filesystem      Size  Used Avail Use% Mounted on
tmpfs           1.6G  5.2M  1.6G   1% /run
/dev/nvme0n1p2  468G  108G  337G  25% /
tmpfs           7.8G  8.3M  7.8G   1% /dev/shm
tmpfs           5.0M  8.0K  5.0M   1% /run/lock
efivarfs        256K   91K  161K  37% /sys/firmware/efi/efivars
/dev/nvme0n1p1  511M  6.3M  505M   2% /boot/efi
tmpfs           1.6G  120K  1.6G   1% /run/user/1000
```

Có rất nhiều thông tin nhưng hãy chú ý đến hai phân vùng `nvme0n1p1` và `nvme0n1p2`

- Như đã biết ở phần tên về ý nghĩa thì
- `nvme0n1p1` là phân vùng __*boot*__m gần như dữ liệu ở đây rất ít khi bị thay đổi _(trừ khi cập nhật hệ điều hành)_. `505MB` được cấp hơi lớn so với `6.3M` đã dùng thì hơi quá nhưng ổn.
- `nvme0n1p2` là phân vùng dữ liệu tổng _(bao gồm cả hệ điều hành)_. Có thể thấy người dùng đã sử dụng `108G` trên tổng số `468G` có thể dùng, chiếm __*25%*__ tổng dung lượng.

## Mount ổ cứng

!!! note "Note"
    Trong phần này trình bày các bước khởi tạo và bắt đầu một ổ cứng mới trên Ubuntu thông qua _command-line_

### Thiết lập phân vùng

Hầu hết các ổ cứng sẽ thường được các kỹ thuật viên khởi tạo hộ sẵn từ đầu nên sau khi kết nối sẽ được _mount_ sẵn. Trường hợp trên là có thêm một ổ cứng nữa được cắm sẵn vào thiết bị và là _ổ đĩa mới_ chưa có định dạng nên nó mới không có thông tin.

1. Tải về công cụ `parted` để tạo phân vùng cho ổ cứng _(nếu thiết bị chưa có)_:
    ```bash
    sudo parted /dev/sda
    ```
1. Tạo loại __partition table__ _(bảng phân vùng)_
    ```bash
    mklabel gpt
    ```
    - `gpt` hoặc `mbr`. Thường bây giờ sẽ dùng là `gpt` thay cho `mbr`
1. Cài đặt định dạng ổ cứng __*new partition*__
    ```text
    mkpart primary ext4 0% 100%
    sudo mkfs.ext4 /dev/sda1
    ```
    - Không nhất thiết phải dùng `ext4`, nhưng nên là `ext4` nếu đang hoạt động trên hệ điều hành __UNIX__. Các phân vùng khác thì là sử dụng chung với Windows như FAT, .. sẽ thường gây ra lỗi khi sử dụng. Tốt nhất có thể hiểu là nếu ổ cứng này thuộc quyền quản lý của hệ điều hành này thì nên để `ext4`
1. Kiểm tra lại với `lsblk`, nếu bảng đã có một phân vùng mới là `/dev/sda1` thì tức là thành công.
    ```text
    sda           8:0    0 931.5G  0 disk
    └─sda1        8:1    0 931.5G  0 part 
    ```
### Mount

Cài đặt cho ổ cứng thành công, phân vùng đã có, nhưng muốn sử dụng thì bắt buộc phải gắn cho nó một địa chỉ ảo trên hệ điều hành.

- Tạo một đại chỉ thư mục rỗng mới dùng làm địa chỉ ảo cho thiết bị phần cứng:
    ```text
    mkdir /storage
    ```
- Sau đó lệnh `mount` sẽ gán phân vùng của ổ cứng với địa chỉ thư mục vừa rồi:
    ```text
    sudo mount /dev/sda1 /storage/
    ```
- Lần này vẫn kiểm tra lại với `lsblk` sẽ thấy có phần __MOUNTPOINTS__
    ```text
    sda           8:0    0 931.5G  0 disk
    └─sda1        8:1    0 931.5G  0 part /storage
    ```

## Format

Nếu ổ cứng đang được sử dụng __*(mounted)*__ như trên thì phải hủy nó trước:

```bash
sudo umount /dev/sbXN
```

_Thay `XN` tương ứng._

### Format

```bash
sudo dd if=/dev/zero of=/dev/sdb bs=1M status=progress
```
