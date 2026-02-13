# fastapi-sample
Basic sample to set up a FastAPI app

## Uses

* Python 3.12+
* [UV](https://docs.astral.sh/uv/)
* [FastAPI](https://fastapi.tiangolo.com/)

## Initial set up

Initial set. Does not need to be done again.

### Created VSCode Dev Container for Python3

* This is done via VSCode's "Add Dev Container Configuration Files..." action
* Chose "Python 3" container with version `bullseye 3.12`
* Added `"postCreateCommand": "curl -LsSf https://astral.sh/uv/install.sh | sh"` to install UV
* Reopen folder in the Dev Container
    * This will take a while on first creation

### Init the project with UV

```bash
# while in project root
uv init
```

### Initial dependencies

```bash
uv add fastapi[all]
# fastapi[all] installs all of fastAPI, including requests and uvicorn.  You can exclude [all] but then you'd install each package as needed.
```

This also creates a `.venv` if it doesn't exist.

## Setting up from repo clone

This is how to set up the project if you are doing a fresh clone of the repo

### Clone and run app

1. Clone repo
2. cd into project directory
3. Open the repo folder in VSCode
    * VSCode should ask you want to open it in a Dev Container, select yes
4. Copy `example.env` to `.env`
    * See `Environment variables` section for more details
5. Install dependencies with `uv sync`
6. Run the app with `uv run uvicorn app.main:app --reload`

### VSCode Python Selection

Tell VSCode to use the correct Python interpreter.  If you use the wrong python your .py files will show errors because the packages may not be installed to that environment.

1. `ctrl` + `shift` + `p` and start to type: `Python: Select Interpreter"
    * alternatively open a `.py` file and at the bottom right there should be a python version displayed.  Click that and you can choose which python to use.
2. Choose the one in your `.venv` folder.
    * If it's not available you can find the path using `uv run which python` the path ends with `/bin/python`.  That's the python uv is using.  Enter the entire path.
    * You need to do `uv` command first so it creats the `.venv`
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
