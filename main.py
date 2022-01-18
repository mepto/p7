from datetime import timedelta
from timeit import default_timer as timer

from bruteforce import BruteForce
from optimized import Wallet
# from optimized import Optimised
from utils import write_results

if __name__ == '__main__':
    print('Optimized started...')
    opt_start = timer()
    cost, wallet, profit = Wallet().get_max_profit()
    write_results(cost, wallet, profit)
    opt_end = timer()
    print(f"Time spent: {timedelta(seconds=opt_end - opt_start)}")
    print('-------------------------')
    print('BruteForce started...')
    brute_start = timer()
    cost, wallet, profit = BruteForce().best_item()
    write_results(cost, wallet, profit)
    brute_end = timer()
    print(f"Time spent: {timedelta(seconds=brute_end - brute_start)}")
