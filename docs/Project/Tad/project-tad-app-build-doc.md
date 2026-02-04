# \[TadApp\]

## Linux

__*Chỉ dành cho Linux vì hiện tại hệ điều hành khác chưa làm*__

Tạo tệp __tasks.json__ bên trong thư mục __.vscode__ như này:

```json
{
    // See https://go.microsoft.com/fwlink/?LinkId=733558
    // for the documentation about the tasks.json format
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Mkdocs Build",
            "type": "shell",
            "linux": {
                "command": "source ./env.sh; if [ \"${fileExtname}\" == \".md\" ]; then quick_rebuild; elif [ \"${fileExtname}\" == \".yml\" ]; then rebuild; else echo 'Build docs false'; fi",
            },
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "isBackground": true,
        }
    ]
}
```

Ý tưởng của kịch bản này là sẽ build nhanh nếu đang ở tệp `.md` và build tổng nếu ở tệp `.yml`. Nhờ thế tốc độ dựng một tệp nhanh hơn nhiều _(cỡ `ms` là xong)_.

Thêm phím tắt để dựng nữa là được, thêm trong tệp __*keybindings.json*__ của __VsCode__ nữa là ổn:

```json
    {
        "key": "ctrl+q",
        "command": "workbench.action.tasks.build",
        "when": "editorLangId == 'markdown' || editorLangId == yaml"
    },
```

!!! warning "Warning"
    Cài đặt như vậy hoạt động được vì mình đã bỏ cái nút `ctrl+q` sẽ thoát ứng dụng của __*VsCode*__. __*Cài đặt ngu vl*__.

Và có điển nữa cần sửa đổi một chút. Trong hàm build hoặc foreach_git hãy thêm foreach_taddoc và nó như sau:

```bash
for i in $(ls | grep tad); do ...; done;
```