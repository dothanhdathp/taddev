# \[ROS\]<br>Getting Start

!!! danger "Chú Ý"
    <mark class=red>Từ giờ mọi ví dụ sẽ đều dành riêng cho hệ điều hành __Ubuntu__ các hệ điều hành khác vui lòng tự tham khảo trên trang chủ.</mark>

!!! quote "Tóm Tắt"
    - Lệnh sau tạo một __Package__ mới + __Node__ mới.
        ```bash
        ros2 pkg create --build-type ament_cmake --license Apache-2.0 --node-name <node_name> <package_name>
        ```
    - Lệnh sau tạo một __Package__.
        ```bash
        ros2 pkg create --build-type ament_cmake --license Apache-2.0 <package_name>
        ```

## Tạo Môi Trường

### Khởi động môi trường

!!! danger "Luôn phải chạy mỗi khi bắt đầu một phiên làm việc"
    Luôn phải chạy lệnh dưới đây mỗi khi khởi động một __*terminal*__ mới. Bước này tạo lập môi trường hoạt động cho __*Ros*__.

    ```bash
    source /opt/ros/jazzy/setup.bash
    ```

    Để tiện có thể nhúng trực tiếp vào tệp `~/.bash_aliases`, `~/.bashrc`, ... hoặc tạo một command alias đến với nó.

### Tạo Thư Mục Làm Việc

!!! abstract "Tùy Chọn"
    Phần này không bắt buộc. Chỉ là nên đặt và cấu hình như này để thống nhất hoạt động trong các dự án __ROS__ và nó tỏ ra khá hiệu quả.

Tại thư mục gốc tạo một thư mục mới, ví dụ mình đặt là __Ros__ làm nơi gốc chứa mã. Thế nên trong đó không có gì cả. Tạo một thư mục `src` là nơi làm việc (đây là bắt buộc).

### (ROS) Hello World

#### Tạo Package Và Node

Vào trong thư mục `src` vừa tạo ở bước trên và tạo một __*package*__ rỗng với tên:

- __C++__: `c_helloworld_package`, trong package được khởi tạo với một __*node*__ mặc định là `c_helloworld_node` bằng lệnh sau:
- __Python__: `py_helloworld_package`, trong package được khởi tạo với một __*node*__ mặc định là `py_helloworld_node` bằng lệnh sau:

=== "C++"
    ```bash
    ros2 pkg create --build-type ament_cmake --license Apache-2.0 --node-name c_helloworld_node c_helloworld_package
    ```
=== "Python"
    ```bash
    ros2 pkg create --build-type ament_python --license Apache-2.0 --node-name py_helloworld_node py_helloworld_package
    ```

Sau khi hoàn thành trong thư mục `src` sẽ có một thư mục như thế này:

=== "C++"
    ```text
    c_helloworld_package/
    ├── CMakeLists.txt
    ├── include
    │   └── c_helloworld_package
    ├── LICENSE
    ├── package.xml
    └── src
        └── c_helloworld_node.cpp
    ```
=== "Python"
    ```text
    py_helloworld_package/
    ├── LICENSE
    ├── package.xml
    ├── py_helloworld_package
    │   ├── __init__.py
    │   └── py_helloworld_node.py
    ├── resource
    │   └── py_helloworld_package
    ├── setup.cfg
    ├── setup.py
    └── test
        ├── test_copyright.py
        ├── test_flake8.py
        └── test_pep257.py
    ```

Đây là ví dụ nên không cần đi sâu vào chi tiết, chỉ cần biết nội dung của tệp thực thi như sau:

=== "C++"
    ```cpp title="c_helloworld_node.cpp"
    #include <cstdio>

    int main(int argc, char ** argv)
    {
        (void) argc;
        (void) argv;

        printf("hello world c_helloworld_package package\n");
        return 0;
    }
    ```
=== "Python"
    ```python title="py_helloworld_node.py"
    def main():
        print('Hi from py_helloworld_package.')

    if __name__ == '__main__':
        main()
    ```

#### Build Ros Hello World

Trở lại đầu thư mục `cd ~/Ros` và thực hiện lệnh:

```bash
colcon build
```

#### Run Ros Hello World

!!! warning "Warning"
    Sau khi dựng cần chạy tệp này để tải lên hệ thống thông tin về môi trường hoạt động, các node, etc, .. của ROS

```bash
. install/local_setup.sh
```

Sau đó chạy thử Node với công thức:

```text
ros2 run <package_name> <node_name>
```

Ví dụ:

=== "Node C++"
    ```bash
    ros2 run c_helloworld_package c_helloworld_node
    ```
=== "Node Python"
    ```bash
    ros2 run py_helloworld_package py_helloworld_node
    ```

## Ngoài lề

!!! question "Liệu có thể tạo riêng __*package*__ và __*node*__?"
    Có thể tạo riêng gói với lệnh:
    
    ```bash
    ros2 pkg create --build-type <build_type> --license Apache-2.0 <package_name>
    ```

    Nhưng sau đó các node phải khai báo bằng tay, __*không thể tạo node bằng command cho package đã có sẵn với công cụ dòng lệnh.*__

    Điều này bởi vì trong node đã có sẵn yêu cầu riêng về `<build_type>`, việc thêm một node mới sẽ yêu cầu thêm nhiều khai báo lẻ tẻ trong các tệp cấu hình thế nên mới cần khai báo tay. Các cấu hình thêm có đôi chút phức tạp và có thể phá vỡ cấu trúc vốn có của một __*package*__ thế nên nó là dạng __*hành động không an toàn*__. Vì vậy nên các công cụ dòng lệnh không có thêm hỗ trợ đó.

    Về cơ bản việc đó không phải không thể, nhưng nó có phần hơi phức tạp đôi chút nên người sáng tạo cảm thấy không cần thiết phải tạo công cụ sẵn có cho chúng.

!!! question "Liệu __*package*__ có thể có hai `build_type` được không?"
    Không biết nhưng chắc là không.

!!! question "Tạo Node bằng tay thế nào?"
    Xem ở bài sau.