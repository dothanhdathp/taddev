# \[Linux\] Install Zorin

## Tải về

Lên trang chủ của Zorin rồi đăng ký một tài khoản. Sau khi đăng ký và đồng ý các thỏa thuận thì sẽ nhận được bản tải về qua mail.

Trong mail có chứa một đường dẫn để tải về. Mình không biết để làm gì nhưng chắc có lẽ để giảm thiểu băng thông yêu cầu tải về tử hệ thống.

Vì thế, sau khi có được bản `img` thì mình đã upload lại lên đây:
[Google Drive](https://drive.google.com/drive/folders/1Yzkyzxjeaqn-l_OEA0PHAGIO3u6N6eCH)

Sau đó có một số cài đặt quan trọng cần để ý như sau:

- Cài đặt bộ gõ tiếng Việt [iBamboo](linux-tools-ibamboo.md)

## Bộ gõ Tiếng Việt

??? note "Giải thích"
    - Thêm kho lưu trữ PPA của Bamboo Engine
    - Cập nhật hệ thống
    - Tải về ibus-bamboo
    - Khởi động lại ibus để hệ thống nhận diện

```bash
sudo add-apt-repository ppa:bamboo-engine/ibus-bamboo
sudo apt-get update
sudo apt-get install ibus ibus-bamboo --install-recommends
ibus restart
```

## Clipboard Indicator

Cái này tương tự như bộ lưu trữ __Clipboard__ trên Windows. Giúp lưu trữ được nhiều các bộ tạm hơn phục vụ đa mục đích.

```bash
sudo apt install gnome-tweaks chrome-gnome-shell
```

Sau khi cài đặt xong có thể vào trang này:

[https://extensions.gnome.org/extension/779/clipboard-indicator/](https://extensions.gnome.org/extension/779/clipboard-indicator/)

Lúc này sẽ có nút __Install__ bên cạnh. Nhấn vào nó để tải về công cụ.

Sau đó nhớ chọn vào góc dưới và đổi lại `hot-key`. Tốt nhất thì là nên xóa hết để tiết kiệm phân bổ các phím tắt chỉ để lại mở của nút `super+v` để mở lại bảng `hot-key` là được rồi.