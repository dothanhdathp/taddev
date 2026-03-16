#  Git Branch

> [Tài liệu kỹ thuật về git-branch](https://git-scm.com/docs/git-branch)

## Mô Tả

Lệnh `git branch` dùng để liệt kê, tạo, hoặc xóa một nhánh trên git.

### Công Thức

```text
git branch [--color[=<when>] | --no-color] [--show-current]
	   [-v [--abbrev=<n> | --no-abbrev]]
	   [--column[=<options>] | --no-column] [--sort=<key>]
	   [--merged [<commit>]] [--no-merged [<commit>]]
	   [--contains [<commit>]] [--no-contains [<commit>]]
	   [--points-at <object>] [--format=<format>]
	   [(-r|--remotes) | (-a|--all)]
	   [--list] [<pattern>…​]
git branch [--track[=(direct|inherit)] | --no-track] [-f]
	   [--recurse-submodules] <branch-name> [<start-point>]
git branch (--set-upstream-to=<upstream>|-u <upstream>) [<branch-name>]
git branch --unset-upstream [<branch-name>]
git branch (-m|-M) [<old-branch>] <new-branch>
git branch (-c|-C) [<old-branch>] <new-branch>
git branch (-d|-D) [-r] <branch-name>…​
git branch --edit-description [<branch-name>]
```

## Hướng Dẫn

### Quick Start

1. Thông thường, ta chỉ dùng lệnh này để xem nhánh của mình hiện tại đang hoạt động là nhánh nào trên _**remote**_, sử dụng câu lệnh đơn giản là `git branch`
1. Trong trường hợp ta muốn xem toàn bộ các nhánh tồn tại, sử dụng `git branch -a` hoặc `git branch --list`
1. Trong môi trường git làm việc với nhiều nhánh, có thể cài đặt nhánh chính với `--set-upstream-to=[remote/branch-name]` để đặt nhánh đó làm nhánh chính. Khi đó lệnh `git push` sẽ tự động đẩy commit lên nhánh đang được đăng ký.
    - Tương tự, để hủy, ta dùng `git branch --unset-upstream [remote/branch-name]` để xóa nhánh khỏi đăng ký nhánh khỏi phiên làm việc mặc định.


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

### Giải thích

Các bước xóa một nhánh trên _git_

1. Tạo một branch khác biệt lập với nhánh cần xóa.
    ```bash
    git checkout --orphan latest_branch    
    ```
1. Thêm tất cả các tệp vào nhánh mới được tạo:
    ```bash
    git add -A
    ```
1. Cam kết các thay đổi:
    ```bash
    git commit -am "commit message"
    ```
1. Xóa nhánh chính (mặc định) (bước này là vĩnh viễn):
    ```bash
    git branch -D main
    ```
1. Đổi tên nhánh hiện tại thành `main`:
    ```bash
    git branch -m main
    ```
1. Cuối cùng, tất cả các thay đổi được hoàn thành trên kho lưu trữ cục bộ của bạn và buộc cập nhật kho lưu trữ từ xa của bạn:
    ```bash
    git push -f origin main
    ```

### Hàm delete_git_history

Thêm hàm này vào tệp `.bashrc` hoặc `.bash_aliases` và dùng nó như là một cách sử dụng tệp hệ thống.
<mark>Chú ý! Lệnh này cần tải và cài đặt git.</mark>

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