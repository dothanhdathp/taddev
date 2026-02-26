# Android Android OS

## Android

- __Android__ là hệ điều hành được tạo ra làm hệ điều hành cho điện thoại cảm ứng. Sau này được phổ biến trên nhiều thiết bị cảm ứng đa phương tiện khác nhau như máy tính bảng, ô tô, điện thoại thông minh, thậm chí cả máy tính cá nhân (laptop).
- Hệ điều hành __Android__ rất linh hoạt, nó vốn được thiết kế dựa trên phần khung __*tương thích với nhiều loại phần cứng khác nhau*__, tối giản thời gian phát triển cho lập trình viên tạo các ứng dụng, phần mềm có thể hoạt động với nhiều loại thiết bị phần cứng mà vẫn hoạt động tương tự.
- Điểm nổi bật nhất của __Android__ chính là khả năng tùy cao nhờ việc __*open source*__, Android có thể nói là hệ điều hành dẫn đầu trong khả năng tương thích, sáng tạo, làm được nhiều việc một lúc.
- Bên cạnh những điểm đó, __Android__ cũng có nhiều hạn chế. Đó là về tốc độ xử lý và phản hồi không quá ấn tượng. Cho nên đến tận thời điểm hiện tại, Android chưa hề có một chương trình hiệu năng cao nào ví dụ như các __trò chơi AAA__ - đây là điều xứng đáng để đánh đổi với khả năng tương thích.

## RoadMap

```puml
@startmindmap
skinparam backgroundcolor transparent
!$URL = "/OS/Android"

* [[$URL/android Android]]

** Common
***_ Về Android
***_ [[$URL/android-adb/ ADB]]

** Core
***_ [[$URL/android-core Android Core]]
***_ [[$URL/android-core-architecture Architecture]]
****_ [[$URL/android-core-architecture-hal HAL]]
****_ Kernel
*** System
****_ [[$URL/android-core-architecture-hal SELinux]]

** Dev
*** [[$URL/android-application Application]]
**** 
**** Activity
**** Service
**** Resource
**** JNI

** Example

@endmindmap
```

## What is API

- [API Levels](https://apilevels.com/)

## Reference

- [Android On Wikipedia](https://en.wikipedia.org/wiki/Android_(operating_system))