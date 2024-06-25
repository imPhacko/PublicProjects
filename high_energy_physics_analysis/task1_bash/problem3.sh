#!/bin/bash

HELP_DEFAULT="Usage: bash ex3.sh [option] [value]

Specify your option:
    branch, -b      Name of output branch
    commitn, -cn    Checkout to a given commit number
    date, -d        Checkout to a given date
                        format: YYYY-MM-DD hh:mm:ss"


# parse several arguments
COMMIT_HASH=""
BRANCH_NAME=""
while [ ! $# -eq 0 ]; do
    case "$1" in
    branch|-b)
        BRANCH_NAME="${2}"
        shift 2
        ;;
    commitn|-cn)
        COMMIT_HASH=`git rev-list --all --reverse | \
                        awk 'FNR == '${2}' {print}'`
        shift 2
        ;;
    date|-d)
        COMMIT_HASH=`git rev-list \
                        -n 1 \
                        --first-parent \
                        --before="${2} ${3}" \
                        master`
        shift 3
        ;;
    help|-h)
        echo "${HELP_DEFAULT}"
        exit
        ;;
    *)
        echo "Unrecognized option. Type help."
        exit
        ;;
    esac
done

# check for errors
if [ "${COMMIT_HASH}" = "" ]; then
    echo "Incorrect options or commit not found"
    exit
fi

if [ "${BRANCH_NAME}" = "" ]; then
    echo "No new branch has been specified"
    exit
fi

# deliver the desired effect
git branch ${BRANCH_NAME} ${COMMIT_HASH}
