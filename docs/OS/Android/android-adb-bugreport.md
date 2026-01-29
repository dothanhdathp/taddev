# \[Android\] ADB bugreport

`adb bugreport` là lệnh thường thấy nhất để sử dụng khi muốn debug. Sau khi sử dụng lệnh, công cụ sẽ tạo ra một tệp `.zip` có tên được bắt đầu bằng _bugreport-XXX-XXXX.zip_ với theo sau đó là thời gian với tên thiết bị.

## Cấu Trúc Tệp

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

## ndk-stack

> Hướng dẫn debug tombstone. [ndk-stack](https://developer.android.com/ndk/guides/ndk-stack)

### ndk-stack ở đâu?

Trong tệp __*ndk*__ thường có sẵn một tệp dùng để _debug_, _trace_ cho các tệp tombstone là tệp `ndk-stack`. Trong các máy Ubuntu/Linux thường sẽ nằm ở đây:
`~/Android/Sdk/ndk/{version}/`. Tại đó, sẽ có tệp _script_ __*ndk-stack*__ chạy đến các tệp trong `{version}/prebuilt/linux-x86_64/bin/*`. Nói chung là đừng quan tâm nhiều, chỉ cần nhớ có thể dùng tệp đó là được.

Hướng dẫn sử dụng là:

```text
usage: ndk-stack.py [-h] -sym SYMBOL_DIR [-i INPUT]

Symbolizes Android crashes.

optional arguments:
  -h, --help            show this help message and exit
  -sym SYMBOL_DIR, --sym SYMBOL_DIR
                        directory containing unstripped .so files
  -i INPUT, -dump INPUT, --dump INPUT
                        input filename

See <https://developer.android.com/ndk/guides/ndk-stack>.
```

Vậy nên, để sử dụng thì sẽ dùng lệnh như sau:

```bash
ndk-stack.py -sym SYMBOL_DIR -i tombstone_xx
```

### Where is

```bash
$PATH_TO_YOUR_APP/build/intermediates/../{architecture}
```

*Ghi chú: Các kiến trúc (architecture) phổ biến là __armeabi__, __armeabi-v7a__, __arm64-v8a__, __x86__ và __x86_64__*

