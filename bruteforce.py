import argparse
import csv
from dataclasses import dataclass
from datetime import timedelta
import itertools
from pathlib import Path
import time

MAX_COST = 500


def timer(func):
    def inner(*args, **kwargs):
        start = time.time()
        f = func(*args, **kwargs)
        end = time.time()
        print(f'Programme duration time: {timedelta(seconds=end - start)}')
        return f
    return inner


@dataclass
class BestWallet:
    wallet: tuple
    cost: float
    profit: float


class Wallet:
    """Generate investment wallets with brute force."""
    def __init__(self, dataset=None):
        self.dataset = CsvFile(dataset).read()
        self.actions = self.get_actions()
        print(f'Working with {len(self.dataset)} actions...')
        self.combinations = self.get_combinations()

    def get_actions(self) -> list:
        """Get all action names from dataset."""
        return list(self.dataset.keys())

    def get_combinations(self) -> list:
        """Generate all actions combinations from csv file data."""
        combs = []
        for i in range(1, len(self.actions) + 1):
            combs.append(itertools.combinations(self.actions, i))
        return combs

    def get_total_cost(self, combination) -> float:
        """Get total cost for one combination of actions."""
        cost = 0
        for item in combination:
            cost += self.dataset[item]['price']
        return cost

    def get_profit(self, combination) -> float:
        """Get profit for one combination of actions."""
        profit = 0
        for item in combination:
            profit += self.dataset[item]['actual_profit']
        return profit

    def get_maxed_combinations(self) -> BestWallet:
        """Get the list of combinations below MAX_TOTAL with price and profit."""
        best = None
        profit = 0
        for combination_list in self.combinations:
            for combination in combination_list:
                total_cost = self.get_total_cost(combination)
                if total_cost < MAX_COST:
                    current_profit = self.get_profit(combination)
                    # Replace best if more interesting than the one already stored
                    if current_profit > profit:
                        best = BestWallet(wallet=combination,
                                          cost=round(total_cost, 2),
                                          profit=round(current_profit, 2)
                                          )
                        profit = current_profit
        return best

    @timer
    def get_best_wallet(self) -> tuple[float, tuple, float]:
        """Print best return on investment combination of actions."""
        best = self.get_maxed_combinations()
        return best.cost, best.wallet, best.profit


class CsvFile:
    """
    Read from csv file and return data.

    :return: dict
    """
    def __init__(self, dataset):
        self.filepath = Path(dataset)
        # Check if path provided is relevant
        if not self.filepath.is_file():
            raise FileExistsError('The path provided is not to a file or the file does not exist.')

    def read(self) -> dict:
        """Read data from csv file."""
        all_data = {}

        with open(self.filepath, newline='') as csvfile:
            dataset = csv.reader(csvfile, delimiter=',', quotechar='|')
            next(dataset, None)  # skip the headers
            skipped_actions = 0
            # Populate dict
            for rows in dataset:
                if float(rows[1]) > 0 and (float(rows[1]) * float(rows[2]) / 100) > 0:
                    action = rows[0]
                    cost = int(round(float(rows[1]), 2) * 100)
                    profit = int(round(float(rows[2]), 2) * 100)
                    actual_profit = int(round(float(rows[1]) * (float(rows[2]) / 100), 2) * 100)

                    all_data[action] = {
                        'price': cost / 100,
                        'profit': profit / 100,
                        'actual_profit': actual_profit / 100
                    }
                else:
                    skipped_actions += 1

        print(f'{skipped_actions} actions were skipped (action price or actual profit were negative).')
        return dict(reversed(sorted(all_data.items(), key=lambda x: x[1]['price'])))


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
