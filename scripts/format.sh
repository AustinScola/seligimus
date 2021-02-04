#!/bin/bash

set -eu

HERE="$(dirname "$(readlink -f "$BASH_SOURCE")")"
SELIGIMUS="$(realpath "${HERE}/..")"

pushd "${SELIGIMUS}" > /dev/null
trap "popd > /dev/null" EXIT

python3 -m yapf -i -r .
python3 -m isort .
