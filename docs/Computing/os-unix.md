# UNIX

- Tồn tại từ rất rất lâu, UNIX là một hệ điều hành cổ đại từ những năm 1969 với phiên bản nổi tiếng nhất là **UNIX System V**
- Sự thành công của hệ điều hành này không phải đến từ bản thân nó mà đến từ cái gọi là **Triết Lý UNIX**, nền tảng cho các hệ điều hành sau này học tập và làm theo _(trừ Windows của Microsoft)_
- Các khái niệm chung của **Linux** mà được định nghĩa từ **UNIX** sẽ được trình bày ở đây.

## Triết Lý UNIX

**Triết Lý UNIX** là một khái niệm tổng hợp, không phải là khái niệm được công nhận rộng rãi. Nó gồm các yêu cầu quy chuẩn cho một hệ điều hành cơ bản như sau:

1. Hệ điều hành nên cung cấp các công cụ đơn giản, mỗi công cục có <mark>chức năng hạn chế</mark> và <mark>nhiệm vụ rõ ràng</mark>
1. Hệ thống tệp thống nhất và dựa trên [inode](https://en.wikipedia.org/wiki/Inode)
1. Giao tiếp giữa các tiến trình được gọi là các _đường ống_ 
1. Một ngôn ngữ tập lệnh và kịch bản gọi là _(**shell**)_ được sử dụng để kết hợp các công việc thành công việc phức tạp.