# \[VSCode\] Example Company Snipppets for Markdown

[🔙 [VSCode] Snipppets](../software-vscode-snippets.md)

> Ví dụ về snippets cho markdown mình tự định nghĩa trên máy công ty

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
    "note-abstract":    { "prefix": "/note-abstract", "body": ["!!! abstract \"Abstract\""]},
    "note-info":        { "prefix": "/note-info",     "body": ["!!! info \"Info\""]},
    "note-tip":         { "prefix": "/note-tip",      "body": ["!!! tip \"Tip\""]},
    "note-success":     { "prefix": "/note-success",  "body": ["!!! success \"Success\""]},
    "note-question":    { "prefix": "/note-question", "body": ["!!! question \"Question\""]},
    "note-warning":     { "prefix": "/note-warning",  "body": ["!!! warning \"Warning\""]},
    "note-failure":     { "prefix": "/note-failure",  "body": ["!!! failure \"Failure\""]},
    "note-danger":      { "prefix": "/note-danger",   "body": ["!!! danger \"Danger\""]},
    "note-bug":         { "prefix": "/note-bug",      "body": ["!!! bug \"Bug\""]},
    "note-example":     { "prefix": "/note-example",  "body": ["!!! example \"Example\""]},
    "note-quote":       { "prefix": "/note-quote",    "body": ["!!! quote \"Quote\""]},
    "colapse":          { "prefix": "/colapse",          "body": ["??? note \"Note\""]},
    "colapse-abstract": { "prefix": "/colapse-abstract", "body": ["??? abstract \"Abstract\""]},
    "colapse-info":     { "prefix": "/colapse-info",     "body": ["??? info \"Info\""]},
    "colapse-tip":      { "prefix": "/colapse-tip",      "body": ["??? tip \"Tip\""]},
    "colapse-success":  { "prefix": "/colapse-success",  "body": ["??? success \"Success\""]},
    "colapse-question": { "prefix": "/colapse-question", "body": ["??? question \"Question\""]},
    "colapse-warning":  { "prefix": "/colapse-warning",  "body": ["??? warning \"Warning\""]},
    "colapse-failure":  { "prefix": "/colapse-failure",  "body": ["??? failure \"Failure\""]},
    "colapse-danger":   { "prefix": "/colapse-danger",   "body": ["??? danger \"Danger\""]},
    "colapse-bug":      { "prefix": "/colapse-bug",      "body": ["??? bug \"Bug\""]},
    "colapse-example":  { "prefix": "/colapse-example",  "body": ["??? example \"Example\""]},
    "colapse-quote":    { "prefix": "/colapse-quote",    "body": ["??? quote \"Quote\""]},
    "puml": {
        "prefix": "/puml",
        "body": [
            "```puml",
            "@startuml",
            "skinparam backgroundcolor transparent",
            "!$URL = \"http://localhost:\"",
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
            "!$URL = \"http://localhost:\"",
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
            "!$URL = \"http://localhost:\"",
            "@endwbs",
            "```"
        ],
    },
}
```