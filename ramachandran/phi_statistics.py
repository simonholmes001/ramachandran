import numpy as np
import pandas as pd
import pickle

input_path = '/media/simon/disk/protein_folding/phi_angles'
output_path = '/media/simon/disk/protein_folding/phi_angle_statistics'

class CollectStatistics:

    def __init__(self, input_path, output_path, name):
        self.input_path = input_path
        self.output_path = output_path
        self.name = name

    def open_files(self):
            with open(self.input_path + '/' + self.name + '_amino_phi_.pickle', 'rb') as labels_file:
                try:
                    self.phi_df = pd.read_pickle(labels_file)
                except:
                    pass
            try:
                return self.phi_df
            except:
                pass

    def collect_statistics(self):

        self.results = []

        try:
            # self.results.append("Data for {}".format(self.name))
            for i in set(self.phi_df[:,0]):
                mask = (self.phi_df[:,0] == i)
                test_data = self.phi_df[mask]
                mean = test_data[:,1].mean().round(5)
                # std = test_data[:,1].std().round(2)
                # median = np.median(test_data[:,1]).round(2)
                # max = test_data[:,1].max().round(2)
                # min = test_data[:,1].min().round(2)
                self.results.append("{}: ".format(i))
                self.results.append(mean)
                # self.results.append(std)
                # self.results.append(median)
                # self.results.append(max)
                # self.results.append(min)
            self.results_array = np.array(self.results)
        except:
            pass
        try:
            return self.results_array
        except:
            pass

    def save_phi_statistics(self):
        with open(self.output_path + '/' + self.name.split('_')[0] + '_phi_statistics.pickle', 'wb', buffering=500000000) as file:
            try:
                pickle.dump(self.results_array, file, protocol=4) # Save as a pickle object
            except:
                print(self.name)
                pass
