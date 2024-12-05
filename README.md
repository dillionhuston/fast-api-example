# FastAPI Example

## Overview

This repo contains a simple FastAPI example along with standard Poetry setup, as well as Mypy static type checking, code formatting and linting with ruff
and security linting with bandit.

## Running the API

To run the project, ensure you have [Poetry](https://python-poetry.org) installed, then, from the terminal:

```bash
poetry install
poetry run fastapi dev src/fast_api_example/main.py
```

Once the API is running, make a request:

```bash
$ curl http://127.0.0.1:8000
{"Hello":"World"}

$ curl http://127.0.0.1:8000/items/1234?query=somequery
{"item_id":1234,"query":"somequery"}
```

## Running Code Quality Checks

To run the project's default code quality checks, make sure to install the configured pre-commit hooks, then run them.
After this, any commit to the repo will trigger the pre-commit hooks (if needed, this can be pypasses by adding the
`--no-verify` flag to the commit, but avoid this wherever possible).

```bash
$ pre-commit install
$ pre-commit run --all-files

Mypy static type checking................................................Passed
Ruff code linting........................................................Passed
Ruff code formatting.....................................................Passed
Bandit security linting..................................................Passed
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

For details on more advanced aspects of deployment (e.g., HTTPS) and alternate deployment
approaches, see the [FastAPI deployment docs](https://fastapi.tiangolo.com/deployment/).
