# Write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

print(names)

bill_payer_index = random.randint(0, len(names) - 1 )

bill_payer_name = names[bill_payer_index]

print(bill_payer_name + " is going to buy the meal today!")