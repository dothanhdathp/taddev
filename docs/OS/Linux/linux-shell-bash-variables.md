# Biến Trong Bash

Biến trong bash rất dễ khai báo. Ví dụ

```bash
i=10; echo $i;
```

Kết quả là 10 vì `i` đã được gán kết quả.

- Giá trị của biến được tồn tại trong một _session_, hoặc là _terminal_ khai báo biến đó. Khi sang terminal khác, giá trị của nó cũng thay đổi.
- Giá trị của biến nếu được khai báo trong tệp script như `script.sh` thì giá trị được tạo chỉ còn giá trị nội bộ trong tệp, nó không tác động đến môi trường chung.

## 