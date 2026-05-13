# Win MAS<br>Microsoft Activation Scripts

Cái công cụ này cũng chẳng cũ, rất rất nhiều người biết nhưng ít người nói. Cái này crack bằng cách sử dụng một số Key Active Windows của một số công ty lớn.

Về cơ bản đó là __Microsoft__ có một cơ chế đơn giản là có một gói vĩnh cửu dành cho một số công ty. Nơi mà họ sẽ được hưởng ưu đãi kích hoạt theo thời hạn bằng một __*Key*__ chung, tất cả các máy có key đó sẽ đều được kích hoạt. Key đó được tính theo thời gian và công ty đóng tiền hàng tháng, hoặc năm. Nói chung là bao nhiêu máy cũng được cả.

- [Trang chủ](https://massgrave.dev/)
- [Github](https://github.com/massgravel/Microsoft-Activation-Scripts)

## How

### Cách 1 Chạy command

Ở màn __PơwerShell__ gọi lệnh sau:

=== "Win 8/10/11"
	```bash
	irm https://get.activated.win | iex
	```
	
	Nếu không được thì có khả năng là máy tính chưa được cập nhật. Có thể gọi lệnh sau:

	```bash
	iex (curl.exe -s --doh-url https://1.1.1.1/dns-query https://get.activated.win | Out-String)
	```
=== "Windows 7"
	```bash
	iex ((New-Object Net.WebClient).DownloadString('https://get.activated.win'))
	```

### Cách 2 Cách Truyền Thống

1. Tải xuống tập lệnh: [MAS_AIO.cmd](https://massgrave.dev/#:~:text=Download%20the%20script,That%27s%20all.) hoặc [bản ZIP](https://massgrave.dev/#:~:text=Download%20the%20script,That%27s%20all.).
1. Chạy file có tên [MAS_AIO.cmd](https://massgrave.dev/#:~:text=Download%20the%20script,That%27s%20all.).
1. Bạn sẽ thấy các tùy chọn kích hoạt. Làm theo hướng dẫn trên màn hình.
1. Thế thôi.

## Download

- [Download Windows](https://gravesoft.dev/download_windows)
- [Office C2R Installers](https://gravesoft.dev/office_c2r_links)
- [Office C2R Custom Install](https://gravesoft.dev/office_c2r_custom)