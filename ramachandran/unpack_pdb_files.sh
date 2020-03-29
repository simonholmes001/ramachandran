#!/usr/bin/env bash

# Script to unpack the PDB.cif.gz files

#echo $*

cd ./$*
pwd # in /ramachandran/data
for dir in */
do
    echo $dir
    cd ${dir}
    pwd # in ramachandran/data/10 etc
    for file in ./*
    do
        echo $file
        gzip -d ${file}
    done
    for cif in ./*
    do
        echo $cif
        mv $cif ../
    done
    cd ../
done
pwd # in /ramachandran/data

mkdir extracted_data
# Add in stepwise movement of files for entire PDB otherwise script fails as mv command too much
#mv 0*.cif extracted_data
#mv 1*.cif extracted_data
#mv 2*.cif extracted_data
#mv 3*.cif extracted_data
#mv 4*.cif extracted_data
#mv 5*.cif extracted_data
#mv 6*.cif extracted_data
#mv 7*.cif extracted_data
#mv 8*.cif extracted_data
#mv 9*.cif extracted_data
mv *.cif extracted_data
mv extracted_data ../
cd ../
rm -rf $*
pwd # in /ramachandran/
