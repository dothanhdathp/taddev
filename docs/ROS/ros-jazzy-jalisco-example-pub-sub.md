# \[ROS\] Ví Dụ Publisher/Subscriber

> Viết một hệ thống __Publisher__ và __Subscriber__ đơn giản.

Mục đích của bài này là bắt đầu viết một bộ gồm hai node thực hiện chức năng __Publisher__ và __Subscriber__ đơn giản dựa trên lý thuyết về __Nodes__ và __Topic__ trong phần [Basic Concept](ros-basic-concepts.md).

## I. Create Package

Đầu tiên cần tạo một gói thực thi

=== "C++"
    ```bash
    ros2 pkg create --build-type ament_cmake --license Apache-2.0 cpp_pubsub
    ```
=== "Python"
    ```bash
    ros2 pkg create --build-type ament_python --license Apache-2.0 py_pubsub
    ```

## II. Write The Publisher Node

### 2.2 Tạo Publisher

Sau khi khởi tạo thì có sẵn các tệp cần thiết trong các gói `cpp_pubsub`/`py_pubsub` rồi. Tiếp theo vào trong thư mục `cpp_pubsub/src`/`py_pubsub/py_pubsub` của gói và bắt đầu tạo nội dung của __Node__.

Code mẫu có sẵn trên server rồi, có thể tải về qua lệnh:

=== "C++"
    ```bash
    wget -O publisher_lambda_function.cpp https://raw.githubusercontent.com/ros2/examples/jazzy/rclcpp/topics/minimal_publisher/lambda.cpp
    ```
=== "Python"
    ```bash
    wget https://raw.githubusercontent.com/ros2/examples/jazzy/rclpy/topics/minimal_publisher/examples_rclpy_minimal_publisher/publisher_member_function.py
    ```

Nội dung của tệp mẫu như sau:

=== "C++"
    ```cpp title="publisher_lambda_function.cpp"
    #include <chrono>
    #include <memory>
    #include <string>

    #include "rclcpp/rclcpp.hpp"
    #include "std_msgs/msg/string.hpp"

    using namespace std::chrono_literals;

    /* This example creates a subclass of Node and uses a fancy C++11 lambda
    * function to shorten the callback syntax, at the expense of making the
    * code somewhat more difficult to understand at first glance. */

    class MinimalPublisher : public rclcpp::Node
    {
    public:
        MinimalPublisher()
        : Node("minimal_publisher"), count_(0)
        {
            publisher_ = this->create_publisher<std_msgs::msg::String>("topic", 10);
            auto timer_callback =
            [this]() -> void {
                auto message = std_msgs::msg::String();
                message.data = "Hello, world! " + std::to_string(this->count_++);
                RCLCPP_INFO(this->get_logger(), "Publishing: '%s'", message.data.c_str());
                this->publisher_->publish(message);
            };
            timer_ = this->create_wall_timer(500ms, timer_callback);
        }

    private:
        rclcpp::TimerBase::SharedPtr timer_;
        rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
        size_t count_;
    };

    int main(int argc, char * argv[])
    {
        rclcpp::init(argc, argv);
        rclcpp::spin(std::make_shared<MinimalPublisher>());
        rclcpp::shutdown();
        return 0;
    }
    ```
=== "Python"
    ```python title="publisher_member_function.py"
    import rclpy
    from rclpy.node import Node

    from std_msgs.msg import String

    class MinimalPublisher(Node):

        def __init__(self):
            super().__init__('minimal_publisher')
            self.publisher_ = self.create_publisher(String, 'topic', 10)
            timer_period = 0.5  # seconds
            self.timer = self.create_timer(timer_period, self.timer_callback)
            self.i = 0

        def timer_callback(self):
            msg = String()
            msg.data = 'Hello World: %d' % self.i
            self.publisher_.publish(msg)
            self.get_logger().info('Publishing: "%s"' % msg.data)
            self.i += 1


    def main(args=None):
        rclpy.init(args=args)

        minimal_publisher = MinimalPublisher()

        rclpy.spin(minimal_publisher)

        # Destroy the node explicitly
        # (optional - otherwise it will be done automatically
        # when the garbage collector destroys the node object)
        minimal_publisher.destroy_node()
        rclpy.shutdown()


    if __name__ == '__main__':
        main()
    ```

