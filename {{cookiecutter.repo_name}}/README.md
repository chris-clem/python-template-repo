# {{cookiecutter.repo_name}}

TODO: addd GitHub Actions Badge
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Setup

1. Create a fresh Python 3.7 environment with [Conda](https://docs.conda.io/projects/conda/en/latest/)
```bash
conda create -n {{cookiecutter.repo_name}} python=3.7
conda activate {{cookiecutter.repo_name}}
```

2. Install dependencies with [Poetry](https://python-poetry.org)
Install Poetry by following the install instructions for your OS on their [website](https://python-poetry.org/docs/#installation). Then run the following commands to install the dependecies:
```bash
poetry install
```

3. Install [pre-commit](https://pre-commit.com) hooks from `.pre-commit-config.yaml`
```bash
pre-commit install
```

4. Run the tests
```bash
poetry run pytest
```

## Run {{cookiecutter.script_name}}
```bash
poetry run {{cookiecutter.script_name}}
```