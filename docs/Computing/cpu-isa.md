# CPU Instruction Set Architecture

## Các Kiến Trúc

| Tên Kiến Trúc           | Hệ Bit | Thông Tin                                                              |
| :---------------------- | :----- | :--------------------------------------------------------------------- |
| **`x86`/`i386`/`i686`** | 32-bit | Hiện nay đang <u>dần bị khai tử</u>, chỉ còn trên các máy tính rất cũ. |
| **`x86_64`/`amd64`**    | 64-bit | Hiện nay trên hầu hết các hệ máy                                       |
| **`arm`/`armv7`**       | 32-bit | Có xuất hiện trên một số thiết bị cũ.                                  |
| **`aarch64`/`arm64`**   | 64-bit | Tiêu chuẩn hiện nay trên các thiết bị Android và Apple M1/M2/M3/       |
| `RISC-V`                |        | Mới. Được kỳ vọng cao                                                  |
| `MIPS`                  |        | Trên các router đời cũ                                                 |
| `PowerPC`               |        | Trên các máy Mac cũ                                                    |


## Tham Khảo

!!! abstract "Computer Organization and Design: The Hardware/Software Interface"
    - Tác Giả: _Patterson & Hennessy_
    - Cuốn sách quan trọng nhất. Nên chọn phiên bản RISC-V Edition hoặc ARM Edition để học về các tập lệnh hiện đại thay vì bản x86 cũ.
!!! abstract "Computer Architecture: A Quantitative Approach"
    - Tác Giả: _Hennessy & Patterson_
    - Dành cho mức độ nâng cao hơn, đi sâu vào hiệu suất, tính toán song song và tối ưu hóa ISA.