### 2.3 Cấu Hình Phụ Thuộc

#### 2.3.1 package.xml

Trong tệp __package.xml__ cần đảm bảo có ba cấu hình sau `<description>`, `<maintainer>` và thẻ `<license>`:

- `<description>`: Mô tả về chức năng, mục đích của __nodes__
- `<maintainer `: điền email và tên của người chịu trách nhiệm trong module này.
- `<license>`: các bản quyền cần có. Mặc định sẽ luôn có __Apache-2.0__

```xml
<description>Examples of minimal publisher/subscriber using rclcpp</description>
<maintainer email="you@email.com">Your Name</maintainer>
<license>Apache-2.0</license>
```

Sau đó thêm vào cấu hình cho các gói phục thuộc trong thẻ `<depend>`:

```xml
<depend>rclcpp</depend>
<depend>std_msgs</depend>
```

Điều này tuyên bố gói cần `rclpy` và `std_msgs` khi mã của nó được thực thi.


=== "C++"
    #### 2.3.2c CMakeLists.txt

    Trong tệp __*CMakeLists.txt*__ bên dưới `find_package(ament_cmake REQUIRED)`, thêm vào hai dòng sau:

    ```cmake
    find_package(rclcpp REQUIRED)
    find_package(std_msgs REQUIRED)
    ```

    Sau đó, thêm tệp thực thi và đặt tên cho nó là `talker` để chạy với `ros2`:

    ```cmake
    add_executable(talker src/publisher_lambda_function.cpp)
    ament_target_dependencies(talker rclcpp std_msgs)
    ```

    Cuối cùng, thêm `install(TARGETS...)`, như vậy thì `ros2` mới có thể tìm thấy tệp thực thi:

    ```cmake
    install(TARGETS
      talker
      DESTINATION lib/${PROJECT_NAME})
    ```

    Sau tất cả thì tệp mẫu sẽ có dạng như này:

    ```cmake title="CMakelist.txt"
    cmake_minimum_required(VERSION 3.5)
    project(cpp_pubsub)

    # Default to C++14
    if(NOT CMAKE_CXX_STANDARD)
    set(CMAKE_CXX_STANDARD 14)
    endif()

    if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
    add_compile_options(-Wall -Wextra -Wpedantic)
    endif()

    find_package(ament_cmake REQUIRED)
    find_package(rclcpp REQUIRED)
    find_package(std_msgs REQUIRED)

    add_executable(talker src/publisher_lambda_function.cpp)
    ament_target_dependencies(talker rclcpp std_msgs)

    install(TARGETS
      talker
      DESTINATION lib/${PROJECT_NAME})

    ament_package()
    ```
=== "Python"
    #### 2.3.2p setup.py

    ##### 2.3.2.1p Add an entry point

    Tương ứng với các trường __*maintainer*__, __*maintainer_email*__, __*description*__ và __*license*__ trong tệp __*package.xml*__, khai báo lần lượt chúng vào gói __*setup.py*__ như sau:

    ```py
    maintainer='YourName',
    maintainer_email='you@email.com',
    description='Examples of minimal publisher/subscriber using rclpy',
    license='Apache-2.0',
    ```

    Thêm dòng sau vào trong ngoặc `console_scripts` của trường `entry_points`:

    ```py
    entry_points={
        'console_scripts': [
            'talker = py_pubsub.publisher_member_function:main',
        ],
    },
    ```

    ##### 2.3.2.2p Check setup.cfg

    Nội dung của `setup.cfg` tệp sẽ được điền tự động chính xác, như vậy:

    ```text
    [develop]
    script_dir=$base/lib/py_pubsub
    [install]
    install_scripts=$base/lib/py_pubsub
    ```

    Điều này chỉ đơn giản là yêu cầu setuptools đặt các tệp thực thi của bạn vào __*lib*__, bởi vì `ros2` chạy sẽ tìm họ ở đó.

    Bạn có thể xây dựng gói của mình ngay bây giờ, lấy nguồn tệp thiết lập cục bộ và chạy gói đó, nhưng trước tiên hãy tạo nút đăng ký để bạn có thể xem toàn bộ hệ thống đang hoạt động.

