import os
import pandas as pd
import numpy as np
import csv
import pickle

"""
When structure_prediction & ramachandran are run on PDB entry 1a11
See: https://stackoverflow.com/questions/25355401/getting-all-dihedral-angles-in-pymol
"""

# Activate code when 1a11_amino_psi_.pickel file is available to test results

# with open('../output/1a11_amino_psi_.pickle', 'rb') as labels_file:
#         psi_df = pd.read_pickle(labels_file)
#         psi_array = np.array(psi_df)
#         psi_degrees = np.rad2deg(psi_array)
#
# with open('../output/1a11_amino_phi_.pickle', 'rb') as labels_file:
#     phi_df = pd.read_pickle(labels_file)
#     phi_array = np.array(phi_df)
#     phi_degrees = np.rad2deg(phi_array)
#
# for i in range(0,20):
#     print("psi {}: {}".format(i, psi_degrees[i]))
#
# for i in range(0,20):
#     print("phi {}: {}".format(i, phi_degrees[i]))
