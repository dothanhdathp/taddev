# \[Win\] Password

## Forget Password

Cách này được dùng khi mà quên mất mật khẩu của máy tính.

1. Tại màn hình mở khóa, giữ __*Shitf*__ và chọn __*Reset*__ máy tính.
1. Máy sẻ khởi động lại ở __*Recovery Mode*__
1. Sau đó chọn mục __*Troubleshoots*__ -> __*Advanced option*__ -> __*Commad Prompt*__
1. Nhập các lệnh sau:
	- Vào thư mục __system32__
		```bash
		c:
		cd Windows\System32
		```
	- Chạy lệnh sau. Ok lệnh `ren` để đổi tên. Mục đích là chạy __CMD__ bằng __Accessibility__
		```bash
		ren utilman.exe utilman1.exe
		ren cmd.exe utilman.exe
		exit
		```
1. Trở lại và chọn __Continue__ lúc này màn __Accessibility__ và thấy nó mở lên màn __cmd__. Chạy lệnh sau để sửa đổi mật khẩu:
	```bash
	control userpasswords2
	```
	Nó sẻ mở lên pop-up điểu khiển __User Accounts__
1. Chọn tài khoản và ấn __Reset Password...__ để đổi mật khẩu.

!!! danger "Danger"
	Xong việc nhớ trở lại `C:\Windows\System32` để đổi lại tên nhé.