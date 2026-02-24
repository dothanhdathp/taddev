# MkDocs Plugins

## Search

## Plantuml

Vẽ và trình diễn biểu đồ bằng __Planuml__

```bash title="Tải về plugin"
pip install mkdocs-network-graph-plugin
```

- Thêm khai báo `plantuml` trong tệp __mkdocs.yml__
- `puml_url` là trường cần thiết dẫn đến __*server*__ dùng để tạo ra các bản đồ _planuml_

```yaml title="mkdocs.yml"
plugins:
  - search
  - plantuml:
      puml_url: https://www.plantuml.com/plantuml/
```

## Network Graph

Trình diễn đồ thị ở cạnh bên cho biết mối quan hệ / liên kết giữa các tệp __*Markdown*__

```bash title="Tải về plugin"
pip install mkdocs-network-graph-plugin
```

Thêm khai báo `graph` trong tệp __mkdocs.yml__

```yaml title="mkdocs.yml"
plugins:
  - search
  - graph # This is the alias for mkdocs-network-graph-plugin
  # ... other plugins
```