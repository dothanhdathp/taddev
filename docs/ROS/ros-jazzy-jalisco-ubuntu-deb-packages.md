# \[ROS\] Ubuntu (deb packages)

> Nguồn: [https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debs.html#ubuntu-deb-packages](https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debs.html)

## 

Lặp lại các bước của 

```bash title="Tải Về"
sudo apt update && sudo apt install curl -y
export ROS_APT_SOURCE_VERSION=$(curl -s https://api.github.com/repos/ros-infrastructure/ros-apt-source/releases/latest | grep -F "tag_name" | awk -F\" '{print $4}')
curl -L -o /tmp/ros2-apt-source.deb "https://github.com/ros-infrastructure/ros-apt-source/releases/download/${ROS_APT_SOURCE_VERSION}/ros2-apt-source_${ROS_APT_SOURCE_VERSION}.$(. /etc/os-release && echo ${UBUNTU_CODENAME:-${VERSION_CODENAME}})_all.deb"
```

- Sau đó có thể dùng lệnh `echo $ROS_APT_SOURCE_VERSION` để đọc ra giá trị của __ROS_APT_SOURCE_VERSION__ được cài đặt.

```bash title="Cài Đặt"
sudo dpkg -i /tmp/ros2-apt-source.deb
```