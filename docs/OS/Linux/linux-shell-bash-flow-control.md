# Điều Khiển Luồng

## FOR

```text title="Syntax"

# General
for i in {list}; do {command}; done;

# Mutil Commands
for i in {list}; do {command}; {command}; {command}; done;
```
### Ví Dụ

```bash
for i in a b c; do echo $i; done;
for i in $(ls); do echo $i; done;
```

```bash title="File"
#!/usr/bin/bash

for i in a b c; do
    echo 1
    echo 2
done;
```

## SWITCH-CASE

```bash title="File"
#!/usr/bin/bash

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
```
