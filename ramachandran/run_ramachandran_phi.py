import os
from ramachandran import Ramachandran
from tqdm import tqdm

import argparse

parser = argparse.ArgumentParser(description='To set to the path to the data')
parser.add_argument('-i', '--input_directory', help='An input directory must be named', required=True)

args = parser.parse_args()

data_path = args.input_directory

def main(data_path):
    for root, dirs, files in os.walk(data_path, topdown=False):
        for name in tqdm(files):
            if 'dihedral' in name:
                test_sample = name
                rama = Ramachandran(data_path, data_path + '/' + test_sample, name)
                rama.make_test_array(test_sample)
                rama.vectorise_phi()
                rama.phi()
                rama.save_phi(data_path, name)

if __name__ == '__main__':
    main(data_path)
