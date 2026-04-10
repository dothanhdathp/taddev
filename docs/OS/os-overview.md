# OS Overview

## Hệ điều hành là gì?

Hệ điều hành (Operating System - OS) là một phần mềm hệ thống quản lý và điều khiển mọi hoạt động của một thiết bị điện tử, bao gồm cả phần cứng và phần mềm. Nó đóng vai trò như một trung gian giữa người dùng và thiết bị, cho phép người dùng tương tác và sử dụng thiết bị một cách hiệu quả.

Nói đơn giản nhất nó chính là __Phần mềm / hệ phần mềm quản lý__ nhưng ở __cấp bậc cao nhất__

## Mục đích và vai trò

Các chức năng chính của hệ điều hành:

1. __Quản lý tiến trình _(Process Management)___:
    - Tạo, hủy, lập lịch và đồng bộ hóa các tiến trình.
2. __Quản lý bộ nhớ _(Memory Management)___:
    - Cấp phát, theo dõi và giải phóng bộ nhớ cho các tiến trình.
3. __Quản lý thiết bị _(Device Management)___:
    - Điều phối truy cập và giao tiếp với các thiết bị phần cứng.
4. __Quản lý hệ thống tệp _(File System Management)___:
    - Tổ chức, lưu trữ, truy xuất và bảo vệ dữ liệu trong hệ thống tệp.
5. __Quản lý người dùng và bảo mật _(Security & Access Control)___:
    - Xác thực người dùng, phân quyền và bảo vệ tài nguyên hệ thống.
6. __Giao tiếp giữa tiến trình (Inter-process _Communication - IPC)___:
    - Cho phép các tiến trình trao đổi dữ liệu và phối hợp hoạt động.
7. __Giao diện người dùng _(User Interface)___:
    - Cung cấp giao diện dòng lệnh hoặc đồ họa để người dùng tương tác.
8. __Quản lý tài nguyên hệ thống _(Resource Allocation)___:
    - Phân phối CPU, bộ nhớ, thiết bị I/O một cách hiệu quả.

## Phân Loại Hệ Điều Hành

### 1. Phân loại theo số lượng người dùng và nhiệm vụ

- **Đơn nhiệm, một người dùng (Single-user, Single-tasking)**: Chỉ một người có thể sử dụng và chỉ chạy được một chương trình tại một thời điểm. Ví dụ điển hình là MS-DOS.
- **Đa nhiệm, một người dùng (Single-user, Multi-tasking)**: Phổ biến trên máy tính cá nhân hiện nay. Một người dùng có thể chạy nhiều ứng dụng cùng lúc (như vừa soạn thảo văn bản vừa nghe nhạc). Ví dụ: Windows, macOS.
- **Đa người dùng (Multi-user)**: Cho phép nhiều người dùng truy cập và sử dụng tài nguyên hệ thống cùng một lúc, thường thấy trên các máy chủ (Servers). Ví dụ: Linux, Unix.

### 2. Phân loại theo cách xử lý (Processing Style)

Cách này tập trung vào việc hệ điều hành quản lý luồng công việc như thế nào:

- **Hệ thống xử lý theo lô (Batch Processing)**: Các công việc có tính chất giống nhau được gom lại thành một "lô" và thực hiện lần lượt. Người dùng không tương tác trực tiếp khi hệ thống đang chạy.
- **Hệ thống chia sẻ thời gian (Time-sharing)**: CPU luân chuyển cực nhanh giữa các tác vụ, tạo cảm giác như nhiều chương trình đang chạy đồng thời. Đây là cơ sở của các hệ điều hành hiện đại.
- **Hệ điều hành thời gian thực (Real-time OS - RTOS)**: Dùng cho các hệ thống yêu cầu độ chính xác cực cao về thời gian, nơi một phần nghìn giây cũng quan trọng.
- **Hard Real-time**: Lỗi thời gian là lỗi hệ thống (như túi khí ô tô, điều khiển tên lửa).
- **Soft Real-time**: Chấp nhận độ trễ nhỏ (như livestream video).

### 3. Phân loại theo thiết bị phần cứng

Tùy vào môi trường triển khai mà hệ điều hành được tối ưu hóa khác nhau:

- **Hệ điều hành máy tính (Desktop OS)**: Tối ưu cho chuột, bàn phím và giao diện đồ họa phức tạp (Windows, Linux Distros).
- **Hệ điều hành di động (Mobile OS)**: Tối ưu cho màn hình cảm ứng, tiết kiệm năng lượng và kết nối không dây (Android, iOS).
- **Hệ điều hành nhúng (Embedded OS)**: Được nạp vào chip của các thiết bị chuyên dụng như máy giặt, router Wi-Fi hay hệ thống điều khiển công nghiệp.
- **Hệ điều hành mạng (Network OS)**: Chạy trên máy chủ để quản lý dữ liệu, người dùng, nhóm, bảo mật và các chức năng mạng khác.

### 4. Phân loại theo cấu trúc nhân (Kernel Architecture)

Đối với người làm kỹ thuật hoặc nghiên cứu hệ thống, đây là cách phân loại quan trọng nhất:

