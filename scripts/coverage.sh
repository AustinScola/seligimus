#!/bin/bash

set -eu

HERE="$(dirname "$(readlink -f "$BASH_SOURCE")")"
SELIGIMUS="$(realpath "${HERE}/..")"

cd "${SELIGIMUS}"

source "${SELIGIMUS}/scripts/library/venv.sh"
use_clean_venv_from_frozen_requirements "test" frozen_test_requirements.txt

python3 -m pytest --cov=seligimus --cov-report term-missing
