from constants import MAX_COST
from utils import CsvFile


class Wallet:
    """ Create optimised wallet for actions list """

    def __init__(self):
        """ Instantiate Wallet object """
        self.dataset = CsvFile(tup=True).read()
        print(f'Working with {len(self.dataset)} actions...')

    def get_best_wallet(self):
        """
        Generate matrix to get best items in wallet
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

        # Retrieve beset actions based on sum
        current_capacity = capacity
        current_row = len(actions)
        actions_selection = []

        while current_capacity >= 0 and current_row >= 0:
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
