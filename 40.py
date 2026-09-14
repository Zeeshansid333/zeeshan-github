balance = float(input("Enter account balance: "))
amount = float(input("Enter withdrawal amount: "))

minimum_balance = 500

if amount <= 0:
    print("Invalid withdrawal amount")
elif amount % 100 != 0:
    print("Amount must be a multiple of 100")
elif amount + minimum_balance > balance:
    print("Withdrawal rejected")
    print("Insufficient balance or minimum balance rule violated")
else:
    balance -= amount
    print("Withdrawal approved")
    print("Remaining balance:", balance)
