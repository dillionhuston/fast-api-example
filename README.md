# FastAPI Example

## Overview

This repo contains a simple FastAPI example along with standard Poetry setup, as well as Mypy static type checking, code formatting and linting with ruff
and security linting with bandit.

## Running the API

To run the project, ensure you have [Poetry](https://python-poetry.org) installed, then, from the terminal:

```bash
poetry install
poetry run fastapi dev src/app.main.py
```

Once the API is running, make a request:

```bash
$ curl http://127.0.0.1:8000

# Outputs:
# {"Hello":"World"}

$ curl http://127.0.0.1:8000/items/1234?query=somequery

# Outputs
# {"item_id":1234,"query":"somequery"}
```

## Running Code Quality Checks

To run the project's default code quality checks, ensure you have [Task](https://taskfile.dev) installed, the from the terminal:

```bash
$ task code-quality-checks

# Outputs:
# [task] Running mypy static type checking
# Success: no issues found in 2 source files
# [task] Running ruff code formatting
# 2 files already formatted
# [task] Running ruff code linting
# All checks passed!
# [task] Running bandit security linting
```

## Build a Deployable Artifact

To build the API into a Python wheel which can deployed to a server/cloud hosting envrinment etc., from the terminal:

```bash
poetry build
```

This will create a `dist` folder in the root containing a `.whl` file, and a `.tar.gz` file. The wheel can either be
pushed to a package repository or used directly if applicable.

## Run the API on a Server

Assuming the package has either been deployed to the server or pushed to a package respository, ensure the server is
running an appropriate version of Python and use pip to install the API package:

```bash
# From wheel
pip install </path/to/api/.whl>

# From package manager
pip install fast-api-example
```

Finally, invoke the API startup script (see `tool.poetry.scripts` in `pyproject.toml`):

```bash
api-start
```
