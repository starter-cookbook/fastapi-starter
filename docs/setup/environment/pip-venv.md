---
title: Using Pip + venv
parent: Environment
nav_order: 3
---

# Using Pip+venv

Details how to set up a Python environment using Pip+venv.

{: .note }
Pip and venv are available when you install Python. This means you can use this method without installing any other dependencies. This is the simplest way to manage your Python environment.

1. Starting with a basic python dev container or install
2. Create virtual environment
    ```bash
    # cd into your project directory
    python3 -m venv venv
    ```
    * Python will be in `./venv/bin/python`
        * Use that path to tell your IDE/Editor such as VSCode which python to use
3. Activate the virtual environment
    ```bash
    source venv/bin/activate
    ```
4. Install whatever you need
    ```bash
    pip install "package name"
    ```


## Basic workflow

1. cd into or open your project folder
2. Activate your venv
    1. Or create it if it does not exist. This would be the case if you are cloning a repo since the repo will usually not have a venv folder in it.
3. Install from your requirements.txt
4. Make your changes
5. Freeze your requirements if you have changed your packages and dependencies
6. Run your app
7. Commit and push changes depending on your source control workflow

## Common commands

### Activate venv

Activate the virtual environment before working on your project so that changes are reflected in the venv instead of in your host system.

You would do this any time you open your IDE/Editor.

```bash
source venv/bin/activate
```

### Freeze requirements

```bash
# after installing, updating, removing or changing a package
pip freeze > requirements.txt
```

{: .note }
Take a look at the `requirements.txt` file. You will notice that it simply lists all dependencies, including those installed when you install a package.  This is one of the "downsides" of pip+venv. Later it becomes difficult to see which packages you installed and which were installed as associated dependencies.

### Install dependencies from the requirements.txt

```bash
# activate venv first
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
