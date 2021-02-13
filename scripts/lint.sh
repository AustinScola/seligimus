#!/bin/bash

set -eu

HERE="$(dirname "$(readlink -f "$BASH_SOURCE")")"
SELIGIMUS="$(realpath "${HERE}/..")"

cd "${SELIGIMUS}"

source "${SELIGIMUS}/scripts/library/venv.sh"
use_venv "test" frozen_test_requirements.txt

find . \( -path ./venvs -o -path ./build \) -prune -false -o -name "*.py" | xargs python3 -m pylint
