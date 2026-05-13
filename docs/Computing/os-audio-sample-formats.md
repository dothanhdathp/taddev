# OS Audio Sample Formats<br>Định Dạng Âm Thanh Tiêu Chuẩn

## Định Nghĩa

Khi chuyển âm thanh tự nhiên sang dạng số hoặc ngược lại bằng kỹ thuật [ADC,DAC](), thì âm thanh kỹ thuật số khi lưu lại phải luôn có định dạng tiêu chuẩn. Các định dạng đó quy định

## PCM Formats

Các định dạng này `S8`, `U8`, `S16_LE`, `S16_BE`, `U16_LE`, `U16_BE`, `S24_LE`, `S24_BE`, `U24_LE`, `U24_BE`, `S32_LE`, `S32_BE`, `U32_LE`, `U32_BE`, `FLOAT_LE`, `FLOAT_BE`, `FLOAT64_LE`, `FLOAT64_BE` là các định dạng mẫu tiêu chuẩn cho PCM.

Cách đặt tên của chúng có ý nghĩa như sau:

- __Prefix (Type)__: Tiền tố được định nghĩa bằng một chữ cái `S` hoặc `U`
    - `S` đại diệu cho mẫu âm thanh được mã hoá dưới dạng số nguyên có dấu __*(Signed Integer)*__
    - `U` đại diệu cho mẫu âm thanh được mã hoá dưới dạng số nguyên không dấu __*(Unsigned Integer)*__
    - `FLOAT` đại diệu cho mẫu âm thanh được mã hoá dưới dạng thập phân __*(floating-point)*__
- __Bit Depth__: Con số theo sau dấu mô tả _bit depth_, hay số _bits_ được sử dụng để mã hoá dữ liệu âm thanh.
- __Suffix ([Endianness](os-endianness.md))__: là một trong hai dạng `_LE` và `_BE`.
    - `_LE`= __Little Endian__ (byte _ít quan trọng_ được xếp đầu tiên)
    - `_BE`= __Big Endian__ (byte _quan trọng_ được xếp nhất đầu tiên)

Ghép các phần với nhau là được ý nghĩa đầy đủ của định dạng mẫu âm thanh.

Thông thường hiện nay phổ biến nhất vẫn là dạng mẫu có dấu _signed_ và _little endian_. Số lượng mẫu mã hoá tuỳ thuộc vào mục đích và hệ thống được sử dụng.

- `S16_LE` : __*16 bits*__ thường phổ biến trong các hệ thống gọi điện, voice-call, cần thiết sự ổn định với tốc độ cao nhất nhưng vẫn đảm bảo chất lượng nghe vừa phải.
- `S24_LE` : __*24 bits*__, nhưng thật sự mỗi mẫu vẫn cần đến bộ chứa 32-bit. Sử dụng 24-bit mã hoá chỉ đơn giản là để giảm tối ưu cho mã hoá và đóng gói. Định dạng này phổ biến trong các tệp mp3 cho chất lượng âm vừa phải, các loại âm thanh như tone, ring, hoặc âm thanh stream cho camera, video, ... qua __*internet*__.
- `S32_BE` : Âm thanh chất lượng cao. Thường được sử dụng trong xử lý nội bộ khi xử lý giải nén hoặc thu âm các tệp âm thanh siêu chất lượng. Chất lượng dạng này là một trong những dạng cực kỳ tốt, thường cần đến các thiết bị cao cấp mới hỗ trợ định dạng này.


## Encoded and Special Formats

Các định danh khác theo sau đây thuộc các dạng riêng biệt, cái mà sẽ phục vụ chủ yếu cho một hệ thống âm thanh nào đó được tự định nghĩa bởi một công ty hoặc tập đoàn nào đó, kết luận nó hình thành một hệ sinh thái độc lập. Bởi tính phổ biến, sẽ có khá nhiều thiết bị đồng ý mở rộng khả năng xử lý cho các dạng dữ liệu âm thanh này.

| Format                | Type           | Description                                                                                                                                                        |
| :-------------------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `MU_LAW (µ-law)`      | Encoding       | Sơ đồ nén kỹ thuật số 8 bit phi tuyến tính, chủ yếu được sử dụng trong điện thoại Bắc Mỹ và Nhật Bản (hệ thống sóng mang T).                                       |
| `A_LAW`               | Encoding       | Sơ đồ nén kỹ thuật số 8 bit phi tuyến tính, tương tự như định luật μ, được sử dụng ở hầu hết các nơi khác trên thế giới (hệ thống sóng mang điện tử).              |
| `IMA_ADPCM`           | Encoding       | Điều chế mã xung vi sai thích ứng đa phương tiện tương tác. Một định dạng nén có độ trễ thấp phổ biến.                                                             |
| `MPEG`                | Encoding       | Đại diện cho âm thanh nén như MP3. Trình điều khiển ALSA thường truyền trực tiếp luồng này tới thiết bị đầu ra HDMI hoặc S/PDIF.                                   |
| `GSM`                 | Encoding       | Hệ thống toàn cầu cho bộ giải mã âm thanh truyền thông di động. Được sử dụng để nén giọng nói.                                                                     |
| `IEC958_SUBFRAME_...` | Encoded Stream | Được sử dụng để truyền các luồng âm thanh kỹ thuật số thô (như AC-3/Dolby Digital hoặc DTS) qua S/PDIF bằng tiêu chuẩn IEC 60958.                                  |
| `G723_24/40`          | Encoding       | Bộ giải mã giọng nói tốc độ bit thấp (G.723) mã hóa giọng nói ở tốc độ 2,4 kbps và 4,0 kbps. Phiên bản _1B cho biết cách triển khai băng thông khác nhau.          |
| `DSD_U8/U16/U32`      | Special PCM    | Truyền trực tiếp kỹ thuật số. Định dạng có độ phân giải cao 1 bit được sử dụng trong SACD, thường được mã hóa để truyền tải trong các vùng chứa 8, 16 hoặc 32 bit. |
| `SPECIAL`             | Special        | Định dạng có mục đích chung thường được sử dụng khi phần cứng có thể xử lý định dạng không được xác định rõ ràng trong bộ tiêu chuẩn.                              |