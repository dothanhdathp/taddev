# Kernel Module

| Mục Đích                                          | Lệnh                                           |
| :------------------------------------------------ | :--------------------------------------------- |
| Liệt kê các Driver đang được nạp (Kernel Modules) | `lsmod`                                        |
| Cho các thiết bị PCI (Card đồ họa, Wifi, v.v.)    | `lspci -k`                                     |
| Cho các thiết bị USB                              | `lsusb -t`                                     |
| Xem thông tin chi tiết của một Driver cụ thể      | `modinfo <module_name>`                        |
| Kiểm tra các Driver được tích hợp sẵn (Built-in)  | `cat /lib/modules/$(uname -r)/modules.builtin` |
| Xem nhật ký nạp Driver (Dmesg)                    | `dmesg | grep -i driver`                       |