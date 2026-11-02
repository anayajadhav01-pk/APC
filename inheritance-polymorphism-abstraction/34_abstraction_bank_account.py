from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, acc_no, balance=0.0):
        self.acc_no = acc_no
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

class SavingsAccount(BankAccount):
    def deposit(self, amount):
        self.balance += amount
        print(f'Savings {self.acc_no}: Deposited {amount}. Balance: {self.balance}')

    def withdraw(self, amount):
        if amount <= self.balance - 500:
            self.balance -= amount
            print(f'Savings {self.acc_no}: Withdrawn {amount}. Balance: {self.balance}')
        else:
            print(f'Savings {self.acc_no}: Minimum balance violation or insufficient funds.')

class CurrentAccount(BankAccount):
    def deposit(self, amount):
        self.balance += amount
        print(f'Current {self.acc_no}: Deposited {amount}. Balance: {self.balance}')

    def withdraw(self, amount):
        if amount <= self.balance + 10000:
            self.balance -= amount
            print(f'Current {self.acc_no}: Withdrawn {amount} (Overdraft allowed). Balance: {self.balance}')
        else:
            print(f'Current {self.acc_no}: Overdraft limit exceeded.')

sa = SavingsAccount('SB-100', 5000)
ca = CurrentAccount('CA-200', 3000)

sa.deposit(1500)
sa.withdraw(5500)
ca.withdraw(8000)
