# Sed

## Overview

- Lệnh này là lệnh dùng để chỉnh sửa một đoạn văn bản trong tệp từ bên ngoài.
- __sed__ là viết tắt của __stream editor__

## Kiến trúc

```bash
sed [options] 'command' filename
```

## Cơ bản

### Thay đổi từ

#### Xem thay đổi

!!! Note "Ghi chú"
    Bước này không làm thay đổi nội dung gốc của tệp đích. Sau khi dùng lệnh thì kết quả ví dụ của tệp mẫu được hiện ra.

Thay đổi tất cả các `old str` thành `new str` trong tệp `example.txt` như sau:

```bash
sed 's/[old str]/[new str]/g' example.txt
```

Trường hợp có _ký tự đặc biệt_ thì `'\<special_word>'`, ví dụ đổi __*should*__ thành __*shouldn't*__ như sau:

```bash
sed 's/should/new should'\''t/g' text.txt
```

- Ký tự đặc biệt là `'` được đặt <u>phía sau</u> `\` và <u>bên trong</u> hai dấu nháy đơn `'`

