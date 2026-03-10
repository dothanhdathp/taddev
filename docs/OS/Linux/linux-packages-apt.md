# Linux Apt

## APT

**APT** là viết tắt của **Advanced Package Tool**, tức là công cụ quản lý phần mềm, và các gói cài đặt trong linux.

Các chức năng của `apt`. Lưu ý lệnh `sudo` không nằm trong tập lệnh gốc, nó chỉ là lệnh dùng để yêu cầu truy cập với quyền quản trị viên vì việc cài mới một ứng dụng tự do khá là nguy hiểm với hệ điều hành.

- 
```bash
sudo apt get install {package-name}
```

### Các Gói Đã Cài

Hiển thị toàn bộ danh sách các ứng dụng đã tải

```bash
apt list --installed
```

