from enum import Enum
from types import DynamicClassAttribute

WELCOME = 'Best wallet finder programme'
MAIN_MENU = '''[bold blue]---------- SELECT PROGRAMME TYPE -----------[/]
0 - Exit
---------------------
1 - Bruteforce
2 - Optimised'''
FILE_MENU = '''
[bold blue]------------- SELECT A DATASET -------------[/]
0 - Exit
---------------------'''
EXIT = "[bold green]END PROGRAMME"

MAX_COST = 500

DEFAULT_MSG = 'Please make a selection: \n'


class Files(Enum):
    """ Class to store files"""
    DATASET1 = (1, 'dataset0_Python+P7.csv', '20 actions dataset')
    DATASET2 = (2, 'dataset0_Python+P7_extended.csv', '25 actions dataset')
    DATASET3 = (3, 'dataset1_Python+P7.csv', '1001 actions dataset - not recommended with bruteforce')
    DATASET4 = (4, 'dataset2_Python+P7.csv', '1000 actions dataset - not recommended with bruteforce')

    @DynamicClassAttribute
    def value(self):
        """The value of the Enum member."""
        return self._value_[0]

    @DynamicClassAttribute
    def file(self):
        """The label of the Enum member."""
        return self._value_[1]

    @DynamicClassAttribute
    def info(self):
        """The label of the Enum member."""
        return self._value_[2]
