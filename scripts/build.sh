#!/bin/bash

set -eu

HERE="$(dirname "$(readlink -f "$BASH_SOURCE")")"
SELIGIMUS="$(realpath "${HERE}/..")"

pushd "${SELIGIMUS}" > /dev/null
trap "popd > /dev/null" EXIT

python3 setup.py sdist bdist_wheel

rm -rf seligimus.egg-info build