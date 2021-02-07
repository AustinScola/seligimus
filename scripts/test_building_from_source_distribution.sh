#!/bin/bash

set -eu

HERE="$(dirname "$(readlink -f "$BASH_SOURCE")")"
SELIGIMUS="$(realpath "${HERE}/..")"
DISTRIBUTION_DIRECTORY="${SELIGIMUS}/dist"

# Find all source distributions in the distribution directory.
VERSION_FILE="${SELIGIMUS}/VERSION.txt"
VERSION="$(cat "${VERSION_FILE}")"
SOURCE_DISTRIBUTION="${DISTRIBUTION_DIRECTORY}/seligimus-${VERSION}.tar.gz"

if ! [[ -a "${SOURCE_DISTRIBUTION}" ]]; then
    echo "ERROR: ..."
    exit 1
fi

echo "Found source distribution '${SOURCE_DISTRIBUTION}'."

# Extract the source distribution.
BUILD_DIRECTORY="${SELIGIMUS}/build"
rm -rf "${BUILD_DIRECTORY}"
mkdir "${BUILD_DIRECTORY}"
tar -xf "${SOURCE_DISTRIBUTION}" -C "${BUILD_DIRECTORY}"

# Change directories to the extracted source distribution.
EXTRACTED_SOURCE_DIRECTORY="${BUILD_DIRECTORY}/seligimus-${VERSION}"
cd "${EXTRACTED_SOURCE_DIRECTORY}" > /dev/null

./scripts/build.sh

# Check that the contents of the source distribution built using the source distribution is equal
# to the contents of the orignal source distribution.
SOURCE_DISTRIBUTION_CONTENTS="$(tar --list --file "${SOURCE_DISTRIBUTION}")"
BUILT_SOURCE_DISTRIBUTION="${EXTRACTED_SOURCE_DIRECTORY}/dist/seligimus-${VERSION}.tar.gz"
BUILT_SOURCE_DISTRIBUTION_CONTENTS="$(tar --list --file "${BUILT_SOURCE_DISTRIBUTION}")"

if [[ "${SOURCE_DISTRIBUTION_CONTENTS}" != "${BUILT_SOURCE_DISTRIBUTION_CONTENTS}" ]]; then
    echo "ERROR: The contents of the source distribution built using the source distribution do"\
         "not match the contents of the original source distribution."
    exit 1
fi

# Test the contents of the wheel that was built using the source distribution to the contents of the
# wheel built from the repository.
WHEEL="${DISTRIBUTION_DIRECTORY}/seligimus-${VERSION}-py3-none-any.whl"
BUILT_WHEEL="${EXTRACTED_SOURCE_DIRECTORY}/dist/seligimus-${VERSION}-py3-none-any.whl"

# diff -y <(unzip -l "${WHEEL}") <(unzip -l "${BUILT_WHEEL}")
zipcmp "${WHEEL}" "${BUILT_WHEEL}"
