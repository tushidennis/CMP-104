class Account:
    def __init__(self):
         self.name = ""
         self.account_number = 555567778
         self.account_balance =10000
         
    def deposite(self, amount):
         self.account_balance = self.account_balance + amount
         print(self.account_balance)
         
    def withdraw(self, amount):
        self.account_balance = self.account_balance-amount
        print(self.account_balance)