import os
from tqdm import tqdm
from phi_statistics import CollectStatistics

# import argparse
#
# parser = argparse.ArgumentParser(description='To set to the path to the data')
# parser.add_argument('-i', '--input_directory', help='An input directory for the psi angles must be named', required=True)
# parser.add_argument('-a', '--amino_acid_input', help='An input directory for the amino acid tags must be named', required=True)
#
# args = parser.parse_args()
#
# phi_data_path = args.input_directory
# amino_acid_data_path = args.amino_acid_input

input_path = '/media/simon/disk/protein_folding/phi_angles'
output_path = '/media/simon/disk/protein_folding/phi_angle_statistics'

def main(input_path, output_path):
    for root, dirs, files in os.walk(input_path, topdown=False):
        for name in tqdm(files):
            if 'phi' in name:
                phi_stats = CollectStatistics(input_path, output_path, name.split('_')[0])
                phi_stats.open_files()
                phi_stats.collect_statistics()
                phi_stats.save_phi_statistics()

if __name__ == '__main__':
    main(input_path, output_path)
