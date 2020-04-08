# Ramachandran

[![Build Status](https://img.shields.io/travis/simonholmes001/amino_acid_feature_extraction.svg)](https://travis-ci.com/simonholmes001/amino_acid_feature_extraction)
[![docs](https://readthedocs.org/projects/amino-acid-feature-extraction/badge/?version=latest)](https://amino-acid-feature-extraction.readthedocs.io/en/latest/?badge=latest)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/simonholmes001/amino_acid_feature_extraction/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/simonholmes001/amino_acid_feature_extraction/?branch=master)
[![Build Status](https://scrutinizer-ci.com/g/simonholmes001/amino_acid_feature_extraction/badges/build.png?b=master)](https://scrutinizer-ci.com/g/simonholmes001/amino_acid_feature_extraction/build-status/master)
[![Code Intelligence Status](https://scrutinizer-ci.com/g/simonholmes001/amino_acid_feature_extraction/badges/code-intelligence.svg?b=master)](https://scrutinizer-ci.com/code-intelligence)
[![license](https://img.shields.io/pypi/l/sphinx_rtd_theme.svg)](https://pypi.python.org/pypi/sphinx_rtd_theme/)

* MIT license

# Contents

- [To Do](#todo)
- [Objectives](#objectives)
- [Data Sources & Collection](#data)
- [Requirements & Pre-Requisites](#requirements)
- [Introduction](#introduction)
- [Set-up & Usage](#set_up)

## <a name="todo"></a> To Do

-[ ] Finish README

-[ ] Update badges

-[ ] Pre-processing

-[ ] Adjacency matrix

-[ ] Save pytorch tensors as pickle objects

-[ ] Preprocessing on large data sets

-[ ] Unit tests

-[ ] Model development

-[ ] Training

-[ ] Hyperparameter optimization

-[ ] Evaluation

## <a name="objectives"></a> Objectives

This project aims to analyse the statistical distribution of dihedral angles for each of the amino acids present in the
protein entries of the **Protein Data Bank** [PDB](https://www.rcsb.org) (database downloaded as of Jan 2020).

## <a name="data"></a> Data Sources & Collection

This project uses data from the [Protein Data Base](https://www.rcsb.org/). To download the entire PDB, the following script
should be run from the command line:

```bash
rsync -rlpt -v -z --delete --port=33444 \
rsync.rcsb.org::ftp_data/structures/divided/mmCIF/ ./mmCIF
```
Downloading the entire PDB data base will take approx 2 1/2 days & will require 43.94 GB of disk space.

Running these scripts will download a number of folders, with each folder containing a number of gzip files.
These files contain the experimentally determined 3D coordinate structures of various proteins. In addition to the x-, y-
& z-atomic coordinates, the files contain metadata explaining the experimental design, structural resolution, author information,
and a number of other items pertaining to the 3D structure determination. The files are in a `.cif` format (Crystallographic Information File).

A small sample of the PDB can be downloaded from [here](http://bit.ly/2Qv1seW).

## <a name="requirements"></a> Requirements & Pre-Requisites

This project was developed in python3.7. All other requirements are installed via the creation
of a conda virtual environment when the `create_database.sh` script is run.

Other pre-requisites include running the <a name="features"></a> [amino_acid_feature_extraction repo](https://github.com/simonholmes001/amino_acid_feature_extraction) (which
itselfs runs scrips from the [pubchem_api repo](https://github.com/simonholmes001/pubchem_api)) & the [protein_structure repo](https://github.com/simonholmes001/structure_prediction).

To run the [amino_acid_feature_extraction repo](https://github.com/simonholmes001/amino_acid_feature_extraction), run `git clone https://github.com/simonholmes001/amino_acid_feature_extraction.git`
from the command line, `cd` into the repo & run the command `bash -i feature_extraction.sh`. Running
this command will generate a number of files in a folder called `output/`. The file called <a name="above"></a>`standardised_features.csv` should be copied to the
folder containing the [protein_structure repo](https://github.com/simonholmes001/structure_prediction), as per the instructions in the [README](https://github.com/simonholmes001/structure_prediction/blob/master/README.md).

To run the [protein_structure repo](https://github.com/simonholmes001/structure_prediction), run `git clone https://github.com/simonholmes001/structure_prediction.git`
from the command line, `cd` into the repo & run the command `bash -i create_datasets.sh [YOUR_FOLDER_CONTAING_PDB_FILES] [NAME_OF_TEMPORARY_STORAGE_FOLDER]` after following
the instructions presented in teh [README](https://github.com/simonholmes001/structure_prediction/blob/master/README.md) file.

The data required for this project are located in the `structure_prediction/output/final_final_features/` folder.

## <a name="Introduction"></a> Introduction

### Dihedral (Torsion) Angles



## <a name="set_up"></a> Set-up & Usage

### Repo Set-Up

The repo should be downloaded by running <a name="below"></a>`git clone https://github.com/simonholmes001/structure_prediction.git`
in the command line. `cd` into the newly created `structure_prediction` folder & copy
the `standardised_features.csv` file from [above](#above) into the repo.
Create also a folder to hold the PDB folders - in this example, this folder shall be called `pdb/`. The simplfied
folder structure should now look like this:

```
structure_prediction
    |- pdb/
    |   |- folders containting pdb.cif.gz files
    |- structure_prediction/
    |   |- scripts to run the project
    |- tests/
    |- create_datasets.sh
    |- environment.yml
    |- README.md
    |- standardised_features.csv
```

### Pre-Processing

To run the preprocessing phase of the project, `cd` into the repo and run the
following command from the terminal:

`bash -i create_datasets.sh [YOUR_FOLDER_CONTAING_PDB_FILES] [NAME_OF_TEMPORARY_STORAGE_FOLDER]`

In this example, this would mean running the following command:

`bash -i create_datasets.sh pdb temporary`

The `pdb` flag directs the script to look for the downloaded PDB files in a folder called `pdb/`.
The `temporary` flag indicates to the script a folder location to store data temporarily.

Running this command will perform the following events:

- Create a conda virtual environment for the dependencies, based on the `environment.yml` file
- Unpacks the pdb.cif.gz files to pdb.cif files & stores the pdb.cif files in a temporary folder called `extracted_data/`
- Deletes the `pdb/` folder to tidy folder structure & remove no longer necessary files. If you want to keep a copy of the PDB downloaded data, it is highly recommended to make a copy out of the `structure_prediction` folder as after the unpacking, the initial `pdb/` folder will get deleted to save space
- Extracts the alpha Carbon x-, y-, z-atomic coordinate information from the pdb.cif files (for more explanations, see [TBD](#proteins))
- Removes any empty files, such as DNA or RNA submissions
- Creates adjacency matrices for each protein
- Merges the adjacency matrices with the amino acid features obtained [here](#features)
- Transfers the adjacency matrices & merged adjacency_feature matrices to a folder called `output/`
- Deletes all of the other temporary folders

### Alpha Carbon Coordinate data

### Adjacency Matrices

### Amino Acid Features

## Model Training

### Progress

-[x] Pre-processing

-[x] Adjacency matrix

-[x] Save pytorch tensors as pickle objects

-[ ] Preprocessing on large data sets

-[ ] Unit tests

-[ ] Model development

-[ ] Training

-[ ] Hyperparameter optimization

-[ ] Evaluation

# Background

The PDB curates the largest collection of experimentally determined 3D protein structures.

### Command line tools for downloading the protein data base (PDB) dataset

See:
- http://www.wwpdb.org/ftp/pdb-ftp-sites

To download coordinate files in PDB Exchange Format using the macromolecular Crystallographic Information File (mmCIF) run the following commands:


```bash

rsync -rlpt -v -z --delete --port=33444 \
rsync.rcsb.org::ftp_data/structures/divided/mmCIF/ ./mmCIF
```
Downloading the entire PDB data base will take approx 2 1/2 days & will require 43.94 GB of disk space.

### Data Items Describing Atomic Positions

See:
- http://mmcif.wwpdb.org/docs/tutorials/content/atomic-description.html

### Data Items Describing Molecular Entities

See:
- http://mmcif.wwpdb.org/docs/tutorials/content/molecular-entities.html

### Introduction to PDB Format

See:
- https://www.cgl.ucsf.edu/chimera/docs/UsersGuide/tutorials/pdbintro.html
