import itertools

from utils import CsvFile

MAX_TOTAL = 500


class BruteForce:
    """ Generate investment wallets with brute force """

    def __init__(self, dataset=None):
        self.combinations = self.get_combinations()
        self.dataset = dataset
        self.all_wallets = self.get_maxed_combinations()

    def get_combinations(self):
        """ Generate all actions combinations from csv file data """
        self.dataset = CsvFile().read()
        combinations = []
        for i in range(1, len(self.dataset)):
            combinations += [x for x in itertools.combinations(self.dataset, i)]
        return combinations

    @staticmethod
    def get_total_cost(combination):
        """ Get total cost for one combination of actions """
        cost = 0
        for item in combination:
            cost += item[1]
        return cost

    @staticmethod
    def get_profit(combination):
        """ Get profit for one combination of actions """
        profit = 0
        for item in combination:
            profit += item[1] * (item[2] / 100)
        return profit

    def get_maxed_combinations(self):
        """ Get the list of combinations below MAX_TOTAL with price and profit """
        best = []
        profit = 0
        for combination in self.combinations:
            total_cost = self.get_total_cost(combination)
            if total_cost < MAX_TOTAL:
                current_profit = self.get_profit(combination)
                if current_profit > profit:
                    best = {
                        'wallet': combination,
                        'cost': total_cost,
                        'profit': current_profit
                    }
                    profit = current_profit
        return best

    def best_item(self):
        """ Prints best return on investment combination of actions """
        print(self.get_maxed_combinations())
