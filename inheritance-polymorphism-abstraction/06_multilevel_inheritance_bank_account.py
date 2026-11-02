class BankAccount:
    def __init__(self, acc_num, balance):
        self.acc_num = acc_num
        self.balance = balance

    def display_account(self):
        print('Account Number:', self.acc_num)
        print('Balance:', self.balance)

class SavingsAccount(BankAccount):
    def __init__(self, acc_num, balance, interest_rate):
        super().__init__(acc_num, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return (self.balance * self.interest_rate) / 100

class PremiumSavingsAccount(SavingsAccount):
    def __init__(self, acc_num, balance, interest_rate, cashback_percent):
        super().__init__(acc_num, balance, interest_rate)
        self.cashback_percent = cashback_percent

    def display_all(self):
        self.display_account()
        print('Interest Rate:', self.interest_rate, '%')
        print('Annual Interest:', self.calculate_interest())
        print('Cashback Benefit:', self.cashback_percent, '%')

psa = PremiumSavingsAccount('ACC-9901', 150000, 4.5, 2.0)
psa.display_all()