| Loại nhân (Kernel) | Đặc điểm                                                                                                                   | Ví dụ                   |
| :----------------- | :------------------------------------------------------------------------------------------------------------------------- | :---------------------- |
| Monolithic Kernel  | Tất cả dịch vụ (file system, driver, VFS) chạy chung trong không gian nhân (kernel space). Tốc độ nhanh nhưng khó bảo trì. | Linux, BSD              |
| Microkernel        | Chỉ giữ những phần tối thiểu ở nhân, các dịch vụ khác đẩy ra không gian người dùng (user space). Tính ổn định cao.         | QNX, L4, Mach           |
| Hybrid Kernel      | Sự kết hợp giữa hai loại trên để cân bằng giữa hiệu năng và tính linh hoạt.                                                | Windows NT, macOS (XNU) |

## UNIX Và Unix-Like

### Unix-Like

Có khá nhiều hệ điều hành phổ biến, nhưng rất may chúng đều quy về hai mối chính để phân biệt là __Unix-like__ và phần còn lại.

#### Thế nào là Unix-Like

__Unix-Like__:

- Là tập hợp của các hệ điều hành sử dụng bộ hành vì và quản lý bộ nhớ, quyền, ... tương đồng với nhau. Hay nói cách khác, trải nghiệm người dùng trên những hệ điều hành này sẽ cảm thấy có rất nhiều điểm giống nhau.
- Gọi là _like (giống)_ vì các hệ điều hành dạng Unix-Like hoàn toàn không phải cùng nguồn gốc. Chúng có thể từ nhiều nguồn khác nhau nhưng mà vì cảm thấy Unix có cách tổ chức và hành vi tuyệt vời nên đã có tình làm giống như nó.
- Unix-like nổi tiếng, hay có thể nói rằng hệ điều hành tạo ra khái niệm __Unix-Like__ chính là __Linux__. Nhân Linux là tiền thân của vô vàn hệ điều hành sau này. Trong bốn hệ điều hành nổi danh nhất thế giới thì có tới ba cái đều học hỏi và ít nhiều kế thừa từ Linux:
    - Ubuntu: Con cả, dành cho máy tính bàn và là một trong những lựa chọn hàng đầu cho các máy server
    - iOS: Hệ điều hành của Apple, lõi cũng từ Linux và kế thừa khái niệm Unix-Like
    - Android: Hệ điều hành phổ biến nhất trên điện thoại, máy tính bảng, ... và các thiết bị khác. Cũng kế thừa từ Linux.
Và trong số đó chỉ có __Windows__ lựa chọn con đường khác. Nhưng đúng như thời gian đã chứng minh, __Windown__ cho người dùng trải nghiệm khá tốt với chuột nhưng cách tổ chức bộ nhớ rất tệ. Sau quãng thời gian dài sử dụng, rất nhiều người đã công nhận bộ _command_ và tổ chức bộ nhớ của Windows kém xa so với Linux. Nhưng ở nửa đầu của sự phát triển, nơi máy tính vẫn còn là một thứ công cụ phép thuật xa xỉ và khó hiểu thì chính hệ điều hành Windows mới là thứ đem chiếc máy tính khô khan đến với người dùng. __Window__ vẫn thành công và có họ riêng __VMS-like__ mặc dù không được nhiều người quan tâm.

#### Chia hệ điều hành theo đối tượng phát triển

Cách chia này khoa học và hợp lý hơn. Các hệ điều hành khác nhau có hành vi giống nhau nhưng thực chất, sâu bên trong vẫn còn rất nhiều điểm khác biệt. Lúc này sự phân loại theo bên phát triển sẽ hợp lý hơn. Ví dụ như cùng họ Unix like, Ubuntu cho máy tính để bàn với mục tiêu cung cấp một hệ điều hành tốt, ổn định và miễn phí hoàn toàn cho người dùng. Trong  khi đó hệ điều hành Android nhắm đến khả năng tích hợp với nhiều loại thiết bị phần cứng và đa dụng hơn. Các nhánh có thể phân biệt như sau:

| Developer                              | Hệ điều hành                                     |
| :------------------------------------- | :----------------------------------------------- |
| Microsoft                              | Windows                                          |
| Apple                                  | iOS, macOS                                       |
| Linux kernel developers + distributors | GNU/Linux, Debian, Ubuntu, Fedora, RHEL, Arch... |
| Google                                 | Android, Chrome OS                               |
| Others                                 |                                                  |

<mark>TO DO More ...</mark>

## Các Hệ Điều Hành Quan trọng

|           |                                 |                                           |                           |
| :-------- | :------------------------------ | :---------------------------------------- | :------------------------ |
| Microsoft | [Windows](Windows/windows.md)   |                                           |                           |
| Linux     | [Linux](./Linux/linux.md)       | [Ubuntu](./Linux/linux-install-ubuntu.md) | [Zorin](./Linux/zorin.md) |
| Google    | [Android](./Android/android.md) | Chrome OS                                 |                           |
| Apple     | iOS                             | MacOS                                     |                           |
| ROTS      |                                 |                                           |                           |

## Tham Khảo

- Gemini
- [Wikipedia Operating System](https://en.wikipedia.org/wiki/Operating_system)
- [Embedded Operating System](https://en.wikipedia.org/wiki/Embedded_operating_system)