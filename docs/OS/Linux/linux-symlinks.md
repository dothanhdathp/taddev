# Linux Symlinks

> Tạo _symlinks_ trong __*Linux*__

__*Symlinks*__ dạng giống như _shortcut_ có trong Windows, dạng một đường dẫn ngắn tới một tệp, hoặc thư mục ở vị trí khác mà không cần phải di chuyển toàn bộ tệp đích tới vị trí thực thi.

## Công thức

```bash
ln -s {target} {new-link}
```

__Lệnh này nên cẩn thận khi sử dụng vì nó nếu sử dụng ngược, địa chỉ đích sẽ bị thay đổi và khá nguy hiểm.__