# \[VSCode\] Example Company Keybindings

[🔙 [VSCode] Keybindings](../software-vscode-keybindings.md)

```json
// Place your key bindings in this file to override the defaults
[
    {
        "command": "editor.action.insertSnippet",
        "args": {
            "snippet": "<u>${TM_SELECTED_TEXT}</u>"
        },
        "key": "ctrl+shift+u", // whatever you like
        "when": "editorTextFocus && editorLangId == 'markdown'"
    },
    {
        "command": "editor.action.insertSnippet",
        "args": {
            "snippet": "# \\[${TM_SELECTED_TEXT}\\]"
        },
        "key": "ctrl+1", // whatever you like
        "when": "editorTextFocus && editorLangId == 'markdown'"
    },
    {
        "command": "editor.action.insertSnippet",
        "args": {
            "snippet": "## ${TM_SELECTED_TEXT}"
        },
        "key": "ctrl+2", // whatever you like
        "when": "editorTextFocus && editorLangId == 'markdown'"
    },
    {
        "command": "editor.action.insertSnippet",
        "args": {
            "snippet": "<br>"
        },
        "key": "shift+alt+enter", // whatever you like
        "when": "editorTextFocus && editorLangId == 'markdown'"
    },
    {
        "command": "editor.action.insertSnippet",
        "args": {
            "snippet": "### ${TM_SELECTED_TEXT}"
        },
        "key": "ctrl+3", // whatever you like
        "when": "editorTextFocus && editorLangId == 'markdown'"
    },
    {
        "command": "editor.action.insertSnippet",
        "args": {
            "snippet": "#### ${TM_SELECTED_TEXT}"
        },
        "key": "ctrl+4", // whatever you like
        "when": "editorTextFocus && editorLangId == 'markdown'"
    },
    {
        "command": "editor.action.insertSnippet",
        "args": {
            "snippet": "##### ${TM_SELECTED_TEXT}"
        },
        "key": "ctrl+5", // whatever you like
        "when": "editorTextFocus && editorLangId == 'markdown'"
    },
    {
        "command": "editor.action.insertSnippet",
        "args": {
            "snippet": "###### ${TM_SELECTED_TEXT}"
        },
        "key": "ctrl+6", // whatever you like
        "when": "editorTextFocus && editorLangId == 'markdown'"
    },
    {
        "command": "editor.action.insertSnippet",
        "args": {
            "snippet": "[${TM_SELECTED_TEXT}]()"
        },
        "key": "ctrl+shift+l", // whatever you like
        "when": "editorTextFocus && editorLangId == 'markdown'"
    },
    {
        "command": "editor.action.insertSnippet",
        "args": {
            "snippet": "_${TM_SELECTED_TEXT}_"
        },
        "key": "ctrl+shift+i", // whatever you like
        "when": "editorTextFocus && editorLangId == 'markdown'"
    },
    {
        "command": "editor.action.insertSnippet",
        "args": {
            "snippet": "__${TM_SELECTED_TEXT}__"
        },
        "key": "ctrl+shift+b", // whatever you like
        "when": "editorTextFocus && editorLangId == 'markdown'"
    },
    {
        "command": "editor.action.insertSnippet",
        "args": {
            "snippet": "__*${TM_SELECTED_TEXT}*__"
        },
        "key": "ctrl+shift+q", // whatever you like
        "when": "editorTextFocus && editorLangId == 'markdown'"
    },
    {
        "command": "editor.action.insertSnippet",
        "args": {
            "snippet": "<p class=\"header\">\n\t${TM_SELECTED_TEXT}\n</p><hr class=\"header\">"
        },
        "key": "ctrl+shift+h", // whatever you like
        "when": "editorTextFocus && editorLangId == 'markdown'"
    },
    {
        "command": "editor.action.insertSnippet",
        "args": {
            "snippet": "~~${TM_SELECTED_TEXT}~~"
        },
        "key": "ctrl+shift+r", // whatever you like
        "when": "editorTextFocus && editorLangId == 'markdown'"
    },
    {
        "command": "editor.action.insertSnippet",
        "args": {
            "snippet": "<mark>${TM_SELECTED_TEXT}</mark>"
        },
        "key": "ctrl+shift+m", // whatever you like
        "when": "editorTextFocus && editorLangId == 'markdown'"
    },
    {
        "command": "editor.action.insertSnippet",
        "args": {
            "snippet": "```text\n${TM_SELECTED_TEXT}\n```"
        },
        "key": "ctrl+shift+`", // whatever you like
        "when": "editorTextFocus && editorLangId == 'markdown'"
    },
    {
        "command": "editor.action.insertSnippet",
        "args": {
            "snippet": "~~${TM_SELECTED_TEXT}~~"
        },
        "key": "alt+`", // whatever you like
        "when": "editorTextFocus && editorLangId == 'markdown'"
    },
    {
        "command": "editor.action.insertSnippet",
        "args": {
            "snippet": "+++ ${TM_SELECTED_TEXT}\n\n+++"
        },
        "key": "ctrl+shift+d",
        "when": "editorTextFocus && editorLangId == 'markdown'"
    },
    {
        "command": "editor.action.insertSnippet",
        "args": {
            "snippet": "for(auto ${TM_SELECTED_TEXT}) {\n\t\n}"
        },
        "key": "ctrl+shift+q", // q for quick
        "when": "editorTextFocus && editorLangId == 'cpp'"
    },
    {
        "command": "editor.action.joinLines",
        "key": "ctrl+shift+j",
        "when": "editorLangId == 'markdown'"
    },
    {
        "key": "ctrl+m s",
        "command": "-extension.updateMarkdownSections",
        "when": "editorTextFocus && editorLangId == 'markdown'"
    },
    {
        "key": "ctrl+m t",
        "command": "-extension.updateMarkdownToc",
        "when": "editorTextFocus && editorLangId == 'markdown'"
    },
    {
        "key": "ctrl+k ctrl+w",
        "command": "workbench.action.closeEditorsInOtherGroups"
    },
    {
        "key": "ctrl+k ctrl+w",
        "command": "workbench.action.closeOtherEditors"
    },
    {
        "key": "ctrl+shift+alt+right",
        "command": "workbench.action.moveEditorToNextGroup"
    },
    {
        "key": "ctrl+alt+right",
        "command": "-workbench.action.moveEditorToNextGroup"
    },
    {
        "key": "ctrl+shift+alt+left",
        "command": "workbench.action.moveEditorToPreviousGroup"
    },
    {
        "key": "ctrl+alt+left",
        "command": "-workbench.action.moveEditorToPreviousGroup"
    },
    {
        "key": "ctrl+shift+pageup",
        "command": "workbench.action.moveEditorLeftInGroup"
    },
    {
        "key": "ctrl+shift+pageup",
        "command": "-workbench.action.moveEditorLeftInGroup"
    },
    {
        "key": "ctrl+shift+pagedown",
        "command": "workbench.action.moveEditorRightInGroup"
    },
    {
        "key": "ctrl+shift+pagedown",
        "command": "-workbench.action.moveEditorRightInGroup"
    },
    {
        "key": "ctrl+alt+d",
        "command": "editor.debug.action.toggleBreakpoint",
        "when": "debuggersAvailable && disassemblyViewFocus || debuggersAvailable && editorTextFocus"
    },
    {
        "key": "f9",
        "command": "-editor.debug.action.toggleBreakpoint",
        "when": "debuggersAvailable && disassemblyViewFocus || debuggersAvailable && editorTextFocus"
    },
    {
        "key": "ctrl+t",
        "command": "extension.translate",
        "when": "editorTextFocus && editorLangId == 'markdown'"
    },
    {
        "key": "ctrl+shift+t",
        "command": "-extension.translate",
        "when": "editorTextFocus && editorLangId == 'markdown'"
    },
]
```