## III. Write The Subscriber Node

Ở phía __*Subscriber*__ cũng không có quá nhiều khác biệt. Vẫn trong cùng một __*package*__ sẽ tạo thêm một node để thực hiện chức năng nhận

### 3.1 Tạo Subscriber

Cũng tương tự như __Publisher__, có thể tải code mẫu về qua lệnh sau _(cách này nhanh hơn viết tay và xem xét được cấu trúc code)_:

=== "C++"
    ```bash
    wget -O subscriber_lambda_function.cpp https://raw.githubusercontent.com/ros2/examples/jazzy/rclcpp/topics/minimal_subscriber/lambda.cpp
    ```
=== "Python"
    ```bash
    wget https://raw.githubusercontent.com/ros2/examples/jazzy/rclpy/topics/minimal_subscriber/examples_rclpy_minimal_subscriber/subscriber_member_function.py
    ```

Để chúng trong thư mục của _`cpp_pubsub/src` (hoặc `py_pubsub/py_pubsub` của python)_

Nội dung của tệp đó như này:

=== "C++"
    ```cpp title="subscriber_lambda_function.cpp"
    #include <memory>

    #include "rclcpp/rclcpp.hpp"
    #include "std_msgs/msg/string.hpp"

    class MinimalSubscriber : public rclcpp::Node
    {
    public:
        MinimalSubscriber()
        : Node("minimal_subscriber")
        {
            auto topic_callback =
            [this](std_msgs::msg::String::UniquePtr msg) -> void {
                RCLCPP_INFO(this->get_logger(), "I heard: '%s'", msg->data.c_str());
            };
            subscription_ =
            this->create_subscription<std_msgs::msg::String>("topic", 10, topic_callback);
        }

    private:
        rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscription_;
    };

    int main(int argc, char * argv[])
    {
        rclcpp::init(argc, argv);
        rclcpp::spin(std::make_shared<MinimalSubscriber>());
        rclcpp::shutdown();
        return 0;
    }
    ```
=== "Python"
    ```py title="subscriber_member_function.py"
    import rclpy
    from rclpy.node import Node

    from std_msgs.msg import String


    class MinimalSubscriber(Node):

        def __init__(self):
            super().__init__('minimal_subscriber')
            self.subscription = self.create_subscription(
                String,
                'topic',
                self.listener_callback,
                10)
            self.subscription  # prevent unused variable warning

        def listener_callback(self, msg):
            self.get_logger().info('I heard: "%s"' % msg.data)


    def main(args=None):
        rclpy.init(args=args)

        minimal_subscriber = MinimalSubscriber()

        rclpy.spin(minimal_subscriber)

        # Destroy the node explicitly
        # (optional - otherwise it will be done automatically
        # when the garbage collector destroys the node object)
        minimal_subscriber.destroy_node()
        rclpy.shutdown()


    if __name__ == '__main__':
        main()
    ```

### 3.2 Cấu Hình Phụ Thuộc

Node __Subscriber__ sẽ dùng chung các khai báo với __Publisher__ nên sẽ không cần khai báo gì thêm trong __*package.xml*__.

=== "C++"
    #### 3.2.1c CMakeLists.txt

    Mở lại tệp __*CMakeLists.txt*__ và thêm khai báo này vào:

    ```cmake
    add_executable(listener src/subscriber_lambda_function.cpp)
    ament_target_dependencies(listener rclcpp std_msgs)

    install(TARGETS
    talker
    listener
    DESTINATION lib/${PROJECT_NAME})
    ```

=== "Python"
    #### 3.2.1p setup.py

    Mở lại tệp `setup.py` và khai báo _entry_point_ cho __*listener*__

    ```py
    entry_points={
        'console_scripts': [
            'talker = py_pubsub.publisher_member_function:main',
            'listener = py_pubsub.subscriber_member_function:main',
        ],
    },
    ```

## IV. Build and run

Sau khi đã hoàn thành các bước ở trên, kiểm tra lại một chút cấu trúc thư mục cuối cùng sẽ như sau:

=== "C++"
    ```text
    cpp_pubsub/
    ├── CMakeLists.txt
    ├── include
    │   └── cpp_pubsub
    ├── LICENSE
    ├── package.xml
    └── src
        ├── publisher_lambda_function.cpp
        └── subscriber_lambda_function.cpp
    ```
