import numpy as np
import pandas as pd
import pickle

class CollectStatistics:
    """
    Collects the means of the angles in each protein for each amino acid
    """

    def __init__(self, input_path, output_path, name, angle):
        self.input_path = input_path
        self.output_path = output_path
        self.name = name
        self.angle = angle

    def open_files(self):
        with open(self.input_path + '/' + self.name + '_amino_' + self.angle + '_.pickle', 'rb') as labels_file:
            try:
                self.df = pd.read_pickle(labels_file)
            except:
                pass
        try:
            return self.df
        except:
            pass

    def collect_statistics(self):

        self.results = []

        try:
            for i in set(self.df[:,0]):
                mask = (self.df[:,0] == i)
                test_data = self.df[mask]
                mean = test_data[:,1].mean().round(5)
                self.results.append("{}: ".format(i))
                self.results.append(mean)
            self.results_array = np.array(self.results)
        except:
            pass
        try:
            return self.results_array
        except:
            pass

    def save_statistics(self):
        with open(self.output_path + '/' + self.name.split('_')[0] + '_' + angle + '_statistics.pickle', 'wb', buffering=500000000) as file:
            try:
                pickle.dump(self.results_array, file, protocol=4)
            except:
                print(self.name)
                pass
