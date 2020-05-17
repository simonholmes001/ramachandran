import numpy as np
import pandas as pd
import pickle

class ConcatenateStatistics:

    def __init__(self, input_path, output_path, name, angle, pickle_list):
        self.input_path = input_path
        self.output_path = output_path
        self.name = name
        self.angle = angle
        self.pickle_list = pickle_list

    def open_file_save_csv(self, pickle_list):
        try:
            with open(self.input_path + '/' + self.name.split('_')[0] + '_amino_' + self.angle + '_.pickle', 'rb') as labels_file:
                data_file = pickle.load(labels_file)
                self.pickle_list.append(data_file)
        except:
            pass

        return self.pickle_list

    def concatenate_csv(self):
        concat_df = np.concatenate((self.pickle_list))
        print(concat_df)
        print(concat_df.shape)
        dataframe = pd.DataFrame(concat_df)
        print(dataframe.head())
        print(dataframe.tail())
        print(dataframe.shape)

        dataframe.to_csv(self.output_path + self.angle + '_all_proteins.csv', encoding='utf-8', index=False, header=None)
