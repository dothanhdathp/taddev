# Android 14 for Pi

> - Nguồn bài viết tại: [raspberrypi forum](https://forums.raspberrypi.com/viewtopic.php?t=376222)
> - [Android 14 (konstakang)](https://konstakang.com/devices/rpi4/AOSP14/)

## About Reversion

| Reversion            | Content        |
| :------------------- | :------------- |
| `android-14.0`       | Maintained     |
| `android-14.0.0_r22` | Not naintained |
| `android-14.0.0_r34` | Not naintained |

## Rev android-14.0
> - [Github](https://github.com/raspberry-vanilla/android_local_manifest/tree/android-14.0)

### Install Packages

#### Primary Packages

```bash
sudo apt-get install git-core gnupg flex bison build-essential zip curl zlib1g-dev libc6-dev-i386 x11proto-core-dev libx11-dev lib32z1-dev libgl1-mesa-dev libxml2-utils xsltproc unzip fontconfig
```

### Additional Packages

```bash
sudo apt-get install bc coreutils dosfstools e2fsprogs fdisk kpartx mtools ninja-build pkg-config python3-pip rsync
sudo pip3 install meson mako jinja2 ply pyyaml dataclasses
```

### Initialize Repo

#### Full

```bash
repo init -u https://android.googlesource.com/platform/manifest -b android-14.0.0_r67
curl -o .repo/local_manifests/manifest_brcm_rpi.xml -L https://raw.githubusercontent.com/raspberry-vanilla/android_local_manifest/android-14.0/manifest_brcm_rpi.xml --create-dirs
```

#### Reduced

```bash title="Reduced"
repo init -u https://android.googlesource.com/platform/manifest -b android-14.0.0_r67 --depth=1
curl -o .repo/local_manifests/manifest_brcm_rpi.xml -L https://raw.githubusercontent.com/raspberry-vanilla/android_local_manifest/android-14.0/manifest_brcm_rpi.xml --create-dirs
curl -o .repo/local_manifests/remove_projects.xml -L https://raw.githubusercontent.com/raspberry-vanilla/android_local_manifest/android-14.0/remove_projects.xml
```

### Sync Source Code

#### One Steps

This way short but slow

```bash
repo sync 
```

#### Two Steps

This way faster

```bash
repo sync -j 16 --network-only 
repo sync -j 64 --local-only
```

### Setup Android build environment

#### Set Environment

```bash
. build/envsetup.sh
```

#### Select build target

=== "rpi4"
    ```text title="Tablet"
    lunch aosp_rpi4-ap2a-userdebug
    ```
    ```text title="TV"
    lunch aosp_rpi4_tv-ap2a-userdebug
    ```
    ```text title="Car"
    lunch aosp_rpi4_car-ap2a-userdebug
    ```
=== "rpi5"
    ```text title="Tablet"
    lunch aosp_rpi5-ap2a-userdebug
    ```
    ```text title="TV"
    lunch aosp_rpi5_tv-ap2a-userdebug
    ```
    ```text title="Car"
    lunch aosp_rpi5_car-ap2a-userdebug
    ```

## Compile

```bash
make bootimage systemimage vendorimage -j$(nproc)
```

## Make Image

=== "rpi4"
    ```bash
    ./rpi4-mkimg.sh
    ```
=== "rpi5"
    ```bash
    ./rpi5-mkimg.sh
    ```

Also look into [Linux kernel build instructions](https://github.com/raspberry-vanilla/android_kernel_manifest/tree/android-13.0).

## Rev android-14.0.0_r22
> - [Github](https://github.com/raspberry-vanilla/android_local_manifest/tree/android-14.0.0_r22)

### Android-14.0.0_r22 Initialize Repo

=== "Reduced"
    ```bash title="Reduced"
    repo init -u https://android.googlesource.com/platform/manifest -b android-14.0.0_r22 --depth=1
    curl -o .repo/local_manifests/manifest_brcm_rpi.xml -L https://raw.githubusercontent.com/raspberry-vanilla/android_local_manifest/android-14.0.0_r22/manifest_brcm_rpi.xml --create-dirs
    curl -o .repo/local_manifests/remove_projects.xml -L https://raw.githubusercontent.com/raspberry-vanilla/android_local_manifest/android-14.0.0_r22/remove_projects.xml
    ```
=== "Full"
    ```bash
    repo init -u https://android.googlesource.com/platform/manifest -b android-14.0.0_r22
    curl -o .repo/local_manifests/manifest_brcm_rpi.xml -L https://raw.githubusercontent.com/raspberry-vanilla/android_local_manifest/android-14.0.0_r22/manifest_brcm_rpi.xml --create-dirs
    ```

### Android-14.0.0_r22 Build Target

=== "rpi4"
    ```text title="Tablet"
    lunch aosp_rpi4-userdebug
    ```
    ```text title="TV"
    lunch aosp_rpi4_tv-userdebug
    ```
    ```text title="Car"
    lunch aosp_rpi4_car-userdebug
    ```
=== "rpi5"
    ```text title="Tablet"
    lunch aosp_rpi5-userdebug
    ```
    ```text title="TV"
    lunch aosp_rpi5_tv-userdebug
    ```
    ```text title="Car"
    lunch aosp_rpi5_car-userdebug
    ```

## Rev android-14.0.0_r34
> - [Github](https://github.com/raspberry-vanilla/android_local_manifest/tree/android-14.0.0_r34)

### Android-14.0.0_r34 Initialize Repo

Tất cả các phần khác giống hệt chỉ khác ở bước **Initialize Repo** thay bằng các câu lệnh sau

=== "Reduced"
    ```bash title="Reduced"
    repo init -u https://android.googlesource.com/platform/manifest -b android-14.0.0_r34 --depth=1
    curl -o .repo/local_manifests/manifest_brcm_rpi.xml -L https://raw.githubusercontent.com/raspberry-vanilla/android_local_manifest/android-14.0.0_r34/manifest_brcm_rpi.xml --create-dirs
    curl -o .repo/local_manifests/remove_projects.xml -L https://raw.githubusercontent.com/raspberry-vanilla/android_local_manifest/android-14.0.0_r34/remove_projects.xml
    ```
=== "Full"
    ```bash
    repo init -u https://android.googlesource.com/platform/manifest -b android-14.0.0_r34
    curl -o .repo/local_manifests/manifest_brcm_rpi.xml -L https://raw.githubusercontent.com/raspberry-vanilla/android_local_manifest/android-14.0.0_r34/manifest_brcm_rpi.xml --create-dirs
    ```

### Android-14.0.0_r34 Build Target

=== "rpi4"
    ```text title="Tablet"
    lunch aosp_rpi4-ap1a-userdebug
    ```
    ```text title="TV"
    lunch aosp_rpi4_tv-ap1a-userdebug
    ```
    ```text title="Car"
    lunch aosp_rpi4_car-ap1a-userdebug
    ```
=== "rpi5"
    ```text title="Tablet"
    lunch aosp_rpi5-ap1a-userdebug
    ```
    ```text title="TV"
    lunch aosp_rpi5_tv-ap1a-userdebug
    ```
    ```text title="Car"
    lunch aosp_rpi5_car-ap1a-userdebug
    ```