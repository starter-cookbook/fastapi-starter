---
title: Install Python
parent: Setup
nav_order: 1
---

# Installing Python

First you need to have a Python environment.

See the official [python](https://www.python.org/) web site with up to date ways to install Python.  This guide contains general ways to get a Python environment set up.


## Install on your host machine

The most basic way to get a Python environment set up is to install it on your host machine.  Go to the official Python website and follow their guide to getting started.

Many OS installs already have Python installed.  To check, open a command line terminal and type:

```bash
python3 --version
```

or 

```bash
python --version
```

If you receive a response with a Python version you already have Python installed.

## Use a Dev Container

You can use a Dev Container to spin up a Python environment.  A Dev Container is useful if you do not want to modify your host system.  With a Dev Container you can run a containerized environment for Python.

Commonly VSCode with a Dev Container is used.  Typically it uses Docker a container, but it is also possible to use Podman.

### Install required software

1. Install [Docker](https://www.docker.com/) or [Docker Desktop](https://www.docker.com/products/docker-desktop/)
2. Install [VSCode](https://code.visualstudio.com/)
3. Install the VSCode extension [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

### Create the Dev Container

1. Using VSCode open the folder where you want to place your project files

   ```bash
   # cd into your source folder
   mkdir my-python-app
   cd my-python-app
   code .
   ```

3. Open the `Command Palette` typically `Ctrl` + `Shift` + `P`
4. Start typing `Dev Containers: Add Dev Containers Configuration Files...`
5. Select `Add configuration to workspace`
  1. This will create a `.devcontainer` folder and allow you to include your Dev Container configuration in source control.
5. Select a Dev Container `Python 3` by `devcontainers` is a basic container that can be used
6. Select the default version it offers (3.12, 3.14 or higher)
7. You can skip "Select additional features to install"
8. You can skip the step to add dependabot configuration or you can add it if you are using GitHub and want to have dependabot configuration set up.
9. VSCode may ask for permission to access files.  You must allow it to access files.
10. You should now have a `.devcontainer/devcontainer.json` in your folder.  If you opted to add dependabot configuration you should also see that file.
11. VSCode should prompt you with a message "Folder contains a Dev Container configuration file. Reopen folder to develop in a container" select "Reopen in Container" to open your folder in the Dev Container.
  1. Alternatively, if you are not prompted, click on the `><` in the bottom left of the VSCode window and select "Reopen in Container"
12. VSCode will then build the container and reopen your folder in the container.  This may take some minutes.  Click on "(show log)" to check on progress.
13.  Once VSCode completes building the container and reopens your folder in the container open the VSCode Terminal and type

  ```bash
  python --version
  which python
  ```

  You should see output similar to

  ```bash
  vscode ➜ /workspaces/my-python-app $ python --version
  Python 3.14.2
  vscode ➜ /workspaces/my-python-app $ which python
  /usr/local/bin/python
  vscode ➜ /workspaces/my-python-app $ 
  ```

14. When you close VSCode and reopen your project folder later choose to oepn it in the container.

