class ATM:
    def __init__(self, account_number, holder_name, balance=0.0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def check_balance(self):
        print('Current Balance:', self.balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print('Deposited:', amount)
        else:
            print('Invalid amount')

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print('Withdrawn:', amount)
        else:
            print('Insufficient balance or invalid amount')

    def display_details(self):
        print('Account Number:', self.account_number)
        print('Holder Name:', self.holder_name)
        print('Balance:', self.balance)

atm = ATM('SB-123456', 'Vijay Patil', 5000.0)

while True:
    print('\n1. Check Balance')
    print('2. Deposit')
    print('3. Withdraw')
    print('4. Display Details')
    print('5. Exit')
    choice = input('Enter choice (1-5): ')

    if choice == '1':
        atm.check_balance()
    elif choice == '2':
        amt = float(input('Enter deposit amount: '))
        atm.deposit(amt)
    elif choice == '3':
        amt = float(input('Enter withdrawal amount: '))
        atm.withdraw(amt)
    elif choice == '4':
        atm.display_details()
    elif choice == '5':
        print('Exiting ATM')
        break
    else:
        print('Invalid choice')
