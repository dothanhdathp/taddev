# MkDocs Mermaid

## Tải về mermaid-plugin

```yml
pip install mkdocs-mermaid2-plugin
```

## Khai báo plugins

_Nên dùng javascript, có thể kiểm tra trực tiếp tệp **js** có tồn tại hay không_

=== "javascript"
  ```yml
  plugins:
    - mermaid2:
      javascript: https://unpkg.com/mermaid@11.12.2/dist/mermaid.esm.min.mjs
  ```
=== "version"
  ```yml
  plugins:
    - mermaid2:
        version: 11.12.2
  ```

## Superfences

Chế độ này sẽ tự động căn chỉnh màu sắc của map tương đồng với theme của mkdocs. À thì cũng được nhưng có nhiều vấn đề phát sinh như méo hình, lỗi xuống dòng, ... nên thôi dẹp đi.

=== "Cách 1"
  ```yml
  markdown_extensions:
    - pymdownx.superfences:
        custom_fences:
          - name: mermaid
            class: mermaid
            format: !!python/name:mermaid2.fence_mermaid_custom
  ```
=== "Cách 2"
  ```yml
  markdown_extensions:
    - pymdownx.superfences:
        custom_fences:
          - name: mermaid
            class: mermaid
            format: !!python/name:pymdownx.superfences.fence_code_format
  ```