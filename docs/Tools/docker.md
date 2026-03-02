# Linux Docker

## Setup repository

- __Add Docker's official GPG key:__
    ```bash
    sudo apt update
    sudo apt install ca-certificates curl
    sudo install -m 0755 -d /etc/apt/keyrings
    sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
    sudo chmod a+r /etc/apt/keyrings/docker.asc
    ```
- __Add the repository to Apt sources:__
    ```bash
    sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
    Types: deb
    URIs: https://download.docker.com/linux/ubuntu
    Suites: $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}")
    Components: stable
    Signed-By: /etc/apt/keyrings/docker.asc
    EOF

    sudo apt update
    ```

## Install the Docker packages

### Install Version

=== "Latest"
    ```bash
    sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
    ```
=== "Specific version"
    ```bash
    apt list --all-versions docker-ce
    ```

### Check Services

```bash
sudo systemctl status docker
```

```bash
sudo systemctl start docker
```

## Tiến trình

Kiểm tra xem tiến trình `docker` nào đang chạy:

- Xem tiến trình đang chạy
    ```bash
    sudo docker ps
    ```
- Đọc lấy __ID__ tiến trình trong trường __CONTAINER ID__
    ```text
    CONTAINER ID   IMAGE                            COMMAND            CREATED          STATUS          PORTS                                         NAMES
    440d092cf27d   plantuml/plantuml-server:jetty   "/entrypoint.sh"   16 minutes ago   Up 16 minutes   0.0.0.0:8080->8080/tcp, [::]:8080->8080/tcp   hungry_hamilton
    ```
- __Dừng tiến trình__ bằng cách
    ```bash
    sudo docker stop <CONTAINER ID>
    ```