import csv
import os
from datetime import datetime
from pathlib import Path


class NoDataError(Exception):
    pass


def get_data_folder():
    """ Retrieve folder with datasets """
    return os.path.join(os.path.dirname(__file__), "data")


class CsvFile:
    """ Read and store data """

    def __init__(self, filepath=None, data=None):
        self.filepath = filepath
        self.data = data

    def read(self) -> dict:
        """ Read data from csv file """
        if not self.filepath:
            self.filepath = os.path.join(get_data_folder(), 'dataset0_Python+P7.csv')
        all_data = {}
        with open(self.filepath, newline='') as csvfile:
            dataset = csv.reader(csvfile, delimiter=',', quotechar='|')
            next(dataset, None)  # skip the headers
            for rows in dataset:
                all_data[rows[0]] = {
                    'price': float(rows[1]),
                    'profit': float(rows[2])
                }
        return all_data

    def write(self):
        """ Write data to csv file """
        if not self.data:
            raise NoDataError('No data provided. Cannot read data')
        else:
            if not self.filepath:
                downloads_path = str(Path.home() / "Downloads")
                self.filepath = f'{downloads_path}_results{datetime.now()}.csv'
            with open(self.filepath, 'w', newline='') as csvfile:
                dataset = csv.writer(csvfile, delimiter=' ',
                                     quotechar='|', quoting=csv.QUOTE_MINIMAL)
                for wallet in self.data:
                    for item in wallet:
                        dataset.writerow(item)
