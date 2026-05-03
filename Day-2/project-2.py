print("Welcome to the tip Calculator!")
total_bill = float(input("What was the total bill?: "))
percentage = int(input("What percentage are your tipping (10, 12, 15): "))
people = int(input("How many people to split the bill with?: "))

percentage = percentage / 100
final_bill = (total_bill + (total_bill * percentage)) / people

print(f"Per person should pay ${round(final_bill, 2)}")
