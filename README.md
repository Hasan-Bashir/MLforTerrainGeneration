# Machine Learning for Terrain Generation and Landscape Metrics

This project was made using [uv](https://docs.astral.sh/uv/) --- you will need to install uv to use this package. To run the code, first clone the repository locally.

## Getting Started

You will need:

- uv, a Python project and package manager built in Rust.

Recommend:
[Ruff formatting linter](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff), [mypy type checker](https://marketplace.visualstudio.com/items?itemName=ms-python.mypy-type-checker), [pytest](https://docs.pytest.org/en/stable/) for testing.

Add the following to your settings.json (Press Cmd/Ctrl+Shift+P, type settings, click Preference: Open User Settins (JSON)):

```{json}
"[python]": {
        "editor.defaultFormatter": "charliermarsh.ruff",
        "editor.codeActionsOnSave": {
            "source.fixAll": "explicit",
            "source.organizeImports": "explicit"
        },
        "editor.tabSize": 4
    },
```

Mypy type checker extension for VSCode.
I recommend enabling Format on Save in your settings for all file types.

After cloning the repo, run `uv sync` this should install all the dependencies required for the project.
