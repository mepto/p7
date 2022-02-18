import csv
import os


class NoDataError(Exception):
    pass


def get_data_folder():
    """ Retrieve folder with datasets """
    return os.path.join(os.path.dirname(__file__), "data")


class CsvFile:
    """ Read and store data """

    def __init__(self, filepath=None, data=None, tup=False):
        self.filepath = filepath
        self.data = data
        self.tuple = tup

    def read(self) -> dict:
        """ Read data from csv file """
        if not self.filepath:
            self.filepath = os.path.join(get_data_folder(), 'dataset0_Python+P7.csv')

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
                        'price': round(cost, 2),
                        'profit': round(profit, 2),
                        'actual_profit': round(actual_profit, 2)
                    }

        if not self.tuple:
            raw_data = dict(reversed(sorted(all_data.items(), key=lambda x: x[1]['price'])))
        else:
            raw_data = list(reversed(sorted(all_data, key=lambda x: x[1])))
        return raw_data


def write_results(cost, wallet, profit):
    """ Write information to console """
    print(f"Total cost: {cost}")
    print("Wallet:")
    print(f"{wallet}")
    print(f"Total profit: {profit}")
