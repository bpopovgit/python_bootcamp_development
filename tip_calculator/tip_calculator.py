print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))

tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
allowed_tips = [10, 12, 15]

while tip not in allowed_tips:
    print("Please try again.")
    tip = input("What percentage tip would you like to give? 10, 12, or 15?")

tip_as_percent = tip / 100

people = int(input("How many people to split the bill? "))

calculated_bill_per_person = (bill + bill * tip_as_percent) / people

result = f"Each person should pay: ${calculated_bill_per_person:.2f}"
print(result)

