# Android 16 for Pi

> - Nguồn bài viết tại: [raspberrypi forum](https://forums.raspberrypi.com/viewtopic.php?t=376222)
> - [Android 16 (konstakang)](https://konstakang.com/devices/rpi4/AOSP16/)

## About Reversion

| Reversion            | Content        |
| :------------------- | :------------- |
| `android-16.0`       | Maintained     |
| `android-16.0.0_r1`  | Not naintained |
| `android-16.0.0_r3` | Not naintained |

## Rev android-16.0
> - [Github](https://github.com/raspberry-vanilla/android_local_manifest/tree/android-16.0)

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
repo init -u https://android.googlesource.com/platform/manifest -b android-16.0.0_r4
curl -o .repo/local_manifests/manifest_brcm_rpi.xml -L https://raw.githubusercontent.com/raspberry-vanilla/android_local_manifest/android-16.0/manifest_brcm_rpi.xml --create-dirs
```

#### Reduced

```bash title="Reduced"
repo init -u https://android.googlesource.com/platform/manifest -b android-16.0.0_r4 --depth=1
curl -o .repo/local_manifests/manifest_brcm_rpi.xml -L https://raw.githubusercontent.com/raspberry-vanilla/android_local_manifest/android-16.0/manifest_brcm_rpi.xml --create-dirs
curl -o .repo/local_manifests/remove_projects.xml -L https://raw.githubusercontent.com/raspberry-vanilla/android_local_manifest/android-16.0/remove_projects.xml
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
    lunch aosp_rpi4-bp4a-userdebug
    ```
    ```text title="TV"
    lunch aosp_rpi4_tv-bp4a-userdebug
    ```
    ```text title="Car"
    lunch aosp_rpi4_car-bp4a-userdebug
    ```
=== "rpi5"
    ```text title="Tablet"
    lunch aosp_rpi5-bp4a-userdebug
    ```
    ```text title="TV"
    lunch aosp_rpi5_tv-bp4a-userdebug
    ```
    ```text title="Car"
    lunch aosp_rpi5_car-bp4a-userdebug
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

Also look into [Linux kernel build instructions](https://github.com/raspberry-vanilla/android_kernel_manifest/tree/android-16.0).

## Rev android-16.0.0_r1
> - [Github](https://github.com/raspberry-vanilla/android_local_manifest/tree/android-16.0.0_r1)

### Android-16.0.0_r1 Initialize Repo

=== "Reduced"
    ```bash
    repo init -u https://android.googlesource.com/platform/manifest -b android-16.0.0_r1 --depth=1
    curl -o .repo/local_manifests/manifest_brcm_rpi.xml -L https://raw.githubusercontent.com/raspberry-vanilla/android_local_manifest/android-16.0.0_r1/manifest_brcm_rpi.xml --create-dirs
    curl -o .repo/local_manifests/remove_projects.xml -L https://raw.githubusercontent.com/raspberry-vanilla/android_local_manifest/android-16.0.0_r1/remove_projects.xml
    ```
=== "Full"
    ```bash
    repo init -u https://android.googlesource.com/platform/manifest -b android-16.0.0_r1
    curl -o .repo/local_manifests/manifest_brcm_rpi.xml -L https://raw.githubusercontent.com/raspberry-vanilla/android_local_manifest/android-16.0.0_r1/manifest_brcm_rpi.xml --create-dirs
    ```

### Android-16.0.0_r1 Build Target

=== "rpi4"
    ```text title="Tablet"
    lunch aosp_rpi4-bp2a-userdebug
    ```
    ```text title="TV"
    lunch aosp_rpi4_tv-bp2a-userdebug
    ```
    ```text title="Car"
    lunch aosp_rpi4_car-bp2a-userdebug
    ```
=== "rpi5"
    ```text title="Tablet"
    lunch aosp_rpi5-bp2a-userdebug
    ```
    ```text title="TV"
    lunch aosp_rpi5_tv-bp2a-userdebug
    ```
    ```text title="Car"
    lunch aosp_rpi5_car-bp2a-userdebug
    ```

## Rev android-16.0.0_r3
> - [Github](https://github.com/raspberry-vanilla/android_local_manifest/tree/android-16.0.0_r14)

### Android-16.0.0_r3 Initialize Repo

=== "Reduced"
    ```bash
    repo init -u https://android.googlesource.com/platform/manifest -b android-16.0.0_r3 --depth=1
    curl -o .repo/local_manifests/manifest_brcm_rpi.xml -L https://raw.githubusercontent.com/raspberry-vanilla/android_local_manifest/android-16.0.0_r3/manifest_brcm_rpi.xml --create-dirs
    curl -o .repo/local_manifests/remove_projects.xml -L https://raw.githubusercontent.com/raspberry-vanilla/android_local_manifest/android-16.0.0_r3/remove_projects.xml
    ```
=== "Full"
    ```bash
    repo init -u https://android.googlesource.com/platform/manifest -b android-16.0.0_r3
    curl -o .repo/local_manifests/manifest_brcm_rpi.xml -L https://raw.githubusercontent.com/raspberry-vanilla/android_local_manifest/android-16.0.0_r3/manifest_brcm_rpi.xml --create-dirs
    ```

### Android-16.0.0_r3 Build Target

=== "rpi4"
    ```text title="Tablet"
    lunch aosp_rpi4-bp3a-userdebug
    ```
    ```text title="TV"
    lunch aosp_rpi4_tv-bp3a-userdebug
    ```
    ```text title="Car"
    lunch aosp_rpi4_car-bp3a-userdebug
    ```
=== "rpi5"
    ```text title="Tablet"
    lunch aosp_rpi5-bp3a-userdebug
    ```
    ```text title="TV"
    lunch aosp_rpi5_tv-bp3a-userdebug
    ```
    ```text title="Car"
    lunch aosp_rpi5_car-bp3a-userdebug
    ```