# VSCode Example Company Keybindings

```json
// Place your key bindings in this file to override the defaults
[
    {
        "command": "editor.action.insertSnippet",
        "args": {
            "snippet": "<u>${TM_SELECTED_TEXT}</u>"
        },
        "key": "ctrl+u", // whatever you like
        "when": "editorTextFocus && editorLangId == 'markdown'"
    },
    {
        "command": "editor.action.insertSnippet",
        "args": {
            "snippet": "# ${TM_SELECTED_TEXT}"
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
            "snippet": "**${TM_SELECTED_TEXT}**"
        },
        "key": "ctrl+shift+b", // whatever you like
        "when": "editorTextFocus && editorLangId == 'markdown'"
    },
    {
        "command": "editor.action.insertSnippet",
        "args": {
            "snippet": "_**${TM_SELECTED_TEXT}**_"
        },
        "key": "ctrl+shift+q", // whatever you like
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
        "description": "Replace all spaces in selected text with hyphens",
        "command": "editor.action.insertSnippet",
        "args": {
            "snippet": "${TM_SELECTED_TEXT/( )/-/g}"
        },
        "key": "ctrl+alt+shift+h"
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
        "key": "ctrl+shift+alt+pagedown",
        "command": "workbench.action.moveEditorToNextGroup"
    },
    {
        "key": "ctrl+shift+alt+pageup",
        "command": "workbench.action.moveEditorToPreviousGroup"
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
    {
        "key": "ctrl+shift+down",
        "command": "editor.action.copyLinesDownAction",
        "when": "editorTextFocus && !editorReadonly"
    },
    {
        "key": "ctrl+shift+up",
        "command": "editor.action.copyLinesUpAction",
        "when": "editorTextFocus && !editorReadonly"
    },
    {
        "key": "alt+backspace",
        "command": "workbench.action.reopenClosedEditor"
    },
    {
        "key": "ctrl+shift+t",
        "command": "-workbench.action.reopenClosedEditor"
    },
    {
        "key": "ctrl+shift+w",
        "command": "-workbench.action.closeWindow"
    },
    {
        "key": "ctrl+shift+pageup",
        "command": "workbench.action.moveEditorLeftInGroup"
    },
    {
        "key": "ctrl+shift+pagedown",
        "command": "workbench.action.navigateBack"
    },
    {
        "key": "shift+alt+left",
        "command": "workbench.action.navigateBack",
    },
    {
        "key": "shift+alt+right",
        "command": "workbench.action.navigateForward",
    },
    {
        "key": "ctrl+q",
        "command": "workbench.action.tasks.build",
        "when": "editorLangId == 'markdown' || editorLangId == yaml"
    },
    {
        "key": "ctrl+q",
        "command": "-workbench.action.quit"
    }
]
```