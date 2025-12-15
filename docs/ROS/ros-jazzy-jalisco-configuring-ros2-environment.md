# \[ROS\] Cấu Hình Môi Trường
> [https://docs.ros.org/en/jazzy/Tutorials/Beginner-CLI-Tools/Configuring-ROS2-Environment.html](https://docs.ros.org/en/jazzy/Tutorials/Beginner-CLI-Tools/Configuring-ROS2-Environment.html)

## Khởi Động Bằng Script

=== "Linux"
    ```bash
    source /opt/ros/jazzy/setup.bash
    ```
=== "macOS"
    ```bash
    . ~/ros2_install/ros2-osx/setup.bash
    ```
=== "Windows"
    ```cmd
    call C:\dev\ros2\local_setup.bat
    ```

Các lệnh có thể thêm vào các tệp tiền khởi động 0 Ubuntu là tệp `~/.bashrc` hoặc `~/.bash_aliase`...

### Kiểm tra các biến môi trường

=== "Linux"
    ```bash
    printenv | grep -i ROS
    ```
=== "macOS"
    ```bash
    printenv | grep -i ROS
    ```
=== "Windows"
    ```cmd
    set | findstr -i ROS
    ```

### ROS_DOMAIN_ID

- Nếu chưa biết __ROS_DOMAIN_ID__ là gì thì tham khảo đường dẫn sau [ROS_DOMAIN_ID](ros-concepts-ros-domain-id.md)

Sau khi xác định được số nguyên duy nhất cho nhóm nút ROS 2 của mình, bạn có thể đặt biến môi trường bằng lệnh sau:

=== "Linux"
    ```text
    export ROS_DOMAIN_ID=<your_domain_id>
    ```
=== "macOS"
    ```text
    export ROS_DOMAIN_ID=<your_domain_id>
    ```
=== "Windows"
    ```cmd
    set ROS_DOMAIN_ID=<your_domain_id>
    ```

Cái biến này có thể được khai báo trực tiếp với đơ  thay đổi 

### ROS_AUTOMATIC_DISCOVERY_RANGEB