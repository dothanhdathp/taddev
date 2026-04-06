# Android 15 for Pi

> - Nguồn bài viết tại: [raspberrypi forum](https://forums.raspberrypi.com/viewtopic.php?t=376222)
> - [Android 15 (konstakang)](https://konstakang.com/devices/rpi4/AOSP14/)

## About Reversion

| Reversion            | Content        |
| :------------------- | :------------- |
| `android-15.0`       | Maintained     |
| `android-15.0.0_r4`  | Not naintained |
| `android-15.0.0_r14` | Not naintained |

## Rev android-15.0
> - [Github](https://github.com/raspberry-vanilla/android_local_manifest/tree/android-15.0)

### Install Packages

#### Primary Packages

```bash
sudo apt-get install git-core gnupg flex bison build-essential zip curl zlib1g-dev libc6-dev-i386 x11proto-core-dev libx11-dev lib32z1-dev libgl1-mesa-dev libxml2-utils xsltproc unzip fontconfig
```

### Additional Packages

```bash
sudo apt-get install dosfstools e2fsprogs fdisk kpartx mtools rsync
```

### Initialize Repo

#### Full

```bash
repo init -u https://android.googlesource.com/platform/manifest -b android-15.0.0_r32
curl -o .repo/local_manifests/manifest_brcm_rpi.xml -L https://raw.githubusercontent.com/raspberry-vanilla/android_local_manifest/android-15.0/manifest_brcm_rpi.xml --create-dirs
```

#### Reduced

```bash title="Reduced"
repo init -u https://android.googlesource.com/platform/manifest -b android-15.0.0_r32 --depth=1
curl -o .repo/local_manifests/manifest_brcm_rpi.xml -L https://raw.githubusercontent.com/raspberry-vanilla/android_local_manifest/android-15.0/manifest_brcm_rpi.xml --create-dirs
curl -o .repo/local_manifests/remove_projects.xml -L https://raw.githubusercontent.com/raspberry-vanilla/android_local_manifest/android-15.0/remove_projects.xml
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
    lunch aosp_rpi4-bp1a-userdebug
    ```
    ```text title="TV"
    lunch aosp_rpi4_tv-bp1a-userdebug
    ```
    ```text title="Car"
    lunch aosp_rpi4_car-bp1a-userdebug
    ```
=== "rpi5"
    ```text title="Tablet"
    lunch aosp_rpi5-bp1a-userdebug
    ```
    ```text title="TV"
    lunch aosp_rpi5_tv-bp1a-userdebug
    ```
    ```text title="Car"
    lunch aosp_rpi5_car-bp1a-userdebug
    ```

### Compile

```bash
make bootimage systemimage vendorimage -j$(nproc)
```

### Make Image

=== "rpi4"
    ```bash
    ./rpi4-mkimg.sh
    ```
=== "rpi5"
    ```bash
    ./rpi5-mkimg.sh
    ```

Also look into [Linux kernel build instructions](https://github.com/raspberry-vanilla/android_kernel_manifest/tree/android-13.0).

## Rev android-15.0.0_r4
> - [Github](https://github.com/raspberry-vanilla/android_local_manifest/tree/android-14.0.0_r22)

### Android-15.0.0_r4 Addition Package

```bash
sudo apt-get install bc coreutils dosfstools e2fsprogs fdisk kpartx mtools ninja-build pkg-config python3-pip
sudo pip3 install meson mako jinja2 ply pyyaml dataclasses
```

### Android-15.0.0_r4 Initialize Repo

=== "Reduced"
    ```bash
    repo init -u https://android.googlesource.com/platform/manifest -b android-15.0.0_r4 --depth=1
    curl -o .repo/local_manifests/manifest_brcm_rpi.xml -L https://raw.githubusercontent.com/raspberry-vanilla/android_local_manifest/android-15.0.0_r4/manifest_brcm_rpi.xml --create-dirs
    curl -o .repo/local_manifests/remove_projects.xml -L https://raw.githubusercontent.com/raspberry-vanilla/android_local_manifest/android-15.0.0_r4/remove_projects.xml
    ```
=== "Full"
    ```bash
    repo init -u https://android.googlesource.com/platform/manifest -b android-15.0.0_r4
    curl -o .repo/local_manifests/manifest_brcm_rpi.xml -L https://raw.githubusercontent.com/raspberry-vanilla/android_local_manifest/android-15.0.0_r4/manifest_brcm_rpi.xml --create-dirs
    ```

### Android-15.0.0_r4 Build Target

=== "rpi4"
    ```text title="Tablet"
    lunch aosp_rpi4-ap3a-userdebug
    ```
    ```text title="TV"
    lunch aosp_rpi4_tv-ap3a-userdebug
    ```
    ```text title="Car"
    lunch aosp_rpi4_car-ap3a-userdebug
    ```
=== "rpi5"
    ```text title="Tablet"
    lunch aosp_rpi5-ap3a-userdebug
    ```
    ```text title="TV"
    lunch aosp_rpi5_tv-ap3a-userdebug
    ```
    ```text title="Car"
    lunch aosp_rpi5_car-ap3a-userdebug
    ```

## Rev android-15.0.0_r14
> - [Github](https://github.com/raspberry-vanilla/android_local_manifest/tree/android-15.0.0_r14)

### Android-15.0.0_r14 Addition Package

```bash
sudo apt-get install coreutils dosfstools e2fsprogs fdisk kpartx mtools ninja-build pkg-config python3-pip rsync
sudo pip3 install dataclasses jinja2 mako meson ply pyyaml
```

### Android-15.0.0_r14 Initialize Repo

=== "Reduced"
    ```bash
    repo init -u https://android.googlesource.com/platform/manifest -b android-15.0.0_r14 --depth=1
    curl -o .repo/local_manifests/manifest_brcm_rpi.xml -L https://raw.githubusercontent.com/raspberry-vanilla/android_local_manifest/android-15.0.0_r14/manifest_brcm_rpi.xml --create-dirs
    curl -o .repo/local_manifests/remove_projects.xml -L https://raw.githubusercontent.com/raspberry-vanilla/android_local_manifest/android-15.0.0_r14/remove_projects.xml
    ```
=== "Full"
    ```bash
    repo init -u https://android.googlesource.com/platform/manifest -b android-15.0.0_r14
    curl -o .repo/local_manifests/manifest_brcm_rpi.xml -L https://raw.githubusercontent.com/raspberry-vanilla/android_local_manifest/android-15.0.0_r14/manifest_brcm_rpi.xml --create-dirs
    ```

### Android-15.0.0_r14 Build Target

=== "rpi4"
    ```text title="Tablet"
    lunch aosp_rpi4-ap4a-userdebug
    ```
    ```text title="TV"
    lunch aosp_rpi4_tv-ap4a-userdebug
    ```
    ```text title="Car"
    lunch aosp_rpi4_car-ap4a-userdebug
    ```
=== "rpi5"
    ```text title="Tablet"
    lunch aosp_rpi5-ap4a-userdebug
    ```
    ```text title="TV"
    lunch aosp_rpi5_tv-ap4a-userdebug
    ```
    ```text title="Car"
    lunch aosp_rpi5_car-ap4a-userdebug
    ```