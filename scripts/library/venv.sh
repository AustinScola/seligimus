#!/bin/bash

set -eu

function _make_venv() {
    local VENV_PATH="$1"
    python3 -m venv --clear "${VENV_PATH}"
}

function _activate_venv() {
    source "${VENV_PATH}/bin/activate"
}

function _install_requirements() {
    local REQUIREMENTS_FILE_NAME="$1"
    local REQUIREMENTS_FILE_PATH="${SELIGIMUS}/requirements/${REQUIREMENTS_FILE_NAME}"
    python3 -m pip install -r "${REQUIREMENTS_FILE_PATH}"
}

function get_venv_name_from_requirements_file() {
    local REQUIREMENTS_FILE_PATH="$1"
    local REQUIREMENTS_FILE_NAME="$(basename "${REQUIREMENTS_FILE_PATH}")"
    local VENV_NAME="$( echo "${REQUIREMENTS_FILE_NAME}" | cut --delimiter=_ --fields=1)"
    echo "${VENV_NAME}"
}

function get_venv_path() {
    local VENV_NAME="$1"
    local VENV_PATH="${SELIGIMUS}/venvs/${VENV_NAME}"
    echo "${VENV_PATH}"
}

function use_clean_venv() {
    local VENV_NAME="$1"
    local REQUIREMENTS_FILE_NAME="$2"

    local VENV_PATH="$(get_venv_path "${VENV_NAME}")"

    _make_venv "${VENV_PATH}"
    _activate_venv "${VENV_PATH}"
    _install_requirements "basic_requirements.txt"
    _install_requirements "${REQUIREMENTS_FILE_NAME}"
}
