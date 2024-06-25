#!/bin/bash

HELP_DEFAULT="Usage: bash ex2.sh [option] [value]

Specify your option:
    commitn     Checkout to a given commit number
    date        Checkout to a given date
                    format: YYYY-MM-DD hh:mm:ss"


# check for no or incorrect number of arguments
if [ $# -eq 0 ] || [ $# -ge 4 ]; then
    echo "${HELP_DEFAULT}"
    exit
fi


# parse the arguments
case "$1" in
commitn)
    COMMIT_HASH=`git rev-list --all --reverse | awk 'FNR == '${2}' {print}'`
    git checkout ${COMMIT_HASH}
    ;;
date)
    COMMIT_HASH=`git rev-list -n 1 --first-parent --before="${2} ${3}" master`
    git checkout ${COMMIT_HASH}
    ;;
help)
    echo "${HELP_DEFAULT}"
    ;;
*)
    echo "Unrecognized option. Type help."
    ;;
esac
