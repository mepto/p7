import csv
import os
import time
from datetime import timedelta

from menu import Menu


def get_data_folder():
    """ Retrieve folder with datasets """
    return os.path.join(os.path.dirname(__file__), "data")


class CsvFile:
    """ Read and store data """

    def __init__(self, dataset, tup=False):
        self.tuple = tup
        self.filepath = os.path.join(get_data_folder(), dataset)

    def read(self) -> dict:
        """ Read data from csv file """

        if self.tuple:
            all_data = []
        else:
            all_data = {}

        with open(self.filepath, newline='') as csvfile:
            dataset = csv.reader(csvfile, delimiter=',', quotechar='|')
            next(dataset, None)  # skip the headers
            for rows in dataset:
                action = rows[0]
                cost = round(float(rows[1]), 2)
                profit = round(float(rows[2]), 2)
                actual_profit = round(float(rows[1]) * (float(rows[2]) / 100), 2)

                if self.tuple:
                    all_data.append(
                        (
                            action,
                            int(cost * 100),
                            int(profit * 100),
                            int(cost * (profit / 100) * 100)
                        ),
                    )
                else:
                    all_data[action] = {
                        'price': cost,
                        'profit': profit,
                        'actual_profit': actual_profit
                    }

        if not self.tuple:
            raw_data = dict(reversed(sorted(all_data.items(), key=lambda x: x[1]['price'])))
        else:
            raw_data = list(reversed(sorted(all_data, key=lambda x: x[1])))
        return raw_data


def timer(func):
    def inner(*args, **kwargs):
        start = time.time()
        f = func(*args, **kwargs)
        end = time.time()
        Menu.timer(timedelta(seconds=end - start))
        return f
    return inner
