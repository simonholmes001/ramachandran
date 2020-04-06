#!/usr/bin/env bash

# Script to prepare data for analysing dihedral angles in the PDB protein population

# Need to include the following cmd arguments: $1 -> folder containing the pdb.cif files;
# $2 -> storage location for the dihedral_extracted data; $3 -> location of amino acid tags

# Check for required arguments
if [ $# -ne 3 ]; then
    echo "usage: $0 You must enter the folder name of the pdb data AND the location of the coordinate files as arguments" 1>&3
    echo Exiting script...
    exit 1
fi

# Preparation of a virtual environment
echo Creating virtual environment for data preparation...
ENV=$(cat ./environment.yml | grep name | cut -f 2 -d ':')
conda update -n base conda # to update to latest version of conda
conda remove --name $ENV --all # to remove any previously installed environments called $ENV
conda activate base
conda env create -f environment.yml
conda activate $ENV
echo Virtual environment ready

rm -rf ./$2
rm -rf ./extracted_data
rm -rf ./output

echo Preparing to unpack files...
bash ./ramachandran/unpack_pdb_files.sh $1 # to unpack the pdf.cif.gz files & put all unpacked pdb.cif files in a folder called extracted_data/
echo Unpacking completed

echo Preparing to extract alpha C info...
bash ./ramachandran/extract_atomic_coordinate_info.sh $2 # to extract alpha-C coordinate information from the pdf.cif files in the extracted_data/ folder & to put them in the $2/ folder
echo Extraction complete

echo Deleting any empty coordinate files, DNA / RNA files as an example...
bash ./ramachandran/remove_empty_files.sh $2
echo Clean-up completed

echo Preparing dihedral matrix. This will take some time...
python3 ./ramachandran/create_dihedral_matrix.py -d $2
echo Dihedral matrices created

echo Preparing psi angles....
python3 ./ramachandran/run_ramachandran.py -i $2
echo Psi angles extracted

echo Matching psi angles and amino acid tags....
python3 ./ramachandran/run_psi_angles.py -i $2 -a $3
echo Psi angles and amino acid tags merged

# Create the output folder and transfer files there
mkdir ./output

cd ./$2
mv *_amino_* ../output/
cd ../
rm -rf ./$2
rm -rf ./extracted_data

conda deactivate

echo All files have been processed
echo
echo Script completed.
