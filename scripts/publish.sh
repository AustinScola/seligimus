#!/bin/bash

set -eu

HERE="$(dirname "$(readlink -f "$BASH_SOURCE")")"
SELIGIMUS="$(realpath "${HERE}/..")"
DISTRIBUTION_DIRECTORY="${SELIGIMUS}/dist"

VERSION_FILE="${SELIGIMUS}/VERSION.txt"
VERSION="$(cat "${VERSION_FILE}")"

WHEEL="${DISTRIBUTION_DIRECTORY}/seligimus-${VERSION}-py3-none-any.whl"
SOURCE_DISTRIBUTION="${DISTRIBUTION_DIRECTORY}/seligimus-${VERSION}.tar.gz"

# Check that the API token has been provided.
set +u
if [[ -z "${PYPI_TOKEN}" ]]; then
    echo "ERROR: PyPI API token not set. Please provide it as an environment varibale."
    exit 1
fi
set -u

source "${SELIGIMUS}/scripts/library/venv.sh"
use_clean_venv_from_frozen_requirements deployment frozen_deployment_requirements.txt

python3 -m twine upload \
    --non-interactive \
    --username __token__ \
    --password "${PYPI_TOKEN}" \
    "${WHEEL}" "${SOURCE_DISTRIBUTION}"
