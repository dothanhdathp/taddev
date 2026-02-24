# OS

## Map

```puml
@startmindmap
skinparam backgroundcolor transparent
!$URL = "/OS"

* OS
** Chung
***_ [[$URL/os-overview Overview]]
***_ [[$URL/os-endianness Endianness]]
***_ [[$URL/os-file-system File System]]
** Operating System APIs
***_ [[$URL/ POSIX/Win32]]
****_ POSIX
*****_ [[$RUL/os-posix-signal POSIX Signal]]
*****_ [[$RUL/os-posix-signal-sigkill SIGKILL]]
*****_ [[$RUL/os-posix-shell POSIX Shell]]
****_ Win32
*****_ [[$URL/os-win32-windows-exception Windows Exception]]
**_ OS API
*** POSIX
**** Linux/Ubuntu
**** Zorin
*****_ [[$URL/Linux/zorin-install Install Zorin]]
***_ Win32
**** [[$URL/Windows/windows Windows]]
***** Version
******_ XP //(dừng hỗ trợ)//
******_ Vista //(dừng hỗ trợ)//
******_ Windows 7 //(dừng hỗ trợ)//
******_ Windows 8 //(dừng hỗ trợ)//
******_ Windows 10 //(dừng hỗ trợ)//
******_ Windows 11 (hiện tại)
@endmindmap
```

## Table

- **Cấu Trúc Tệp và Hệ Thống**
    - [Endianness](os-endianness.md) là về cách phân bổ các bit bộ nhớ.
    - [File System](os-file-system.md) nói về các hệ thống tệp, hệ thống phân loại tệp trong một số hệ điều hành khác nhau.