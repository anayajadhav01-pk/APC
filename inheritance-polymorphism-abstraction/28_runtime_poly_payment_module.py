class Payment:
    def make_payment(self, amount):
        pass

class UPIPayment(Payment):
    def make_payment(self, amount):
        print(f'Payment of Rs.{amount} processed instantly via UPI.')

class CardPayment(Payment):
    def make_payment(self, amount):
        print(f'Payment of Rs.{amount} processed securely via Credit/Debit Card.')

class WalletPayment(Payment):
    def make_payment(self, amount):
        print(f'Payment of Rs.{amount} debited from Digital Wallet balance.')

def process_checkout(payment_method, amount):
    payment_method.make_payment(amount)

methods = [UPIPayment(), CardPayment(), WalletPayment()]
for m in methods:
    process_checkout(m, 1499.00)
