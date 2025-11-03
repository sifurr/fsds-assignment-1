user_input = input("Enter your age: ")
age = int(user_input)

if age < 5:
    print("Free")
elif age <= 18:
    print("==50% Discount")
elif age >= 60:
    print("==30% Discount")
else: 
    print("Full Price")