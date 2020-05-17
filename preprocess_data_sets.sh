#!/usr/bin/env bash

# Script to prepare data from the downloaded PDB for the structure_prediction project

# Check for required arguments
if [ $# -ne 1 ]; then
    echo "usage: $0 You must enter an argument corresponding to PDB folder to process" 1>&0
    echo Exiting script...
    exit 1
fi

# Need to run m to q
echo $*

# Preparation of a virtual environment
echo Creating virtual environment for data preparation...
ENV=$(cat ./environment.yml | grep name | cut -f 2 -d ':')
conda update -n base conda # to update to latest version of conda
conda remove --name $ENV --all # to remove any previously installed environments called $ENV
conda activate base
conda env create -fy environment.yml
conda activate $ENV
echo Virtual environment ready

echo Starting...
mkdir data
echo Loading data sets 0 to 9
echo Loading Data 0...
cp -r /media/simon/disk/protein_folding/test_data/$*0 data
sleep 5
echo Loading Data 1...
cp -r /media/simon/disk/protein_folding/test_data/$*1 data
sleep 5
echo Loading Data 2...
cp -r /media/simon/disk/protein_folding/test_data/$*2 data
sleep 5
echo Loading Data 3...
cp -r /media/simon/disk/protein_folding/test_data/$*3 data
sleep 5
echo Loading Data 4...
cp -r /media/simon/disk/protein_folding/test_data/$*4 data
sleep 5
echo Loading Data 5...
cp -r /media/simon/disk/protein_folding/test_data/$*5 data
sleep 5
echo Loading Data 6...
cp -r /media/simon/disk/protein_folding/test_data/$*6 data
sleep 5
echo Loading Data 7...
cp -r /media/simon/disk/protein_folding/test_data/$*7 data
sleep 5
echo Loading Data 8...
cp -r /media/simon/disk/protein_folding/test_data/$*8 data
sleep 5
echo Loading Data 9...
cp -r /media/simon/disk/protein_folding/test_data/$*9 data
sleep 5

echo Running script...
bash -i create_datasets.sh data holding /media/simon/disk/protein_folding/amino_acid_tags/
sleep 5
echo Transfer data to external drives...
echo Transferring phi angle files...
cp output/*amino_phi* /media/simon/disk/protein_folding/phi_angles/
sleep 5
echo Transferring psi angle files...
cp output/*amino_psi* /media/simon/disk/protein_folding/psi_angles_2/
sleep 5

echo Starting data sets a to j

mkdir data
echo Loading DataSet a...
cp -r /media/simon/disk/protein_folding/test_data/$*a data
sleep 5
echo Loading DataSet b...
cp -r /media/simon/disk/protein_folding/test_data/$*b data
sleep 5
echo Loading DataSet c...
cp -r /media/simon/disk/protein_folding/test_data/$*c data
sleep 5
echo Loading DataSet d...
cp -r /media/simon/disk/protein_folding/test_data/$*d data
sleep 5
echo Loading DataSet e...
cp -r /media/simon/disk/protein_folding/test_data/$*e data
sleep 5
echo Loading DataSet f...
cp -r /media/simon/disk/protein_folding/test_data/$*f data
sleep 5
echo Loading DataSet g...
cp -r /media/simon/disk/protein_folding/test_data/$*g data
sleep 5
echo Loading DataSet h...
cp -r /media/simon/disk/protein_folding/test_data/$*h data
sleep 5
echo Loading DataSet i...
cp -r /media/simon/disk/protein_folding/test_data/$*i data
sleep 5
echo Loading DataSet j...
cp -r /media/simon/disk/protein_folding/test_data/$*j data
sleep 5

echo Running script...
bash -i create_datasets.sh data holding /media/simon/disk/protein_folding/amino_acid_tags/
sleep 5
echo Transfer data to external drives...
echo Transferring phi angle files...
cp output/*amino_phi* /media/simon/disk/protein_folding/phi_angles/
sleep 5
echo Transferring psi angle files...
cp output/*amino_psi* /media/simon/disk/protein_folding/psi_angles_2/
sleep 5

echo Starting DataSets k to s

mkdir data
echo Loading DataSet k...
cp -r /media/simon/disk/protein_folding/test_data/$*k data
sleep 5
echo Loading DataSet l...
cp -r /media/simon/disk/protein_folding/test_data/$*l data
sleep 5
echo Loading DataSet m...
cp -r /media/simon/disk/protein_folding/test_data/$*m data
sleep 5
echo Loading DataSet n...
cp -r /media/simon/disk/protein_folding/test_data/$*n data
sleep 5
echo Loading DataSet o...
cp -r /media/simon/disk/protein_folding/test_data/$*o data
sleep 5
echo Loading DataSet p...
cp -r /media/simon/disk/protein_folding/test_data/$*p data
sleep 5
echo Loading DataSet q...
cp -r /media/simon/disk/protein_folding/test_data/$*q data
sleep 5
echo Loading DataSet r...
cp -r /media/simon/disk/protein_folding/test_data/$*r data
sleep 5
echo Loading DataSet s...
cp -r /media/simon/disk/protein_folding/test_data/$*s data
sleep 5

echo Running script...
bash -i create_datasets.sh data holding /media/simon/disk/protein_folding/amino_acid_tags/
sleep 5
echo Transfer data to external drives...
echo Transferring phi angle files...
cp output/*amino_phi* /media/simon/disk/protein_folding/phi_angles/
sleep 5
echo Transferring psi angle files...
cp output/*amino_psi* /media/simon/disk/protein_folding/psi_angles_2/
sleep 5

echo Starting DataSets t to z
mkdir data
echo Loading DataSet t...
cp -r /media/simon/disk/protein_folding/test_data/$*t data
sleep 5
echo Loading DataSet u...
cp -r /media/simon/disk/protein_folding/test_data/$*u data
sleep 5
echo Loading DataSet v...
cp -r /media/simon/disk/protein_folding/test_data/$*v data
sleep 5
echo Loading DataSet w...
cp -r /media/simon/disk/protein_folding/test_data/$*w data
sleep 5
echo Loading DataSet x...
cp -r /media/simon/disk/protein_folding/test_data/$*x data
sleep 5
echo Loading DataSet y...
cp -r /media/simon/disk/protein_folding/test_data/$*y data
sleep 5
echo Loading DataSet z...
cp -r /media/simon/disk/protein_folding/test_data/$*z data
sleep 5

echo Running script...
bash -i create_datasets.sh data holding /media/simon/disk/protein_folding/amino_acid_tags/
sleep 5
echo Transfer data to external drives...
echo Transferring phi angle files...
cp output/*amino_phi* /media/simon/disk/protein_folding/phi_angles/
sleep 5
echo Transferring psi angle files...
cp output/*amino_psi* /media/simon/disk/protein_folding/psi_angles_2/
sleep 5

conda deactivate

echo Script completed
