# fastapi-sample
Basic sample to set up a FastAPI app

## Uses

* Python 3.12+
* [Poetry](https://python-poetry.org/)
* [FastAPI](https://fastapi.tiangolo.com/)

## Initial set up

Initial set. Does not need to be done again.

### Create VSCode Dev Container for Python3

* This is done via VSCode's "Add Dev Container Configuration Files..." action
* Chose "Python 3" container with version `bullseye 3.12`
* Add `"postCreateCommand": "curl -sSL https://install.python-poetry.org | python3 -"` to install Poetry
    * See the Poetry site for most up to date install script
    * Alternatively you can run this script in the dev container if you do not use the `postCreateCommand`
* Reopen folder in the Dev Container
    * This will take a while on first creation

### Init the project with Poetry

```bash
poetry init
```

This will take you through project config and creates `pyproject.toml` based on input.

If your source files are in a subfolder like `app` then tell `poetry` where the package is by adding this to the bottom of the `pyproject.tml`

```toml
[tool.poetry]
packages = [
    {include = "app"}
]
```

### Initial dependencies

```bash
poetry add fastapi[all]
# fastapi[all] installs all kinds of fastapi stuff, including requests and uvicorn.  You can exclude [all] but then you'd install each package as needed.
```

## Setting up from repo clone

This is how to set up the project if you are doing a fresh clone of the repo

### Clone and run app

1. Clone repo
2. cd into project directory
3. Open the repo folder in VSCode
    * VSCode should ask you want to open it in a Dev Container, select yes
4. Copy `example.env` to `.env`
    * See `Environment variables` section for more details
5. Install dependencies with `poetry install`
6. Run the app with `poetry run uvicorn app.main:app --reload`
    * If you activate the env you don't need `poetry run`

### Activate virtual env

Without activating the virtual env you need to run things through `poetry`.  For example `poetry run python hello.py` or `poetry run uvicorn....`

Activate the virtual env so you can just do `python hello.py`

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

#### Deactivate the env

```bash
deactivate
```

### VSCode Python Selection

Tell VSCode to use the correct Python interpreter.  If you use the wrong python your .py files will show errors because the packages may not be installed to that environment.

1. `ctrl` + `shift` + `p` and start to type: `Python: Select Interpreter"
    * alternatively open a `.py` file and at the bottom right there should be a python version displayed.  Click that and you can choose which python to use.
2. Choose the one created by `poetry`
    * If it's not available you can find the path using `poetry env info` under `Virtualenv` and next to `Executable` you can see the path that ends with `/bin/python`.  That's the python `poetry` uses.  Enter the entire path.
    * You need to do `poetry install` first so it creats the env
3. When you are on a `.py` file you should be able to see the interpreter being used in the lower right of VSCode

## Environment varialbles

1. Copy `example.env` to `.env`
2. Fill out the `.env` values as needed

`.env` is in the gitingore since it may contain senstive info like keys.

Note that you can also just create the env varables at the OS or container level.  For example in the `~/.bash_profile` but it's not recommended.

## Run app

```bash
# Activate the env
# run app locally and reload on code changes
uvicorn app.main:app --reload
# the app will run under http://127.0.0.1:8000
```

```bash
# If you do not activate the env you can still run the app
poetry run uvicorn app.main:app --reload
```

### Docs

FastAPI generates API docs.  Access them by going to http://127.0.0.1:8000/docs

There is also http://127.0.0.1:8000/redoc

### OpenAPI

FastAPI will also crate an OpenAPI json at http://127.0.0.1:8000/openapi.json


## Useful Poetry commands

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

## The old pip+venv way

This section is a note on the basic pip + venv way to set up the project.

You do not need this. This is only for historical reference.

1. Starting with a basic python dev container
2. Create virtual environment
    ```bash
    python3 -m venv venv
    ```
    * Python will be in `./venv/bin/python`
        * Use that path to tell VSCode which python to use
3. Activate virtual environment
    ```bash
    source venv/bin/activate
    ```
4. Install whatever you need
    ```bash
    pip install "package name"
    ```

### Freeze requirements

```bash
pip freeze > requirements.txt
```

### Install dependencies from the requirements.txt

```bash
pip install -r requirements.txt
```

### Update pip
```bash
# activate venv first
pip install --upgrade pip
```

### If you need to deactivate venv

```bash
deactivate
```
