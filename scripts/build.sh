#!/bin/bash

set -eu

HERE="$(dirname "$(readlink -f "$BASH_SOURCE")")"
SELIGIMUS="$(realpath "${HERE}/..")"

pushd "${SELIGIMUS}" > /dev/null
trap "popd > /dev/null" EXIT

python3 -m venv "${SELIGIMUS}/venv"
source "${SELIGIMUS}/venv/bin/activate"
python3 -m pip install -r "${SELIGIMUS}/requirements/build_requirements.txt"

python3 setup.py sdist bdist_wheel

rm -rf seligimus.egg-info build
