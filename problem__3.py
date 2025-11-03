user_input = input("Enter your marks (0 - 100): ")
marks = float(user_input)

if marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B")
elif marks >= 60:
    print("c")
else:
    print("Fail")
