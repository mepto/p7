import argparse
import csv
import time
from datetime import timedelta
from pathlib import Path

MAX_COST = 500


def timer(func):
    def inner(*args, **kwargs):
        start = time.time()
        f = func(*args, **kwargs)
        end = time.time()
        print(f'Programme duration time: {timedelta(seconds=end - start)}')
        return f
    return inner


class CsvFile:
    """
    Read from csv file and return data.

    :return: list
    """
    def __init__(self, dataset):
        self.filepath = Path(dataset)
        # Check if path provided is relevant
        if not self.filepath.is_file():
            raise FileExistsError('The path provided is not to a file or the file does not exist.')

    def read(self) -> list:
        """Read data from csv file."""
        all_data = []
        with open(self.filepath, newline='') as csvfile:
            dataset = csv.reader(csvfile, delimiter=',', quotechar='|')
            next(dataset, None)  # skip the headers
            skipped_actions = 0
            for rows in dataset:
                if float(rows[1]) > 0 and (float(rows[1]) * float(rows[2]) / 100) > 0:
                    action = rows[0]
                    # Unfloat costs and profits as matrix will require integers
                    cost = int(round(float(rows[1]), 2) * 100)
                    profit = int(round(float(rows[2]), 2) * 100)
                    actual_profit = int(round(float(rows[1]) * (float(rows[2]) / 100), 2) * 100)

                    all_data.append(
                        (
                            action,
                            cost,
                            profit,
                            actual_profit
                        ),
                    )
                else:
                    skipped_actions += 1

        print(f'{skipped_actions} actions were skipped (action price or actual profit were negative).')
        return list(reversed(sorted(all_data, key=lambda x: x[1])))


class Wallet:
    """Create optimised wallet for actions list."""
    def __init__(self, dataset: dict = None):
        """Instantiate Wallet object."""
        self.dataset = CsvFile(dataset).read()
        print(f'Working with {len(self.dataset)} actions...')

    @timer
    def get_best_wallet(self) -> tuple[float, tuple, float]:
        """
        Generate matrix to get best items in wallet.

        :return: cost as float, wallet as tuple, profit as float
        """
        actions = self.dataset
        # As prices are * 100 to unfloat them, adapt max cost
        capacity = MAX_COST * 100

        # Generate matrix
        matrix = [[0 for x in range(capacity + 1)] for x in range(len(actions) + 1)]

        # Populate matrix
        for row in range(1, len(actions) + 1):
            for col in range(1, capacity + 1):
                if actions[row - 1][1] <= col:
                    matrix[row][col] = max(actions[row - 1][3] + matrix[row - 1][col - actions[row - 1][1]],
                                           matrix[row - 1][col])
                else:
                    matrix[row][col] = matrix[row - 1][col]

        # Retrieve best actions based on sum
        current_capacity = capacity
        current_row = len(actions)
        actions_selection = []

        while current_capacity >= 0 and current_row > 0:
            e = actions[current_row - 1]
            if matrix[current_row][current_capacity] == matrix[current_row - 1][current_capacity - e[1]] + e[3]:
                actions_selection.append(e)
                current_capacity -= e[1]
            current_row -= 1

        # Get cost and profit actions list based on best wallet
        cost = 0
        profit = 0
        wallet = ()

        for action in actions_selection:
            cost += action[1]
            profit += action[3]
            wallet += (action[0],)

        # Return cost (refloated), wallet, profit (refloated)
        return float(cost / 100), wallet, float(profit / 100)


def init_argparse() -> argparse.ArgumentParser:
    """Parse arguments passed in command line."""
    parser = argparse.ArgumentParser(
        usage="%(prog)s [OPTION] [FILE]...",
        description="Pass a full file path with which to make the best actions wallet."
    )
    parser.add_argument('file', nargs='*')
    return parser


if __name__ == '__main__':
    # Get dataset selection
    parser = init_argparse()
    args = parser.parse_args()
    # Check if quantity of args given is correct
    if not args.file or len(args.file) != 1:
        raise NotImplementedError("This programme requires 1 path to a file exactly to proceed.")

    filepath = args.file[0]
    print(f'Selected file: {filepath}')

    cost, wallet, profit = Wallet(filepath).get_best_wallet()

    # Display results in console
    print('----------- Results -----------')
    print(f'Total cost: {cost}')
    print(f'Total profit:{profit}')
    print('*** BEST WALLET: ***')
    for action in sorted(wallet):
        print(f'{action}')
