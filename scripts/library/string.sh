#!/bin/bash

function number_of_lines() {
    local STRING="$1"
    local NUMBER_OF_LINES
    if [[ -z "${STRING}" ]]; then
        NUMBER_OF_LINES=0
    else
        NUMBER_OF_LINES="$(echo "${STRING}" | wc -l)"
    fi
    echo "${NUMBER_OF_LINES}"
}
