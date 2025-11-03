user_input = input("Enter your bill amount: ")
bill = float(user_input)

if bill > 1000:
    discount = bill * 0.10
    final_amount = bill - discount
    print(final_amount)
else:
    print("no discount")