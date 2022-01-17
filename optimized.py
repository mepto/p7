from utils import CsvFile

MAX_COST = 500


class Wallet:
    def __init__(self):
        self.dataset = CsvFile(with_ratio=True).read()
        print(f'Working with {len(self.dataset)} actions...')

    def get_max_profit(self):
        wallet = []
        profit_count = 0
        max_wallet_cost = MAX_COST
        for action in self.dataset:
            action_price = float(self.dataset[action]['price'])
            if max_wallet_cost - action_price >= 0:
                # lower wallet cost
                max_wallet_cost -= action_price
                # Increase max profit
                profit_count += (action_price * (float(self.dataset[action]['profit']) / 100))

                # Add action to wallet
                wallet.append(action)

        return MAX_COST - max_wallet_cost, wallet, round(profit_count, 2)
