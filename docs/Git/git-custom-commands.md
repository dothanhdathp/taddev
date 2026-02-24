# \[Git\] Custom Commands

Một số mẹo vặt khi thao tác với ___git___

### Với Windows

Vì __Windows__ sẽ sử dụng một hệ thống `git bash` khác _(cái mà được chạy qua môi trường ảo)_. Thường nó sẽ tải _env_ qua `%USERPROFILE%`. Ở đây dễ thấy làm gì có tệp `~/.bashrc`. Giải pháp đơn giản chỉ là tự tạo tệp đó và truyền vào nội dung tương tự là được.

## Commands

### foreach_git

#### Mô tả

!!! abstract "Hướng dẫn"
   Lệnh này sẽ áp dụng câu lệnh với tất cả các thư mục git con có trong đường dẫn. Lệnh này tìm đến các thư mục có chứa tệp ẩn `.git` tại thư mục và thực thi câu lệnh trên đó.

   Ví dụ:

   ```bash
   foreach_git git pull
   ```

```bash
function foreach_git()
{
   if [ $# -eq 0 ]; then
      echo "Usage: foreach_git <git command>"
      return 1
   fi

   base_dir=$(pwd)

   # Find all .git directories and run command inside their parent directories
   for i in $(find -name .git); do
        cd ${i:2:-4};
        $@;
        cd $base_dir;
   done;
}
```

??? abstract "foreach_taddoc"
    *Một biến thể khác của foreach_git sử dụng để đọc thay đổi duy nhất cho các tệp tài liệu*

    ```bash
    function foreach_taddoc()
    {
        if [ $# -eq 0 ]; then
            echo "Usage: foreach_git <git command>"
            return 1
        fi

        base_dir=$(pwd)

        # Find all .git directories and run command inside their parent directories
        for i in $(find -name .git | grep tad); do
                cd ${i:2:-4};
            echo;
            echo ----- $(pwd) -----
            echo;
                $@;
                cd $base_dir;
            echo;
        done;
    }
    ```

### delete_git_history

??? abstract "Hướng dẫn"
    Lệnh này xoá toàn bộ lịch sử của git trên nhánh hiện tại. Điều này tốt với các dự án cá nhân làm tối ưu hoá dung lượng của các tệp git.
    
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