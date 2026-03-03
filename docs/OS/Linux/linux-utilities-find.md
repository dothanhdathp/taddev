# Linux Find

Lệnh này là lệnh khá là phổ biến dùng để tìm kiếm tệp và thực thi trên các tệp.

```bash
# Tìm với tên
find -name NAME

# Tìm với định dạng
find -name "*.ext"

# Tìm các thư mục
find -type d

# Tìm các tệp thực thi
find -type f

# Tìm các tệp / thư mục theo tên
find -type f -name NAME
find -type d -name NAME

# Tìm các tệp / thư mục theo tên. Và thực thi với mỗi kết quả
find ./ -type d -name NAME -exec {command} +
find ./ -type f -name NAME -exec {command} +
```

```bash title="Đổi mode tất cả"
find ./ -type d -exec chmod 744 {} +
find ./ -type f -exec chmod 744 {} +
```