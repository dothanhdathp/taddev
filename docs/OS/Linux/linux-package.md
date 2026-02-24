# \[Linux\] Hệ Thống Quản Lý Gói

## Các Gói

Có các công cụ quản lý gói sau:

- `apt`
- `dpkg`
- `snap`

## Xem danh sách các gói đã cài:

```text
sudo apt list --installed
```

Cập nhật gói

```text
sudo snap list
```

## Các gói giống nhau có thể dùng chung một cách để xóa

```text
function uninstall_package()
{
    if [ $# -eq 0 ]; then
        echo "Need a package name."
        return 1
    fi

    for i in $#; do
        sudo apt-get remove $1 -y;
        sudo apt-get purge $1 -y;
        sudo apt-get autoremove;
        sudo apt-get clean;
    done;
}
```

```text
sudo apt-get remove libreoffice* -y;
sudo apt-get purge libreoffice* -y;
```

## Xóa các phần mềm ít cần thiết

Hướng dẫn xóa các phần mềm không cần thiết cho máy ảo / server Ubuntu bản destop cho mục đích riêng mà không cần các ứng dụng nội bộ cài đặt sẵn trên Ubuntu.

```bash
sudo snap remove thunderbird
sudo snap remove spotify
sudo apt remove libreoffice*
sudo apt purge libreoffice*
sudo apt remove evolution*
sudo apt purge evolution*
sudo apt remove evolution-data-server*
sudo apt purge evolution-data-server*
sudo apt remove rhythmbox*
sudo apt purge rhythmbox*
sudo apt remove totem*
sudo apt purge totem*
sudo apt remove totem-plugins*
sudo apt purge totem-plugins*

sudo apt remove cheese
sudo apt remove shotwell
sudo apt remove simple-scan*
sudo apt purge cheese
sudo apt purge shotwell
sudo apt purge simple-scan*

sudo apt remove aisprompt
sudo apt remove aisleriot
sudo apt remove gnome-mahjongg
sudo apt remove gnome-mines
sudo apt remove gnome-sudoku
sudo apt remove transmission*
sudo apt purge aisprompt
sudo apt purge aisleriot
sudo apt purge gnome-mahjongg
sudo apt purge gnome-mines
sudo apt purge gnome-sudoku
sudo apt purge transmission*
```

Xong thì có thể chạy lại lệnh sau để lấy về Ubuntu nhỏ và nhẹ

```bash
sudo apt install ubuntu-desktop-minimal
```

## Cài đặt UART console cho PI

### 1. Identify the UART device

The Pi4 has two UARTs:
- PL011 (ttyAMA0) – the main hardware UART.
- miniUART (ttyS0) – secondary, less stable.

By default, Bluetooth uses the PL011, so you may need to disable Bluetooth to free it for GPIO pins.

### 2. Edit boot configuration

Open `/boot/firmware/config.txt`:

```text
sudo nano /boot/firmware/config.txt
```

Add these lines:

```text
enable_uart=1
dtoverlay=disable-bt
```

- `enable_uart=1` ensures the UART is active.
- `dtoverlay=disable-bt` disables Bluetooth so PL011 is mapped to GPIO14 (TX) and GPIO15 (RX).

### 3. Redirect console to UART

Edit `/boot/firmware/cmdline.txt`:


```bash
sudo nano /boot/firmware/cmdline.txt
```

Replace the existing console setting with:

```text
console=serial0,115200 console=tty1
```

- `serial0` is a symlink to the active UART (usually ttyAMA0).
- `115200` is the baud rate.

### 4. Verify UART mapping

After reboot, check which device is active:

```text
dmesg | grep tty
```

You should see something like:

```text
fe201000.serial: ttyAMA0 at MMIO ...
```