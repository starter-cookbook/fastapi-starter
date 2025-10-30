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

### Initial dependencies

```bash
poetry add fastapi[all]
```

This creates the `poetry.lock` and also updates `pyproject.toml`

3. Create virtual environment
    ```bash
    python3 -m venv venv
    ```
4. Activate virtual environment
    ```bash
    source venv/bin/activate
    ```
5. Install FastAPI
    ```bash
    pip install "fastapi[all]"
    ```
    * This will also install other things like uvicorn
    * If an error occurs due to a `wheel` error install `wheel`
        ```bash
        pip install wheel
        ```
6. Freeze requirements
    ```bash
    pip freeze > requirements.txt
    ```

## Setting up from repo clone

This is how to set up the project if you are doing a fresh clone of the repo

1. Clone repo
2. cd into project directory
3. Open the repo folder in VSCode
    * VSCode should ask you want to open it in a Dev Container, select yes
4. Create a virtual environment
    ```bash
    python3 -m venv venv
    ```
5. Activate the venv
    ```bash
    source venv/bin/activate
    ```
    * Check you are in the venv
        ```bash
        which python && which pip
        # should display /venv/bin/python and venv/bin/pip
        ```
6. Optionally add an alias to your bashrc to activate venv easier
    ```bash
    # in ~/.bashrc add the following
    alias start_venv=`source venv/bin/activate`
    ```
7. Install dependencies from the requirements.txt
    ```bash
    pip install -r requirements.txt
    ```
8. Tell VSCode to use the correct Python interpreter
    1. `ctrl` + `shift` + `p`
    2. Start to type: `Python: Select Interpreter"
    3. Choose `./venv/bin/python`
        * If it's not available choose `Enter interpreter path...` then enter `./venv/bin/python`
    4. When you are on a `.py` file you should be able to see the interpreter being used in the lower right of VSCode
9. Set up env vars - see `Environment variables` section


## Environment varialbles

1. Copy `example.env` to `.env`
2. Fill out the `.env` values as needed

Note that you can also just create the env varables at the OS or container level.  For example in the `~/.bash_profile` but it's not recommended.

## Freeze requirements

Do this when a package is added

```bash
pip freeze > requirements.txt
```

## Install requirements

Do this when you need to install requirements.  Usually this is when you do a clean clone or when requirements.txt has been changed by someone else.

```bash
pip install -r requirements.txt
```

## Updating pip

If you need to update pip

```bash
# activate venv
pip install --upgrade pip
```

## Deactivate venv

Shouldn't need to do this, but if you need to it can be done with

```bash
deactivate
```

## Run app

```bash
# run app locally and reload on code changes
uvicorn app.main:app --reload
# the app will run under http://127.0.0.1:8000
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

### Activate shell

Note that this is mainly if you want to run `python` commands directly.  Poetry installs packages to an isolated environment regardless of whether you activate shell.

```bash
poetry shell
# now you can do python run instead of poetry python run
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
