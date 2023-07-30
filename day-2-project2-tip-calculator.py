#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?\n $ "))

tip = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
tip_percentage = bill*(tip/100)
total_bill_with_tip = bill + tip_percentage

people = int(input("How many people to split the bills?\n"))
final_amount = total_bill_with_tip/people
#Format to 2 decimals using f-string ":.2f"
print(f"Each person should pay: ${final_amount:.2f}") 