# Android Applications

## Yêu cầu

Tầng ứng dụng hầu hết sẽ được viết bằng hai ngôn ngữ chính, là __Java__ và __Kotlints__.

## Phân Loại

Như trong bài [Architecture](/OS/Android/andeeroid-core-architecture) Tầng ứng dụng của Android chia làm ba loại là:

1. __Android Apps__
1. __Privileged App__
1. __Device Manufacturer App__

Về cơ bản cách viết của ba tầng này không quá khác biệt, chỉ có khác nhau về quyền truy cập và phân bổ.

### Android Apps

Các ứng dụng __Android Apps__ thông thường sẽ chỉ dùng ứng dụng cơ bản, sử dụng một __*key chung*__ hoặc không khóa. Điều này hạn chế quyền truy cập vào các thành phần hệ thống cơ bản.

Khi các ứng dụng này muốn sử dụng một quyền gì đều yêu cầu phải có sự đồng ý của người dùng, ví dụ như quyền sử truy cập vào các tệp hình ảnh, âm thanh, ... quyền sử dụng __Bluetooth__, __Wifi__, ...

Nhìn chung mấu chốt các ứng dụng này chỉ dùng các Android API cơ bản, dùng để _giấu_ các quy trình phần dưới.

### Privileged App

Các ứng dụng __Privileged App__ thông thường sẽ chỉ dùng ứng dụng cơ bản, ứng dụng độc quyền của thiết bị. Các ứng dụng này thường được hưỡng một số quyền lợi riêng như:

- Luôn tồn tại và có sẵn.
- Một số phần mềm sẽ có sẵn quyền truy cập, sử dụng các tài nguyên cá nhân.
- Tương tác với nhau để đảm bảo thiết bị hoạt động ổn định, đem lại một số trải nghiệm thú vị.

Ví dụ như một số ứng dụng độc quyền sẽ sử dụng một số API độc quyền để thao tác phần cứng riêng của thiết bị ví dụ như cảm biến điều hòa, quạt, ... nằm trên các hệ thống xe hơi. Hoặc một số tùy biến bao phủ lên trên __SystemUI__ phục vụ việc đổi theme, thay đổi một số hành vi nhỏ trên giao diện đem lại trải nghiệm khác.

### Device Manufacturer App
