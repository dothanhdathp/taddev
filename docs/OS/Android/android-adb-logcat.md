# \[Android\] ADB Logcat

__logcat__ là lệnh được sử dụng để đọc nhật ký android từ adb. Ở chế độ mặc định, __*logcat*__ trả về nhật ký ở dạng _text_.

- `adb logcat` gõ command thì sẽ trả về nhật ký, đọc trên thiết bị kết nối __adb__
- Ngoài ra có thể sử dụng `adb shell` để vào __*shell*__ của thiết bị và gõ `adb logcat`, lúc này thì việc đọc và trả về log được sẽ được trình diễn trên thiết bị đích.

## Level

Dùng chữ cái để thay đổi cấp độ in log

- `V`: _Verbose_ (mức độ ưu tiên thấp nhất)
- `D`: _Debug_
- `I`: _Info_
- `W`: _Warning_
- `E`: _Error_
- `F`: _Fatal_
- `S`: _Silent_ (mức độ ưu tiên cao nhất, khi đó không có nội dung nào được in lên màn hình)

Để cân đối mức độ log sẽ dùng lệnh sau

```text
logcat *:{level}
```

Thay _{level}_ bằng các chữ cái bên trên.

## Select Class Log

`logcat` cũng cho phép tương tác để lựa chọn một số loại log sẽ được hiển thị bằng cờ `-b`, ví dụ

```text
logcat -b 
```

## Format

Với cờ `-v`, điều khiển cấu trúc đầu ra được in ra màn hình tùy theo nhu cầu sử dụng.

- __brief__: Hiển thị mức độ ưu tiên, thẻ và PID của quá trình đưa ra thông báo.
- __long__: Hiển thị tất cả các trường siêu dữ liệu và phân tách các tin nhắn bằng dòng trống.
- __process__: Chỉ hiển thị PID.
- __raw__: Hiển thị thông báo nhật ký thô không có trường siêu dữ liệu nào khác.
- __tag__: Chỉ hiển thị mức độ ưu tiên và thẻ.
- __thread__: Định dạng cũ hiển thị mức độ ưu tiên, PID và TID của luồng phát ra thông báo.
- `threadtime` _(mặc định)_: Hiển thị ngày, thời gian gọi, mức độ ưu tiên, thẻ, PID và TID của luồng phát hànhmessage.
- __time__: Hiển thị ngày, thời gian gọi, mức độ ưu tiên, thẻ và PID của quá trình đưa ra thông báo.

...

Nhưng nói chung cái này cũng không quá là cần thiết trừ các trường hợp rất đặc biệt. Thế nên sẽ để lại sau.

## Alternative log buffers

> Bộ đệm nhật ký thay thế

Hệ thống ghi nhật ký Android giữ nhiều vùng đệm tròn cho thông điệp tường trình và không phải tất cả thông điệp tường trình đều được gửi đến bộ đệm vòng tròn mặc định. Để xem thông báo nhật ký bổ sung, hãy chạy lệnh logcat với tùy chọn `-b` để yêu cầu xem bộ đệm tròn thay thế. Bạn có thể xem bất kỳ bộ đệm thay thế nào sau đây:

- `radio`: Xem bộ đệm chứa các tin nhắn liên quan đến radio/điện thoại.
- `events`: Xem các thông báo bộ đệm sự kiện hệ thống nhị phân được giải thích.
- `main`: Xem bộ đệm nhật ký chính (mặc định), không chứa thông báo nhật ký hệ thống và sự cố.
- `system`: Xem bộ đệm nhật ký hệ thống (mặc định).
- `crash`: Xem bộ đệm nhật ký sự cố (mặc định).
- `all`: Xem tất cả các bộ đệm.
- `default`: Báo cáo bộ `main`, `system`, và `crash`.

Đây là tính năng cực kỳ thú vị tại sao lại không biết nhỉ. Đặc biệt trong các trường hợp chỉ cần log tại một __module__ nào đó vả bỏ qua các module xung quanh thì đây chính xác là tính năng cực kỳ tốt.

## Clean

Có hai cách xóa dữ liệu trong log bằng lệnh:

```text
adb logcat -c
```

Lệnh này dùng để xóa toàn bộ log cả trong buffer dự trữ của thiết bị _(dành khi bạn để bộ nhớ cho nhật ký nhiều)_

```text
adb logcat -b all -c
```