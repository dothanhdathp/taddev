# Delete Branch

## How

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