from datetime import timedelta
from timeit import default_timer as timer

from bruteforce import BruteForce

if __name__ == '__main__':
    print('BruteForce started...')
    start = timer()
    data = BruteForce()
    maxed = data.best_item()
    end = timer()
    print(f"Time spent: {timedelta(seconds=end - start)}")
