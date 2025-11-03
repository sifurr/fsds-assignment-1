account_balance = input("Enter your account balance: ")
balance = float(account_balance)
withdrawal_amount = input("Enter withdrawal amount: ")
withdrawal = float(withdrawal_amount)

if withdrawal > balance:
    print("Insufficient Balance")
elif withdrawal <= balance:
    print("Transaction Successful")