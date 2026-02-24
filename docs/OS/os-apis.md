# POSIX & Win32

> Thế giới có rất nhiều hệ điều hành, nhưng chúng chỉ xoay quanh hai tiêu chuẩn là chuẩn __POSIX__ và __Win32__.

## Tiêu Chuẩn Của Hệ Điều Hành

### POSIX

__POSIX__ _(Portable Operating System Interface)_ là bộ tiêu chuẩn được thiết lập bởi __IEEE__ nhằm chuẩn hóa hệ thống hệ điều hành cho các hệ điều hành kiểu __*UNIX-like*__.

Theo chuẩn __POSIX__, hệ điều hành này coi mọi thứ là dạng tệp _(file)_. Các hàm tiêu chuẩn để tương tác với hệ điều hành bao gồm `open()`, `fork()`, `read()`, `write()`, và thư viện đa luồng `pthreads`,... sẽ tương tác với thành phần hệ thống như các tệp.

Ngoài ra chuẩn này cũng yêu cầu một số lệnh chung của hệ thống sẽ dùng chung một vài kiến trúc như `grep`, `sed`, `ls`, `awk`, ...

Các tệp được phân tách bởi dấu `/`

Hai hệ điều hành nổi tiếng nhất theo tiêu chuẩn này là __Linux__ và __macOS__. Linux có rất nhiều biến thể như __BSD__, __Ubuntu__, __Zorin__, ...

Lợi ích của __POSIX__ chính là: Nếu phần mềm bạn viết tuân thủ tiêu chuẩn __POSIX__, và hệ điều hành tuân thủ __POSIX__ thì chúng hoạt động được với nhau. Tiêu chuẩn này tránh cho việc phát triển phần mềm lại cho các hệ điều hành khác nhau, đấy là lý do hầu hết các ứng dụng nếu có thể chạy trên __Linux__ thì nó cũng có thể chạy trên __macOS__

### Win32

__Win32__ theo một đường lối khác hẳn. Win32 theo triết lý __Object__ và __Handles__. Kiến trúc này không phải POSIX thế nên nó sẽ không thể hoạt động. Thêm nữa do kiến trúc khác, các ngữ cảnh thực thi cũng khác nhau rất nhiều, thế nên một tác vụ nếu chạy tốt trên POSIX nó cũng không cho ra được hiệu năng tốt trên __Win32__.

## Driver

Với các thành phần phần cứng, hai hệ tiêu chuẩn cũng mang những triết lý không tương đương. Với hệ thống POSIX có tính năng bảo mật mạnh mẽ khiến cho việc chiếm quyền sử dụng các thành phần phần cứng từ `root` là gần như bất khả thi. Điều này hạn chế đáng kể các ứng dụng từ bên thứ ba có thể thao tác và chiến quyền điều khiển với bàn phím, chuột để thực thi các mã độc xấu.

Bù lại thì __Win32__ cung cấp tốt cho chế độ __*Plug and Play*__, nó khiến các lệnh từ phím và chuột được tăng mạnh, đem lại trải nghiệm tốt cho các trò chơi tốc độ cao.

Các phần sụn hỗ trợ cho màn hình như __DirectX__ cũng là một thành phần khác mang lại chiến thắng này.

## Đối Với Lập Trình Viên

Đối với các lập trình viên, điều này càng thú vị hơn với __POSIX__ và __Win32__.

### GNU cho Linux

Thường chúng ta học C/C++ đều được giới thiệu trình biên dịch GNU, bởi vì nó miễn phí. Điểm đáng buồn là trình biên dịch này là cho __POSIX__ chứ không phải cho __Win32__. Các nền của của hệ điều hành như quản lý các tệp hay quản lý các thiết bị đầu vào, đầu ra như GPIO của USB, ETH Port, ... đều được viết bằng __C__ như __Linus Torvalds__ từng viết và xây dựng lên hệ điều hành Linux.

Chính bởi vì điều đó nên việc biên dịch __C/C++__ trên __Windows__ lại khó khăn đến như vậy, đồng thời mình luôn cảm thấy có độ trễ nhẹ trong khâu xử lý là bình thường.

### Nếu là Win32, xin hãy dùng C++ MSVC

Đặc biệt với các hệ điều hành của Windows sử dụng hệ thống __Win32__ thì nên dùng __C++__ trên công cụ biên dịch __MSVC__. Điều này là vì những lập trình viên hệ thống của Windows đã rất cố gắng để viết tất cả các lệnh trong thư viện sẽ thực thi gần nhất với mã máy nên nó sẽ có hiệu năng cơ bản cao nhất.

Trên hệ điều hành __Windows__, quãng thời gian phát triển dài đã biến ngôn ngữ C++ trở thành ngôn ngữ gần với mã máy nhất (hơn cả C). Điều này khá là dễ hiểu khi mà thực sự nếu bạn có thể nhúng trực tiếp các mã máy vào trong một thư viện thì phần còn lại của ngôn ngữ chỉ là công cụ.

Việc tại sao POSIX không làm điều đó là vì __Linus__. Ông này rất ghét viết __Kernel__ bằng __C++__ bởi vì _nó không tường minh, và trên các hệ máy khác nhau nó cũng không tường minh_. Đơn giản mỗi mã lệnh của C chỉ đơn giản là nó sẽ làm đúng việc một việc đó, không có tham chiếu, không có ánh xạ, .. điều này khiến tất cả các hệ thống đều có thể thống nhất mối quan hệ cho __C__ và các mã mãy __OpCode__.

Thực sự thì lúc đầu Windows cũng sử dụng __*C*__ và __*Assembly*__ để viết các API cấp thấp. Nhưng sau khi tính năng mở rộng, các lập trình viên thích khả năng hướng đối tượng của __C++__ hơn nên đã dẫn chuyển dịch sang __C++__ cho __MSVC__.

Thế nên nếu trên Windows, hãy dùng C++ để lập trình và dùng MSVC để dựng. Thậm chí kể cả lập trình driver cũng dùng được. Một lựa chọn khác có thể là __C#__.