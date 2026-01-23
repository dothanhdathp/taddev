# \[Linux\] OpenSSH

Mở SSH server cho phép thiết bị khác truy cập vào và sử dụng câu lệnh.

## Các Bước

- __Step 1: Update System Packages__
    ```bash
    sudo apt update && sudo apt upgrade -y
    ```
- __Step 2: Install OpenSSH Server__
    ```bash
    sudo apt install openssh-server
    ```
- __Step 3: Verify the SSH Service Status__
    ```bash
    sudo systemctl status ssh
    ```
- Step 4: Configure the Firewall 
    - Allow SSH
        ```bash
        sudo ufw allow ssh
        ```
    - Check Firewall Status (optional)
        ```bash
        sudo ufw status
        ```

## Tổng hợp

```bash title="Sumarize Command"
sudo apt update && sudo apt upgrade -y
sudo apt install openssh-server
sudo ufw allow ssh
```

```bash title="Check"
sudo systemctl status ssh
sudo ufw status
```

## Máy Đích

Trên máy đích sử dụng lệnh sau để kết nối

```bash
ssh accout@ipaddress:diractory
```