#!/bin/bash

set -eu

HERE="$(dirname "$(readlink -f "$BASH_SOURCE")")"
SELIGIMUS="$(realpath "${HERE}/..")"

cd "${SELIGIMUS}"

find . \( -path ./venvs -o -path ./build \) -prune -false -o -name "*.py" | xargs python3 -m pylint
