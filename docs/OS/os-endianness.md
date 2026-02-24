# OS Endianness

> Tham khảo: [https://en.wikipedia.org/wiki/Endianness](https://en.wikipedia.org/wiki/Endianness)

## Định Nghĩa

__Endianness__ hay cụ thể hơn là nói đến hai chế độ phổ biến là __big-endian (BE)__ và __little-endian (LE)__. __Endianness__ đề cập đến <u>cách mà máy tính lưu trữ giá trị vào bộ nhớ</u>.

Trước khi bắt đầu cần nói qua rằng, máy tính lưu trữ dữ liệu vào bộ nhớ theo __các khối `byte`__. Ví dụ, thường máy tính không lưu đầy đủ giá trị từng __*bits*__ một vào bộ nhớ mà sẽ thường lưu trữ cả một __tập hợp các byte__, điều đó phụ thuộc vào __*kiến trúc hệ thống*__ - hãy ví dụ với kiến trúc `32-bit` và `64-bit` thông dụng của __*Windows*__ cho dễ hiểu.

Ví dụ với hệ thống `32-bit`, mỗi lần lưu địa chỉ thì hệ điều hành sẽ lưu một khối `4 bytes` = `32 bits`. Theo định nghĩa bây giờ nó gọi là kiểu biến __size_t__ của hệ thống, với các ví dụ cũ họ hay sử dụng đơn vị là một số nguyên __interger__.

Biểu diễn `32 bits` của một số nguyên như sau: `[byte 3][byte 2][byte 1][byte 0]` ví dụ với số nguyên $596,658,984$ có biểu diễn dưới dạng _bit nhị phân_ như là `0010 0011 1001 0000 0100 1011 0010 1000` và:

- `byte 0` = `0010 1000`
- `byte 1` = `0100 1011`
- `byte 2` = `1001 0000`
- `byte 3` = `0010 0011`

## LSb & MSb

__Bit cuối cùng__ của `byte 0` được gọi là __LSb__ hay __least significant bit__ _(bit ít quan trọng nhất)_

__Bit đầu tiên của__ của `byte 3` được gọi là __MSb__ hay __most significant bit__ _(bit quan trọng nhất)_

Cũng theo mô tả đó thì `byte 0` được tính là __*byte ít quan trọng nhất*__ và `byte 3` là __*byte quan trọng nhất*__

```text
[xxxx xxxx] [xxxx xxxx] [xxxx xxxx] [xxxx xxxx]
 ¦                                           ¦
 MSb                                         LSb
```

## Big-Endian, Little-Endian

Theo đó phương pháp của __Big-Endian__ và __Little-Endian__ như sau:

- Hệ thống __Big-Endian__ lưu trữ __*byte quan trọng nhất*__ của một __WORD__ ở địa chỉ bộ nhớ nhỏ nhất và __*byte ít quan trọng nhất*__ ở địa chỉ lớn nhất.
- Hệ thống __Little-Endian__ làm ngược lại, lưu trữ __*byte quan trọng nhất*__ của một __WORD__ ở địa chỉ bộ nhớ lớn nhất và __*byte ít quan trọng nhất*__ ở địa chỉ nhỏ nhất.

<figure markdown="span">
    ![](img/32bit-Endianess.svg.png)
    <figcaption>Sơ đồ minh họa tính chất big-endian so với little-endian</figcaption>
</figure>

## So Sánh

Cả hai phương pháp lưu trữ đều hợp lệ và tồn tại cho đến ngày nay. Lý do là:

- __Little-Endian__ có hiệu năng cao hơn đối với tính toán cấp độ bit và thân thiện với các ngôn ngữ lập trình hệ thống như _Verilog_
- __Big-Endian__ lại có khả năng mạnh mẽ hơn trong các hệ thống mạng, có ưu điểm trong truyền dẫn và tái cấu trúc thông tin.

