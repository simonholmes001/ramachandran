#!/usr/bin/env bash

# Script to pack the output files

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
