import os

import pandas as pd
from tqdm import tqdm

import argparse

parser = argparse.ArgumentParser(description='To set W_PATH to the same directory that contains the coordinate data extracted from the pdb.cif files')
parser.add_argument('-o', '--output_directory', help='An output directory must be named', required=True)

args = parser.parse_args()

W_PATH = args.output_directory

class CreateDihedralMatrix:

    def __init__(self, walk_path):
        self.walk_path = walk_path

    def dihedral_angles_matrix(self):

        for root, dirs, files in os.walk('./' + self.walk_path, topdown=False):
            for name in tqdm(files):
                with open('./' + self.walk_path + '/' + name) as infile:
                    target_list = infile.read().split('\n')
                    df_1 = pd.DataFrame(data=target_list, columns=["header"])  # Put list in a dataframe m X 1 column
                    df_1 = df_1[:-1] # Removes additional row that is included
                    cif_to_df_2 = df_1.header.str.split(expand=True)  # Put dataframe to m x 20 columns
                    assert df_1.shape[0] == cif_to_df_2.shape[0]
                    critical_info_to_df_3 = cif_to_df_2.drop(columns=[0, 1, 2, 4, 6, 7, 8, 9, 13, 14, 15, 16, 17, 18, 19, 20], axis=1)  # df containing aa & coordinate positions
                    assert cif_to_df_2.shape[0] == critical_info_to_df_3.shape[0]
                    dihedral_coordinates_df_4 = critical_info_to_df_3.loc[critical_info_to_df_3[3].isin(['N', 'CA', 'C'])] # Select atoms for dihedral angle calculation

                    # Save adjacency matrix to csv fie

                    dihedral_coordinates_df_4.to_csv('./' + self.walk_path  + '/' + name.split('.')[0] + '_dihedral_matrix_' + '.csv', encoding='utf-8', index=False, header=False)

def main():
    dihedral = CreateDihedralMatrix(args.output_directory)
    dihedral.dihedral_angles_matrix()

if __name__ == '__main__':
    main()
