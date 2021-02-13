#!/bin/bash

set -eu

HERE="$(dirname "$(readlink -f "$BASH_SOURCE")")"
SELIGIMUS="$(realpath "${HERE}/..")"
DISTRIBUTION="${SELIGIMUS}/dist"

source "${SELIGIMUS}/scripts/library/string.sh"

function help() {
    echo "$0 [-h | --help | ((-w | --wheel) <wheel_file>)]"
    echo
    echo "Options:"
    echo "    -h, --help             Print help and exit"
    echo "    -w, --wheel <wheel>    Test the given wheel"
}

function parse_arguments() {
    while [[ "$#" -gt 0 ]]; do
        case "$1" in
            -h | --help)
                help
                exit
                ;;
            -w | --wheel)
                WHEEL_FILE="$2"
                shift
                ;;
            *)
                echo "ERROR: Unknown argument $1"
                help
                exit 2
                ;;
        esac
        shift
    done
}

find_wheel() {
    # Find all wheel files in the distribution directory.
    WHEEL_FILES=$(find "${DISTRIBUTION}" -maxdepth 1 -name "*.whl")

    # Determine the number of wheel files.
    NUMBER_OF_WHEELS="$(number_of_lines "${WHEEL_FILES}")"

    # Error if there is more than one wheel file.
    if [[ "${NUMBER_OF_WHEELS}" -gt 1 ]]; then
        echo "ERROR: There are ${NUMBER_OF_WHEELS} wheel files in the distribution directory"\
             "${DISTRIBUTION} and it was only expected that there would be one wheel file."
        echo
        echo "Try removing the contents of the distribution directory with 'rm -rf ${DISTRIBUTION}'"\
             "and then rebuilding with '${SELIGIMUS}/scripts/build.sh'?"
        exit 1
    fi

    WHEEL_FILE="${WHEEL_FILES}"
    echo "Found a wheel file '${WHEEL_FILE}' to test."
}

if [[ "$#" -ge 1 ]]; then
    parse_arguments "$@"
else
    find_wheel
fi

source "${SELIGIMUS}/scripts/library/venv.sh"
VENV_NAME=wheel_testing
use_clean_venv_from_frozen_requirements "${VENV_NAME}" frozen_test_requirements.txt

# Install the wheel in the virtual environment.
python3 -m pip install ${WHEEL_FILE}

# Go to the tests directory. Note that if we went to the root Seligimus directory then the the code 
# would be used in testing instead of installed wheel (and we wouldn't actually be testing the
# wheel).
cd "${SELIGIMUS}/tests"

# Verify that the installed Seligmus is being used when running Python.
SELIGIMUS_PATH=$(python3 -c 'from pathlib import Path; import seligimus; print(Path(seligimus.__file__).parent)')

VENV_PATH="$(get_venv_path "${VENV_NAME}")"
if ! [[ "${SELIGIMUS_PATH}" =~ ^"${VENV_PATH}".* ]]; then
    echo "ERROR: The wheel-installed Seligimus is not being used from Python. Instead the path to"\
        "Seligimus is '${SELIGIMUS_PATH}'."
    exit 1
else
    echo "Inside the virtual environment, the path to Seligimus is '${SELIGIMUS_PATH}'."
fi

# Run the Python tests against the Seligimus package installed from the wheel.
python3 -m pytest
