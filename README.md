# fastapi-sample
Basic sample to set up a FastAPI app

## Uses

* Python 3.12+
* [FastAPI](https://fastapi.tiangolo.com/)


## Useful commands

```bash
# activate virtual environment (venv) for python
source venv/bin/activate

# run app
uvicorn app.main:app --reload
```

## Initial set up

Initial set. Does not need to be done again

1. Create VSCode Dev Container for Python3
    * This is done via VSCode's "Add Dev Container Configuration Files..." action
    * Chose "Python 3" container with version `bullseye 3.12`
2. Reopen folder in the Dev Container.
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


