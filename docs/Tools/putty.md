# putty.exe

## putty.exe

- _**putty.exe**_ dùng để đọc tính hiệu từ TCPIP, hoặc serial console. _**putty.exe**_ có thể chạy trực tiếp và cấu hình bằng tay.
- _**putty.exe**_ cũng hoạt động ở chế độ CLI, qua lệnh dưới đây:

```bash
putty.exe -serial COM10 -sercfg 115200,8,n,1,N -m command
```

## plink.exe

_**plink.exe**_ để truyền _command (lệnh hoặc nội dung)_ vào đường serial, dùng để thi thoảng nếu mình muốn chạy tự động gì đó qua _**serial**_. Chẳng hạn _command tools_.

```text
plink.exe -serial COM10 -sercfg 115200,8,n,1,X < command
```

## Sử dụng plink để dùng serial com trong command

Ở đây mình sẽ lưu vào tệp tin `pcom.bat`

`%~1`, `%~2` là sử dụng cho hai đầu vào. Cách dùng ví dụ như sau:

```bat
pcom COM1 115200
```
### Nội dung tệp
```bat
@echo off

:: Set your variables here
:loop

:: Execute the plink command
plink.exe -serial %~1 -sercfg %~2,8,n,1,X < break
plink.exe -serial %~1 -sercfg %~2,8,n,1,X
:: Go back to the start of the loop
goto loop
```