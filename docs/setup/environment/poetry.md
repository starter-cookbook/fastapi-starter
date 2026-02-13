---
title: Using Poetry
parent: Environment
nav_order: 2
---

# Using Poetry to manage your Python environment

Details how to set up a Python environment using Poetry.

{: .note }
Poetry is an alternative to pip+venv for dependency management in your Python environment. One of its benefits is being able to organize the packages you install versus dumping all dependencies into a single file that does not indicate the packages you manually installed.

For the latest on installing and using Poetry visit the official web site [python-poetry.org](https://python-poetry.org/)

## Installation

1. Start with your base Python dev container or install
2. Install Poetry
    1. If you are using a VSCode Dev Container you can add the following to your `devcontainer.json`

    ```json
    "postCreateCommand": "curl -sSL https://install.python-poetry.org | python3 -"
    ```

    1. This will install Poetry after your dev container is created or recreated.  Alternatively you can install Poetry manually.
    2. See the official Poetry site for updated install instructions.

## Initial project set up

```bash
# cd into your project directory
poetry init
```

This will take you through project config and creates `pyproject.toml` based on input.

If your source files are in a subfolder like `app` then tell `poetry` where the package is by adding this to the bottom of the `pyproject.toml`

```toml
[tool.poetry]
packages = [
    {include = "app"}
]
```

## Basic workflow

1. cd into your project directory
2. Install dependencies with `poetry install`
3. Optionally activate the virtual env
4. Make changes, add packages
5. Run your app
6. Commit and push changes according to your source control workflow.

{: .warning }
When using Poetry you should in general not use `pip`. Using pip to install packages will install them to your global system unless you have activated the Poetry environment.  Even if you have the Poetry virtual environment active Poetry won't track and update it's `pyproject.toml` and `poetry.lock` files if you use `pip`

## Adding a package

```bash
poetry add package_name
```

Example: `poetry add fastapi[all]`

Poetry will write the package dependency to the `pyproject.toml`

## Install dependencies

You would do this when you do an initial repo clone or when you want to install your dependences.

```bash
poetry install
```

## Run app

It depends on your app.  The following is an example for a FastAPI app.

```bash
poetry run uvicorn app.main:app --reload
```

{: .note }
If you activate the virtual env you do no need to type `poetry run`

```bash
# Activate the env then run
uvicorn app.main:app --reload
```

## Activate virtual env

Without activating the virtual env you need to run commands through `poetry`.  For example `poetry run python hello.py` or `poetry run uvicorn....`

Activating the virtual env will allow you to run `python hello.py`

This is a shortcut to activate the env

```bash
eval $(poetry env activate)
```

This is an explanation of what it is doing.

```bash
# Shows the command to activate the env
poetry env activate
# Then you copy that command and run it
# It will look something like this
# source /home/vscode/.cache/pypoetry/virtualenvs/project-name-aBc123-py3.12/bin/activate
# After running that the env is activated
which python
# Should show you are using the python in the virtual env
# So doing eval $(poetry env activate) evaluates the source command that env activate outputs
```

### Deactivate the env

```bash
deactivate
```

## View Poetry environment info

```bash
poetry install
poetry env info
```

This shows where your venv is located.  Useful if you need to tell your IDE/editor which python to use. Under `Virtualenv` and next to `Executable` you can see the path that ends with `/bin/python`.  That's the python your Poetry environment uses.


## Common Poetry commands

### Version

```bash
poetry --version
```

### Add a package

```bash
poetry add package-name
```

### Install dependencies

Installs dependencies from lock file.

```bash
poetry install
```

### See Poetry env info

```bash
# list
poetry env list

# see everything
poetry env info

# see just the virtual environment path
# useful in telling VSCode which python to use
poetry env info --path
```

### Activate env

```bash
eval $(poetry env activate)
```

#### Deactivate env

```bash
deactivate
```

### Delete the env

This can be useful if you want to wipe the env and install all packages again.

```bash
# list the envs
poetry env list
# remove the env, replace project-name-id-py3.12 with actual env name
poetry env remove project-name-id-py3.12
```
