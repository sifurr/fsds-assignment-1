user_input = input("Enter consumed Unit: ")
consumed_unit = float(user_input)

total_bill = 0

if consumed_unit <= 100:
    total_bill = consumed_unit * 5

if consumed_unit > 100 and consumed_unit <= 200:
    first_100_unit = 100 * 5
    total_bill = (consumed_unit - 100) * 7 + first_100_unit

if consumed_unit > 200:
    first_100_unit = 100 * 5
    from_101_to_200 = 100 * 7
    total_bill = (consumed_unit - 200) * 10 + first_100_unit + from_101_to_200

print(f"Total payable amount: {total_bill:.2f} BDT")
