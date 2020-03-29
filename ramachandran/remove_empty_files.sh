#!/bin/bash

# Script to remove any empty coordinate files after extraction of coordinate information (DNA & RNA files for example)

cd ./$*

list="$(find . -name '*.cif')"
for file in $list
do
if [ -s $file ]
then
     echo "File not empty"
else
     rm $file
fi
done


