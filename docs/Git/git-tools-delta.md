# Delta
> [Github](https://github.com/dandavison/delta)

Công cụ này giúp hiển thị git diff đẹp hơn mà quan trọng nó **không thay đổi lệnh `git diff` của bạn**.

## Setup

1. PreBuild
    Cần có Rust để biên dịch. Nếu chưa có, có thể install _**toolchain**_ bằng cách 

    ```bash
    sudo apt install cargo
    sudo apt install rustup
    rustup update stable
    ```
1. Clone Source
    ```bash
    git clone https://github.com/dandavison/delta/
    cd delta
    cargo build --release
    ```
1. Build
    ```bash
    cargo build --release
    ```
    Tệp release được đặt tại `/target/release/delta`
1. Install
    - Sau chép tệp `/target/release/delta` và `/usr/bin/`
        ```bash
        sudo cp ./target/release/delta /usr/bin/
        ```
    - Kiểm tra bằng cách dùng lệnh `which delta`

## Git Setup

Thêm các thành phần  sau vào tệp `~/.gitconfig`

```text
[interactive]
	diffFilter = delta --color-only
[delta]
	navigate = true
	dark = true
	side-by-side = true
	line-numbers = true
[core]
	pager = delta
```

Hoặc dùng lệnh

```bash
git config --global core.pager delta
git config --global interactive.diffFilter 'delta --color-only'
git config --global delta.navigate true
git config --global delta.dark true
git config --global delta.side-by-side true
git config --global delta.line-numbers true
# git config --global merge.conflictStyle zdiff3
```