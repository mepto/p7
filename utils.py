import csv
import os


class NoDataError(Exception):
    pass


def get_data_folder():
    """ Retrieve folder with datasets """
    return os.path.join(os.path.dirname(__file__), "data")


class CsvFile:
    """ Read and store data """

    def __init__(self, filepath=None, data=None, with_ratio=False):
        self.filepath = filepath
        self.data = data
        self.with_ratio = with_ratio

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
                if self.with_ratio:
                    all_data[rows[0]].update({
                        'ratio': float(rows[2]) / float(rows[1])
                    })
        if self.with_ratio:
            raw_data = reversed(sorted(all_data.items(), key=lambda x: x[1]['ratio']))
        else:
            raw_data = reversed(sorted(all_data.items(), key=lambda x: x[1]['profit']))
        return dict(raw_data)


def write_results(cost, wallet, profit):
    print(f"Total cost: {cost}")
    print("Wallet:")
    print(f"{wallet}")
    print(f"Total profit: {profit}")
