#!/usr/bin/env bash

# Copyright (c) 2017-2025 Postgres Professional

set -eux

# prepare python environment
VENV_PATH="/tmp/testgres_venv"
rm -rf $VENV_PATH
python -m venv "${VENV_PATH}"
export VIRTUAL_ENV_DISABLE_PROMPT=1
source "${VENV_PATH}/bin/activate"

# Codestyle is checked
pip install flake8 flake8-pyproject
flake8
pip uninstall -y flake8 flake8-pyproject

# Functional is tested
pip install pytest pytest-xdist
python -m pytest -l -v -n 4

set +eux
