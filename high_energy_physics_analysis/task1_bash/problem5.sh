#!/bin/bash

IN_FILENAME="generated_data.out"
OUT_FILENAME="masses.out"

E=10
X=3
Y=2
Z=1
M=0
CALCULATE_M()
{
    E2=`echo $E | awk '{print sqrt($1**2)}'`
    XYZ2=`echo $X $Y $Z | awk '{print sqrt($2**2 + $3**2 + $4**2)}'`
    COMP=`echo $E2 $XYZ2 | awk '{ print ($1 < $2) ? "true" : "false" }'`
    if [ ${COMP} = "true" ]; then
        M=0
    else
        M=`echo $E2 $XYZ2 | awk '{ print (sqrt($1 - $2))}'`
    fi
}

# CSV header, flushing a preexisting file
echo "M1,M2,M3,M4" > ${OUT_FILENAME}

# going after quadruples line by line
for ln in `cat ${IN_FILENAME} | awk 'FNR>=2'`; do
    E=`echo $ln | awk 'BEGIN {FS=","} {print $1}'`
    X=`echo $ln | awk 'BEGIN {FS=","} {print $2}'`
    Y=`echo $ln | awk 'BEGIN {FS=","} {print $3}'`
    Z=`echo $ln | awk 'BEGIN {FS=","} {print $4}'`
    CALCULATE_M
    PRINT="$M"
    
    E=`echo $ln | awk 'BEGIN {FS=","} {print $5}'`
    X=`echo $ln | awk 'BEGIN {FS=","} {print $6}'`
    Y=`echo $ln | awk 'BEGIN {FS=","} {print $7}'`
    Z=`echo $ln | awk 'BEGIN {FS=","} {print $8}'`
    CALCULATE_M
    PRINT="${PRINT},$M"
    
    E=`echo $ln | awk 'BEGIN {FS=","} {print $9}'`
    X=`echo $ln | awk 'BEGIN {FS=","} {print $10}'`
    Y=`echo $ln | awk 'BEGIN {FS=","} {print $11}'`
    Z=`echo $ln | awk 'BEGIN {FS=","} {print $12}'`
    CALCULATE_M
    PRINT="${PRINT},$M"
    
    E=`echo $ln | awk 'BEGIN {FS=","} {print $13}'`
    X=`echo $ln | awk 'BEGIN {FS=","} {print $14}'`
    Y=`echo $ln | awk 'BEGIN {FS=","} {print $15}'`
    Z=`echo $ln | awk 'BEGIN {FS=","} {print $16}'`
    CALCULATE_M
    PRINT="${PRINT},$M"

    echo ${PRINT} >> ${OUT_FILENAME}
done
