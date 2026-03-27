# Linux Bash - So Sánh

## So Sánh Số

```bash
#!/usr/bin/bash

# set i=5
i=5;

# Equal
if [ $i -eq 0 ]; then echo "5 = 0 is true"; else echo "5 = 0 is false"; fi;
# Greater
if [ $i -gt 0 ]; then echo "5 > 0 is true"; else echo "5 > 0 is false"; fi;
# Lower
if [ $i -lt 0 ]; then echo "5 < 0 is true"; else echo "5 < 0 is false"; fi;
# Greater + Equal
if [ $i -ge 5 ]; then echo "5 >= 5 is true"; else echo "5 >= 5 is false"; fi;
# Lower + Equal
if [ $i -le 4 ]; then echo "5 <= 4 is true"; else echo "5 <= 4 is false"; fi;
```

## Kiểm Tra Tệp

Kiểm tra tệp tồn tại hay không với

| Cờ               | Tác Dụng                                                                 |
| :--------------- | :----------------------------------------------------------------------- |
| `-e` (exist)     | Trả về true nếu **tệp hoặc thư mục tồn tại**.                            |
| `-f` (file)      | Trả về true nếu **đường dẫn tồn tại và là một tệp thông thường**.        |
| `-d` (directory) | Trả về true nếu **đường dẫn tồn tại và là một thư mục**.                 |
| `-s` (size)      | Trả về true nếu **tệp tồn tại và có kích thước lớn hơn 0 (không rỗng)**. |
| `-r` (read)      | Trả về true nếu **tệp tồn tại** và **có quyền đọc**.                     |

```bash
if [ -e ~/.bashrc ]; then echo true; else echo false; fi;
```

Kết quả là **true** _(`~/.bashrc` là tệp cấu hình người dùng mặc định sẽ luôn tồn tại trong userspace của **Linux**)_