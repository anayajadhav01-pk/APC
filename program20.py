file = open("transactions.txt", "r")

total_deposit = 0
total_withdrawal = 0
largest = 0

for line in file:
    type, amount = line.strip().split(",")

    amount = float(amount)

    if type == "deposit":
        total_deposit += amount
    elif type == "withdrawal":
        total_withdrawal += amount

    if amount > largest:
        largest = amount

file.close()

balance = total_deposit - total_withdrawal

print("Total Deposits:", total_deposit)
print("Total Withdrawals:", total_withdrawal)
print("Final Balance:", balance)
print("Largest Transaction:", largest)