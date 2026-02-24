# Linux Ethernet

## Thông Tin Mạng

Để xem thông tin sử dụng:

```bash
ifconfig
```
```text title="Kết Quả"
eth0: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        ether d8:3a:dd:1d:82:64  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 116  bytes 11728 (11.4 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 116  bytes 11728 (11.4 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

wlan0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.1.105  netmask 255.255.255.0  broadcast 192.168.1.255
        inet6 fd00::c8e9:fc9d:6d75:3f32  prefixlen 64  scopeid 0x0<global>
        inet6 fe80::48f1:d06e:589b:9661  prefixlen 64  scopeid 0x20<link>
        ether d8:3a:dd:1d:82:65  txqueuelen 1000  (Ethernet)
        RX packets 4087  bytes 2585185 (2.4 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 1337  bytes 128067 (125.0 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

```

- `eth0`: Mạng Dây
- `lo`: ??? (không biết)
- `wlan0`: Wifi