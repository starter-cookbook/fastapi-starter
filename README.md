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
