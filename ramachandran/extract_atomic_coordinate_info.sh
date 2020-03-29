#!/bin/bash

# Script to extract atomic coordinates from the PDB.cif files

echo $*
mkdir ./$*

cd ./extracted_data

list="$(find . -name '*.cif')"
for file in $list
do
	TARGET=$(echo "${file##*/}")
	grep "^ATOM.*\|^MODEL" ${TARGET} > ../$*/$TARGET
done
