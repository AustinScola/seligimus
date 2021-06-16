#!/bin/bash

set -eu

HERE="$(dirname "$(readlink -f "$BASH_SOURCE")")"
SELIGIMUS="$(realpath "${HERE}/..")"

cd "${SELIGIMUS}"

source "${SELIGIMUS}/scripts/library/venv.sh"
use_venv format frozen_format_requirements.txt

source "${SELIGIMUS}/scripts/library/cpus.sh"
NUMBER_OF_CPUS="$(get_number_of_cpus)"

python3 -m yapf --parallel -i -r .
python3 -m isort --jobs "${NUMBER_OF_CPUS}" .
