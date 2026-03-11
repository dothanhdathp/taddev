# Audio

Âm thanh là hướng nghiên cứu về âm thanh, dữ liệu âm thanh, nén âm thanh và các thứ liên quan.

## Các Khái Niệm

- [Sample Rate (Tần số lấy mẫu)](#sample-rate)
- [Bit Depth (Độ sâu bit)](#bit-depth)

### Sample Rate

**Sample Rate (Hz)**: Cho biết <mark>có bao nhiêu mẫu âm thanh được ghi lại trong một giây</mark>. Theo [định luật Nyquist–Shannon](https://vi.wikipedia.org/wiki/%C4%90%E1%BB%8Bnh_l%C3%BD_l%E1%BA%A5y_m%E1%BA%ABu_Nyquist%E2%80%93Shannon), cần lấy mẫu ít nhất gấp đôi tần số cao nhất muốn ghi lại. Tai người nghe đến **20kHz**, nên lấy mẫu ở tần số **44.1kHz** là ít nhất. 

Các tần số phổ biến là:

- `16kHz`: Cho radio, điện thoại ở các hệ thống cổ.
- `44.1kHz`: Thường cho các nhạc, phim.
- `48kHz`: Trên các âm thanh chất lượng cao.
- `96kHz`: Chuẩn âm thanh chất lượng cực cao như **Hi-res**

### Bit Depth

Quyết định độ phân giải của mỗi mẫu biên độ. **Bit depth** càng cao thì [Dynamic Range](#dynamic-range) càng rộng và [Quantization Noise]() càng thấp.

Các độ phân giải phổ biến: `16-bit`, `24-bit`, `32-bit (float)`.

### Bitrate

**Tốc độ bit**. Đo bằng _**kbps (kilobits per second)**_. Con số này cho biết lượng dữ liệu được xử lý trong một giây. Công thức:

$$
Bitrate = SampleRate \times BitDepth \times Channels
$$

Trong đó, [Channels](#channels) là số kênh âm thanh.

### Channels

Số kênh âm thanh cho biết số kênh (luồng âm thanh) đồng thời mà gói dữ liệu âm thanh đang mang. Càng nhiều kênh càng đem lại khả năng tái tạo âm thanh tốt hơn. Ví dụ như trong các loa thường là loa đơn, âm thanh có một kênh gọi là **Mono**. Khi đó âm thanh sẽ được phát ra ở một đầu loa duy nhất. Trong tai nghe thường là âm thanh **Stereo** với hai kênh. Đây cũng là định dạng phổ biến nhất. 

### Tra Cứu

- **Dynamic Range**: Dải động, sự khác biệt giữa âm thanh nhỏ nhất và lớn nhất
- **Quantization Noise**: Nhiễu lượng tử
- thuật toán Dithering

## Các Loại Âm Thanh

| Định dạng     | Compression  | Miễn Phí | Mô Tả                                                                                                 |
| :------------ | :----------: | :------: | :---------------------------------------------------------------------------------------------------- |
| WAV           | Uncompressed | &check;  | Âm thanh không nén, dữ liệu thô được phát triển từ **Windows**                                        |
| AIFF          | Uncompressed |          | Âm thanh không nén, dữ liệu thô và của Apple                                                          |
| FLAC          |   Lossless   | &check;  | Hiệu suất nén tốt, hỗ trợ metadata mạnh mẽ.                                                           |
| ALAC          |   Lossless   |          | Apple Lossless Audio Codec. Đã được Apple mở mã nguồn (Open Source).                                  |
| APE           |   Lossless   |          | Monkey's Audio, nén rất sâu nhưng tốn CPU để giải mã. Ít phổ biến.                                    |
| MP3           |    Lossy     | &check;  | Phổ biến nhất, cấu trúc dựa trên các Frame độc lập.                                                   |
| AAC           |    Lossy     |          | Kế thừa MP3, hiệu suất tốt hơn ở bitrate thấp. Vẫn còn bản quyền (thường đi kèm với chuẩn MP4/H.264). |
| Opus          |    Lossy     | &check;  | Độ trễ cực thấp, linh hoạt từ 6kbps đến 512kbps. Lụa chọn tốt nhất cho VoIP và Streamming.            |
| Vorbis (.ogg) |    Lossy     | &check;  | Có nhiều điểm tương đồng với MP3. Chỉ là MP3 phổ biến hơn.                                            |
