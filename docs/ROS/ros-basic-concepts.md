# ROS Concepts

> Tìm hiểu về các khái niệm cơ bản.
<br>Tham khảo: [link](https://docs.ros.org/en/jazzy/Concepts.html)

## Tổng Quan

Ở phần này sẽ bắt đầu tìm hiểu những thành phần đầu tiên của __ROS__. Các khái niệm cần tìm hiểu là:

- Nodes
- Topics
- Services
- Parameters
- Actions

`turtlesim` thuộc về một phần khác nơi bạn sẽ điều khiển một con rùa làm gì đó.

Các khái niệm cơ bản này không có thay đổi giữa các phiên bản khác nhau quá nhiều. Chúng về cơ bản là những __*thành phần cơ sở - cốt lõi*__ của __ROS__

## ROS Graph

Khái niệm này không có trong mục __*Concepts*__ gốc. __*ROS Graph*__ nói đến một mạng lưới tổng, một __*hệ thống*__ của __ROS__ được xây dựng từ các thành phần cơ bản. Một mạng lưới ROS nhìn đại khái như sau:

<figure markdown="span">
    ![](img/Nodes-TopicandService.gif)
    <figcaption>Một ví dụ về đổ thị ROS</figcaption>
</figure>

## Nodes

- Nguồn Tham Khảo: [About-Nodes](https://docs.ros.org/en/jazzy/Concepts/Basic/About-Nodes.html)

!!! quote "Định Nghĩa Gốc"
    Nút là người tham gia vào biểu đồ ROS 2, sử dụng thư viện máy khách để liên lạc với các nút khác. Các nút có thể giao tiếp với các nút khác trong cùng một quy trình, trong một quy trình khác hoặc trên một máy khác. Các nút thường là đơn vị tính toán trong biểu đồ ROS; mỗi nút nên làm một việc hợp lý.

    Các nút có thể xuất bản lên các chủ đề được đặt tên để phân phối dữ liệu đến các nút khác hoặc đăng ký các chủ đề được đặt tên để nhận dữ liệu từ các nút khác. Họ cũng có thể hoạt động như một máy khách dịch vụ để nhờ một nút khác thay mặt họ thực hiện tính toán hoặc như một máy chủ dịch vụ để cung cấp chức năng cho các nút khác. Đối với các tính toán kéo dài, một nút có thể hoạt động như một máy khách hành động để nhờ một nút khác thực hiện thay mặt chúng hoặc như một máy chủ hành động để cung cấp chức năng cho các nút khác. Các nút có thể cung cấp các tham số có thể định cấu hình để thay đổi hành vi trong thời gian chạy.

    Các nút thường là sự kết hợp phức tạp của nhà xuất bản, người đăng ký, máy chủ dịch vụ, máy khách dịch vụ, máy chủ hành động và máy khách hành động, tất cả cùng một lúc.

    Kết nối giữa các nút được thiết lập thông qua quá trình khám phá phân tán.

__*Nodes*__ hay _Các Nút_ là thành phần cơ bản đầu tiên. Các Nút đại diện cho một _module_, một nút sẽ _(nên)_ thực thi một chức năng xác định. Ví dụ như trong một robot dò đường thì __*nodes*__ có thể là khối điều khiển bánh xe. Bốn bánh xe sẽ có 4 nút. Hoặc là hai nút với mỗi nút điều khiển bánh hai xe trước / sau _(việc đó tùy thuộc vào người thực hiện)_.

Để mô tả Node gần giống như công nhân thực hiện nhiệm vụ trực tiếp.

## Topic

__Topic__ là một <mark>phương thức giao tiếp</mark> giữa các __Nodes__. Nó có hai thành phần là:

- __Publisher__ _(người xuất bản)_
- __Subcriber__ _(người lắng nghe)_

### Hoạt Động

- __Publisher__ sẽ gửi một bản tin __Message__ tới __Topic__.
- __Topic__ sẽ thông báo bản tin đó tới tất cả các __Subcriber__.

<figure markdown="span">
    ![](img/Topic-SinglePublisherandSingleSubscriber.gif)
    <figcaption>Một nút có thể xuất bản dữ liệu tới bất kỳ số lượng chủ đề nào và đồng thời có đăng ký tới bất kỳ số lượng chủ đề nào.</figcaption>
</figure>

<figure markdown="span">
    ![](img/Topic-MultiplePublisherandMultipleSubscriber.gif)
    <figcaption>Chủ đề là một trong những cách chính để dữ liệu được truyền tải giữa các nút và do đó giữa các phần khác nhau của hệ thống.</figcaption>
</figure>

Thế nên, trong cách thức liên lạc này, người xuất bản sẽ không thể nào đảm bảo được bản tin sẽ đến được người nghe. Cơ chế này cũng không xác đinh người gửi. Miễn là có quyền thì __Publisher__ có thể đẩy bản tin lên một __Topic__, và miễn là đăng ký thì phía __Subcriber__ có thể lắng nghe được bản tin đó.

### Ví dụ

- [Publisher and Subscriber](ros-jazzy-jalisco-example-pub-sub.md)

## Service

__Service__ là cơ chế tiếp theo, cũng là thuộc một trong những kiểu phương thức liên lạc giữa các Node với nhau. Cơ chế này có 4 khái niệm liên quan là __Service Client__, __Service Server__, __Message Request__ và __Message Respond__.

Cách  thức hoạt động của Service sẽ theo một vòng cụ thể và rõ ràng có mục đích. Trong cơ chế này thì:

__Service Server__ sẽ nhận yêu cầu qua __Message Request__ được gửi từ __Service Client__ và thực hiện một hành động nào đấy. Phía __Service Server__ có thể trả lại __Message Respond__ cho __Service Client__.

<figure markdown="span">
    ![](img/Service-SingleServiceClient.gif)
    <figcaption>Single Service/Client</figcaption>
</figure>

<figure markdown="span">
    ![](img/Service-MultipleServiceClient.gif)
    <figcaption>Multiple Service/Client</figcaption>
</figure>

## So Sánh Topic Với Service

Việc triển khai của __Topic__ giống như là thông báo, thường nó sẽ có hướng giống như để ghi nhật ký hơn là hoạt động. Tuy rằng đôi khi các Nodes có thể đọc bản tin và điều chỉnh hành vi nếu một Node nào đó gặp trục trặc và chỉ còn có thể thông báo lên topic rằng nó sắp dừng hoạt động. Nhưng nhìn chung cơ chế này mang ý nghĩa __Thông Báo__.

Cơ chế __Service__ lại mang nhiều hướng về hoạt động hơn. Ở __Service__ có sự yêu cầu đồng bộ về hoạt động. Nếu thiết kế đúng tức là hành vi tiếp theo của một __Nodes__ sẽ cần nhận được trạng thái, hoặc sự điều chỉnh từ một __Nodes__ khác để hoạt động ổn định. Để làm rõ có thể xem ví dụ:

_Một chiếc xe tự hành có __Nodes__ là bánh xe. Khi hoạt động Nodes điều khiển bánh xe xác định nó gặp trục trặc và không thể quay, thế nên nó bắt đầu yêu cầu lên __Server__ để quy định trạng thái tiếp theo. Ở __Server__ có  thể đọc trạng thái từ __Camera__ và nhận thấy xe đang có vật cản, thế nên nó có thể yêu cầu __Nodes__ điều khiển bánh xe tăng sức mạnh động cơ lên để vượt qua vật cản. Khi yêu cầu được trả xuống, có thể sẽ có thêm yêu cầu __Nodes__ bánh xe lắng nghe phản hồi từ phía __Server__ để điều chỉnh tốc độ bánh về như cũ sau khi đã vượt qua._

## Tham Khảo

1. [Understanding ROS2 Nodes](https://docs.ros.org/en/jazzy/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Nodes/Understanding-ROS2-Nodes.html)
1. [Understanding ROS2 Topics](https://docs.ros.org/en/jazzy/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Topics/Understanding-ROS2-Topics.html)
1. [Understanding ROS2 Services](https://docs.ros.org/en/jazzy/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Services/Understanding-ROS2-Services.html)
1. [About Nodes](https://docs.ros.org/en/jazzy/Concepts/Basic/About-Nodes.html)
1. [About Topics](https://docs.ros.org/en/jazzy/Concepts/Basic/About-Topics.html)
1. [About Services](https://docs.ros.org/en/jazzy/Concepts/Basic/About-Services.html)