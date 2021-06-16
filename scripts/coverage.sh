#!/bin/bash

set -eu

HERE="$(dirname "$(readlink -f "$BASH_SOURCE")")"
SELIGIMUS="$(realpath "${HERE}/..")"

cd "${SELIGIMUS}"

source "${SELIGIMUS}/scripts/library/venv.sh"
use_venv "coverage" frozen_coverage_requirements.txt

python3 -m pytest --cov=seligimus --cov-report term-missing
