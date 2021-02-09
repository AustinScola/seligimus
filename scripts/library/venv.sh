#!/bin/bash

set -eu

function _make_venv() {
    VENV="$1"
    rm -rf "${VENV}"
    python3 -m venv "${VENV}"
}

function _activate_venv() {
    source "${VENV}/bin/activate"
}

function _install_requirements() {
    REQUIREMENTS_FILE="$1"
    REQUIREMENTS_PATH="${SELIGIMUS}/requirements/${REQUIREMENTS_FILE}"
    python3 -m pip install -r "${REQUIREMENTS_PATH}"
}

function use_venv() {
    VENV_NAME="$1"
    REQUIREMENTS_FILE="$2"

    VENV="${SELIGIMUS}/venvs/${VENV_NAME}"

    _make_venv "${VENV}"
    _activate_venv "${VENV}"
    _install_requirements "${REQUIREMENTS_FILE}"
}
