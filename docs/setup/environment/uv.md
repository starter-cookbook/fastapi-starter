---
title: Using UV
parent: Environment
nav_order: 1
---

Details how to set up a Python evironment using UV.

For the latest on UV installation and use visit the official site.

## Official site

[docs.astral.sh/uv/](https://docs.astral.sh/uv/)

## Install

Start with a base Python environment then install UV.

{: .note }
UV will install Python when you run `uv venv` even if you do not have Python installed.  UV is able to manage Python installs and versions.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

If you are using a VSCode Dev Container you can run this command in the `postCreateCommand` of your `devcontainer.json` or you can run it manually after the container is built.

```json
"postCreateCommand": "curl -LsSf https://astral.sh/uv/install.sh | sh"
```

## Initial project set up

```bash
# cd into your project directory then
uv init
```

This will create a `pyproject.toml`, `.python-version` and `main.py`.

## Workflow

1. Install all dependencies with `uv sync`
2. Make changes, add packages, etc
3. Run app with `uv run ...`.  Example: `uv run uvicorn app.main:app --reload`
4. Commit and push updates according to your source control workflow

{: .note }
You do not need to activate a virtual environment.  As long as you use the `uv` command it will handle that for you.

## Common commands

### Version

```bash
uv --version
```

### Init

```bash
# cd into your project directory then
uv init
```

### Create .venv

uv will create the `.venv` folder as needed so you do not need to create it, but you can if you want to recreate it.

```bash
uv venv
```

You can also activate the venv with `source .venv/bin/activate`, but you do not need to do this if you are using the uv command.  You would do this if you wanated to run the app without the `uv run` command.

### Install all dependencies

```bash
uv sync
```

### Install package

```bash
uv add package-name
```

#### Install from requirements.txt

```bash
uv add -r requirements.txt
```

{: .warning }
This will install all packages in the `requirements.txt` as you added them with the `add` command. So all package will appear in the pyproject.toml.

### Remove package

```bash
uv remove package-name
```

### Update UV

```bash
# if you installed it using the installer script
uv self update
```

If you installed it another way (pip, winget, homebrew, etc) then use the original install method to udpate UV.

### See dependency tree

```bash
uv tree
```

