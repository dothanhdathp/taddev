# \[Pi\] AOSP 15 for Pi4

> AOSP 15 for Pi4

## Nguồn

- Bài viết: [https://forums.raspberrypi.com/viewtopic.php?t=376222](https://forums.raspberrypi.com/viewtopic.php?t=376222)
- Konstakang (author): [https://konstakang.com/devices/rpi4/AOSP15/](https://konstakang.com/devices/rpi4/AOSP15/)
    - _Chắc sẽ còn nhiều phiên bản AOSP khác cho Android 13_
- [Github android-15](https://github.com/raspberry-vanilla/android_local_manifest/tree/android-15.0)

## Hướng dẫn

### Establish Android Build Environment

Tham khảo hướng dẫn ở [Thiết lập để phát triển AOSP (9.0 trở lên)](https://source.android.com/docs/setup/start/requirements)

Tải về các gói cài đặt cần thiết:

```text
sudo apt-get install git-core gnupg flex bison build-essential zip curl zlib1g-dev libc6-dev-i386 x11proto-core-dev libx11-dev lib32z1-dev libgl1-mesa-dev libxml2-utils xsltproc unzip fontconfig
```

Sau đó thì tải về __repo__ (nếu chưa có)

### Tải thêm một số gói ngoài lề

```text
sudo apt-get install dosfstools e2fsprogs fdisk kpartx mtools rsync
```

### Init Repo

=== "Cách 1 : Đầy đủ"
    ```text title="Init Repo"
    repo init -u https://android.googlesource.com/platform/manifest -b android-15.0.0_r32 --depth=1
    ```
    ```text title="Tải về XML"
    curl -o .repo/local_manifests/manifest_brcm_rpi.xml -L https://raw.githubusercontent.com/raspberry-vanilla/android_local_manifest/android-15.0/manifest_brcm_rpi.xml --create-dirs
    ```
=== "Cách 2 : Reduce Size Clone"
    ```text title="Init Repo"
    repo init -u https://android.googlesource.com/platform/manifest -b android-15.0.0_r32 --depth=1
    ```
    ```text title="Tải về XML"
    curl -o .repo/local_manifests/manifest_brcm_rpi.xml -L https://raw.githubusercontent.com/raspberry-vanilla/android_local_manifest/android-15.0/manifest_brcm_rpi.xml --create-dirs
    curl -o .repo/local_manifests/remove_projects.xml -L https://raw.githubusercontent.com/raspberry-vanilla/android_local_manifest/android-15.0/remove_projects.xml
    ```

### Sync

=== "Sync"
    Cách này đơn giản nhưng tiện.

    ```text title="Sync Full"
    repo sync
    ```
=== "Sync Optimize"
    Cách này có thể nhanh hơn nếu thiết bị không chịu nổi.

    ```text title="Init Git Repo"
    repo sync --force-checkout --force-sync --fail-fast --jobs-checkout=8 --jobs-network=8 --network-only
    ```
    ```text title="Pull Source Code"
    repo sync --force-checkout --force-sync --fail-fast --jobs-checkout=64 --local-only
    ```

## Build

### Setup Android Build Environment

```text title=""
. build/envsetup.sh
```

### Select The Target Device

=== "Pi4"
    ```text title="Original"
    lunch aosp_rpi4-bp1a-userdebug
    ```
    ```text title="TV"
    lunch aosp_rpi4_tv-bp1a-userdebug
    ```
    ```text title="CAR"
    lunch aosp_rpi4_car-bp1a-userdebug
    ```
=== "Pi5"
    ```text title="Original"
    lunch aosp_rpi5-bp1a-userdebug
    ```
    ```text title="TV"
    lunch aosp_rpi5_tv-bp1a-userdebug
    ```
    ```text title="CAR"
    lunch aosp_rpi5_car-bp1a-userdebug
    ```