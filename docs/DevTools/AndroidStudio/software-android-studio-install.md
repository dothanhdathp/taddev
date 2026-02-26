# Install Android Studio

## Tổng Quan

Hướng dẫn tải về __Android Studio__. Tải rất dễ cài cũng rất dễ. Cái quan trọng là ở phiên bản của __Android Studio__ thì nhiều vấn đề. __Android__ chỉ tồn tại một số phiên bản ổn định và một số trong đó là thỏa mãn các điều kiện cho phép việc chuyển đổi/sửa đổi tốt.

## Đường Dẫn

- Tải về Android Studio ___mới nhất___ từ trang chủ [link](https://developer.android.com/studio)
- Các ___phiên bản cũ hơn___ có thể xem ở đây [link](https://developer.android.com/studio/archive)

### Các phiên bản khuyến nghị

??? quote "Android Studio Hedgehog | 2023.1.1 Patch 2 January 23, 2024"
    _Bản này thì là bản ổn định nhất với UI được thay đổi gọn gàng hơn rất nhiều so với các bản cũ._

    | OS                   |   Size   |   Type    | File                                                                                                                                                     | SHA-256 checksums                                                  |
    | :------------------- | :------: | :-------: | :------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------- |
    | ChromeOS             | 911.8 MB | Installed | [android-studio-2023.1.1.28-cros.deb](https://redirector.gvt1.com/edgedl/android/studio/install/2023.1.1.28/android-studio-2023.1.1.28-cros.deb)         | `0fc8e9b8172a8e5011633701de3aa1ef19a776a0213822894d04a880bfbd4142` |
    | Mac (Apple Silicon)  |  1.2 GB  | Installed | [android-studio-2023.1.1.28-mac_arm.dmg](https://redirector.gvt1.com/edgedl/android/studio/install/2023.1.1.28/android-studio-2023.1.1.28-mac_arm.dmg)   | `1c63fb096b174106d53fa50584943b00e4da569c3f0ef4320c0d8231522cf299` |
    | Mac (Intel)          |  1.2 GB  | Installed | [android-studio-2023.1.1.28-mac.dmg](https://redirector.gvt1.com/edgedl/android/studio/install/2023.1.1.28/android-studio-2023.1.1.28-mac.dmg)           | `c19ce237293ae6455bdb1dad6db032852375a7e204c5d7c2252cb8d0234b0f69` |
    | **Windows (64-bit)** |  1.1 GB  | Installed | [android-studio-2023.1.1.28-windows.exe](https://redirector.gvt1.com/edgedl/android/studio/install/2023.1.1.28/android-studio-2023.1.1.28-windows.exe)   | `b6f1569d3a944e82b1beb5d4de39d7bdb434a7f2992eb965aae55c46915dff90` |
    | **Linux**            |  1.2 GB  | Zip File  | [android-studio-2023.1.1.28-linux.tar.gz](https://edgedl.me.gvt1.com/edgedl/android/studio/ide-zips/2023.1.1.28/android-studio-2023.1.1.28-linux.tar.gz) | `139d0dbb4909353b68fbf55c09b6d31a34512044a9d4f02ce0f1a9accca128f9` |
    | Mac (Apple Silicon)  |  1.2 GB  | Zip File  | [android-studio-2023.1.1.28-mac_arm.zip](https://edgedl.me.gvt1.com/edgedl/android/studio/ide-zips/2023.1.1.28/android-studio-2023.1.1.28-mac_arm.zip)   | `f5d76886251c49ab5e646fd3d7f38c2462b83673d1388d49e049bc054480fc85` |
    | Mac (Intel)          |  1.2 GB  | Zip File  | [android-studio-2023.1.1.28-mac.zip](https://edgedl.me.gvt1.com/edgedl/android/studio/ide-zips/2023.1.1.28/android-studio-2023.1.1.28-mac.zip)           | `3a5d073f22623ac501a2dd8b52983de58aa4ace88f15b72d49a036a49081318e` |
    | **Windows (64-bit)** |  1.1 GB  | Zip File  | [android-studio-2023.1.1.28-windows.zip](https://edgedl.me.gvt1.com/edgedl/android/studio/ide-zips/2023.1.1.28/android-studio-2023.1.1.28-windows.zip)   | `d8ff95274b59cf51aa60b06c4d26a1c9f9c75ae172135fd05684cc03f4363cba` |

??? quote "Android Studio Iguana | 2023.2.1 Patch 2 April 9, 2024"
    | OS                   |   Size   |   Type    | File                                        | SHA-256 checksums                                                  |
    | :------------------- | :------: | :-------: | :------------------------------------------ | :----------------------------------------------------------------- |
    | ChromeOS             | 944.2 MB | Installed | [android-studio-2023.2.1.25-cros.deb](https://edgedl.me.gvt1.com/edgedl/android/studio/install/2023.2.1.25/android-studio-2023.2.1.25-cros.deb)     | `fe1a2628d8698a27559cb8876f20f78ca0dd4dd0ed44045967815403a0c260ed` |
    | Mac (Apple Silicon)  |  1.2 GB  | Installed | [android-studio-2023.2.1.25-mac_arm.dmg](https://edgedl.me.gvt1.com/edgedl/android/studio/install/2023.2.1.25/android-studio-2023.2.1.25-mac_arm.dmg)  | `bc55ca35f72e6dcdccff617e6794e9fa4cebc28feff9fa612430d3fd01f95a3a` |
    | Mac (Intel)          |  1.2 GB  | Installed | [android-studio-2023.2.1.25-mac.dmg](https://edgedl.me.gvt1.com/edgedl/android/studio/install/2023.2.1.25/android-studio-2023.2.1.25-mac.dmg)      | `f16ef3483b341ef387c60d6d5a58618e190543256ddde4526c0dc730034a07df` |
    | **Windows (64-bit)** |  1.1 GB  | Installed | [android-studio-2023.2.1.25-windows.exe](https://edgedl.me.gvt1.com/edgedl/android/studio/install/2023.2.1.25/android-studio-2023.2.1.25-windows.exe)  | `ea891f977305dfaf58dfafed7908a6b14d7fdd9d2b024a80a13bd80b3a82c346` |
    | **Linux**            |  1.2 GB  | Zip File  | [android-studio-2023.2.1.25-linux.tar.gz](https://edgedl.me.gvt1.com/edgedl/android/studio/ide-zips/2023.2.1.25/android-studio-2023.2.1.25-linux.tar.gz) | `cd63ead467dc92a08ff6b3695c01d57e802976fc64acddcd31cd6a2427ffa1bc` |
    | Mac (Apple Silicon)  |  1.2 GB  | Zip File  | [android-studio-2023.2.1.25-mac_arm.zip](https://edgedl.me.gvt1.com/edgedl/android/studio/ide-zips/2023.2.1.25/android-studio-2023.2.1.25-mac_arm.zip)  | `7b2b386c66fd353a3d3a23638a0ff48024ec21aa952e12aa9f80f8176b779ab4` |
    | Mac (Intel)          |  1.2 GB  | Zip File  | [android-studio-2023.2.1.25-mac.zip](https://edgedl.me.gvt1.com/edgedl/android/studio/ide-zips/2023.2.1.25/android-studio-2023.2.1.25-mac.zip)      | `e52299b8568145f5065a8feeeb7ee4ea2d4aae277a8b5298c349bce288c8d10b` |
    | **Windows (64-bit)** |  1.2 GB  | Zip File  | [android-studio-2023.2.1.25-windows.zip](https://edgedl.me.gvt1.com/edgedl/android/studio/ide-zips/2023.2.1.25/android-studio-2023.2.1.25-windows.zip)  | `a1169fc0f6501846cc49e1075331709f7801c00caf77d311d9c0a7c39b8cad5a` | 

??? quote "Android Studio 4.1.3 March 18, 2021"
    <mark>Chủ yếu để dựng cho **Carlife** hệ thống cũ của **Android 9**</mark>

    | OS               |   Size   |   Type    | File                                                                                                                                                         | SHA-256 checksums                                                  |
    | :--------------- | :------: | :-------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------- |
    | ChromeOS         | 778.7 MB | Installed | [android-studio-ide-201.7199119-cros.deb](https://edgedl.me.gvt1.com/edgedl/android/studio/install/4.1.3.0/android-studio-ide-201.7199119-cros.deb)          | `d899b4419b25aa936e6bd50dc35f00ea055364069c2e43422d0b77604233a253` |
    | Mac              | 919.7 MB | Installed | [android-studio-ide-201.7199119-mac.dmg](https://edgedl.me.gvt1.com/edgedl/android/studio/install/4.1.3.0/android-studio-ide-201.7199119-mac.dmg)            | `e4b146e94595f9a928afba31c90303414b3b2a396796a8114d81cad484cada02` |
    | Windows (64-bit) | 939.7 MB | Installed | [android-studio-ide-201.7199119-windows.exe](https://edgedl.me.gvt1.com/edgedl/android/studio/install/4.1.3.0/android-studio-ide-201.7199119-windows.exe)    | `a5ef7507b1816e8e9c909d7037d7fff09263cd41935be0edc4a0383441e92b10` |
    | Linux            | 925.4 MB | Zip files | [android-studio-ide-201.7199119-linux.tar.gz](https://edgedl.me.gvt1.com/edgedl/android/studio/ide-zips/4.1.3.0/android-studio-ide-201.7199119-linux.tar.gz) | `f599749ca47cda06d392e2764017c8a8a0c7b963a6a88ed494b432bece7cbc1b` |
    | Mac              | 918.9 MB | Zip files | [android-studio-ide-201.7199119-mac.zip](https://edgedl.me.gvt1.com/edgedl/android/studio/ide-zips/4.1.3.0/android-studio-ide-201.7199119-mac.zip)           | `d512219e7d9261a1ccf3a92e31b3b03bfd4689221ef8e298abb3875d7493d5dc` |
    | Windows (64-bit) | 943.8 MB | Zip files | [android-studio-ide-201.7199119-windows.zip](https://edgedl.me.gvt1.com/edgedl/android/studio/ide-zips/4.1.3.0/android-studio-ide-201.7199119-windows.zip)   | `666436918f58c6ecc903d40410c4bc061e0fe0463e6be3920893a8020b833fb2` |

## Windows MultilInstall

1. Không nhất thiết chỉ có một bản cài đặt của __Android Studio__. Có thể cài đặt nhiều phiên bản __Android Studio__ trên cùng một máy.
1. Nếu cài đặt là mặc định thì nó sẽ để ở trong đường dẫn `C:\Program Files\Android`
1. Trong đó sẽ có nhiều thư mục của __Android Studio__