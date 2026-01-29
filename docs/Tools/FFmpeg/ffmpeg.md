# FFmpeg

__FFmpeg__ là công cụ chơi nhạc, chuyển đổi, nén/giải nén các loại dữ liệu đa phương tiện. __FFmpeg__ được phát triển bởi bên thứ ba đồng thời là một `open-source`, khuyến khích mọi người tải về và sử dụng.

__FFmpeg__ cực kỳ mạnh mẽ, với việc có thể tích hợp và thao tác với __hầu hết mọi loại tệp đa phương tiện ở tốc độ tốt__ làm mình không biết phải nói gì với cái công cụ này - quá tuyệt vời. Đây là sản phẩm miễn phí tuyệt vời nhất, hỗ trợ một bộ các bộ giải mã cho các loại tệp tin __đa phương tiện__ từ xưa đến nay.

## Tải Về và Cài Đặt

=== "Ubuntu/Linux"
    Ubuntu/Linux hỗ trợ trực tiếp công cụ này.

    ```bash
    sudo apt update
    sudo apt install ffmpeg
    ```

## Công Cụ

- __ffmpeg__: Công cụ dòng lệnh chính. Nó được sử dụng để chuyển mã, định dạng và thao tác video và âm thanh.
    - _Ví dụ: Chuyển đổi `.mp4` thành `.webm` hoặc trích xuất âm thanh từ tệp video._
- __ffprobe__: Một máy phân tích phương tiện truyền thông. Nó được sử dụng để xem siêu dữ liệu và chi tiết bên trong của tệp phương tiện (tốc độ bit, độ phân giải, codec, v.v.).
    - _Ví dụ: Kiểm tra xem tệp video có sử dụng codec __H.264__ hoặc __H.265__ hay không._
- __ffplay__: Trình phát đa phương tiện di động, đơn giản dựa trên thư viện SDL và FFmpeg. Nó thường được sử dụng để kiểm tra nhanh hoặc xem trước các bộ lọc.

## ffplay

__ffplay__ để chơi nhạc. Sử dụng dòng lệnh sau để phát một bài trực tuyến.

```bash
ffplay {file}
```

Sau khi bài nhạc kết thúc, chương trình sẽ không tự động thoát, để kết thúc cần cờ `-autoexit`

```bash
ffplay -autoexit {file}
```

## ffmpeg

__ffmpeg__ để chuyển đổi dữ liệu tệp âm thanh nhị phân thành các định dạng khác dựa trên _codec.

### Cùng Định Dạng

Cùng Định Dạng là khi chuyển đổi các tệp đa phương tiện có cùng thể ví dụ như các tệp _âm thanh_ với các tệp _video_. Hầu hết ffmpeg sẽ tự lựa chọn _codex_ nếu không có yêu cầu về _codex_. Chỉ cần điền đúng tên miền mở rộng _(dạng như **mp3**, **aac**, **m4a**,..)_ là được. __ffmpeg__ sẽ tự lựa chọn codex chuyển đổi.

=== "Audio"
    ```bash
    ffmpeg -i {file-input} {file-output}
    ```
    Ví dụ
    ```bash
    ffmpeg -i file.wav file.mp3
    ```
=== "Video"
    ```text

    ```

### Chuyển đổi dữ liệu pcm thành wav

Chuyển đổi tệp tin từ loại này sang loại khác. Trung bình cách này khác với cách sử dụng tệp pcm _(raw data)_ vì bản chất nó đã có đầy đủ các thông số của dữ liệu nằm trong tên tệp rồi. Miễn là các tệp có đầy đủ thông tin thì sự chuyển đổi được diễn ra bình thường.

```bash
ffmpeg -f s16le -ar 44.1k -ac 2 -i file.pcm file.wav
```
- `-f s16le`    : signed 16-bit little endian samples
- `-ar 44.1k`   : sample rate 44.1kHz
- `-ac 2`       : 2 channels (stereo)
- `-i file.pcm` : input file
- `file.wav`    : output file

### Chuyển đổi wav file thành raw data

```bash
ffmpeg -i input.flv -f s16le -acodec pcm_s16le output.raw
```