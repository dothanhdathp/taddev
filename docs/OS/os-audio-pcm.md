# OS Thuật ngữ và khái niệm của PCM

Để sử dụng thiết bị PCM, bạn cần phải làm quen với một số khái niệm và thuật ngữ. Thuật ngữ và khái niệm của PCM tôi lấy ở [link này](https://larsimmisch.github.io/pyalsaaudio/terminology.html)

## Chủ đề chính
### Sample

Âm thanh PCM, dù là đầu vào hay đầu ra, đều bao gồm các _mẫu_ (__Sample__). <mark>Một mẫu duy nhất biểu diễn biên độ của một kênh âm thanh tại một thời điểm nhất định.</mark> Rất nhiều mẫu riêng lẻ là cần thiết để biểu diễn âm thanh thực tế; đối với âm thanh CD, 44100 mẫu được lấy mỗi giây.

Các mẫu có thể có nhiều kích cỡ khác nhau, từ độ chính xác 8 bit đến 64 bit. <mark>Định dạng cụ thể của mỗi mẫu cũng có thể khác nhau</mark> - chúng có thể là số nguyên byte big endian, số nguyên byte little endian hoặc số dấu phẩy động.

Về mặt âm nhạc, _kích thước mẫu quyết định phạm vi động_ __(the sample size determines the dynamic range)__. Phạm vi động là sự khác biệt giữa tín hiệu nhỏ nhất và lớn nhất có thể tái tạo được.

### Frame

Một khung bao gồm chính xác <mark>một mẫu cho mỗi kênh</mark>. Nếu chỉ có một kênh (âm thanh Mono) thì khung chỉ đơn giản là một mẫu duy nhất. Nếu âm thanh là âm thanh nổi, mỗi khung bao gồm hai mẫu, v.v.

### Frame size

Đây là <mark>kích thước tính bằng byte của mỗi khung</mark>. Kích thước này có thể thay đổi rất nhiều: nếu mỗi mẫu là 8 bit và chúng ta đang xử lý âm thanh đơn sắc, kích thước khung là một byte. Đối với âm thanh sáu kênh với mẫu dấu phẩy động 64 bit, kích thước khung là 48 byte.

### Rate

Âm thanh PCM bao gồm một luồng các khung âm thanh. Tốc độ âm thanh kiểm soát tần suất khung hiện tại được thay thế. Ví dụ, tốc độ 8000 Hz có nghĩa là một khung mới được phát hoặc thu 8000 lần mỗi giây.

### Data rate

Đây là số byte phải được tiêu thụ hoặc cung cấp mỗi giây ở một tốc độ và kích thước khung hình nhất định.
Âm thanh đơn sắc 8000 Hz với mẫu 8 bit (1 byte) có tốc độ dữ liệu là 8000 * 1 * 1 = 8 kb/giây hoặc 64kbit/giây. Tốc độ này thường được sử dụng cho điện thoại.
Ở đầu kia của thang đo, âm thanh 96000 Hz, 6 kênh với mẫu 64 bit (8 byte) có tốc độ dữ liệu là 96000 * 6 * 8 = 4608 kb/giây (gần 5 MB dữ liệu âm thanh mỗi giây).
Nếu không đáp ứng được yêu cầu về tốc độ dữ liệu, sẽ xảy ra tình trạng tràn dữ liệu (khi thu thập) hoặc thiếu dữ liệu (khi phát lại); thuật ngữ `xrun` được sử dụng để chỉ cả hai sự kiện.

### Period
CPU xử lý dữ liệu mẫu theo từng khối khung, được gọi là chu kỳ (cũng được một số hệ thống gọi là đoạn). Bộ đệm mẫu của nhân hệ điều hành phải chứa ít nhất hai chu kỳ (tại bất kỳ thời điểm nào, một chu kỳ được xử lý bởi phần cứng âm thanh và một chu kỳ được xử lý bởi CPU).

<mark>Việc hoàn thành một chu kỳ sẽ kích hoạt ngắt CPU, gây ra chi phí xử lý và chuyển đổi ngữ cảnh.</mark> Do đó, kích thước chu kỳ nhỏ hơn sẽ gây ra mức sử dụng tài nguyên CPU cao hơn ở một tốc độ dữ liệu nhất định.

Kích thước bộ đệm lớn hơn cải thiện khả năng phục hồi của hệ thống đối với xrun. Bộ đệm được chia thành nhiều chu kỳ nhỏ hơn cũng làm được điều đó, vì nó cho phép bộ đệm được xả/bổ sung sớm hơn.

Mặt khác, kích thước bộ đệm lớn hơn cũng làm tăng độ trễ phát lại, tức là thời gian cần thiết để một khung hình được ứng dụng gửi đi cho đến khi thực sự có thể nghe được.

Tương tự như vậy, kích thước chu kỳ lớn hơn sẽ làm tăng độ trễ chụp.

Sự cân bằng giữa độ trễ, khả năng phục hồi `xrun` và mức sử dụng tài nguyên phải được thực hiện tùy thuộc vào ứng dụng.

### Period size
Đây là <mark>kích thước của mỗi chu kỳ tính theo khung</mark>. Không phải byte, mà là khung! Trong chu kỳ [alsaaudio](https://larsimmisch.github.io/pyalsaaudio/libalsaaudio.html#module-alsaaudio), kích thước được thiết lập trực tiếp, do đó, điều quan trọng là phải hiểu ý nghĩa của con số này. Nếu kích thước chu kỳ được cấu hình thành ví dụ 32, mỗi lần ghi phải chứa chính xác 32 khung dữ liệu âm thanh và mỗi lần đọc sẽ trả về 32 khung dữ liệu hoặc không có gì cả.

### Sample size
Mỗi mẫu chiếm không gian `physical_bits` trong space. `nominal_bits` cho biết có bao nhiêu bit ít quan trọng nhất được sử dụng. Đây là độ sâu bit trong tên định dạng và đôi khi được gọi là bit mẫu hoặc chiều rộng định dạng .`significant_bits` cho biết có bao nhiêu bit quan trọng nhất của `noun_bits` được mẫu sử dụng. Điều này có thể được coi là độ phân giải mẫu . Điều này được hình dung như sau:


```txt
MSB |00000000 XXXXXXXX XXXXXXXX 00000000| LSB
              |--significant--|
              |---------nominal---------|
    |-------------physical--------------|
```
## Ngoài ra

### Bit Depth

Trong `WAV`, __Bit Depth__ là số lượng `bits` được sử dụng để trình diễn biên độ của tần số trong mỗi __audio sample__.

## Tham Khảo

- [Audio Sample Formats - Định Dạng Âm Thanh Tiêu Chuẩn](os-audio-sample-formats.md)