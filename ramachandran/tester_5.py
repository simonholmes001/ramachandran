import os
import pandas as pd
import numpy as np
import csv
import pickle

with open('../output/1j5a_amino_psi_.pickle', 'rb') as labels_file:
        psi_df = pd.read_pickle(labels_file)
        psi_array = np.array(psi_df)

with open('../output/1j5a_amino_phi_.pickle', 'rb') as labels_file:
    phi_df = pd.read_pickle(labels_file)
    phi_array = np.array(phi_df)

for i in range(0,5):
    print("psi {}: {}".format(i, psi_array[i]))
    print("phi {}: {}".format(i, phi_array[i]))
