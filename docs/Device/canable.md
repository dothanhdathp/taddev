# CANable

## Tổng quan

CANable 2.0 là một bộ chuyển đổi USB sang CAN nhỏ gọn, giá rẻ, mã nguồn mở. CANable được nhận diện như một cổng nối tiếp ảo trên máy tính của bạn và hoạt động như một giao diện đường truyền nối tiếp sang bus CAN. Với phần mềm tùy chọn candleLight , CANable được nhận diện như một giao diện CAN gốc trên Linux. CANable 2.0 hỗ trợ cả CAN tiêu chuẩn và CAN-FD.

Bộ chuyển đổi CANable tương thích với các nền tảng nhúng dựa trên ARM như Raspberry Pi, Raspberry Pi Zero, ODROID, BeagleBone, v.v. và rất phù hợp để tích hợp vào các sản phẩm OEM.

## Tính năng CANable 2.0

- Hỗ trợ CAN2.0A và B, tốc độ truyền dữ liệu lên đến 1M.
- Hỗ trợ SLCan ban đầu cho CAN-FD (phiên bản beta, 2M/5Mbaud)
- Tương thích với socketcan thông qua slcand
- Đầu nối USB-C và các lỗ gắn có thể tháo rời
- Đầu nối vít 4 chân: CANH, CANL, 5V (đầu ra), GND
- Nút để vào chế độ bootloader
- Công tắc để bật/tắt tính năng chấm dứt hoạt động trên bo mạch
- Thư viện Python đơn giản, đa nền tảng
- Sản xuất tại Hoa Kỳ
- Có thể mua sản phẩm tại Openlight Labs.

## Hỗ trợ phần mềm

- **Cangaroo (Windows, Linux)**: Gửi/nhận các khung dữ liệu chuẩn và FD, giải mã thông báo từ các tệp DBC.
- **SocketCAN (Linux)** Hỗ trợ Linux gốc bằng slcand
- _**python-can (Windows, Linux, Mac)**_ Dễ dàng giao tiếp với bus CAN bằng cách sử dụng CANable và các tập lệnh Python của bạn.



## Tham Khảo

- [Trang chủ CANable](https://canable.io/)