# \[Android\] ADB bugreport

`adb bugreport` là lệnh thường thấy nhất để sử dụng khi muốn debug. Sau khi sử dụng lệnh, công cụ sẽ tạo ra một tệp `.zip` có tên được bắt đầu bằng _bugreport-XXX-XXXX.zip_ với theo sau đó là thời gian với tên thiết bị.

Trong tệp __*bugreport*__ có cấu trúc như sau:

```text
. (bugreport-atom-UQ1A.231205.015-2026-01-28-11-13-04)
├── FS
│   ├── data
│   │   ├── anr
│   │   ├── misc
│   │   │   ├── bluetooth
│   │   │   │   └── logs
│   │   │   ├── logd <---------------------- logcat history
│   │   │   ├── profiles
│   │   │   │   └── cur
│   │   │   ├── recovery
│   │   │   │   └── proc
│   │   │   ├── update_engine
│   │   │   │   └── prefs
│   │   │   ├── update_engine_log
│   │   │   └── wmtrace
│   │   ├── system
│   │   │   └── dropbox
│   │   └── tombstones <---------------------- report deadly process
│   ├── linkerconfig
│   ├── proc
│   ├── system
│   ├── system_ext
│   └── vendor
├── lshal-debug
└── proto
```

Trong đó hai tệp quan trọng nhất đó là:

- `./FS/data/misc/logd` sẽ chứa nhật ký của toàn bộ chương trình.
    - Đây là một thư mục, và nó có chứa rất nhiều tệp con ở trong như __*logcat.001, logcat.002, ...*__.
    - Về mặt thời gian, các tập có số thứ tự càng cao là những nhật ký xa xôi nhất. Các số thấp là các nhật ký gần nhất.
- `./FS/data/misc/tombstone` chứa các tệp phản hồi được ghi lại nếu một tiến trình bị kết thúc một cách ép buộc như __crash()__, __abort()__, ... dùng để đọc lại khi một tiến trình bị chết đứng.
    - Trong thư mục này gồm nhiều tệp có dạng như **tombstone_xx** và **tombstone_xx.pb**. Trong đó tệp **tombstone_xx** đọc như thông thường, còn tệp **tombstone_xx.pb** được dùng để _debug_ kèm với công cụ trong __ndk__

## Hướng dẫn debug tombstone