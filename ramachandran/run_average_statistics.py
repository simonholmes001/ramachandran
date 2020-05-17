import os
from tqdm import tqdm
from average_statistics_over_all_proteins import ConcatenateStatistics

import argparse

parser = argparse.ArgumentParser(description='To set to the path to the data')
parser.add_argument('-i', '--input_path', help='An input path where the angles are located', required=True)
parser.add_argument('-o', '--output_path', help='An output path to save the statistics', required=True)
parser.add_argument('-a', '--angle', help='The angle statistics being collected', required=True)

args = parser.parse_args()

input_path = args.input_path
output_path = args.output_path
angle = args.angle

def main(input_path, output_path, angle, pickle_list):
    for root, dirs, files in os.walk(input_path, topdown=False):
        for name in tqdm(files):
            if angle in name:
                concat = ConcatenateStatistics(input_path, output_path, name.split('_')[0], angle, pickle_list)
                concat.open_file_save_csv(pickle_list)
    concat.concatenate_csv()

if __name__ == '__main__':
    pickle_list = []
    main(input_path, output_path, angle, pickle_list)
    print(len(pickle_list))
