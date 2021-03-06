import os
from tqdm import tqdm
from psi_angles import PsiDihedralAngleStatistics

import argparse

parser = argparse.ArgumentParser(description='To set to the path to the data')
parser.add_argument('-i', '--input_directory', help='An input directory for the psi angles must be named', required=True)
parser.add_argument('-a', '--amino_acid_input', help='An input directory for the amino acid tags must be named', required=True)

args = parser.parse_args()

psi_data_path = args.input_directory
amino_acid_data_path = args.amino_acid_input

# psi_data_path = '../dihedral'
# amino_acid_data_path = '../../structure_prediction/output/final_features'
def main(psi_data_path, amino_acid_data_path):
    for root, dirs, files in os.walk(psi_data_path, topdown=False):
        for name in tqdm(files):
            if 'psi' in name:
                psi = PsiDihedralAngleStatistics(psi_data_path, amino_acid_data_path, name.split('_')[0])
                psi.get_amino_acid_array()
                psi.encode()
                psi.get_psi()
                psi.check_length()
                psi.combine_amino_acid_psi()
                psi.save_psi_angles()

if __name__ == '__main__':
    main(psi_data_path, amino_acid_data_path)
