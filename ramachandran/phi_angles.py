import numpy as np
import pandas as pd
import csv
import pickle

# Matching amino acid labels to phi angles for each protein
# psi_data_path = '../dihedral_coordinates'
# amino_acid_data_path = '../../structure_prediction/output/final_features'

class PhiDihedralAngleStatistics:
    def __init__(self, phi_data_path, amino_acid_data_path, name):
        self.phi_data_path = phi_data_path
        self.amino_acid_data_path = amino_acid_data_path
        self.name = name

    def get_amino_acid_array(self):
        """Extracts the amino acid sequence from the _tag data"""
        self.amino_acid_list = []
        with open(self.amino_acid_data_path +'/' + self.name + '_amino_acid_tag_.csv', newline='') as f:
            self.reader = csv.reader(f)
            self.data = list(self.reader)
            for i in self.data:
                self.amino_acid_list.append(i[0])
        return self.amino_acid_list

    def encode(self):
        self.alphabet = 'ALA','ARG','ASN','ASP','CYS','GLN','GLU','GLY','HIS','ILE','LEU','LYS','MET','PHE','PRO','SER','THR','TRP','TYR','VAL', 'SEC', 'PYL', 'UNK'
        self.char_to_int = dict((c, i) for i, c in enumerate(self.alphabet))
        # int_to_char = dict((i, c) for i, c in enumerate(alphabet))
        self.amino_acid_encoded = [self.char_to_int[char] for char in self.amino_acid_list]
        return self.amino_acid_encoded

    def get_phi(self):
        with open(self.phi_data_path + '/' + self.name + '_phi.pickle', 'rb') as labels_file:
            self.phi_df = pd.read_pickle(labels_file)
            self.phi_array = np.array(self.phi_df)

    def check_length(self):
        self.delta = len(self.amino_acid_encoded) - len(self.phi_array)
        if self.delta != 0:
            del self.amino_acid_encoded[-self.delta:]
        return self.amino_acid_encoded

    def combine_amino_acid_phi(self):
        try:
            self.amino_phi_array = np.column_stack([self.amino_acid_encoded, self.phi_array])
        except:
            pass
        try:
            return self.amino_phi_array
        except:
            pass

    def save_phi_angles(self):
        try:
            with open(self.phi_data_path + '/' + self.name.split('_')[0] + '_amino_phi_.pickle', 'wb') as file:
                pickle.dump(self.amino_phi_array, file) # Save as a pickle object
        except:
            pass