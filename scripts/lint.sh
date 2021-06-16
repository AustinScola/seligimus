#!/bin/bash

set -eu

HERE="$(dirname "$(readlink -f "$BASH_SOURCE")")"
SELIGIMUS="$(realpath "${HERE}/..")"

cd "${SELIGIMUS}"

source "${SELIGIMUS}/scripts/library/venv.sh"
use_venv "lint" frozen_lint_requirements.txt

find . \( -path ./venvs -o -path ./build \) -prune -false -o -name "*.py" | xargs python3 -m pylint -j 0 --output-format=colorized
