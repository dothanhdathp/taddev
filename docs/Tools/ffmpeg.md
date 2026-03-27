# FFmpeg

__FFmpeg__ là công cụ chơi nhạc, chuyển đổi, nén/giải nén các loại dữ liệu đa phương tiện. __FFmpeg__ được phát triển bởi bên thứ ba đồng thời là một `open-source`, khuyến khích mọi người tải về và sử dụng.

__FFmpeg__ cực kỳ mạnh mẽ, với việc có thể tích hợp và thao tác với __hầu hết mọi loại tệp đa phương tiện ở tốc độ tốt__ làm mình không biết phải nói gì với cái công cụ này - quá tuyệt vời. Đây là sản phẩm miễn phí tuyệt vời nhất, hỗ trợ một bộ các bộ giải mã cho các loại tệp tin __đa phương tiện__ từ xưa đến nay.

## Tải Về và Cài Đặt

=== "Windows"
    Windows không có sẵn bản phân phối, bắt buộc phải cài đặt bản build phụ cho Windows. Tìm kiếm phiên bản phát hành trên [đường dẫn này](https://github.com/BtbN/FFmpeg-Builds/releases)
=== "Ubuntu/Linux"
    Ubuntu/Linux hỗ trợ trực tiếp công cụ này.

    ```bash
    sudo apt update
    sudo apt install ffmpeg
    ```

## Bộ Công Cụ

- __ffmpeg__: Công cụ dòng lệnh chính. Nó được sử dụng để chuyển mã, định dạng và thao tác video và âm thanh.
    - _Ví dụ: Chuyển đổi `.mp4` thành `.webm` hoặc trích xuất âm thanh từ tệp video._
- __ffprobe__: Một máy phân tích phương tiện truyền thông. Nó được sử dụng để xem siêu dữ liệu và chi tiết bên trong của tệp phương tiện (tốc độ bit, độ phân giải, codec, v.v.).
    - _Ví dụ: Kiểm tra xem tệp video có sử dụng codec **H.264** hoặc **H.265** hay không._
- __ffplay__: Trình phát đa phương tiện di động, đơn giản dựa trên thư viện SDL và FFmpeg. Nó thường được sử dụng để kiểm tra nhanh hoặc xem trước các bộ lọc.

## Công Dụng

### Chơi nhạc

```bash
# Play, no exit when done
ffplay {file}

# Play, auto exit when done
ffplay -autoexit {file}
```

- `-autoexit`: Tự động thoát sau khi tiến trình chơi nhạc kết thúc.

### Convert

#### Same Type

```bash
ffmpeg -i {file-input} {file-output}

# Example
ffmpeg -i file.wav file.mp3
```

#### Diff Type

Khi hai tệp không có cùng định dạng, cần có một số sự bổ sung qua câu lệnh để bổ sung thông tin chuyển đổi.

##### Video To Audio

Thay `v-ext`, `a-ext` lần lượt là đuôi phần mở rộng của các loại tệp video và audio. Ví dụ như là `.mp4`, `.avi` ... cho **Video**. Và  `.mp3`, `.flac` ... cho **Audio**

```bash
ffmpeg -i {input-file}.{v-ext} -vn -c:a {a-ext} {output-file}.{a-ext}

# Example
ffmpeg -i input.mp4 -vn -c:a mp3 output.mp3
ffmpeg -i input.mp4 -vn -c:a flac output.flac
ffmpeg -i input.avi -vn -c:a mp3 output.mp3
ffmpeg -i input.avi -vn -c:a flac output.flac
```

##### Raw To Audio

- `raw` là định dạng cho loại **dữ liệu thô** _(dữ liệu không nén)_. Dữ liệu thô thường được tìm thấy nhiều nhất trong các tệp pcm hoặc trong các tệp dữ liệu không nén, ví dụ như way.
- Dữ liệu thô chính là phần dữ liệu quan trọng nhất của các loại dữ liệu. Chính nó là phần được sử dụng để hoạt động cho các thiết bị khác.
- Phần lớn các tệp media đểu được bổ sung các phần mô tả được gọi là metadata chứa các thứ như hình ảnh, ca sĩ, nhạc sĩ... Nhưng quan trọng nhất là phần mô tả về cấu hình để có thể phát lại tệp dữ liệu.

###### Wav to PCM

Chuyển đổi audio 16-bit thành raw

```bash
ffmpeg -i input.ext -f s16le -acodec pcm_s16le output.ext
```

###### PCM to Wav

- Ví dụ này chuyển đổi một tệp dữ liệu gốc của âm thanh thành tệp _**wav (định dạng do Microsoft phát hành)**_
- Dữ liệu pcm có thể dump ra từ pcm trên các hệ điều hành dạng Linux

```bash
ffmpeg -f s16le -ar 44.1k -ac 2 -i file.pcm file.wav
```

- `-f s16le`    : signed 16-bit little endian samples
- `-ar 44.1k`   : sample rate 44.1kHz
- `-ac 2`       : 2 channels (stereo)
- `-i file.pcm` : input file
- `file.wav`    : output file