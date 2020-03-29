import os

import numpy as np
import pandas as pd
from scipy.spatial import distance
from tqdm import tqdm

import torch
import pickle

with open('../../coordinate_data/1j51.cif') as infile:
    target_list = infile.read().split('\n')
    df_1 = pd.DataFrame(data=target_list, columns=["header"])  # Put list in a dataframe m X 1 column
    df_1 = df_1[:-1] # Removes additional row that is included
    cif_to_df_2 = df_1.header.str.split(expand=True)  # Put dataframe to m x 20 columns
    assert df_1.shape[0] == cif_to_df_2.shape[0]
    critical_info_to_df_3 = cif_to_df_2.drop(columns=[0, 1, 2, 4, 6, 7, 8, 9, 13, 14, 15, 16, 17, 18, 19, 20], axis=1)  # df containing aa & coordinate positions
    assert cif_to_df_2.shape[0] == critical_info_to_df_3.shape[0]
    dihedral_coordinates_df_4 = critical_info_to_df_3.loc[critical_info_to_df_3[3].isin(['N', 'CA', 'C'])] # Select atoms for dihedral angle calculation
    print(dihedral_coordinates_df_4.head(50))




     # convert_to_array = critical_info_to_df_3.drop(columns=[5], axis=1).to_numpy() # Removes aa flag & contains only coordinate info
    # calculate_distances = distance.pdist(convert_to_array, 'euclidean')
    # make_square = distance.squareform(calculate_distances)
    # adjacency_matrix_df_4 = pd.DataFrame(make_square)
    # assert critical_info_to_df_3.shape[0] == adjacency_matrix_df_4.shape[0]
    #
    # # Save adjacency matrix to csv fie
    #
    # adjacency_matrix_df_4.to_csv('./' + self.walk_path  + '/' + name.split('.')[0] + '_adjacency_matrix_' + '.csv', encoding='utf-8', index=False, header=False)
    #
    # # Convert adjacency matrix to numpy arrays, pytorch tensor & save numpy & pickle
    #
    # # Adjacency matrix
    # adjacency_to_array = adjacency_matrix_df_4.to_numpy() # Convert to numpy array
    # adjacency_to_tensor = torch.from_numpy(adjacency_to_array) # Convert to pytorch tensor
    # with open('./' + self.walk_path + '/' + name.split('.')[0] + '_label', 'wb') as file:
    #     pickle.dump(adjacency_to_tensor, file) # Save as a pickle object
    # np.save('./' + self.walk_path + '/' + name.split('.')[0] + '_adjacency', adjacency_to_array) # Save numpy array

    # Save amino acid tags to csv file

    # amino_acid_tags_df.to_csv('./' + self.walk_path + '/' + name.split('.')[0] + '_amino_acid_tag_' + '.csv', encoding='utf-8', index=False, header=False)


    # df_join = pd.concat([critical_info_to_df_3, adjacency_matrix_df_4], axis=1, join='inner')  # Join the databases
    # assert adjacency_matrix_df_4.shape[0] == df_join.shape[0]
    # df_join_2 = df_join.drop(columns=[10, 11, 12], axis=1) # Remove original coordinate information
    # assert df_join.shape[0] == df_join_2.shape[0]
