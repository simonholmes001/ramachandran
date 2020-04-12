import numpy as np
import pandas as pd
import csv

# Development of matching amino acid labels to psi angles

psi_data_path = '../dihedral'
amino_acid_data_path = '../../structure_prediction/output/final_features'
name = '1j5u'
alphabet = 'ALA','ARG','ASN','ASP','CYS','GLN','GLU','GLY','HIS','ILE','LEU','LYS','MET','PHE','PRO','SER','THR','TRP','TYR','VAL'
char_to_int = dict((c, i) for i, c in enumerate(alphabet))
int_to_char = dict((i, c) for i, c in enumerate(alphabet))

with open(amino_acid_data_path +'/' + name + '_amino_acid_tag_.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
amino_acid_list = []
for i in data:
    amino_acid_list.append(i[0])
# print(amino_acid_list)

amino_acid_encoded = [char_to_int[char] for char in amino_acid_list]

with open(psi_data_path + '/' + name + '_psi.pickle', 'rb') as labels_file:
    psi_df = pd.read_pickle(labels_file)
    psi_array = np.array(psi_df)
# print(psi_array)

del amino_acid_encoded[-1]

print("amino acid list: {}".format(len(amino_acid_list)))
print("amino acid encoded: {}".format(len(amino_acid_encoded)))
print("psi_array: {}".format(len(psi_array)))

amino_psi_array = np.column_stack([amino_acid_encoded, psi_array])
print("Amino Psi Array: {}".format(amino_psi_array))
# print("Length amino_psi array: {}".format(len(amino_psi)))
# print("Type amino_psi: {}".format(type(amino_psi)))
