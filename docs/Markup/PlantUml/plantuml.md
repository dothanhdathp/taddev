# PlantUml

PlantUML là một công cụ rất linh hoạt tạo điều kiện tạo ra sự tạo ra nhanh chóng và đơn giản của một loạt các sơ đồ.

## PlantUML

### Tóm Tắt

1. Chủ yếu mình dùng _{{ book("Docker Server", "plantuml", "plantuml-docker-server") }}_
1. Các loại đồ thị hay dùng nhất là
	- {{ book("Sequence diagram", "plantuml", "plantuml-sequence-diagram") }} để vẽ đồ thị 
	- {{ book("Class diagram", "plantuml", "plantuml-class-diagram") }} để vẽ biển đồ quan hệ trong lập trình.
	- {{ book("MindMap diagram", "plantuml", "plantuml-mindmap-diagram") }} để vẽ sơ đồ tư duy
	- {{ book("WBS diagram", "plantuml", "plantuml-wbs-diagram") }} để vẽ đồ thị phả hệ

### Nội Dung

```puml
@startmindmap
skinparam backgroundcolor transparent
!$URL = "http://localhost:65000/book/plantuml/"

* [[$URL/plantuml.html PlantUml]]
** PlantUml Server
*** [[$URL/plantuml-jetty-server.html Jetty Server]]
*** [[$URL/plantuml-docker-server.html Docker Server]]
** UML Diagrams
***_ [[$URL/plantuml-sequence-diagram.html Sequence diagram 🏲]]
***_ [[$URL/plantuml-usecase-diagram.html Usecase diagram]]
***_ [[$URL/plantuml-class-diagram.html Class diagram 🏲]]
***_ [[$URL/plantuml-object-diagram.html Object diagram]]
***_ [[$URL/plantuml-activity-diagram.html Activity diagram]]
***_ [[$URL/plantuml-component-diagram.html Component diagram]]
***_ [[$URL/plantuml-deployment-diagram.html Deployment diagram]]
***_ [[$URL/plantuml-state-diagram.html State diagram]]
***_ [[$URL/plantuml-timing-diagram.html Timing diagram]]
** Non-UML Diagrams
***_ [[$URL/plantuml-json-data.html JSON data]]
***_ [[$URL/plantuml-yaml-data.html YAML data]]
***_ [[$URL/plantuml-ebnf-diagram.html EBNF diagram]]
***_ [[$URL/plantuml-regex-diagram.html Regex diagram]]
***_ [[$URL/plantuml-network-diagram-nwdiag.html Network diagram (nwdiag)]]
***_ [[$URL/plantuml-ui-mockups-salt.html UI mockups (salt)]]
***_ [[$URL/plantuml-archimate-diagram.html Archimate diagram]]
***_ [[$URL/plantuml-sdl.html SDL]]
***_ [[$URL/plantuml-ditaa-diagram.html Ditaa diagram]]
***_ [[$URL/plantuml-gantt-diagram.html Gantt diagram]]
***_ [[$URL/plantuml-chronology-diagram.html Chronology diagram]]
***_ [[$URL/plantuml-mindmap-diagram.html MindMap diagram 🏲]]
***_ [[$URL/plantuml-wbs-diagram.html WBS diagram 🏲]]
***_ [[$URL/plantuml-mathematics-diagram.html Mathematics]]
***_ [[$URL/plantuml-ie-diagram.html IE diagram]]
***_ [[$URL/plantuml-er-diagram.html ER diagram]]
** [[$URL/plantuml-themes.html Themes]]
*** [[$URL/plantuml-themes-light.html Themes Light]]
*** [[$URL/plantuml-themes-dark.html Themes Dark]]
*** [[$URL/plantuml-themes-paper.html Themes Paper]]
*** [[$URL/plantuml-themes-reddress.html Themes Reddress]]
@endmindmap
```