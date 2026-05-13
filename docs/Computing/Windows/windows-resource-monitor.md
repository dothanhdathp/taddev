# Windows Resource Monitor

- **Resource Monitor** quản lý các tệp và các tiến trình sử dụng tệp.

## Mở Resource Monitor

1. Vào _**Run**_ gõ `resmon`

## Ứng Dụng

### Tìm tiến trình đang kiểm soát tệp

Thi thoảng khi xóa tệp, thư mục nào đó mà máy báo là tệp / thư mục đó đang được sử dụng bởi một tiến trình nào đó nên không thể xóa, bạn có thể thử cách sau: 

- [Mở Resource Monitor](#mo-resource-monitor)
- Chuyển hướng sang mục **CPU / Associated Handles** và vào ô tìm kiếm.
- Điền tên đầy đủ đường dẫn vào mục tìm kiếm sẽ ra tiến trình đang giữ tệp.
    ![alt text](<img/windows-resource-monitor-0.png>)