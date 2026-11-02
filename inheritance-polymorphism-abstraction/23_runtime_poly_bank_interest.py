class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def calculate_interest(self):
        pass

class SavingsAccount(BankAccount):
    def calculate_interest(self):
        return self.balance * 0.04

class CurrentAccount(BankAccount):
    def calculate_interest(self):
        return 0.0

class FixedDepositAccount(BankAccount):
    def calculate_interest(self):
        return self.balance * 0.075

accounts = [SavingsAccount(50000), CurrentAccount(100000), FixedDepositAccount(200000)]
for acc in accounts:
    print(f'{acc.__class__.__name__} Interest on {acc.balance}: {acc.calculate_interest()}')
