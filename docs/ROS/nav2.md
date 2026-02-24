# \[Nav2\]

> Về hệ thống dẫn đường trong robot, hỗ trợ và tương tác khá là mạnh với __ROS__
<br> Trang chủ: [https://docs.nav2.org/](https://docs.nav2.org/)

## Overview

Nav2 là phiên bản kế thừa được hỗ trợ chuyên nghiệp của __ROS Navigation Stack__, triển khai các loại công nghệ tương tự cung cấp năng lượng cho __Phương tiện Tự Hành__ (_Autonomous Vehicles_) đã được gỡ bỏ, tối ưu hóa và làm lại cho _mobile_ và _surface robotics_. Dự án này cho phép rô-bốt di động điều hướng trong các môi trường phức tạp để hoàn thành các tác vụ ứng dụng do người dùng xác định với hầu hết mọi loại động học rô-bốt. Nó không chỉ có thể di chuyển từ Điểm A đến Điểm B mà còn có thể có các tư thế trung gian và thể hiện các loại nhiệm vụ khác như theo dõi đối tượng, điều hướng vùng phủ sóng hoàn chỉnh, v.v. Nav2 là khung điều hướng chất lượng cao và cấp sản xuất được hơn 100 công ty trên toàn thế giới tin cậy.

Nó cung cấp nhận thức, lập kế hoạch, kiểm soát, bản địa hóa, trực quan hóa và nhiều hơn thế nữa để xây dựng các hệ thống tự trị có độ tin cậy cao. Điều này sẽ tính toán mô hình môi trường từ dữ liệu cảm biến và ngữ nghĩa, sơ đồ đường đi linh hoạt, tính toán vận tốc cho động cơ, tránh chướng ngại vật và cấu trúc các hành vi của robot cấp cao hơn. Để tìm hiểu thêm về dự án này, chẳng hạn như các dự án liên quan, việc sử dụng robot, so sánh ROS1 và người bảo trì, hãy xem Giới thiệu và Liên hệ. Để tìm hiểu thêm về các khái niệm điều hướng và ROS, hãy xem Khái niệm điều hướng.

Nav2 sử dụng cây hành vi để tạo hành vi điều hướng thông minh và tùy chỉnh thông qua việc phối hợp nhiều máy chủ mô-đun độc lập. Máy chủ tác vụ có thể được sử dụng để tính toán đường dẫn, nỗ lực kiểm soát, hành vi hoặc bất kỳ tác vụ nào khác liên quan đến điều hướng. Các máy chủ riêng biệt này giao tiếp với cây hành vi (BT) qua giao diện ROS, chẳng hạn như máy chủ hành động hoặc dịch vụ. Robot có thể sử dụng nhiều cây hành vi khác nhau để cho phép robot thực hiện nhiều loại nhiệm vụ độc đáo và phức tạp.

Sơ đồ dưới đây sẽ cho bạn cái nhìn đầu tiên về cấu trúc của Nav2. Lưu ý rằng có thể có nhiều plugin cho bộ điều khiển, trình lập kế hoạch và khôi phục trong mỗi máy chủ của họ. Điều này có thể được sử dụng để tạo hành vi điều hướng theo ngữ cảnh. Mỗi máy chủ cũng trả lại các chỉ báo trạng thái cho BT Navigator để thực hiện các hành vi theo ngữ cảnh dựa trên kết quả của chúng.

Đầu vào dự kiến ​​cho Nav2 là các phép biến đổi TF tuân theo __REP-105__, nguồn bản đồ nếu sử dụng Lớp sơ đồ chi phí tĩnh, tệp BT XML và mọi nguồn dữ liệu cảm biến có liên quan. Sau đó, nó sẽ cung cấp các lệnh vận tốc hợp lệ để động cơ của robot toàn diện hoặc không toàn diện tuân theo khi được cấu hình đúng. Chúng tôi hiện hỗ trợ tất cả các loại robot chính: loại cơ sở ba chiều, dẫn động vi sai, có chân và ackermann (giống ô tô)! Chúng tôi hỗ trợ chúng một cách độc đáo bằng cả robot hình tròn và robot có hình dạng tùy ý để kiểm tra va chạm SE2.

Nó có các công cụ để:

- Tải, phục vụ và lưu trữ bản đồ
- Định vị robot trên bản đồ được cung cấp (SLAM cung cấp bản đồ ban đầu)
- Lập kế hoạch một đường đi hoàn chỉnh xuyên qua môi trường, thậm chí khả thi về mặt động học cho các robot lớn
- Điều khiển robot đi theo đường đi và tự động điều chỉnh tránh va chạm
- Kế hoạch trơn tru để liên tục, suôn sẻ và/hoặc khả thi hơn
- Chuyển đổi dữ liệu cảm biến thành mô hình môi trường của thế giới
- Xây dựng các hành vi robot phức tạp và có khả năng tùy biến cao bằng cách sử dụng cây hành vi
- Thực hiện các hành vi được xác định trước trong trường hợp thất bại, có sự can thiệp của con người hoặc các hành vi khác
- Thực hiện theo các điểm tham chiếu tuần tự bao gồm một nhiệm vụ
- Quản lý vòng đời chương trình của hệ thống và cơ quan giám sát cho máy chủ
- Các plugin được tải động dễ dàng để tạo các thuật toán, hành vi tùy chỉnh, v.v.
- Giám sát dữ liệu cảm biến thô về va chạm sắp xảy ra hoặc tình huống nguy hiểm
- API Python3 để tương tác với Nav2 và các máy chủ tác vụ nội bộ của nó theo cách Pythonic
- Tốc độ đầu ra mượt mà hơn để đảm bảo tính khả thi của các lệnh
- … và hơn thế nữa!

<figure markdown="span">
    ![](img/nav2_architecture.png)
    <figcaption>Bản đồ cấu trúc điều khiển cơ bản của Nav2</figcaption>
</figure>

Chúng tôi cũng cung cấp một bộ plugin khởi đầu để giúp bạn tiếp tục. Bạn có thể tìm thấy danh sách tất cả các plugin trên [Navigation Plugin](https://docs.nav2.org/plugins/index.html#plugins) - nhưng chúng bao gồm các thuật toán về mặt cắt ngang bao gồm các hành vi phổ biến và các loại nền tảng robot.

## Phân Phối

__Nav2__ có sẵn trên nhiều bản phân phối ROS 2 với các mức hỗ trợ khác nhau:

| Phiên Bản           | Trạng Thái                              |
| :------------------ | :-------------------------------------- |
| Rolling Ridley      | Development                             |
| Kilted Kaiju        | <mark class=green>Active Support</mark> |
| Jazzy Jalisco       | <mark class=green>Active Support</mark> |
| Iron Irwini         | <mark class=red>End of Life</mark>      |
| Humble Hawksbill    | Maintained                              |
| Galactic Geochelone | <mark class=red>End of Life</mark>      |