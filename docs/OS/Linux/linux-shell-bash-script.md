# \[Linux\] Bash Script

- __Script__ hiểu đơn giản là thực thi một tập hợp của các lệnh _(command)_ theo một kịch bản thay vì điền từng dòng lên _terminal_
- Bash Script có tên đuôi là các tệp `.sh` và để hoạt động chỉ cần chạy chúng như các tệp thực thi thông thường.
    - Trên thực tế phần mở rộng `.sh` chỉ để xác định đây là tệp kịch bản. Có hay không không quan trọng.
- Bash Script bắt đầu với `#!/usr/bin/bash` để định hình cho tệp sẽ sử dụng công cụ __bash__ để đọc dòng lệnh, hoặc kiểu như là môi trường __bash__.

## Ví dụ

Tạo một tệp script mới.

```text
touch example.sh
```
Thêm quyền thực thi cho tệp

```text
sudo chmod +x ./example.sh
```
Dán nội dung sau vào tệp, có thể dùng nano hoặc vim hoặc bất kỳ trình chỉnh sửa văn bản nào.

```bash title="example.sh"
#!/usr/bin/bash

echo Hello World
```
```text title="Kết Quả"
Hello World
```

