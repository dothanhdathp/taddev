# RTOS

Để học tập và nghiên cứu về RTOS, việc lựa chọn phần cứng phù hợp sẽ giúp bạn quan sát được sự khác biệt rõ rệt giữa lập trình tuần tự truyền thống (Super Loop) và lập trình đa nhiệm.

## 1. Thiết bị phần cứng phổ biến cho RTOS

Dưới đây là các dòng board mạch được cộng đồng hỗ trợ mạnh mẽ nhất:

- **STM32 (Dòng Discovery hoặc Nucleo)**: Đây là lựa chọn hàng đầu trong công nghiệp. STM32 hỗ trợ cực tốt cho FreeRTOS thông qua công cụ cấu hình đồ họa STM32CubeMX.
- **ESP32**: Một lựa chọn rất kinh tế vì nó tích hợp sẵn Wi-Fi, Bluetooth và quan trọng nhất là FreeRTOS được tích hợp sâu vào bộ SDK (ESP-IDF). ESP32 có 2 nhân (dual-core), giúp bạn học được cả cách quản lý RTOS trên hệ thống đa nhân.
- **Raspberry Pi Pico**: Sử dụng chip RP2040, hỗ trợ tốt cho cả FreeRTOS và Zephyr. Nó có tài liệu hướng dẫn rất chi tiết cho người mới.
- **Arduino (Các dòng ARM như Due hoặc Nano Every)**: Dù Arduino Uno (AVR) có thể chạy RTOS nhưng bộ nhớ rất hạn chế. Bạn nên dùng các dòng chạy chip ARM để có trải nghiệm mượt mà hơn.

## 2. Các khái niệm cốt lõi nên bắt đầu từ đâu?

Đừng vội vàng viết code ngay. Bạn nên tìm hiểu các khái niệm theo lộ trình sau để xây dựng tư duy "thời gian thực":

### Giai đoạn 1: Quản lý tác vụ (Task Management)

Đây là nền móng của mọi RTOS.

- **Task (Tác vụ)**: Hiểu rằng mỗi task là một hàm chạy độc lập với vòng lặp vô tận.
- **Scheduler (Bộ lập lịch)**: Cách RTOS quyết định task nào được chạy tiếp theo (thường dựa trên độ ưu tiên).
- **Context Switching (Chuyển đổi ngữ cảnh)**: Cơ chế CPU lưu lại trạng thái của task này để nhảy sang task khác.

### Giai đoạn 2: Điều phối và Đồng bộ (Synchronization)

Khi các tác vụ cần nói chuyện với nhau hoặc dùng chung tài nguyên (như một cổng UART).

- **Semaphore**: Dùng để đồng bộ hóa (ví dụ: Task A chờ Task B xong mới được chạy).
- **Mutex (Mutual Exclusion)**: Dùng để bảo vệ tài nguyên dùng chung, tránh việc hai task cùng ghi dữ liệu vào một chỗ gây lỗi.
- **Queues (Hàng đợi)**: Cách an toàn để gửi dữ liệu giữa các task.

### Giai đoạn 3: Quản lý thời gian và Ngắt

- **Software Timers**: Tạo các sự kiện lặp lại sau một khoảng thời gian nhất định.
- **Interrupt Management**: Cách RTOS xử lý các ngắt từ phần cứng (nút nhấn, cảm biến) mà không làm treo hệ thống.

## 3. Tài liệu học tập đề xuất

- **Cuốn sách "Mastering the FreeRTOS Real Time Kernel"**: Đây là "kinh thánh" cho người mới bắt đầu. Nó giải thích cực kỳ dễ hiểu về cơ chế bên trong của RTOS.
- **Khóa học Udemy**: Các khóa học của FastBit Embedded Brain Academy về RTOS là những tài liệu thực hành rất chất lượng trên dòng STM32.
- **Trang chủ Zephyr Project**: Nếu bạn muốn theo hướng hiện đại và làm các dự án IoT chuyên nghiệp.

!!! tip "Lời khuyên cho bạn"
    Hãy bắt đầu bằng cách mô phỏng trên Ubuntu (như đã thảo luận ở trên) để hiểu cách Task và Queue hoạt động trước, sau đó mới chuyển sang nạp code vào board mạch thật để xử lý các vấn đề về ngắt (Interrupt) và phần cứng.