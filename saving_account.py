from account import Account
class savings_accout(Account):
    def __init__(self):
        Account.__init__(self)
        self.transfer_limit = 5000

    def withdraw(self, amount):
        if amount < self.transfer_limit:
            self.account_balance = self.account_balance - amount
            print(self.account_balance)
        else:
            print("you have passed your limit")