=== "Python"
    ```py
    py_pubsub/
    ├── LICENSE
    ├── package.xml
    ├── py_pubsub
    │   ├── __init__.py
    │   └── publisher_member_function.py
    ├── resource
    │   └── py_pubsub
    ├── setup.cfg
    ├── setup.py
    └── test
        ├── test_copyright.py
        ├── test_flake8.py
        └── test_pep257.py
    ```

### 4.1 Build

_Chạy lại lệnh môi trường (nếu quên)_

```text
source /opt/ros/jazzy/setup.bash
```

#### Build All

```text
colcon build
```

#### Build Package

=== "C++"
    ```bash
    colcon build --packages-select cpp_pubsub
    ```
=== "Python"
    ```bash
    colcon build --packages-select py_pubsub
    ```

### 4.2 Run

Nếu dựng thành công thì sẽ có các tệp ở ngoài, nhớ chạy lệnh sau để tải vào các tham số:

```bash
source install/local_setup.sh
```

#### Chạy Talker

=== "C++"
    ```bash
    ros2 run cpp_pubsub talker
    ```
=== "Python"
    ```bash
    ros2 run py_pubsub talker
    ```

Nếu hoạt động thành công, nó sẽ khởi động một tiến trình liên tục đếm:

```text
[INFO] [1765794827.703273863] [minimal_publisher]: Publishing: "Hello World: 0"
[INFO] [1765794828.106089499] [minimal_publisher]: Publishing: "Hello World: 1"
[INFO] [1765794828.605986917] [minimal_publisher]: Publishing: "Hello World: 2"
[INFO] [1765794829.106189608] [minimal_publisher]: Publishing: "Hello World: 3"
[INFO] [1765794829.606064508] [minimal_publisher]: Publishing: "Hello World: 4"
...
```

#### Chạy Listener

Mở một terminal khác và chạy __*Listener*__.

_Trong một session khác phải chạy lại các lệnh cấu hình môi trường:_

```text
source /opt/ros/jazzy/setup.bash
source install/local_setup.sh
```

=== "C++"
    ```bash
    ros2 run cpp_pubsub listener
    ```
=== "Python"
    ```bash
    ros2 run py_pubsub listener
    ```

- Sau khi được khởi động, bên này sẽ liên tục nhận được bản tin từ bên `talker` gửi đến.

```text
[INFO] [1765794854.699498615] [minimal_subscriber]: I heard: "Hello World: 54"
[INFO] [1765794855.107735598] [minimal_subscriber]: I heard: "Hello World: 55"
[INFO] [1765794855.607276252] [minimal_subscriber]: I heard: "Hello World: 56"
[INFO] [1765794856.107218753] [minimal_subscriber]: I heard: "Hello World: 57"
[INFO] [1765794856.607221215] [minimal_subscriber]: I heard: "Hello World: 58"
[INFO] [1765794857.107434008] [minimal_subscriber]: I heard: "Hello World: 59"
...
```

## Tổng Kết

1. Tạo __Package__
1. Tạo __Node__ cho _talker_ + _listener_
1. Khai báo cấu hình phụ thuộc trong `package.xml`
    1. Tiện thể khai báo thêm thông tin người phát triển.
1. Cấu hình dựng trong:
    1. __C++__: _CMakelist.txt_
    1. __Python__: _setup.py_
1. Build + Run
    1. _Nhớ phải chạy môi trường ROS trước khi build_
    1. Sau đó nhớ phải chạy tệp `install/local_setup.sh`

## Tham Khảo

- [[C++] Ví dụ mẫu cho publisher](https://github.com/ros2/examples/tree/jazzy/rclcpp/topics/minimal_publisher)
- [[C++] Ví dụ mẫu cho subscriber](https://github.com/ros2/examples/tree/jazzy/rclcpp/topics/minimal_subscriber)
- [[Python] Ví dụ mẫu cho publisher](https://github.com/ros2/examples/tree/jazzy/rclpy/topics/minimal_publisher)
- [[Python] Ví dụ mẫu cho subscriber](https://github.com/ros2/examples/tree/jazzy/rclpy/topics/minimal_subscriber)
