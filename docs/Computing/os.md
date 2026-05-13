# Operating System

## Operating System

### Tóm Tắt Nội Dung

Cuốn sách {{ book("Operating System", "operating-system") }} viết về **hệ điều hành** và các khái niệm, thuật ngữ xoay quanh hệ điều hành.

- {{ book("Chương 1: Lời Mở Đầu", "operating-system") }}
- {{ book("Chương 2: Phân loại hệ điều hành", "operating-system", "os-types") }}
	- Chương này phân loại hệ điều hành theo các cấu trúc như **User & Tasking**, **Processing Style**, **Device Types** và theo **Kernel Architecture**
- {{ book("Chương 3: File System", "operating-system", "os-file-system") }}
	- Các định dạng tệp như `NTFS`, `FAT32`, `exFAT`, `ext4`, `APFS`
- {{ book("Chương 4: OS API", "operating-system", "os-api") }}
	- Tiêu chuẩn `POSIX` và `WIN32`
- {{ book("Chương 5: POSIX", "operating-system", "os-posix") }}
	- POSIX Signal
	- POSIX SIGKILL
		- `Named Mutex`, `Robust Mutexes`, `Death Lock`
	- POSIX Shell
- {{ book("Chương 6: Win32", "operating-system", "os-win32") }}

### Danh Sách Chương

```puml
@startmindmap

skinparam backgroundcolor transparent
!$URL = "http://localhost:65000/book/operating-system/"

* Operating System
** [[$URL/os.html Chung]]

** [[$URL/os-types.html Phân Loại]]
***_ Theo User & Tasking
****_ Single-user
*****_ Single-tasking
*****_ Multi-tasking
****_ Multi-user
***_ Theo Processing Style
****_ Batch Processing
****_ Time-sharing
****_ Real-time OS - RTOS
*****_ Hard Real-time
*****_ Soft Real-time
***_ Theo Device Types
****_ Desktop OS
****_ Mobile OS
****_ Embedded OS
****_ Network OS
***_ Theo Kernel Architecture
****_ Monolithic Kernel
****_ Microkernel
****_ Hybrid Kernel

** [[$URL/os-api.html API]]
*** [[$URL/os-posix.html POSIX]]
*** [[$URL/os-win32.html Win32]]

@endmindmap
```