# Delete Branch

## How

Để làm được điều này đầu tiên bạn cần phải tạo branch mới, xóa branch hiện tại và cập nhật lại!

Checkout/create orphan branch (this branch won't show in git branch command):

git checkout --orphan latest_branch
Add all the files to the newly created branch:

git add -A
Commit the changes:

git commit -am "commit message"
Delete main (default) branch (this step is permanent):

git branch -D main
Rename the current branch to main:

git branch -m main
Finally, all changes are completed on your local repository, and force update your remote repository:

git push -f origin main

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