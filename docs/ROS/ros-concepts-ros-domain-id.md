# \[ROS\] ROS_DOMAIN_ID

> Nguồn: [https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Domain-ID.html](https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Domain-ID.html)

## Overview
> Tổng quan

Như đã giải thích ở nơi khác, phần mềm trung gian mặc định mà ROS 2 sử dụng để liên lạc là __DDS__. Trong __DDS__, cơ chế chính để các mạng logic khác nhau chia sẻ mạng vật lý được gọi là __Domain ID__. Các nút ROS 2 trên cùng một miền có thể tự do khám phá và gửi tin nhắn cho nhau, trong khi các nút ROS 2 trên các miền khác nhau thì không thể. Tất cả các nút ROS 2 đều sử dụng __Domain ID__ 0 theo mặc định. Để tránh nhiễu giữa các nhóm máy tính khác nhau chạy ROS 2 trên cùng một mạng, nên đặt một __Domain ID__ khác nhau cho mỗi nhóm.

## Choosing a domain ID (short version)
> Chọn __Domain ID__ (phiên bản ngắn)

Văn bản bên dưới giải thích nguồn gốc của phạm vi __Domain ID__ nên được sử dụng trong ROS 2. Để bỏ qua thông tin cơ bản đó và chỉ chọn một số an toàn, chỉ cần chọn __Domain ID__ trong khoảng từ 0 đến 101.

## Choosing a domain ID (long version)
> Chọn __Domain ID__ (phiên bản dài)

__Domain ID__ được __DDS__ sử dụng để tính toán các cổng UDP sẽ được sử dụng để khám phá và liên lạc. Xem bài viết này để biết chi tiết về cách tính toán các cổng. Hãy nhớ mạng cơ bản của chúng tôi, cổng UDP là số nguyên 16 bit không dấu. Do đó, số cổng cao nhất có thể được chỉ định là 65535. Thực hiện một số phép toán với công thức trong bài viết trên, điều này có nghĩa là __Domain ID__ cao nhất có thể được chỉ định là 232, trong khi __Domain ID__ thấp nhất có thể được chỉ định là 0.

### Platform-specific constraints
> Các ràng buộc dành riêng cho nền tảng

Để có khả năng tương thích tối đa, cần tuân thủ một số ràng buộc bổ sung dành riêng cho nền tảng khi chọn __Domain ID__. Đặc biệt, tốt nhất là tránh phân bổ __Domain ID__ trong phạm vi cổng tạm thời của hệ điều hành. Điều này tránh được những xung đột có thể xảy ra giữa các cổng được nút ROS 2 sử dụng và các dịch vụ mạng khác trên máy tính.

Dưới đây là một số lưu ý dành riêng cho nền tảng về các cổng tạm thời.

=== "Linux"
    Theo mặc định, nhân Linux sử dụng các cổng `32768-60999` cho các cổng phù du. Điều này có nghĩa là __*domain IDs*__ `0-101` và `215-232` có thể được sử dụng một cách an toàn mà không va chạm với các cổng phù du. Phạm vi cổng tạm thời có thể được cấu hình trong Linux bằng cách đặt các giá trị tùy chỉnh trong `/proc/sys/net/ipv4/ip_local_port_range`. Nếu sử dụng phạm vi cổng tạm thời tùy chỉnh, các con số trên có thể phải được điều chỉnh cho phù hợp.
=== "macOS"
    Theo mặc định, phạm vi cổng tạm thời trên __macOS__ là `49152-65535`. Điều này có nghĩa là ID miền 0-166 có thể được sử dụng một cách an toàn mà không va chạm với các cổng tạm thời __*(ephemeral port)*__. Có thể định cấu hình phạm vi cổng tạm thời trong __macOS__ bằng cách đặt các giá trị `sysctl` tùy chỉnh cho `net.inet.ip.portrange.first` và `net.inet.ip.portrange.last`. Nếu sử dụng phạm vi cổng tạm thời tùy chỉnh, các con số trên có thể phải được điều chỉnh cho phù hợp.
=== "Windows"
    By default, the ephemeral port range on __Windows__ là `49152-65535`. Điều này có nghĩa là __*domain IDs*__ `0-166` có thể được sử dụng một cách an toàn mà không va chạm với các cổng phù du. Phạm vi cổng tạm thời có thể được cấu hình trong Windows bằng cách sử dụng `netsh`. Nếu sử dụng phạm vi cổng tạm thời tùy chỉnh, các con số trên có thể phải được điều chỉnh cho phù hợp.

### Participant constraints
> Những ràng buộc của người tham gia

Đối với mỗi tiến trình ROS 2 chạy trên máy tính, một DDS __*“participant” (người tham gia)*__ được tạo ra. Vì mỗi người tham gia DDS chiếm hai cổng trên máy tính nên việc chạy hơn 120 quy trình ROS 2 trên một máy tính có thể tràn sang các ID miền khác hoặc các cổng tạm thời.

Để biết lý do tại sao, hãy xem xét ID miền 1 và 2.

- ID miền 1 sử dụng cổng 7650 và 7651 cho phát đa hướng.
- ID miền 2 sử dụng cổng 7900 và 7901 cho phát đa hướng.
- Khi tạo quy trình đầu tiên (người tham gia thứ 0) trong miền ID 1, các cổng 7660 và 7661 được sử dụng cho unicast.
- Khi tạo quy trình thứ 120 (người tham gia thứ 119) trong miền ID 1, các cổng 7898 và 7899 được sử dụng cho unicast.
- Khi tạo quy trình thứ 121 (người tham gia thứ 120) trong miền ID 1, các cổng 7900 và 7901 được sử dụng cho unicast và chồng chéo với ID miền 2.
- Nếu biết rằng máy tính sẽ chỉ sử dụng một ID miền tại một thời điểm và ID miền đủ thấp thì việc tạo nhiều quy trình ROS 2 hơn mức này là an toàn.
- Khi chọn ID miền gần đầu phạm vi ID miền dành riêng cho nền tảng, cần xem xét một hạn chế bổ sung.
- Ví dụ: giả sử một máy tính Linux có ID miền là 101:
- Quá trình zero’th ROS 2 trên máy tính sẽ kết nối với các cổng 32650, 32651, 32660 và 32661.
- Quá trình ROS 2 đầu tiên trên máy tính sẽ kết nối với các cổng 32650, 32651, 32662 và 32663.
- Quá trình ROS 2 thứ 53 trên máy tính sẽ kết nối với các cổng 32650, 32651, 32766 và 32767.
- Quá trình ROS 2 thứ 54 trên máy tính sẽ kết nối với các cổng 32650, 32651, 32768 và 32769, chạy vào phạm vi cổng phù du.

Do đó, số lượng quy trình tối đa cần được tạo khi sử dụng ID miền 101 trên Linux là 54. Tương tự, số lượng quy trình tối đa cần tạo khi sử dụng ID miền 232 trên Linux là 63, vì số cổng tối đa là 65535.

Tình trạng tương tự trên macOS và Windows, mặc dù con số khác nhau. Trên macOS và Windows, khi chọn ID miền là 166 (đầu phạm vi), số lượng quy trình ROS 2 tối đa có thể được tạo trên máy tính trước khi chạy vào phạm vi cổng tạm thời là 120.

### Domain ID to UDP Port Calculator

- Domain ID: 0
- Participant ID: 0
- Discovery Multicast Port: `7400`
- User Multicast Port: `7401`
- Discovery Unicast Port: `7410`
- User Unicast Port: `7411`
