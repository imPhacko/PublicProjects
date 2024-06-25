#!/bin/bash

FILENAME="generated_data.out"

HELP_DEFAULT="Usage: bash ex4.sh [option]

Specify your option:
    fast    Fast generation
    slow    Slow generation"


# check for no or incorrect number of arguments
if [ $# -eq 0 ] || [ $# -ge 2 ]; then
    echo "${HELP_DEFAULT}"
    exit
fi

# slow and accurate
go_slow()
{
    #CSV header
    echo "n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14,n15,n16" > ${FILENAME}
    
    while [ `stat -c "%s" ${FILENAME}` -l 1000000 ]; do
        LINE="${RANDOM}"
        for i in {1..15}; do
            LINE=${LINE}",${RANDOM}"
        done
        echo "${LINE}" >> ${FILENAME}
    done
}

# fast and dirty
go_fast()
{
    #CSV header
    echo "n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14,n15,n16" > ${FILENAME}
    
    GENERATE=true
    SAFETY_COUNTER=0
    while ${GENERATE}; do
        LINE="${RANDOM}"
        for i in {1..15}; do
            LINE=${LINE}",${RANDOM}"
        done
        echo "${LINE}" >> ${FILENAME}
        
        if [ $((SAFETY_COUNTER % 1000)) -eq 0 ]; then
            if [ `stat -c "%s" ${FILENAME}` -ge 1000000 ]; then
                GENERATE=false
            fi
        fi
        SAFETY_COUNTER=$((SAFETY_COUNTER + 1))
    done
}

# parse the arguments
case "$1" in
fast)
    touch ${FILENAME}
    go_fast
    ;;
slow)
    touch ${FILENAME}
    go_slow
    ;;
help)
    echo "${HELP_DEFAULT}"
    ;;
*)
    echo "Unrecognized option. Type help."
    ;;
esac
