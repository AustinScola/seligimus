#!/bin/bash

set -eu

HERE="$(dirname "$(readlink -f "$BASH_SOURCE")")"
SELIGIMUS="$(realpath "${HERE}/..")"
SCRIPTS_DIRECTORY="${SELIGIMUS}/scripts"

# Change directories to the scirpts directory.
cd "${SCRIPTS_DIRECTORY}"

# Test the contents of the source distribution match the expected contents.
./test_source_distribution_contents.sh

# Test that the source distribution can be used to build the seligimus package.
./test_building_from_source_distribution.sh
