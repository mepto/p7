from bruteforce import BruteForce
from constants import DEFAULT_MSG, Files
from menu import Menu
from optimized import Wallet

if __name__ == '__main__':
    # Get algorithm selection
    menu = Menu()
    algo_type = menu.get_user_choice(DEFAULT_MSG, [*range(0, 3)])
    if algo_type == 0:
        menu.exit()

    # Get dataset selection
    menu.file_menu()
    file = menu.get_user_choice(DEFAULT_MSG, [*range(0, len(Files) + 1)])
    if file == 0:
        menu.exit()

    for item in Files:
        if item.value == file:
            file = item.file

    # Launch selected algorithm with selected file
    if algo_type == 1:
        cost, wallet, profit = BruteForce(dataset=file).get_best_wallet()
    elif algo_type == 2:
        cost, wallet, profit = Wallet(dataset=file).get_best_wallet()

    # Display results in console
    menu.write_results(cost, wallet, profit)

    # Leave programme
    menu.exit()
