# Sổ tay GStreamer

!!! danger "Danger"
    Đây là bài viết tổng hợp các kiến thức về GStreamer một cách ngắn gọn. Hãy chắc chắn học hành bài bản rồi mới quay lại đây.

## Các thành phần

- __Elements__ là các thành phần cơ bản nhất của gstreamer
- __pipeline__ là đường ống, bao gồm một hoặc nhiều các khối __Elements__ cơ bản.
- __Pad__ có thể coi như là các ổ cắm, chúng dùng để cho các __Elements__ giao tiếp và kết nối với nhau hoặc truyền dữ liệu giữa hai nguyên tố __*(Elements)*__. Có thể coi các __Pads__
- __Bus__ là đường riêng, cái mà __gstreamer__ mở ra để đưa các thông báo lỗi ra ngoài hoặc nhận các cơ chế điều khiển từ bên ngoài. Bus giúp người dùng có thể can thiệp vào tiến trình của đường ống giữa lúc đường ống đang hoạt động.