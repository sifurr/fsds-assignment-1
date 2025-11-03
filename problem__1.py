user_input = input("Enter temperature in Celsius: ")
temperature = float(user_input)

if temperature > 25:
    print("It's hot outside!")
elif temperature >= 10:
    print("It's cool outside")
else:
    print("It's too cold!")
