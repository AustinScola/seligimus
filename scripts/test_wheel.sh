#!/bin/bash

set -eu

HERE="$(dirname "$(readlink -f "$BASH_SOURCE")")"
SELIGIMUS="$(realpath "${HERE}/..")"
DISTRIBUTION="${SELIGIMUS}/dist"

# Find all wheel files in the distribution directory.
WHEEL_FILES=$(find "${DISTRIBUTION}" -maxdepth 1 -name "*.whl")

# Determine the number of wheel files.
NUMBER_OF_WHEELS="$(echo "${WHEEL_FILES}" | wc -l )"

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

VENV="${SELIGIMUS}/venvs/wheel_testing"

# Remove the virtual environment if it already exists.
rm -rf "${VENV}"

# Create a virtual environment to install the wheel file in.
python3 -m venv "${VENV}"

# Activate the virtual environment.
source "${VENV}/bin/activate"

# Install the wheel in the virtual environment.
python3 -m pip install ${WHEEL_FILE}

# Install the testing dependencies in the virtual environment.
python3 -m pip install -r "${SELIGIMUS}/requirements/test_requirements.txt"

# Go to the tests directory. Note that if we went to the root Seligimus directory then the the code 
# would be used in testing instead of installed wheel (and we wouldn't actually be testing the
# wheel).
pushd "${SELIGIMUS}/tests" > /dev/null
trap "popd > /dev/null" EXIT

# Verify that the installed Seligmus is being used when running Python.
SELIGIMUS_PATH=$(python3 -c 'from pathlib import Path; import seligimus; print(Path(seligimus.__file__).parent)')

if ! [[ "${SELIGIMUS_PATH}" =~ ^"${VENV}".* ]]; then
    echo "ERROR: The wheel-installed Seligimus is not being used from Python. Instead the path to"\
        "Seligimus is '${SELIGIMUS_PATH}'."
    exit 1
else
    echo "Inside the virtual environment, the path to Seligimus is '${SELIGIMUS_PATH}'."
fi

# Run the Python tests against the Seligimus package installed from the wheel.
python3 -m pytest
