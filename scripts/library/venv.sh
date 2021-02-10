#!/bin/bash

set -eu

function _make_venv() {
    local VENV="$1"
    python3 -m venv --clear "${VENV}"
}

function _activate_venv() {
    source "${VENV}/bin/activate"
}

function _install_requirements() {
    local REQUIREMENTS_FILE="$1"
    local REQUIREMENTS_PATH="${SELIGIMUS}/requirements/${REQUIREMENTS_FILE}"
    python3 -m pip install -r "${REQUIREMENTS_PATH}"
}

function get_venv_path() {
    local VENV_NAME="$1"
    local VENV_PATH="${SELIGIMUS}/venvs/${VENV_NAME}"
    echo "${VENV_PATH}"
}

function use_venv() {
    local VENV_NAME="$1"
    local REQUIREMENTS_FILE="$2"

    local VENV="${SELIGIMUS}/venvs/${VENV_NAME}"

    _make_venv "${VENV}"
    _activate_venv "${VENV}"
    _install_requirements "basic_requirements.txt"
    _install_requirements "${REQUIREMENTS_FILE}"
}
