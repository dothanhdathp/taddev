# Android Proto

- Trong cấu trúc của một file **bugreport.zip** Android, các file có định dạng .proto (thường nằm trong thư mục proto/) đóng vai trò là "nguồn sự thật" (Source of Truth) dạng nhị phân, chứa dữ liệu thô từ các service của hệ thống.
- Có nhiều tệp proto, chúng cho biết ứng dụng nào bị treo, bị **crashed** nằm ở tầng trên của ứng dụng.

## Incident Report

- Trong các tệp của proto có một tệp khá dài mang tên `incident_report.proto`. Tệp này lưu trữ nhiều thông tin nhất.
- Thường các tệp đó sẽ mang CỰC KỲ NHIỀU THÔNG TIN dưới dạng binary, cần công cụ trong AOSP để giải mã.

Sau khi xây dựng thành công chương trình thường sẽ có công cụ tên là `incident_report`, đặt tại thư mục kết xuất đầu ra của _**image**_. Nếu không có gì đặc biệt nó thường nằm tại `out/host/linux-x86/bin/incident_report`

Lúc này bạn cần sử dụng công cụ đó để tái tạo lại các bản proto thành các bản dễ đọc, thân thiện với người dùng hơn. Với dự án tôi từng làm thì hướng dẫn công cụ thế này:

```bash title="command"
incident_report --help
```
```
usage: incident_report -i INPUT [-o OUTPUT]

Pretty-prints an incident report protobuf file.
  -i INPUT    the input file. INPUT may be '-' to use stdin
  -o OUTPUT   the output file. OUTPUT may be '-' or omitted to use stdout


usage: incident_report [-o OUTPUT] [-t|b] [-s SERIAL] [SECTION...]

Take an incident report over adb (which must be in the PATH).
  -b          output the incident report raw protobuf format
  -o OUTPUT   the output file. OUTPUT may be '-' or omitted to use stdout
  -r REASON   human readable description of why the report is taken.
  -s SERIAL   sent to adb to choose which device, instead of $ANDROID_SERIAL
  -t          output the incident report in pretty-printed text format

  SECTION     which bugreport sections to print, either the int code of the
              section in the Incident proto or the field name.  If ommited,
              the report will contain all fields
```

Theo như hướng dẫn đó thì câu lệnh sẽ thế này:

```bash title="command"
incident_report -i incident_report.proto -o incident_report.proto.txt
```