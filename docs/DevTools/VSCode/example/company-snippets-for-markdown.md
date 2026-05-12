# VSCode Example Company Snipppets for Markdown

> Ví dụ về snippets cho markdown mình tự định nghĩa trên máy công ty

{% raw %}
```json
{
    // Place your snippets for markdown here. Each snippet is defined under a snippet name and has a prefix, body and 
    // description. The prefix is what is used to trigger the snippet and the body will be expanded and inserted. Possible variables are:
    // $1, $2 for tab stops, $0 for the final cursor position, and ${1:label}, ${2:another} for placeholders. Placeholders with the 
    // same ids are connected.
    // Example:
    // "Print to console": {
    //  "prefix": "log",
    //  "body": [
    //      "console.log('$1');",
    //      "$2"
    //  ],
    //  "description": "Log output to console"
    // }
    "Table": {
        "prefix": "/table",
        "body": [
            "|1 |2 |3 |",
            "|:-|:-|:-|",
            "|  |  |  |"
        ],
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
    "note":             { "prefix": "/note",          "body": ["!!! note \"Note\""]},
    "note-abstract":    { "prefix": "/abstract-note", "body": ["!!! abstract \"Abstract\""]},
    "note-info":        { "prefix": "/info-note",     "body": ["!!! info \"Info\""]},
    "note-tip":         { "prefix": "/tip-note",      "body": ["!!! tip \"Tip\""]},
    "note-success":     { "prefix": "/success-note",  "body": ["!!! success \"Success\""]},
    "note-question":    { "prefix": "/question-note", "body": ["!!! question \"Question\""]},
    "note-warning":     { "prefix": "/warning-note",  "body": ["!!! warning \"Warning\""]},
    "note-failure":     { "prefix": "/failure-note",  "body": ["!!! failure \"Failure\""]},
    "note-danger":      { "prefix": "/danger-note",   "body": ["!!! danger \"Danger\""]},
    "note-bug":         { "prefix": "/bug-note",      "body": ["!!! bug \"Bug\""]},
    "note-example":     { "prefix": "/example-note",  "body": ["!!! example \"Example\""]},
    "note-quote":       { "prefix": "/quote-note",    "body": ["!!! quote \"Quote\""]},
    "colapse":          { "prefix": "/colapse",          "body": ["??? note \"Note\""]},e
    "colapse-abstract": { "prefix": "/abstract-colapse", "body": ["??? abstract \"Abstract\""]},
    "colapse-info":     { "prefix": "/info-colapse",     "body": ["??? info \"Info\""]},
    "colapse-tip":      { "prefix": "/tip-colapse",      "body": ["??? tip \"Tip\""]},
    "colapse-success":  { "prefix": "/success-colapse",  "body": ["??? success \"Success\""]},
    "colapse-question": { "prefix": "/question-colapse", "body": ["??? question \"Question\""]},
    "colapse-warning":  { "prefix": "/warning-colapse",  "body": ["??? warning \"Warning\""]},
    "colapse-failure":  { "prefix": "/failure-colapse",  "body": ["??? failure \"Failure\""]},
    "colapse-danger":   { "prefix": "/danger-colapse",   "body": ["??? danger \"Danger\""]},
    "colapse-bug":      { "prefix": "/bug-colapse",      "body": ["??? bug \"Bug\""]},
    "colapse-example":  { "prefix": "/example-colapse",  "body": ["??? example \"Example\""]},
    "colapse-quote":    { "prefix": "/quote-colapse",    "body": ["??? quote \"Quote\""]},
    "puml": {
        "prefix": "/puml",
        "body": [
            "```puml",
            "@startuml",
            "skinparam backgroundcolor transparent",
            "!$URL = \"\"",
            "@enduml",
            "```"
        ],
    },
    "puml-mindmap": {
        "prefix": "/puml-mindmap",
        "body": [
            "```puml",
            "@startmindmap",
            "skinparam backgroundcolor transparent",
            "!\\$URL = \"\"",
            "@endmindmap",
            "```"
        ],
    },
    "puml-wbs": {
        "prefix": "/puml-wbs",
        "body": [
            "```puml",
            "@startwbs",
            "skinparam backgroundcolor transparent",
            "!\\$URL = \"\"",
            "@endwbs",
            "```"
        ],
    },
    "puml-general": {
        "prefix": "/puml-general",
        "body": [
            "```puml",
            "@startuml",
            "skinparam backgroundcolor transparent",
            "@endwbs",
            "```"
        ],
    },
    "vi-en": {
        "prefix": "/vi-en",
        "body": [
            "=== \"VI\"",
            "=== \"EN\"",
        ],
    },
    "sticky-note": {
        "prefix": "/vi-en",
        "body": [
            "<div class=\"sticky-note\" markdown=\"1\">",
            "<div class=\"sticky-note-header\">:::</div>",
            "Note in here",
            "</div>",
        ],
    },
    "diagram": {
        "prefix": "/diagram",
        "body": [
            "{{ diagram(\"file.puml\") }}",
        ],
    },
    "center-text": {
        "prefix": "/center-text",
        "body": [
            "<div style=\"text-align: center; font-style: italic; font-color: gray;\">",
            "</div>"
        ],
        "description": ""
    },
    "collapsible": {
        "prefix": "/collapsible",
        "body": [
            "<details>",
            "\t<summary>telechip-private-key</summary>",
            "</details>"
        ],
        "description": ""
    },
    "mdbook-tabs": {
        "prefix": "/mdbook-tabs",
        "body": [
            "{{#tabs }}",
            "{{#tab name=\"Tab 1\" }}",
            "**Tab content 1**",
            "{{#endtab }}",
            "{{#tab name=\"Tab 2\" }}",
            "_Tab content 2_",
            "{{#endtab }}",
            "{{#tab name=\"Tab 3\" }}",
            "~~Tab content 3~~",
            "{{#endtab }}",
            "{{#endtabs }}",
        ],
        "description": ""
    },
    "mdbook-2-pages-view": {
        "prefix": "/mdbook-2-pages-view",
        "body": [
            "<div style=\"display: flex; gap: 20px;\"><div style=\"flex: 1;\">",
            "page_1",
            "</div><div style=\"flex: 1;\">",
            "page_2",
            "</div></div>"
        ],
        "description": ""
    },
    "markdown-detail": {
		"prefix": "/markdown-detail",
		"body": [
			"<details>",
			"<summary>${1:Summary}</summary>",
			"",
			"",
			"",
			"</details>"
		]
    }
}
```
{% endraw %}