import csv
import os
from pathlib import Path
from datetime import datetime


class NoDataError(Exception):
    pass


def get_data_folder():
    return os.path.join(os.path.dirname(__file__), "data")


class CsvFile:
    """ Read and store data """

    def __init__(self, filepath=None, data=None):
        self.filepath = filepath

        self.data = data

    def read(self):
        if not self.filepath:
            self.filepath = os.path.join(get_data_folder(), 'dataset0_Python+P7.csv')
        all_data = []
        with open(self.filepath, newline='') as csvfile:
            dataset = csv.reader(csvfile, delimiter=' ', quotechar='|')
            next(dataset, None)  # skip the headers
            for row in dataset:
                all_data.append(row)
        return all_data

    def write(self):
        if not self.data:
            raise NoDataError('No data provided. Cannot read data')
        else:
            if not self.filepath:
                downloads_path = str(Path.home() / "Downloads")
                self.filepath = f'{downloads_path}_results{datetime.now()}.csv'
            with open(self.filepath, 'w', newline='') as csvfile:
                dataset = csv.writer(csvfile, delimiter=' ',
                                     quotechar='|', quoting=csv.QUOTE_MINIMAL)
                for item in self.data.keys():
                    csvfile.write("%s,%s\n" % (item, self.data[item]))
