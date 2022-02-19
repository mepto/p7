import sys

from constants import EXIT, FILE_MENU, MAIN_MENU, WELCOME, Files


class Menu:
    """ Display messages to the user in the console """

    def __init__(self):
        self.timer = ''
        self.welcome()
        self.main_menu()

    @staticmethod
    def welcome():
        print(WELCOME)

    @staticmethod
    def main_menu():
        print(MAIN_MENU)

    @staticmethod
    def file_menu():
        print(FILE_MENU)
        for item in Files:
            print(f'{item.value}: {item.name} - {item.file} ({item.info})')

    @staticmethod
    def exit():
        print(EXIT)
        sys.exit()

    @staticmethod
    def get_user_choice(message: str, choice_list: list) -> int:
        """
        Loops until user enters proper choice
        :return: user choice
        """
        user_choice = input(message)
        while not user_choice or not user_choice.isdigit() or int(user_choice) not in choice_list:
            reason = None
            if len(user_choice) == 0:
                reason = 'Empty entry.'
            elif not user_choice.isdigit():
                reason = f'"{user_choice}" is not a number'
            elif int(user_choice) not in choice_list:
                reason = f'Entry "{user_choice}" is not in available choices.'

            user_choice = input(f'{reason}\n{message}')

        return int(user_choice)

    @staticmethod
    def get_user_input(message):
        return input(f'{message}: ')

    @staticmethod
    def write_results(cost, wallet, profit):
        """ Write information to console """
        print('********************')
        print(f"Total cost: {cost}")
        print("*** BEST WALLET: ***")
        print(*wallet, sep="\n")
        print(f"Total profit: {profit}")
        print('********************')
