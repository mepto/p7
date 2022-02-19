import itertools

from constants import MAX_COST
from utils import CsvFile, timer


class BruteForce:
    """ Generate investment wallets with brute force """

    def __init__(self, dataset=None):
        self.dataset = CsvFile(dataset=dataset).read()
        self.actions = self.get_actions()
        print(f'Working with {len(self.actions)} actions...')
        self.combinations = self.get_combinations()

    def get_actions(self) -> list:
        """ Gets all action names from dataset """
        return list(self.dataset.keys())

    def get_combinations(self) -> list:
        """ Generate all actions combinations from csv file data """
        combs = []
        for i in range(1, len(self.actions) + 1):
            combs += list([itertools.combinations(self.actions, i)])
        return combs

    def get_total_cost(self, combination) -> float:
        """ Get total cost for one combination of actions """
        cost = 0
        for item in combination:
            cost += self.dataset[item]['price']
        return cost

    def get_profit(self, combination) -> float:
        """ Get profit for one combination of actions """
        profit = 0
        for item in combination:
            profit += self.dataset[item]['actual_profit']
        return profit

    def get_maxed_combinations(self) -> dict:
        """ Get the list of combinations below MAX_TOTAL with price and profit """
        best = []
        profit = 0
        for combination_list in self.combinations:
            for combination in combination_list:
                total_cost = self.get_total_cost(combination)
                if total_cost < MAX_COST:
                    current_profit = self.get_profit(combination)
                    if current_profit > profit:
                        best = {
                            'wallet': combination,
                            'cost': total_cost,
                            'profit': current_profit
                        }
                        profit = current_profit
        return best

    @timer
    def get_best_wallet(self):
        """ Prints best return on investment combination of actions """
        best = self.get_maxed_combinations()
        return best['cost'], best['wallet'], round(best['profit'], 2)
