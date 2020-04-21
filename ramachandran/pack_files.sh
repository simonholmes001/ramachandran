#!/usr/bin/env bash

# Script to pack the output files

# Check for required arguments
if [ $# -ne 2 ]; then
    echo "usage: $0 You must enter an argument corresponding to PDB folder to process" 1>&2
    echo Exiting script...
    exit 1
fi


cd $1
pwd
for file in */
do
    for file in ./*
    do
        echo $file
        gzip ${file}
    done
    for gz in ./*
    do
        mv $gz $2
    done
    cd ../
done
pwd
