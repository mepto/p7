import sys

import rich.prompt
from rich.console import Console

from constants import EXIT, FILE_MENU, MAIN_MENU, WELCOME, Files

console = Console()


class Menu:
    """ Display messages to the user in the console """

    def __init__(self):
        self.timer = ''
        self.welcome()
        self.main_menu()

    @staticmethod
    def welcome():
        console.rule('[bold blue]', characters='*')
        console.rule(f'[bold blue]{WELCOME}')
        console.rule('[bold blue]', characters='*')

    @staticmethod
    def main_menu():
        console.print(MAIN_MENU, justify='center')

    @staticmethod
    def file_menu():
        console.print(FILE_MENU, justify='center')
        for item in Files:
            console.print(f'{item.value}: {item.name} - {item.file} ([white]{item.info})', justify='center')

    @staticmethod
    def actions_nb(nb):
        console.print(f'[bold blue]Working with[/] [yellow]{nb}[/] [bold blue]actions...[/]')

    @staticmethod
    def skipped_entries(nb):
        console.print(f'{nb} actions were skipped (action price or actual profit were negative)')

    @staticmethod
    def exit():
        console.rule(EXIT)
        sys.exit()

    @staticmethod
    def get_user_choice(message: str, choice_list: list) -> int:
        """
        Loops until user enters proper choice
        :return: user choice
        """
        choices = [str(x) for x in choice_list]
        return rich.prompt.IntPrompt.ask(f'[bold magenta]{message}', choices=choices)

    @staticmethod
    def write_results(cost, wallet, profit):
        """ Write information to console """
        console.rule('[bold blue]Results')
        console.print(f"[u bold blue]Total cost:[/] [yellow]{cost}")
        console.print(f"[u bold blue]Total profit:[/] [yellow]{profit}")
        console.print('[u bold blue]*** BEST WALLET: ***')
        for action in sorted(wallet):
            console.print(f'[yellow]{action}')

    @staticmethod
    def timer(time):
        console.print(f'[bold blue]Processing time:[/] [yellow]{time}[/]')
