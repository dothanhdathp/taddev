# Android AOSP for Pi

> - Nguồn bài viết tại: [raspberrypi forum](https://forums.raspberrypi.com/viewtopic.php?t=376222)
> - [Android 16 (konstakang)](https://konstakang.com/devices/rpi4/AOSP16/)

## Hướng Dẫn

{{ slide("dev/build-android-16-for-pi4-pi5.html") }}

## About Reversion

| Reversion          | Maintained |                                            Github                                             |   Pi4   |   Pi5   |
| :----------------- | :--------: | :-------------------------------------------------------------------------------------------: | :-----: | :-----: |
| android-16.0       |  &check;   |    [_link_](https://github.com/raspberry-vanilla/android_local_manifest/tree/android-16.0)    | &check; | &check; |
| android-16.0.0_r1  |  &cross;   | [_link_](https://github.com/raspberry-vanilla/android_local_manifest/tree/android-16.0.0_r1)  | &check; | &check; |
| android-16.0.0_r3  |  &cross;   | [_link_](https://github.com/raspberry-vanilla/android_local_manifest/tree/android-16.0.0_r3)  | &check; | &check; |
| android-15.0       |  &check;   |    [_link_](https://github.com/raspberry-vanilla/android_local_manifest/tree/android-15.0)    | &check; | &check; |
| android-15.0.0_r4  |  &cross;   | [_link_](https://github.com/raspberry-vanilla/android_local_manifest/tree/android-15.0.0_r4)  | &check; | &check; |
| android-15.0.0_r14 |  &cross;   | [_link_](https://github.com/raspberry-vanilla/android_local_manifest/tree/android-15.0.0_r14) | &check; | &check; |
| android-14.0       |  &check;   |    [_link_](https://github.com/raspberry-vanilla/android_local_manifest/tree/android-14.0)    | &check; | &check; |
| android-14.0.0_r22 |  &cross;   | [_link_](https://github.com/raspberry-vanilla/android_local_manifest/tree/android-14.0.0_r22) | &check; | &check; |
| android-14.0.0_r34 |  &cross;   | [_link_](https://github.com/raspberry-vanilla/android_local_manifest/tree/android-14.0.0_r34) | &check; | &check; |
| android-13.0       |  &check;   |    [_link_](https://github.com/raspberry-vanilla/android_local_manifest/tree/android-13.0)    | &check; | &cross; |
| android-12.1       |  &check;   |    [_link_](https://github.com/raspberry-vanilla/android_local_manifest/tree/android-12.1)    | &check; | &cross; |

## Các Phiên Bản

<!--------------------------------------------------------------------------
****************************************************************************
android-16.0
****************************************************************************
---------------------------------------------------------------------------->

??? success "android-16.0"

    **Primary Packages**

    ```bash
    sudo apt-get install git-core gnupg flex bison build-essential \
    zip curl zlib1g-dev libc6-dev-i386 x11proto-core-dev libx11-dev \
    lib32z1-dev libgl1-mesa-dev libxml2-utils xsltproc unzip fontconfig
    ```

    **Additional Packages**

    ```bash
    sudo apt-get install dosfstools e2fsprogs fdisk kpartx mtools rsync
    ```

    **Init Repo**

    === "Reduced"
        ```bash
        repo init -u https://android.googlesource.com/platform/manifest -b android-16.0.0_r4 --depth=1
        curl -o .repo/local_manifests/manifest_brcm_rpi.xml -L https://raw.githubusercontent.com/raspberry-vanilla/android_local_manifest/android-16.0/manifest_brcm_rpi.xml --create-dirs
        curl -o .repo/local_manifests/remove_projects.xml -L https://raw.githubusercontent.com/raspberry-vanilla/android_local_manifest/android-16.0/remove_projects.xml
        ```
    === "Full"
        ```bash
        repo init -u https://android.googlesource.com/platform/manifest -b android-16.0.0_r4
        curl -o .repo/local_manifests/manifest_brcm_rpi.xml -L https://raw.githubusercontent.com/raspberry-vanilla/android_local_manifest/android-16.0/manifest_brcm_rpi.xml --create-dirs
        ```

    **Sync**

    === "Sync Optimize"
        ```bash
        repo sync -j 16 --network-only 
        repo sync -j 64 --local-only
        ```
    === "Sync Normal"
        ```bash
        repo sync 
        ```

    **Set Environment**

    ```bash
    . build/envsetup.sh
    ```

    **Select build target**

    === "Raspberry Pi 4"
        - Tablet
            ```bash
            lunch aosp_rpi4-bp4a-userdebug
            ```
        - TV
            ```bash
            lunch aosp_rpi4_tv-bp4a-userdebug
            ```
        - Car
            ```bash
            lunch aosp_rpi4_car-bp4a-userdebug
            ```
    === "Raspberry Pi 5"
        - Tablet
            ```bash
            lunch aosp_rpi5-bp4a-userdebug
            ```
        - TV
            ```bash
            lunch aosp_rpi5_tv-bp4a-userdebug
            ```
        - Car
            ```bash
            lunch aosp_rpi5_car-bp4a-userdebug
            ```

    **Compile**

    ```bash
    make bootimage systemimage vendorimage -j$(nproc)
    ```

    **Make Image**

    === "Raspberry Pi 4"
        ```bash
        ./rpi4-mkimg.sh
        ```
    === "Raspberry Pi 5"
        ```bash
        ./rpi5-mkimg.sh
        ```

    **Output**

    ???

<!--------------------------------------------------------------------------
****************************************************************************
android-16.0.0_r1
****************************************************************************
---------------------------------------------------------------------------->

??? warning "android-16.0.0_r1"
    > [Github](https://github.com/raspberry-vanilla/android_local_manifest/tree/android-16.0.0_r1)

    **Primary Packages**

    ```bash
    sudo apt-get install git-core gnupg flex bison build-essential \
    zip curl zlib1g-dev libc6-dev-i386 x11proto-core-dev libx11-dev \
    lib32z1-dev libgl1-mesa-dev libxml2-utils xsltproc unzip fontconfig
    ```

    **Additional Packages**

    ```bash
    sudo apt-get install dosfstools e2fsprogs fdisk kpartx mtools rsync
    ```

    **Init Repo**

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

    **Sync**

    === "Sync Optimize"
        ```bash
        repo sync -j 16 --network-only 
        repo sync -j 64 --local-only
        ```
    === "Sync Normal"
        ```bash
        repo sync 
        ```

    **Set Environment**

    ```bash
    . build/envsetup.sh
    ```

    **Select build target**

    === "Raspberry Pi 4"
        - Tablet
            ```bash
            lunch aosp_rpi4-bp2a-userdebug
            ```
        - TV
            ```bash
            lunch aosp_rpi4_tv-bp2a-userdebug
            ```
        - Car
            ```bash
            lunch aosp_rpi4_car-bp2a-userdebug
            ```
    === "Raspberry Pi 5"
        - Tablet
            ```bash
            lunch aosp_rpi5-bp2a-userdebug
            ```
        - TV
            ```bash
            lunch aosp_rpi5_tv-bp2a-userdebug
            ```
        - Car
            ```bash
            lunch aosp_rpi5_car-bp2a-userdebug
            ```

    **Compile**

    ```bash
    make bootimage systemimage vendorimage -j$(nproc)
    ```

    **Make Image**

    === "Raspberry Pi 4"
        ```bash
        ./rpi4-mkimg.sh
        ```
    === "Raspberry Pi 5"
        ```bash
        ./rpi5-mkimg.sh
        ```

    **Output**

    ???

<!--------------------------------------------------------------------------
****************************************************************************
android-16.0.0_r3
****************************************************************************
---------------------------------------------------------------------------->

??? warning "android-16.0.0_r3"
    > [Github](https://github.com/raspberry-vanilla/android_local_manifest/tree/android-16.0.0_r3)

    **Primary Packages**

    ```bash
    sudo apt-get install git-core gnupg flex bison build-essential \
    zip curl zlib1g-dev libc6-dev-i386 x11proto-core-dev libx11-dev \
    lib32z1-dev libgl1-mesa-dev libxml2-utils xsltproc unzip fontconfig
    ```

    **Additional Packages**

    ```bash
    sudo apt-get install dosfstools e2fsprogs fdisk kpartx mtools rsync
    ```

    **Init Repo **

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

    **Sync**

    === "Sync Optimize"
        ```bash
        repo sync -j 16 --network-only 
        repo sync -j 64 --local-only
        ```
    === "Sync Normal"
        ```bash
        repo sync 
        ```

    **Set Environment**

    ```bash
    . build/envsetup.sh
    ```

    **Select build target**

    === "Raspberry Pi 4"
        - Tablet
            ```bash
            lunch aosp_rpi4-bp3a-userdebug
            ```
        - TV
            ```bash
            lunch aosp_rpi4_tv-bp3a-userdebug
            ```
        - Car
            ```bash
            lunch aosp_rpi4_car-bp3a-userdebug
            ```
    === "Raspberry Pi 5"
        - Tablet
            ```bash
            lunch aosp_rpi5-bp3a-userdebug
            ```
        - TV
            ```bash
            lunch aosp_rpi5_tv-bp3a-userdebug
            ```
        - Car
            ```bash
            lunch aosp_rpi5_car-bp3a-userdebug
            ```

    **Compile**

    ```bash
    make bootimage systemimage vendorimage -j$(nproc)
    ```

    **Make Image**

    === "Raspberry Pi 4"
        ```bash
        ./rpi4-mkimg.sh
        ```
    === "Raspberry Pi 5"
        ```bash
        ./rpi5-mkimg.sh
        ```

    **Output**

    ???


<!--------------------------------------------------------------------------
****************************************************************************
android-15.0
****************************************************************************
---------------------------------------------------------------------------->

??? success "android-15.0"
    > [Github](https://github.com/raspberry-vanilla/android_local_manifest/tree/android-15.0)

    **Primary Packages**

    ```bash
    sudo apt-get install git-core gnupg flex bison build-essential zip curl zlib1g-dev libc6-dev-i386 x11proto-core-dev libx11-dev lib32z1-dev libgl1-mesa-dev libxml2-utils xsltproc unzip fontconfig
    ```

    **Additional Packages**

    ```bash
    sudo apt-get install dosfstools e2fsprogs fdisk kpartx mtools rsync
    ```

    **Init Repo **

    === "Reduced"
        ```bash
        repo init -u https://android.googlesource.com/platform/manifest -b android-15.0.0_r32 --depth=1
        curl -o .repo/local_manifests/manifest_brcm_rpi.xml -L https://raw.githubusercontent.com/raspberry-vanilla/android_local_manifest/android-15.0/manifest_brcm_rpi.xml --create-dirs
        curl -o .repo/local_manifests/remove_projects.xml -L https://raw.githubusercontent.com/raspberry-vanilla/android_local_manifest/android-15.0/remove_projects.xml
        ```
    === "Full"
        ```bash
        repo init -u https://android.googlesource.com/platform/manifest -b android-15.0.0_r32
        curl -o .repo/local_manifests/manifest_brcm_rpi.xml -L https://raw.githubusercontent.com/raspberry-vanilla/android_local_manifest/android-15.0/manifest_brcm_rpi.xml --create-dirs
        ```

    **Sync**

    === "Sync Optimize"
        ```bash
        repo sync -j 16 --network-only 
        repo sync -j 64 --local-only
        ```
    === "Sync Normal"
        ```bash
        repo sync 
        ```

    **Set Environment**

    ```bash
    . build/envsetup.sh
    ```

    **Select build target**

    === "Raspberry Pi 4"
        - Tablet
            ```bash
            lunch aosp_rpi4-bp1a-userdebug
            ```
        - TV
            ```bash
            lunch aosp_rpi4_tv-bp1a-userdebug
            ```
        - Car
            ```bash
            lunch aosp_rpi4_car-bp1a-userdebug
            ```
    === "Raspberry Pi 5"
        - Tablet
            ```bash
            lunch aosp_rpi5-bp1a-userdebug
            ```
        - TV
            ```bash
            lunch aosp_rpi5_tv-bp1a-userdebug
            ```
        - Car
            ```bash
            lunch aosp_rpi5_car-bp1a-userdebug
            ```

    **Compile**

    ```bash
    make bootimage systemimage vendorimage -j$(nproc)
    ```

    **Make Image**

    === "Raspberry Pi 4"
        ```bash
        ./rpi4-mkimg.sh
        ```
    === "Raspberry Pi 5"
        ```bash
        ./rpi5-mkimg.sh
        ```

    **Output**

    ???

<!--------------------------------------------------------------------------
****************************************************************************
android-15.0.0_r4
****************************************************************************
---------------------------------------------------------------------------->

??? warning "android-15.0.0_r4"
    > [Github](https://github.com/raspberry-vanilla/android_local_manifest/tree/android-15.0.0_r4)

    **Primary Packages**

    ```bash
    sudo apt-get install git-core gnupg flex bison build-essential zip curl zlib1g-dev libc6-dev-i386 x11proto-core-dev libx11-dev lib32z1-dev libgl1-mesa-dev libxml2-utils xsltproc unzip fontconfig
    ```

    **Additional Packages**

    ```bash
    sudo apt-get install bc coreutils dosfstools e2fsprogs fdisk kpartx mtools ninja-build pkg-config python3-pip
    sudo pip3 install meson mako jinja2 ply pyyaml dataclasses
    ```

    **Init Repo **

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

    **Sync**

    === "Sync Optimize"
        ```bash
        repo sync -j 16 --network-only 
        repo sync -j 64 --local-only
        ```
    === "Sync Normal"
        ```bash
        repo sync 
        ```

    **Set Environment**

    ```bash
    . build/envsetup.sh
    ```

    **Select build target**

    === "Raspberry Pi 4"
        - Tablet
            ```bash
            lunch aosp_rpi4-ap3a-userdebug
            ```
        - TV
            ```bash
            lunch aosp_rpi4_tv-ap3a-userdebug
            ```
        - Car
            ```bash
            lunch aosp_rpi4_car-ap3a-userdebug
            ```
    === "Raspberry Pi 5"
        - Tablet
            ```bash
            lunch aosp_rpi5-ap3a-userdebug
            ```
        - TV
            ```bash
            lunch aosp_rpi5_tv-ap3a-userdebug
            ```
        - Car
            ```bash
            lunch aosp_rpi5_car-ap3a-userdebug
            ```

    **Compile**

    ```bash
    make bootimage systemimage vendorimage -j$(nproc)
    ```

    **Make Image**

    === "Raspberry Pi 4"
        ```bash
        ./rpi4-mkimg.sh
        ```
    === "Raspberry Pi 5"
        ```bash
        ./rpi5-mkimg.sh
        ```

    **Output**

    ???

<!--------------------------------------------------------------------------
****************************************************************************
android-15.0.0_r14
****************************************************************************
---------------------------------------------------------------------------->

??? warning "android-15.0.0_r14"
    > [Github](https://github.com/raspberry-vanilla/android_local_manifest/tree/android-15.0.0_r14)

    **Primary Packages**

    ```bash
    sudo apt-get install git-core gnupg flex bison build-essential zip curl zlib1g-dev libc6-dev-i386 x11proto-core-dev libx11-dev lib32z1-dev libgl1-mesa-dev libxml2-utils xsltproc unzip fontconfig
    ```

    **Additional Packages**

    ```bash
    sudo apt-get install coreutils dosfstools e2fsprogs fdisk kpartx mtools ninja-build pkg-config python3-pip rsync
    sudo pip3 install dataclasses jinja2 mako meson ply pyyaml
    ```

    **Init Repo **

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

    **Sync**

    === "Sync Optimize"
        ```bash
        repo sync -j 16 --network-only 
        repo sync -j 64 --local-only
        ```
    === "Sync Normal"
        ```bash
        repo sync 
        ```

    **Set Environment**

    ```bash
    . build/envsetup.sh
    ```

    **Select build target**

    === "Raspberry Pi 4"
        - Tablet
            ```bash
            lunch aosp_rpi4-ap4a-userdebug
            ```
        - TV
            ```bash
            lunch aosp_rpi4_tv-ap4a-userdebug
            ```
        - Car
            ```bash
            lunch aosp_rpi4_car-ap4a-userdebug
            ```
    === "Raspberry Pi 5"
        - Tablet
            ```bash
            lunch aosp_rpi5-ap4a-userdebug
            ```
        - TV
            ```bash
            lunch aosp_rpi5_tv-ap4a-userdebug
            ```
        - Car
            ```bash
            lunch aosp_rpi5_car-ap4a-userdebug
            ```

    **Compile**

    ```bash
    make bootimage systemimage vendorimage -j$(nproc)
    ```

    **Make Image**

    === "Raspberry Pi 4"
        ```bash
        ./rpi4-mkimg.sh
        ```
    === "Raspberry Pi 5"
        ```bash
        ./rpi5-mkimg.sh
        ```

    **Output**

    ???

<!--------------------------------------------------------------------------
****************************************************************************
android-14.0
****************************************************************************
---------------------------------------------------------------------------->

??? success "android-14.0"
    > [Github](https://github.com/raspberry-vanilla/android_local_manifest/tree/android-14.0)

    **Primary Packages**

    ```bash
    sudo apt-get install git-core gnupg flex bison build-essential zip curl zlib1g-dev libc6-dev-i386 x11proto-core-dev libx11-dev lib32z1-dev libgl1-mesa-dev libxml2-utils xsltproc unzip fontconfig
    ```

    **Additional Packages**

    ```bash
    sudo apt-get install bc coreutils dosfstools e2fsprogs fdisk kpartx mtools ninja-build pkg-config python3-pip rsync
    sudo pip3 install meson mako jinja2 ply pyyaml dataclasses
    ```

    **Init Repo **

    === "Reduced"
        ```bash
        repo init -u https://android.googlesource.com/platform/manifest -b android-14.0.0_r67 --depth=1
        curl -o .repo/local_manifests/manifest_brcm_rpi.xml -L https://raw.githubusercontent.com/raspberry-vanilla/android_local_manifest/android-14.0/manifest_brcm_rpi.xml --create-dirs
        curl -o .repo/local_manifests/remove_projects.xml -L https://raw.githubusercontent.com/raspberry-vanilla/android_local_manifest/android-14.0/remove_projects.xml
        ```
    === "Full"
        ```bash
        repo init -u https://android.googlesource.com/platform/manifest -b android-14.0.0_r67
        curl -o .repo/local_manifests/manifest_brcm_rpi.xml -L https://raw.githubusercontent.com/raspberry-vanilla/android_local_manifest/android-14.0/manifest_brcm_rpi.xml --create-dirs
        ```

    **Sync**

    === "Sync Optimize"
        ```bash
        repo sync -j 16 --network-only 
        repo sync -j 64 --local-only
        ```
    === "Sync Normal"
        ```bash
        repo sync 
        ```

    **Set Environment**

    ```bash
    . build/envsetup.sh
    ```

    **Select build target**

    === "Raspberry Pi 4"
        - Tablet
            ```bash
            lunch aosp_rpi4-ap2a-userdebug
            ```
        - TV
            ```bash
            lunch aosp_rpi4_tv-ap2a-userdebug
            ```
        - Car
            ```bash
            lunch aosp_rpi4_car-ap2a-userdebug
            ```
    === "Raspberry Pi 5"
        - Tablet
            ```bash
            lunch aosp_rpi5-ap2a-userdebug
            ```
        - TV
            ```bash
            lunch aosp_rpi5_tv-ap2a-userdebug
            ```
        - Car
            ```bash
            lunch aosp_rpi5_car-ap2a-userdebug
            ```

    **Compile**

    ```bash
    make bootimage systemimage vendorimage -j$(nproc)
    ```

    **Make Image**

    === "Raspberry Pi 4"
        ```bash
        ./rpi4-mkimg.sh
        ```
    === "Raspberry Pi 5"
        ```bash
        ./rpi5-mkimg.sh
        ```

    **Output**

    ???

<!--------------------------------------------------------------------------
****************************************************************************
android-14.0.0_r22
****************************************************************************
---------------------------------------------------------------------------->

??? warning "android-14.0.0_r22"
    > [Github](https://github.com/raspberry-vanilla/android_local_manifest/tree/android-14.0.0_r22)

    **Primary Packages**

    ```bash
    sudo apt-get install git-core gnupg flex bison build-essential zip curl zlib1g-dev libc6-dev-i386 x11proto-core-dev libx11-dev lib32z1-dev libgl1-mesa-dev libxml2-utils xsltproc unzip fontconfig
    ```

    **Additional Packages**

    ```bash
    sudo apt-get install coreutils dosfstools e2fsprogs fdisk kpartx mtools ninja-build pkg-config python3-pip rsync
    sudo pip3 install dataclasses jinja2 mako meson ply pyyaml
    ```

    **Init Repo **

    === "Reduced"
        ```bash
        repo init -u https://android.googlesource.com/platform/manifest -b android-14.0.0_r22 --depth=1
        curl -o .repo/local_manifests/manifest_brcm_rpi.xml -L https://raw.githubusercontent.com/raspberry-vanilla/android_local_manifest/android-14.0.0_r22/manifest_brcm_rpi.xml --create-dirs
        curl -o .repo/local_manifests/remove_projects.xml -L https://raw.githubusercontent.com/raspberry-vanilla/android_local_manifest/android-14.0.0_r22/remove_projects.xml
        ```
    === "Full"
        ```bash
        repo init -u https://android.googlesource.com/platform/manifest -b android-14.0.0_r22
        curl -o .repo/local_manifests/manifest_brcm_rpi.xml -L https://raw.githubusercontent.com/raspberry-vanilla/android_local_manifest/android-14.0.0_r22/manifest_brcm_rpi.xml --create-dirs
        ```

    **Sync**

    === "Sync Optimize"
        ```bash
        repo sync -j 16 --network-only 
        repo sync -j 64 --local-only
        ```
    === "Sync Normal"
        ```bash
        repo sync 
        ```

    **Set Environment**

    ```bash
    . build/envsetup.sh
    ```

    **Select build target**

    === "Raspberry Pi 4"
        - Tablet
            ```bash
            lunch aosp_rpi4-userdebug
            ```
        - TV
            ```bash
            lunch aosp_rpi4_tv-userdebug
            ```
        - Car
            ```bash
            lunch aosp_rpi4_car-userdebug
            ```
    === "Raspberry Pi 5"
        - Tablet
            ```bash
            lunch aosp_rpi5-userdebug
            ```
        - TV
            ```bash
            lunch aosp_rpi5_tv-userdebug
            ```
        - Car
            ```bash
            lunch aosp_rpi5_car-userdebug
            ```

    **Compile**

    ```bash
    make bootimage systemimage vendorimage -j$(nproc)
    ```

    **Make Image**

    === "Raspberry Pi 4"
        ```bash
        ./rpi4-mkimg.sh
        ```
    === "Raspberry Pi 5"
        ```bash
        ./rpi5-mkimg.sh
        ```

    **Output**

    ???

<!--------------------------------------------------------------------------
****************************************************************************
android-14.0.0_r34
****************************************************************************
---------------------------------------------------------------------------->

??? warning "android-14.0.0_r34"
    > [Github](https://github.com/raspberry-vanilla/android_local_manifest/tree/android-14.0.0_r34)

    **Primary Packages**

    ```bash
    sudo apt-get install git-core gnupg flex bison build-essential zip curl zlib1g-dev libc6-dev-i386 x11proto-core-dev libx11-dev lib32z1-dev libgl1-mesa-dev libxml2-utils xsltproc unzip fontconfig
    ```

    **Additional Packages**

    ```bash
    sudo apt-get install coreutils dosfstools e2fsprogs fdisk kpartx mtools ninja-build pkg-config python3-pip rsync
    sudo pip3 install dataclasses jinja2 mako meson ply pyyaml
    ```

    **Init Repo **

    === "Reduced"
        ```bash
        repo init -u https://android.googlesource.com/platform/manifest -b android-14.0.0_r34 --depth=1
        curl -o .repo/local_manifests/manifest_brcm_rpi.xml -L https://raw.githubusercontent.com/raspberry-vanilla/android_local_manifest/android-14.0.0_r34/manifest_brcm_rpi.xml --create-dirs
        curl -o .repo/local_manifests/remove_projects.xml -L https://raw.githubusercontent.com/raspberry-vanilla/android_local_manifest/android-14.0.0_r34/remove_projects.xml
        ```
    === "Full"
        ```bash
        repo init -u https://android.googlesource.com/platform/manifest -b android-14.0.0_r34
        curl -o .repo/local_manifests/manifest_brcm_rpi.xml -L https://raw.githubusercontent.com/raspberry-vanilla/android_local_manifest/android-14.0.0_r34/manifest_brcm_rpi.xml --create-dirs
        ```

    **Sync**

    === "Sync Optimize"
        ```bash
        repo sync -j 16 --network-only 
        repo sync -j 64 --local-only
        ```
    === "Sync Normal"
        ```bash
        repo sync 
        ```

    **Set Environment**

    ```bash
    . build/envsetup.sh
    ```

    **Select build target**

    === "Raspberry Pi 4"
        - Tablet
            ```bash
            lunch aosp_rpi4-ap1a-userdebug
            ```
        - TV
            ```bash
            lunch aosp_rpi4_tv-ap1a-userdebug
            ```
        - Car
            ```bash
            lunch aosp_rpi4_car-ap1a-userdebug
            ```
    === "Raspberry Pi 5"
        - Tablet
            ```bash
            lunch aosp_rpi5-ap1a-userdebug
            ```
        - TV
            ```bash
            lunch aosp_rpi5_tv-ap1a-userdebug
            ```
        - Car
            ```bash
            lunch aosp_rpi5_car-ap1a-userdebug
            ```

    **Compile**

    ```bash
    make bootimage systemimage vendorimage -j$(nproc)
    ```

    **Make Image**

    === "Raspberry Pi 4"
        ```bash
        ./rpi4-mkimg.sh
        ```
    === "Raspberry Pi 5"
        ```bash
        ./rpi5-mkimg.sh
        ```

    **Output**

    ???

<!--------------------------------------------------------------------------
****************************************************************************
android-13.0
****************************************************************************
---------------------------------------------------------------------------->

??? success "android-13.0"
    > [Github](https://github.com/raspberry-vanilla/android_local_manifest/tree/android-13.0)

    **Primary Packages**

    ```bash
    sudo apt-get install git-core gnupg flex bison build-essential zip curl zlib1g-dev libc6-dev-i386 x11proto-core-dev libx11-dev lib32z1-dev libgl1-mesa-dev libxml2-utils xsltproc unzip fontconfig
    ```

    **Additional Packages**

    ```bash
    sudo apt-get install bc coreutils dosfstools e2fsprogs fdisk kpartx mtools ninja-build pkg-config python3-pip
    sudo pip3 install meson mako jinja2 ply pyyaml dataclasses
    ```

    **Init Repo **

    === "Reduced"
        ```bash
        repo init -u https://android.googlesource.com/platform/manifest -b android-13.0.0_r75 --depth=1
        curl -o .repo/local_manifests/manifest_brcm_rpi4.xml -L https://raw.githubusercontent.com/raspberry-vanilla/android_local_manifest/android-13.0/manifest_brcm_rpi4.xml --create-dirs
        curl -o .repo/local_manifests/remove_projects.xml -L https://raw.githubusercontent.com/raspberry-vanilla/android_local_manifest/android-13.0/remove_projects.xml
        ```
    === "Full"
        ```bash
        repo init -u https://android.googlesource.com/platform/manifest -b android-13.0.0_r75
        curl -o .repo/local_manifests/manifest_brcm_rpi4.xml -L https://raw.githubusercontent.com/raspberry-vanilla/android_local_manifest/android-13.0/manifest_brcm_rpi4.xml --create-dirs
        ```

    **Sync**

    === "Sync Optimize"
        ```bash
        repo sync -j 16 --network-only 
        repo sync -j 64 --local-only
        ```
    === "Sync Normal"
        ```bash
        repo sync 
        ```

    **Set Environment**

    ```bash
    . build/envsetup.sh
    ```

    **Select build target**

    - Raspberry Pi 4
        - Tablet
            ```bash
            lunch aosp_rpi4-userdebug
            ```
        - TV
            ```bash
            lunch aosp_rpi4_tv-userdebug
            ```
        - Car
            ```bash
            lunch aosp_rpi4_car-userdebug
            ```

    **Compile**

    ```bash
    make bootimage systemimage vendorimage -j$(nproc)
    ```

    **Make Image**

    ```bash
    ./rpi4-mkimg.sh
    ```

    **Output**

    ???

<!--------------------------------------------------------------------------
****************************************************************************
android-12.1
****************************************************************************
---------------------------------------------------------------------------->

??? success "android-12.1"
    > [Github](https://github.com/raspberry-vanilla/android_local_manifest/tree/android-12.1)

    **Primary Packages**

    ```bash
    sudo apt-get install git-core gnupg flex bison build-essential zip curl zlib1g-dev libc6-dev-i386 x11proto-core-dev libx11-dev lib32z1-dev libgl1-mesa-dev libxml2-utils xsltproc unzip fontconfig
    ```

    **Additional Packages**

    ```bash
    sudo apt-get install bc coreutils dosfstools e2fsprogs fdisk kpartx mtools ninja-build pkg-config python3-pip
    sudo pip3 install meson mako jinja2 ply pyyaml
    ```

    **Init Repo **

    === "Reduced"
        ```bash
        repo init -u https://android.googlesource.com/platform/manifest -b android-12.1.0_r22 --depth=1
        curl -o .repo/local_manifests/manifest_brcm_rpi4.xml -L https://raw.githubusercontent.com/raspberry-vanilla/android_local_manifest/android-12.1/manifest_brcm_rpi4.xml --create-dirs
        curl -o .repo/local_manifests/remove_projects.xml -L https://raw.githubusercontent.com/raspberry-vanilla/android_local_manifest/android-12.1/remove_projects.xml
        ```
    === "Full"
        ```bash
        repo init -u https://android.googlesource.com/platform/manifest -b android-12.1.0_r22
        curl -o .repo/local_manifests/manifest_brcm_rpi4.xml -L https://raw.githubusercontent.com/raspberry-vanilla/android_local_manifest/android-12.1/manifest_brcm_rpi4.xml --create-dirs
        ```

    **Sync**

    === "Sync Optimize"
        ```bash
        repo sync -j 16 --network-only 
        repo sync -j 64 --local-only
        ```
    === "Sync Normal"
        ```bash
        repo sync 
        ```

    **Compile**

    ```bash
    . build/envsetup.sh
    lunch aosp_rpi4-userdebug
    make bootimage systemimage vendorimage -j$(nproc)
    ```

    **Output**

    ???
