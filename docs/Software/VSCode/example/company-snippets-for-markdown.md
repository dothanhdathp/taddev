# \[VSCode\] Example Company Snipppets for Markdown

[🔙 [VSCode] Snipppets](../software-vscode-snippets.md)

> Ví dụ về snippets cho markdown mình tự định nghĩa trên máy công ty

```text
{
	// Place your snippets for markdown here. Each snippet is defined under a snippet name and has a prefix, body and 
	// description. The prefix is what is used to trigger the snippet and the body will be expanded and inserted. Possible variables are:
	// $1, $2 for tab stops, $0 for the final cursor position, and ${1:label}, ${2:another} for placeholders. Placeholders with the 
	// same ids are connected.
	// Example:
	// "Print to console": {
	// 	"prefix": "log",
	// 	"body": [
	// 		"console.log('$1');",
	// 		"$2"
	// 	],
	// 	"description": "Log output to console"
	// }
	"Table": {
		"prefix": "/table",
		"body": [
			"|1 |2 |3 |",
			"|:-|:-|:-|",
			"|  |  |  |"
		],
	},
	"Table Of Content": {
		"prefix": "/toc",
		"body": [
			"[[TOC]]",
		],
	},
	"Detail": {
		"prefix": "/detail",
		"body": [
			"<details><summary>title</summary>",
			"</details>"
		],
	},
	"Padding Detail": {
		"prefix": "/pdetail",
		"body": [
			"<details>",
			"<summary padding-left: 16px;>",
			"</summary>",
			"</details>"
		],
	},
	"padding": {
		"prefix": "/padding",
		"body": [
			"<div style=\"padding-left: 20px;\">\n\n</div>"
		],
	},
	"space": {
		"prefix": "/space",
		"body": [
			"&emsp;"
		],
	},
	"space-header": {
		"prefix": "/space-header",
		"body": [
			"&emsp;>>&emsp;"
		],
	},
	"two-column": {
		"prefix": "/two-column",
		"body": [
			"<div style=\"display: flex; gap: 20px;\">",
			"  <div style=\"flex: 1;\">",
			"  </div>",
			"  <div style=\"flex: 1;\">",
  			"  </div>",
			"</div>"
		]
	},
	"two-column-2": {
		"prefix": "/two-column-3-7",
		"body": [
			"<div class=\"two-column\">",
			"<div style=\"float: left; width: 30%;\">",
			"</div>",
			"<div style=\"float: right; width: 70%;\">",
			"</div>",
			"</div>"
		]
	},
	"center": {
		"prefix": "/center-text",
		"body": [
			"<div style=\"text-align: center;\">",
			"</div>"
		]
	},
	"center-image": {
		"prefix": "/center-image",
		"body": [
			"<figure markdown=\"span\">",
			"\t",
			"\t<figcaption></figcaption>",
			"</figure>"
		]
	},
	"center-table": {
		"prefix": "/center-table",
		"body": [
			"<div class=\"center-table\" markdown>",
			"</figure>"
		]
	},
	"right": {
		"prefix": "/right",
		"body": [
			"<div style=\"text-align: right;\">",
			"",
			"</div>"
		]
	},
	"marp-slide": {
		"prefix": "/slide",
		"body": [
			"---",
			"marp: true",
			"theme: uncover",
			"style: |",
			"  ul {",
			"    -size: 25px",
			"  }",
			"---",
			"Hello Tad",
			"---"
		]
	},
	"note": {
		"prefix": "/note",
		"body": [
			"!!! note \"Note\""
		]
	},
	"note-abstract": {
		"prefix": "/note-abstract",
		"body": [
			"!!! abstract \"Abstract\""
		]
	},
	"note-info": {
		"prefix": "/note-info",
		"body": [
			"!!! info \"Info\""
		]
	},
	"note-tip": {
		"prefix": "/note-tip",
		"body": [
			"!!! tip \"Tip\""
		]
	},
	"note-success": {
		"prefix": "/note-success",
		"body": [
			"!!! success \"Success\""
		]
	},
	"note-question": {
		"prefix": "/note-question",
		"body": [
			"!!! question \"Question\""
		]
	},
	"note-warning": {
		"prefix": "/note-warning",
		"body": [
			"!!! warning \"Warning\""
		]
	},
	"note-failure": {
		"prefix": "/note-failure",
		"body": [
			"!!! failure \"Failure\""
		]
	},
	"note-danger": {
		"prefix": "/note-danger",
		"body": [
			"!!! danger \"Danger\""
		]
	},
	"note-bug": {
		"prefix": "/note-bug",
		"body": [
			"!!! bug \"Bug\""
		]
	},
	"note-example": {
		"prefix": "/note-example",
		"body": [
			"!!! example \"Example\""
		]
	},
	"note-quote": {
		"prefix": "/note-quote",
		"body": [
			"!!! quote \"Quote\""
		]
	},
	"quick-link": {
		"prefix": "/qlink",
		"body": [
			"&emsp;[](./)",
		]
	},
	"add-script": {
		"prefix": "/script",
		"body": [
			"<script src=\"http://localhost:8000/.theme/script.js\"></script>",
		]
	},
	"image": {
		"prefix": "/image",
		"body": [
			"<style type=\"text/css\">img{width:  100px; height: 100px;}</style>",
		]
	},
	"limit-image-size": {
		"prefix": "/limit-image-size",
		"body": [
			"<style type=\"text/css\">img{width:  100px; height: 100px;}</style>",
		]
	},
	"img-block-page": {
		"prefix": "/img-block-page",
		"body": [
			"<div class=\"container\"><br>\n\n</div>",
		]
	},
	"mermaid-flowchart": {
		"prefix": "/mermaid-flowchart",
		"body": [
			"```mermaid-flowchart",
			"flowchart TD",
			"A[Christmas] -->|Get money| B(Go shopping)",
			"B --> C{Let me think}",
			"C -->|One| D[Laptop]",
			"C -->|Two| E[iPhone]",
			"C -->|Three| F[fa:fa-car Car]",
			"```"
		],
	},
	"mermaid-sequenceDiagram": {
		"prefix": "/mermaid-sequenceDiagram",
		"body": [
			"```mermaid",
			"sequenceDiagram",
			"Alice->>+John: Hello John, how are you?",
			"Alice->>+John: John, can you hear me?",
			"John-->>-Alice: Hi Alice, I can hear you!",
			"John-->>-Alice: I feel great!",
			"```"
		],
	},
	"mermaid-classDiagram": {
		"prefix": "/mermaid-classDiagram",
		"body": [
			"```mermaid",
			"classDiagram",
			"Animal <|-- Duck",
			"Animal <|-- Fish",
			"Animal <|-- Zebra",
			"Animal : +int age",
			"Animal : +String gender",
			"Animal: +isMammal()",
			"Animal: +mate()",
			"class Duck{",
			"+String beakColor",
			"+swim()",
			"+quack()",
			"}",
			"class Fish{",
			"-int sizeInFeet",
			"-canEat()",
			"}",
			"class Zebra{",
			"+bool is_wild",
			"+run()",
			"}",
			"```"
		],
	},
	"mermaid-stateDiagram-v2": {
		"prefix": "/mermaid-stateDiagram-v2",
		"body": [
			"```mermaid",
			"stateDiagram-v2",
			"[*] --> Still",
			"Still --> [*]",
			"Still --> Moving",
			"Moving --> Still",
			"Moving --> Crash",
			"Crash --> [*]",
			"```"
		],
	},
	"mermaid-erDiagram": {
		"prefix": "/mermaid-erDiagram",
		"body": [
			"```mermaid",
			"erDiagram",
			"CUSTOMER }|..|{ DELIVERY-ADDRESS : has",
			"CUSTOMER ||--o{ ORDER : places",
			"CUSTOMER ||--o{ INVOICE : \"liable for\"",
			"DELIVERY-ADDRESS ||--o{ ORDER : receives",
			"INVOICE ||--|{ ORDER : covers",
			"ORDER ||--|{ ORDER-ITEM : includes",
			"PRODUCT-CATEGORY ||--|{ PRODUCT : contains",
			"PRODUCT ||--o{ ORDER-ITEM : \"ordered in\"",
			"```"
		],
	},
	"mermaid-gantt": {
		"prefix": "/mermaid-gantt",
		"body": [
			"```mermaid",
			"gantt",
			"title A Gantt Diagram",
			"dateFormat\tYYYY-MM-DD",
			"section Section",
			"A task\t\t:a1, 2014-01-01, 30d",
			"Another task\t\t:after a1 , 20d",
			"section Another",
			"Task in sec\t\t:2014-01-12 , 12d",
			"another task\t\t: 24d",
			"```"
		],
	},
	"mermaid-journey": {
		"prefix": "/mermaid-journey",
		"body": [
			"```mermaid",
			"journey",
			"title My working day",
			"section Go to work",
			"Make tea: 5: Me",
			"Go upstairs: 3: Me",
			"Do work: 1: Me, Cat",
			"section Go home",
			"Go downstairs: 5: Me",
			"Sit down: 3: Me",
			"```"
		],
	},
	"mermaid-gitGraph": {
		"prefix": "/mermaid-gitGraph",
		"body": [
			"```mermaid",
			"gitGraph",
			"commit",
			"commit",
			"branch develop",
			"checkout develop",
			"commit",
			"commit",
			"checkout main",
			"merge develop",
			"commit",
			"commit",
			"```"
		],
	},
	"mermaid-pie": {
		"prefix": "/mermaid-pie",
		"body": [
			"```mermaid",
			"pie title Pets adopted by volunteers",
			"\"Dogs\" : 386",
			"\"Cats\" : 85",
			"\"Rats\" : 15",
			"```"
		],
	},
	"mermaid-mindmap": {
		"prefix": "/mermaid-mindmap",
		"body": [
			"```mermaid",
			"mindmap",
			"  root((mindmap))",
			"    Origins",
			"      Long history",
			"      ::icon(fa fa-book)",
			"      Popularisation",
			"        British popular psychology author Tony Buzan",
			"    Research",
			"      On effectivness<br/>and features",
			"      On Automatic creation",
			"        Uses",
			"            Creative techniques",
			"            Strategic planning",
			"            Argument mapping",
			"    Tools",
			"      Pen and paper",
			"      Mermaid",
			"```"
		],
	},
	"mermaid-quadrantChart": {
		"prefix": "/mermaid-quadrantChart",
		"body": [
			"```mermaid",
			"quadrantChart",
			"title Reach and engagement of campaigns",
			"x-axis Low Reach --> High Reach",
			"y-axis Low Engagement --> High Engagement",
			"quadrant-1 We should expand",
			"quadrant-2 Need to promote",
			"quadrant-3 Re-evaluate",
			"quadrant-4 May be improved",
			"Campaign A: [0.3, 0.6]",
			"Campaign B: [0.45, 0.23]",
			"Campaign C: [0.57, 0.69]",
			"Campaign D: [0.78, 0.34]",
			"Campaign E: [0.40, 0.34]",
			"Campaign F: [0.35, 0.78]",
			"```"
		],
	},
	"mermaid-xychart-beta": {
		"prefix": "/mermaid-xychart-beta",
		"body": [
			"```mermaid",
			"xychart-beta",
			"title \"Sales Revenue\"",
			"x-axis [jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec]",
			"y-axis \"Revenue (in $)\" 4000 --> 11000",
			"bar [5000, 6000, 7500, 8200, 9500, 10500, 11000, 10200, 9200, 8500, 7000, 6000]",
			"line [5000, 6000, 7500, 8200, 9500, 10500, 11000, 10200, 9200, 8500, 7000, 6000]",
			"```"
		],
	},
	"mermaid-timeline": {
		"prefix": "/mermaid-timeline",
		"body": [
			"```mermaid",
			"timeline",
			"title History of Social Media Platform",
			"2002 : LinkedIn",
			"2004 : Facebook",
			"     : Google",
			"2005 : Youtube",
			"2006 : Twitter",
			"```"
		],
	},
	"roadmap-table-content": {
		"prefix": "/roadmap-table-content",
		"body": [
			"<div class=\"two-column\">",
			"<div style=\"float: left; width: 30%;\">",
			"",
			"+++ Chapter 0: Getting Start",
			"- Introduce",
			"+++",
			"+++ Chapter 1: Begin",
			"- Topic 1.1",
			"- Topic 1.2",
			"+++",
			"",
			"</div>",
			"<div div style=\"float: right; width: 70%;\">",
			"",
			"```plantuml",
			"@startsalt",
			"{",
			"{T",
			"+ =Chapter 0: Getting Start",
			"++ Instroduce",
			"+ =Chapter 1: Begin",
			"++ Topic 1.1",
			"++ Topic 1.2",
			"}",
			"}",
			"@endsalt",
			"```",
			"",
			"</div>",
			"</div>"
		],
	},
	"uml": {
		"prefix": "/uml",
		"body": [
			"```plantuml",
			"@startuml",
			"@enduml",
			"```"
		],
	},
	"uml-mindmap": {
		"prefix": "/uml-mindmap",
		"body": [
			"```plantuml",
			"@startmindmap",
			"@endmindmap",
			"```"
		],
	},
	"uml-wbs": {
		"prefix": "/uml-wbs",
		"body": [
			"```plantuml",
			"@startwbs",
			"@endwbs",
			"```"
		],
	},
	"code-c": {
		"prefix": "/code-c",
		"body": ["```c",
		"",
		"```",]
	},
	"code-rust": {
		"prefix": "/code-rust",
		"body": ["```rust",
		"",
		"```",]
	},
	"code-javascript": {
		"prefix": "/code-javascript",
		"body": ["```javascript",
		"",
		"```",]
	},
	"code-html": {
		"prefix": "/code-html",
		"body": ["```html",
		"",
		"```",]
	},
	"code-cpp": {
		"prefix": "/code-cpp",
		"body": ["```c++",
		"",
		"```",]
	},
	"code-python": {
		"prefix": "/code-python",
		"body": ["```python",
		"",
		"```",]
	},
	"code-java": {
		"prefix": "/code-java",
		"body": ["```java",
		"",
		"```",]
	},
	"code-bash": {
		"prefix": "/code-bash",
		"body": ["```bash",
		"",
		"```",]
	},
	"code-text": {
		"prefix": "/code-text",
		"body": ["```text",
		"",
		"```",]
	},
	"uml-participant": {
		"prefix": "participant",
		"body": "participant",
	},
	"uml-actor": {
		"prefix": "actor",
		"body": "actor",
	},
	"uml-boundary": {
		"prefix": "boundary",
		"body": "boundary",
	},
	"uml-control": {
		"prefix": "control",
		"body": "control",
	},
	"uml-entity": {
		"prefix": "entity",
		"body": "entity",
	},
	"uml-database": {
		"prefix": "database",
		"body": "database",
	},
	"uml-collections": {
		"prefix": "collections",
		"body": "collections",
	},
	"uml-queue": {
		"prefix": "queue",
		"body": "queue",
	},
}
```