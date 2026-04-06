# Android 12 for Pi4

> - Nguồn bài viết tại: [raspberrypi forum](https://forums.raspberrypi.com/viewtopic.php?t=376222)
> - [Android 12 (konstakang)](https://konstakang.com/devices/rpi4/AOSP12/)
> - [Github](https://github.com/raspberry-vanilla/android_local_manifest/tree/android-12.1)

## Install Package

### Primary Packages

```bash
sudo apt-get install git-core gnupg flex bison build-essential zip curl zlib1g-dev libc6-dev-i386 x11proto-core-dev libx11-dev lib32z1-dev libgl1-mesa-dev libxml2-utils xsltproc unzip fontconfig
```

### Additional Packages

```bash
sudo apt-get install bc coreutils dosfstools e2fsprogs fdisk kpartx mtools ninja-build pkg-config python3-pip
sudo pip3 install meson mako jinja2 ply pyyaml
```

## Initialize Repo

### Full

```bash
repo init -u https://android.googlesource.com/platform/manifest -b android-12.1.0_r22
curl -o .repo/local_manifests/manifest_brcm_rpi4.xml -L https://raw.githubusercontent.com/raspberry-vanilla/android_local_manifest/android-12.1/manifest_brcm_rpi4.xml --create-dirs
```
### Reduced

```bash title="Reduced"
repo init -u https://android.googlesource.com/platform/manifest -b android-12.1.0_r22 --depth=1
curl -o .repo/local_manifests/manifest_brcm_rpi4.xml -L https://raw.githubusercontent.com/raspberry-vanilla/android_local_manifest/android-12.1/manifest_brcm_rpi4.xml --create-dirs
curl -o .repo/local_manifests/remove_projects.xml -L https://raw.githubusercontent.com/raspberry-vanilla/android_local_manifest/android-12.1/remove_projects.xml
```

## Sync Source Code

### One Steps

This way short but slow

```bash
repo sync 
```

### Two Steps

This way faster

```bash
repo sync -j 16 --network-only 
repo sync -j 64 --local-only
```

## Compile

```bash
. build/envsetup.sh
lunch aosp_rpi4-userdebug
make bootimage systemimage vendorimage -j$(nproc)
```

## Make Image

```bash
./rpi4-mkimg.sh
```