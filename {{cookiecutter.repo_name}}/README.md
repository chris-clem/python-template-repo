# {{cookiecutter.repo_name}}

TODO: addd GitHub Actions Badge
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Setup

1. Set up Python (e.g. with Miniconda)

```bash
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
~/miniconda3/bin/conda init zsh
```

1. Install dependencies with [Poetry](https://python-poetry.org)

Install Poetry by following the install instructions for your OS on their
[website](https://python-poetry.org/docs/#installation). Then run the following
commands to install the dependecies:

```bash
poetry install
```

1. Install [pre-commit](https://pre-commit.com) hooks from `.pre-commit-config.yaml`

```bash
git init
poetry run pre-commit install
```

1. Run the tests

```bash
poetry run pytest
```

## Run {{cookiecutter.script_name}}

```bash
poetry run {{cookiecutter.script_name}}
```
