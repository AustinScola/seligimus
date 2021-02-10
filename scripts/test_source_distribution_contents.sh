#!/bin/bash

set -eu

NEWLINE=$'\n'

HERE="$(dirname "$(readlink -f "$BASH_SOURCE")")"
SELIGIMUS="$(realpath "${HERE}/..")"
DISTRIBUTION_DIRECTORY="${SELIGIMUS}/dist"

# Find all source distributions in the distribution directory.
VERSION_FILE="${SELIGIMUS}/VERSION.txt"
VERSION="$(cat "${VERSION_FILE}")"
SOURCE_DISTRIBUTION="${DISTRIBUTION_DIRECTORY}/seligimus-${VERSION}.tar.gz"

if ! [[ -a "${SOURCE_DISTRIBUTION}" ]]; then
    echo "ERROR: Expected the source distribution to be located at at '${SOURCE_DISTRIBUTION}' but"\
         "it was not there."
    exit 1
fi

echo "Found source distribution '${SOURCE_DISTRIBUTION}'."

# Get a list of files in the source distribution.
contents="$(tar --list --file ${SOURCE_DISTRIBUTION})"

# Sort the contents.
contents=$(echo "${contents}" | sort -t "/")

# Create a list of the files expected to be in the source distribution.
expected_contents=""

# Add the Python files in the seligimus package to the list of expected contents.
PYTHON_FILES="$(find "${SELIGIMUS}/seligimus" -type f -name "*.py" -printf "seligimus/%P\n")"
expected_contents+="${PYTHON_FILES}"

# Add the readme to the list of expected contents.
expected_contents+=$'\nREADME.md'

# Add the version file to the list of expected contents.
expected_contents+=$'\nVERSION.txt'

# Add the license file to the list of expected contents.
expected_contents+=$'\nLICENSE.txt'

# Add files used for building distributions to the list of expected contents.
expected_contents+=$'\nscripts/build.sh'
expected_contents+=$'\nscripts/library/venv.sh'
expected_contents+=$'\nrequirements/basic_requirements.txt'
expected_contents+=$'\nrequirements/build_requirements.txt'
expected_contents+=$'\nsetup.py'
expected_contents+=$'\nsetup.cfg'

# Add the egg info files to the list of expected contents.
expected_contents+=$'\nseligimus.egg-info/dependency_links.txt'
expected_contents+=$'\nseligimus.egg-info/PKG-INFO'
expected_contents+=$'\nseligimus.egg-info/SOURCES.txt'
expected_contents+=$'\nseligimus.egg-info/top_level.txt'

# Add the manifest to the list of expected contents.
expected_contents+=$'\nMANIFEST.in'

# Add the package info to the list of expected contents.
expected_contents+=$'\nPKG-INFO'

# Add all the parent directories for each file.
directories=""
while read expected_file ; do
    parent_directory=""
    IFS=/ read -ra path_parts <<< "${expected_file}"

    # The last part is the file name so remove this.
    unset path_parts[-1]

    for subdirectory in "${path_parts[@]}"; do
        parent_directory+="${subdirectory}/"
        directories+="${NEWLINE}${parent_directory}"
    done

done <<< "${expected_contents}"
expected_contents+="${NEWLINE}${directories}"

# Sort the expected contents.
expected_contents=$(echo "${expected_contents}" | sort --unique --field-separator "/")

# Add the leading directory to the expected contents.
expected_contents="$(echo "${expected_contents}" | sed "s/^/seligimus-${VERSION}\//")"

# Compare the list of files in the source distribution to the expected list.
diff <(echo "${contents}" ) <(echo "${expected_contents}")
