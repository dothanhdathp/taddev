# AOSP Android cho Pi4

> AOSP cho Pi4

## Nguồn

- Bài viết: [https://forums.raspberrypi.com/viewtopic.php?t=376222](https://forums.raspberrypi.com/viewtopic.php?t=376222)
- Konstakang (author): [https://konstakang.com/devices/rpi4/AOSP15/](https://konstakang.com/devices/rpi4/AOSP15/)
    - _Chắc sẽ còn nhiều phiên bản AOSP khác cho Android 13_

Thường thì sẽ sử dụng trực tiếp hướng dẫn trên github repo.

- [Github Android 12.1](https://github.com/raspberry-vanilla/android_local_manifest/tree/android-12.1)
- [Github Android 13](https://github.com/raspberry-vanilla/android_local_manifest/tree/android-13.0)
- [Github Android 14](https://github.com/raspberry-vanilla/android_local_manifest/tree/android-14.0)
- [Github Android 15](https://github.com/raspberry-vanilla/android_local_manifest/tree/android-15.0)
- [Github Android 16](https://github.com/raspberry-vanilla/android_local_manifest/tree/android-16.0)

## Hướng Dẫn Xây Dựng

### 1. Chuẩn Bị Môi Trường Android

Thiết lập [Android build environment](https://source.android.com/docs/setup/start/requirements).


```text
sudo apt-get install git-core gnupg flex bison build-essential zip curl zlib1g-dev libc6-dev-i386 x11proto-core-dev libx11-dev lib32z1-dev libgl1-mesa-dev libxml2-utils xsltproc unzip fontconfig
```

Sau đó thì tải về __repo__ (nếu chưa có)

### 2. Tải thêm một các gói ngoài lề khác

```text
sudo apt-get install dosfstools e2fsprogs fdisk kpartx mtools rsync
```

### 3. Khởi tạo Repo

=== "Đầy đủ"
    ```text title="Init Repo"
    repo init -u https://android.googlesource.com/platform/manifest -b android-15.0.0_r32 --depth=1
    ```
    ```text title="Tải về XML"
    curl -o .repo/local_manifests/manifest_brcm_rpi.xml -L https://raw.githubusercontent.com/raspberry-vanilla/android_local_manifest/android-15.0/manifest_brcm_rpi.xml --create-dirs
    ```
=== "Reduce Size (nên chọn)"
    ```text title="Init Repo"
    repo init -u https://android.googlesource.com/platform/manifest -b android-15.0.0_r32 --depth=1
    ```
    ```text title="Tải về XML"
    curl -o .repo/local_manifests/manifest_brcm_rpi.xml -L https://raw.githubusercontent.com/raspberry-vanilla/android_local_manifest/android-15.0/manifest_brcm_rpi.xml --create-dirs
    curl -o .repo/local_manifests/remove_projects.xml -L https://raw.githubusercontent.com/raspberry-vanilla/android_local_manifest/android-15.0/remove_projects.xml
    ```

### Sync

Đầu tiên cầu sử dụng lệnh này để tải về các bản git

```bash
repo sync --network-only -j 8
```

Và sau đó sử dụng lệnh này để tải về các bản phân phối.

```bash
repo sync --local-only -j 16
```

## Build

### Setup Android Build Environment

```bash title="Cài Đặt Môi Trường"
source build/envsetup.sh
```

### Select The Target Device

=== "Pi4"
    ```bash title="Original"
    lunch aosp_rpi4-bp1a-userdebug
    ```
    ```bash title="TV"
    lunch aosp_rpi4_tv-bp1a-userdebug
    ```
    ```bash title="CAR"
    lunch aosp_rpi4_car-bp1a-userdebug
    ```
=== "Pi5"
    ```bash title="Original"
    lunch aosp_rpi5-bp1a-userdebug
    ```
    ```bash title="TV"
    lunch aosp_rpi5_tv-bp1a-userdebug
    ```
    ```bash title="CAR"
    lunch aosp_rpi5_car-bp1a-userdebug
    ```

### Biên Dịch Mục Tiêu

```bash
make bootimage systemimage vendorimage -j$(nproc)
```

### Tạo image cho thiết bị

=== "Pi4"
    ```bash
    ./rpi4-mkimg.sh
    ```
=== "Pi5"
    ```bash
    ./rpi5-mkimg.sh
    ```