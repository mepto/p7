import itertools
from utils import CsvFile


# Chaque action ne peut être achetée qu'une seule fois.
#
# Nous ne pouvons pas acheter une fraction d'action.
#
# Nous pouvons dépenser au maximum 500 euros par client.


class BruteForce:
    """ Generate investment portfolio """

    def __init__(self, dataset=None):
        self.combinations = {}
        self.dataset = dataset

    def get_combinations(self):
        self.dataset = CsvFile().read()
        combinations = []
        for i in range(1, len(self.dataset)):
            combinations.append(i)
            range_combinations = [list(x) for x in itertools.combinations(self.dataset, i)]
            combinations.append(range_combinations)
        return combinations
