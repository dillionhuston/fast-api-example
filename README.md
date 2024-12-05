# FastAPI Example

[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)
[![Linting: Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)

## Overview

This repo contains a simple [FastAPI](https://fastapi.tiangolo.com) example along with standard Poetry setup, as well as [Mypy](https://github.com/python/mypy) static type checking,
code formatting and linting with [Ruff](https://github.com/astral-sh/ruff) and security linting with [Bandit](https://github.com/PyCQA/bandit). All
code quality checks are facilitated using [pre-commit](https://github.com/pre-commit/pre-commit) hooks.

## Running the API

To run the project, ensure you have Python 3.11 installed (ideally via [Pyenv](https://github.com/pyenv/pyenv)), as welll as [Poetry](https://github.com/python-poetry/poetry), then, from the terminal run:

```bash
poetry install
poetry run fastapi dev src/fast_api_example/main.py
```

Once the API is running, make a request:

```bash
curl http://127.0.0.1:8000
{"Hello":"World"}

curl http://127.0.0.1:8000/items/1234?query=somequery
{"item_id":1234,"query":"somequery"}
```

## Running Code Quality Checks

To run the project's default code quality checks, make sure to install the configured pre-commit hooks, then run them, after which
any commit to the repo will trigger the hooks:

```bash
poetry run pre-commit install
poetry run pre-commit run --all-files

Mypy static type checking................................................Passed
Ruff code linting........................................................Passed
Ruff code formatting.....................................................Passed
Bandit security linting..................................................Passed
```

If needed, hooks can be pypasses by adding the `--no-verify` flag to the commit, but avoid this wherever possible.

## Build a Deployable Artifact

To build the API into a Python wheel which can deployed to a server/cloud hosting envrinment, from the terminal simply run:

```bash
poetry build
```

This will create a `dist` folder in the root containing a `.whl` file, and a `.tar.gz` file. The wheel can either be
pushed to a package repository or used directly if applicable.

## Run the API on a Server

Assuming the package has either been deployed to the server or pushed to a package respository, and that an appropriate Python version is installed, create a virtual environment and install the wheel/package:

```bash
python -m venv. venv
source .venv/bin/activate

# From wheel
pip install </path/to/api/.whl>

# From package manager
pip install fast-api-example
```

Finally, invoke the API startup script (see `tool.poetry.scripts` in `pyproject.toml`):

```bash
api-start

INFO:     Started server process [15561]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

For details on more advanced aspects of deployment (e.g., HTTPS) and alternate deployment
approaches, see the [FastAPI deployment docs](https://fastapi.tiangolo.com/deployment/).
