# \[ROS\] Cài đặt

> Hướng dẫn cài đặt / hủy cài đặt __ROS Jazzy Jalisco__. Ubuntu-Install-Debs
<br>Nguồn tham khảo: [https://docs.ros.org/en/kilted/Installation/Ubuntu-Install-Debs.html](https://docs.ros.org/en/kilted/Installation/Ubuntu-Install-Debs.html)

## Yêu Cầu

Các hệ điều hành __*Ubuntu Linux 24.04*__, Windows 10, RHEL-9/Fedora, macOS đều có thể hoạt động, nhưng mà để chắc chắn nên sử dụng hệ điều hành __*Ubuntu Linux 24.04*__ là phiên bản có sự hỗ trợ tốt và đầy đủ nhất.

- Nếu muốn nghiên cứu thì nên cài đặt từ gói __deb__ hoặc __RPMS__ _(tùy thuộc vào nền tảng)_
- Nếu muốn thay đổi sâu hơn có thể tải về bản phát triển mới nhất từ nguồn và sửa đổi.

!!! warning "Chọn OS"
    Ở đây vì ROS là một hệ thống chạy không được hoàn chỉnh lắm trên nhiều nền tảng khác nhau thế nên khuyến nghị là nên sử dụng __*Ubuntu*__. Các công nghệ trên ROS khá là cũ và ít được cập nhật cho các hệ điều hành khác nhau thế nên nó hoàn toàn không ổn định khi sử dụng.

## Cài Đặt

### Kiểm Tra Các Yêu Cầu

#### Check OS Req

Phiên bản này yêu cầu hệ điều hành __*Ubuntu Linux 24.04*__ kiểm tra lõi Linux thỏa mãn điều kiện không với lệnh `hostnamectl`. Ở hệ điều hành __Ubuntu 24.04__ có cấu hình như sau:

```text
 Static hostname: dtdat-OptiPlex-7050
       Icon name: computer-desktop
         Chassis: desktop 🖥️
      Machine ID: 4a91574106e24e4bb18349616726377e
         Boot ID: e31648a38281492880aaa98121849eb6
Operating System: Ubuntu 24.04.2 LTS
          Kernel: Linux 6.8.0-88-generic
    Architecture: x86-64
 Hardware Vendor: Dell Inc.
  Hardware Model: OptiPlex 7050
Firmware Version: 1.5.2
   Firmware Date: Mon 2017-06-19
    Firmware Age: 8y 5month 2w 2d
```

Thế nên chỉ cần có cấu hình cao hơn yêu cầu không quá nhiều là được. Với mình hiện tại đang sử dụng hệ điều hành __*Zorin OS*__ _(cũng cùng nhân linux)_.


#### Check System setup

##### Set locale

Đảm bảo bạn có ngôn ngữ hỗ trợ `UTF-8`. Nếu bạn đang ở trong một môi trường tối thiểu (chẳng hạn như vùng chứa docker), ngôn ngữ có thể là `POSIX`. ROS thử nghiệm với các cài đặt sau. Tuy nhiên, sẽ ổn thôi nếu bạn đang sử dụng một ngôn ngữ được hỗ trợ `UTF-8` khác.

```bash title="Kiểm tra cấu hình"
locale  # check for UTF-8
```

Hai thông số khuyên nghị là `LC_ALL=en_US.UTF-8` và `LANG=en_US.UTF-8`. Nếu không có thì có thể cài đặt theo như dòng lệnh dưới đây.

```bash title="Cấu hình khuyến nghị & Cài đặt 🚩"
sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8
```

##### Enable required repositories

> Kích hoạt các kho lưu trữ cần thiết

Bạn sẽ cần thêm kho lưu trữ ROS 2 apt vào hệ thống của mình.

Đầu tiên hãy đảm bảo rằng __Ubuntu Universe repository__ được bật. [_(What is **Ubuntu Universe repository**?)_](https://help.ubuntu.com/community/Repositories/Ubuntu)

```bash
sudo apt install software-properties-common
sudo add-apt-repository universe
```

Việc cài đặt gói `ros2-apt-source` sẽ định cấu hình kho lưu trữ ROS 2 cho hệ thống của bạn. Các bản cập nhật cấu hình kho lưu trữ sẽ tự động diễn ra khi các phiên bản mới của gói này được phát hành vào kho lưu trữ ROS.


```bash title="🚩"
sudo apt update && sudo apt install curl -y
export ROS_APT_SOURCE_VERSION=$(curl -s https://api.github.com/repos/ros-infrastructure/ros-apt-source/releases/latest | grep -F "tag_name" | awk -F\" '{print $4}')
curl -L -o /tmp/ros2-apt-source.deb "https://github.com/ros-infrastructure/ros-apt-source/releases/download/${ROS_APT_SOURCE_VERSION}/ros2-apt-source_${ROS_APT_SOURCE_VERSION}.$(. /etc/os-release && echo ${UBUNTU_CODENAME:-${VERSION_CODENAME}})_all.deb"
sudo dpkg -i /tmp/ros2-apt-source.deb
```

__Phân Tích:__

- `sudo apt update && sudo apt install curl -y` -> Tải và cài đặt `curl`
- `export ROS_APT_SOURCE_VERSION=$(curl -s https://api.github.com/repos/ros-infrastructure/ros-apt-source/releases/latest | grep -F "tag_name" | awk -F\" '{print $4}')` ->
    - Lệnh này truy cập vào đường dẫn [latest](https://api.github.com/repos/ros-infrastructure/ros-apt-source/releases/latest) mô tả phiên bản mới nhất và các thông tin của chúng, dữ liệu được đặt dưới dạng  tệp __*json*__.
- 

##### Install development tools (bắt buộc)

> Cài đặt công cụ phát triển

Nếu bạn định xây dựng bằng các gói ROS hoặc tự phát triển, bạn cũng có thể cài đặt các công cụ phát triển:

```bash
sudo apt update && sudo apt install ros-dev-tools
```

!!! quote "Đôi lời"
    Không hiểu sao cái này bị đặt thành tùy chọn. Nếu không cài đặt bước này thì bước sau không thực hiện được luôn.


## Install ROS 2 (Jazzy Jalisco)

Cập nhật bộ đệm kho lưu trữ apt của bạn sau khi thiết lập kho lưu trữ.

```text
sudo apt update
```

=== "Desktop Install (Recommended)"
    Phiên bản đầy đủ với __*ROS, RViz, demos, tutorials*__

    ```bash
    sudo apt install ros-jazzy-desktop
    ```

=== "ROS-Base Install (Bare Bones)"
    Phiên bản rút gọn chỉ còn các __*Communication libraries*__, _message packages_, _command line tools_. __No GUI tools__.

    ```bash
    sudo apt install ros-jazzy-ros-base
    ```

!!! success "Thành Công"
    - Nếu cài đặt thành công thì sẽ có thư mục `/opt/ros/jazzy`
    - Các phiên bản khác nhau sẽ có phần phiên bản _(jazzy)_ khác nhau. Nhưng mình nhớ ở đâu có đề cập rằng không nên cài đặt nhiều phiên bản __ROS__ trên cùng một thiết bị.

## Xử lý lỗi

!!! bug "Bug"
    ```bash
    $ sudo add-apt-repository universe
    Unable to handle repository shortcut 'universe'
    ```
    Lỗi này xảy ra khi hệ điều hành đang sử dụng không phải __Ubuntu__, cái này chỉ có cách sử dụng cách 2 để cài đặt __Ros__ thôi.

    - Tham Khảo: Ubuntu (source)
