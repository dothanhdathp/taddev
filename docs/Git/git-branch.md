# \[Git\] Git Branch

## Git Branch

Lệnh `git branch` dùng để xem nhánh hiện tại.

```bash
git branch
```

Nếu muốn xem tất cả các nhánh khả dụng, sử dụng:

```bash
git branch -a
```

Kết quả sẽ hiện đầy đủ các nhánh kèm các thông tin về _remote_ của các branch. Ví dụ như này:

```text
  dev
* stream-usb-media
  remotes/origin/HEAD -> origin/dev
  remotes/origin/dev
  remotes/origin/master
  remotes/origin/refactor-stream-websocket-client
  remotes/origin/stream-usb-media
  remotes/origin/tv-update-string
```

Như trên kia thì:

- Dấu `*` chỉ đến nhánh `stream-usb-media` là nhánh hiện tại đang hoạt động.
- `remotes/origin/HEAD -> origin/dev` cho biết rằng __HEAD__ đang nằm ở nhánh `origin/dev`
- Nhánh `stream-usb-media` thật ra đầy đủ chính là `remotes/origin/stream-usb-media` 

## Switch Branch

Có hai lệnh dành cho việc này là switch và checkout:

- `switch`: Switch branches
- `checkout`: Switch branches or restore working tree files

Ví dụ:

```bash
git switch master
```

Hoặc

```bash
git checkout master
```

## Delete Branch

- Để làm được điều này đầu tiên bạn cần phải tạo branch mới, xóa branch hiện tại và cập nhật lại!
    ```bash
    git checkout --orphan latest_branch
    ```
- Thêm tất cả các tệp vào nhánh mới được tạo:
    ```bash
    git add -A
    ```
- Cam kết các thay đổi:
    ```bash
    git commit -am "commit message"
    ```
- Xóa nhánh chính (mặc định) (bước này là vĩnh viễn):
    ```bash
    git branch -D main
    ```
- Đổi tên nhánh hiện tại thành `main`:
    ```bash
    git branch -m main
    ```
- Cuối cùng, tất cả các thay đổi được hoàn thành trên kho lưu trữ cục bộ của bạn và buộc cập nhật kho lưu trữ từ xa của bạn:
    ```bash
    git push -f origin main
    ```

```bash
function delete_git_history()
{
    read -p "This action will clean all history in your current branch! Are you sure [Y/n] " response
    case "$response" in
        [Yy]* | "" )
			br=$(git branch --show-current)
			brt="${br}_temp"
			git checkout --orphan ${brt}
			git add -A
			git commit -am "init"
			git branch -D ${br}
			git branch -m ${br}
			git push -f origin ${br}
            ;;
        [Nn]* )
            echo "Operation cancelled."
            return 1
            ;;
        * )
            echo "Invalid input. Please enter Y or N."
            confirm
            ;;
    esac
}
```