import os
import concurrent.futures
from tqdm import tqdm
from phi_angles import PhiDihedralAngleStatistics

import argparse

parser = argparse.ArgumentParser(description='To set to the path to the data')
parser.add_argument('-i', '--input_directory', help='An input directory for the psi angles must be named', required=True)
parser.add_argument('-a', '--amino_acid_input', help='An input directory for the amino acid tags must be named', required=True)

args = parser.parse_args()

phi_data_path = args.input_directory
amino_acid_data_path = args.amino_acid_input

# psi_data_path = '../dihedral_coordinates'
# amino_acid_data_path = '../../structure_prediction/output/final_features'
def main(phi_data_path, amino_acid_data_path):
    for root, dirs, files in os.walk(phi_data_path, topdown=False):
        for name in tqdm(files):
            if 'phi' in name:
                phi = PhiDihedralAngleStatistics(phi_data_path, amino_acid_data_path, name.split('_')[0])
                phi.get_amino_acid_array()
                phi.encode()
                phi.get_phi()
                phi.check_length()
                phi.combine_amino_acid_phi()
                phi.save_phi_angles()

if __name__ == '__main__':
    main(phi_data_path, amino_acid_data_path)
