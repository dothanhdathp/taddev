# ROS Phân Tích Publisher/Subscriber


- Thư viện thường sẽ cài đặt tại: `/opt/ros/jazzy`
- Tham khảo API C++ tại: [https://docs.ros.org/en/jazzy/p/rclcpp/generated/index.html](https://docs.ros.org/en/jazzy/p/rclcpp/generated/index.html)

## Chung

- ???

## C++

### C++ Publisher

```cpp
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
    MinimalPublisher() : Node("minimal_publisher"), count_(0)
    {
        publisher_ = this->create_publisher<std_msgs::msg::String>("topic", 10);
        auto timer_callback = [this]() -> void {
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
e
int main(int argc, char * argv[])
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<MinimalPublisher>());
    rclcpp::shutdown();
    return 0;e
}
```

- `rclcpp::Node` đại diện cho một Node trong ROS.
- `Node("minimal_publisher")` chỉ đơn giản là đặt tên node là __*minimal_publisher*__
- Trong lớp này tiếp theo cần tạo class `rclcpp::Publisher`, lấy __SharedPtr__

### rclcpp::Node

```cpp
explicit Node(const std::string & node_name, const NodeOptions & options = NodeOptions());
```
- [rclcpp::Node]()

```cpp
template<
    typename MessageT,
    typename AllocatorT = std::allocator<void>,
    typename PublisherT = rclcpp::Publisher<MessageT, AllocatorT>>
std::shared_ptr<PublisherT> create_publisher(
    const std::string &topic_name,
    const rclcpp::QoS &qos,
    const PublisherOptionsWithAllocator<AllocatorT> &options = PublisherOptionsWithAllocator<AllocatorT>()
)
```

## Subscriber


```cpp
#include <memory>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

class MinimalSubscriber : public rclcpp::Node
{
private:
    rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscription_;

public:
    MinimalSubscriber()
    : Node("minimal_subscriber")
    {
        auto topic_callback = [this](std_msgs::msg::String::UniquePtr msg) -> void {
            RCLCPP_INFO(this->get_logger(), "I heard: '%s'", msg->data.c_str());
        };
        subscription_ = this->create_subscription<std_msgs::msg::String>("topic", 10, topic_callback);
    }

};

int main(int argc, char * argv[])
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<MinimalSubscriber>());
    rclcpp::shutdown();
    return 0;
}
```

