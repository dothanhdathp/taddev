# System Info

## RAM

### Lệnh free

Kiểm tra thông tin của RAM với câu lệnh `free -h`

```bash
$ free -h
            total        used        free      shared  buff/cache   available
Mem:            15Gi       1.8Gi        12Gi       226Mi       1.6Gi        13Gi
Swap:          2.0Gi          0B       2.0Gi
```

Muốn có đầy đủ thông tin thì có thể đọc từ __*system file*__ `proc/meminfo`

### meminfo

```bash
$ cat /proc/meminfo
MemTotal:       16236108 kB
MemFree:        13240436 kB
MemAvailable:   14341892 kB
Buffers:          159008 kB
Cached:          1376768 kB
SwapCached:            0 kB
Active:          1903572 kB
Inactive:         456844 kB
...
```

### top/htop

Hai lệnh `top/htop` dùng để xem thông tin RAM một cách trực tiếp. Tức là theo dõi mức độ tiêu thụ RAM cũng như CPU một cách trực tiếp thông qua màn hình __*console*__.

#### top

Một cửa sổ giao diệnh của lệnh top

<figure markdown="span">
    ![alt text](img/linux-top.png)
    <figcaption>Lệnh _top_ trên hệ thống</figcaption>
</figure>

#### htop

Khác với `top`, `htop` không phải lệnh có sẵn và nó cần tải về. Về tổng quan nó cũng gần như `top` chỉ là đẹp hơn.

```text
sudo apt update
sudo apt install htop
```

